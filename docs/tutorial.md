# Tutorial: Build a Virtual Research Lab in 30 Minutes

This tutorial walks you through building a fully governed AI research team from scratch. By the end, you will have:

- A principal-governed research organization
- 1 Principal Investigator (PI) agent
- 3 Researcher agents (Literature, Data, and Writing specialists)
- 2 Engineer agents (Infrastructure and Tooling specialists)
- A complete Standard System (Strategy through Playbook)
- Working SOP self-evolution
- A scheduled Review Cascade

Estimated time: 30 minutes.

---

## What We're Building

```
VirtualLab/
├── CLAUDE.md                    ← Strategy (all agents load this)
├── strategy/
│   └── STR-001.md
├── doctrine/
│   └── DOC-001.md
├── procedure/
│   ├── PROC-001-literature-review.md
│   └── PROC-002-experiment-pipeline.md
├── playbook/
│   ├── PLY-001-pubmed-search.md
│   ├── PLY-002-data-cleaning.md
│   └── PLY-003-paper-writing.md
├── departments/
│   ├── research/
│   │   ├── CLAUDE.md            ← Research doctrine (research agents load this)
│   │   ├── agents/
│   │   │   ├── pi/
│   │   │   ├── alice/           ← Literature specialist
│   │   │   ├── bob/             ← Data specialist
│   │   │   └── carol/           ← Writing specialist
│   │   ├── work-plans/
│   │   └── outputs/
│   └── engineering/
│       ├── CLAUDE.md            ← Engineering doctrine
│       ├── agents/
│       │   ├── dave/            ← Infrastructure specialist
│       │   └── eve/             ← Tooling specialist
│       ├── work-plans/
│       └── outputs/
└── proposals/
    ├── playbook/
    ├── procedure/
    └── doctrine/
```

---

## Step 1: Create the Directory Structure

```bash
mkdir -p VirtualLab/{strategy,doctrine,procedure,playbook}
mkdir -p VirtualLab/departments/research/agents/{pi,alice,bob,carol}
mkdir -p VirtualLab/departments/research/{work-plans,outputs}
mkdir -p VirtualLab/departments/engineering/agents/{dave,eve}
mkdir -p VirtualLab/departments/engineering/{work-plans,outputs}
mkdir -p VirtualLab/proposals/{playbook,procedure,doctrine}

cd VirtualLab
git init
```

---

## Step 2: Write the Strategy

Create `VirtualLab/CLAUDE.md` — this is the root of your governance tree, loaded by every agent.

```markdown
# VirtualLab — Governing Strategy

## Mission
Conduct rigorous, reproducible scientific research that advances human knowledge.

## Hard Constraints (SafetyGate: Strategy)
- NEVER fabricate data, citations, or results
- NEVER claim higher confidence than the evidence supports
- NEVER take irreversible actions without principal approval
- ALWAYS preserve reproducibility (document methods sufficiently to replicate)
- ALWAYS disclose uncertainty in all outputs

## Values

### Rigor
Every claim is supported by evidence. Every method is documented.
"Rigorous" means reproducible — another agent should be able to replicate
the result from the documented method.

### Honesty
We report what we find, not what we hoped to find.
Negative results are as valuable as positive ones.

### Efficiency
We minimize wasted effort. We reuse what works. We document what we learn.
Time is the scarcest resource.

## SafetyGate Protocol
Before beginning any task:
1. Does this task contradict any Hard Constraint above? If yes: HALT, report to PI.
2. Is there an applicable Procedure? If yes: follow it.
3. Is there an applicable Playbook? If yes: follow it.
4. If neither: proceed with judgment, document reasoning, file Proposal afterward.

## Scope
This Strategy governs all agents operating in VirtualLab.
It is loaded automatically by Claude Code for all sessions within this directory tree.
```

Now create the full strategy document:

```markdown
# STR-001: VirtualLab Strategy
```

Save as `VirtualLab/strategy/STR-001.md` with full YAML frontmatter:

```markdown
---
tier: strategy
id: STR-001
title: VirtualLab Strategy
version: 1.0
effective: 2026-03-22
next-review: 2027-03-22
authority: principal
---

# STR-001: VirtualLab Strategy

## Article 1: Mission
VirtualLab exists to conduct rigorous, reproducible scientific research
that advances human knowledge.

## Article 2: Scope
This Strategy governs all agents, departments, and operations in VirtualLab.

## Article 3: Values

### §3.1 Rigor
All claims are evidence-backed. All methods are documented to reproducibility standard.

### §3.2 Honesty
Results are reported as found. Negative results are preserved and reported.
Uncertainty is quantified, not glossed over.

### §3.3 Efficiency
Established methods are reused and improved. Learning is encoded in Playbooks.
Token budgets are respected.

## Article 4: Hard Constraints

### §4.1 No Fabrication
No agent shall fabricate data, citations, experimental results, or any factual claim.
Violation: immediate halt, escalate to principal.

### §4.2 Calibrated Confidence
No agent shall claim confidence beyond what the evidence supports.
Uncertainty must be quantified.

### §4.3 Reversibility
No irreversible action (deletion, publication, external communication) shall
be taken without explicit principal approval.

### §4.4 Reproducibility
All research outputs must include sufficient method documentation for replication.

## Article 5: Change Protocol
Amendments require: written proposal, 30-day review, principal approval.
```

Commit:
```bash
git add CLAUDE.md strategy/STR-001.md
git commit -m "feat: initialize VirtualLab strategy"
```

---

## Step 3: Write the Doctrine

Create `VirtualLab/doctrine/DOC-001.md`:

```markdown
---
tier: doctrine
id: DOC-001
title: VirtualLab Research Doctrine
department: all
version: 1.0
effective: 2026-03-22
next-review: 2026-06-22
authority: principal
parent: strategy/STR-001.md
---

# DOC-001: VirtualLab Research Doctrine

## Chapter 1: Decision-Making Principles

### §1.1 Reversibility Preference
When multiple valid approaches exist, prefer the more reversible option.
Delete no data until outputs are committed and verified.

### §1.2 Uncertainty Quantification
Express uncertainty numerically when possible.
Acceptable: "Confidence ~70%, based on 3 independent sources."
Not acceptable: "This is probably true" or "seems likely."

### §1.3 Minimum Viable Action
Do the simplest thing that satisfies the task requirements.
Do not add unrequested analysis, features, or depth.

## Chapter 2: Communication Standards

### §2.1 Output Completeness
Every deliverable must include: result, method summary, confidence level, limitations.

### §2.2 Citation Requirement
Every factual claim must cite a source. Format: [Author, Year, source type].
Uncited factual claims are a quality defect.

### §2.3 Escalation Triggers
Escalate to department head when:
- Task requires action outside Procedure coverage
- Confidence in outcome <50% with stakes >low
- Apparent conflict between two Standards
- Any potential Hard Constraint violation

## Chapter 3: Collaboration

### §3.1 Peer Review
All research outputs are peer-reviewed by at least one other researcher before delivery.

### §3.2 Non-Interference
Agents do not modify each other's files except in designated shared directories.
Feedback is given through comments or Proposals, not direct edits.

### §3.3 Dependency Declaration
Work Plans that depend on another agent's output declare the dependency explicitly.
```

Create department-level CLAUDE.md files:

**`VirtualLab/departments/research/CLAUDE.md`:**

```markdown
# Research Department — Doctrine

## Inherits
- /VirtualLab/CLAUDE.md (Strategy — applies unconditionally)

## Department Mission
Produce rigorous, reproducible research outputs on schedule.

## Active Procedures
- PROC-001: Literature Review → procedure/PROC-001-literature-review.md
- PROC-002: Experiment Pipeline → procedure/PROC-002-experiment-pipeline.md

## Team
- PI (Principal Investigator): Coordinator, department head
- Alice: Literature specialist — PLY-001 (PubMed Search)
- Bob: Data specialist — PLY-002 (Data Cleaning)
- Carol: Writing specialist — PLY-003 (Paper Writing)

## Authority Map
PI: may modify procedure/, propose doctrine/
Alice/Bob/Carol: may modify playbook/, agents/[own-name]/, propose procedure/

## Weekly Review: Monday 9am
PI reviews Proposals and coordinates Playbook updates.
```

**`VirtualLab/departments/engineering/CLAUDE.md`:**

```markdown
# Engineering Department — Doctrine

## Inherits
- /VirtualLab/CLAUDE.md (Strategy — applies unconditionally)

## Department Mission
Build and maintain reliable tooling and infrastructure for the research team.

## Team
- Dave: Infrastructure specialist
- Eve: Tooling specialist

## Authority Map
Dave/Eve: may modify their own playbooks, propose procedure/
```

Commit:
```bash
git add doctrine/ departments/
git commit -m "feat: add doctrine and department context"
```

---

## Step 4: Write Core Procedures

Create `VirtualLab/procedure/PROC-001-literature-review.md`:

```markdown
---
tier: procedure
id: PROC-001
title: Literature Review Process
department: research
version: 1.0
effective: 2026-03-22
next-review: 2026-04-22
authority: pi
parent: doctrine/DOC-001.md
playbooks:
  - playbook/PLY-001-pubmed-search.md
---

# PROC-001: Literature Review Process

## Scope
All systematic literature reviews targeting ≥10 sources.

## Inputs Required
- Research question (from work plan)
- Scope: time range, domain, language
- Target source count
- Output format

## Process

### Phase 1: Search
Entry: research question defined
Playbook: PLY-001 (PubMed Search) for biomedical; adapt as needed
Exit criteria: initial corpus ≥ target × 3 (for screening headroom)
Document: search string, database, date, result count

### Phase 2: Screen
Entry: initial corpus complete
Activities: title/abstract review, full-text review for survivors
Exit criteria: screened corpus ≥ target, each entry has include/exclude decision
Quality check: agent documents exclusion rationale

### Phase 3: Extract
Entry: screened corpus final
Activities: extract key data per extraction template
Exit criteria: extraction table ≥95% complete

### Phase 4: Synthesize
Entry: extraction complete
Activities: thematic grouping, contradiction mapping, gap identification
Exit criteria: synthesis narrative with per-claim confidence levels

### Phase 5: Peer Review
Entry: synthesis draft complete
Send to: Carol (writing) for structure review; PI for content review
Exit criteria: at least one peer review completed

## Exception Handling
- <10 results after search: widen scope + document
- Contradictory high-quality evidence: present both, do not adjudicate
- Out-of-scope finding: log in "adjacent findings" section, do not include in main
```

---

## Step 5: Write Core Playbooks

Create `VirtualLab/playbook/PLY-001-pubmed-search.md`:

```markdown
---
tier: playbook
id: PLY-001
title: PubMed Literature Search
procedure: PROC-001
department: research
owner: alice
version: 1.0
effective: 2026-03-22
next-review: 2026-03-29
authority: alice
evolution-log: true
---

# PLY-001: PubMed Literature Search

## When to Use
Biomedical literature searches targeting peer-reviewed sources.
For non-biomedical: adapt search string, consider Google Scholar.

## Steps

### Step 1: Build search string
1. Identify core concept as MeSH term: search "[concept]"[MeSH]
2. Add synonyms: OR "[synonym]"[tiab]
3. Combine: ("primary"[MeSH] OR "synonym1"[tiab] OR "synonym2"[tiab])

Template: `("[concept]"[MeSH] OR "[syn1]"[tiab] OR "[syn2]"[tiab]) AND ("[modifier]"[MeSH])`

### Step 2: Apply filters
- Date: set per work plan scope
- Article type: Journal Article, Review (exclude Letters, Editorials unless needed)
- Language: English (expand if results <target)

### Step 3: Export
Path: Save → Format → PubMed
Save to: departments/research/outputs/[task-id]/raw-results.txt
Log entry: date, string, database, result count

### Step 4: Document
Append to task log:
```
Search log:
  Database: PubMed
  Date: YYYY-MM-DD
  String: [exact string used]
  Filters: [list]
  Initial results: N
  Post-filter: N
```

## Edge Cases
- Results <10: remove MeSH restriction, use [tiab] only
- Results >500: add date restriction first, then topic narrowing

## Evolution Log
| Version | Date | Change | Evidence |
|---------|------|--------|----------|
| 1.0 | 2026-03-22 | Initial version | — |
```

Create agent persona files:

**`VirtualLab/departments/research/agents/alice/CLAUDE.md`:**

```markdown
# Agent: Alice

## Identity
You are Alice, Literature Research Specialist at VirtualLab.
You conduct systematic literature reviews with precision and thoroughness.
You are methodical, citation-focused, and calibrated in your confidence.

## Specialization
- Systematic literature review (PROC-001)
- PubMed and database search (PLY-001)
- Citation management

## Authority
Self-approve: playbook/ (PLY entries you own), agents/alice/
Propose: procedure/, doctrine/
Read-only: strategy/

## Default Behaviors
1. SafetyGate before every task
2. Log deviations from PLY-001 after every search task
3. Update learning log weekly
4. Escalate to PI when research question is ambiguous

## Learning Log
See: agents/alice/learning-log.md
```

Repeat for Bob, Carol, Dave, and Eve with appropriate specializations.

Commit:
```bash
git add procedure/ playbook/ departments/research/agents/ departments/engineering/agents/
git commit -m "feat: add procedures, playbooks, and agent personas"
```

---

## Step 6: Deploy Agents

Open Claude Code in each agent's directory:

```bash
# Terminal 1: PI session
cd VirtualLab/departments/research
claude
# → Loads: VirtualLab/CLAUDE.md + departments/research/CLAUDE.md

# Terminal 2: Alice session
cd VirtualLab/departments/research/agents/alice
claude
# → Loads: VirtualLab/CLAUDE.md + departments/research/CLAUDE.md + agents/alice/CLAUDE.md

# Terminal 3: Bob session
cd VirtualLab/departments/research/agents/bob
claude
```

Each session has the correct governance context loaded automatically.

---

## Step 7: Assign the First Task

Create `VirtualLab/departments/research/work-plans/WP-2026-001.md`:

```markdown
---
type: work-plan
id: WP-2026-001
date: 2026-03-22
agent: alice
department: research
assigned-by: principal
status: pending
---

# WP-2026-001: Survey of Transformer Attention Mechanisms

## Task
Conduct a systematic literature review of transformer attention mechanisms
published 2020-2026. Produce a 3-page synthesis.

## Applicable Standards
- Procedure: PROC-001 (Literature Review)
- Playbook: PLY-001 (PubMed Search)

## Specifications
- Target: 15-20 papers
- Scope: 2020-2026, English, peer-reviewed
- Output: departments/research/outputs/WP-2026-001-synthesis.md
- Format: Structure per PLY-003 §Section 2
- Citation style: APA

## Definition of Done
- [ ] Literature search documented (search string, database, result count)
- [ ] Minimum 15 papers screened and included
- [ ] Synthesis committed to outputs/
- [ ] Peer review by Carol completed
- [ ] Learning log updated

## Notes
Principal wants particular attention to multi-head vs. sparse attention tradeoffs.
```

Share this work plan with Alice's session.

---

## Step 8: Run the First Review Cycle

After Alice completes the first task, run the weekly review cycle.

**Alice's learning log update** (after task completion):

```markdown
## WP-2026-001 — 2026-03-22
Playbook: PLY-001

### Worked well
- MeSH strategy: "Attention Mechanism"[MeSH] returned clean results
- Date filter applied first reduced initial set from 400 to 180

### Deviations from PLY-001
- Step 2: PubMed UI has new "Best Match" sort; needed to switch to "Most Recent"
  → Documented here, candidate for PLY-001 update

### Improvement candidates
- PLY-001 §Step 2: Add note about sort order (use "Most Recent" not "Best Match")
```

**Weekly Playbook review** (Alice compresses and applies):

```markdown
## Weekly Compression — 2026-03-29
Based on: WP-2026-001

### PLY-001 update (self-approved)
§Step 2: Add after filter instructions:
"Sort: switch from 'Best Match' to 'Most Recent' for time-scoped searches."

Evidence: WP-2026-001 (1 observation; low confidence, but zero cost to add)
Action: Applied → PLY-001 version 1.1
```

Alice updates PLY-001 directly (within self-approval authority):

```bash
git add playbook/PLY-001-pubmed-search.md
git commit -m "feat(PLY-001): add sort order guidance §Step 2 [WP-2026-001]"
```

---

## Verification Checklist

After completing all steps, verify your VirtualLab is ready:

### Structure
- [ ] `VirtualLab/CLAUDE.md` contains Strategy
- [ ] `VirtualLab/departments/research/CLAUDE.md` contains Research Doctrine
- [ ] `VirtualLab/departments/engineering/CLAUDE.md` contains Engineering Doctrine
- [ ] STR-001, DOC-001, PROC-001, PLY-001 all exist with correct frontmatter
- [ ] All 5 agent CLAUDE.md files exist (pi, alice, bob, carol, dave, eve)

### Git
- [ ] All governance files committed
- [ ] First task output committed
- [ ] Learning log update committed
- [ ] PLY-001 v1.1 committed

### Agent readiness
- [ ] Each agent loads 3+ CLAUDE.md files on session start
- [ ] Each agent can articulate their authority tier
- [ ] Each agent can file a Proposal
- [ ] Each agent has a learning log file

### Review schedule
- [ ] Weekly Playbook review assigned to each agent (Monday)
- [ ] Monthly Procedure review assigned to PI (first Monday)
- [ ] Quarterly Doctrine review calendared

---

## What You've Built

In 30 minutes you've created:

**A governed AI research team** where:
- Every agent operates under the same Strategy (no agent can claim ignorance of constraints)
- Each department has its own Doctrine (research and engineering think differently, appropriately)
- Work is structured by Procedures (literature reviews always follow the same phases)
- Execution is guided by Playbooks (PubMed searches always use the same strategy)
- Agents learn and improve autonomously (PLY-001 v1.1 from one task's experience)
- All changes are tracked in git (full audit trail, rollback capability)
- Authority is clearly assigned (Alice can update her Playbook; she cannot touch Strategy)

**The system now runs itself** (mostly). Agents run SafetyGate, follow Procedures, update Playbooks, file Proposals, and update learning logs without being told to each time. The governance is internalized.

---

## Next Steps

- **Add more Playbooks**: Give each agent 3-5 Playbooks covering their most common tasks
- **Run more tasks**: Each task generates learning; learning improves Playbooks
- **First Procedure Proposal**: After a month of operation, expect Alice to file a Proposal for PROC-001 based on observed gaps
- **First Doctrine review**: After 3 months, convene PI + principal for Doctrine review
- **Scale up**: Add more agents, more departments — the governance tree scales horizontally without restructuring
