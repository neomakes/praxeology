<p align="center">
  <img src="assets/banner-3d.gif" alt="Praxeology — 3D governance manifold where a golden ball rolls across tiers from Strategy to Execution" width="100%">
</p>
<p align="center">
  <a href="assets/banner-3d.html"><em>View Interactive 3D Banner</em></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/version-0.1.0-green.svg" alt="v0.1.0">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg" alt="Active">
  <img src="https://img.shields.io/badge/built%20by-NeoMakes-black.svg" alt="NeoMakes">
</p>

<p align="center">
  <a href="README.md"><strong>English</strong></a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.es.md">Español</a>
</p>

<p align="center">
  <a href="docs/quickstart.md">Quick Start</a> (<a href="docs/quickstart.ko.md">한국어</a> · <a href="docs/quickstart.ja.md">日本語</a> · <a href="docs/quickstart.zh.md">中文</a> · <a href="docs/quickstart.fr.md">FR</a> · <a href="docs/quickstart.de.md">DE</a> · <a href="docs/quickstart.es.md">ES</a>) ·
  <a href="docs/role-design.md">Role Design</a> (<a href="docs/role-design.ko.md">한국어</a> · <a href="docs/role-design.ja.md">日本語</a> · <a href="docs/role-design.zh.md">中文</a> · <a href="docs/role-design.fr.md">FR</a> · <a href="docs/role-design.de.md">DE</a> · <a href="docs/role-design.es.md">ES</a>)
</p>

---

## The Problem

**Parallelization is solved.** Today's AI coding tools already make individual agents incredibly productive. Running 5 agents in parallel is a solved problem.

**Coordination is not.** When those 5 agents finish their work, who resolves conflicts? Who verifies consistency? Who prevents Agent A from overwriting Agent B's decisions? Who stops role drift across sessions? Multi-agent frameworks solve the *start* — Praxeology solves what comes after: **coordination, state tracking, conflict resolution, and evolutionary alignment.**

**Praxeology is the missing governance layer.** It sits above your coding tools, not replacing them — ensuring your agents operate as a coherent organization rather than a collection of independent chatbots.

It governs three axes simultaneously: **Logical** (why and how — doctrine hierarchy), **Tactical** (what and when — goal-to-task decomposition), and **Contextual** (who and where — organizational structure). Agents query all three axes to determine the right action, and feed results back via `.backprop()` — the organizational equivalent of automatic differentiation.

---

## Production Proof

This isn't theory. [NeoMakes](https://neomakes.com) runs this every day.

> **1 human + 9 AI agents · 38 governance rules · 7 departments**
> Daily todos → Weekly reviews → Monthly amendments
> Agents detect gaps, propose fixes, evolve their own SOPs.

> Praxeology is the only governance framework where AI agents follow rules, learn from experience, and can explain the reasoning behind their actions.

Each agent has defined **Speech Rules** (sentence limits, tone), **Anti-Patterns** (forbidden behaviors), and **Emotional Triggers** (situation-dependent response changes) — ensuring consistent, distinguishable behavior across all 9 agents. NeoMakes is one instance. Yours will look different.

---

## How It Works — The Six W's

Every organizational action answers six questions: **Why, How, What, When, Who, Where.** Praxeology organizes these into 3 axes, each with 5 hierarchical layers:

```
         Logical (Why/How)        Tactical (What/When)      Contextual (Who/Where)
         ─────────────────        ────────────────────      ──────────────────────
Tier 1   Strategy                 Goal                      Space
Tier 2   Doctrine                 Program                   Channel
Tier 3   Procedure                Campaign                  Thread
Tier 4   Playbook                 Plan                      Crew
Tier 5   Case                     Work                      Session
```

**Forward Pass — Acting:**
An agent receives a task (Work). It checks relevant Playbooks and Procedures for how to act, verifies against Doctrine constraints, and executes within its Session context. This is the normal flow — top-down governance guiding action.

**Backward Pass — Learning (`.backprop()`):**
When the result surprises — a rule was missing, a plan didn't match reality, or a task fell outside someone's authority — the feedback propagates *backward* through all 3 axes simultaneously:
- **Logical:** Case → Playbook gap → Procedure review → Doctrine amendment
- **Tactical:** Work result → Plan adjustment → Campaign reprioritization → Goal reassessment
- **Contextual:** Session learning → Crew skill update → Thread reassignment → Channel restructuring

Higher tiers are stable; lower tiers absorb most changes. Only significant surprises propagate upward — like waves on the surface while the deep ocean stays calm.

---

## What Makes It Different

Not a feature list. A coordination problem solver.

| Your Problem | Praxeology's Answer |
|---|---|
| Agents drift from their role over sessions | **ConstitutionalGuard** — behavioral verification against all 3 axes |
| No way to safely constrain agent actions | **SafetyGate** — Higher tiers lock critical rules that lower tiers cannot override |
| Agents can't improve their own processes | **SOP Evolution** — `.backprop()` loop. Gradient descent for governance |
| Changes in one place break another | **Review Cascade** — Bidirectional propagation across all 3 axes |
| Agents can't flag when rules are bad | **Proposal Flow** — Structured amendment requests from any agent to the founder |
| No institutional memory across sessions | **Case Memory** — Every execution recorded as a Case, searchable for future decisions |
| Agents don't know what to do next | **`what_now()`** — Cross-axis recommendation engine that finds the highest-value action |

---

## Quick Start

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
bash setup.sh    # Interactive wizard: org name, mission, departments, agents
bash launch.sh   # Your governance system is live
```

> **New?** Start with [Quick Start Guide](docs/quickstart.md) and [Role Design Guide](docs/role-design.md).

---

## Agent Design System

Every agent gets a `CLAUDE.md` that defines not just *what* it does, but *how* it behaves:

```
Identity → Persona → Speech Rules → Anti-Patterns → Emotional Triggers → Values → Boundaries
```

This makes agents **distinguishable, consistent, and bounded**. A QA agent sounds different from an executor. A planner never writes code. A reviewer never approves their own work. See [Role Design Guide](docs/role-design.md) for the full template and scaling strategies (3 to 15+ agents).

---

## MCP Server — Praxeology Runtime

Praxeology v1 is a document framework. The MCP server makes it a **runtime** — agents can search doctrine, track objectives, record cases, detect gaps, and evolve their own governance.

### Installation

```bash
pip install praxeology-mcp
```

Or install from source:

```bash
git clone https://github.com/neomakes/praxeology.git
cd praxeology
pip install -e .
```

### Quick Start

```bash
# Bootstrap a new project
praxeology init --name MyOrg --agents 3

# Migrate existing Praxeology v1 files to DB
praxeology migrate --project-dir .

# The MCP server starts automatically via .mcp.json
```

### 17 MCP Tools — 3 Axes × 5 Operations + 2 Cross-Axis

| Axis | search | read | create | escalate | feedback |
|------|--------|------|--------|----------|----------|
| **Logical** (Why/How) | Search standards & cases | Read with history | Create standard/case/gap/proposal | Flag for review | Record result + surprise |
| **Tactical** (What/When) | Search objectives | Read with parent chain | Create goal→work hierarchy | Block + notify parent | Update status |
| **Contextual** (Who/Where) | Search org structure | Read crew + access | Create space→session | Delegate to other crew | Record KPI review |

**Cross-Axis:**
- `what_now(crew_id)` — "What should I do right now?" Recommends highest-value action by cross-referencing all 3 axes.
- `backprop(case_id, result, surprise)` — The organizational equivalent of automatic differentiation. Records execution result and propagates feedback simultaneously to all 3 axes: updates doctrine (Logical), adjusts plans (Tactical), and logs crew performance (Contextual). High surprise auto-creates gaps; very high surprise auto-generates amendment proposals. Over time, this is gradient descent for governance.

### Heartbeat Engine

Built-in 2-tier background check:
- **Lightweight** (rule-based, cost = 0): Checks pending work, overdue schedules, open gaps
- **Heavyweight** (LLM, triggered only when needed): Evaluates whether action is required

Over time, as gaps are absorbed into doctrine, more situations are handled by the lightweight tier — **cost decreases with use**.

---

## Examples

- [examples/solo-dev/](examples/solo-dev/) — Solo developer + 3 agents (minimal)
- [examples/tech-startup/](examples/tech-startup/) — Early-stage software company
- [examples/one-piece-crew/](examples/one-piece-crew/) — Fictional crew with full persona system

---

## The Theory — Why This Works

The same 5-tier structure appears across every domain of organized action:

| Tier | National Law | Military (C2) | Corporate | Individual | Deep Learning | Essence |
|------|-------------|---------------|-----------|------------|---------------|---------|
| **1 Strategy** | Constitution | National Defense Strategy | Articles of Incorporation | Values & Identity | Objective function *J*, Manifold | **Why** — fundamental purpose |
| **2 Doctrine** | Statute Law | Operational Doctrine | Corporate Regulations | Personal Principles | Constraints *g(x) ≤ 0* | **What** — principles & boundaries |
| **3 Procedure** | Decree / Rules | OPLAN / OPORD | Operating Guidelines | Goals & Routines | Policy *π*, Control input *u* | **How** — resource allocation |
| **4 Playbook** | Administrative Rules | TTP (Tactics, Techniques, Procedures) | SOP / Best Practices | Habits & Mastery | Deterministic mapping *y = f(x)* | **Execute** — repeatable patterns |
| **Case/Exec** | Enforcement | FRAGO / C2 | Work Execution | Flow & Adaptation | Feedback loop *Δe*, Kalman filter | **Now** — real-time control |

Governance is not domain-specific. The pattern is universal. A framework that works for a military unit works for a startup or an AI agent fleet. For the full mathematical mapping (systems engineering, gradient descent), see [docs/architecture.md](docs/architecture.md).

---

## Directory Structure

```
your-org/
├── CLAUDE.md                  # Root context for AI agents (generated)
├── launch.sh                  # Daily launch script (generated)
├── _standard/                 # Governance documents
│   ├── README.md              # Master index of all governance artifacts
│   ├── {department}/          # One folder per department
│   │   ├── STR-{NNN}.md      #   (e.g., strategy, operations, finance, engineering)
│   │   ├── DOC-{NNN}.md
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # Agent / team member definitions
│   ├── CLAUDE.md              # Shared crew rules
│   └── {agent}/               # Per-agent subdirectory
│       ├── CLAUDE.md          # Agent context and persona
│       └── sop.md             # Agent SOPs
├── _project/                  # Active projects
├── _setting/                  # Operational settings
├── docs/                      # Framework documentation
├── templates/                 # Reusable document templates
└── examples/                  # Reference implementations
```

---

## Integration Guides

| Guide | Description |
|-------|-------------|
| [Discord Integration](docs/discord-integration.md) | Channel structure, bot mentions, loop prevention |
| [Google Drive Integration](docs/drive-integration.md) | Symlink setup, regulation storage, workspaces |
| [Crew Manager Dashboard](docs/crew-manager.md) | Web dashboard for session monitoring |
| [Claude Code Setup](docs/claude-code-setup.md) | CLAUDE.md hierarchy, MCP servers, per-agent sessions |
| [Work Cycle](docs/work-cycle.md) | Todo/weekly schemas, reporting cycle, Standard Gap flow |

## Documentation

| Document | Description |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Design philosophy and core mechanisms |
| [docs/getting-started.md](docs/getting-started.md) | Prerequisites, installation, first steps |
| [docs/standard-system.md](docs/standard-system.md) | The 5-tier document system in depth |
| [docs/crew-system.md](docs/crew-system.md) | Agent management, SOP self-evolution |
| [docs/tutorial.md](docs/tutorial.md) | Full walkthrough building a governed agent team |

---

## Origin

Built by **[NeoMakes](https://neomakes.com)** — a one-person company developing on-device AI for extreme environments. The framework emerged from governing a fleet of AI agents with the same rigor applied to military command structures.

The name comes from praxeology, the study of human action. Purposeful action has structure. That structure is universal. Make it explicit, and you can govern anything.

---

## License

MIT License — see [LICENSE](LICENSE).

Copyright (c) 2026 NeoMakes
