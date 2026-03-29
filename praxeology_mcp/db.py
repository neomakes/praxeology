"""
Praxeology MCP — SQLite database module.

Public API:
    init_db(db_path)  -> sqlite3.Connection
    get_db(db_path)   -> sqlite3.Connection
    log_metric(conn, tool_name, axis, tokens, latency)
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Schema DDL
# ---------------------------------------------------------------------------

_SCHEMA = """
-- ── Logical axis ──────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS standards (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    tier        TEXT NOT NULL CHECK(tier IN ('strategy','doctrine','procedure','playbook')),
    department  TEXT NOT NULL,
    code        TEXT NOT NULL,          -- e.g. DOC-201
    title       TEXT NOT NULL,
    content     TEXT NOT NULL DEFAULT '',
    version     INTEGER NOT NULL DEFAULT 1,
    created_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now')),
    updated_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE TABLE IF NOT EXISTS cases (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    standard_id  INTEGER REFERENCES standards(id) ON DELETE SET NULL,
    objective_id INTEGER REFERENCES objectives(id) ON DELETE SET NULL,
    crew_id      TEXT,
    session_id   TEXT,
    task         TEXT NOT NULL DEFAULT '',
    action       TEXT NOT NULL DEFAULT '',
    result       TEXT NOT NULL DEFAULT '',
    surprise     REAL NOT NULL DEFAULT 0,
    created_at   TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE TABLE IF NOT EXISTS gaps (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id     INTEGER REFERENCES cases(id) ON DELETE SET NULL,
    description TEXT NOT NULL DEFAULT '',
    frequency   INTEGER NOT NULL DEFAULT 1,
    status      TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open','proposed','resolved')),
    created_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE TABLE IF NOT EXISTS proposals (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    gap_id          INTEGER REFERENCES gaps(id) ON DELETE SET NULL,
    proposed_by     TEXT,
    proposed_change TEXT NOT NULL DEFAULT '',
    status          TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending','approved','rejected')),
    reviewed_at     TEXT,
    created_at      TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

-- ── Tactical axis ─────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS objectives (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    tier        TEXT NOT NULL CHECK(tier IN ('goal','program','campaign','plan','work')),
    parent_id   INTEGER REFERENCES objectives(id) ON DELETE SET NULL,
    title       TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    status      TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending','in_progress','done','blocked')),
    priority    TEXT NOT NULL DEFAULT 'mid' CHECK(priority IN ('high','mid','low')),
    assignee    TEXT,
    due_date    TEXT,
    created_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now')),
    updated_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE TABLE IF NOT EXISTS schedules (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    objective_id INTEGER NOT NULL REFERENCES objectives(id) ON DELETE CASCADE,
    cron         TEXT NOT NULL,
    next_run     TEXT,
    last_run     TEXT,
    enabled      INTEGER NOT NULL DEFAULT 1
);

-- ── Contextual axis ───────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS contexts (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    tier       TEXT NOT NULL CHECK(tier IN ('space','channel','thread','crew','session')),
    parent_id  INTEGER REFERENCES contexts(id) ON DELETE SET NULL,
    name       TEXT NOT NULL,
    metadata   TEXT NOT NULL DEFAULT '{}',   -- JSON
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE TABLE IF NOT EXISTS reviews (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    crew_id          TEXT NOT NULL,
    period           TEXT NOT NULL,          -- e.g. 2026-W13
    kpi_score        REAL,
    peer_score       REAL,
    evolution_score  REAL,
    notes            TEXT NOT NULL DEFAULT '',
    created_at       TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE TABLE IF NOT EXISTS delegations (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    from_crew  TEXT NOT NULL,
    to_crew    TEXT NOT NULL,
    task       TEXT NOT NULL DEFAULT '',
    status     TEXT NOT NULL DEFAULT 'pending',
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

CREATE TABLE IF NOT EXISTS channel_access (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    crew_id    TEXT NOT NULL,
    channel_id TEXT NOT NULL,
    permission TEXT NOT NULL DEFAULT 'r' CHECK(permission IN ('rw','r','none'))
);

-- ── Cross-axis ────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS metrics_log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    tool_name   TEXT NOT NULL,
    axis        TEXT NOT NULL,
    tokens_used INTEGER NOT NULL DEFAULT 0,
    latency_ms  INTEGER NOT NULL DEFAULT 0,
    created_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
);

-- ── FTS5 ──────────────────────────────────────────────────────────────────

CREATE VIRTUAL TABLE IF NOT EXISTS standards_fts USING fts5(
    title,
    content,
    content=standards,
    content_rowid=id
);

CREATE VIRTUAL TABLE IF NOT EXISTS cases_fts USING fts5(
    task,
    action,
    result,
    content=cases,
    content_rowid=id
);

-- ── Indexes ───────────────────────────────────────────────────────────────

CREATE INDEX IF NOT EXISTS idx_standards_tier       ON standards(tier);
CREATE INDEX IF NOT EXISTS idx_standards_department ON standards(department);
CREATE INDEX IF NOT EXISTS idx_standards_code       ON standards(code);

CREATE INDEX IF NOT EXISTS idx_cases_standard_id    ON cases(standard_id);
CREATE INDEX IF NOT EXISTS idx_cases_objective_id   ON cases(objective_id);
CREATE INDEX IF NOT EXISTS idx_cases_crew_id        ON cases(crew_id);
CREATE INDEX IF NOT EXISTS idx_cases_status         ON cases(result);

CREATE INDEX IF NOT EXISTS idx_gaps_case_id         ON gaps(case_id);
CREATE INDEX IF NOT EXISTS idx_gaps_status          ON gaps(status);

CREATE INDEX IF NOT EXISTS idx_proposals_gap_id     ON proposals(gap_id);
CREATE INDEX IF NOT EXISTS idx_proposals_status     ON proposals(status);

CREATE INDEX IF NOT EXISTS idx_objectives_parent_id ON objectives(parent_id);
CREATE INDEX IF NOT EXISTS idx_objectives_status    ON objectives(status);
CREATE INDEX IF NOT EXISTS idx_objectives_assignee  ON objectives(assignee);

CREATE INDEX IF NOT EXISTS idx_schedules_obj_id     ON schedules(objective_id);

CREATE INDEX IF NOT EXISTS idx_contexts_parent_id   ON contexts(parent_id);
CREATE INDEX IF NOT EXISTS idx_contexts_tier        ON contexts(tier);

CREATE INDEX IF NOT EXISTS idx_reviews_crew_id      ON reviews(crew_id);

CREATE INDEX IF NOT EXISTS idx_delegations_from     ON delegations(from_crew);
CREATE INDEX IF NOT EXISTS idx_delegations_to       ON delegations(to_crew);
CREATE INDEX IF NOT EXISTS idx_delegations_status   ON delegations(status);

CREATE INDEX IF NOT EXISTS idx_channel_access_crew  ON channel_access(crew_id);

CREATE INDEX IF NOT EXISTS idx_metrics_tool         ON metrics_log(tool_name);
CREATE INDEX IF NOT EXISTS idx_metrics_axis         ON metrics_log(axis);
"""

# FTS triggers keep the virtual tables in sync with their content tables.
_FTS_TRIGGERS = """
CREATE TRIGGER IF NOT EXISTS standards_fts_insert
    AFTER INSERT ON standards BEGIN
        INSERT INTO standards_fts(rowid, title, content)
        VALUES (new.id, new.title, new.content);
    END;

CREATE TRIGGER IF NOT EXISTS standards_fts_update
    AFTER UPDATE ON standards BEGIN
        INSERT INTO standards_fts(standards_fts, rowid, title, content)
        VALUES ('delete', old.id, old.title, old.content);
        INSERT INTO standards_fts(rowid, title, content)
        VALUES (new.id, new.title, new.content);
    END;

CREATE TRIGGER IF NOT EXISTS standards_fts_delete
    AFTER DELETE ON standards BEGIN
        INSERT INTO standards_fts(standards_fts, rowid, title, content)
        VALUES ('delete', old.id, old.title, old.content);
    END;

CREATE TRIGGER IF NOT EXISTS cases_fts_insert
    AFTER INSERT ON cases BEGIN
        INSERT INTO cases_fts(rowid, task, action, result)
        VALUES (new.id, new.task, new.action, new.result);
    END;

CREATE TRIGGER IF NOT EXISTS cases_fts_update
    AFTER UPDATE ON cases BEGIN
        INSERT INTO cases_fts(cases_fts, rowid, task, action, result)
        VALUES ('delete', old.id, old.task, old.action, old.result);
        INSERT INTO cases_fts(rowid, task, action, result)
        VALUES (new.id, new.task, new.action, new.result);
    END;

CREATE TRIGGER IF NOT EXISTS cases_fts_delete
    AFTER DELETE ON cases BEGIN
        INSERT INTO cases_fts(cases_fts, rowid, task, action, result)
        VALUES ('delete', old.id, old.task, old.action, old.result);
    END;
"""


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def init_db(db_path: str) -> sqlite3.Connection:
    """Create all tables, FTS5 virtual tables, indexes, and triggers.

    Idempotent — safe to call on an existing database.
    Returns an open connection with WAL mode and row_factory set.
    """
    conn = _connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    # objectives must exist before cases (FK reference), so we execute the
    # full schema in a single executescript which runs statements in order.
    conn.executescript(_SCHEMA)
    conn.executescript(_FTS_TRIGGERS)
    conn.commit()
    return conn


def get_db(db_path: str) -> sqlite3.Connection:
    """Return an open connection for the given path.

    Enables WAL, foreign keys, and sqlite3.Row factory.
    Does NOT create tables — call init_db first.
    """
    conn = _connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def log_metric(
    conn: sqlite3.Connection,
    tool_name: str,
    axis: str,
    tokens: int,
    latency: int,
) -> None:
    """Insert one row into metrics_log."""
    conn.execute(
        "INSERT INTO metrics_log (tool_name, axis, tokens_used, latency_ms, created_at)"
        " VALUES (?, ?, ?, ?, ?)",
        (tool_name, axis, tokens, latency, _utcnow()),
    )
    conn.commit()


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def _utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
