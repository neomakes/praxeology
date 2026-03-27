<p align="center">
  <img src="assets/banner.svg" alt="praxeology — Human–AI Collaborative Governance for Purposeful Action" width="100%">
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
  <a href="docs/quickstart.md">Quick Start</a> (<a href="docs/quickstart.ko.md">한국어</a> · <a href="docs/quickstart.ja.md">日本語</a> · <a href="docs/quickstart.zh.md">中文</a>) ·
  <a href="docs/role-design.md">Role Design</a> (<a href="docs/role-design.ko.md">한국어</a> · <a href="docs/role-design.ja.md">日本語</a> · <a href="docs/role-design.zh.md">中文</a>)
</p>

---

## Why Praxeology?

Tools like [gstack](https://github.com/gstack-io/gstack) and [oh-my-claudecode](https://github.com/anthropics/claude-code) are excellent at making individual AI agents productive — browsing, coding, testing, deploying. But when you scale from **one agent** to **many agents working together**, a new problem emerges: **governance**.

Without governance, agents duplicate work, contradict each other, overstep boundaries, and drift from their intended roles over time. Prompt engineering alone doesn't solve this — you need structure that persists across sessions, evolves through use, and mirrors how the most effective human organizations have governed action for centuries.

Praxeology provides that structure. It's not a replacement for your coding tools — it's the **constitutional layer** that sits above them, ensuring your agents operate as a coherent organization rather than a collection of independent chatbots.

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

> **New to Praxeology?** Start with [docs/quickstart.md](docs/quickstart.md) for a 3-step guide, and [docs/role-design.md](docs/role-design.md) for designing your agents.

---

## Key Features

| Feature | Description |
|---------|-------------|
| **SafetyGate** | Higher-tier documents can declare hard limits that no lower-tier document can override |
| **Proposal Flow** | Any agent or team member can propose an amendment via the structured Proposal format |
| **SOP Evolution** | Procedures and Playbooks evolve through the Review Cascade before promotion |
| **Review Cascade** | Changes propagate upward: Playbook → Procedure → Doctrine → Strategy for consistency checks |
| **Reverse Flow** | Strategy changes cascade downward: all lower tiers are flagged for review |
| **Department Codes** | Departments with numeric code series (e.g., 1xx–7xx in the NeoMakes instance) with role + staff assignments |

---

## Directory Structure

```
your-org/
├── CLAUDE.md                  # Root context for AI agents (generated)
├── launch.sh                  # Daily launch script (generated)
├── _standard/                 # Governance documents
│   ├── README.md              # Master index of all governance artifacts
│   ├── {department}/          # One folder per department (e.g., strategy, operations, finance, ...)
│   │   ├── STR-{NNN}.md      #   NeoMakes instance uses: ceo, coo, cfo, cto, cdo, chro, ciso
│   │   ├── DOC-{NNN}.md
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
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

Map departments to organizational roles. Each department owns its governance stack. The top-level Strategy document is the organization's constitution. (The NeoMakes instance uses CEO/COO/CFO/CTO/CDO/CHRO/CISO departments — yours can be anything.)

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

- [examples/solo-dev/](examples/solo-dev/) — Solo developer + 3 agents (minimal setup)
- [examples/tech-startup/](examples/tech-startup/) — Early-stage software company
- [examples/one-piece-crew/](examples/one-piece-crew/) — Fictional crew with full persona system (demonstration)

---

## Production Use — NeoMakes (One Instance)

Praxeology is not theoretical. It runs a real company every day. NeoMakes is one instance of this framework — yours will look different.

**[NeoMakes, Inc.](https://neomakes.com)** operates as a 1-person company with 9 AI agents governed by Praxeology:

| Metric | Value |
|--------|-------|
| Agents | 9 (organized across 7 C-level departments) |
| Enacted regulations | 38 (STR/DOC/PRC/PLY across all departments) |
| Daily operations | Todo tracking, daily reports, weekly planning, monthly reviews |
| Integrations | Claude Code + Discord (4 channels) + Google Drive + Notion + Calendar |
| Self-evolution | Agents detect Standard Gaps daily → Proposals weekly → Amendments monthly |

The agents have defined personas with **Speech Rules** (sentence limits, tone), **Anti-Patterns** (forbidden behaviors), and **Emotional Triggers** (situation-dependent response changes) — ensuring consistent, distinguishable behavior across all 9 agents.

### Integration Guides

| Guide | Description |
|-------|-------------|
| [Discord Integration](docs/discord-integration.md) | Channel structure, bot mentions, loop prevention, bot-to-bot communication |
| [Google Drive Integration](docs/drive-integration.md) | Symlink setup, regulation storage, room-based workspaces |
| [Crew Manager Dashboard](docs/crew-manager.md) | Web dashboard for session monitoring, todo management, permission approval |
| [Claude Code Setup](docs/claude-code-setup.md) | CLAUDE.md hierarchy, MCP servers, per-agent session configuration |
| [Work Cycle](docs/work-cycle.md) | weekly.json/todo.json schemas, reporting cycle, Standard Gap reverse flow |

---

## Origin

Praxeology was built by **[NeoMakes](https://neomakes.com)** — a one-person company developing foundational human-AI interaction technology for extreme environments. The framework emerged from the need to govern a growing fleet of AI agents with the same rigor applied to human organizations.

The name comes from praxeology, the study of human action. The insight: purposeful action has structure. That structure is universal. Make it explicit, and you can govern anything.

---

## License

MIT License — see [LICENSE](LICENSE).

Copyright (c) 2026 NeoMakes
