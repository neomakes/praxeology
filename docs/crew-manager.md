# Crew Manager

Web dashboard for monitoring and managing NeoMakes AI agent sessions. Provides real-time session state, task visibility, permission approval, and activity history for all 9 crew members.

---

## Overview

Each crew member runs as a Claude Code session inside a `tmux` window, connected to Discord via the claude-plugins channel system. Crew Manager polls these tmux panes continuously and exposes a browser UI at `http://localhost:8765`.

**Dependencies:** Python 3.9+, `tmux`, Claude Code CLI (`claude`), Discord plugin configured per crew.

---

## How to Run

```bash
python3 _admin/crew-manager.py
```

Opens at `http://localhost:8765`. No arguments needed for normal use.

Sessions are started/stopped from the UI or via the API. The process itself does not need to stay in a terminal — run it in a tmux session or as a background process if preferred.

---

## Features

### Session State Monitoring

Each crew card shows one of four states derived by inspecting the last lines of the tmux pane output:

| State | Indicator |
|---|---|
| `working` | Active token counter with `…`, spinner chars (`⠋⠙⠹…`), or `Running` in output |
| `idle` | `❯` prompt visible, or `✻` completion marker present |
| `permission_pending` | `Do you want to…` or `Permission` prompt detected |
| `offline` | tmux session not running |

Detection order (highest priority first):

1. Token counter + `…` = generating output
2. Spinner characters = tool executing
3. `Running` keyword = bash/tool active
4. `❯` prompt = waiting for input
5. `✻` marker = task just completed
6. `| thinking |` without prompt/marker = still generating

### Todo Toggle

Each crew card renders their `todo.json` task list. Tasks can be checked off directly from the dashboard without opening a terminal.

- Clicking a checkbox sends `POST /api/todo/{name}/{id}/toggle`
- The status cycles between `pending` and `done`
- Changes write back to `_crew/{name}/todo.json` immediately

### Permission Approval

When a Claude Code session hits a tool-use permission prompt, the dashboard surfaces it as an alert banner on that crew's card. The banner shows:

- A one-line risk summary (e.g. `🟡 파일 수정: src/index.ts`, `🔴 터미널 명령: rm -rf ...`)
- Risk level color: green (low), yellow (medium), red (high — `rm -rf`, `--force`, `.env` files, etc.)
- **Yes / No / Dismiss** buttons

Approval sends the corresponding arrow-key + Enter sequence to the tmux session. Dismiss hides the banner without responding (the session stays blocked until manually handled).

High-risk patterns flagged automatically: `rm -rf`, `rm -r`, `DROP`, `reset --hard`, `--force`, paths containing `.env`, `credentials`, `.ssh`.

### Activity Streak

Each crew detail view shows a 7-day activity bar (GitHub contribution style). Activity is measured in session minutes extracted from the OMC status bar (`session:NNm`). Four intensity levels:

| Level | Threshold |
|---|---|
| 0 (none) | 0 minutes |
| 1 (low) | ≤ 33% of weekly peak |
| 2 (medium) | ≤ 66% of weekly peak |
| 3 (high) | > 66% of weekly peak |

Data is persisted to `_admin/token_log.json` and updated on each status poll.

### Session Restore

Starting a crew with the **Resume** option passes `--continue` to Claude Code, which reloads the previous conversation context. This is equivalent to running:

```bash
cd _crew/{name} && claude --continue --channels plugin:discord@claude-plugins-official
```

Use Resume after a planned shutdown where the crew saved context to `todo.json` notes. Use Start (no flag) for a fresh session.

---

## API Endpoints

### GET

| Endpoint | Description |
|---|---|
| `GET /api/status` | All crew statuses (name, online, state, ctx%, wk%, time%) |
| `GET /api/permissions` | Pending permission prompts across all running sessions |
| `GET /api/reports/daily` | Whether each crew submitted yesterday's daily report |
| `GET /api/crew/{name}/detail` | Full detail for one crew: status, todo, weekly, streak, report |
| `GET /api/token-summary` | Aggregated session activity from token_log.json |

### POST

| Endpoint | Description |
|---|---|
| `POST /api/start/{name}` | Start a crew session (fresh) |
| `POST /api/stop/{name}` | Kill a crew's tmux session immediately |
| `POST /api/restart/{name}` | Stop then start a crew session |
| `POST /api/start-all` | Start all 9 crews (fresh) |
| `POST /api/resume-all` | Start all 9 crews with `--continue` |
| `POST /api/restart-all` | Restart all running sessions |
| `POST /api/stop-all` | Kill all crew sessions |
| `POST /api/graceful-stop/{name}` | Send context-save prompt, then stop after acknowledgement |
| `POST /api/graceful-stop-all` | Graceful stop for all running sessions |
| `POST /api/permission/{name}` | Respond to permission prompt. Body: `{"choice": "1"}` (1=Yes, 2=No, 3=other) |
| `POST /api/todo/{name}/{id}/toggle` | Toggle a todo item status between `pending` and `done` |
| `POST /api/backup-crew` | Backup crew state files to a timestamped archive |

---

## Integration with Claude Code Sessions

Each session is launched in a tmux window named `crew_{name}` (e.g. `crew_zoro`). The dashboard interacts with sessions exclusively through:

1. **tmux capture-pane** — read last N lines of terminal output for state detection
2. **tmux send-keys** — inject keystrokes for permission responses and graceful-stop prompts

The OMC status bar embedded in each Claude Code session provides structured data the dashboard parses:

```
[OMC#version] | time:N%(remaining) wk:N%(remaining) | mode | session:NNm | ctx:N% | tools
```

Parsed fields: `ctx:N%` (context usage), `wk:N%` (weekly budget), `session:NNm` (session duration).

Session state files (Discord plugin config, `.env` token) live under `~/.claude/channels/discord-{name}/`. The crew working directories are under `_crew/{name}/`.

---

## UI Layout

```
┌─────────────────────────────────────────────────────────────┐
│  NeoMakes Crew Manager                          [Start All] │
│                                                             │
│  [Permission Alert: 조로 — 🟡 파일 수정: src/x.ts] [Y][N][x] │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ 조로  working │  │ 나미  idle   │  │ 우솝  offline│      │
│  │ COO   ctx:42%│  │ CFO   ctx:8% │  │ CTO          │      │
│  │ ☑ task 1     │  │ ☐ task 1     │  │  [Start]     │      │
│  │ ☐ task 2     │  │ ☑ task 2     │  └──────────────┘      │
│  │ ▪▪▪░░░░ (streak)│  │ ░▪▪▪▪▪▪ │                          │
│  └──────────────┘  └──────────────┘                        │
└─────────────────────────────────────────────────────────────┘
```

Each crew card shows: display name, role, live status badge, context/weekly/time budget percentages, todo checklist, and 7-day activity streak.
