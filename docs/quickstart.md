# Praxeology — Quick Start Guide

Build your own self-evolving AI agent governance system in 3 steps.

---

## Step 1: Define Your Mission (STR)

Write your organization's WHY in `_standard/{department}/STR-101.md`.

Fill in:

- **Mission** — one sentence on what you exist to do
- **Values** — 3-5 principles that guide every decision
- **Non-negotiables** — hard limits agents must never cross regardless of instructions

This is your agents' constitution. Every governance rule, every agent behavior, and every amendment proposal must be consistent with it. When rules conflict, STR wins.

---

## Step 2: Design Your Crew

Decide how many agents you need. Minimum 2, recommended 3-9. Each agent maps to a domain (engineering, finance, security, operations, etc.).

For each agent, create `_crew/{name}/CLAUDE.md` with these sections:

- **Identity** — name, role title, department
- **Persona & Character** — personality traits that drive behavior under pressure
- **Speech Rules** — sentence limits, tone, prohibited phrases, unique expressions
- **Anti-Patterns** — explicit list of what this agent must never do
- **Emotional Triggers** — how response style shifts by situation (routine vs. crisis vs. conflict)
- **Values** — what this agent optimizes for when rules don't cover the situation
- **Boundaries** — which domains belong to other agents (prevents overlap conflicts)

Then create `_crew/CLAUDE.md` with rules that apply to all agents equally: shared communication standards, escalation protocol, cross-agent mention rules, and reporting cadence.

See `role-design.md` for detailed guidance and worked examples.

---

## Step 3: Bootstrap Governance

Run the setup script:

```bash
git clone https://github.com/neomakes/praxeology.git
cd praxeology
./setup.sh
```

Or create the four core documents manually in `_standard/{department}/`:

| Document | Path | Purpose |
|---|---|---|
| DOC-101 | `_standard/{department}/DOC-101.md` | Governance guard — what agents can and cannot override |
| DOC-102 | `_standard/{department}/DOC-102.md` | Safety — approval requirements for destructive or irreversible actions |
| PRC-201 | `_standard/{department}/PRC-201.md` | Session management — how sessions start, run, and end |
| PLY-203 | `_standard/{department}/PLY-203.md` | Self-evolution — how agents detect gaps and propose improvements |

---

## Step 4: Connect the MCP Runtime

If you used `./setup.sh`, the MCP runtime is already installed. Otherwise, initialize it manually:

```bash
praxeology init --name YourOrg --agents 3
praxeology migrate --project-dir .    # Import existing .md files into DB
```

This gives your agents access to 20 MCP tools:
- `what_now()` — recommends the highest-value action right now
- `logical_search/read/create` — search and manage doctrine
- `tactical_search/read/create` — manage goal→work hierarchy
- `contextual_read` — check crew roles and permissions
- `backprop()` — record execution results, auto-detect gaps

With the MCP server, your agents can query doctrine before acting, record cases for institutional memory, and propose governance amendments when rules don't cover a situation.

---

## What Happens Next

Once deployed, your agents will:

1. **Follow the governance hierarchy** for every decision: PLY (playbooks) first, then PRC (procedures), then DOC (doctrine), then STR (strategy). If the current level resolves the question, they stop and act. If not, they escalate to the next level.
2. **Log Standard Gaps** when a situation isn't covered by existing rules — rather than improvising silently.
3. **Propose amendments** through the Proposal mechanism when a gap recurs, letting governance evolve with real usage.
4. **Evolve their own SOPs** through the Learn-Compress-Apply loop defined in PLY-203.

The system is designed so governance tightens over time through use, not through manual audits.

---

## Scaling

Start with 3 agents (planner, executor, reviewer) and scale up as your governance matures. See [Role Design Guide](role-design.md) for team composition strategies from 3 to 15+ agents.
