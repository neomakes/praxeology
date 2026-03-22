# Velocity Labs — Tech Startup Example

> Praxeology Framework | Version 1.0 | Enacted 2026-03-22

A solo founder running a 1-person tech startup with 4 AI agents. This example demonstrates the framework applied to a lean product team where a single human owns vision and final authority, while agents handle engineering, quality, and project coordination.

---

## Team Structure

| Agent | Role | C-Level | Domain |
|-------|------|---------|--------|
| Alex (human) | Founder / CEO | CEO | Vision, Product, Final Authority |
| Engineer | Senior Engineer | CTO | Implementation, Architecture |
| QA | Quality Assurance | CTO (QA function) | Testing, Verification |
| PM | Project Manager | COO | Planning, Coordination, Delivery |

---

## Domain Radar

| Domain | Engineer | QA | PM |
|--------|----------|----|----|
| Execution / Implementation | 10 | 5 | 3 |
| Quality / Testing | 5 | 10 | 4 |
| Planning / Coordination | 3 | 4 | 10 |
| Strategy / Product | 4 | 3 | 6 |
| Technology / Architecture | 9 | 6 | 3 |

---

## Governance Structure

```
_standard/
  ceo/STR-101.md       — Startup mission and product vision (WHY)
  cto/DOC-401.md       — Code quality standards (WHAT)

_crew/
  CLAUDE.md            — Shared rules for all agents
  engineer/CLAUDE.md   — Senior engineer persona + boundaries
  engineer/sop.md      — Engineer workflow procedures
  qa/CLAUDE.md         — QA agent persona + boundaries
  pm/CLAUDE.md         — Project manager persona + boundaries
```

---

## Key Design Decisions

1. **Founder is the only human.** Alex holds CEO authority. All agents escalate to Alex for decisions outside their scope.
2. **Engineer is the sole code writer.** QA tests; it does not fix. PM plans; it does not implement.
3. **PM owns the task queue.** Engineer and QA pull from PM's prioritized backlog, not from raw requests.
4. **QA is a gate, not a suggestion.** Nothing ships without QA sign-off or explicit founder override.
5. **Lean by default.** No unnecessary process overhead. Each agent does one thing excellently.
