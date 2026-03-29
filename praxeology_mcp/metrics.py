"""
Praxeology MCP — Metrics tools.

Tools:
    metrics_summary  — Aggregated metrics for a given period
    metrics_compare  — Side-by-side comparison of two periods
    metrics_trend    — Daily trend for a single metric over N days
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timedelta, timezone
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


# ---------------------------------------------------------------------------
# Period helpers
# ---------------------------------------------------------------------------

def _period_bounds(period: str) -> tuple[str, str]:
    """Return (start_iso, end_iso) for a named period string.

    Supported: "today", "week", "month", "all",
               "this_week", "last_week", "this_month", "last_month".
    """
    now = datetime.now(timezone.utc)

    if period in ("today",):
        start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end = now
    elif period in ("week", "this_week"):
        # Monday of current week
        start = (now - timedelta(days=now.weekday())).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        end = now
    elif period == "last_week":
        this_monday = (now - timedelta(days=now.weekday())).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        start = this_monday - timedelta(days=7)
        end = this_monday - timedelta(seconds=1)
    elif period in ("month", "this_month"):
        start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        end = now
    elif period == "last_month":
        first_of_this = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        last_of_prev = first_of_this - timedelta(seconds=1)
        start = last_of_prev.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        end = first_of_this - timedelta(seconds=1)
    elif period == "all":
        start = datetime(2000, 1, 1, tzinfo=timezone.utc)
        end = now
    else:
        raise ValueError(
            f"Unknown period '{period}'. Use: today, week, month, all, "
            "this_week, last_week, this_month, last_month."
        )

    fmt = "%Y-%m-%dT%H:%M:%SZ"
    return start.strftime(fmt), end.strftime(fmt)


def _fetch_summary(conn, start: str, end: str) -> dict[str, Any]:
    """Query DB and return a metrics summary dict for the given time window."""

    # Total tool calls
    row = conn.execute(
        "SELECT COUNT(*) AS cnt FROM metrics_log WHERE created_at >= ? AND created_at <= ?",
        (start, end),
    ).fetchone()
    total_tool_calls = row["cnt"] if row else 0

    # Calls by axis
    rows = conn.execute(
        "SELECT axis, COUNT(*) AS cnt FROM metrics_log"
        " WHERE created_at >= ? AND created_at <= ?"
        " GROUP BY axis",
        (start, end),
    ).fetchall()
    calls_by_axis: dict[str, int] = {"logical": 0, "tactical": 0, "contextual": 0, "cross": 0}
    for r in rows:
        axis = r["axis"]
        if axis in calls_by_axis:
            calls_by_axis[axis] = r["cnt"]
        else:
            calls_by_axis[axis] = r["cnt"]

    # Average latency
    row = conn.execute(
        "SELECT AVG(latency_ms) AS avg_lat FROM metrics_log"
        " WHERE created_at >= ? AND created_at <= ?",
        (start, end),
    ).fetchone()
    avg_latency_ms = round(row["avg_lat"], 2) if row and row["avg_lat"] is not None else 0.0

    # Total tokens
    row = conn.execute(
        "SELECT SUM(tokens_used) AS total FROM metrics_log"
        " WHERE created_at >= ? AND created_at <= ?",
        (start, end),
    ).fetchone()
    total_tokens = row["total"] if row and row["total"] is not None else 0

    # Open gaps
    row = conn.execute(
        "SELECT COUNT(*) AS cnt FROM gaps WHERE status = 'open'"
        " AND created_at >= ? AND created_at <= ?",
        (start, end),
    ).fetchone()
    gap_count = row["cnt"] if row else 0

    # Pending proposals
    row = conn.execute(
        "SELECT COUNT(*) AS cnt FROM proposals WHERE status = 'pending'"
        " AND created_at >= ? AND created_at <= ?",
        (start, end),
    ).fetchone()
    proposal_count = row["cnt"] if row else 0

    gap_to_proposal_rate = round(proposal_count / gap_count, 4) if gap_count > 0 else 0.0

    return {
        "total_tool_calls": total_tool_calls,
        "calls_by_axis": calls_by_axis,
        "avg_latency_ms": avg_latency_ms,
        "total_tokens": total_tokens,
        "gap_count": gap_count,
        "proposal_count": proposal_count,
        "gap_to_proposal_rate": gap_to_proposal_rate,
    }


# ---------------------------------------------------------------------------
# Tool registration — called by server.py
# ---------------------------------------------------------------------------

def register(mcp) -> None:
    """Register all metrics tools onto the given FastMCP instance."""

    @mcp.tool()
    def metrics_summary(period: str = "today") -> str:
        """Aggregated system metrics for a named period.

        Args:
            period: One of "today", "week", "month", "all",
                    "this_week", "last_week", "this_month", "last_month".

        Returns:
            JSON object with total_tool_calls, calls_by_axis,
            avg_latency_ms, total_tokens, gap_count, proposal_count,
            gap_to_proposal_rate.
        """
        t0 = time.monotonic_ns()
        try:
            start, end = _period_bounds(period)
        except ValueError as exc:
            return json.dumps({"error": str(exc)})

        conn = get_db(_db_path())
        try:
            result = _fetch_summary(conn, start, end)
            result["period"] = period
            result["range"] = {"start": start, "end": end}

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "metrics_summary", "cross", 0, latency)
            return json.dumps(result, ensure_ascii=False)

        except Exception as exc:
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def metrics_compare(period1: str = "last_week", period2: str = "this_week") -> str:
        """Compare metrics between two periods to show learning trends.

        If lightweight heartbeat ticks increase while heavyweight calls decrease,
        the system is learning (cost decreases with use).

        Args:
            period1: Baseline period (e.g. "last_week").
            period2: Comparison period (e.g. "this_week").

        Returns:
            JSON with period1 summary, period2 summary, and delta
            (absolute difference + percentage change for each metric).
        """
        t0 = time.monotonic_ns()
        try:
            start1, end1 = _period_bounds(period1)
            start2, end2 = _period_bounds(period2)
        except ValueError as exc:
            return json.dumps({"error": str(exc)})

        conn = get_db(_db_path())
        try:
            s1 = _fetch_summary(conn, start1, end1)
            s2 = _fetch_summary(conn, start2, end2)

            # Build delta for scalar metrics
            scalar_keys = [
                "total_tool_calls",
                "avg_latency_ms",
                "total_tokens",
                "gap_count",
                "proposal_count",
                "gap_to_proposal_rate",
            ]
            delta: dict[str, Any] = {}
            for key in scalar_keys:
                v1 = s1[key]
                v2 = s2[key]
                diff = round(v2 - v1, 4) if isinstance(v2, float) else v2 - v1
                if v1 != 0:
                    pct = round((v2 - v1) / abs(v1) * 100, 2)
                else:
                    pct = None
                delta[key] = {"diff": diff, "pct_change": pct}

            # Delta for calls_by_axis
            axis_delta: dict[str, Any] = {}
            all_axes = set(s1["calls_by_axis"]) | set(s2["calls_by_axis"])
            for axis in all_axes:
                v1 = s1["calls_by_axis"].get(axis, 0)
                v2 = s2["calls_by_axis"].get(axis, 0)
                diff = v2 - v1
                pct = round(diff / abs(v1) * 100, 2) if v1 != 0 else None
                axis_delta[axis] = {"diff": diff, "pct_change": pct}
            delta["calls_by_axis"] = axis_delta

            result = {
                period1: {**s1, "range": {"start": start1, "end": end1}},
                period2: {**s2, "range": {"start": start2, "end": end2}},
                "delta": delta,
            }

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "metrics_compare", "cross", 0, latency)
            return json.dumps(result, ensure_ascii=False)

        except Exception as exc:
            return json.dumps({"error": str(exc)})

    @mcp.tool()
    def metrics_trend(metric: str = "tool_calls", days: int = 7) -> str:
        """Daily trend for a specific metric over N days.

        Args:
            metric: One of "tool_calls", "tokens", "latency",
                    "gaps_opened", "gaps_resolved", "proposals".
            days: Number of days to look back (default 7, max 365).

        Returns:
            JSON array of {date, value} objects sorted ascending by date.
        """
        t0 = time.monotonic_ns()
        supported = {"tool_calls", "tokens", "latency", "gaps_opened", "gaps_resolved", "proposals"}
        if metric not in supported:
            return json.dumps(
                {"error": f"metric must be one of {sorted(supported)}"}
            )

        days = max(1, min(days, 365))
        conn = get_db(_db_path())
        try:
            now = datetime.now(timezone.utc)
            trend: list[dict[str, Any]] = []

            for i in range(days - 1, -1, -1):
                day_start = (now - timedelta(days=i)).replace(
                    hour=0, minute=0, second=0, microsecond=0
                )
                day_end = day_start.replace(
                    hour=23, minute=59, second=59
                )
                ds = day_start.strftime("%Y-%m-%dT%H:%M:%SZ")
                de = day_end.strftime("%Y-%m-%dT%H:%M:%SZ")
                date_label = day_start.strftime("%Y-%m-%d")

                if metric == "tool_calls":
                    row = conn.execute(
                        "SELECT COUNT(*) AS v FROM metrics_log"
                        " WHERE created_at >= ? AND created_at <= ?",
                        (ds, de),
                    ).fetchone()
                    value = row["v"] if row else 0

                elif metric == "tokens":
                    row = conn.execute(
                        "SELECT COALESCE(SUM(tokens_used), 0) AS v FROM metrics_log"
                        " WHERE created_at >= ? AND created_at <= ?",
                        (ds, de),
                    ).fetchone()
                    value = row["v"] if row else 0

                elif metric == "latency":
                    row = conn.execute(
                        "SELECT COALESCE(AVG(latency_ms), 0) AS v FROM metrics_log"
                        " WHERE created_at >= ? AND created_at <= ?",
                        (ds, de),
                    ).fetchone()
                    value = round(row["v"], 2) if row else 0.0

                elif metric == "gaps_opened":
                    row = conn.execute(
                        "SELECT COUNT(*) AS v FROM gaps"
                        " WHERE created_at >= ? AND created_at <= ?",
                        (ds, de),
                    ).fetchone()
                    value = row["v"] if row else 0

                elif metric == "gaps_resolved":
                    row = conn.execute(
                        "SELECT COUNT(*) AS v FROM gaps"
                        " WHERE status = 'resolved'"
                        " AND created_at >= ? AND created_at <= ?",
                        (ds, de),
                    ).fetchone()
                    value = row["v"] if row else 0

                elif metric == "proposals":
                    row = conn.execute(
                        "SELECT COUNT(*) AS v FROM proposals"
                        " WHERE created_at >= ? AND created_at <= ?",
                        (ds, de),
                    ).fetchone()
                    value = row["v"] if row else 0

                trend.append({"date": date_label, "value": value})

            latency = (time.monotonic_ns() - t0) // 1_000_000
            log_metric(conn, "metrics_trend", "cross", 0, latency)
            return json.dumps(trend, ensure_ascii=False)

        except Exception as exc:
            return json.dumps({"error": str(exc)})
