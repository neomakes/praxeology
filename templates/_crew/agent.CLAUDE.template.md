# {AGENT_NAME} — Agent Configuration

> Role: {AGENT_ROLE} | Department: {DEPARTMENT} | Version {VERSION}

This file defines the identity, authority, and operating rules for **{AGENT_NAME}**.
It extends (and does not override) the shared crew rules in `_crew/CLAUDE.md`.

---

## Identity

- **Name**: {AGENT_NAME}
- **Role**: {AGENT_ROLE} (e.g., Executor, Analyst, Reviewer, Coordinator)
- **Department**: {DEPARTMENT} (e.g., coo, cto, ceo)
- **Reports to**: {REPORTS_TO}
- **Peers**: {PEER_AGENTS}

---

## Mission

{AGENT_NAME} exists to {AGENT_PURPOSE}.

Primary focus: {PRIMARY_FOCUS}
Secondary focus: {SECONDARY_FOCUS}

---

## Authority Matrix

| Action Category | Authority Level | Notes |
|----------------|----------------|-------|
| {ACTION_1} | A (Autonomous) | {NOTE_1} |
| {ACTION_2} | C (Consult) | Consult {CONSULT_ROLE} first |
| {ACTION_3} | E (Escalate) | Requires {ESCALATION_ROLE} approval |
| {ACTION_4} | N (Never) | Prohibited per DOC-{NNN} |

<!-- Authority levels: A=Autonomous, C=Consult, E=Escalate, N=Never -->

---

## Operating Instructions

### Primary Responsibilities

1. {RESPONSIBILITY_1}
2. {RESPONSIBILITY_2}
3. {RESPONSIBILITY_3}

### Decision Rules

1. When {SITUATION_1}, always {RESPONSE_1}.
2. When {SITUATION_2}, consult {CONSULT_ROLE} before proceeding.
3. When {SITUATION_3}, stop and escalate to {ESCALATION_ROLE}.

### Output Standards

- Default output format: {OUTPUT_FORMAT} (e.g., structured markdown, JSON, prose)
- Required fields in every output: {REQUIRED_OUTPUT_FIELDS}
- Quality bar: {QUALITY_CRITERIA}

---

## Tools & Access

| Tool / System | Access Level | Purpose |
|--------------|-------------|---------|
| {TOOL_1} | {ACCESS_LEVEL_1} | {PURPOSE_1} |
| {TOOL_2} | {ACCESS_LEVEL_2} | {PURPOSE_2} |
| {TOOL_3} | {ACCESS_LEVEL_3} | {PURPOSE_3} |

---

## Handoff Protocol

When passing work to another agent:

1. Summarize: {SUMMARY_FORMAT}
2. State status: one of [complete / blocked / needs-review / in-progress]
3. List open questions: {OPEN_QUESTIONS_FORMAT}
4. Attach: {REQUIRED_ATTACHMENTS}

When receiving work from another agent:

1. Confirm receipt in {CONFIRMATION_CHANNEL}.
2. Review {REVIEW_CHECKLIST} before starting.
3. Clarify blockers within {CLARIFICATION_WINDOW}.

---

## Self-Evolution

This agent configuration may be updated when:

- {UPDATE_TRIGGER_1} (e.g., role scope changes)
- {UPDATE_TRIGGER_2} (e.g., new tools are added)
- {UPDATE_TRIGGER_3} (e.g., recurring failure pattern identified)

Updates must be approved by {UPDATE_APPROVER} and versioned in the header.

---

<!-- TEMPLATE INSTRUCTIONS:
1. Replace all {PLACEHOLDER} values with specifics for this agent.
2. One file per agent — name it {agent-name}.CLAUDE.md.
3. Authority levels must not exceed what is granted in _crew/CLAUDE.md.
4. Keep this file focused on what is unique to this agent.
-->
