# NeoTOC

> **An open-source framework that gives AI agents concrete Personas and Behavior Trees, controlling them safely while operating them as a crew.**

Inspired by the Straw Hat Pirates from One Piece — each agent has a distinct personality, role, and set of behavioral rules. They don't just execute tasks; they inhabit roles, respect boundaries, and report like real crew members.

## Vision

### v1 — Current Architecture

```
Luffy (You) → OMC Orchestrator → Agent Assignment → Telegram One-Way Reporting
```

The captain gives orders. The orchestrator (oh-my-claudecode) assigns the right crew member. Each agent executes within their Behavior Tree rules and reports back via Telegram.

### v2 — The Dream (Roadmap)

**Thousand Sunny**: A Telegram group where you drop a task and the crew self-organizes.

```
Luffy:  "We need a Bayesian Search algorithm."
Robin:  "I found 3 relevant papers. Let me analyze them first."
Zoro:   "Ready to implement. Starting as soon as Robin finishes."
Nami:   "Estimated token cost: $2.30. Off-peak hours recommended."
Usopp:  "I'll prepare the test suite. This thing better not have bugs!"
Sanji:  "Dependencies locked. Environment is served."
```

Each crew member autonomously discusses, divides labor, executes, and reports. The captain intervenes only when needed.

## Philosophy — NeoRoger

NeoTOC is built on the **NeoRoger** foundation:

| Pillar | Origin | Application |
|--------|--------|-------------|
| **Praxeology** | Mises — the logic of human action | Agents act purposefully within defined constraints |
| **Thymology** | Mises — understanding of human values | Each persona has values that drive behavior |
| **Behavior Tree** | Game AI — structured decision trees | Actions are controlled, predictable, and debuggable |
| **Ralph Loop** | Persistence engine | Tasks repeat until truly complete — no silent failures |
| **Root Guard** | Safety mechanism | The root node enforces boundaries every tick |
| **AAR** | Military — After Action Review | Every significant action requires human review and approval |

## The Crew

| Member | Role | Specialty |
|--------|------|-----------|
| **Zoro** | Code Executor | Core implementation, refactoring, commits |
| **Nami** | Navigator & CFO | Project planning, token costs, resource management |
| **Usopp** | QA Engineer & Tester | Testing, bug hunting, edge case detection |
| **Sanji** | DevOps & Dependency Manager | Packages, environments, supply chain |
| **Chopper** | Health & Wellbeing Monitor | User burnout detection, health checks |
| **Robin** | Intelligence & Research Analyst | Research, architecture analysis, competitive intel |
| **Franky** | Infrastructure Engineer | CI/CD, builds, deployment, infra |
| **Brook** | Documentation & Session Archivist | Logs, reports, changelogs, knowledge preservation |
| **Jinbe** | Integration & Stability Engineer | MCP connectors, external services, system stability |

## Documentation

- **Vision & Specs**: `docs/vision/` — PRD, SDS, Schema, Engineering Plan, Market Analysis, Critical Evaluation
- **Philosophy**: `docs/philosophy/` — NeoRoger Blueprint
- **Crew Personas**: `crew/` — 9 crew member persona definitions with BT rules
- **Behavior Rules**: `RULES.md` — Root Guard, Ralph Loop, and all crew BT sequences

## Current Stack

- **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** — AI agent runtime
- **[oh-my-claudecode (OMC)](https://github.com/nicobailon/oh-my-claudecode)** — Multi-agent orchestration layer
- **[gstack](https://github.com/anthropics/claude-code)** — Development tooling
- **Telegram G-Staff** — Crew reporting channel

## Project Structure

```
neotoc/
├── README.md              # This file (English)
├── README.ko.md           # Korean version
├── CLAUDE.md              # Claude Code global settings
├── RULES.md               # Behavior Tree rules
├── LICENSE
├── crew/                  # Crew member persona definitions
│   ├── zoro.md            # Code Executor
│   ├── nami.md            # Navigator & CFO
│   ├── usopp.md           # QA Engineer & Tester
│   ├── sanji.md           # DevOps & Dependency Manager
│   ├── chopper.md         # Health & Wellbeing Monitor
│   ├── robin.md           # Intelligence & Research Analyst
│   ├── franky.md          # Infrastructure Engineer
│   ├── brook.md           # Documentation & Session Archivist
│   └── jinbe.md           # Integration & Stability Engineer
├── templates/             # Task and session templates
│   ├── TASKS.md
│   └── SESSION.md
└── docs/
    ├── vision/            # PRD, SDS, Schema, Engineering Plan, etc.
    └── philosophy/        # NeoRoger Blueprint
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/neomakes/neotoc.git
cd neotoc

# Explore the crew
ls crew/

# Read the rules
cat RULES.md

# Check the blueprint
cat docs/neeroger-blueprint.md
```

## Contributing

NeoTOC is open source. Issues and PRs are welcome.

Whether you want to refine a crew member's persona, add new BT rules, or propose a new crew member — jump in. The Thousand Sunny has room for everyone.

## License

MIT License
