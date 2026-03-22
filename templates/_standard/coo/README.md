# COO — Operations & Execution

> C-Level: Chief Operating Officer | G-Staff: G-3 (Operations)

This file contains all four governance tiers for the COO domain (2xx series).
Fill in each section to define your organization's operational system.

---

## Strategy (Tier 1 — WHY)

### STR-2xx: {Your Operational Philosophy}

<!-- Template: Define why operations exist as a function in your organization.
     Ask: "What does excellent execution mean for us, and why does it matter?" -->

```yaml
---
id: STR-2xx
tier: strategy
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
department: coo
---
```

#### Article 1 — Operational Purpose

1. Operations exist to {OPERATIONAL_PURPOSE}.
2. We measure operational success by {OPERATIONAL_SUCCESS_METRIC}.
3. Our operational philosophy is {OPERATIONAL_PHILOSOPHY} (e.g., lean, systems-driven, people-first).

#### Article 2 — Execution Standards

1. We define "done" as {DEFINITION_OF_DONE}.
2. Quality is non-negotiable when {QUALITY_THRESHOLD_CONDITIONS}.
3. Speed is prioritized when {SPEED_PRIORITY_CONDITIONS}.

---

## Doctrine (Tier 2 — WHAT)

### DOC-2xx: {Your Operational Rules}

<!-- Template: Define the inviolable rules governing how work gets done.
     Ask: "What operational commitments can never be broken, regardless of pressure?" -->

```yaml
---
id: DOC-2xx
tier: doctrine
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
department: coo
---
```

#### Article 1 — Commitments (We Always)

1. We always {COMMITMENT_1} (e.g., document decisions before executing them).
2. We always {COMMITMENT_2} (e.g., communicate blockers within 24 hours).
3. We always {COMMITMENT_3} (e.g., conduct post-mortems after failures).

#### Article 2 — Prohibitions (We Never)

1. We never {PROHIBITION_1} (e.g., ship without a review step).
2. We never {PROHIBITION_2} (e.g., skip the handoff checklist).
3. We never {PROHIBITION_3} (e.g., close a task without verifying output).

#### Article 3 — Coordination Rules

1. Cross-department dependencies must be flagged {FLAGGING_TIMEFRAME} in advance.
2. Blocking issues escalate to {ESCALATION_ROLE} after {ESCALATION_TIMEOUT}.
3. All recurring processes must have a documented owner by {OWNER_DEADLINE}.

---

## Procedure (Tier 3 — HOW)

### PRC-2xx: {Your Operational Planning Process}

<!-- Template: Define the concrete rhythm and process for managing operations.
     Ask: "What is the exact cadence and method we use to plan and track work?" -->

```yaml
---
id: PRC-2xx
tier: procedure
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
review_cycle: {quarterly|monthly}
department: coo
---
```

#### Article 1 — Work Cycle Rhythm

1. **Daily**: {DAILY_STANDUP_FORMAT} at {TIME} covering {DAILY_TOPICS}.
2. **Weekly**: {WEEKLY_REVIEW_FORMAT} on {DAY} covering {WEEKLY_TOPICS}.
3. **Monthly**: {MONTHLY_REVIEW_FORMAT} on {DAY} covering {MONTHLY_TOPICS}.

#### Article 2 — Task Management

1. All tasks are tracked in {TASK_TRACKING_SYSTEM}.
2. Tasks must include: {REQUIRED_TASK_FIELDS} (e.g., owner, due date, status, priority).
3. Overdue tasks trigger {OVERDUE_PROTOCOL} after {OVERDUE_THRESHOLD}.

#### Article 3 — Capacity Management

1. Total operational capacity is calculated as {CAPACITY_CALCULATION_METHOD}.
2. No more than {MAX_WIP_PERCENTAGE}% of capacity is allocated to concurrent work.
3. {BUFFER_PERCENTAGE}% buffer is maintained for unplanned work.

---

## Playbook (Tier 4 — PATTERNS)

### PLY-2xx: {Your Standard Operational Patterns}

<!-- Template: Define the repeatable workflows your operations team uses.
     Ask: "What situations recur in operations, and what is our standard playbook?" -->

```yaml
---
id: PLY-2xx
tier: playbook
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
department: coo
---
```

#### Pattern 1 — {PATTERN_NAME_1} (e.g., New Project Kickoff)

**Trigger**: {WHEN_THIS_PATTERN_APPLIES}

**Steps**:
1. {STEP_1}
2. {STEP_2}
3. {STEP_3}

**Output**: {EXPECTED_OUTPUT}

**Owner**: {RESPONSIBLE_ROLE}

---

#### Pattern 2 — {PATTERN_NAME_2} (e.g., Operational Incident Response)

**Trigger**: {WHEN_THIS_PATTERN_APPLIES}

**Steps**:
1. {STEP_1}
2. {STEP_2}
3. {STEP_3}

**Output**: {EXPECTED_OUTPUT}

**Owner**: {RESPONSIBLE_ROLE}

---

#### Pattern 3 — {PATTERN_NAME_3} (e.g., Process Handoff)

**Trigger**: {WHEN_THIS_PATTERN_APPLIES}

**Steps**:
1. {STEP_1}
2. {STEP_2}
3. {STEP_3}

**Output**: {EXPECTED_OUTPUT}

**Owner**: {RESPONSIBLE_ROLE}

---

<!-- TEMPLATE INSTRUCTIONS:
1. Replace all {PLACEHOLDER} values with your organization's specifics.
2. Adjust the work cycle rhythm to match your actual cadence.
3. Add patterns for every recurring operational situation your team faces.
4. Keep this file as coo/README.md in your _standard/ directory.
-->
