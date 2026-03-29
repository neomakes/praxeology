"""
Praxeology MCP — Contextual axis tools.

Space → Channel → Thread → Crew → Session hierarchy

Tools:
    contextual_search    — Search contexts table by name, optional tier filter
    contextual_read      — Read context by ID or name+tier; includes parent chain
    contextual_create    — Create context with tier hierarchy validation
    contextual_escalate  — Escalate from session context; create delegation record
    contextual_feedback  — Record a crew review (KPI score + notes)
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

_VALID_TIERS = ("space", "channel", "thread", "crew", "session")

# Parent tier must be strictly higher in the hierarchy (or None for space).
_TIER_PARENT = {
    "space": None,
    "channel": "space",
    "thread": "channel",
    "crew": None,        # crew can be top-level or under a space/channel
    "session": "crew",
}


def _db_path() -> str:
    return os.environ.get("PRAXEOLOGY_DB", _DEFAULT_DB)


def _utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _row_to_dict(row) -> dict:
    return dict(row) if row is not None else {}


def _build_parent_chain(conn, context_id: int) -> list[dict]:
    """Walk up the parent_id chain and return list from root to direct parent."""
    chain: list[dict] = []
    visited: set[int] = set()
    current_id = context_id
    while current_id is not None:
        if current_id in visited:
            break  # cycle guard
        visited.add(current_id)
        row = conn.execute(
            "SELECT id, tier, name, parent_id, metadata, created_at"
            " FROM contexts WHERE id = ?",
            (current_id,),
        ).fetchone()
        if row is None:
            break
        chain.append(_row_to_dict(row))
        current_id = row["parent_id"]
    chain.reverse()
    return chain


# ---------------------------------------------------------------------------
# Tool registration helper — called by server.py
# ---------------------------------------------------------------------------

def register(mcp) -> None:
    """Register all contextual axis tools onto the given FastMCP instance."""

    @mcp.tool()
    def contextual_search(query: str, tier: str = None) -> str:
        """Search contexts by name substring.

        Args:
            query: Substring to match against context names (case-insensitive).
            tier: Optional tier filter — one of space/channel/thread/crew/session.

        Returns:
            JSON array of matching context records.
        """
        t0 = time.monotonic_ns()

        if tier is not None and tier not in _VALID_TIERS:
            return json.dumps({"error": f"tier must be one of {list(_VALID_TIERS)}"})

        conn = get_db(_db_path())
        try:
            if tier:
                rows = conn.execute(
                    """
                    SELECT id, tier, name, parent_id, metadata, created_at
                    FROM contexts
                    WHERE name LIKE ? AND tier = ?
                    ORDER BY created_at DESC
                    LIMIT 100
                    """,
                    (f"%{query}%", tier),
                ).fetchall()
            else:
                rows = conn.execute(
                    """
                    SELECT id, tier, name, parent_id, metadata, created_at
                    FROM contexts
                    WHERE name LIKE ?
                    ORDER BY created_at DESC
                    LIMIT 100
                    """,
                    (f"%{query}%",),
                ).fetchall()

            results = [_row_to_dict(r) for r in rows]
            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "contextual_search", "contextual", 0, latency)
            return json.dumps(results, ensure_ascii=False)

        except Exception as exc:
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def contextual_read(
        id: int = None, name: str = None, tier: str = None
    ) -> str:
        """Read a context record with its full parent chain.

        Look up by ID, or by name + tier combination. For crew-tier contexts,
        also returns associated channel_access entries.

        Args:
            id: Primary key of the context (takes priority over name/tier).
            name: Context name — requires tier when used.
            tier: Tier filter used with name lookup.

        Returns:
            JSON object with context data, parent_chain list, and optionally
            channel_access list for crew tier.
        """
        t0 = time.monotonic_ns()
        conn = get_db(_db_path())
        try:
            if id is not None:
                row = conn.execute(
                    "SELECT id, tier, name, parent_id, metadata, created_at"
                    " FROM contexts WHERE id = ?",
                    (id,),
                ).fetchone()
            elif name is not None and tier is not None:
                if tier not in _VALID_TIERS:
                    return json.dumps(
                        {"error": f"tier must be one of {list(_VALID_TIERS)}"}
                    )
                row = conn.execute(
                    "SELECT id, tier, name, parent_id, metadata, created_at"
                    " FROM contexts WHERE name = ? AND tier = ?",
                    (name, tier),
                ).fetchone()
            else:
                return json.dumps(
                    {"error": "Provide id, or both name and tier"}
                )

            if row is None:
                return json.dumps({"error": "Context not found"})

            ctx = _row_to_dict(row)
            parent_chain = _build_parent_chain(conn, ctx["parent_id"]) if ctx.get("parent_id") else []
            ctx["parent_chain"] = parent_chain

            # For crew tier, attach channel_access records
            if ctx["tier"] == "crew":
                access_rows = conn.execute(
                    "SELECT id, crew_id, channel_id, permission"
                    " FROM channel_access WHERE crew_id = ?",
                    (ctx["name"],),
                ).fetchall()
                ctx["channel_access"] = [_row_to_dict(r) for r in access_rows]

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "contextual_read", "contextual", 0, latency)
            return json.dumps(ctx, ensure_ascii=False)

        except Exception as exc:
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def contextual_create(
        tier: str,
        name: str,
        parent_id: int = None,
        metadata: str = "{}",
    ) -> str:
        """Create a new context node in the hierarchy.

        Validates that the tier is valid and that the parent (if given) has a
        compatible tier. For crew tier, channel_access entries can be embedded
        in metadata as {"channel_access": [{"channel_id": "...", "permission": "rw"}]}.

        Args:
            tier: One of space/channel/thread/crew/session.
            name: Unique name for this context node.
            parent_id: Optional ID of parent context.
            metadata: JSON string of extra attributes (default "{}").

        Returns:
            JSON with created context id and tier.
        """
        t0 = time.monotonic_ns()

        if tier not in _VALID_TIERS:
            return json.dumps({"error": f"tier must be one of {list(_VALID_TIERS)}"})

        # Validate metadata is valid JSON
        try:
            meta_obj = json.loads(metadata)
        except json.JSONDecodeError as exc:
            return json.dumps({"error": f"metadata is not valid JSON: {exc}"})

        conn = get_db(_db_path())
        try:
            # Validate parent tier hierarchy
            if parent_id is not None:
                parent_row = conn.execute(
                    "SELECT id, tier FROM contexts WHERE id = ?", (parent_id,)
                ).fetchone()
                if parent_row is None:
                    return json.dumps(
                        {"error": f"No context with id={parent_id}"}
                    )
                expected_parent_tier = _TIER_PARENT.get(tier)
                if (
                    expected_parent_tier is not None
                    and parent_row["tier"] != expected_parent_tier
                ):
                    return json.dumps(
                        {
                            "error": (
                                f"tier '{tier}' expects parent tier"
                                f" '{expected_parent_tier}',"
                                f" got '{parent_row['tier']}'"
                            )
                        }
                    )

            # Strip channel_access from metadata before storing
            channel_access_entries = meta_obj.pop("channel_access", None)
            clean_metadata = json.dumps(meta_obj, ensure_ascii=False)

            cursor = conn.execute(
                "INSERT INTO contexts (tier, name, parent_id, metadata, created_at)"
                " VALUES (?, ?, ?, ?, ?)",
                (tier, name, parent_id, clean_metadata, _utcnow()),
            )
            conn.commit()
            new_id = cursor.lastrowid

            # Create channel_access entries for crew tier
            access_created: list[int] = []
            if tier == "crew" and channel_access_entries:
                for entry in channel_access_entries:
                    channel_id = entry.get("channel_id")
                    permission = entry.get("permission", "r")
                    if channel_id:
                        acc = conn.execute(
                            "INSERT INTO channel_access (crew_id, channel_id, permission)"
                            " VALUES (?, ?, ?)",
                            (name, channel_id, permission),
                        )
                        conn.commit()
                        access_created.append(acc.lastrowid)

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "contextual_create", "contextual", 0, latency)

            result: dict[str, Any] = {"id": new_id, "tier": tier, "name": name}
            if access_created:
                result["channel_access_ids"] = access_created
            return json.dumps(result)

        except Exception as exc:
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def contextual_escalate(session_id: int, reason: str) -> str:
        """Escalate from a session context to its parent crew.

        Looks up the session context, finds its parent crew context, and
        creates a delegation record from the crew to a captain/escalation target.

        Args:
            session_id: ID of the session-tier context to escalate from.
            reason: Human-readable description of why escalation is needed.

        Returns:
            JSON with session info, parent crew, and the created delegation id.
        """
        t0 = time.monotonic_ns()
        conn = get_db(_db_path())
        try:
            session_row = conn.execute(
                "SELECT id, tier, name, parent_id FROM contexts WHERE id = ?",
                (session_id,),
            ).fetchone()

            if session_row is None:
                return json.dumps(
                    {"error": f"No context with id={session_id}"}
                )

            if session_row["tier"] != "session":
                return json.dumps(
                    {
                        "error": (
                            f"context id={session_id} has tier"
                            f" '{session_row['tier']}', expected 'session'"
                        )
                    }
                )

            # Resolve parent crew
            from_crew = "unknown"
            parent_id = session_row["parent_id"]
            if parent_id is not None:
                parent_row = conn.execute(
                    "SELECT tier, name FROM contexts WHERE id = ?", (parent_id,)
                ).fetchone()
                if parent_row is not None and parent_row["tier"] == "crew":
                    from_crew = parent_row["name"]

            cursor = conn.execute(
                "INSERT INTO delegations (from_crew, to_crew, task, status, created_at)"
                " VALUES (?, ?, ?, 'pending', ?)",
                (from_crew, "captain", reason, _utcnow()),
            )
            conn.commit()
            delegation_id = cursor.lastrowid

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "contextual_escalate", "contextual", 0, latency)

            return json.dumps(
                {
                    "session_id": session_id,
                    "session_name": session_row["name"],
                    "from_crew": from_crew,
                    "to_crew": "captain",
                    "reason": reason,
                    "delegation_id": delegation_id,
                    "status": "pending",
                },
                ensure_ascii=False,
            )

        except Exception as exc:
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def contextual_feedback(
        crew_id: str, period: str, kpi_score: float, notes: str = ""
    ) -> str:
        """Record a performance review for a crew member.

        Inserts a row into the reviews table with the given KPI score and notes.

        Args:
            crew_id: Identifier of the crew member (e.g. 'zoro', 'nami').
            period: Review period string (e.g. '2026-W13', '2026-04').
            kpi_score: Numeric KPI score (typically 0.0–1.0 or 0–100).
            notes: Optional free-text review notes.

        Returns:
            JSON with the created review id and all recorded fields.
        """
        t0 = time.monotonic_ns()
        conn = get_db(_db_path())
        try:
            cursor = conn.execute(
                "INSERT INTO reviews"
                " (crew_id, period, kpi_score, notes, created_at)"
                " VALUES (?, ?, ?, ?, ?)",
                (crew_id, period, kpi_score, notes, _utcnow()),
            )
            conn.commit()
            review_id = cursor.lastrowid

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "contextual_feedback", "contextual", 0, latency)

            return json.dumps(
                {
                    "id": review_id,
                    "crew_id": crew_id,
                    "period": period,
                    "kpi_score": kpi_score,
                    "notes": notes,
                    "created_at": _utcnow(),
                },
                ensure_ascii=False,
            )

        except Exception as exc:
            return json.dumps({"error": str(exc)})
