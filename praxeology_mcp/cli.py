"""
Praxeology MCP — CLI module.

Usage:
    python3 -m praxeology_mcp init --name MyOrg --agents 3
    python3 -m praxeology_mcp connect
"""

from __future__ import annotations

import argparse
import json
import os
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
# Command: onboard
# ---------------------------------------------------------------------------

def _print_progress_tree(space: str = "", channels: list = None, crew: list = None,
                         mission: str = "", rules: list = None, procedures: list = None,
                         goal: str = "", programs: list = None, campaigns: list = None) -> None:
    """Print current onboard progress as hierarchical ASCII tree."""
    print()
    print("  ── Progress ──")

    # ── Logical: STR → DOC → PRC → PLY (nested) ──
    if mission or rules:
        print("  WHY & HOW")
        if mission:
            print(f"    STR-001  {mission}")

        if rules:
            # Build doctrine → procedure → playbook hierarchy
            for di, rule in enumerate(rules):
                code = f"DOC-{di + 1:03d}"
                is_last_doc = di == len(rules) - 1 and not (procedures and any(
                    isinstance(p, dict) and p.get("doctrine") != rule for p in (procedures or [])))
                doc_prefix = "└──" if is_last_doc else "├──"
                print(f"    {doc_prefix} {code}  {rule}")

                # Find procedures under this doctrine
                if procedures:
                    doc_procs = [p for p in procedures if isinstance(p, dict)
                                 and p.get("doctrine") == rule and not p.get("playbook_of")]
                    for pi, proc in enumerate(doc_procs):
                        prc_code = f"PRC-{di + 1}{pi + 1:02d}"
                        indent = "        " if is_last_doc else "    │   "
                        # Find playbooks under this procedure
                        doc_plays = [p for p in procedures if isinstance(p, dict)
                                     and p.get("playbook_of") == proc["name"]]
                        is_last_prc = pi == len(doc_procs) - 1 and not doc_plays
                        prc_prefix = "└──" if is_last_prc else "├──"
                        print(f"{indent}{prc_prefix} {prc_code}  {proc['name']}")

                        for pli, play in enumerate(doc_plays):
                            ply_code = f"PLY-{di + 1}{pi + 1}{pli + 1}"
                            play_indent = indent + ("    " if is_last_prc else "│   ")
                            is_last_ply = pli == len(doc_plays) - 1
                            ply_prefix = "└──" if is_last_ply else "├──"
                            print(f"{play_indent}{ply_prefix} {ply_code}  {play['name']}")

    # ── Contextual: Space → Channel → Thread → Crew ──
    if space:
        print("  WHO & WHERE")
        print(f"    {space} (Space)")
        if channels:
            for ci, ch in enumerate(channels):
                ch_name = ch["name"] if isinstance(ch, dict) else ch
                threads = ch.get("threads", []) if isinstance(ch, dict) else []
                is_last_ch = ci == len(channels) - 1 and not crew
                ch_prefix = "└──" if is_last_ch else "├──"
                print(f"      {ch_prefix} # {ch_name}")
                for ti, th in enumerate(threads):
                    is_last_th = ti == len(threads) - 1
                    th_indent = "          " if is_last_ch else "      │   "
                    th_prefix = "└──" if is_last_th else "├──"
                    print(f"{th_indent}{th_prefix} {th}")
        if crew:
            for i, c in enumerate(crew):
                is_last = i == len(crew) - 1
                prefix = "└──" if is_last else "├──"
                name = c["name"] if isinstance(c, dict) else c
                print(f"      {prefix} @{name}")

    # ── Tactical: Goal → Program → Campaign → Plan ──
    if goal:
        print("  WHAT & WHEN")
        print(f"    {goal} (Goal)")
        if programs:
            for pi, prog in enumerate(programs):
                is_last_prog = pi == len(programs) - 1
                prog_prefix = "└──" if is_last_prog else "├──"
                print(f"      {prog_prefix} {prog} (Program)")
                if campaigns:
                    prog_camps = [c for c in campaigns if c.get("program") == prog]
                    for ci, camp in enumerate(prog_camps):
                        is_last_camp = ci == len(prog_camps) - 1
                        camp_indent = "          " if is_last_prog else "      │   "
                        camp_prefix = "└──" if is_last_camp else "├──"
                        print(f"{camp_indent}{camp_prefix} {camp['name']} (Campaign)")
                        for pli, plan in enumerate(camp.get("plans", [])):
                            is_last_plan = pli == len(camp["plans"]) - 1
                            plan_indent = camp_indent + ("    " if is_last_camp else "│   ")
                            plan_prefix = "└──" if is_last_plan else "├──"
                            print(f"{plan_indent}{plan_prefix} {plan}")

    print()


def _sanitize_name(raw: str) -> str:
    """Remove path traversal characters from a name."""
    return raw.replace("/", "").replace("\\", "").replace("..", "").strip()


_onboard_llm = None  # Set during onboard LLM selection
_onboard_lang = "en"  # Set during onboard language selection


def _detect_backends() -> list[dict]:
    """Detect available LLM backends."""
    backends = []

    # Check Ollama
    try:
        import urllib.request
        resp = urllib.request.urlopen("http://localhost:11434/api/tags", timeout=3)
        data = json.loads(resp.read().decode())
        models = [m["name"] for m in data.get("models", [])]
        if models:
            backends.append({"backend": "ollama", "models": models, "label": f"Ollama (localhost:11434) — {', '.join(models[:5])}"})
    except Exception:
        pass

    # Check Claude API
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if api_key:
        backends.append({"backend": "claude", "models": ["claude-sonnet-4-6", "claude-haiku-4-5-20251001"], "label": "Claude API (key detected)"})

    return backends


def _try_suggest(parent_tier: str, parent_content: str, child_tier: str, count: int = 4) -> list[str]:
    """Call LLM to suggest child tier items. Returns empty list on failure."""
    global _onboard_llm
    if _onboard_llm is None:
        return []
    try:
        lang_instruction = " Respond in Korean." if _onboard_lang == "ko" else ""
        prompt = (
            f'Given this {parent_tier}: "{parent_content}"\n\n'
            f"Suggest exactly {count} concise {child_tier} items for an AI agent governance system. "
            f"Return ONLY a JSON array of {count} strings, nothing else.{lang_instruction}"
        )
        response = _onboard_llm.chat([
            {"role": "system", "content": "You are a governance design assistant. Return only valid JSON arrays."},
            {"role": "user", "content": prompt},
        ])
        content = response.get("content", "")
        start = content.find("[")
        end = content.rfind("]") + 1
        if start >= 0 and end > start:
            import json as _json
            return _json.loads(content[start:end])[:count]
    except Exception:
        pass
    return []


def _suggest_and_select(parent_tier: str, parent_content: str, child_tier: str, label: str) -> list[str]:
    """Suggest items via LLM, let user select + add custom. Returns selected items."""
    global _onboard_llm
    if _onboard_llm is None:
        # No LLM — manual only
        selected: list[str] = []
        print(f"  {label} (enter empty line to finish):")
        n = 1
        while True:
            item = input(f"    {label} {n}: ").strip()
            if not item:
                break
            selected.append(item)
            n += 1
        return selected

    print(f"  Generating {child_tier} suggestions...", end=" ", flush=True)
    suggestions = _try_suggest(parent_tier, parent_content, child_tier)

    if suggestions:
        print("done.")
        print()
        for i, s in enumerate(suggestions, 1):
            print(f"    [{i}] {s}")
        print(f"    [0] Skip suggestions / enter manually")
        print()
        sel = input(f"  Select (e.g. 1,3 or 0 for manual): ").strip()

        selected = []
        if sel != "0":
            for part in sel.split(","):
                part = part.strip()
                if part.isdigit() and 1 <= int(part) <= len(suggestions):
                    selected.append(suggestions[int(part) - 1])
    else:
        print("failed. Manual input.")
        selected = []

    # Always allow adding more manually
    print(f"  Add more {label} (enter empty line to finish):")
    n = len(selected) + 1
    while True:
        item = input(f"    {label} {n}: ").strip()
        if not item:
            break
        selected.append(item)
        n += 1

    return selected


def cmd_onboard(_args: argparse.Namespace) -> None:
    """Interactive 3-phase setup wizard with LLM-assisted forward prediction."""
    global _onboard_llm
    try:
        print()
        print("  Praxeology — Onboard Wizard")
        print("  ============================")
        print()

        # ── 1. Language selection (first) ──
        print("  Language / 언어:")
        print("    [1] English")
        print("    [2] 한국어")
        lang_choice = input("  Select [1]: ").strip() or "1"
        _onboard_lang = "ko" if lang_choice == "2" else "en"
        print()

        # ── 2. LLM backend selection ──
        print("  Detecting available LLM backends...")
        backends = _detect_backends()

        if backends:
            for i, b in enumerate(backends, 1):
                print(f"    [{i}] {b['label']}")
            print(f"    [{len(backends) + 1}] No LLM — manual input only")
            print()
            choice = input(f"  Select backend [1]: ").strip() or "1"

            if choice.isdigit() and 1 <= int(choice) <= len(backends):
                selected_backend = backends[int(choice) - 1]
                models = selected_backend["models"]
                print()
                for i, m in enumerate(models, 1):
                    print(f"    [{i}] {m}")
                model_choice = input(f"  Select model [1]: ").strip() or "1"
                if model_choice.isdigit() and 1 <= int(model_choice) <= len(models):
                    model_name = models[int(model_choice) - 1]
                else:
                    model_name = models[0]

                from praxeology_mcp.agent_runner import LLMClient
                _onboard_llm = LLMClient(
                    model=model_name,
                    backend=selected_backend["backend"],
                )
                print(f"\n  Using: {selected_backend['backend']} / {model_name}")
            else:
                _onboard_llm = None
                print("\n  Manual input mode.")
        else:
            print("    No LLM backends detected. Manual input mode.")
            _onboard_llm = None
        print()

        org_name = input("  Organization name: ").strip()
        if not org_name:
            print("  Organization name cannot be empty.")
            sys.exit(1)

        # ══════════════════════════════════════════════════════════════
        # Phase 1: WHY & HOW (Logical)
        # ══════════════════════════════════════════════════════════════
        print()
        print("  ── Phase 1/3: Why & How (Logical) ──")
        print()

        mission = input("  Strategy (mission/vision): ").strip()
        print()

        # LLM-assisted tree: Strategy → Doctrines
        if mission:
            rules = _suggest_and_select("strategy", mission, "doctrine rule", "Rule")
        else:
            rules = []
            print("  Doctrine rules (enter empty line to finish):")
            n = 1
            while True:
                rule = input(f"    Rule {n}: ").strip()
                if not rule:
                    break
                rules.append(rule)
                n += 1
        print()

        # Tree: each Doctrine → Procedures for that doctrine
        procedures: list[dict] = []  # [{"name": str, "doctrine": str}]
        for rule in rules:
            rule_ctx = f"Strategy: {mission}. Doctrine: {rule}"
            print(f"  Procedures for doctrine: '{rule[:60]}'")
            procs = _suggest_and_select("doctrine", rule_ctx, "procedure", "Procedure")
            for p in procs:
                procedures.append({"name": p, "doctrine": rule})

            # Tree: each Procedure → Playbooks for that procedure
            for proc in procs:
                proc_ctx = f"Strategy: {mission}. Doctrine: {rule}. Procedure: {proc}"
                print(f"    Playbooks for procedure: '{proc[:50]}'")
                playbooks = _suggest_and_select("procedure", proc_ctx, "playbook (concrete how-to)", "Playbook")
                for pb in playbooks:
                    procedures.append({"name": pb, "doctrine": rule, "playbook_of": proc})
        print()

        # ══════════════════════════════════════════════════════════════
        # Phase 2: WHO & WHERE (Contextual)
        # ══════════════════════════════════════════════════════════════
        _print_progress_tree(mission=mission, rules=rules, procedures=procedures)
        print("  ── Phase 2/3: Who & Where (Contextual) ──")
        print()

        space_name = input(f"  Space name [{org_name}]: ").strip() or org_name
        print()

        # LLM-assisted: Space+Strategy → Channel suggestions
        space_ctx = f"Organization: {space_name}. Strategy: {mission}"
        ch_suggestions = _suggest_and_select("organization", space_ctx, "department/channel name", "Channel")

        channels: list[dict] = []
        for ch_name in ch_suggestions:
            # Show progress tree with current channel highlighted
            _print_progress_tree(
                mission=mission, rules=rules, procedures=procedures,
                space=space_name,
                channels=channels + [{"name": ch_name, "threads": ["(selecting...)"]}],
            )
            # LLM-assisted: Channel → Thread suggestions (with explicit channel context)
            th_ctx = f"Organization: {space_name}. Channel: '{ch_name}'. Strategy: {mission}. Suggest threads/topics specifically for the '{ch_name}' channel."
            th_suggestions = _suggest_and_select(
                f"channel named '{ch_name}'", th_ctx, f"thread/topic for '{ch_name}'", "Thread"
            )
            channels.append({"name": ch_name, "threads": th_suggestions})

        # Show completed contextual tree
        _print_progress_tree(mission=mission, rules=rules, procedures=procedures,
                             space=space_name, channels=channels)
        print()

        # LLM-assisted: Organization context → Crew role suggestions
        crew_ctx = f"Organization: {space_name}. Strategy: {mission}. Channels: {', '.join(c['name'] for c in channels)}"
        print("  Generating crew role suggestions...", end=" ", flush=True)
        crew_suggestions = _try_suggest("organization with channels", crew_ctx, "agent role (format: Name / Role / Department)")

        if crew_suggestions:
            print("done.")
            for i, s in enumerate(crew_suggestions, 1):
                print(f"    [{i}] {s}")
            print(f"    [0] Skip suggestions / enter manually")
            print()
            sel = input("  Select roles to create (e.g. 1,3 or 0): ").strip()
        else:
            print("LLM not available.")
            sel = "0"

        crew_members: list[dict] = []

        # Add selected suggestions
        if sel != "0" and crew_suggestions:
            for part in sel.split(","):
                part = part.strip()
                if part.isdigit() and 1 <= int(part) <= len(crew_suggestions):
                    suggested = crew_suggestions[int(part) - 1]
                    # Parse "Name / Role / Department" format
                    parts = [p.strip() for p in suggested.split("/")]
                    name = _sanitize_name(parts[0]) if len(parts) > 0 else ""
                    role = parts[1] if len(parts) > 1 else ""
                    dept = parts[2] if len(parts) > 2 else ""
                    if name:
                        persona = input(f"    Persona for {name}: ").strip()
                        ch_assign = ""
                        if channels:
                            ch_names = ", ".join(ch["name"] for ch in channels)
                            ch_assign = input(f"    Channel for {name} [{ch_names}]: ").strip()
                        crew_members.append({
                            "name": name, "role": role, "department": dept,
                            "persona": persona, "channel": ch_assign,
                        })

        # Always allow adding more manually
        print("  Add more crew (enter empty name to finish):")
        n = len(crew_members) + 1
        while True:
            print(f"  Crew {n}:")
            raw_name = input("    Name: ").strip()
            name = _sanitize_name(raw_name)
            if not name:
                break
            role = input("    Role: ").strip()
            department = input("    Department: ").strip()
            persona = input("    Persona: ").strip()
            if channels:
                ch_names = ", ".join(ch["name"] for ch in channels)
                channel = input(f"    Channel [{ch_names}]: ").strip()
            else:
                channel = ""
            crew_members.append({
                "name": name, "role": role, "department": department,
                "persona": persona, "channel": channel,
            })
            n += 1
            print()

        if not crew_members:
            print("  At least 1 crew member is required.")
            sys.exit(1)

        # ══════════════════════════════════════════════════════════════
        # Phase 3: WHAT & WHEN (Tactical)
        # ══════════════════════════════════════════════════════════════
        _print_progress_tree(mission=mission, rules=rules, procedures=procedures,
                             space=space_name, channels=channels, crew=crew_members)
        sys.stdout.flush()
        print()
        print("  ══════════════════════════════════════════")
        print("  ── Phase 3/3: What & When (Tactical) ──")
        print("  ══════════════════════════════════════════")
        print()
        sys.stdout.flush()

        goal = input("  Goal (long-term objective): ").strip()
        print()

        # LLM-assisted: Goal → Program suggestions
        if goal:
            programs = _suggest_and_select("goal", goal, "program (major initiative)", "Program")
        else:
            programs = []
        print()

        # LLM-assisted: Programs → Campaign suggestions (per program)
        campaigns: list[dict] = []  # [{"name": str, "program": str, "plans": [str]}]
        for prog in programs:
            prog_ctx = f"Goal: {goal}. Program: {prog}"
            camp_names = _suggest_and_select("program", prog_ctx, "campaign (quarterly initiative)", "Campaign")
            for camp in camp_names:
                # LLM-assisted: Campaign → Plan suggestions
                camp_ctx = f"Goal: {goal}. Program: {prog}. Campaign: {camp}"
                plans = _suggest_and_select("campaign", camp_ctx, "plan (sprint/weekly plan)", "Plan")
                campaigns.append({"name": camp, "program": prog, "plans": plans})
        print()

        # If no programs, allow direct plan input
        if not programs:
            plan = input("  Plan (short-term plan): ").strip()
            plans_flat = [plan] if plan else []
        else:
            plans_flat = []  # plans are inside campaigns

        # Work items are NOT collected — what_now() will generate them
        print("  (Work items will be auto-generated by what_now() from Plans.)")
        print()

        # ══════════════════════════════════════════════════════════════
        # Generate files + DB
        # ══════════════════════════════════════════════════════════════
        print("  Generating...")
        cwd = Path.cwd()

        # Files: CLAUDE.md, _crew/, _standard/, .mcp.json
        root_claude = cwd / "CLAUDE.md"
        root_claude.write_text(_ROOT_CLAUDE_MD.format(name=org_name), encoding="utf-8")
        print("    + CLAUDE.md")

        crew_dir = cwd / "_crew"
        crew_dir.mkdir(exist_ok=True)
        crew_claude = crew_dir / "CLAUDE.md"
        crew_claude.write_text(_CREW_CLAUDE_MD.format(name=org_name), encoding="utf-8")
        print("    + _crew/CLAUDE.md")

        for idx, member in enumerate(crew_members, start=1):
            member_dir = crew_dir / member["name"].lower()
            member_dir.mkdir(exist_ok=True)
            content = _AGENT_CLAUDE_MD.format(agent_name=member["name"], agent_num=idx)
            content = content.replace(
                "- Role: [Define role here]", f"- Role: {member['role']}",
            ).replace(
                "- Department: [Define department here]", f"- Department: {member['department']}",
            ).replace(
                "[Describe the agent's personality and working style here.]", member["persona"],
            )
            (member_dir / "CLAUDE.md").write_text(content, encoding="utf-8")
            print(f"    + _crew/{member['name'].lower()}/CLAUDE.md")

        standard_dir = cwd / "_standard"
        standard_dir.mkdir(exist_ok=True)
        print("    + _standard/")

        mcp_json_path = cwd / ".mcp.json"
        mcp_json_path.write_text(
            json.dumps(_build_mcp_json(cwd), indent=2) + "\n", encoding="utf-8"
        )
        print("    + .mcp.json")

        # DB
        db_dir = Path.home() / ".claude" / "praxeology"
        db_dir.mkdir(parents=True, exist_ok=True)
        db_path = db_dir / "praxeology.db"

        from praxeology_mcp.db import init_db
        conn = init_db(str(db_path))

        counts = {"standards": 0, "objectives": 0, "contexts": 0}

        # ── Logical axis ──
        if mission:
            conn.execute(
                "INSERT INTO standards (tier, department, code, title, content) VALUES (?, ?, ?, ?, ?)",
                ("strategy", "org", "STR-001", f"{org_name} — Strategy", mission),
            )
            counts["standards"] += 1

        for i, rule in enumerate(rules, 1):
            conn.execute(
                "INSERT INTO standards (tier, department, code, title, content) VALUES (?, ?, ?, ?, ?)",
                ("doctrine", "org", f"DOC-{i:03d}", f"Doctrine {i}", rule),
            )
            counts["standards"] += 1

        prc_n = 0
        ply_n = 0
        for proc in procedures:
            if isinstance(proc, dict):
                if proc.get("playbook_of"):
                    ply_n += 1
                    conn.execute(
                        "INSERT INTO standards (tier, department, code, title, content) VALUES (?, ?, ?, ?, ?)",
                        ("playbook", "org", f"PLY-{ply_n:03d}", proc["name"],
                         f"Playbook for procedure: {proc.get('playbook_of', '')}"),
                    )
                else:
                    prc_n += 1
                    conn.execute(
                        "INSERT INTO standards (tier, department, code, title, content) VALUES (?, ?, ?, ?, ?)",
                        ("procedure", "org", f"PRC-{prc_n:03d}", proc["name"],
                         f"Under doctrine: {proc.get('doctrine', '')}"),
                    )
            else:
                prc_n += 1
                conn.execute(
                    "INSERT INTO standards (tier, department, code, title, content) VALUES (?, ?, ?, ?, ?)",
                    ("procedure", "org", f"PRC-{prc_n:03d}", f"Procedure {prc_n}", proc),
                )
            counts["standards"] += 1

        conn.commit()

        # ── Contextual axis ──
        # Space
        cur = conn.execute(
            "INSERT INTO contexts (tier, name, metadata) VALUES ('space', ?, ?)",
            (space_name, json.dumps({"org": org_name})),
        )
        space_id = cur.lastrowid
        counts["contexts"] += 1

        # Channels + Threads
        channel_id_map: dict[str, int] = {}
        for ch in channels:
            cur = conn.execute(
                "INSERT INTO contexts (tier, parent_id, name) VALUES ('channel', ?, ?)",
                (space_id, ch["name"]),
            )
            ch_id = cur.lastrowid
            channel_id_map[ch["name"]] = ch_id
            counts["contexts"] += 1

            for th_name in ch["threads"]:
                conn.execute(
                    "INSERT INTO contexts (tier, parent_id, name) VALUES ('thread', ?, ?)",
                    (ch_id, th_name),
                )
                counts["contexts"] += 1

        # Crew
        for member in crew_members:
            parent_id = channel_id_map.get(member.get("channel", ""), space_id)
            conn.execute(
                "INSERT INTO contexts (tier, parent_id, name, metadata) VALUES ('crew', ?, ?, ?)",
                (parent_id, member["name"], json.dumps({
                    "role": member["role"], "department": member["department"],
                    "source_dir": str(crew_dir / member["name"].lower()),
                })),
            )
            counts["contexts"] += 1

        conn.commit()

        # ── Tactical axis (Goal → Program → Campaign → Plan) ──
        goal_id = None
        if goal:
            cur = conn.execute(
                "INSERT INTO objectives (tier, title, description) VALUES ('goal', ?, ?)",
                (f"{org_name} — Goal", goal),
            )
            goal_id = cur.lastrowid
            counts["objectives"] += 1

        # Programs → Campaigns → Plans (from LLM-assisted input)
        for prog_name in programs:
            cur = conn.execute(
                "INSERT INTO objectives (tier, parent_id, title) VALUES ('program', ?, ?)",
                (goal_id, prog_name),
            )
            prog_id = cur.lastrowid
            counts["objectives"] += 1

            for camp in campaigns:
                if camp["program"] == prog_name:
                    cur = conn.execute(
                        "INSERT INTO objectives (tier, parent_id, title) VALUES ('campaign', ?, ?)",
                        (prog_id, camp["name"]),
                    )
                    camp_id = cur.lastrowid
                    counts["objectives"] += 1

                    for plan_name in camp["plans"]:
                        conn.execute(
                            "INSERT INTO objectives (tier, parent_id, title) VALUES ('plan', ?, ?)",
                            (camp_id, plan_name),
                        )
                        counts["objectives"] += 1

        # Fallback: direct plan input (if no programs)
        if not programs and plans_flat:
            for p in plans_flat:
                conn.execute(
                    "INSERT INTO objectives (tier, parent_id, title) VALUES ('plan', ?, ?)",
                    (goal_id, p),
                )
                counts["objectives"] += 1

        conn.commit()

        print(
            f"    + Database initialized "
            f"({counts['standards']} standards, {counts['contexts']} contexts, "
            f"{counts['objectives']} objectives)"
        )
        print()
        print("  Onboard complete! Run 'praxeology start' to begin.")
        print()

    except KeyboardInterrupt:
        print()
        print("Onboard cancelled.")
        sys.exit(0)


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


_DEFAULT_DB = str(Path.home() / ".claude" / "praxeology" / "praxeology.db")


def _db_path() -> str:
    return os.environ.get("PRAXEOLOGY_DB", _DEFAULT_DB)


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
    port = getattr(args, "port", 5160)
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
# Command: start (agent daemons)
# ---------------------------------------------------------------------------

def cmd_start(args: argparse.Namespace) -> None:
    from praxeology_mcp.daemon import DaemonManager
    from praxeology_mcp.db import get_db, init_db

    dm = DaemonManager()
    db_path = _db_path()
    init_db(db_path)
    conn = get_db(db_path)

    backend = getattr(args, "backend", "ollama")
    model = getattr(args, "model", "qwen3:14b")
    interval = getattr(args, "interval", 60)
    base_url = getattr(args, "base_url", None)
    crew_filter = getattr(args, "crew", None)

    if crew_filter:
        # Start a single crew member
        crew_names = [crew_filter]
    else:
        # Start all registered crew from DB
        rows = conn.execute(
            "SELECT name FROM contexts WHERE tier = 'crew' ORDER BY name"
        ).fetchall()
        if not rows:
            print("No crew members registered. Run 'praxeology onboard' or 'praxeology migrate' first.")
            return
        crew_names = [r["name"] for r in rows]

    print(f"Starting {len(crew_names)} agent(s) — model={model} backend={backend}")

    # Start heartbeat if not running
    hb_status = dm.status("heartbeat")
    if not hb_status.get("running"):
        hb_result = dm.start(
            target_module="praxeology_mcp.heartbeat",
            target_func="run_daemon",
            name="heartbeat",
            args={"db_path": db_path, "interval": 300},
        )
        print(f"  heartbeat: {hb_result['status']} (PID {hb_result.get('pid', '?')})")

    for crew_name in crew_names:
        daemon_name = f"agent-{crew_name.lower().replace(' ', '-')}"
        agent_args = {
            "crew_id": crew_name,
            "model": model,
            "db_path": db_path,
            "backend": backend,
            "interval": interval,
        }
        if base_url:
            agent_args["base_url"] = base_url

        result = dm.start(
            target_module="praxeology_mcp.agent_runner",
            target_func="run_agent",
            name=daemon_name,
            args=agent_args,
        )
        print(f"  {crew_name}: {result['status']} (PID {result.get('pid', '?')})")

    print(f"\nAll agents started. Use 'praxeology dashboard' to monitor.")


# ---------------------------------------------------------------------------
# Command: stop (agent daemons)
# ---------------------------------------------------------------------------

def cmd_stop(args: argparse.Namespace) -> None:
    from praxeology_mcp.daemon import DaemonManager

    dm = DaemonManager()
    crew_filter = getattr(args, "crew", None)
    stop_all = getattr(args, "stop_all", False)

    if stop_all:
        results = dm.stop_all()
        if not results:
            print("No daemons running.")
        for r in results:
            print(f"  {r['name']}: {r['status']}")
        return

    if crew_filter:
        daemon_name = f"agent-{crew_filter.lower().replace(' ', '-')}"
        result = dm.stop(daemon_name)
        print(f"  {crew_filter}: {result['status']}")
        return

    # Stop all agent-* daemons but keep heartbeat
    daemons = dm.list_all()
    agent_daemons = [d for d in daemons if d["name"].startswith("agent-")]
    if not agent_daemons:
        print("No agent daemons running.")
        return

    for d in agent_daemons:
        result = dm.stop(d["name"])
        print(f"  {d['name']}: {result['status']}")


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
        "--port", type=int, default=5160, metavar="PORT",
        help="Port to run the dashboard on (default: 5160)",
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

    # onboard
    subparsers.add_parser("onboard", help="Interactive setup wizard for new organization")

    # start
    start_parser = subparsers.add_parser("start", help="Start agent daemons")
    start_parser.add_argument("--crew", metavar="NAME", help="Start a specific crew member (default: all)")
    start_parser.add_argument("--model", default="qwen3:14b", help="LLM model (default: qwen3:14b)")
    start_parser.add_argument("--backend", default="ollama", choices=["ollama", "claude"], help="LLM backend")
    start_parser.add_argument("--interval", type=int, default=60, help="Seconds between ticks (default: 60)")
    start_parser.add_argument("--base-url", default=None, help="LLM API base URL override")

    # stop
    stop_parser = subparsers.add_parser("stop", help="Stop agent daemons")
    stop_parser.add_argument("--crew", metavar="NAME", help="Stop a specific crew member")
    stop_parser.add_argument("--all", action="store_true", dest="stop_all", help="Stop all agents + heartbeat")

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
    elif parsed.command == "onboard":
        cmd_onboard(parsed)
    elif parsed.command == "start":
        cmd_start(parsed)
    elif parsed.command == "stop":
        cmd_stop(parsed)
    else:
        parser.print_help()
        sys.exit(1)
