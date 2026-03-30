# Praxeology CLI Reference

Complete command reference for the `praxeology` CLI.

---

## Getting Started

### `praxeology onboard`

Interactive wizard that designs your organization from scratch.

**7-step process:**
1. Organization name
2. Number of crew members
3. Each crew member: name, role, department, persona
4. Mission statement (Strategy)
5. Core doctrine rules (what agents must never violate)
6. Primary goal
7. Initial work items

**Generates:**
- `CLAUDE.md` — root context with mission and governance rules
- `_crew/CLAUDE.md` — shared crew rules
- `_crew/{name}/CLAUDE.md` — per-agent persona and role definition
- `_standard/{dept}/` — department directories
- `.mcp.json` — MCP server configuration (with venv Python path)
- Database entries: standards, objectives, contexts

```bash
praxeology onboard
```

### `praxeology start`

Start agents as independent daemon processes. Each agent runs its own `what_now() → LLM → tool execution → backprop()` loop.

```bash
praxeology start                                     # Start all registered crew
praxeology start --crew builder                      # Start one agent
praxeology start --crew builder --model qwen3:14b    # Specify LLM backbone
praxeology start --crew reviewer --model claude-opus-4-6 --backend claude  # Use Claude API
praxeology start --crew analyst --interval 120       # Custom tick interval (seconds)
```

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--crew NAME` | (all) | Start specific agent only |
| `--model MODEL` | `qwen3:14b` | LLM model name |
| `--backend {ollama,claude}` | `ollama` | LLM backend provider |
| `--interval SECONDS` | `60` | Seconds between work ticks |
| `--base-url URL` | (auto) | Override LLM API endpoint |

When starting all agents, sentinel (safety-net monitor) starts automatically.

### `praxeology stop`

Stop running agent daemons.

```bash
praxeology stop                    # Stop all agents (sentinel remains as safety net)
praxeology stop --crew builder     # Stop one agent
praxeology stop --all              # Stop everything including sentinel
```

### `praxeology dashboard`

Launch the web monitoring dashboard.

```bash
praxeology dashboard               # Default: localhost:5060
praxeology dashboard --port 8080   # Custom port
```

**Tabs:**
- **Doctrine** — governance standards (Strategy, Doctrine, Procedure, Playbook)
- **Objectives** — goal hierarchy (Goal → Program → Campaign → Plan → Work)
- **Crew** — performance reviews and delegations
- **Metrics** — tool usage, token cost, latency aggregates
- **Gaps** — detected governance gaps and amendment proposals
- **Backprop** — execution history with surprise scores
- **Heartbeat** — sentinel monitoring logs

---

## Management

### `praxeology status`

Show current system state in the terminal.

```bash
praxeology status
```

**Output includes:**
- Database path and row counts for all 11 tables
- Each agent's state (running/stopped) with PID
- Sentinel state
- Configuration values (sensitive values masked)

### `praxeology migrate`

Import existing markdown and JSON files into the governance database.

```bash
praxeology migrate --project-dir .
```

**Imports:**
- `_standard/**/*.md` → `standards` table
- `todo.json` / `weekly.json` → `objectives` table
- `_crew/*/CLAUDE.md` → `contexts` table (crew tier)

Idempotent — safe to run multiple times. Duplicates are skipped.

### `praxeology config`

Manage system configuration.

```bash
praxeology config --discord-webhook URL     # Set Discord webhook for sentinel alerts
praxeology config --default-model MODEL     # Set default LLM model for all agents
praxeology config --list                    # Show all config values (tokens masked)
```

Discord webhook URLs are validated against `https://discord.com/api/webhooks/{id}/{token}` format. Tokens are masked in all CLI output.

### `praxeology sentinel`

Manage the sentinel — a lightweight safety-net daemon that monitors the database when all agents are stopped.

```bash
praxeology sentinel start       # Start sentinel manually
praxeology sentinel stop        # Stop sentinel
praxeology sentinel status      # Check sentinel state
```

The sentinel runs a 2-tier check every 5 minutes:
- **Tier 1 (rule-based, cost=0):** Counts pending work, overdue schedules, high-frequency gaps, unread delegations
- **Tier 2 (conditional):** If priority score >= 5, creates a work objective and sends Discord alert

When agents are running, they handle these checks via `what_now()`. The sentinel is only needed as a safety net when agents are stopped.

---

## Advanced

### `praxeology agent`

Manage individual agent daemons.

```bash
praxeology agent list                       # Show all registered agents with status/PID/model
praxeology agent logs --crew builder        # View recent activity log
praxeology agent logs --crew builder --follow  # Real-time log (tail -f)
```

### `praxeology db`

Database management utilities.

```bash
praxeology db export --output backup.sql    # Export database backup
praxeology db reset                         # Reset database (destructive — requires confirmation)
```
