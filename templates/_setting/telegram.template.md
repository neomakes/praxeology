# {ORGANIZATION_NAME} — Telegram Channel Configuration

> Version {VERSION} | Owner: {OWNER_ROLE} | Last updated: {LAST_UPDATED_DATE}

This document defines how Telegram channels are used within **{ORGANIZATION_NAME}**,
including channel purpose, routing rules, and agent communication protocols.

---

## Channel Registry

| Channel Name | Chat ID | Purpose | Who Posts | Who Reads |
|-------------|---------|---------|-----------|-----------|
| {CHANNEL_1_NAME} | {CHAT_ID_1} | {PURPOSE_1} | {POSTER_1} | {READER_1} |
| {CHANNEL_2_NAME} | {CHAT_ID_2} | {PURPOSE_2} | {POSTER_2} | {READER_2} |
| {CHANNEL_3_NAME} | {CHAT_ID_3} | {PURPOSE_3} | {POSTER_3} | {READER_3} |
| {CHANNEL_4_NAME} | {CHAT_ID_4} | {PURPOSE_4} | {POSTER_4} | {READER_4} |

<!-- Common channel types to consider:
  - #alerts       — automated system alerts, agent errors
  - #updates      — task completions, status changes
  - #commands     — human-to-agent instructions
  - #logs         — verbose activity log (agents only write)
  - #escalations  — items requiring human attention
-->

---

## Routing Rules

These rules determine which channel receives which type of message.

| Message Type | Route To | Format |
|-------------|----------|--------|
| Task completed | {COMPLETION_CHANNEL} | {COMPLETION_FORMAT} |
| Error or failure | {ERROR_CHANNEL} | {ERROR_FORMAT} |
| Escalation required | {ESCALATION_CHANNEL} | {ESCALATION_FORMAT} |
| Status update | {STATUS_CHANNEL} | {STATUS_FORMAT} |
| Human command received | {COMMAND_CHANNEL} | {COMMAND_FORMAT} |
| {CUSTOM_TYPE} | {CUSTOM_CHANNEL} | {CUSTOM_FORMAT} |

---

## Message Format Standards

### Standard Agent Message

```
[{AGENT_NAME}] {MESSAGE_CATEGORY} — {SUMMARY}

Status: {STATUS}
Details: {DETAILS}
Action required: {ACTION_REQUIRED | None}
Ref: {REFERENCE_ID}
```

### Escalation Message

```
[ESCALATION] {URGENCY_LEVEL} — {TITLE}

Agent: {AGENT_NAME}
Issue: {ISSUE_DESCRIPTION}
Attempted: {WHAT_WAS_TRIED}
Blocked by: {BLOCKER}
Needs: {WHAT_IS_NEEDED}
Deadline: {DEADLINE | None}
```

### Error Alert

```
[ERROR] {ERROR_CODE} — {ERROR_TITLE}

Agent: {AGENT_NAME}
Time: {TIMESTAMP}
Context: {CONTEXT}
Error: {ERROR_MESSAGE}
Impact: {IMPACT_ASSESSMENT}
```

---

## Bot Configuration

| Setting | Value |
|---------|-------|
| Bot Name | {BOT_NAME} |
| Bot Token | Stored in {TOKEN_LOCATION} (never hardcode) |
| Webhook URL | {WEBHOOK_URL} |
| Allowed User IDs | {ALLOWED_USER_IDS} |
| Allowed Group IDs | {ALLOWED_GROUP_IDS} |
| Rate limit | {RATE_LIMIT} messages per {RATE_WINDOW} |

---

## Access Control

### Who May Send Messages

| Agent / Role | Channels Allowed | Message Types |
|-------------|-----------------|---------------|
| {AGENT_1} | {ALLOWED_CHANNELS_1} | {ALLOWED_TYPES_1} |
| {AGENT_2} | {ALLOWED_CHANNELS_2} | {ALLOWED_TYPES_2} |
| {HUMAN_ROLE_1} | All channels | All types |

### Command Authorization

Only the following user IDs may issue commands to agents via Telegram:

```
{AUTHORIZED_USER_ID_1}  # {NAME_1} — {ROLE_1}
{AUTHORIZED_USER_ID_2}  # {NAME_2} — {ROLE_2}
```

Any message from an unauthorized sender must be ignored and logged to {SECURITY_LOG_CHANNEL}.

---

## Notification Rules

| Event | Notify | Channel | Priority |
|-------|--------|---------|----------|
| System startup | {NOTIFY_ROLE_1} | {CHANNEL} | Low |
| Task failure | {NOTIFY_ROLE_2} | {CHANNEL} | High |
| Security alert | {NOTIFY_ROLE_3} | {CHANNEL} | Critical |
| Daily summary | {NOTIFY_ROLE_4} | {CHANNEL} | Low |
| {CUSTOM_EVENT} | {NOTIFY_ROLE} | {CHANNEL} | {PRIORITY} |

---

## Retention & Archival

- Messages in {HIGH_VOLUME_CHANNEL} are archived after {ARCHIVE_AFTER}.
- Escalation threads are retained for {ESCALATION_RETENTION_PERIOD}.
- Security-related messages are retained for {SECURITY_RETENTION_PERIOD}.
- Archive location: {ARCHIVE_LOCATION}.

---

<!-- TEMPLATE INSTRUCTIONS:
1. Replace all {PLACEHOLDER} values with your actual channel names, chat IDs, and roles.
2. Never hardcode bot tokens — always reference a secrets store.
3. Keep the authorized user ID list minimal and reviewed regularly.
4. Add or remove channel rows to match your actual Telegram setup.
5. Save as _setting/telegram.md in your governance folder.
-->
