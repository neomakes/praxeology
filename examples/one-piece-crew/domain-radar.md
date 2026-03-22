# Straw Hat Pirates — Domain Radar

> Text representation of crew domain competency scores (0–10).
> Used to identify coverage gaps and assign tasks to the right agent.

---

## Scores by Domain

```
Domain                   | Zoro | Nami | Robin | Crew Avg
-------------------------|------|------|-------|----------
Execution / Ops          |  10  |   3  |   4   |   5.7
Finance / Resources      |   2  |  10  |   3   |   5.0
Intelligence / Security  |   3  |   5  |  10   |   6.0
Strategy                 |   4  |   6  |   7   |   5.7
Diplomacy / Network      |   2  |   4  |   5   |   3.7
Technology / R&D         |   7  |   2  |   5   |   4.7
HR / Crew Wellbeing      |   3  |   4  |   3   |   3.3
```

---

## Text Radar (ASCII)

```
Execution/Ops
          10 |  Zoro ████████████████████
           8 |
           6 |                          Robin ████████████
           4 |        Nami ████████
           2 |
           0 +--------------------------------------------------

Finance/Resources
          10 |        Nami ████████████████████
           8 |
           6 |
           4 |
           2 |  Zoro ████   Robin ████
           0 +--------------------------------------------------

Intelligence/Security
          10 |                          Robin ████████████████████
           8 |
           6 |
           4 |        Nami ████████████
           2 |  Zoro ████
           0 +--------------------------------------------------

Strategy
          10 |
           8 |
           6 |        Nami ████████████  Robin ██████████████
           4 |  Zoro ████████
           2 |
           0 +--------------------------------------------------
```

---

## Coverage Analysis

| Gap Area | Risk | Mitigation |
|----------|------|-----------|
| Diplomacy / Network | Medium — no dedicated CDO | Robin handles intelligence gathering; Nami negotiates resource deals |
| HR / Wellbeing | Low — small crew | Captain manages crew morale directly |
| Technology / R&D | Low — Zoro executes well | Robin provides research context |

---

## Assignment Guide

When a task arrives, route it as follows:

- Write or modify code → **Zoro**
- Budget approval, priority conflict, route planning → **Nami**
- Security review, threat assessment, research context → **Robin**
- Vision, final call, crew conflicts → **Captain (Luffy)**
