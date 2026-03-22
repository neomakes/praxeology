# Getting Started with Praxeology

This guide takes you from zero to a running governed AI agent team in under 30 minutes.

---

## Prerequisites

### Required

**Claude Code** — the host environment for all agents.
Install from [claude.ai/code](https://claude.ai/code) or via the Anthropic CLI.
Verify: `claude --version`

**Git** — version control for all governance documents.
```bash
# macOS
brew install git

# Ubuntu/Debian
apt-get install git
```
Verify: `git --version`

### Optional

**Telegram** — enables async communication between agents and the principal.
Set up a Telegram bot via [@BotFather](https://t.me/BotFather) and note your bot token.
Not required for local-only operation.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/neomakes/praxeology.git
cd praxeology
```

### 2. Run setup

```bash
bash setup.sh
```

The setup script:
- Creates the org directory scaffold
- Initializes git tracking for governance documents
- Configures CLAUDE.md auto-loading
- Optionally sets up Telegram integration

---

## First Steps

### Step 1: Create your organization

The organization is the root of your governance tree. It defines Strategy-tier constraints that apply to every agent in the system.

Create `org/CLAUDE.md`:

```markdown
# [Your Org Name] — Strategy

## Mission
[One sentence: what this org exists to accomplish]

## Values
1. [Core value 1]
2. [Core value 2]
3. [Core value 3]

## Hard Constraints (SafetyGate: Strategy)
- NEVER [constraint 1]
- NEVER [constraint 2]
- ALWAYS [constraint 1]

## Scope
This governance applies to all agents operating under this organization.
```

Commit this file:
```bash
git add org/CLAUDE.md
git commit -m "feat: initialize org strategy"
```

### Step 2: Define departments

Departments segment your agent team by function. Each department inherits org-level Strategy and adds its own Doctrine and Procedures.

Create `org/departments/research/CLAUDE.md`:

```markdown
# Research Department — Doctrine

## Inherits
- org/CLAUDE.md (Strategy)

## Department Mission
Produce rigorous, reproducible research outputs.

## Principles
1. Cite sources for all factual claims
2. Prefer primary sources over secondary
3. Flag uncertainty explicitly — never feign confidence
4. All outputs are reproducible from documented methods

## Procedures
- See procedure/literature-search.md
- See procedure/report-writing.md
```

### Step 3: Deploy agents

An agent is a Claude Code session configured with the appropriate CLAUDE.md context. Deploy by opening Claude Code in the relevant department directory.

```bash
# Open a research agent session
cd org/departments/research
claude
```

When Claude Code starts, it automatically loads:
1. `org/CLAUDE.md` (Strategy)
2. `org/departments/research/CLAUDE.md` (Department Doctrine)
3. Any CLAUDE.md in intermediate directories

The agent now has its full governance context loaded without any manual prompt engineering.

**Naming convention**: Give each agent a persona that reflects its role.

```markdown
<!-- Add to department CLAUDE.md -->
## Agent Identity
You are Alex, a research analyst at [Org Name].
Your role: literature review, data synthesis, report drafting.
Your authority tier: Playbook (can self-approve Playbook changes;
must propose Procedure changes and above).
```

### Step 4: Run your first task

With an agent session open, assign a task through a Work Plan:

```markdown
# Work Plan: WP-2026-001
Date: 2026-03-22
Agent: Alex (research)
Assigned by: Principal

## Task
Survey recent literature on transformer attention mechanisms.
Produce a 2-page summary with key papers, findings, and open questions.

## Constraints
- Time budget: 2 hours
- Output format: Markdown, committed to research/outputs/
- Citation style: APA

## Definition of Done
- [ ] Minimum 10 papers reviewed
- [ ] Summary committed to git
- [ ] Learning log updated
```

Save this as `org/departments/research/work-plans/WP-2026-001.md` and share it with the agent session.

The agent will:
1. Run SafetyGate on the task
2. Check for applicable Procedures and Playbooks
3. Execute the task
4. Commit outputs
5. Update learning log
6. Mark work plan complete

### Step 5: Verify the first cycle

After the agent completes the task, verify:

```bash
# Check outputs were committed
git log --oneline -5

# Check learning log was updated
cat org/departments/research/agents/alex/learning-log.md

# Check no SafetyGate violations
grep -r "HALT" org/departments/research/agents/alex/
```

---

## Verification Checklist

Before considering your installation production-ready:

### Governance structure
- [ ] `org/CLAUDE.md` exists and contains Strategy
- [ ] At least one department CLAUDE.md with Doctrine
- [ ] At least one Procedure document
- [ ] At least one Playbook document
- [ ] Git initialized and tracking all governance files

### Agent configuration
- [ ] Each agent has a defined identity and authority tier
- [ ] Each agent knows how to invoke SafetyGate
- [ ] Each agent knows how to file a Proposal
- [ ] Each agent has a learning log file

### Operational readiness
- [ ] Test task completed successfully
- [ ] Outputs committed to git
- [ ] Learning log updated
- [ ] No unresolved SafetyGate HALT conditions

### Review schedule
- [ ] Weekly Playbook review scheduled
- [ ] Monthly Procedure review scheduled
- [ ] Quarterly Doctrine review scheduled
- [ ] Annual Strategy review scheduled

---

## Telegram Multi-Bot Setup

When running multiple agents with individual Telegram bots, each agent needs its own isolated channel state. The launch script handles this automatically via `TELEGRAM_STATE_DIR`, but there are important details to be aware of.

### Setup procedure (per agent)

1. **Create bot**: `@BotFather` → `/newbot` → note the token
2. **Save token**: Write the token to `_crew/{agent}/.env`:
   ```
   TELEGRAM_BOT_TOKEN=your_token_here
   ```
3. **Set OWNER_ID** in `launch.sh`: Your Telegram user ID (find via `@userinfobot`)
4. **Launch**: `bash launch.sh agent1 agent2 ...`

The launch script auto-provisions `access.json` with allowlist policy, restricting each bot to the owner only.

### Group chat setup

Multiple agents can participate in a shared Telegram group for collaborative conversations.

1. **Create a Telegram group** and invite all participating bots
2. **Get the group ID**: Send a message in the group, then check via bot API:
   ```bash
   curl -s "https://api.telegram.org/bot<TOKEN>/getUpdates" | python3 -m json.tool
   ```
   Look for `chat.id` in the response (negative number, e.g., `-5178557722`).
3. **Configure in `launch.sh`**:
   ```bash
   GROUPS=("-5178557722:zoro,nami,usopp")
   MENTION_PATTERNS[zoro]="조로,zoro"
   MENTION_PATTERNS[nami]="나미,nami"
   ```

The launch script registers groups in each agent's `access.json` with:
- `requireMention: false` — agents receive all group messages and respond when their expertise is relevant
- `mentionPatterns` — agents always respond when their name (natural language) appears
- `allowFrom: []` — both the owner and other bots can trigger responses, enabling agent-to-agent collaboration

**Loop prevention** is critical in group chats. See [crew-system.md](./crew-system.md#group-chat-rules) for the required CLAUDE.md rules that prevent infinite response chains between agents.

### Security

- **Never read `.env` files** containing bot tokens — not even for debugging. Use `getMe` API to verify a bot works without exposing the token in logs.
- **Rotate tokens immediately** if exposed. Use `@BotFather` → `/mybots` → select bot → `API Token` → `Revoke`.
- **`.env` and `access.json`** must be in `.gitignore` — never commit secrets.

### Known issue: Bot-to-bot messages are invisible (Telegram platform limitation)

Telegram Bot API **does not deliver messages from one bot to another bot** in group chats. This is a hard platform restriction — not configurable via privacy mode, admin status, or any API parameter.

> "Bots talking to each other could potentially get stuck in unwelcome loops. To avoid this, we decided that bots will not be able to see messages from other bots regardless of mode." — [Telegram Bot FAQ](https://core.telegram.org/bots/faq)

**Impact**: In a multi-agent group chat, agents can see the owner's messages but cannot see each other's responses. Each agent operates in isolation within the group.

**Workarounds**:

| Approach | Description |
|----------|-------------|
| Owner relays | Owner manually summarizes or quotes one agent's response for another |
| External message bus | Agents share messages via a backend service (database, REST API, file system) outside Telegram |
| Web-based comm hub | Use a web application with group chat functionality as the agent-to-agent channel, keeping Telegram for owner↔agent only |

**Recommended architecture**: Use Telegram for **owner ↔ agent** communication (DMs and group commands). Use an **external coordination layer** (web dashboard, shared database, or message queue) for **agent ↔ agent** collaboration. This cleanly separates the two communication patterns and avoids the platform limitation entirely.

### Known issue: `/telegram:access` hardcoded path

The `/telegram:access` skill reads from `~/.claude/channels/telegram/access.json` regardless of `TELEGRAM_STATE_DIR`. This means it cannot manage per-agent access in multi-bot setups.

**Workaround**: The launch script auto-provisions `access.json` directly in each agent's state directory, bypassing the skill entirely. To manually manage access after launch, edit the agent's access.json directly:

```bash
# View access state for a specific agent
cat ~/.claude/channels/{agent}/access.json

# Manually approve a user (replace SENDER_ID)
python3 -c "
import json, os
path = os.path.expanduser('~/.claude/channels/{agent}/access.json')
data = json.load(open(path))
data['allowFrom'].append('SENDER_ID')
data['allowFrom'] = list(set(data['allowFrom']))
json.dump(data, open(path, 'w'), indent=2)
"
```

---

## Common Setup Issues

### Agent is not loading governance documents

Verify that CLAUDE.md files are in directories that are parent to the agent's working directory. Claude Code loads CLAUDE.md files from the working directory upward to the filesystem root.

```bash
# Check what CLAUDE.md files exist
find org/ -name "CLAUDE.md" | sort
```

### Agent is modifying documents above its authority tier

Add explicit authority statements to the agent's department CLAUDE.md:

```markdown
## Authority
- You MAY modify files in: playbook/, work-plans/, agents/[your-name]/
- You MUST NOT modify files in: strategy/, doctrine/, procedure/
- You MAY submit Proposals to: procedure/, doctrine/, strategy/
- Proposals go in: proposals/[tier]/[YYYY-MM-DD]-[title].md
```

### Agent is stuck on security prompt (not responding)

Claude Code has built-in security prompts for cross-directory `cd` and `git` operations. On first launch, each agent session will pause at a "Do you want to proceed?" prompt. **This cannot be bypassed via settings.**

**Fix**: Attach to the tmux session and manually approve:
```bash
tmux attach -t crew_{agent}
# Select option 2: "Yes, allow during this session"
# Detach: Ctrl+B, D
```

This only happens once per session. If an agent suddenly stops responding in a group chat, check if it's stuck on a security prompt.

### Proposals are not being reviewed

Set up a review trigger. The simplest approach is a git hook or a periodic work plan assigned to the department head agent:

```markdown
# Work Plan: WP-WEEKLY-REVIEW
Recurrence: Every Monday
Agent: [Department Head]
Task: Review all pending proposals in proposals/. Accept, reject, or request revision.
```

### Git conflicts in governance documents

This usually means two agents modified the same document. Prevent this with file ownership conventions:

```markdown
## File Ownership (in CLAUDE.md)
- research/agents/alex/ — owned by Alex, no other agent modifies
- research/playbook/ — owned by department head; agents submit proposals only
```

---

## Next Steps

- Read [standard-system.md](./standard-system.md) to understand each tier in depth
- Read [crew-system.md](./crew-system.md) to learn agent management patterns
- Follow [tutorial.md](./tutorial.md) for a full walkthrough building a research lab
- Read [architecture.md](./architecture.md) for the underlying design philosophy
