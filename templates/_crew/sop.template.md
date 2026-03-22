# SOP-{NNN}: {SOP_TITLE}

> Department: {DEPARTMENT} | Owner: {OWNER_ROLE} | Version {VERSION}
> Status: draft | Last reviewed: {LAST_REVIEWED_DATE}

---

## Purpose

This SOP defines the standard procedure for **{PROCESS_NAME}**.

It applies when: {APPLICABILITY_CONDITION}
It does not apply when: {EXCLUSION_CONDITION}

---

## Trigger

This SOP is activated by:

- **Event**: {TRIGGER_EVENT} (e.g., new request received, threshold exceeded, scheduled cycle)
- **Signal**: {TRIGGER_SIGNAL} (e.g., message in {CHANNEL}, status change to {STATUS})
- **Frequency**: {EXECUTION_FREQUENCY} (e.g., on-demand, daily, weekly)

---

## Roles

| Role | Responsibility |
|------|---------------|
| **Owner** | {OWNER_ROLE} — accountable for SOP execution |
| **Executor** | {EXECUTOR_ROLE} — performs the steps |
| **Reviewer** | {REVIEWER_ROLE} — verifies output quality |
| **Approver** | {APPROVER_ROLE} — signs off on completion |

---

## Inputs

| Input | Source | Required? |
|-------|--------|-----------|
| {INPUT_1} | {SOURCE_1} | Yes / No |
| {INPUT_2} | {SOURCE_2} | Yes / No |
| {INPUT_3} | {SOURCE_3} | Yes / No |

---

## Procedure

### Step 1 — {STEP_1_NAME}

**Who**: {STEP_1_OWNER}
**When**: {STEP_1_TIMING}

1. {STEP_1_ACTION_1}
2. {STEP_1_ACTION_2}
3. {STEP_1_ACTION_3}

**Checkpoint**: {STEP_1_CHECKPOINT} (e.g., confirm X before proceeding)

---

### Step 2 — {STEP_2_NAME}

**Who**: {STEP_2_OWNER}
**When**: After Step 1 checkpoint is cleared

1. {STEP_2_ACTION_1}
2. {STEP_2_ACTION_2}
3. {STEP_2_ACTION_3}

**Checkpoint**: {STEP_2_CHECKPOINT}

---

### Step 3 — {STEP_3_NAME}

**Who**: {STEP_3_OWNER}
**When**: After Step 2 checkpoint is cleared

1. {STEP_3_ACTION_1}
2. {STEP_3_ACTION_2}
3. {STEP_3_ACTION_3}

**Checkpoint**: {STEP_3_CHECKPOINT}

---

<!-- Add more steps as needed. Each step should have a clear owner, timing, actions, and checkpoint. -->

---

## Outputs

| Output | Destination | Format |
|--------|-------------|--------|
| {OUTPUT_1} | {DESTINATION_1} | {FORMAT_1} |
| {OUTPUT_2} | {DESTINATION_2} | {FORMAT_2} |

---

## Exception Handling

| Situation | Response |
|-----------|----------|
| {EXCEPTION_1} | {EXCEPTION_RESPONSE_1} |
| {EXCEPTION_2} | {EXCEPTION_RESPONSE_2} |
| Input missing or invalid | Stop, notify {NOTIFY_ROLE}, do not proceed |
| Step fails after {MAX_RETRIES} retries | Escalate to {ESCALATION_ROLE} |

---

## Quality Criteria

This SOP is considered successfully executed when:

1. {QUALITY_CRITERION_1}
2. {QUALITY_CRITERION_2}
3. {QUALITY_CRITERION_3}

---

## Self-Evolution

This SOP should be reviewed and potentially updated when:

- {EVOLUTION_TRIGGER_1} (e.g., the process fails more than {FAILURE_THRESHOLD} times)
- {EVOLUTION_TRIGGER_2} (e.g., the trigger or inputs change)
- {EVOLUTION_TRIGGER_3} (e.g., a better method is discovered)

To propose a change:
1. Document the observed gap in {GAP_LOG_LOCATION}.
2. Draft the proposed change and submit to {REVIEW_ROLE}.
3. Upon approval, increment version and update `Last reviewed` date.
4. Notify {NOTIFICATION_LIST} of the change.

---

## Revision History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1 | {DATE} | {AUTHOR} | Initial draft |

---

<!-- TEMPLATE INSTRUCTIONS:
1. Replace all {PLACEHOLDER} values with specifics for this process.
2. Name this file {sop-name}.md or SOP-{NNN}.md.
3. Keep steps atomic — each step should be completable by one person in one session.
4. The self-evolution section is what makes this a living document — fill it in carefully.
-->
