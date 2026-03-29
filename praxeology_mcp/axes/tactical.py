"""
Praxeology MCP — Tactical axis tools.

Goal → Program → Campaign → Plan → Work

Tools:
    tactical_search    — Search objectives by query, tier, status
    tactical_read      — Read objective by ID with full ancestor chain
    tactical_create    — Create objective with tier/parent validation
    tactical_escalate  — Block an objective and record reason
    tactical_feedback  — Update status and append notes; check children on done
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

_TIER_ORDER = ["goal", "program", "campaign", "plan", "work"]
_VALID_TIERS = set(_TIER_ORDER)
_VALID_STATUSES = {"pending", "in_progress", "done", "blocked"}
_VALID_PRIORITIES = {"high", "mid", "low"}


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
    """Register all tactical axis tools onto the given FastMCP instance."""

    @mcp.tool()
    def tactical_search(
        query: str,
        tier: str = None,
        status: str = None,
    ) -> str:
        """Search objectives by keyword, optionally filtered by tier and/or status.

        Args:
            query: Search terms matched against title and description (LIKE).
            tier: Optional tier filter — one of goal/program/campaign/plan/work.
            status: Optional status filter — one of pending/in_progress/done/blocked.

        Returns:
            JSON array of matching objective records.
        """
        t0 = time.monotonic_ns()

        if tier is not None and tier not in _VALID_TIERS:
            return json.dumps({"error": f"tier must be one of {_TIER_ORDER}"})
        if status is not None and status not in _VALID_STATUSES:
            return json.dumps({"error": f"status must be one of {sorted(_VALID_STATUSES)}"})

        conn = get_db(_db_path())
        try:
            like = f"%{query}%"
            params: list[Any] = [like, like]
            where_clauses = ["(title LIKE ? OR description LIKE ?)"]

            if tier:
                where_clauses.append("tier = ?")
                params.append(tier)
            if status:
                where_clauses.append("status = ?")
                params.append(status)

            where_sql = " AND ".join(where_clauses)
            rows = conn.execute(
                f"SELECT * FROM objectives WHERE {where_sql} ORDER BY created_at DESC LIMIT 100",
                params,
            ).fetchall()

            results = [_row_to_dict(r) for r in rows]
            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "tactical_search", "tactical", 0, latency)
            conn.close()
            return json.dumps(results, ensure_ascii=False)

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def tactical_read(id: int) -> str:
        """Read an objective by ID, including its full ancestor chain up to root.

        Args:
            id: Primary key of the objective.

        Returns:
            JSON object with 'objective' (the target record) and 'ancestors'
            (list from immediate parent to root, ordered nearest-first).
        """
        t0 = time.monotonic_ns()
        conn = get_db(_db_path())
        try:
            row = conn.execute(
                "SELECT * FROM objectives WHERE id = ?", (id,)
            ).fetchone()
            if row is None:
                conn.close()
                return json.dumps({"error": f"No objective with id={id}"})

            objective = _row_to_dict(row)

            # Walk parent chain to root
            ancestors: list[dict] = []
            current_parent_id = objective.get("parent_id")
            seen: set[int] = {id}
            while current_parent_id is not None:
                if current_parent_id in seen:
                    break  # cycle guard
                seen.add(current_parent_id)
                parent_row = conn.execute(
                    "SELECT * FROM objectives WHERE id = ?", (current_parent_id,)
                ).fetchone()
                if parent_row is None:
                    break
                parent = _row_to_dict(parent_row)
                ancestors.append(parent)
                current_parent_id = parent.get("parent_id")

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "tactical_read", "tactical", 0, latency)
            conn.close()
            return json.dumps(
                {"objective": objective, "ancestors": ancestors},
                ensure_ascii=False,
            )

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def tactical_create(
        tier: str,
        title: str,
        description: str = "",
        parent_id: int = None,
        priority: str = "mid",
        assignee: str = None,
        due_date: str = None,
    ) -> str:
        """Create a new objective in the Goal→Program→Campaign→Plan→Work hierarchy.

        Args:
            tier: One of goal/program/campaign/plan/work.
            title: Short title for the objective.
            description: Optional longer description.
            parent_id: ID of the parent objective. Parent must exist and be a
                       higher tier (e.g. a plan can only parent a work item).
            priority: One of high/mid/low (default mid).
            assignee: Optional crew member ID to assign.
            due_date: Optional ISO date string (YYYY-MM-DD).

        Returns:
            JSON with 'id' of the created objective.
        """
        t0 = time.monotonic_ns()

        if tier not in _VALID_TIERS:
            return json.dumps({"error": f"tier must be one of {_TIER_ORDER}"})
        if priority not in _VALID_PRIORITIES:
            return json.dumps({"error": f"priority must be one of {sorted(_VALID_PRIORITIES)}"})
        if not title or not title.strip():
            return json.dumps({"error": "title must not be empty"})

        conn = get_db(_db_path())
        try:
            if parent_id is not None:
                parent_row = conn.execute(
                    "SELECT id, tier FROM objectives WHERE id = ?", (parent_id,)
                ).fetchone()
                if parent_row is None:
                    conn.close()
                    return json.dumps({"error": f"No parent objective with id={parent_id}"})

                parent_tier = parent_row["tier"]
                parent_tier_idx = _TIER_ORDER.index(parent_tier)
                child_tier_idx = _TIER_ORDER.index(tier)
                if child_tier_idx <= parent_tier_idx:
                    conn.close()
                    return json.dumps({
                        "error": (
                            f"Child tier '{tier}' must be lower than parent tier '{parent_tier}'. "
                            f"Hierarchy: {' > '.join(_TIER_ORDER)}"
                        )
                    })

            now = _utcnow()
            cursor = conn.execute(
                """
                INSERT INTO objectives
                    (tier, parent_id, title, description, status, priority,
                     assignee, due_date, created_at, updated_at)
                VALUES (?, ?, ?, ?, 'pending', ?, ?, ?, ?, ?)
                """,
                (tier, parent_id, title.strip(), description, priority,
                 assignee, due_date, now, now),
            )
            conn.commit()
            new_id = cursor.lastrowid

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "tactical_create", "tactical", 0, latency)
            conn.close()
            return json.dumps({"id": new_id, "tier": tier, "title": title.strip()})

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def tactical_escalate(id: int, reason: str) -> str:
        """Escalate an objective — set status to blocked and record reason.

        For work items, the parent plan's status is also set to blocked if it
        is currently pending or in_progress.

        Args:
            id: ID of the objective to escalate.
            reason: Human-readable escalation reason (appended to description).

        Returns:
            JSON with updated objective and parent_notified flag.
        """
        t0 = time.monotonic_ns()

        if not reason or not reason.strip():
            return json.dumps({"error": "reason must not be empty"})

        conn = get_db(_db_path())
        try:
            row = conn.execute(
                "SELECT * FROM objectives WHERE id = ?", (id,)
            ).fetchone()
            if row is None:
                conn.close()
                return json.dumps({"error": f"No objective with id={id}"})

            obj = _row_to_dict(row)
            now = _utcnow()
            escalation_note = f"\n[ESCALATED {now}] {reason.strip()}"
            new_description = (obj.get("description") or "") + escalation_note

            conn.execute(
                "UPDATE objectives SET status = 'blocked', description = ?, updated_at = ? WHERE id = ?",
                (new_description, now, id),
            )
            conn.commit()

            parent_notified = False
            if obj["tier"] == "work" and obj.get("parent_id") is not None:
                parent_row = conn.execute(
                    "SELECT id, status FROM objectives WHERE id = ?",
                    (obj["parent_id"],),
                ).fetchone()
                if parent_row and parent_row["status"] in ("pending", "in_progress"):
                    conn.execute(
                        "UPDATE objectives SET status = 'blocked', updated_at = ? WHERE id = ?",
                        (now, obj["parent_id"]),
                    )
                    conn.commit()
                    parent_notified = True

            updated_row = conn.execute(
                "SELECT * FROM objectives WHERE id = ?", (id,)
            ).fetchone()

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "tactical_escalate", "tactical", 0, latency)
            conn.close()

            return json.dumps(
                {
                    "objective": _row_to_dict(updated_row),
                    "parent_notified": parent_notified,
                },
                ensure_ascii=False,
            )

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def tactical_feedback(
        id: int,
        status: str,
        notes: str = "",
    ) -> str:
        """Update an objective's status and optionally append notes to description.

        If status is set to 'done' and the objective has children, reports how
        many children are still incomplete.

        Args:
            id: ID of the objective to update.
            status: New status — one of pending/in_progress/done/blocked.
            notes: Optional notes to append to the description.

        Returns:
            JSON with updated objective and, when status=done, a
            'children_incomplete' count.
        """
        t0 = time.monotonic_ns()

        if status not in _VALID_STATUSES:
            return json.dumps({"error": f"status must be one of {sorted(_VALID_STATUSES)}"})

        conn = get_db(_db_path())
        try:
            row = conn.execute(
                "SELECT * FROM objectives WHERE id = ?", (id,)
            ).fetchone()
            if row is None:
                conn.close()
                return json.dumps({"error": f"No objective with id={id}"})

            obj = _row_to_dict(row)
            now = _utcnow()

            new_description = obj.get("description") or ""
            if notes and notes.strip():
                new_description += f"\n[{now}] {notes.strip()}"

            conn.execute(
                "UPDATE objectives SET status = ?, description = ?, updated_at = ? WHERE id = ?",
                (status, new_description, now, id),
            )
            conn.commit()

            updated_row = conn.execute(
                "SELECT * FROM objectives WHERE id = ?", (id,)
            ).fetchone()

            response: dict[str, Any] = {"objective": _row_to_dict(updated_row)}

            if status == "done":
                incomplete_count = conn.execute(
                    "SELECT COUNT(*) FROM objectives WHERE parent_id = ? AND status != 'done'",
                    (id,),
                ).fetchone()[0]
                response["children_incomplete"] = incomplete_count

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "tactical_feedback", "tactical", 0, latency)
            conn.close()
            return json.dumps(response, ensure_ascii=False)

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})
