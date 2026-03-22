# {ORGANIZATION_NAME} — Permission Matrix

> Version {VERSION} | Last updated: {LAST_UPDATED_DATE} | Owner: {OWNER_ROLE}

This document defines what each agent and role is authorized to do across all systems and domains.
It is the authoritative source for access control decisions within **{ORGANIZATION_NAME}**.

---

## Permission Levels

| Symbol | Level | Meaning |
|--------|-------|---------|
| A | Autonomous | May act without prior approval |
| C | Consult | Must consult {CONSULT_ROLE} before acting |
| E | Escalate | Requires explicit approval from {ESCALATION_ROLE} |
| R | Read-only | May observe but not modify |
| N | None | No access; action is prohibited |

---

## Agent Permission Matrix

> Rows = Actions | Columns = Agents/Roles

| Action | {AGENT_1} | {AGENT_2} | {AGENT_3} | {HUMAN_ROLE_1} | Notes |
|--------|-----------|-----------|-----------|----------------|-------|
| Read governance docs | R | R | R | A | All agents can read |
| Create task | A | A | C | A | {AGENT_3} must consult {CONSULT_ROLE} |
| Close task | A | C | N | A | |
| Send external message | C | N | N | A | Must consult {COMMS_ROLE} |
| Modify codebase | A | N | N | A | {AGENT_1} only |
| Deploy to production | E | N | N | A | Requires {DEPLOY_APPROVER} |
| Access financial data | N | N | N | A | Humans only |
| Create governance doc | E | N | N | A | Requires {GOV_APPROVER} |
| Amend Doctrine (Tier 2) | N | N | N | E | Board-level only |
| {CUSTOM_ACTION_1} | {PERM} | {PERM} | {PERM} | {PERM} | {NOTE} |
| {CUSTOM_ACTION_2} | {PERM} | {PERM} | {PERM} | {PERM} | {NOTE} |

---

## System Access Matrix

> Rows = Systems | Columns = Agents/Roles

| System | {AGENT_1} | {AGENT_2} | {AGENT_3} | {HUMAN_ROLE_1} | Notes |
|--------|-----------|-----------|-----------|----------------|-------|
| {SYSTEM_1} | A | R | N | A | |
| {SYSTEM_2} | R | A | N | A | |
| {SYSTEM_3} | N | N | N | A | Humans only |
| {SYSTEM_4} | R | R | R | A | Read-only for agents |
| {CUSTOM_SYSTEM} | {PERM} | {PERM} | {PERM} | {PERM} | {NOTE} |

---

## Escalation Paths

| Situation | First Contact | If Unavailable |
|-----------|--------------|----------------|
| Action requires E-level approval | {PRIMARY_ESCALATION_ROLE} | {BACKUP_ESCALATION_ROLE} |
| Security incident | {SECURITY_CONTACT} | {SECURITY_BACKUP} |
| Governance conflict | {GOVERNANCE_CONTACT} | {GOVERNANCE_BACKUP} |
| System outage | {OPS_CONTACT} | {OPS_BACKUP} |
| {CUSTOM_SITUATION} | {CONTACT} | {BACKUP} |

---

## Temporary Permission Grants

Temporary elevated permissions may be granted when:

1. {GRANT_CONDITION_1} (e.g., emergency response requires it)
2. {GRANT_CONDITION_2} (e.g., a specific project requires time-limited access)

Process:
1. Request submitted to {GRANT_APPROVER} with justification.
2. Approval documented in {GRANT_LOG_LOCATION}.
3. Expiry date set — maximum duration: {MAX_GRANT_DURATION}.
4. Access revoked automatically or manually by {REVOCATION_OWNER} at expiry.

---

## Review Schedule

| Trigger | Action | Owner |
|---------|--------|-------|
| Every {REVIEW_FREQUENCY} | Full matrix audit | {AUDIT_OWNER} |
| Agent role changes | Update affected rows | {UPDATE_OWNER} |
| New system added | Add system row | {UPDATE_OWNER} |
| Security incident | Emergency review | {CISO_ROLE} |

---

<!-- TEMPLATE INSTRUCTIONS:
1. Replace all {PLACEHOLDER} values with your actual agents, roles, and systems.
2. Add a column for every agent and human role in your organization.
3. Add a row for every action and system that needs access control.
4. Be explicit about N (none) — do not leave cells blank.
5. Save as _setting/permissions.md in your governance folder.
-->
