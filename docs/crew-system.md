# The Crew System: Agent Management

The Crew System is the operational layer of Praxeology. It covers how agents are created, governed, and how they learn over time. The Crew System turns the Standard System's documents into living, executing agents.

---

## The CLAUDE.md Hierarchy Mechanism

### How it works

Claude Code automatically loads `CLAUDE.md` files from the current working directory up to the filesystem root when a session starts. Praxeology exploits this mechanism to deliver governance context to agents without any manual prompt engineering.

```
File system                    What gets loaded (for agent in /org/departments/research/)
─────────────────────────────────────────────────────────────────────────────────────────
/                              (none — no CLAUDE.md here)
/Users/neo/                    ~/.claude/CLAUDE.md (user-global, if exists)
/Users/neo/neomakes/           (none)
/path/to/praxeology/                   (none)
/org/                          CLAUDE.md  ← Strategy (loads for ALL agents)
/org/departments/              CLAUDE.md  ← Dept roster (optional)
/org/departments/research/     CLAUDE.md  ← Research Doctrine (loads for research agents)
```

**The result**: An agent that opens a file in `/org/departments/research/` automatically has:
1. Org-level Strategy
2. Research department Doctrine
3. All of the above without any prompt engineering by the user

**Scoping is automatic**: A research agent never sees the Engineering department's CLAUDE.md unless its working directory is also in Engineering's path. Governance is scoped by filesystem location.

### What to put in each CLAUDE.md level

**Root org CLAUDE.md** — Strategy tier content:
```markdown
# [Org Name] — Governing Strategy

## Mission
[One sentence]

## Hard Constraints
- NEVER do X
- NEVER do Y
- ALWAYS do Z

## Values
[3-7 values with operational definitions]

## SafetyGate
Before every action, verify compliance with this Strategy.
If violation detected: HALT, log, escalate.
```

**Department CLAUDE.md** — Doctrine tier content:
```markdown
# [Department] — Doctrine

## Inherits
- /org/CLAUDE.md (Strategy — applies unconditionally)

## Department Mission
[One sentence specific to this department]

## Decision Principles
[How to reason when procedures don't cover the case]

## Communication Standards
[How to format outputs, how to escalate]

## Authority Map
You are authorized to:
- Self-approve changes to: playbook/, work-plans/, agents/[your-name]/
- Propose changes to: procedure/
- Read (not modify): doctrine/, strategy/

## Current Procedures
- PROC-[N]: [title] → procedure/[file].md
```

**Agent subdirectory CLAUDE.md** — Agent identity and persona:
```markdown
# Agent: [Name]

## Identity
You are [Name], [role] at [Org Name].

## Specialization
[What you're expert in, what you're not]

## Current Assignments
[Active work plans]

## Learning Log
See: agents/[name]/learning-log.md
```

### CLAUDE.md vs. Standard documents

CLAUDE.md files contain governance summaries and agent identity. The full Standard documents (STR, DOC, PROC, PLY) live in their respective directories. CLAUDE.md serves as the entry point that orients agents and directs them to the full documents when detail is needed.

Do not put 50-clause Procedures in CLAUDE.md. Put a summary and a reference: "Literature reviews follow PROC-001. See `procedure/literature-review.md`."

---

## Agent Persona Design

### The three components of a persona

Every agent needs three components to function within the Crew System:

**1. Identity** — who the agent is
```markdown
You are Maya, a data analyst at Nexus Research.
You have deep expertise in statistical analysis and data visualization.
You work primarily in the Analytics department.
```

**2. Authority tier** — what the agent can self-approve
```markdown
Authority tier: Playbook
- You may modify: playbook/, agents/maya/
- You must propose (not modify): procedure/, doctrine/, strategy/
- All Proposals go to: proposals/[tier]/
```

**3. Behavioral defaults** — how the agent operates by default
```markdown
Default behaviors:
- Always run SafetyGate before beginning any task
- Always document deviations from Playbook steps
- Always update learning log after task completion
- Escalate to department head when uncertainty >40% on consequential decisions
```

### Persona template

```markdown
---
type: agent-persona
name: [Name]
role: [Job title]
department: [Department]
authority-tier: playbook | procedure | doctrine
created: [YYYY-MM-DD]
---

# Agent Persona: [Name]

## Identity
You are [Name], [role] at [Org Name]. [2-3 sentences describing background,
specialty, and working style.]

## Core Competencies
- [Competency 1]: [Brief description]
- [Competency 2]: [Brief description]
- [Competency 3]: [Brief description]

## Authority
Self-approve: playbook/, agents/[name]/
Propose: procedure/, doctrine/
Read-only: strategy/

## Default Behaviors
1. SafetyGate before every task
2. Document deviations from Playbook
3. Update learning log after every task
4. Escalate when: [specific conditions]

## Escalation Path
1. Self-resolve (within Playbook authority)
2. Peer consultation (same department)
3. Department head
4. Principal

## Communication Style
[How this agent writes: formal/informal, length, citation style]
```

### Specialization vs. generalization

Agents with narrow specialization outperform generalists on their specialty tasks but fail on edge cases outside their scope. Agents with broad scope handle novel situations better but lack depth.

**Recommended pattern**: One generalist "coordinator" agent per department with broad Doctrine, several specialist agents with narrow Playbooks. The coordinator handles novel cases; specialists handle volume work.

```
Research Department
│
├── Coordinator (wide scope, Doctrine-level authority)
│   - Novel task triage
│   - Proposal review
│   - Department head liaison
│
├── Literature Analyst (specialist)
│   - Playbook: literature-search, citation-management
│   - Deep expertise, narrow scope
│
├── Data Analyst (specialist)
│   - Playbook: statistical-analysis, visualization
│   - Deep expertise, narrow scope
│
└── Report Writer (specialist)
    - Playbook: report-writing, editing
    - Deep expertise, narrow scope
```

---

## SOP Self-Evolution (Learn → Compress → Apply)

The SOP Self-Evolution cycle is the mechanism by which agents improve their Playbooks over time without requiring manual intervention from principals. It is the primary feedback loop between operational experience and documented guidance.

### The three phases in detail

#### Phase 1: Learn

After every task, the agent appends to its learning log. The learning log is a running record of operational observations.

**Learning log format:**

```markdown
## Task: WP-2026-042
Date: 2026-03-22
Playbook used: PLY-007 (PubMed Search)

### What worked
- MeSH term strategy yielded precise results (18/20 papers relevant)
- Adding "[Systematic Review]"[pt] filter eliminated 60% of noise

### What deviated from Playbook
- Step 3 (export): PubMed UI changed, export now under "Save" not "Export"
  → Used new path, documented here

### What failed
- Initial search string too broad (847 results before filters)
  → Narrowed with date filter first, then applied topic filters

### Edge cases encountered
- (none)

### Improvement candidates
- PLY-007 §Step 3: Update UI path for export
- PLY-007 §Step 1: Add guidance for broad initial results
```

The agent does not modify PLY-007 at this point. It only records observations.

#### Phase 2: Compress

At the weekly Playbook review, the agent reads through accumulated learning log entries and extracts actionable patterns.

**Compression questions:**
1. Does any deviation appear more than once? → Candidate for Playbook update
2. Does any workaround consistently outperform the documented step? → Candidate for step replacement
3. Does any failure pattern suggest a missing guardrail? → Candidate for new step
4. Does any edge case reveal a gap in the current Playbook? → Candidate for edge case section

**Compression output:**

```markdown
## Weekly Compression: 2026-03-22

### Proposed PLY-007 changes
Based on 6 tasks this week:

1. §Step 3 UI path outdated (observed 4/6 tasks)
   Current: "Export" menu
   Actual: "Save" → "Format" → "PubMed"
   Confidence: High (4 consistent observations)

2. §Step 1 lacks guidance for >200 result sets (observed 3/6 tasks)
   Recommendation: Add step to apply date filter before topic filters
   when initial results >200
   Confidence: Medium (3 observations, no contradictions)
```

#### Phase 3: Apply

The agent drafts a Playbook Proposal incorporating the compressed changes.

For Playbook changes (within self-approval authority):
- Draft the updated PLY document
- Commit with message referencing the learning log entries
- Version bump (minor version)
- Update `next-review` date

For Procedure changes (above self-approval authority):
- Draft a PROP document
- Submit to department head queue
- Do not modify the Procedure directly

**Self-evolution is bounded.** An agent cannot use self-evolution to expand its own authority, modify documents above Playbook tier, or remove constraints. Any proposed change that touches Procedure or above requires the Proposal mechanism.

### Evolution log in Playbooks

Every Playbook maintains an evolution log that records what changed and why:

```markdown
## Evolution Log

| Version | Date | Change Summary | Evidence (task IDs) |
|---------|------|----------------|---------------------|
| 3.2 | 2026-03-22 | Updated export path §Step 3 | WP-042, WP-043, WP-044, WP-047 |
| 3.1 | 2026-03-15 | Added broad-results guidance §Step 1 | WP-035, WP-038 |
| 3.0 | 2026-03-01 | Switched to MeSH-first approach | WP-030 (precision +40%) |
```

This log enables reviewers to evaluate whether the evolution is evidence-based and consistent.

---

## Review Cascade

The Review Cascade is the scheduled audit cycle that keeps the governance system aligned with operational reality. Each tier has its own review cadence.

### Daily: Work Plan Retrospective

**Who**: Each agent, autonomously.
**When**: After each task completion (or end of work day).
**Duration**: 5-15 minutes.
**Output**: Learning log entry.

```markdown
## Retrospective template

Task: [WP-ID]
Outcome: [completed | partial | failed]
Playbook adherence: [full | deviated | no playbook applicable]
Deviations: [list or "none"]
Improvement candidates: [list or "none"]
```

### Weekly: Playbook Review

**Who**: Each agent for their own Playbooks; department coordinator reviews all department Playbooks.
**When**: Monday morning (or designated day).
**Duration**: 30-60 minutes.
**Output**: Playbook updates (self-approved) or Proposals (for higher tiers).

Checklist:
- [ ] Review learning log entries from past week
- [ ] Run Compress phase for each active Playbook
- [ ] Draft and apply self-approved updates
- [ ] File Proposals for any above-Playbook changes
- [ ] Update `next-review` dates

### Monthly: Procedure Review

**Who**: Department head + senior agents.
**When**: First Monday of each month.
**Duration**: 2-4 hours for the department.
**Output**: Procedure updates, Doctrine Proposals if needed.

Checklist:
- [ ] Review all Proposals submitted since last review
- [ ] Accept / reject / request revision for each Proposal
- [ ] Review Procedures for alignment with actual operations
- [ ] Check for Procedure gaps (work being done without Procedure coverage)
- [ ] File Doctrine Proposals for systemic issues
- [ ] Update Procedure version numbers and review dates

### Quarterly: Doctrine Review

**Who**: Department heads + principal.
**When**: First week of each quarter.
**Duration**: Half-day to full-day.
**Output**: Doctrine updates, Strategy Proposals if needed.

Checklist:
- [ ] Review all Doctrine-level Proposals from past quarter
- [ ] Assess whether Doctrine still matches operational reality
- [ ] Review for consistency across departments
- [ ] Identify emerging patterns that suggest Doctrine gaps
- [ ] Update Doctrine version and review dates
- [ ] File Strategy Proposals for fundamental changes

### Annual: Strategy Review

**Who**: Principal (with optional external review).
**When**: Once per year (set a fixed date).
**Duration**: Full day.
**Output**: Strategy updates (rare), Doctrine direction.

Checklist:
- [ ] Review mission statement: still accurate?
- [ ] Review hard constraints: still the right constraints?
- [ ] Review values: still reflect actual practice?
- [ ] Assess Strategy-Doctrine alignment across all departments
- [ ] Update Strategy if needed (rare; treat as significant event)
- [ ] Issue "Annual Strategic Guidance" memo to all departments

### Cascade propagation

When a higher tier changes, review propagates downward:

```
Strategy change
  → Triggers: Doctrine audit (within 2 weeks)
      → Triggers: Procedure audit (within 1 month)
          → Triggers: Playbook audit (within 2 weeks after Procedure)
```

Agents responsible for lower tiers receive a notification: "Strategy updated. Review [your tier] for alignment within [timeframe]."

---

## Feedback Loops

### Principal feedback

The principal is the ultimate authority and the primary source of high-level feedback. Principal feedback loops:

**Direct instruction**: The principal issues work plans or amendments to Standards directly.

**Review approval**: The principal reviews and approves Doctrine and Strategy Proposals.

**Performance review**: Periodic review of department outputs, with feedback routed to department heads.

**Intervention**: When SafetyGate violations or major misalignments occur, the principal intervenes directly.

**Principal feedback format:**

```markdown
---
type: principal-feedback
date: 2026-03-22
recipient: research-department
subject: Synthesis quality
---

## Observation
Recent syntheses (WP-035, WP-040, WP-042) lack explicit uncertainty quantification.
Confidence levels are stated informally ("seems likely") rather than numerically.

## Direction
Update PROC-001 §Phase 4 (Synthesize) to require numerical confidence per finding.
Reference: DOC §1.2 (Uncertainty Disclosure).

## Priority: High
Implement by: 2026-04-01
```

### Peer feedback

Agents can provide feedback to peers — but only through structured channels, never by modifying each other's files.

**Peer feedback channels:**

1. **Inline comments**: On shared outputs (e.g., git comments on committed files)
2. **Peer review requests**: Agent explicitly requests review from a peer
3. **Department retrospectives**: Structured team retrospective (monthly)
4. **Proposal co-authoring**: Two agents co-author a Proposal

**Peer feedback does not bypass the hierarchy.** A peer cannot instruct another agent to deviate from a Procedure. Peer feedback informs; authority decides.

---

## Budget Minimization (Token Economy)

Running AI agents has a cost measured in tokens. The Crew System is designed to minimize this cost without sacrificing governance quality.

### Model routing

Not all tasks require the same model capability. Route tasks to the minimum-sufficient model:

| Task Type | Recommended Model | Rationale |
|-----------|-------------------|-----------|
| Simple playbook execution | haiku | Low complexity, high volume |
| Standard research tasks | sonnet | Balanced capability/cost |
| Doctrine-level reasoning | sonnet | Sufficient for most cases |
| Strategy amendments, complex analysis | opus | Complexity justifies cost |
| Proposal review (high stakes) | opus | Stakes justify cost |

**Routing heuristic:**
```
task_complexity = estimate complexity (low/medium/high)
task_stakes = estimate if error is recoverable (yes/no)

if complexity == low and stakes recoverable: haiku
if complexity == medium or stakes recoverable: sonnet
if complexity == high or stakes not recoverable: opus
```

### Context minimization

An agent's context window is a resource. Minimize unnecessary context loading:

**Load lazily**: Do not include full Procedure text in every session. Reference the Procedure and load it only when executing that procedure.

**Summarize upward**: When long outputs are produced, also produce a summary. Future sessions reference the summary; they load the full output only when needed.

**Scope CLAUDE.md tightly**: Put department Doctrine in department CLAUDE.md, not org CLAUDE.md. Agents in Engineering do not need Research Doctrine.

**Work Plan as scope**: Each work plan specifies exactly which Procedures and Playbooks apply. The agent loads those specific documents, not the full Playbook library.

### Batching and parallelism

When multiple independent tasks are available, run them in parallel. The Crew System supports parallel execution at the Work Plan level.

```
Department Queue
│
├── WP-050 (unblocked) → Agent A (running)
├── WP-051 (unblocked) → Agent B (running)
├── WP-052 (blocked on WP-050) → waiting
└── WP-053 (unblocked) → Agent C (running)
```

**Dependency tracking**: Work Plans declare their dependencies in frontmatter:

```yaml
---
type: work-plan
id: WP-052
depends-on: WP-050
---
```

A coordinator agent (or the principal) sequences work plans respecting dependencies.

### Learning amortization

The SOP self-evolution cycle amortizes the cost of learning across tasks. Rather than re-solving the same problem each time, agents encode solutions into Playbooks. Future tasks that use that Playbook benefit from prior learning at zero additional cost.

This is the primary budget efficiency mechanism in the Crew System: **the more a Playbook is used, the cheaper each use becomes** (relative to a world with no Playbook).

Implication: Invest effort in Playbook quality for high-frequency tasks. A well-crafted Playbook for a task that runs 100 times per month saves far more than it costs to create.
