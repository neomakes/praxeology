# CISO — Intelligence & Security

> C-Level: Chief Intelligence & Security Officer | G-Staff: G-2 (Intelligence)

This file contains all four governance tiers for the CISO domain (7xx series).
Fill in each section to define your organization's intelligence and security governance.

---

## Strategy (Tier 1 — WHY)

### STR-7xx: {Your Security & Intelligence Philosophy}

<!-- Template: Define why security and intelligence governance exists in your organization.
     Ask: "What threats do we face, and why does protecting against them matter to our mission?" -->

```yaml
---
id: STR-7xx
tier: strategy
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
department: ciso
---
```

#### Article 1 — Security Purpose

1. Security exists to {SECURITY_PURPOSE} (e.g., protect the organization's ability to execute its mission).
2. Our primary threat model covers {PRIMARY_THREAT_CATEGORIES} (e.g., data breach, operational disruption, reputational attack).
3. We balance security with usability by {BALANCE_PRINCIPLE} (e.g., securing critical assets tightly, enabling flexibility elsewhere).

#### Article 2 — Intelligence Stance

1. We gather intelligence on {INTELLIGENCE_TARGETS} (e.g., competitive landscape, threat actors, environmental risks).
2. Intelligence informs {INTELLIGENCE_USE_CASES} (e.g., strategic decisions, threat response, opportunity identification).
3. We treat intelligence as {INTELLIGENCE_CLASSIFICATION_POLICY}.

---

## Doctrine (Tier 2 — WHAT)

### DOC-7xx: {Your Security Rules}

<!-- Template: Define non-negotiable rules governing security and information handling.
     Ask: "What security commitments and prohibitions can never be compromised?" -->

```yaml
---
id: DOC-7xx
tier: doctrine
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
department: ciso
---
```

#### Article 1 — Commitments (We Always)

1. We always {COMMITMENT_1} (e.g., apply least-privilege access to all systems).
2. We always {COMMITMENT_2} (e.g., report security incidents within {INCIDENT_REPORT_WINDOW}).
3. We always {COMMITMENT_3} (e.g., review access permissions when roles change).
4. We always {COMMITMENT_4} (e.g., maintain an up-to-date inventory of critical assets).

#### Article 2 — Prohibitions (We Never)

1. We never {PROHIBITION_1} (e.g., grant standing admin access where temporary access suffices).
2. We never {PROHIBITION_2} (e.g., store unencrypted sensitive data outside approved systems).
3. We never {PROHIBITION_3} (e.g., share credentials between individuals or systems).

#### Article 3 — Classification System

| Level | Label | Definition | Handling |
|-------|-------|------------|----------|
| 1 | {LEVEL_1_LABEL} | {LEVEL_1_DEFINITION} | {LEVEL_1_HANDLING} |
| 2 | {LEVEL_2_LABEL} | {LEVEL_2_DEFINITION} | {LEVEL_2_HANDLING} |
| 3 | {LEVEL_3_LABEL} | {LEVEL_3_DEFINITION} | {LEVEL_3_HANDLING} |

---

## Procedure (Tier 3 — HOW)

### PRC-7xx: {Your Security Operations Process}

<!-- Template: Define the concrete process for security monitoring, response, and review.
     Ask: "How exactly do we monitor threats, respond to incidents, and review our security posture?" -->

```yaml
---
id: PRC-7xx
tier: procedure
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
review_cycle: {quarterly|monthly}
department: ciso
---
```

#### Article 1 — Security Review Cycle

1. Security posture is reviewed {REVIEW_FREQUENCY} by {REVIEW_OWNER}.
2. Review covers: {REVIEW_SCOPE} (e.g., access audit, vulnerability scan, policy compliance check).
3. Findings are documented in {FINDINGS_LOCATION} and prioritized by {PRIORITIZATION_CRITERIA}.

#### Article 2 — Incident Response

1. Incidents are classified as {INCIDENT_SEVERITY_LEVELS}.
2. Response time targets:
   - Critical: {CRITICAL_RESPONSE_TIME}
   - High: {HIGH_RESPONSE_TIME}
   - Medium: {MEDIUM_RESPONSE_TIME}
3. Incident commander is {INCIDENT_COMMANDER_ROLE}.
4. Post-incident review completed within {POST_INCIDENT_REVIEW_WINDOW}.

#### Article 3 — Access Management

1. Access is provisioned using {ACCESS_PROVISIONING_PROCESS}.
2. Access is reviewed {ACCESS_REVIEW_FREQUENCY} for all systems.
3. Deprovisioning occurs within {DEPROVISIONING_TIMELINE} of role change or departure.

---

## Playbook (Tier 4 — PATTERNS)

### PLY-7xx: {Your Standard Security Patterns}

<!-- Template: Define repeatable security workflows.
     Ask: "What security situations recur and what is our standard response?" -->

```yaml
---
id: PLY-7xx
tier: playbook
title: {TITLE}
status: draft
version: 1
enacted_by: {NAME_OR_ROLE}
enacted_at: {YYYY-MM-DD}
department: ciso
---
```

#### Pattern 1 — {PATTERN_NAME_1} (e.g., New Access Request)

**Trigger**: {WHEN_THIS_PATTERN_APPLIES}

**Steps**:
1. {STEP_1}
2. {STEP_2}
3. {STEP_3}

**Output**: {EXPECTED_OUTPUT}

**Owner**: {RESPONSIBLE_ROLE}

---

#### Pattern 2 — {PATTERN_NAME_2} (e.g., Security Incident Response)

**Trigger**: {WHEN_THIS_PATTERN_APPLIES}

**Steps**:
1. Contain: {CONTAINMENT_STEP}
2. Assess: {ASSESSMENT_STEP}
3. Remediate: {REMEDIATION_STEP}
4. Report: {REPORTING_STEP}
5. Review: {REVIEW_STEP}

**Output**: {EXPECTED_OUTPUT}

**Owner**: {RESPONSIBLE_ROLE}

---

#### Pattern 3 — {PATTERN_NAME_3} (e.g., Threat Intelligence Digest)

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
2. Define your classification levels to match your actual data sensitivity needs.
3. Set incident response times based on realistic staffing capacity.
4. Keep this file as ciso/README.md in your _standard/ directory.
-->
