"""
Praxeology MCP — Logical axis tools.

Strategy → Doctrine → Procedure → Playbook → Case

Tools:
    logical_search    — FTS5 search on standards_fts + cases_fts
    logical_read      — Read a standard or case by ID
    logical_create    — Create standard, case, gap, or proposal
    logical_escalate  — Mark case/gap for escalation
    logical_feedback  — Update case with result and surprise score
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from typing import Any

from praxeology_mcp.db import get_db, log_metric

# ---------------------------------------------------------------------------
# DB path resolution
# ---------------------------------------------------------------------------

_DEFAULT_DB = os.path.expanduser("~/.claude/praxeology/praxeology.db")


def _db_path() -> str:
    return os.environ.get("PRAXEOLOGY_DB", _DEFAULT_DB)


def _utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _row_to_dict(row) -> dict:
    return dict(row) if row is not None else {}


# ---------------------------------------------------------------------------
# Tool registration helper — called by server.py
# ---------------------------------------------------------------------------

def register(mcp) -> None:
    """Register all logical axis tools onto the given FastMCP instance."""

    @mcp.tool()
    def logical_search(query: str, tier: str = None) -> str:
        """FTS5 full-text search across standards and cases.

        Args:
            query: Search terms (FTS5 syntax supported).
            tier: Optional tier filter for standards
                  ('strategy','doctrine','procedure','playbook').

        Returns:
            JSON array of matching records with source table indicated.
        """
        t0 = time.monotonic_ns()
        conn = get_db(_db_path())
        results: list[dict[str, Any]] = []

        try:
            # Search standards_fts
            if tier:
                rows = conn.execute(
                    """
                    SELECT s.id, s.tier, s.department, s.code, s.title,
                           s.content, s.version, s.created_at, s.updated_at,
                           'standards' AS source
                    FROM standards_fts f
                    JOIN standards s ON s.id = f.rowid
                    WHERE standards_fts MATCH ?
                      AND s.tier = ?
                    ORDER BY rank
                    LIMIT 50
                    """,
                    (query, tier),
                ).fetchall()
            else:
                rows = conn.execute(
                    """
                    SELECT s.id, s.tier, s.department, s.code, s.title,
                           s.content, s.version, s.created_at, s.updated_at,
                           'standards' AS source
                    FROM standards_fts f
                    JOIN standards s ON s.id = f.rowid
                    WHERE standards_fts MATCH ?
                    ORDER BY rank
                    LIMIT 50
                    """,
                    (query,),
                ).fetchall()
            results.extend(_row_to_dict(r) for r in rows)

            # Search cases_fts (no tier filter applies)
            rows = conn.execute(
                """
                SELECT c.id, c.standard_id, c.crew_id, c.session_id,
                       c.task, c.action, c.result, c.surprise, c.created_at,
                       'cases' AS source
                FROM cases_fts f
                JOIN cases c ON c.id = f.rowid
                WHERE cases_fts MATCH ?
                ORDER BY rank
                LIMIT 50
                """,
                (query,),
            ).fetchall()
            results.extend(_row_to_dict(r) for r in rows)

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "logical_search", "logical", 0, latency)
            conn.close()
            return json.dumps(results, ensure_ascii=False)

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def logical_read(id: int, table: str = "standards") -> str:
        """Read a specific standard or case by primary key.

        Args:
            id: Primary key of the record.
            table: One of 'standards', 'cases', 'gaps', 'proposals'.

        Returns:
            JSON object of the record, or error if not found.
        """
        t0 = time.monotonic_ns()
        allowed = {"standards", "cases", "gaps", "proposals"}
        if table not in allowed:
            return json.dumps({"error": f"table must be one of {sorted(allowed)}"})

        conn = get_db(_db_path())
        try:
            row = conn.execute(
                f"SELECT * FROM {table} WHERE id = ?", (id,)
            ).fetchone()
            if row is None:
                return json.dumps({"error": f"No record in {table} with id={id}"})

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "logical_read", "logical", 0, latency)
            conn.close()
            return json.dumps(_row_to_dict(row), ensure_ascii=False)

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def logical_create(table: str, data: dict) -> str:
        """Create a new record in the logical axis.

        Args:
            table: Target table — 'standards', 'cases', 'gaps', 'proposals'.
            data: Column-value mapping. created_at is auto-populated for cases
                  if omitted.

        Returns:
            JSON with 'id' of the created record.
        """
        t0 = time.monotonic_ns()
        allowed = {"standards", "cases", "gaps", "proposals"}
        if table not in allowed:
            return json.dumps({"error": f"table must be one of {sorted(allowed)}"})

        if not data:
            return json.dumps({"error": "data must not be empty"})

        # Auto-populate created_at for cases
        if table == "cases" and "created_at" not in data:
            data["created_at"] = _utcnow()

        conn = get_db(_db_path())
        try:
            cols = ", ".join(data.keys())
            placeholders = ", ".join("?" for _ in data)
            cursor = conn.execute(
                f"INSERT INTO {table} ({cols}) VALUES ({placeholders})",
                list(data.values()),
            )
            conn.commit()
            new_id = cursor.lastrowid

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "logical_create", "logical", 0, latency)
            conn.close()
            return json.dumps({"id": new_id, "table": table})

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def logical_escalate(case_id: int, reason: str) -> str:
        """Escalate a case by creating a gap record if surprise > 0.5.

        Args:
            case_id: ID of the case to escalate.
            reason: Human-readable escalation reason.

        Returns:
            JSON with escalation result and gap_id if created.
        """
        t0 = time.monotonic_ns()
        conn = get_db(_db_path())
        try:
            row = conn.execute(
                "SELECT id, surprise FROM cases WHERE id = ?", (case_id,)
            ).fetchone()
            if row is None:
                conn.close()
                return json.dumps({"error": f"No case with id={case_id}"})

            surprise = row["surprise"]
            gap_id = None

            if surprise > 0.5:
                cursor = conn.execute(
                    "INSERT INTO gaps (case_id, description, frequency, status, created_at)"
                    " VALUES (?, ?, 1, 'open', ?)",
                    (case_id, reason, _utcnow()),
                )
                conn.commit()
                gap_id = cursor.lastrowid

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "logical_escalate", "logical", 0, latency)
            conn.close()

            result: dict[str, Any] = {
                "case_id": case_id,
                "surprise": surprise,
                "escalated": gap_id is not None,
                "reason": reason,
            }
            if gap_id is not None:
                result["gap_id"] = gap_id
            return json.dumps(result)

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def logical_feedback(
        case_id: int, result: str, surprise: float = 0.0
    ) -> str:
        """Update a case with execution result and surprise score.

        If surprise exceeds 0.5, a gap record is automatically created.

        Args:
            case_id: ID of the case to update.
            result: Outcome description to record.
            surprise: Surprise score 0.0-1.0 (default 0.0).

        Returns:
            JSON with updated case and gap_id if auto-created.
        """
        t0 = time.monotonic_ns()
        _SURPRISE_THRESHOLD = 0.5

        conn = get_db(_db_path())
        try:
            row = conn.execute(
                "SELECT id FROM cases WHERE id = ?", (case_id,)
            ).fetchone()
            if row is None:
                conn.close()
                return json.dumps({"error": f"No case with id={case_id}"})

            conn.execute(
                "UPDATE cases SET result = ?, surprise = ? WHERE id = ?",
                (result, surprise, case_id),
            )
            conn.commit()

            gap_id = None
            if surprise > _SURPRISE_THRESHOLD:
                cursor = conn.execute(
                    "INSERT INTO gaps (case_id, description, frequency, status, created_at)"
                    " VALUES (?, ?, 1, 'open', ?)",
                    (
                        case_id,
                        f"Auto-gap: surprise={surprise:.2f} — {result[:200]}",
                        _utcnow(),
                    ),
                )
                conn.commit()
                gap_id = cursor.lastrowid

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "logical_feedback", "logical", 0, latency)
            conn.close()

            response: dict[str, Any] = {
                "case_id": case_id,
                "result": result,
                "surprise": surprise,
                "gap_auto_created": gap_id is not None,
            }
            if gap_id is not None:
                response["gap_id"] = gap_id
            return json.dumps(response)

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})
