"""
Praxeology MCP — Cross-axis tools.

Cross-references Logical, Tactical, and Contextual axes to surface
the highest-value action and propagate execution results back.

Tools:
    what_now   — Recommend the highest-value action right now
    backprop   — Backward pass: update all 3 axes from execution result
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
    """Register all cross-axis tools onto the given FastMCP instance."""

    @mcp.tool()
    def what_now(crew_id: str = None) -> str:
        """Recommend the highest-value action right now by cross-referencing all 3 axes.

        Cross-references pending work items (tactical), related standards (logical),
        open gaps, overdue schedules, and recent crew activity (contextual).

        Args:
            crew_id: Optional crew filter. If given, only work items assigned to
                     this crew are considered.

        Returns:
            JSON object with recommended_action, related_standards, open_gaps,
            overdue_schedules, and context summary.
        """
        t0 = time.monotonic_ns()
        conn = get_db(_db_path())
        try:
            # ── Tactical: top 3 pending/in_progress work items ──────────────
            if crew_id:
                work_rows = conn.execute(
                    """
                    SELECT id, title, description, status, priority, assignee,
                           due_date, created_at
                    FROM objectives
                    WHERE tier = 'work'
                      AND status IN ('pending', 'in_progress')
                      AND assignee = ?
                    ORDER BY
                        CASE priority WHEN 'high' THEN 0 WHEN 'mid' THEN 1 ELSE 2 END,
                        created_at ASC
                    LIMIT 3
                    """,
                    (crew_id,),
                ).fetchall()
            else:
                work_rows = conn.execute(
                    """
                    SELECT id, title, description, status, priority, assignee,
                           due_date, created_at
                    FROM objectives
                    WHERE tier = 'work'
                      AND status IN ('pending', 'in_progress')
                    ORDER BY
                        CASE priority WHEN 'high' THEN 0 WHEN 'mid' THEN 1 ELSE 2 END,
                        created_at ASC
                    LIMIT 3
                    """,
                ).fetchall()

            work_items: list[dict[str, Any]] = [_row_to_dict(r) for r in work_rows]
            top_item = work_items[0] if work_items else None

            # ── Logical: related standards via cases linked to top item ──────
            related_standards: list[dict[str, Any]] = []
            if top_item:
                obj_id = top_item["id"]
                std_rows = conn.execute(
                    """
                    SELECT DISTINCT s.id, s.tier, s.department, s.code, s.title
                    FROM cases c
                    JOIN standards s ON s.id = c.standard_id
                    WHERE c.objective_id = ?
                      AND c.standard_id IS NOT NULL
                    LIMIT 5
                    """,
                    (obj_id,),
                ).fetchall()
                related_standards = [_row_to_dict(r) for r in std_rows]

            # ── Logical: open gaps ───────────────────────────────────────────
            gap_rows = conn.execute(
                """
                SELECT id, case_id, description, frequency, created_at
                FROM gaps
                WHERE status = 'open'
                ORDER BY frequency DESC, created_at ASC
                LIMIT 5
                """,
            ).fetchall()
            open_gaps: list[dict[str, Any]] = [_row_to_dict(r) for r in gap_rows]

            # ── Tactical: overdue schedules ──────────────────────────────────
            now_str = _utcnow()
            overdue_rows = conn.execute(
                """
                SELECT s.id, s.objective_id, s.cron, s.next_run, s.last_run,
                       o.title AS objective_title
                FROM schedules s
                JOIN objectives o ON o.id = s.objective_id
                WHERE s.enabled = 1
                  AND s.next_run IS NOT NULL
                  AND s.next_run < ?
                ORDER BY s.next_run ASC
                LIMIT 5
                """,
                (now_str,),
            ).fetchall()
            overdue_schedules: list[dict[str, Any]] = [_row_to_dict(r) for r in overdue_rows]

            # ── Contextual: recent activity summary ──────────────────────────
            if crew_id:
                recent_cases = conn.execute(
                    """
                    SELECT task, action, result, surprise, created_at
                    FROM cases
                    WHERE crew_id = ?
                    ORDER BY created_at DESC
                    LIMIT 5
                    """,
                    (crew_id,),
                ).fetchall()
            else:
                recent_cases = conn.execute(
                    """
                    SELECT crew_id, task, action, result, surprise, created_at
                    FROM cases
                    ORDER BY created_at DESC
                    LIMIT 5
                    """,
                ).fetchall()
            context_summary = [_row_to_dict(r) for r in recent_cases]

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "what_now", "cross", 0, latency)
            conn.close()

            response: dict[str, Any] = {
                "recommended_action": top_item,
                "candidate_work_items": work_items[1:],
                "related_standards": related_standards,
                "open_gaps": open_gaps,
                "overdue_schedules": overdue_schedules,
                "context": context_summary,
            }
            return json.dumps(response, ensure_ascii=False)

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def backprop(case_id: int, result: str, surprise: float = 0.0) -> str:
        """Backward pass: update all 3 axes based on an execution result.

        Reads the case, then fans out updates across logical, tactical, and
        contextual axes proportional to the surprise score.

        Thresholds:
            surprise > 0.5  → create gap record (logical)
            surprise > 0.8  → auto-create proposal from that gap (logical)
            result contains 'done'/'complete'/'finished' → mark objective done (tactical)

        Args:
            case_id:  ID of the case that was executed.
            result:   Outcome description to record on the case.
            surprise: Surprise score 0.0–1.0 (default 0.0).

        Returns:
            JSON summary of all updates made across the 3 axes.
        """
        surprise = max(0.0, min(1.0, surprise))
        t0 = time.monotonic_ns()
        conn = get_db(_db_path())
        updates: dict[str, Any] = {
            "case_id": case_id,
            "result": result,
            "surprise": surprise,
            "logical": {},
            "tactical": {},
            "contextual": {},
        }

        try:
            # ── Read the case ────────────────────────────────────────────────
            case_row = conn.execute(
                "SELECT id, standard_id, objective_id, crew_id FROM cases WHERE id = ?",
                (case_id,),
            ).fetchone()
            if case_row is None:
                conn.close()
                return json.dumps({"error": f"No case with id={case_id}"})

            standard_id = case_row["standard_id"]
            objective_id = case_row["objective_id"]
            crew_id = case_row["crew_id"]

            # ── Update case with result + surprise ───────────────────────────
            conn.execute(
                "UPDATE cases SET result = ?, surprise = ? WHERE id = ?",
                (result, surprise, case_id),
            )
            conn.commit()
            updates["logical"]["case_updated"] = True

            # ── Logical: gap creation ────────────────────────────────────────
            gap_id = None
            if surprise > 0.5:
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
                updates["logical"]["gap_created"] = True
                updates["logical"]["gap_id"] = gap_id

            # ── Logical: auto-proposal ───────────────────────────────────────
            if surprise > 0.8 and gap_id is not None:
                cursor = conn.execute(
                    "INSERT INTO proposals"
                    " (gap_id, proposed_by, proposed_change, status, created_at)"
                    " VALUES (?, ?, ?, 'pending', ?)",
                    (
                        gap_id,
                        crew_id or "system",
                        f"Review standard/procedure — high surprise ({surprise:.2f}) on case {case_id}: {result[:300]}",
                        _utcnow(),
                    ),
                )
                conn.commit()
                updates["logical"]["proposal_created"] = True
                updates["logical"]["proposal_id"] = cursor.lastrowid

            # ── Tactical: mark objective done if result signals completion ───
            _COMPLETION_KEYWORDS = ("done", "complete", "completed", "finished", "resolved")
            result_lower = result.lower()
            if objective_id is not None and any(kw in result_lower for kw in _COMPLETION_KEYWORDS):
                conn.execute(
                    "UPDATE objectives SET status = 'done', updated_at = ? WHERE id = ?",
                    (_utcnow(), objective_id),
                )
                conn.commit()
                updates["tactical"]["objective_id"] = objective_id
                updates["tactical"]["objective_status"] = "done"

            # ── Contextual: log execution in metrics_log ─────────────────────
            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "backprop", "cross", 0, latency)
            updates["contextual"]["metric_logged"] = True
            updates["contextual"]["latency_ms"] = latency

            conn.close()
            return json.dumps(updates, ensure_ascii=False)

        except Exception as exc:
            conn.close()
            return json.dumps({"error": str(exc)})
