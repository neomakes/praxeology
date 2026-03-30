"""
Praxeology MCP — AgentRunner.

Per-crew autonomous daemon that loops:
    what_now(crew_id) → LLM call (Ollama/Claude) → tool execution → backprop()

Supports two backends:
    - Ollama: POST /api/chat (local, cost=0)
    - Claude: POST /v1/messages (cloud, Anthropic API)

Usage:
    # As daemon (via DaemonManager):
    praxeology start --crew zoro --model qwen3:14b

    # Direct (for testing):
    python -m praxeology_mcp.agent_runner --crew zoro --model qwen3:14b
"""

from __future__ import annotations

import json
import logging
import os
import signal
import threading
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from praxeology_mcp.db import get_db, init_db, log_metric

logger = logging.getLogger("praxeology.agent_runner")

_DEFAULT_DB = os.path.expanduser("~/.claude/praxeology/praxeology.db")

# ---------------------------------------------------------------------------
# Tool definitions for LLM (JSON Schema format)
# ---------------------------------------------------------------------------

TOOL_DEFINITIONS = [
    {
        "name": "logical_search",
        "description": "Full-text search across standards (STR/DOC/PRC/PLY).",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
                "tier": {"type": "string", "description": "Filter by tier: strategy/doctrine/procedure/playbook"},
                "department": {"type": "string", "description": "Filter by department"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "logical_read",
        "description": "Read a specific standard by code (e.g. DOC-201).",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {"type": "string", "description": "Standard code, e.g. DOC-201"},
            },
            "required": ["code"],
        },
    },
    {
        "name": "logical_create",
        "description": "Create a new standard entry.",
        "parameters": {
            "type": "object",
            "properties": {
                "tier": {"type": "string", "enum": ["strategy", "doctrine", "procedure", "playbook"]},
                "department": {"type": "string"},
                "code": {"type": "string"},
                "title": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["tier", "department", "code", "title"],
        },
    },
    {
        "name": "tactical_search",
        "description": "Search objectives and work items.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "tier": {"type": "string"},
                "status": {"type": "string"},
                "assignee": {"type": "string"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "tactical_read",
        "description": "Read a specific objective by ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "objective_id": {"type": "integer"},
            },
            "required": ["objective_id"],
        },
    },
    {
        "name": "tactical_create",
        "description": "Create a new objective or work item.",
        "parameters": {
            "type": "object",
            "properties": {
                "tier": {"type": "string", "enum": ["goal", "program", "campaign", "plan", "work"]},
                "title": {"type": "string"},
                "description": {"type": "string"},
                "priority": {"type": "string", "enum": ["high", "mid", "low"]},
                "assignee": {"type": "string"},
                "parent_id": {"type": "integer"},
            },
            "required": ["tier", "title"],
        },
    },
    {
        "name": "tactical_feedback",
        "description": "Update objective status.",
        "parameters": {
            "type": "object",
            "properties": {
                "objective_id": {"type": "integer"},
                "status": {"type": "string", "enum": ["pending", "in_progress", "done", "blocked"]},
                "notes": {"type": "string"},
            },
            "required": ["objective_id", "status"],
        },
    },
    {
        "name": "contextual_search",
        "description": "Search across spaces, channels, threads, crew, sessions.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "tier": {"type": "string"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "backprop",
        "description": "Record execution result and propagate feedback across 3 axes.",
        "parameters": {
            "type": "object",
            "properties": {
                "case_id": {"type": "integer"},
                "result": {"type": "string"},
                "surprise": {"type": "number", "description": "0.0-1.0 surprise score"},
            },
            "required": ["case_id", "result"],
        },
    },
]

_ALLOWED_TOOL_NAMES = frozenset(t["name"] for t in TOOL_DEFINITIONS)


def _tools_for_ollama() -> list[dict]:
    """Format tools for Ollama /api/chat."""
    return [
        {"type": "function", "function": {"name": t["name"], "description": t["description"], "parameters": t["parameters"]}}
        for t in TOOL_DEFINITIONS
    ]


def _tools_for_claude() -> list[dict]:
    """Format tools for Claude /v1/messages."""
    return [
        {"name": t["name"], "description": t["description"], "input_schema": t["parameters"]}
        for t in TOOL_DEFINITIONS
    ]


# ---------------------------------------------------------------------------
# Tool executor — runs tool calls against the DB
# ---------------------------------------------------------------------------

class ToolExecutor:
    """Executes tool calls directly against the SQLite DB."""

    def __init__(self, db_path: str):
        self.db_path = db_path

    def execute(self, tool_name: str, args: dict) -> str:
        if tool_name not in _ALLOWED_TOOL_NAMES:
            return json.dumps({"error": f"Tool '{tool_name}' not in allowlist"})
        conn = get_db(self.db_path)
        try:
            if tool_name == "logical_search":
                return self._logical_search(conn, args)
            elif tool_name == "logical_read":
                return self._logical_read(conn, args)
            elif tool_name == "logical_create":
                return self._logical_create(conn, args)
            elif tool_name == "tactical_search":
                return self._tactical_search(conn, args)
            elif tool_name == "tactical_read":
                return self._tactical_read(conn, args)
            elif tool_name == "tactical_create":
                return self._tactical_create(conn, args)
            elif tool_name == "tactical_feedback":
                return self._tactical_feedback(conn, args)
            elif tool_name == "contextual_search":
                return self._contextual_search(conn, args)
            elif tool_name == "backprop":
                return self._backprop(conn, args)
            else:
                return json.dumps({"error": f"Unknown tool: {tool_name}"})
        except Exception as exc:
            return json.dumps({"error": str(exc)})

    def _logical_search(self, conn, args) -> str:
        query = args["query"]
        rows = conn.execute(
            "SELECT id, tier, department, code, title FROM standards WHERE code LIKE ? OR title LIKE ? LIMIT 10",
            (f"%{query}%", f"%{query}%"),
        ).fetchall()
        return json.dumps([dict(r) for r in rows], ensure_ascii=False)

    def _logical_read(self, conn, args) -> str:
        row = conn.execute(
            "SELECT * FROM standards WHERE code = ?", (args["code"],)
        ).fetchone()
        return json.dumps(dict(row) if row else {"error": "not found"}, ensure_ascii=False)

    def _logical_create(self, conn, args) -> str:
        conn.execute(
            "INSERT INTO standards (tier, department, code, title, content) VALUES (?, ?, ?, ?, ?)",
            (args["tier"], args.get("department", ""), args["code"], args["title"], args.get("content", "")),
        )
        conn.commit()
        return json.dumps({"created": args["code"]})

    def _tactical_search(self, conn, args) -> str:
        query = args["query"]
        sql = "SELECT id, tier, title, status, priority, assignee FROM objectives WHERE title LIKE ?"
        params = [f"%{query}%"]
        if args.get("tier"):
            sql += " AND tier = ?"
            params.append(args["tier"])
        if args.get("status"):
            sql += " AND status = ?"
            params.append(args["status"])
        if args.get("assignee"):
            sql += " AND assignee = ?"
            params.append(args["assignee"])
        sql += " LIMIT 10"
        rows = conn.execute(sql, params).fetchall()
        return json.dumps([dict(r) for r in rows], ensure_ascii=False)

    def _tactical_read(self, conn, args) -> str:
        row = conn.execute(
            "SELECT * FROM objectives WHERE id = ?", (args["objective_id"],)
        ).fetchone()
        return json.dumps(dict(row) if row else {"error": "not found"}, ensure_ascii=False)

    def _tactical_create(self, conn, args) -> str:
        cur = conn.execute(
            "INSERT INTO objectives (tier, title, description, priority, assignee, parent_id) VALUES (?, ?, ?, ?, ?, ?)",
            (args["tier"], args["title"], args.get("description", ""),
             args.get("priority", "mid"), args.get("assignee"), args.get("parent_id")),
        )
        conn.commit()
        return json.dumps({"created": cur.lastrowid, "title": args["title"]})

    def _tactical_feedback(self, conn, args) -> str:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        conn.execute(
            "UPDATE objectives SET status = ?, updated_at = ? WHERE id = ?",
            (args["status"], now, args["objective_id"]),
        )
        conn.commit()
        return json.dumps({"updated": args["objective_id"], "status": args["status"]})

    def _contextual_search(self, conn, args) -> str:
        query = args["query"]
        sql = "SELECT id, tier, name, metadata FROM contexts WHERE name LIKE ?"
        params = [f"%{query}%"]
        if args.get("tier"):
            sql += " AND tier = ?"
            params.append(args["tier"])
        sql += " LIMIT 10"
        rows = conn.execute(sql, params).fetchall()
        return json.dumps([dict(r) for r in rows], ensure_ascii=False)

    def _backprop(self, conn, args) -> str:
        case_id = args["case_id"]
        result = args["result"]
        surprise = max(0.0, min(1.0, args.get("surprise", 0.0)))

        case_row = conn.execute(
            "SELECT id, standard_id, objective_id, crew_id FROM cases WHERE id = ?",
            (case_id,),
        ).fetchone()
        if case_row is None:
            return json.dumps({"error": f"No case with id={case_id}"})

        objective_id = case_row["objective_id"]
        crew_id = case_row["crew_id"]

        conn.execute("UPDATE cases SET result = ?, surprise = ? WHERE id = ?", (result, surprise, case_id))
        conn.commit()

        updates = {"case_updated": True}

        if surprise > 0.5:
            cur = conn.execute(
                "INSERT INTO gaps (case_id, description, frequency, status) VALUES (?, ?, 1, 'open')",
                (case_id, f"Auto-gap: surprise={surprise:.2f} — {result[:200]}"),
            )
            conn.commit()
            gap_id = cur.lastrowid
            updates["gap_created"] = gap_id

            if surprise > 0.8:
                cur2 = conn.execute(
                    "INSERT INTO proposals (gap_id, proposed_by, proposed_change, status) VALUES (?, ?, ?, 'pending')",
                    (gap_id, crew_id or "system", f"Review — high surprise ({surprise:.2f}) on case {case_id}"),
                )
                conn.commit()
                updates["proposal_created"] = cur2.lastrowid

        completion_words = {"done", "completed", "finished", "success"}
        if objective_id and completion_words & set(result.lower().split()):
            now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            conn.execute("UPDATE objectives SET status = 'done', updated_at = ? WHERE id = ?", (now, objective_id))
            conn.commit()
            updates["objective_done"] = objective_id

        return json.dumps(updates, ensure_ascii=False)


# ---------------------------------------------------------------------------
# LLM Client — Ollama and Claude backends
# ---------------------------------------------------------------------------

class LLMClient:
    """Unified LLM client for Ollama and Claude API."""

    def __init__(self, model: str, backend: str = "ollama",
                 base_url: str = None, api_key: str = None):
        self.model = model
        self.backend = backend
        self.base_url = base_url or self._default_url(backend)
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")

    @staticmethod
    def _default_url(backend: str) -> str:
        if backend == "ollama":
            return os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        return "https://api.anthropic.com"

    def chat(self, messages: list[dict], tools: list[dict] = None) -> dict:
        """Send chat request. Returns {"content": str, "tool_calls": [...]}."""
        if self.backend == "ollama":
            return self._chat_ollama(messages, tools)
        return self._chat_claude(messages, tools)

    def _chat_ollama(self, messages: list[dict], tools: list[dict] = None) -> dict:
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "stream": False,
        }
        if tools:
            payload["tools"] = tools

        data = json.dumps(payload).encode()
        req = urllib.request.Request(
            f"{self.base_url}/api/chat",
            data=data,
            headers={"Content-Type": "application/json"},
        )

        resp = urllib.request.urlopen(req, timeout=120)
        result = json.loads(resp.read().decode())
        msg = result.get("message", {})

        tool_calls = []
        for tc in msg.get("tool_calls", []):
            func = tc.get("function", {})
            tool_calls.append({
                "name": func.get("name", ""),
                "arguments": func.get("arguments", {}),
            })

        return {
            "content": msg.get("content", ""),
            "tool_calls": tool_calls,
        }

    def _chat_claude(self, messages: list[dict], tools: list[dict] = None) -> dict:
        payload: dict[str, Any] = {
            "model": self.model,
            "max_tokens": 4096,
            "messages": messages,
        }
        if tools:
            payload["tools"] = tools

        data = json.dumps(payload).encode()
        req = urllib.request.Request(
            f"{self.base_url}/v1/messages",
            data=data,
            headers={
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
            },
        )

        resp = urllib.request.urlopen(req, timeout=120)
        result = json.loads(resp.read().decode())

        content_text = ""
        tool_calls = []
        for block in result.get("content", []):
            if block["type"] == "text":
                content_text += block["text"]
            elif block["type"] == "tool_use":
                tool_calls.append({
                    "name": block["name"],
                    "arguments": block["input"],
                })

        return {
            "content": content_text,
            "tool_calls": tool_calls,
        }


# ---------------------------------------------------------------------------
# AgentRunner — the core autonomous loop
# ---------------------------------------------------------------------------

class AgentRunner:
    """Per-crew autonomous agent daemon.

    Loop:
        1. what_now(crew_id) → find pending work
        2. If work found → create case → call LLM with tools
        3. Execute tool calls → collect results
        4. backprop(case_id, result, surprise)
        5. Wait interval → repeat
    """

    def __init__(self, crew_id: str, model: str, db_path: str,
                 backend: str = "ollama", interval: int = 60,
                 base_url: str = None, api_key: str = None):
        self.crew_id = crew_id
        self.model = model
        self.db_path = db_path
        self.interval = interval
        self._running = False
        self._stop_event = threading.Event()

        self.llm = LLMClient(model, backend, base_url, api_key)
        self.executor = ToolExecutor(db_path)

    def start(self) -> None:
        """Start as daemon thread."""
        self._running = True
        thread = threading.Thread(target=self._loop, daemon=True)
        thread.start()

    def stop(self) -> None:
        self._running = False
        self._stop_event.set()

    def _loop(self) -> None:
        logger.info(f"AgentRunner started: crew={self.crew_id} model={self.model}")
        while self._running:
            try:
                self._tick()
            except Exception as exc:
                logger.error(f"AgentRunner tick error: {exc}")
                self._log_metric("agent_runner.error")
            self._stop_event.wait(timeout=self.interval)

    def _tick(self) -> None:
        """One iteration: find work → execute → report."""
        conn = get_db(self.db_path)

        # 1. what_now — find top pending work
        work = conn.execute(
            """
            SELECT id, title, description, priority, due_date
            FROM objectives
            WHERE tier = 'work' AND status IN ('pending', 'in_progress')
              AND assignee = ?
            ORDER BY
                CASE priority WHEN 'high' THEN 0 WHEN 'mid' THEN 1 ELSE 2 END,
                created_at ASC
            LIMIT 1
            """,
            (self.crew_id,),
        ).fetchone()

        if work is None:
            logger.debug(f"[{self.crew_id}] No pending work.")
            return

        work_dict = dict(work)
        logger.info(f"[{self.crew_id}] Working on: {work_dict['title']}")

        # Mark as in_progress
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        conn.execute(
            "UPDATE objectives SET status = 'in_progress', updated_at = ? WHERE id = ? AND status = 'pending'",
            (now, work_dict["id"]),
        )
        conn.commit()

        # 2. Create case for tracking
        cur = conn.execute(
            "INSERT INTO cases (objective_id, crew_id, task, action, created_at) VALUES (?, ?, ?, ?, ?)",
            (work_dict["id"], self.crew_id, work_dict["title"],
             f"AgentRunner auto-execution", now),
        )
        conn.commit()
        case_id = cur.lastrowid

        # 3. Get context — related standards, recent cases
        standards = conn.execute(
            "SELECT code, title FROM standards ORDER BY tier, code LIMIT 10"
        ).fetchall()
        standards_ctx = "\n".join(f"- {r['code']}: {r['title']}" for r in standards)

        gaps = conn.execute(
            "SELECT description FROM gaps WHERE status = 'open' ORDER BY frequency DESC LIMIT 3"
        ).fetchall()
        gaps_ctx = "\n".join(f"- {r['description']}" for r in gaps) if gaps else "None"

        # 4. Build prompt
        system_prompt = (
            f"You are {self.crew_id}, an autonomous agent governed by Praxeology.\n"
            f"Your current task: {work_dict['title']}\n"
            f"Description: {work_dict.get('description', 'N/A')}\n"
            f"Priority: {work_dict['priority']}\n\n"
            f"Available standards:\n{standards_ctx}\n\n"
            f"Open gaps:\n{gaps_ctx}\n\n"
            f"Use the provided tools to complete the task. "
            f"When done, use tactical_feedback to mark the objective as done. "
            f"Report your result clearly."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Execute task: {work_dict['title']}"},
        ]

        # 5. LLM call with tool loop (max 5 rounds)
        tools = _tools_for_ollama() if self.llm.backend == "ollama" else _tools_for_claude()
        final_content = ""

        for round_num in range(5):
            try:
                response = self.llm.chat(messages, tools)
            except (urllib.error.URLError, Exception) as exc:
                logger.error(f"[{self.crew_id}] LLM call failed: {exc}")
                self._log_metric("agent_runner.llm_error")
                break

            try:
                final_content = response.get("content", "")
                tool_calls = response.get("tool_calls", [])
            except (AttributeError, TypeError) as exc:
                logger.error(f"[{self.crew_id}] LLM response parse error: {exc}")
                self._log_metric("agent_runner.parse_error")
                break

            if not tool_calls:
                break

            # Execute each tool call
            for tc in tool_calls:
                tool_name = tc.get("name", "")
                tool_args = tc.get("arguments", {})
                if not isinstance(tool_args, dict):
                    try:
                        tool_args = json.loads(tool_args) if isinstance(tool_args, str) else {}
                    except (json.JSONDecodeError, TypeError):
                        tool_args = {}

                logger.info(f"[{self.crew_id}] Tool call: {tool_name}({json.dumps(tool_args, ensure_ascii=False)[:100]})")

                tool_result = self.executor.execute(tool_name, tool_args)
                self._log_metric(f"agent_runner.tool.{tool_name}")

                # Add tool result — format differs by backend
                if self.llm.backend == "claude":
                    # Claude API requires tool_use/tool_result content blocks
                    messages.append({
                        "role": "assistant",
                        "content": [
                            *([{"type": "text", "text": final_content}] if final_content else []),
                            {"type": "tool_use", "id": f"call_{round_num}_{tool_name}", "name": tool_name, "input": tool_args},
                        ],
                    })
                    messages.append({
                        "role": "user",
                        "content": [{"type": "tool_result", "tool_use_id": f"call_{round_num}_{tool_name}", "content": tool_result}],
                    })
                else:
                    # Ollama format
                    messages.append({"role": "assistant", "content": final_content, "tool_calls": [tc]})
                    messages.append({"role": "tool", "content": tool_result, "name": tool_name})

        # 6. Record result via backprop
        result_text = final_content[:500] if final_content else "Execution completed (no LLM response)"
        conn.execute(
            "UPDATE cases SET result = ?, action = ? WHERE id = ?",
            (result_text, f"AgentRunner {self.model} — {len(messages)} messages", case_id),
        )
        conn.commit()

        self._log_metric("agent_runner.tick_complete")
        logger.info(f"[{self.crew_id}] Tick complete. Result: {result_text[:100]}")

    def _log_metric(self, name: str) -> None:
        try:
            conn = get_db(self.db_path)
            log_metric(conn, name, "cross", tokens=0, latency=0)
        except Exception:
            pass


# ---------------------------------------------------------------------------
# Daemon entry point — called by DaemonManager
# ---------------------------------------------------------------------------

def run_agent(crew_id: str, model: str, db_path: str = None,
              backend: str = "ollama", interval: int = 60,
              base_url: str = None, api_key: str = None) -> None:
    """Entry point for daemon mode. Called by DaemonManager."""
    if db_path is None:
        db_path = os.environ.get("PRAXEOLOGY_DB", _DEFAULT_DB)
    init_db(db_path)

    logging.basicConfig(
        level=logging.INFO,
        format=f"%(asctime)s [{crew_id}] %(levelname)s %(message)s",
    )

    runner = AgentRunner(
        crew_id=crew_id,
        model=model,
        db_path=db_path,
        backend=backend,
        interval=interval,
        base_url=base_url,
        api_key=api_key,
    )

    # Handle SIGTERM for clean shutdown
    def handle_sigterm(signum, frame):
        runner.stop()
    signal.signal(signal.SIGTERM, handle_sigterm)

    runner._running = True
    runner._loop()


# ---------------------------------------------------------------------------
# CLI entry point — for direct testing
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Praxeology AgentRunner")
    parser.add_argument("--crew", required=True, help="Crew ID")
    parser.add_argument("--model", required=True, help="LLM model name")
    parser.add_argument("--backend", default="ollama", choices=["ollama", "claude"])
    parser.add_argument("--interval", type=int, default=60, help="Seconds between ticks")
    parser.add_argument("--db", default=None, help="DB path")
    parser.add_argument("--base-url", default=None, help="LLM API base URL")
    args = parser.parse_args()

    run_agent(
        crew_id=args.crew,
        model=args.model,
        db_path=args.db,
        backend=args.backend,
        interval=args.interval,
        base_url=args.base_url,
    )
