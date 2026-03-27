# Claude Code Setup for Praxeology

This guide explains how to configure Claude Code so each agent runs inside the full Praxeology governance stack — automatically, without manual prompt engineering.

---

## 1. CLAUDE.md Hierarchy Loading Order

Claude Code scans upward from the working directory to the filesystem root and loads every `CLAUDE.md` it finds, in order from outermost (lowest specificity) to innermost (highest specificity). Praxeology uses this mechanism as its governance delivery channel.

### Loading order for a typical agent session

```
~/.claude/CLAUDE.md                    ← 1. Global user instructions (tools, OMC config)
/workspace/CLAUDE.md                   ← 2. Organization-level strategy and hard constraints
/workspace/_crew/CLAUDE.md             ← 3. Shared crew rules (universal standards)
/workspace/_crew/{agent}/CLAUDE.md     ← 4. Individual agent identity, role, SOP references
```

Each level is loaded automatically when the agent's working directory is inside that path. No manual prompt injection is needed.

### What belongs at each level

**`~/.claude/CLAUDE.md` — user global**
Tool configuration, MCP server declarations, model routing defaults, OMC orchestration rules. This is the principal's environment, not the agent's.

**`/workspace/CLAUDE.md` — organization root**
Mission, hard constraints (`NEVER` / `ALWAYS`), SafetyGate, ConstitutionalGuard, escalation policy. Applies to every agent in the org unconditionally.

```markdown
# [Org Name] — Governing Strategy

## Hard Constraints
- NEVER take destructive actions without explicit approval
- ALWAYS report blockers within 15 minutes

## SafetyGate
Before every action: verify against this Strategy.
If violation detected: HALT, log, escalate to principal.
```

**`/workspace/_crew/CLAUDE.md` — shared crew rules**
Universal standards (the "12 mandatory" set), session lifecycle (PRC-201), budget policy (PLY-301), escalation format, Discord/Telegram mention rules, weekly.json / todo.json schema.

**`/workspace/_crew/{agent}/CLAUDE.md` — individual agent**
Agent identity, persona, communication style, anti-patterns, project access rights, Standard references specific to that role. This is what makes each instance a distinct agent rather than a generic assistant.

### Scoping is automatic

An agent working in `/workspace/_crew/zoro/` loads all four levels above. An agent working in `/workspace/_crew/usopp/` loads the same three upper levels but sees `usopp/CLAUDE.md` at the bottom — never zoro's. Governance is scoped by filesystem location alone.

---

## 2. `.claude/` Directory Structure

```
/workspace/.claude/
├── settings.json           # Shared project permissions and environment variables
├── settings.local.json     # Local machine overrides (not committed to git)
└── projects/               # Per-project memory (auto-managed by Claude Code)
    └── {hashed-path}/
        └── memory/
            └── MEMORY.md

~/.claude/
├── CLAUDE.md               # Global user instructions
├── settings.json           # User-level tool permissions
└── projects/               # Cross-project memory index
```

### `settings.json` — permissions and environment

```json
{
  "permissions": {
    "allow": [
      "Bash(git:*)",
      "Bash(npm:*)",
      "Bash(python:*)",
      "Read(*)",
      "Edit(*)",
      "Write(*)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(sudo:*)"
    ]
  },
  "env": {
    "NODE_ENV": "development",
    "WORKSPACE_ROOT": "/workspace"
  }
}
```

### `settings.local.json` — local overrides

Not committed. Use for secrets, local paths, per-machine tool unlocks.

```json
{
  "env": {
    "DISCORD_BOT_TOKEN": "...",
    "TELEGRAM_BOT_TOKEN": "...",
    "NOTION_TOKEN": "..."
  }
}
```

---

## 3. MCP Server Configuration

MCP servers are declared in `~/.claude/CLAUDE.md` (or `settings.json`) and become available to every Claude Code session on that machine. Each agent inherits them automatically.

### Full configuration example

```json
{
  "mcpServers": {
    "discord": {
      "command": "npx",
      "args": ["-y", "@neomakes/mcp-discord"],
      "env": {
        "DISCORD_BOT_TOKEN": "${DISCORD_BOT_TOKEN}",
        "DISCORD_GUILD_ID": "${DISCORD_GUILD_ID}"
      }
    },
    "telegram": {
      "command": "npx",
      "args": ["-y", "@neomakes/mcp-telegram"],
      "env": {
        "TELEGRAM_BOT_TOKEN": "${TELEGRAM_BOT_TOKEN}"
      }
    },
    "google-calendar": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-calendar"],
      "env": {
        "GOOGLE_CLIENT_ID": "${GOOGLE_CLIENT_ID}",
        "GOOGLE_CLIENT_SECRET": "${GOOGLE_CLIENT_SECRET}",
        "GOOGLE_REFRESH_TOKEN": "${GOOGLE_REFRESH_TOKEN}"
      }
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_TOKEN": "${NOTION_TOKEN}"
      }
    },
    "gmail": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gmail"],
      "env": {
        "GOOGLE_CLIENT_ID": "${GOOGLE_CLIENT_ID}",
        "GOOGLE_CLIENT_SECRET": "${GOOGLE_CLIENT_SECRET}",
        "GOOGLE_REFRESH_TOKEN": "${GOOGLE_REFRESH_TOKEN}"
      }
    },
    "oh-my-claudecode": {
      "command": "npx",
      "args": ["-y", "oh-my-claudecode"],
      "env": {
        "OMC_WORKSPACE": "${WORKSPACE_ROOT}"
      }
    }
  }
}
```

### Discord plugin — multi-channel, bot-to-bot

Each agent runs its own Discord bot token. Configure separate bot applications in the [Discord Developer Portal](https://discord.com/developers/applications) — one per agent.

```json
"discord": {
  "command": "npx",
  "args": ["-y", "@neomakes/mcp-discord"],
  "env": {
    "DISCORD_BOT_TOKEN": "${ZORO_DISCORD_BOT_TOKEN}",
    "DISCORD_GUILD_ID": "${DISCORD_GUILD_ID}",
    "REQUIRE_MENTION": "true"
  }
}
```

Bot-to-bot communication: bots can read each other's messages in shared channels. Mention routing uses `<@BOT_ID>` format — plain `@name` text does not trigger notifications. See the crew `CLAUDE.md` for the full bot ID table.

### Telegram plugin

Single bot token per agent. DM mode does not require mention; group/channel mode requires mention.

```json
"telegram": {
  "command": "npx",
  "args": ["-y", "@neomakes/mcp-telegram"],
  "env": {
    "TELEGRAM_BOT_TOKEN": "${ZORO_TELEGRAM_BOT_TOKEN}"
  }
}
```

### oh-my-claudecode (OMC) tools

OMC provides multi-agent orchestration, state management, LSP tools, and notepad/memory tools. It is the orchestration backbone that connects all agents.

```bash
# Install globally
npm install -g oh-my-claudecode

# Verify
omc --version
```

After installation, the MCP server is available in every Claude Code session and exposes tools like `state_read`, `state_write`, `notepad_write_priority`, `lsp_diagnostics`, `ast_grep_search`, and the full agent catalog.

---

## 4. Per-Agent Session Setup

### One Claude Code instance per agent

Each agent runs as a separate Claude Code process, started from its own working directory. This ensures the correct `CLAUDE.md` stack is loaded.

```bash
# Start Zoro's session
cd /workspace/_crew/zoro
claude

# Start Usopp's session (separate terminal)
cd /workspace/_crew/usopp
claude
```

### Session initialization sequence (PRC-201)

When a session starts, the agent must:

1. Read `_crew/CLAUDE.md` — meta strategy and universal standards
2. Read its own `sop.md` — department-specific procedures
3. Read its department `STR-*.md` from the drive — strategic direction

```markdown
<!-- Example sop.md session start block -->
## Session Start Checklist (PRC-201)
1. Read /workspace/_crew/CLAUDE.md
2. Read /workspace/_crew/{agent}/sop.md  ← this file
3. Read STR for this department if direction check needed
4. Check todo.json for pending tasks
5. Begin work. Report blockers within 15 minutes.
```

The `sop.md` file lives in the agent's directory and contains only department-specific procedures. Universal standards (the 12 mandatory items) are inherited from `_crew/CLAUDE.md` and must not be duplicated in `sop.md`.

### Directory layout for a single agent

```
/workspace/_crew/{agent}/
├── CLAUDE.md          # Identity, persona, role, project access, Standard refs
├── sop.md             # Department-specific SOP (R only at session start)
├── todo.json          # Daily task list (RW during session)
├── weekly.json        # Weekly plan (RW on Sundays)
└── reports/
    └── YYYY-MM-DD.md  # Daily report (W at session end, PLY-201 format)
```

---

## 5. Hooks and Automation

Claude Code supports hooks that fire before and after tool use, and at session boundaries. Hooks run shell commands and can inject additional context into the session via `<system-reminder>` tags.

### Hook configuration

Hooks are configured in `settings.json` under the `hooks` key.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'PreToolUse:Bash hook: use parallel execution for independent tasks.'"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'PostToolUse:Bash hook: verify results before proceeding.'"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/workspace/scripts/session-start.sh"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/workspace/scripts/session-end.sh"
          }
        ]
      }
    ]
  }
}
```

### Session start hook (`session-start.sh`)

Injects fresh context at the top of every session: current date, active OMC state, pending tasks.

```bash
#!/usr/bin/env bash
set -euo pipefail

AGENT=${CLAUDE_AGENT_NAME:-unknown}
DATE=$(date +%Y-%m-%d)
TODO_FILE="/workspace/_crew/${AGENT}/todo.json"

echo "Session started: ${AGENT} on ${DATE}"

# Surface pending tasks if todo.json exists
if [[ -f "$TODO_FILE" ]]; then
  PENDING=$(jq '[.tasks[] | select(.status == "pending" or .status == "in_progress")] | length' "$TODO_FILE")
  echo "Pending tasks: ${PENDING}"
fi
```

### Session end hook (`session-end.sh`)

Prompts the agent to write its daily report and update task statuses before the session closes.

```bash
#!/usr/bin/env bash
set -euo pipefail

AGENT=${CLAUDE_AGENT_NAME:-unknown}
DATE=$(date +%Y-%m-%d)
REPORT_DIR="/workspace/_crew/${AGENT}/reports"

mkdir -p "$REPORT_DIR"
echo "Session ending. Daily report expected at: ${REPORT_DIR}/${DATE}.md"
```

### OMC hooks

oh-my-claudecode injects `<system-reminder>` tags automatically for tool-use guidance, context percentage warnings, and multi-agent state signals. These appear inline in the session transcript and do not require additional configuration once the OMC MCP server is running.

Key OMC signals to handle:

| Signal | Meaning |
|--------|---------|
| `hook success: Success` | Proceed normally |
| `[MAGIC KEYWORD: ...]` | Invoke the named OMC skill |
| `The boulder never stops` | Ralph/ultrawork mode is active — keep executing |
| `ctx:75%+` in status bar | Warn principal, propose session handoff |

---

## Quick Reference

### Start a governed agent session

```bash
# 1. Set environment variables
export DISCORD_BOT_TOKEN="..."
export TELEGRAM_BOT_TOKEN="..."

# 2. Navigate to agent directory (loads correct CLAUDE.md stack)
cd /workspace/_crew/zoro

# 3. Start Claude Code
claude
```

### Verify governance stack is loaded

At session start, ask the agent:

```
What CLAUDE.md files did you load? List them in order.
```

A correctly configured agent will list all four levels from global to agent-specific.

### Troubleshooting

**Agent doesn't see shared crew rules**
Confirm `_crew/CLAUDE.md` exists and the agent's working directory is inside `_crew/{agent}/`, not above it.

**MCP tools not available**
Run `claude mcp list` to verify servers are registered. Check that environment variables are set and tokens are valid.

**Hooks not firing**
Confirm `settings.json` is in the workspace root or `~/.claude/`. Hook `matcher` values are case-sensitive and must match the exact tool name.

**Bot-to-bot mentions not routing**
Confirm you are using `<@BOT_ID>` format with the numeric ID, not `@name` text. Check the bot ID table in `_crew/CLAUDE.md`.
