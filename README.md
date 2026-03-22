<p align="center">
  <img src="assets/banner.svg" alt="praxeology — Human–AI Collaborative Governance for Purposeful Action" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/version-0.1.0-green.svg" alt="v0.1.0">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg" alt="Active">
  <img src="https://img.shields.io/badge/built%20by-NeoMakes-black.svg" alt="NeoMakes">
</p>

---

## What Is This?

**Praxeology** is a human–AI collaborative operating system built on a universal 4+1 tier governance hierarchy. Humans set the strategy and principles; agentic AI executes within those bounds, learns from experience, and proposes improvements back. It captures the observation that all purposeful action — from nations to agentic AI — follows the same structural pattern.

```
Strategy (WHY) → Doctrine (WHAT) → Procedure (HOW) → Playbook (PATTERNS) → Execution (NOW)
```

Higher tiers always override lower ones. No exceptions.

---

## The Isomorphism

The same 4+1 tier structure appears across every domain of organized action:

| Tier | National Law | Military | Corporate | Individual | AI Agent |
|------|-------------|----------|-----------|------------|----------|
| **1 Strategy** | Constitution | Campaign Objective | Mission & Vision | Personal Values | System Prompt / Prime Directive |
| **2 Doctrine** | Statute Law | Rules of Engagement | Corporate Policy | Life Principles | Behavioral Guidelines |
| **3 Procedure** | Regulations | Standard Operating Procedures | SOPs / Protocols | Habits & Routines | Task Instructions |
| **4 Playbook** | Case Law / Precedent | Tactics & Drills | Best Practices | Learned Patterns | Few-shot Examples |
| **Exec Work Plan** | Executive Order | Mission Orders | Sprint / Work Plan | Daily To-Do | Active Context |

This isomorphism is the core thesis: governance is not domain-specific. The pattern is universal. A framework that works for a military unit works for a startup, a research lab, or an AI agent fleet.

---

## Quick Start

**Step 1 — Clone**

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
```

**Step 2 — Run setup**

```bash
bash setup.sh
```

The interactive wizard asks for your organization name, mission, departments, agents, and projects. It generates the full directory structure and all bootstrap documents.

**Step 3 — Launch**

```bash
bash launch.sh
```

Your governance system is live. Open `CLAUDE.md` at the root to see the generated context for AI agents.

---

## Key Features

| Feature | Description |
|---------|-------------|
| **SafetyGate** | Higher-tier documents can declare hard limits that no lower-tier document can override |
| **Proposal Flow** | Any agent or team member can propose an amendment via the structured Proposal format |
| **SOP Evolution** | Procedures and Playbooks evolve through the Review Cascade before promotion |
| **Review Cascade** | Changes propagate upward: Playbook → Procedure → Doctrine → Strategy for consistency checks |
| **Reverse Flow** | Strategy changes cascade downward: all lower tiers are flagged for review |
| **Department Codes** | 7 standard departments (1xx–7xx) with C-level + G-Staff assignments |

---

## Directory Structure

```
your-org/
├── CLAUDE.md                  # Root context for AI agents (generated)
├── launch.sh                  # Daily launch script (generated)
├── _standard/                 # Governance documents
│   ├── README.md              # Master index of all governance artifacts
│   ├── ceo/                   # CEO — Strategy & Vision (1xx)
│   │   ├── strategy.md        # WHY: Mission, values, long-term vision
│   │   ├── doctrine.md        # WHAT: Governing principles
│   │   ├── procedure.md       # HOW: Executive processes
│   │   └── playbook.md        # PATTERNS: Recurring decision patterns
│   ├── coo/                   # COO — Operations & Execution (2xx)
│   ├── cfo/                   # CFO — Finance & Resources (3xx)
│   ├── cto/                   # CTO — Technology & R&D (4xx)
│   ├── cdo/                   # CDO — Diplomacy & Network (5xx)
│   ├── chro/                  # CHRO — HR & Wellbeing (6xx)
│   └── ciso/                  # CISO — Intelligence & Security (7xx)
├── _crew/                     # Agent / team member definitions
│   ├── CLAUDE.md              # Shared crew rules
│   └── {agent}/               # Per-agent subdirectory
│       ├── CLAUDE.md          # Agent context and persona
│       └── sop.md             # Agent SOPs
├── _project/                  # Active projects
│   ├── .praxe/                # Project cards (governance metadata)
│   │   └── {project}.md       # Status, priority, crew assignment, milestones
│   └── {project}/             # Each project directory (code)
├── _setting/                  # Operational settings
│   ├── permissions.md         # Access control matrix
│   └── integrations.md        # External service config
├── docs/                      # Framework documentation
├── templates/                 # Reusable document templates
└── examples/                  # Reference implementations
```

---

## Domain Applications

### Corporate

Map departments to C-suite roles. Use CEO/COO/CFO/CTO/CDO/CHRO/CISO departments. Each department owns its governance stack. The CEO Strategy document is the organization's constitution.

### Research Lab

Map roles to PI, Lab Manager, Finance Lead, Systems Lead, Partnerships, HR, and Security. Use the same tier structure. The Strategy document captures the lab's research mission and ethical constraints. See [docs/tutorial.md](docs/tutorial.md) for a full research lab walkthrough.

### Personal Productivity

A single-person implementation. CEO = you. Strategy = your life mission. Doctrine = your non-negotiables. Procedure = your weekly rituals. Playbook = your accumulated best practices. Work Plan = your daily list.

### AI Agent Team

Each AI agent gets a `_crew/{agent}/CLAUDE.md` defining its role, authority level, and operating constraints. The root `CLAUDE.md` is the team's shared constitution. Higher-tier documents are prepended to agent contexts before execution.

---

## Framework Documentation

| Document | Description |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | Design philosophy, core mechanisms, and the universal governance pattern |
| [docs/getting-started.md](docs/getting-started.md) | Prerequisites, installation, and first steps |
| [docs/standard-system.md](docs/standard-system.md) | The 4+1 tier document system in depth |
| [docs/crew-system.md](docs/crew-system.md) | Agent management, SOP self-evolution, and review cascade |
| [docs/tutorial.md](docs/tutorial.md) | Full walkthrough building a governed AI agent team |

---

## Examples

- [examples/tech-startup/](examples/tech-startup/) — Early-stage software company
- [examples/one-piece-crew/](examples/one-piece-crew/) — Fictional crew (demonstration)

---

## Origin

Praxeology was built by **[NeoMakes](https://neomakes.com)** — a one-person company developing foundational human-AI interaction technology for extreme environments. The framework emerged from the need to govern a growing fleet of AI agents with the same rigor applied to human organizations.

The name comes from praxeology, the study of human action. The insight: purposeful action has structure. That structure is universal. Make it explicit, and you can govern anything.

---

## License

MIT License — see [LICENSE](LICENSE).

Copyright (c) 2026 NeoMakes
