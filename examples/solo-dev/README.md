# Solo Developer — 3 Agent Setup

> Praxeology Framework | Version 1.0 | Enacted 2026-03-26

Minimal Praxeology setup for a solo developer with 3 agents. One human owns all decisions; agents handle implementation, quality, and planning so the developer stays in the problem space instead of the execution space.

---

## Agents

| Agent | Role | Focus |
|-------|------|-------|
| Builder | Executor | Code implementation, bug fixes, features |
| Reviewer | QA + Code Review | Tests, reviews, quality gates |
| Planner | Strategy + Docs | Architecture decisions, documentation, planning |

---

## Domain Radar

| Domain | Builder | Reviewer | Planner |
|--------|---------|----------|---------|
| Execution / Implementation | 10 | 4 | 3 |
| Quality / Testing | 4 | 10 | 3 |
| Planning / Architecture | 3 | 5 | 10 |
| Documentation | 2 | 4 | 9 |
| Strategy | 3 | 4 | 8 |

---

## Directory Structure

```
my-project/
├── CLAUDE.md                 # Shared rules
├── _crew/
│   ├── CLAUDE.md             # Common crew rules
│   ├── builder/CLAUDE.md     # Builder persona
│   ├── reviewer/CLAUDE.md    # Reviewer persona
│   └── planner/CLAUDE.md     # Planner persona
├── _standard/
│   └── ceo/STR-101.md        # Your project mission
└── tool-bindings.yaml
```

---

## Getting Started

1. Copy this directory into your project root
2. Edit `_standard/ceo/STR-101.md` with your project mission
3. Customize each agent's `CLAUDE.md` with project-specific context
4. Start a Claude Code session per agent

---

## Key Design Decisions

1. **Developer is the only human.** All agents escalate for decisions outside their scope.
2. **Builder is the sole code writer.** Reviewer tests and reviews; it does not fix. Planner designs; it does not implement.
3. **Planner owns the task queue.** Builder and Reviewer pull from Planner's prioritized backlog, not from raw requests.
4. **Reviewer is a gate, not a suggestion.** Nothing ships without Reviewer sign-off or explicit developer override.
5. **Lean by default.** No unnecessary process. Each agent does one thing excellently.
