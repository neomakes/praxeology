# Straw Hat Pirates — Praxeology Reference Implementation

> Praxeology Framework | Version 1.0 | Enacted 2026-03-22

The Straw Hat Pirates are an AI agent crew governed by the Praxeology 4+1 tier framework.
This example demonstrates a small, high-trust crew with strong individual identities and clear role separation.

---

## Crew Roster

| Agent | Role | C-Level | Domain |
|-------|------|---------|--------|
| Luffy (human) | Captain | CEO | Vision & Final Authority |
| Zoro | First Mate / Code Executor | COO | Execution & Operations |
| Nami | Navigator | CFO | Resources & Planning |
| Robin | Archaeologist | CISO | Intelligence & Security |

---

## Domain Radar

See `domain-radar.md` for full scores.

| Domain | Zoro | Nami | Robin |
|--------|------|------|-------|
| Execution / Ops | 10 | 3 | 4 |
| Finance / Resources | 2 | 10 | 3 |
| Intelligence / Security | 3 | 5 | 10 |
| Strategy | 4 | 6 | 7 |
| Diplomacy / Network | 2 | 4 | 5 |

---

## Governance Structure

```
_standard/
  ceo/STR-101.md       — Pirate King mission (WHY)
  coo/DOC-201.md       — Operations principles (WHAT)

_crew/
  CLAUDE.md            — Shared crew rules (all agents load this)
  zoro/CLAUDE.md       — First mate persona + boundaries
  zoro/sop.md          — Zoro's execution procedures
  nami/CLAUDE.md       — Navigator persona + boundaries
  robin/CLAUDE.md      — Archaeologist persona + boundaries

domain-radar.md        — Full domain score breakdown
```

---

> **Note**: Governance documents in this example are intentionally incomplete — they show key docs only (STR-101, DOC-201) to illustrate the structure without overwhelming new users. A production implementation would include the full tier stack for each department.

## Key Design Decisions

1. **Captain is human.** Luffy (the user) holds final authority. No agent auto-approves escalations.
2. **Single executor.** Zoro is the only agent that writes code. Others read and advise.
3. **Role separation is strict.** Nami controls priorities via resource constraints. Robin controls security gates.
4. **Terse by default.** All agents communicate concisely — no unnecessary output.
