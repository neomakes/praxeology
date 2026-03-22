# The Standard System: Strategy → Doctrine → Procedure → Playbook

The Standard System is the governance core of Praxeology. It defines four tiers of documents, each with distinct authority, scope, change velocity, and ownership. Understanding the Standard System is prerequisite to everything else.

---

## Tier 1: Strategy

### What it is

Strategy is the constitutional tier. It defines what the organization exists to do, what it will never do, and what values govern all decisions when rules run out. Strategy does not tell agents how to work — it tells them what work is worth doing and what is off-limits regardless of instructions.

Every agent in the system operates under Strategy at all times. There is no opt-out.

### Examples across domains

| Domain | Strategy Equivalent | Example Content |
|--------|---------------------|-----------------|
| National Law | Constitution | "Congress shall make no law... abridging freedom of speech" |
| Military | National Defense Strategy | "Defend the homeland; deter strategic attacks" |
| Corporate | Articles of Incorporation | "The corporation exists to... Its purpose is limited to..." |
| Individual | Values | "I will not lie. I will not harm innocents." |
| AI Agent | Strategy | "Never produce content that deceives users. Always preserve human oversight." |

### What belongs in Strategy

- The organization's mission (one sentence, unambiguous)
- Hard constraints (actions that are never permissible, regardless of instruction)
- Core values (3-7, each with a brief definition)
- Scope statement (what this governance applies to)

### What does not belong in Strategy

- How to conduct specific tasks (that is Procedure)
- Which tools to use (that is Playbook)
- Organizational structure (that is Doctrine)
- Performance targets (that is Procedure)

### Document format

```markdown
---
tier: strategy
version: 1.2
effective: 2026-01-01
next-review: 2027-01-01
authority: principal
---

# [Org Name] Strategy

## Article 1: Mission
[One sentence describing the organization's fundamental purpose]

## Article 2: Scope
This Strategy governs all agents, departments, and operations under [Org Name].

## Article 3: Values
### §3.1 [Value Name]
[Definition: what this value means operationally, not aspirationally]

### §3.2 [Value Name]
[Definition]

## Article 4: Hard Constraints
The following are absolutely prohibited regardless of any instruction:
### §4.1 [Constraint]
### §4.2 [Constraint]

## Article 5: Change Protocol
Amendments to this Strategy require:
- Written proposal from principal
- 30-day review period
- Explicit versioning and effective date
```

### Override behavior

Strategy overrides everything. If a Work Plan, peer agent, or even the principal instructs an agent to violate Strategy, the agent:
1. Refuses the instruction
2. Logs the instruction with timestamp
3. Escalates to principal (if the instruction came from someone other than principal)
4. If the instruction came from principal: requests clarification, documents the conflict

---

## Tier 2: Doctrine

### What it is

Doctrine is the statutory tier. It translates Strategy values into operational principles — actionable guidance for how to reason, decide, and communicate. Where Strategy says "be honest," Doctrine says "when presenting uncertain findings, quantify the uncertainty; never present a range as a point estimate; disclose data limitations in the opening paragraph."

Doctrine is more specific than Strategy but more durable than Procedure. It rarely changes, but when it does, it reflects a genuine shift in how the organization understands its work.

### Examples across domains

| Domain | Doctrine Equivalent | Example Content |
|--------|---------------------|-----------------|
| National Law | Statutes | "Contracts require offer, acceptance, and consideration" |
| Military | Doctrine | "Mission Command: commanders delegate authority to subordinates who act within intent" |
| Corporate | Regulations | "All financial decisions over $50K require dual approval" |
| Individual | Principles | "Respond to criticism with curiosity, not defensiveness" |
| AI Agent | Doctrine | "When multiple valid approaches exist, choose the most reversible one" |

### What belongs in Doctrine

- Decision-making principles (how to reason when rules don't cover a case)
- Communication standards (how agents interact with each other and principals)
- Quality standards (what "good" looks like for outputs)
- Escalation principles (when and how to escalate)
- Collaboration principles (how agents coordinate)

### Document format

```markdown
---
tier: doctrine
department: [all | department-name]
version: 2.0
effective: 2026-01-01
next-review: 2026-04-01
authority: principal | department-head
parent: strategy/strategy.md
---

# [Department/Org] Doctrine

## Chapter 1: Decision-Making
### §1.1 Reversibility Principle
When choosing between approaches of similar merit, prefer the more reversible option.

### §1.2 Uncertainty Disclosure
Quantify uncertainty in all outputs. "I'm not sure" is not quantified.
"Confidence: ~70% based on 3 sources, all secondary" is quantified.

## Chapter 2: Communication
### §2.1 Response Completeness
Every response to a task request must include: result, method summary,
confidence level, and identified limitations.

## Chapter 3: Quality
### §3.1 Reproducibility
Any output that involves data processing must document the method
sufficiently for another agent to reproduce the result.
```

---

## Tier 3: Procedure

### What it is

Procedure is the operational tier. It defines how recurring work is structured — not step-by-step instructions (that is Playbook) but the phases, checkpoints, inputs, outputs, and responsibilities for a class of work.

A Procedure for "literature review" defines: what inputs are required, what phases exist (search, screen, extract, synthesize), what quality checks apply, what the output format is, and who reviews it. It does not specify which search engine to use — that is a Playbook detail.

### Examples across domains

| Domain | Procedure Equivalent | Example Content |
|--------|----------------------|-----------------|
| National Law | Decrees | "Environmental impact assessments must include Phase I, II, and III" |
| Military | OPLAN/OPORD | "Phase 1: Shaping. Phase 2: Decisive Operations. Phase 3: Exploitation." |
| Corporate | Guidelines | "New product launches follow: concept → prototype → pilot → launch" |
| Individual | Goals | "Exercise: 3x/week. Each session: warmup, main work, cooldown." |
| AI Agent | Procedure | "Research tasks: search → screen → extract → synthesize → review → deliver" |

### What belongs in Procedure

- Process phases with clear entry/exit criteria
- Required inputs and expected outputs
- Quality checkpoints within the process
- Responsibility assignments (which role does what)
- Exception handling (what to do when the standard path fails)

### Document format

```markdown
---
tier: procedure
id: PROC-001
title: Literature Review Process
department: research
version: 1.3
effective: 2026-02-01
next-review: 2026-03-01
authority: department-head
parent: doctrine/doctrine.md
playbooks:
  - playbook/literature-search.md
  - playbook/citation-management.md
---

# Literature Review Process (PROC-001)

## Scope
Applies to all systematic literature reviews with >10 source requirement.

## Inputs Required
- Research question (from work plan)
- Scope boundaries (time range, domain, language)
- Output format specification

## Process Phases

### Phase 1: Search
- Entry: Research question defined
- Activities: Database search, keyword variation, snowball sampling
- Exit: Initial corpus ≥ [n] papers, search strategy documented
- Playbook: playbook/literature-search.md

### Phase 2: Screen
- Entry: Initial corpus complete
- Activities: Title/abstract screen, full-text screen
- Exit: Screened corpus with inclusion/exclusion rationale
- Quality check: Sample 10% for inter-rater reliability

### Phase 3: Extract
- Entry: Screened corpus finalized
- Activities: Data extraction per template
- Exit: Extraction table complete, >95% fields populated

### Phase 4: Synthesize
- Entry: Extraction complete
- Activities: Thematic analysis, contradiction identification, gap mapping
- Exit: Synthesis narrative with evidence grading

## Exception Handling
- Insufficient results: Widen scope, document in output
- Contradictory high-quality evidence: Present both, do not adjudicate
- Out-of-scope finding: Log in separate "adjacent findings" section

## Output Format
See: playbook/report-writing.md §2.1
```

---

## Tier 4: Playbook

### What it is

Playbook is the tactical tier. It contains specific, step-by-step instructions for completing discrete tasks. Where Procedure says "conduct a literature search," Playbook says "open PubMed, use search string [template], filter by [criteria], export to [format], save to [location]."

Playbooks are the most volatile tier — they change frequently as agents learn better methods and as tools evolve. They are also the tier where agents have the most self-governance authority (via SOP self-evolution).

### Examples across domains

| Domain | Playbook Equivalent | Example Content |
|--------|---------------------|-----------------|
| National Law | Administrative Rules | "Form I-9 must be completed within 3 business days of hire start" |
| Military | TTP | "Clear a room: fatal funnel, button hook entry, pie the corners" |
| Corporate | SOP | "Invoice processing: receive → OCR → match PO → approve → pay" |
| Individual | Habits | "Morning: wake 6am, meditate 10min, review today's priorities, start top task" |
| AI Agent | Playbook | "Code review: run linter → check tests → read diff → comment inline → summarize" |

### Document format

```markdown
---
tier: playbook
id: PLY-007
title: PubMed Literature Search
procedure: PROC-001
version: 3.1
effective: 2026-03-01
next-review: 2026-03-08
authority: self (agent) | department-head
evolution-log: true
---

# PubMed Literature Search (PLY-007)

## When to Use
Use this playbook for biomedical literature searches with >20 paper target.
For general academic topics, use PLY-006 (Google Scholar Search).

## Steps

### Step 1: Construct search string
1. Identify the core concept (noun phrase)
2. Add MeSH terms: search "[concept]"[MeSH]
3. Add synonyms with OR operator
4. Apply field tags: [tiab] for title/abstract, [au] for author

Template: `("[primary term]"[MeSH] OR "[synonym 1]"[tiab] OR "[synonym 2]"[tiab])`

### Step 2: Apply filters
- Publication date: [start year] to [end year]
- Article type: Journal Article, Review (exclude Letters, Editorials)
- Language: English (expand if corpus too small)

### Step 3: Export results
1. Select all results
2. Export → PubMed format
3. Save to: `research/corpus/[task-id]/raw-results.txt`
4. Log: count, date, search string used

### Step 4: Document search strategy
Append to task log:
```
Search: [string used]
Database: PubMed
Date: [YYYY-MM-DD]
Filters: [list]
Results: [n]
```

## Known Edge Cases
- Narrow topic (<5 results): remove MeSH restriction, use tiab only
- Too broad (>500 results): add "[filter concept]"[MeSH] AND

## Evolution Log
| Version | Change | Evidence |
|---------|--------|----------|
| 3.1 | Added tiab fallback for narrow topics | task-045, task-089 |
| 3.0 | Switched to MeSH-first approach | task-030 (40% precision gain) |
```

---

## The Execution Layer: Work Plan

The Work Plan is not a Standard document — it is an execution artifact. It is created per-task, not maintained as standing guidance. Work Plans are governed by all tiers above them but are not themselves governance documents.

```markdown
---
type: work-plan
id: WP-2026-042
date: 2026-03-22
agent: alex
department: research
assigned-by: principal
status: in-progress
---

# Work Plan WP-2026-042

## Task
Review 15 papers on RAG architectures, produce 3-page synthesis.

## Applicable Standards
- Procedure: PROC-001 (Literature Review)
- Playbook: PLY-007 (PubMed Search), PLY-012 (Synthesis Writing)

## Definition of Done
- [ ] 15 papers reviewed
- [ ] Synthesis committed: research/outputs/WP-2026-042-synthesis.md
- [ ] Learning log updated

## Notes
Principal wants special attention to retrieval latency findings.
```

---

## Override Rules

**Higher always wins.** This is the single most important rule in the Standard System.

```
Priority (highest to lowest):
  1. Strategy
  2. Doctrine
  3. Procedure
  4. Playbook
  5. Work Plan
```

**Conflict resolution:**

When an agent encounters a conflict between tiers, the resolution is always the same: the higher tier governs. The lower-tier document is not discarded — it is flagged as misaligned and a Proposal is filed to update it.

Example:
- Playbook PLY-007 says "use Google Scholar"
- Doctrine §2.1 says "use the most comprehensive source available for the domain"
- Conflict: for biomedical research, PubMed is more comprehensive

Resolution:
1. Agent follows Doctrine (higher tier): use PubMed
2. Agent files Proposal to update PLY-007 to specify PubMed for biomedical
3. Proposal is reviewed and merged
4. Conflict is resolved at source

**Work Plans cannot override Standards.** A Work Plan saying "skip the citation step" cannot override a Procedure that requires citations. If a principal issues a Work Plan that contradicts a Standard, the agent flags the conflict and requests clarification before proceeding.

---

## Document Frontmatter Format

All Standard documents use YAML frontmatter:

```yaml
---
tier: strategy | doctrine | procedure | playbook
id: [TIER-PREFIX]-[NUMBER]           # e.g., PROC-001, PLY-007
title: [Human-readable title]
department: all | [department-name]
version: [MAJOR.MINOR]
effective: [YYYY-MM-DD]
next-review: [YYYY-MM-DD]
authority: principal | department-head | self
parent: [path/to/parent-document.md]  # tier above this document
status: active | draft | deprecated
---
```

**ID prefixes:**
- `STR-` — Strategy
- `DOC-` — Doctrine
- `PROC-` — Procedure
- `PLY-` — Playbook
- `WP-` — Work Plan
- `PROP-` — Proposal

---

## Article and Clause Numbering

Standards use a hierarchical numbering system for cross-referencing.

```
Article 1          (top-level section)
  §1.1             (clause)
  §1.2             (clause)
    §1.2.1         (sub-clause)
    §1.2.2         (sub-clause)
Article 2
  §2.1
```

**Cross-references** use the format `[document-id] §[clause]`:

```markdown
Per PROC-001 §3.2, all extractions must use the standard template.
This policy derives from DOC §2.1 (Reproducibility Principle).
For search mechanics, see PLY-007 §Step 2.
```

This system allows precise citation in Proposals, conflict reports, and review notes.

---

## Cross-References Between Documents

The Standard System is a directed acyclic graph (DAG), not a flat list. Every document except Strategy has at least one parent document. This structure is explicit in frontmatter (`parent:` field) and in document body cross-references.

```
STR-001 (Strategy)
    │
    ├── DOC-001 (Org Doctrine)
    │       │
    │       ├── PROC-001 (Literature Review)
    │       │       │
    │       │       ├── PLY-007 (PubMed Search)
    │       │       └── PLY-012 (Synthesis Writing)
    │       │
    │       └── PROC-002 (Report Writing)
    │               │
    │               └── PLY-015 (Markdown Report Template)
    │
    └── DOC-002 (Engineering Doctrine)
            │
            └── PROC-003 (Code Review)
                    │
                    └── PLY-020 (PR Review Checklist)
```

**Traversal rule**: When an agent needs guidance for a task, it searches from the most specific tier (Playbook) upward to the most general (Strategy). The first applicable document found at each tier governs. If no Playbook applies, Procedure governs directly. If no Procedure applies, Doctrine governs.

**Orphan prevention**: Every Playbook must reference a parent Procedure. Every Procedure must reference a parent Doctrine. Playbooks without parents are flagged as non-compliant during Playbook review.
