"""
Praxeology MCP — CLI module.

Usage:
    python3 -m praxeology_mcp init --name MyOrg --agents 3
    python3 -m praxeology_mcp connect
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Template content
# ---------------------------------------------------------------------------

_ROOT_CLAUDE_MD = """\
# {name}

This project is governed by Praxeology MCP.

## Available MCP Tools

| Tool | Description |
|------|-------------|
| `what_now()` | Returns the highest-priority pending task for the current session |
| `logical_search` | Full-text search across standards (STR/DOC/PRC/PLY) |
| `logical_read` | Read a specific standard by code (e.g. DOC-201) |
| `logical_create` | Create a new standard entry |
| `tactical_search` | Search objectives and work items |
| `tactical_read` | Read a specific objective by ID |
| `tactical_create` | Create a new objective or work item |
| `contextual_search` | Search across spaces, channels, threads, crew, sessions |
| `contextual_read` | Read a specific context node |
| `contextual_create` | Create a new context node |
| `backprop()` | Record a gap, surprise, or lesson from the current session |

## SafetyGate Rules

- **STR violation detected** → HALT. Do not proceed. Report to captain.
- **DOC violation detected** → HALT. Do not proceed. Report to captain.
- **Uncertainty > threshold** → Do not guess. Ask the user before continuing.
- Never execute destructive operations without explicit captain approval.
- Never broaden task scope beyond what was explicitly requested.

## Session Protocol

1. Read your `sop.md` at session start.
2. Call `what_now()` to identify the highest-priority task.
3. Execute the task within defined boundaries.
4. Report: completed / in_progress / blocked.
5. Call `backprop()` if any gap, surprise, or lesson occurred.
"""

_CREW_CLAUDE_MD = """\
# {name} Crew — Shared Rules

All crew members must adhere to these shared standards.

## Communication Rules

- Respond only when directly addressed.
- Keep responses short (1-3 sentences for chat; structured for reports).
- No unsolicited opinions or commentary on other crew members' work.
- Declare results, not intentions. Never end with "I will do X" — do it first.

## Session Protocol

1. Read this file and your own `sop.md`.
2. Call `what_now()` to check current priorities.
3. Execute assigned tasks within your role boundaries.
4. Report daily: completed / in_progress / blocked.
5. Escalate blockers after 15 minutes to captain.

## Escalation

15-min block, crew conflict, SafetyGate violation, out-of-role request:
`[CrewName] reporting. Mission blocked. Reason: [X]. Awaiting your orders, Captain.`

## Language

Answer in the project's primary language. Code and technical terms in English.
"""

_AGENT_CLAUDE_MD = """\
# {agent_name} — Agent {agent_num}

## Identity

- Name: {agent_name}
- Role: [Define role here]
- Department: [Define department here]

## Persona

[Describe the agent's personality and working style here.]

## Speech Rules

- [Define communication style here]
- [Define sentence length and tone here]
- No emojis.

## Anti-Patterns

- [List behaviors to avoid]
- No unsolicited scope expansion.
- No "I will do X" without doing it first.

## Emotional Triggers

- **Routine**: [Describe default state]
- **Blocked**: [Describe response to blockers]
- **Error**: Acknowledge immediately. State cause. State fix.

## Values

- [Core value 1]
- [Core value 2]
- [Core value 3]

## Boundaries

- Does NOT handle: [list out-of-scope responsibilities]
- Escalates to captain when: [list escalation conditions]
"""

def _build_mcp_json(project_dir: Path) -> dict:
    venv_python = str(project_dir / ".venv" / "bin" / "python3")
    return {
        "mcpServers": {
            "praxeology": {
                "command": venv_python,
                "args": ["-m", "praxeology_mcp"],
            }
        }
    }


# ---------------------------------------------------------------------------
# Command: init
# ---------------------------------------------------------------------------

def cmd_init(args: argparse.Namespace) -> None:
    cwd = Path.cwd()
    name: str = args.name
    num_agents: int = args.agents
    existing: bool = getattr(args, "existing", False)

    created: list[str] = []

    if existing:
        # Only create .mcp.json and initialize DB; migrate existing files.
        mcp_json_path = cwd / ".mcp.json"
        mcp_json_path.write_text(
            json.dumps(_build_mcp_json(cwd), indent=2) + "\n", encoding="utf-8"
        )
        created.append(str(mcp_json_path))

        db_dir = Path.home() / ".claude" / "praxeology"
        db_dir.mkdir(parents=True, exist_ok=True)
        db_path = db_dir / "praxeology.db"

        from praxeology_mcp.db import init_db
        init_db(str(db_path))

        # Auto-migrate existing files into DB.
        migrate_args = argparse.Namespace(project_dir=str(cwd))
        cmd_migrate(migrate_args)

        print("Added Praxeology MCP to existing project. Migrated files to DB.")
        return

    # Normal (new project) flow.

    # 1. Root CLAUDE.md
    root_claude = cwd / "CLAUDE.md"
    root_claude.write_text(_ROOT_CLAUDE_MD.format(name=name), encoding="utf-8")
    created.append(str(root_claude))

    # 2. _crew/CLAUDE.md
    crew_dir = cwd / "_crew"
    crew_dir.mkdir(exist_ok=True)
    crew_claude = crew_dir / "CLAUDE.md"
    crew_claude.write_text(_CREW_CLAUDE_MD.format(name=name), encoding="utf-8")
    created.append(str(crew_claude))

    # 3. _standard/ directory
    standard_dir = cwd / "_standard"
    standard_dir.mkdir(exist_ok=True)
    created.append(str(standard_dir) + "/")

    # 4. Agent directories
    for i in range(1, num_agents + 1):
        agent_name = f"agent-{i}"
        agent_dir = crew_dir / agent_name
        agent_dir.mkdir(exist_ok=True)
        agent_claude = agent_dir / "CLAUDE.md"
        agent_claude.write_text(
            _AGENT_CLAUDE_MD.format(agent_name=agent_name.capitalize(), agent_num=i),
            encoding="utf-8",
        )
        created.append(str(agent_claude))

    # 5. .mcp.json
    mcp_json_path = cwd / ".mcp.json"
    mcp_json_path.write_text(
        json.dumps(_build_mcp_json(cwd), indent=2) + "\n", encoding="utf-8"
    )
    created.append(str(mcp_json_path))

    # 6. Initialize DB
    db_dir = Path.home() / ".claude" / "praxeology"
    db_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / "praxeology.db"

    from praxeology_mcp.db import init_db
    init_db(str(db_path))
    created.append(str(db_path) + " (DB)")

    # 7. Print summary
    print(f"Praxeology initialized for '{name}'")
    print()
    print("Created:")
    for path in created:
        print(f"  {path}")
    print()
    print(f"DB: {db_path}")
    print()
    print("Next: edit CLAUDE.md and _crew/agent-*/CLAUDE.md to fill in agent roles.")


# ---------------------------------------------------------------------------
# Command: connect
# ---------------------------------------------------------------------------

def cmd_connect(_args: argparse.Namespace) -> None:
    print("Not implemented yet.")


# ---------------------------------------------------------------------------
# Command: migrate
# ---------------------------------------------------------------------------

_TIER_MAP = {
    "STR": "strategy",
    "DOC": "doctrine",
    "PRC": "procedure",
    "PLY": "playbook",
}

_STATUS_MAP = {
    "pending": "pending",
    "in_progress": "in_progress",
    "done": "done",
    "blocked": "blocked",
}

_PRIORITY_MAP = {
    "high": "high",
    "mid": "mid",
    "low": "low",
}


def _db_path() -> str:
    return str(Path.home() / ".claude" / "praxeology" / "praxeology.db")


def cmd_migrate(args: argparse.Namespace) -> None:
    import re
    import sqlite3

    project_dir = Path(args.project_dir).expanduser().resolve()
    if not project_dir.is_dir():
        print(f"Error: --project-dir '{project_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)

    db_path = _db_path()
    # Ensure DB is initialized.
    from praxeology_mcp.db import init_db
    conn = init_db(db_path)

    migrated_standards = 0
    migrated_objectives = 0
    migrated_crew = 0
    skipped = 0

    # ------------------------------------------------------------------
    # 1. Standards from _standard/**/*.md  (fallback: system/praxeology/**/*.md)
    # ------------------------------------------------------------------
    standard_roots: list[Path] = []
    local_std = project_dir / "_standard"
    drive_std = project_dir / "system" / "praxeology"
    if local_std.is_dir():
        standard_roots.append(local_std)
    if drive_std.is_dir():
        standard_roots.append(drive_std)

    for std_root in standard_roots:
        for md_file in sorted(std_root.rglob("*.md")):
            stem = md_file.stem  # e.g. "DOC-201"
            prefix = stem.split("-")[0].upper() if "-" in stem else ""
            tier = _TIER_MAP.get(prefix)
            if tier is None:
                continue  # not a standard file

            department = md_file.parent.name
            code = stem
            content = md_file.read_text(encoding="utf-8", errors="replace")
            # Use first non-empty line as title, else code.
            title = next(
                (ln.lstrip("# ").strip() for ln in content.splitlines() if ln.strip()),
                code,
            )

            # Idempotency check
            row = conn.execute(
                "SELECT id FROM standards WHERE code = ?", (code,)
            ).fetchone()
            if row is not None:
                skipped += 1
                continue

            conn.execute(
                "INSERT INTO standards (tier, department, code, title, content)"
                " VALUES (?, ?, ?, ?, ?)",
                (tier, department, code, title, content),
            )
            migrated_standards += 1

    conn.commit()

    # ------------------------------------------------------------------
    # 2 & 3. Objectives from _crew/*/todo.json and weekly.json
    # ------------------------------------------------------------------
    crew_dir = project_dir / "_crew"
    if crew_dir.is_dir():
        for member_dir in sorted(crew_dir.iterdir()):
            if not member_dir.is_dir():
                continue

            crew_name = member_dir.name

            # --- todo.json → 'work' tier objectives ---
            todo_path = member_dir / "todo.json"
            if todo_path.is_file():
                try:
                    todo_data = json.loads(todo_path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, OSError):
                    todo_data = {}

                date_str = todo_data.get("date", "")
                tasks = todo_data.get("tasks", [])
                for task in tasks:
                    title = str(task.get("task", "")).strip()
                    if not title:
                        continue
                    status = _STATUS_MAP.get(str(task.get("status", "pending")), "pending")
                    priority = _PRIORITY_MAP.get(str(task.get("priority", "mid")), "mid")
                    notes = str(task.get("notes", ""))

                    # Idempotency: same title + date
                    row = conn.execute(
                        "SELECT id FROM objectives WHERE title = ? AND due_date = ?",
                        (title, date_str or None),
                    ).fetchone()
                    if row is not None:
                        skipped += 1
                        continue

                    conn.execute(
                        "INSERT INTO objectives"
                        " (tier, title, description, status, priority, assignee, due_date)"
                        " VALUES (?, ?, ?, ?, ?, ?, ?)",
                        ("work", title, notes, status, priority, crew_name, date_str or None),
                    )
                    migrated_objectives += 1

            conn.commit()

            # --- weekly.json → 'plan' tier objectives (parent) + 'work' children ---
            weekly_path = member_dir / "weekly.json"
            if weekly_path.is_file():
                try:
                    weekly_data = json.loads(weekly_path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, OSError):
                    weekly_data = {}

                week = weekly_data.get("week", "")
                days = ["mon", "tue", "wed", "thu", "fri"]
                for day in days:
                    day_tasks = weekly_data.get(day, [])
                    if not day_tasks:
                        continue

                    plan_title = f"{crew_name} — {week} {day}"

                    # Idempotency check for the plan objective
                    plan_row = conn.execute(
                        "SELECT id FROM objectives WHERE title = ? AND tier = 'plan'",
                        (plan_title,),
                    ).fetchone()
                    if plan_row is not None:
                        skipped += 1
                        # Still try to insert children that may be missing
                        plan_id = plan_row["id"]
                    else:
                        cur = conn.execute(
                            "INSERT INTO objectives (tier, title, assignee)"
                            " VALUES ('plan', ?, ?)",
                            (plan_title, crew_name),
                        )
                        plan_id = cur.lastrowid
                        migrated_objectives += 1

                    for item in day_tasks:
                        task_title = str(item.get("task", "")).strip()
                        if not task_title:
                            continue
                        priority = _PRIORITY_MAP.get(str(item.get("priority", "mid")), "mid")

                        row = conn.execute(
                            "SELECT id FROM objectives"
                            " WHERE title = ? AND parent_id = ?",
                            (task_title, plan_id),
                        ).fetchone()
                        if row is not None:
                            skipped += 1
                            continue

                        conn.execute(
                            "INSERT INTO objectives"
                            " (tier, parent_id, title, priority, assignee)"
                            " VALUES ('work', ?, ?, ?, ?)",
                            (plan_id, task_title, priority, crew_name),
                        )
                        migrated_objectives += 1

                conn.commit()

            # --- CLAUDE.md → contexts (crew) ---
            claude_md = member_dir / "CLAUDE.md"
            if claude_md.is_file():
                content = claude_md.read_text(encoding="utf-8", errors="replace")
                # Try to parse Name from first heading
                name_match = None
                for line in content.splitlines():
                    line = line.strip()
                    if line.startswith("#"):
                        name_match = line.lstrip("#").strip()
                        break
                display_name = name_match or crew_name

                row = conn.execute(
                    "SELECT id FROM contexts WHERE tier = 'crew' AND name = ?",
                    (display_name,),
                ).fetchone()
                if row is not None:
                    skipped += 1
                else:
                    conn.execute(
                        "INSERT INTO contexts (tier, name, metadata)"
                        " VALUES ('crew', ?, ?)",
                        (display_name, json.dumps({"source_dir": str(member_dir)})),
                    )
                    migrated_crew += 1
                    conn.commit()

    print(
        f"Migrated: {migrated_standards} standards, "
        f"{migrated_objectives} objectives, "
        f"{migrated_crew} crew members. "
        f"Skipped: {skipped} duplicates."
    )


# ---------------------------------------------------------------------------
# Command: heartbeat
# ---------------------------------------------------------------------------

def cmd_heartbeat(args: argparse.Namespace) -> None:
    from praxeology_mcp.daemon import DaemonManager
    dm = DaemonManager()
    db_path = _db_path()

    if args.action == "start":
        result = dm.start(
            target_module="praxeology_mcp.heartbeat",
            target_func="run_daemon",
            name="heartbeat",
            args={"db_path": db_path, "interval": 300},
        )
        print(f"Heartbeat: {result['status']} (PID {result.get('pid', '?')})")
    elif args.action == "stop":
        result = dm.stop("heartbeat")
        print(f"Heartbeat: {result['status']}")
    else:
        print(f"Unknown heartbeat action: {args.action}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Command: daemon
# ---------------------------------------------------------------------------

def cmd_daemon(args: argparse.Namespace) -> None:
    from praxeology_mcp.daemon import DaemonManager
    dm = DaemonManager()
    if args.action == "list":
        daemons = dm.list_all()
        if not daemons:
            print("No daemons registered.")
        else:
            print("Praxeology Daemons")
            print("=" * 40)
            for d in daemons:
                status = "running" if d["running"] else "stopped"
                print(f"  {d['name']}: {status} (PID {d.get('pid', '?')})")
    elif args.action == "stop-all":
        results = dm.stop_all()
        for r in results:
            print(f"  {r['name']}: {r['status']}")


# ---------------------------------------------------------------------------
# Command: config
# ---------------------------------------------------------------------------

def cmd_config(args: argparse.Namespace) -> None:
    from praxeology_mcp.db import get_db, set_config, get_config, init_db
    db_path = _db_path()
    init_db(db_path)
    conn = get_db(db_path)

    if args.list:
        rows = conn.execute("SELECT key, value, updated_at FROM config ORDER BY key").fetchall()
        if not rows:
            print("No configuration set.")
        for row in rows:
            print(f"  {row[0]} = {row[1]}  (updated: {row[2]})")
        return

    if args.discord_webhook:
        import re
        webhook_pattern = re.compile(r"^https://discord\.com/api/webhooks/\d+/.+$")
        if not webhook_pattern.match(args.discord_webhook):
            print("Error: Invalid Discord webhook URL. Expected format: https://discord.com/api/webhooks/{id}/{token}")
            return
        set_config(conn, "discord_webhook", args.discord_webhook)
        # Mask the token portion
        url = args.discord_webhook
        masked = url[:url.rfind("/") + 4] + "***" if "/" in url else url[:20] + "***"
        print(f"Discord webhook set: {masked}")

    if not any([args.discord_webhook, args.list]):
        print("No config option specified. Use --list to see current config, or --discord-webhook URL to set webhook.")


# ---------------------------------------------------------------------------
# Command: dashboard
# ---------------------------------------------------------------------------

def cmd_dashboard(args: argparse.Namespace) -> None:
    from praxeology_mcp.dashboard.app import run_dashboard
    port = getattr(args, "port", 5060)
    print(f"Starting dashboard at http://localhost:{port}")
    run_dashboard(port=port)


# ---------------------------------------------------------------------------
# Command: status
# ---------------------------------------------------------------------------

def cmd_status(args: argparse.Namespace) -> None:
    db_path = _db_path()
    if not Path(db_path).exists():
        print("No Praxeology DB found. Run 'praxeology init' first.")
        return

    from praxeology_mcp.db import get_db
    conn = get_db(db_path)

    tables = [
        "standards", "cases", "gaps", "proposals", "objectives",
        "schedules", "contexts", "reviews", "delegations", "metrics_log",
    ]
    print("Praxeology Status")
    print("=" * 40)
    print(f"DB: {db_path}")
    for t in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  {t}: {count} rows")

    # Heartbeat status
    from praxeology_mcp.daemon import DaemonManager
    dm = DaemonManager()
    hb_status = dm.status("heartbeat")
    if hb_status["running"]:
        print(f"\nHeartbeat: running (PID {hb_status['pid']})")
    elif hb_status.get("stale"):
        print(f"\nHeartbeat: dead (stale PID {hb_status['pid']})")
    else:
        print("\nHeartbeat: not running")

    # Config
    config_rows = conn.execute("SELECT key, value FROM config ORDER BY key").fetchall()
    if config_rows:
        print("\nConfig:")
        for row in config_rows:
            key, value = row[0], row[1]
            # Mask sensitive values
            if "webhook" in key or "token" in key:
                value = value[:30] + "***" if len(value) > 30 else "***"
            print(f"  {key} = {value}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="praxeology_mcp",
        description="Praxeology MCP — project governance scaffold",
    )
    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    # init
    init_parser = subparsers.add_parser("init", help="Scaffold a new Praxeology project")
    init_parser.add_argument("--name", required=True, help="Organization or project name")
    init_parser.add_argument(
        "--agents", type=int, default=0, metavar="N",
        help="Number of agent directories to create (default: 0)",
    )
    init_parser.add_argument(
        "--existing", action="store_true",
        help="Add MCP to an existing project (skip scaffold, only create .mcp.json and migrate DB)",
    )

    # connect
    subparsers.add_parser("connect", help="Connect to an existing Praxeology server")

    # migrate
    migrate_parser = subparsers.add_parser(
        "migrate", help="Import existing Praxeology v1 files into the SQLite DB"
    )
    migrate_parser.add_argument(
        "--project-dir", required=True, metavar="PATH",
        help="Root directory of the Praxeology v1 project to migrate",
    )

    # heartbeat
    heartbeat_parser = subparsers.add_parser(
        "heartbeat", help="Manage the background heartbeat process"
    )
    heartbeat_parser.add_argument(
        "action", choices=["start", "stop"],
        help="Action to perform: start or stop the heartbeat",
    )

    # dashboard
    dashboard_parser = subparsers.add_parser(
        "dashboard", help="Launch the Praxeology web dashboard"
    )
    dashboard_parser.add_argument(
        "--port", type=int, default=5060, metavar="PORT",
        help="Port to run the dashboard on (default: 5060)",
    )

    # status
    subparsers.add_parser("status", help="Show Praxeology DB and heartbeat status")

    # daemon
    daemon_parser = subparsers.add_parser("daemon", help="Manage background daemons")
    daemon_parser.add_argument("action", choices=["list", "stop-all"])

    # config
    config_parser = subparsers.add_parser("config", help="Set configuration values")
    config_parser.add_argument("--discord-webhook", help="Discord webhook URL for heartbeat alerts")
    config_parser.add_argument("--list", action="store_true", help="List all config values")

    parsed = parser.parse_args(argv)

    if parsed.command == "init":
        cmd_init(parsed)
    elif parsed.command == "connect":
        cmd_connect(parsed)
    elif parsed.command == "migrate":
        cmd_migrate(parsed)
    elif parsed.command == "heartbeat":
        cmd_heartbeat(parsed)
    elif parsed.command == "dashboard":
        cmd_dashboard(parsed)
    elif parsed.command == "status":
        cmd_status(parsed)
    elif parsed.command == "daemon":
        cmd_daemon(parsed)
    elif parsed.command == "config":
        cmd_config(parsed)
    else:
        parser.print_help()
        sys.exit(1)
