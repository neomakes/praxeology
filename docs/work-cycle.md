# Work Cycle System

Agent work cycles in Praxeology-governed teams are structured around two planning files, a layered reporting cadence, and a feedback loop that feeds improvements back into the Standard system.

---

## 1. weekly.json — Weekly Task Plan

Created each Sunday morning before the week starts. The crew-manager dashboard renders this automatically.

**Schema**

```json
{
  "week": "2026-W13",
  "mon": [{"task": "description", "priority": "high|mid|low"}],
  "tue": [],
  "wed": [],
  "thu": [],
  "fri": []
}
```

**Fields**

| Field | Type | Description |
|-------|------|-------------|
| `week` | string | ISO week identifier (YYYY-Www) |
| `mon`–`fri` | array | Ordered task list for each weekday |
| `task` | string | Short description of the work item |
| `priority` | enum | `high`, `mid`, or `low` |

**Usage rules**

- One file per crew member per week.
- Tasks are listed in execution order within each day.
- Saturday and Sunday are not included — weekly planning only covers the work week.
- This file is the source of truth for what was planned. Do not retroactively edit it after the day passes.

---

## 2. todo.json — Daily Task Tracker

Derived from `weekly.json` each morning. Breaks the day's planned items into actionable, trackable tasks.

**Schema**

```json
{
  "date": "2026-03-25",
  "tasks": [
    {
      "id": 1,
      "task": "description",
      "status": "pending|in_progress|done|blocked",
      "priority": "high|mid|low",
      "notes": "context for session continuity"
    }
  ]
}
```

**Fields**

| Field | Type | Description |
|-------|------|-------------|
| `date` | string | ISO date (YYYY-MM-DD) |
| `id` | integer | Sequential task ID within the day |
| `task` | string | Task description |
| `status` | enum | `pending`, `in_progress`, `done`, `blocked` |
| `priority` | enum | `high`, `mid`, or `low` |
| `notes` | string | Optional. Session continuity context |

**The `notes` field**

The `notes` field is the most operationally critical part of this schema. Its purpose is session continuity — when a session ends via `/clear` or a context window restart, the next session must be able to resume without losing state. Use it to record:

- What was completed within a task (partial progress)
- Why a task is blocked and what the next action is
- References to files, commits, or external resources touched
- Decisions made mid-task that affect downstream work

An agent that leaves `notes` empty on in-progress or blocked tasks creates unnecessary re-investigation work in the next session.

---

## 3. Reporting Cycle (PRC-202)

Reports are stored in `reports/YYYY-MM-DD.md` within each crew's working directory.

### Daily

Filed at end of each work session.

- Completed items
- In-progress items with current state
- Blocked items with blocker description
- Standard Gap notes (see Section 5)
- Token efficiency memo
- Plan for tomorrow

### Weekly

Filed Sunday morning, before writing the next week's `weekly.json`.

- Summary of the completed week
- Next week's `weekly.json` written and committed
- `sop.md` updated to reflect any procedural changes
- Proposal candidates identified from accumulated Standard Gap notes

### Monthly

- Trend analysis across daily reports
- SOP review for relevance and accuracy
- Budget actuals compared to plan
- Formal Proposal submission for any recurring Standard Gaps

### Quarterly

- Goal achievement rate assessment
- Full SOP review and revision
- Standard amendment batch submitted for Founder approval

### Semi-annual

- Crew structure review
- Full Standard effectiveness evaluation across all documents

### Annual

- Full retrospective
- Next year plan drafted
- SOP full reset considered

---

## 4. Daily Report Format (PLY-201)

**File:** `reports/YYYY-MM-DD.md`

```markdown
# Daily Report — YYYY-MM-DD

## Completed
- [task description] — [brief outcome]

## In Progress
- [task description] — [current state, next action]

## Blocked
- [task description] — [blocker, what is needed to unblock]

## Standard Gap
- [observed gap, which Standard document is affected]

## Token Memo
- [session token usage estimate, any cost anomalies]

## Tomorrow Plan
- [1-3 priority items for the next session]
```

All six sections are required. An empty section uses a single dash (`-`) to mark it explicitly as none.

---

## 5. Standard Gap Reverse Flow (PLY-203)

When a crew member encounters a situation where the existing Standard documents are insufficient, ambiguous, or incorrect, that gap must be recorded and eventually fed back into the Standard system. This is the reverse flow.

```
Daily gap memo
  → Weekly proposal candidate
    → Monthly formal Proposal
      → Founder approval
        → Standard version bump
          → Affected SOP files synced
```

**Step-by-step**

1. **Daily**: At end-of-day, note any situation where Standard guidance was missing or wrong. Record in the `Standard Gap` section of the daily report. Example: "PRC-201 does not cover session handoff when context exceeds 75% — had to improvise."

2. **Weekly**: Review the week's gap notes. If a gap appeared more than once or caused real workflow friction, mark it as a Proposal candidate in the weekly report.

3. **Monthly**: Formalize recurring Proposal candidates into a written Proposal. Submit to Founder for review.

4. **Founder approval**: Founder reviews and either approves, rejects, or requests revision.

5. **Standard version bump**: Approved Proposals result in an increment to the relevant Standard document's version number and a documented change entry.

6. **SOP sync**: All crew members whose `sop.md` references the amended Standard update their files within one work session of the amendment being published.

**Escalation rule**: If Founder feedback on the same issue has occurred 3 or more times without a Standard amendment, submitting a formal Proposal is mandatory, not optional.

---

## File Locations

```
{crew-dir}/
  weekly.json          Current week's plan
  todo.json            Today's task list
  reports/
    YYYY-MM-DD.md      Daily reports
  sop.md               Crew-specific procedures (Standard-synced)
```
