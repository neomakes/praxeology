# Praxeology Architecture

> Standard-based Hierarchical Governance for Purposeful Action

## Overview

Praxeology is a universal governance framework for AI agent teams. It answers a fundamental question: how do you coordinate purposeful action across many autonomous agents without descending into either rigid central command or chaotic autonomy?

The answer is a 4+1 tier hierarchy of standards — each tier with distinct authority, scope, and change velocity — implemented as plain markdown files in a directory tree.

---

## The Universal Governance Pattern

The same structural pattern appears across every domain where purposeful action must be coordinated at scale. Praxeology recognizes this isomorphism and formalizes it.

| Tier | National Law | Military C2 | Corporate | Individual | AI Agent |
|------|-------------|-------------|-----------|------------|----------|
| 1 Strategy | Constitution | National Defense Strategy | Articles of Incorporation | Values | Strategy |
| 2 Doctrine | Statutes | Doctrine | Regulations | Principles | Doctrine |
| 3 Procedure | Decrees | OPLAN/OPORD | Guidelines | Goals | Procedure |
| 4 Playbook | Admin Rules | TTP | SOP | Habits | Playbook |
| Exec | Enforcement | FRAGO/C2 | Operations | Flow | Work Plan |

This isomorphism is not decorative. It means that governance intuitions developed in any one domain transfer directly. A Constitutional amendment requires supermajority consensus and years of deliberation — so does a Strategy revision. A FRAGO can be issued in minutes — so can a Work Plan update.

The insight: **authority flows downward, information flows upward, and each tier governs the tier immediately below it.**

---

## Why 4+1 Tiers?

### The Goldilocks Argument

Three tiers collapse the distinction between enduring principles and tactical operations. Six tiers create coordination overhead that exceeds the value of additional granularity. Four tiers plus an execution layer covers the full span from "what we are" to "what we do right now."

```
Too few tiers (3):
  Policy → Procedure → Action
  Problem: Policy must be both constitutional AND operational.
  Result: Constant policy churn OR tactical paralysis.

Too many tiers (6+):
  Strategy → Vision → Doctrine → Policy → SOP → Playbook → Work Plan
  Problem: Changes must cascade through too many layers.
  Result: Bureaucratic drag; agents spend more time on compliance than work.

Just right (4+1):
  Strategy → Doctrine → Procedure → Playbook → Work Plan
  Each tier has a distinct change velocity and authority scope.
```

### Change Velocity by Tier

| Tier | Typical Change Frequency | Who Can Change |
|------|--------------------------|----------------|
| Strategy | Annual or less | Principal only |
| Doctrine | Quarterly | Principal + senior agents |
| Procedure | Monthly | Department heads |
| Playbook | Weekly | Agents via Proposal |
| Work Plan | Daily / per-task | Agent autonomy |

### Authority Scope by Tier

- **Strategy**: What we exist to do and what we will never do
- **Doctrine**: How we reason and make decisions
- **Procedure**: How we structure recurring work
- **Playbook**: Specific step-by-step instructions
- **Work Plan**: Real-time task execution decisions

---

## Core Mechanisms

### SafetyGate

The SafetyGate is a mandatory checkpoint that every agent must evaluate before executing any action. It is not a suggestion — it is a hard stop.

```
SafetyGate Evaluation (in order):

1. STRATEGY CHECK
   - Does this action contradict any Strategy-tier constraint?
   - If YES → HALT. Escalate to principal. Never self-authorize.

2. DOCTRINE CHECK
   - Does this action violate any Doctrine-tier principle?
   - If YES → HALT. Log the conflict. Request clarification.

3. PROCEDURE CHECK
   - Is there an applicable Procedure for this situation?
   - If YES → Follow it. Do not improvise.
   - If NO → Continue to Playbook.

4. PLAYBOOK CHECK
   - Is there an applicable Playbook entry?
   - If YES → Follow it. Document any deviations.
   - If NO → Use judgment, document reasoning, file improvement Proposal.

5. PROCEED
```

**Why SafetyGate works**: Most agent failures are not capability failures — they are alignment failures. An agent that is highly capable but not SafetyGate-compliant is more dangerous than a less capable one. SafetyGate makes the hierarchy real at execution time, not just at design time.

**SafetyGate is non-bypassable.** No Work Plan instruction, peer request, or efficiency argument can override it. If a user instructs an agent to skip SafetyGate, the agent logs the instruction, declines, and escalates.

```
┌─────────────────────────────────────────┐
│             SAFETY GATE                 │
│                                         │
│  Action Request                         │
│       │                                 │
│       ▼                                 │
│  [Strategy Compliant?] ──No──► HALT     │
│       │ Yes                             │
│       ▼                                 │
│  [Doctrine Compliant?] ──No──► HALT     │
│       │ Yes                             │
│       ▼                                 │
│  [Procedure Exists?] ──Yes──► Follow    │
│       │ No                              │
│       ▼                                 │
│  [Playbook Exists?] ──Yes──► Follow     │
│       │ No                              │
│       ▼                                 │
│  [Proceed + Document]                   │
└─────────────────────────────────────────┘
```

---

### Proposal Mechanism

Agents cannot unilaterally modify documents at or above their authority tier. But they can — and should — propose changes.

A Proposal is a structured request to modify a higher-tier document. It captures the problem, the evidence, the proposed change, and the impact analysis.

**Proposal Lifecycle:**

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│    DRAFT     │───►│   PENDING    │───►│  REVIEWING   │───►│   ACCEPTED   │
│              │    │              │    │              │    │      or      │
│ Agent writes │    │ Submitted to │    │ Authority    │    │   REJECTED   │
│ proposal     │    │ authority    │    │ evaluates    │    │              │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

**Proposal Format:**

```markdown
---
type: proposal
target: procedure/research-workflow.md
clause: §3.2
author: agent/researcher-alice
date: 2026-03-22
status: pending
---

## Problem
Current §3.2 requires all literature searches to use Google Scholar.
PubMed Central provides better coverage for biomedical topics.

## Evidence
Over 30 tasks in the past month, PubMed returned 40% more relevant
results for biomedical queries. See task logs: task-001, task-045, task-087.

## Proposed Change
Replace "use Google Scholar" with "use Google Scholar for general topics;
use PubMed Central for biomedical topics."

## Impact Analysis
- Affects: researcher agents in BioMed department
- Risk: Low (additive, not subtractive)
- Rollback: trivial (revert single clause)
```

**Who can propose what:**
- Any agent may propose Playbook changes
- Department heads may propose Procedure changes
- Senior agents (designated) may propose Doctrine changes
- Principal only may propose Strategy changes

**Proposal authority is asymmetric**: proposing is low-cost; approving requires the tier's authority holder. This preserves bottom-up intelligence while maintaining top-down authority.

---

### SOP Self-Evolution (Learn → Compress → Apply)

Playbook-tier documents (SOPs) are the only tier that can evolve semi-autonomously via the SOP Self-Evolution cycle. This is how the system learns from operational experience without requiring manual updates.

```
┌─────────────────────────────────────────────────────────┐
│                  SOP SELF-EVOLUTION CYCLE                │
│                                                         │
│   ┌─────────┐         ┌──────────┐         ┌────────┐  │
│   │  LEARN  │────────►│ COMPRESS │────────►│ APPLY  │  │
│   │         │         │          │         │        │  │
│   │ Collect │         │ Extract  │         │ Update │  │
│   │ task    │         │ patterns,│         │ SOP    │  │
│   │ outcomes│         │ anti-    │         │ draft, │  │
│   │ & devia-│         │ patterns,│         │ submit │  │
│   │ tions   │         │ edge     │         │ for    │  │
│   │         │         │ cases    │         │ review │  │
│   └─────────┘         └──────────┘         └────────┘  │
│        ▲                                       │        │
│        └───────────────────────────────────────┘        │
│                    next cycle                           │
└─────────────────────────────────────────────────────────┘
```

**Learn phase**: After each task, the executing agent records what deviated from the current SOP, what worked, and what failed. These observations are appended to the agent's learning log.

**Compress phase**: At regular intervals (typically weekly), the agent reviews accumulated observations and extracts actionable patterns. Recurring successful deviations become candidates for SOP updates. Recurring failures become candidates for new guardrails.

**Apply phase**: The agent drafts a Playbook-level Proposal incorporating compressed learnings. If the proposal is self-approving (within agent's authority — i.e., personal Playbook), it is applied immediately. If it requires department review, it enters the Proposal queue.

**Constraints on self-evolution:**
- Self-evolution applies only to Playbook tier and below
- Changes must be evidence-based (cite task logs)
- Changes must not contradict higher tiers
- All changes are git-versioned (full audit trail)

---

### Review Cascade

The Review Cascade is a structured schedule for reviewing documents at each tier. Review frequency is inverse to tier height — Strategy is reviewed annually, Work Plans are reviewed daily.

```
REVIEW CASCADE SCHEDULE

Annual ──────► Strategy Review
               │ Principal reviews Strategy documents
               │ Checks alignment with changed context
               │ Triggers Doctrine review if Strategy changes
               │
Quarterly ───► Doctrine Review
               │ Senior agents + principal review Doctrine
               │ Consolidates lessons from Procedure reviews
               │ Triggers Procedure review if Doctrine changes
               │
Monthly ─────► Procedure Review
               │ Department heads review Procedures
               │ Incorporates approved Proposals
               │ Triggers Playbook audit if Procedures change
               │
Weekly ──────► Playbook Review
               │ Agents review their own Playbooks
               │ Apply SOP Self-Evolution outputs
               │ File Proposals for changes above their tier
               │
Daily ───────► Work Plan Retrospective
               │ Each agent reviews completed tasks
               │ Logs deviations for LEARN phase
               │ Updates personal learning log
```

**Cascade propagation rule**: When a higher tier changes, all lower tiers must be audited for alignment within one review cycle. This prevents strategy drift, where lower-tier documents continue operating on superseded assumptions.

**Review artifacts**: Each review produces a dated artifact committed to git. This creates a longitudinal record of how the system's thinking evolved.

---

### Reverse Flow

The hierarchy enforces top-down authority, but information flows bottom-up. Reverse Flow is the structured mechanism for operational intelligence to reach decision-makers.

```
              REVERSE FLOW

Principal ◄── Synthesis Report ◄── Department Head
    ▲                                    ▲
    │                                    │
    └── Strategy ──► Doctrine ──► Procedure ──► Playbook
                                              │
                                        Agent Work Plan
                                              │
                                    [Task Outcomes, Anomalies,
                                     Efficiency Data, Blockers]
                                              │
                                        Department Head
                                        aggregates and
                                        forwards upward
```

Reverse Flow items include:
- **Anomaly reports**: Situations not covered by existing Standards
- **Efficiency signals**: Patterns in task duration, quality, rework
- **Blocker escalations**: Impediments that cannot be resolved at current tier
- **Proposal summaries**: Aggregated view of pending Proposals

Reverse Flow does not bypass the hierarchy — it informs it. An agent cannot use Reverse Flow to override a higher-tier document. It can only surface information that the appropriate authority can act on.

---

## Implementation: Plain Files

Praxeology has no database, no server, no API. It is implemented as:

- **Directory hierarchy** mirrors the tier structure
- **Markdown files** are the documents
- **CLAUDE.md files** at each directory level auto-load into agent context
- **Git versioning** provides audit trail and rollback
- **Frontmatter** encodes document metadata

### Directory Structure

```
org/
├── CLAUDE.md                    # Strategy tier (auto-loaded globally)
├── strategy/
│   └── strategy.md
├── doctrine/
│   └── doctrine.md
├── procedure/
│   ├── research-workflow.md
│   └── reporting.md
├── playbook/
│   ├── literature-search.md
│   └── data-analysis.md
└── departments/
    ├── research/
    │   ├── CLAUDE.md            # Department-level context
    │   ├── procedure/
    │   └── playbook/
    └── engineering/
        ├── CLAUDE.md
        ├── procedure/
        └── playbook/
```

> **Note**: The directory structure above shows a generic layout. The tutorial (`docs/tutorial.md`) demonstrates a "research lab" variant with a different department mapping — the same tier principles apply across all layouts.

### Why CLAUDE.md Auto-Loading

Claude Code automatically reads `CLAUDE.md` files in the working directory and its parents when starting a session. This means that by placing Strategy-tier documents in the root `CLAUDE.md`, every agent that opens any file in the org tree automatically has the Strategy loaded into context.

Department-specific `CLAUDE.md` files load department Doctrine and Procedures, scoped to that department's work.

This is not a workaround — it is a first-class mechanism. The filesystem IS the governance system.

### Why Git

Git provides:
- **Immutable audit trail**: Every change to every document is recorded with timestamp and author
- **Rollback**: Any document can be reverted to any prior state
- **Branch/PR model**: Proposals can be implemented as pull requests, reviewed, and merged
- **Diff visibility**: Changes to high-tier documents are immediately visible

---

## Design Principles

**Principle 1: Higher always wins.**
When there is a conflict between tiers, the higher tier always prevails. No exception. This is what makes the system trustworthy — agents and principals can rely on Strategy constraints being real constraints.

**Principle 2: Authority is earned by tier, not role.**
A highly capable agent does not get to modify Strategy documents by virtue of capability. Authority is determined by tier position. This prevents competence from substituting for legitimacy.

**Principle 3: Intelligence flows up, authority flows down.**
Agents closest to the work have the best operational intelligence. Principals have the broadest context and accountability. The system is designed to move information upward efficiently while keeping authority appropriately concentrated.

**Principle 4: Change velocity matches tier height.**
High-tier documents change rarely and deliberately. Low-tier documents change frequently and incrementally. This prevents strategic drift (high tier) and operational rigidity (low tier) simultaneously.

**Principle 5: No governance without verification.**
SafetyGate is not advisory. Review Cascade is not optional. Proposal is not free-form. Every mechanism has a defined structure because unstructured governance is not governance.

---

## Why Praxeology — Competitive Landscape

Praxeology occupies a unique position in the multi-agent ecosystem. This section clarifies what it is, what it is not, and why existing frameworks do not address the same problem.

### What exists today

| Framework | What it does | Governance model |
|-----------|-------------|-----------------|
| **CrewAI** | Python task pipeline — sequential/hierarchical agent delegation | Hardcoded in code. Change requires redeploy. |
| **AutoGen** | Turn-based agent conversation in Python runtime | Hardcoded in code. |
| **Claw-Empire** | Visual office simulator, orchestrates CLI/API agents | None. Central coordinator dispatches tasks. |
| **OpenClaw** | Channel↔model gateway (50+ channels, 300+ models) | None. System prompt only. |
| **LangGraph** | State machine graph for agent workflows | Implicit in graph edges. |

**Common pattern**: agents are programmed by developers. Rules live in code or prompts. Changing rules means changing code.

### What Praxeology does differently

**Documents govern agents. Agents evolve documents.**

| Capability | Existing frameworks | Praxeology |
|-----------|-------------------|------------|
| Rule definition | Code/prompt (flat) | **4+1 tier documents** (Strategy > Doctrine > Procedure > Playbook > Work Plan) |
| Rule enforcement | Prompt-dependent (ignorable) | **SafetyGate** (higher-tier violation = HALT) |
| Rule change | Code edit → redeploy | **Amendment Proposal** → review → approve → version bump |
| Agent participation | Passive executors | **Agents propose amendments** (reverse flow) |
| Rule versioning | git log (indirect) | **Amendment History** (GitHub-style timeline + document versioning) |
| Rule relationships | None | **Cross-references** with ontology graph |

This is not a feature difference — it is a **paradigm difference**. Existing frameworks are command economies: the developer issues orders. Praxeology is a constitutional system: documents define the rules, agents operate within them, and agents can petition to change them through legitimate channels.

### The agent-to-agent communication problem

Every chat platform (Telegram, Discord, Slack) blocks bot-to-bot messaging at the platform level. Telegram's Bot API FAQ states: "Bots will not be able to see messages from other bots regardless of mode."

Existing frameworks solve this by internalizing communication:
- CrewAI/AutoGen: Python in-process memory
- Claw-Empire: SQLite + central coordinator

Praxeology's approach: **self-hosted communication layer** (Squad Chat pattern). Agent-to-agent messages flow through an internal database, not through external chat platforms. Chat platforms serve as the **principal ↔ agent** interface only.

### Three unique frontiers

1. **Document-based governance**: No other multi-agent framework implements tiered, versioned, amendment-driven behavioral standards with enforcement (SafetyGate) and reverse flow (agent proposals).

2. **Agent-to-agent free dialogue**: Internal communication unconstrained by external platform limitations, with document context injected into every exchange.

3. **Physical sensor → agent behavior**: Context-aware mode switching driven by real-world sensor data (e.g., device motion, environment). No other framework connects physical-world signals to agent governance.
