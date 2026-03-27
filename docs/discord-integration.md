# Discord Integration

This guide explains how to connect Praxeology agent governance to a Discord server, based on the production NeoMakes crew setup.

---

## 1. Channel Structure

Four channels map to the four organizational functions. Each channel has a distinct scope — agents must stay in the appropriate channel for their work type.

| Channel | Purpose | Who Posts |
|---------|---------|-----------|
| `#lounge` | General coordination, casual crew interaction | All agents |
| `#bridge` | Strategy discussions, planning, captain directives | Captain + strategy-role agents |
| `#engine-room` | Technical execution, code, debugging, builds | Technical agents (CTO domain) |
| `#comms` | External-facing communication, partner/client context | CDO/CISO domain agents |

**Rule:** Agents post in the channel that matches the work type, not the agent's own identity. A technical agent working on a strategy task posts in `#bridge`.

---

## 2. Bot Mention Rules

All group channels operate with `requireMention: true`.

- An agent **only responds** when its own `<@botID>` appears in the message.
- Text-form names (e.g., `@Zoro`, `@zoro`) do **not** trigger a response — only the numeric bot ID format works.
- Messages without a mention are received and logged but produce no response.
- This applies to messages from humans and other bots equally.

```
# Correct — triggers the bot
<@1485963414860730378> please review the PR diff

# Incorrect — bot will not respond
@Zoro please review the PR diff
```

---

## 3. Loop Prevention

Bot-to-bot collaboration is bounded to prevent infinite response chains.

- **Max 3 round-trips** per collaboration thread between any two agents.
- A round-trip counts as: Agent A sends → Agent B responds → that is one trip.
- After 3 trips without resolution, the thread must **escalate to the captain** rather than continue.
- Agents do not self-initiate collaboration with other agents. Bot-to-bot work only happens when the captain has directed it.
- An agent never mentions itself.

**Escalation format when loop limit is reached:**

```
{AgentName} reporting. Mission blocked. Reason: [unable to resolve with {OtherAgent} in 3 trips]. Awaiting your orders, Captain.
```

---

## 4. Bot-to-Bot Communication

Agents can see all messages posted in a channel in real time. To direct a message at a specific agent, the `<@botID>` format is mandatory.

Rules:
1. Always use `<@botID>` when addressing another agent — text names are invisible to bots.
2. Only mention another agent when there is a concrete, specific request. No acknowledgments, no "sounds good", no check-ins.
3. Do not delegate tasks to other agents on your own initiative — only act on captain-directed collaboration.
4. Do not declare intent without delivering results. "I will investigate" is not a valid response. Investigate, then report findings in the same message.

**Response format for bot-to-bot:**

```
(result or answer here)
<@botID> — specific follow-up request if needed
```

---

## 5. Response Format

Group channel responses are kept short by default.

| Context | Max length |
|---------|-----------|
| Standard group response | 1–3 sentences |
| Response requiring detail | End with: "Details in DM." then send full content via DM |
| Daily report / structured output | No sentence limit — formatted list allowed |

**Prohibited response patterns:**

- Agreement/praise: "Good point.", "I agree.", "That's correct." — say nothing or add only new information.
- Announcements without results: "I'll look into this." — look into it first, then reply with the findings.
- Polite closings: "Please let me know if you need anything." — end after the content.

---

## 6. DM Rules

Direct messages between the captain and an agent, or between agents, operate with `requireMention: false`.

- No mention required — any message in a DM is addressed to that agent.
- No length limit — DMs are the appropriate place for detailed reports, long outputs, and back-and-forth clarification.
- The same loop prevention (3 round-trips) still applies to bot-to-bot DM threads.

---

## 7. Bot IDs Reference

Use these IDs in `<@botID>` format when mentioning agents.

| Agent | Role | Bot ID | Mention Format |
|-------|------|--------|----------------|
| Zoro | COO / Code Executor | 1485963414860730378 | `<@1485963414860730378>` |
| Usopp | CTO / QA Engineer | 1485969196646006784 | `<@1485969196646006784>` |
| Sanji | CTO / Environment & Security | 1485973114503430154 | `<@1485973114503430154>` |
| Robin | CISO / Security Analyst | 1485973449682849943 | `<@1485973449682849943>` |
| Nami | CFO / Budget Controller | 1485974089352089640 | `<@1485974089352089640>` |
| Jinbe | CDO / Data Engineer | 1485974653955477514 | `<@1485974653955477514>` |
| Franky | CTO / Infrastructure | 1485975240059125790 | `<@1485975240059125790>` |
| Chopper | CHRO / People Ops | 1485975628355469372 | `<@1485975628355469372>` |
| Brook | CDO / Documentation | 1485976189930573854 | `<@1485976189930573854>` |

---

## 8. Example: Captain-Directed Collaboration

**Scenario:** Captain asks Zoro to get a code review from Robin before merging.

```
# Captain in #engine-room
<@1485963414860730378> implement the auth middleware and get Robin's security sign-off before merging.

# Zoro in #engine-room (after implementing)
Auth middleware implemented. PR #47 ready.
<@1485973449682849943> security review requested on PR #47 — auth middleware, JWT validation, rate limiting.

# Robin in #engine-room
PR #47 reviewed. No injection vectors found. Rate limit header missing on /refresh endpoint — recommend adding before merge.

# Zoro in #engine-room
Fixed. /refresh now returns X-RateLimit headers. Merging.
```

Round-trip count: 1 (Zoro → Robin → Zoro). Within the 3-trip limit.

---

## 9. Governance Alignment

Discord behavior is governed by the same Standard documents that apply to all crew sessions:

- **DOC-201** — Operation principles: role focus, transparency, collaboration scope
- **DOC-102** — Safety operation: communication limits, approval chain
- **PLY-202** — Reporting and escalation: 3-item report format, 15-minute block threshold

The Discord channel is a communication surface, not a separate governance context. All Standard rules apply.
