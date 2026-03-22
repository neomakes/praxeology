# CTO — Technology & R&D

> C-Level: Chief Technology Officer | G-Staff: —

This file contains all four governance tiers for the CTO domain (4xx series).
Fill in each section to define your organization's technology governance system.

---

## Strategy (Tier 1 — WHY)

### STR-4xx: {Your Technology Philosophy}

<!-- Template: Define why technology exists as a function in your organization.
     Ask: "What role does technology play in achieving our mission?" -->

```yaml
---
id: STR-4xx
tier: strategy
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
department: cto
---
```

#### Article 1 — Technology Purpose

1. Technology exists to {TECHNOLOGY_PURPOSE} (e.g., amplify human capability, automate repetitive work).
2. We choose technology based on {TECHNOLOGY_SELECTION_CRITERIA} (e.g., fit for purpose, maintainability, cost).
3. Our technology stack philosophy is {STACK_PHILOSOPHY} (e.g., boring tech wins, best-of-breed, platform-first).

#### Article 2 — Innovation Stance

1. We invest {INNOVATION_PERCENTAGE}% of capacity in exploratory R&D.
2. We adopt new technology when {ADOPTION_CRITERIA}.
3. We sunset legacy systems when {SUNSET_CRITERIA}.

---

## Doctrine (Tier 2 — WHAT)

### DOC-4xx: {Your Technology Rules}

<!-- Template: Define non-negotiable rules for how technology is built and used.
     Ask: "What technical commitments and prohibitions can never be compromised?" -->

```yaml
---
id: DOC-4xx
tier: doctrine
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
department: cto
---
```

#### Article 1 — Commitments (We Always)

1. We always {COMMITMENT_1} (e.g., review code before merging to production).
2. We always {COMMITMENT_2} (e.g., document APIs and interfaces).
3. We always {COMMITMENT_3} (e.g., maintain a tested rollback path for deployments).
4. We always {COMMITMENT_4} (e.g., encrypt sensitive data at rest and in transit).

#### Article 2 — Prohibitions (We Never)

1. We never {PROHIBITION_1} (e.g., deploy to production without passing tests).
2. We never {PROHIBITION_2} (e.g., store credentials in version control).
3. We never {PROHIBITION_3} (e.g., introduce a dependency without evaluating its maintenance status).

#### Article 3 — Technical Standards

1. All code must meet {CODE_STANDARD} before merging.
2. System uptime target: {UPTIME_TARGET} with incident response within {INCIDENT_RESPONSE_TIME}.
3. Technical debt is reviewed {DEBT_REVIEW_FREQUENCY} and addressed on a defined schedule.

---

## Procedure (Tier 3 — HOW)

### PRC-4xx: {Your Technology Development Process}

<!-- Template: Define the concrete process for building and maintaining technology.
     Ask: "How exactly do we plan, build, review, and ship technology?" -->

```yaml
---
id: PRC-4xx
tier: procedure
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
review_cycle: {quarterly|monthly}
department: cto
---
```

#### Article 1 — Development Cycle

1. Work is planned in {SPRINT_LENGTH} cycles using {PLANNING_METHOD}.
2. Each cycle begins with {CYCLE_START_RITUAL} and ends with {CYCLE_END_RITUAL}.
3. Definition of ready: {DEFINITION_OF_READY}.
4. Definition of done: {DEFINITION_OF_DONE}.

#### Article 2 — Code Review Process

1. All changes require review by {REVIEWER_COUNT} reviewer(s) before merge.
2. Review criteria: {REVIEW_CRITERIA} (e.g., correctness, style, test coverage, security).
3. Review must be completed within {REVIEW_SLA}.

#### Article 3 — Deployment Process

1. Deployments follow the sequence: {DEPLOYMENT_STEPS}.
2. Production deployments are authorized by {DEPLOYMENT_AUTHORIZER}.
3. Post-deployment verification covers {VERIFICATION_CHECKLIST}.

---

## Playbook (Tier 4 — PATTERNS)

### PLY-4xx: {Your Standard Technology Patterns}

<!-- Template: Define repeatable technical workflows.
     Ask: "What technical situations recur and what is our standard response?" -->

```yaml
---
id: PLY-4xx
tier: playbook
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
department: cto
---
```

#### Pattern 1 — {PATTERN_NAME_1} (e.g., New Service Setup)

**Trigger**: {WHEN_THIS_PATTERN_APPLIES}

**Steps**:
1. {STEP_1}
2. {STEP_2}
3. {STEP_3}

**Output**: {EXPECTED_OUTPUT}

**Owner**: {RESPONSIBLE_ROLE}

---

#### Pattern 2 — {PATTERN_NAME_2} (e.g., Production Incident Response)

**Trigger**: {WHEN_THIS_PATTERN_APPLIES}

**Steps**:
1. {STEP_1}
2. {STEP_2}
3. {STEP_3}

**Output**: {EXPECTED_OUTPUT}

**Owner**: {RESPONSIBLE_ROLE}

---

#### Pattern 3 — {PATTERN_NAME_3} (e.g., Dependency Upgrade)

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
2. Adapt development cycle length and method to your team's actual practice.
3. Add patterns for every recurring technical situation your team encounters.
4. Keep this file as cto/README.md in your _standard/ directory.
-->
