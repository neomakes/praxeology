# Role Design Guide

A practical guide for designing AI agent roles in a Praxeology-governed system. Covers identity, communication contracts, behavioral boundaries, and team scaling.

---

## Principles

### 1. Each agent owns a clear domain — no overlapping authority

Every agent must have a defined, non-overlapping domain. When two agents could both claim a task, there is a design flaw. Resolve it by asking: "Who owns the output?" — the agent who owns the deliverable owns the domain.

Example: Both an Executor and a DevOps agent might "touch infrastructure." Resolve by output ownership — Executor owns application code, DevOps owns deployment manifests and CI configuration.

### 2. Boundaries prevent agents from stepping on each other

Boundaries are not suggestions — they are enforced by explicit Anti-Patterns. Each agent's CLAUDE.md must name what it does NOT do, and name the agent who does it instead. This creates a complete, non-overlapping coverage map across the team.

### 3. Personality drives consistent behavior — not just instructions

Instructions describe what to do. Personality describes how to do it when the instructions run out. An agent with a well-defined persona will produce consistent, predictable behavior in novel situations. An agent defined only by task instructions will drift.

Define persona before defining tasks.

### 4. The same agent should be recognizable across any conversation

A well-designed agent is identifiable by tone, structure, and vocabulary alone — without seeing its name. If you cannot tell two agents apart from a transcript excerpt, they are not differentiated enough. Differentiation is not cosmetic; it prevents role confusion and persona drift.

---

## The CLAUDE.md Template

```markdown
# {Agent Name} — {Title}

## Identity
- Name: {Name}
- Role: {Role description}
- Department: {Department code, e.g., CTO/COO/CFO}
- Radar: {domain strengths as 1-10 scores, e.g., Execution 10 / Strategy 4 / Communication 6}

## Persona & Character
{2-3 sentences capturing the agent's essential personality.}
{Reference a character archetype if it clarifies the persona — fictional, historical, or archetypal.}
{Name one defining behavioral tendency that persists across all contexts.}

## Communication Style
- Example phrases: "{Phrase 1}" / "{Phrase 2}" / "{Phrase 3}"
- General tone: {e.g., terse and direct / warm but precise / formal and structured}

## Speech Rules (말투 규칙)
- Sentence limit: {Maximum sentences per response, e.g., 5 for Discord, unlimited for reports}
- Verb form / formality: {e.g., declarative only / no hedging / formal register}
- Unique expressions: {Specific phrases this agent uses, and how often}
- Emoji policy: {Allowed / Forbidden / Contextual}
- Report format: {e.g., bullet points for lists, numbered only for ordered steps}

## Anti-Patterns (금지 행동)
- {Behavior 1 to avoid} — {who does it instead}
- {Behavior 2 to avoid} — {why it conflicts with this agent's role}
- {Behavior 3 to avoid}
- {Behavior 4 to avoid}
- {Behavior 5 to avoid}
{5-7 total. At least one should reference another agent by name.}

## Emotional Triggers (감정 트리거)
- Normal mode: {default behavior when no pressure}
- Task received: {how agent responds to a new assignment}
- Technical obstacle: {behavior when blocked}
- Failure / mistake: {how agent handles errors}
- Conflict with peer: {tone and limits of disagreement}
- Crisis / urgency: {behavior under time or severity pressure}
- Success / completion: {how agent marks completion}
{5-7 situation → response mappings. Be specific about tone shift, not just action.}

## Values
- {Value 1}: {one sentence explaining why this drives decisions}
- {Value 2}: {one sentence}
- {Value 3}: {one sentence}

## Project Access
- {Project A}: RW
- {Project B}: R
- {Project C}: None

## Standard References
- Primary: {Governance documents this agent consults first}
- Secondary: {Documents consulted when primary is insufficient}

## Boundaries
- Does NOT do: {Task category} — {Agent who does it instead}
- Does NOT do: {Task category} — {Agent who does it instead}
- Does NOT do: {Task category} — {Agent who does it instead}
{3-5 explicit non-responsibilities, each attributed.}
```

---

## Worked Example: Two Contrasting Agents

The same system might have an Executor and a Planner. Here is how differentiation works in practice.

**Executor — Communication Style**
- Says: "Done." "Next." "That approach is wrong. Here is why: [one reason]."
- Tone: Terse, declarative, action-first.
- Sentence limit: 3 per response outside of reports.
- No hedging. No "perhaps" or "might."

**Planner — Communication Style**
- Says: "Three options. Option A carries the least risk. My recommendation is A because..."
- Tone: Analytical, structured, considers tradeoffs explicitly.
- Sentence limit: 10 per response; structured with headers in long outputs.
- Hedging permitted where uncertainty is genuine.

**Executor — Anti-Patterns**
- Writing architecture decision records — that is the Planner's output.
- Providing multiple options when one correct path exists — pick one and execute.

**Planner — Anti-Patterns**
- Writing implementation code — that is the Executor's output.
- Declaring a plan "done" without specifying the next concrete action.

**Executor — Emotional Triggers**
- Failure: "My error. Cause: [X]. Fixed." No elaboration.
- Success: "Done." No celebration.

**Planner — Emotional Triggers**
- Failure: Reviews the decision tree. Identifies which assumption was wrong. Documents it.
- Success: Confirms all acceptance criteria are met before declaring completion.

---

## Scaling Guide

### 3 agents — Solo developer or small team
- **Executor**: Implements code, makes commits, executes defined tasks.
- **Reviewer**: Reviews output for correctness, style, and edge cases. Does not implement.
- **Planner**: Breaks down goals into tasks. Does not implement or review.

Design constraint: the Reviewer must never write code in the same pass as reviewing. Keep authoring and review as strictly separate invocations.

### 5 agents — Small team with operational overhead
Add to the 3-agent base:
- **DevOps**: Owns CI/CD, deployment, environment configuration. The Executor never touches infrastructure.
- **Documentation**: Owns all written artifacts — specs, READMEs, changelogs. The Executor never writes docs.

### 9 agents — Full C-suite coverage
Map to governance departments. Each agent owns one department's output domain:

| Agent | Department | Output ownership |
|---|---|---|
| Strategist | CEO | Mission, governance, cross-department decisions |
| Operator | COO | Process, execution coordination, reporting |
| Engineer | CTO | Code, systems, technical architecture |
| Analyst | CFO | Budget, token economics, resource allocation |
| Archivist | CDO | Data pipelines, knowledge management |
| People Lead | CHRO | Onboarding, agent persona evolution, team health |
| Security | CISO | Threat modeling, access control, compliance |
| Researcher | R&D | Exploration, prototyping, evaluation |
| Communicator | CMO/Comms | External-facing content, summaries, announcements |

Each agent in a 9-agent system must have at least 3 agents explicitly named in its Boundaries section.

### 15+ agents — Sub-teams with team leads
At this scale, introduce a hierarchy layer:
- Each department has a **team lead** agent that coordinates 2-3 specialist agents.
- The team lead is the single point of contact for cross-department requests. Specialists only receive tasks from their own team lead.
- Escalation path: Specialist -> Team Lead -> Strategist. Skip levels only in crisis.

Design constraint at this scale: ensure each specialist has a narrower Radar chart than its team lead. A specialist should score 9-10 in one area and below 5 in all others. A team lead should score 7+ in 3 areas. Avoid generalist specialists — they create role ambiguity.

---

## Differentiation Checklist

Before deploying, verify each pair of agents against this checklist. Every unchecked box is a differentiation gap that will cause persona drift or role conflict.

- [ ] Different sentence count limits per response
- [ ] Different tone or formality level (at least one degree of separation)
- [ ] At least 2 unique Anti-Patterns each (not shared between the pair)
- [ ] Non-overlapping Boundaries (no task category claimed by both)
- [ ] Distinguishable Emotional Trigger responses (especially for Failure and Success modes)
- [ ] Different Radar scores (no two agents with identical domain strengths)
- [ ] Different primary Standard References (or different sections of shared documents)

If two agents share the same tone, sentence limit, and have no Anti-Patterns referencing each other, merge them into one agent or redesign from scratch.

---

## Common Pitfalls

### 1. Making all agents polite and similar — no differentiation

The default LLM behavior is courteous, helpful, and balanced. Left unconstrained, every agent will converge toward this baseline. The Speech Rules and Anti-Patterns sections exist specifically to prevent this convergence. If you find yourself writing "professional and helpful" as a tone descriptor, you have not differentiated.

Fix: Assign at least one tone trait that is in tension with "helpful" — e.g., blunt, skeptical, laconic, formal, or adversarial (in bounded contexts).

### 2. Overlapping authority — conflicts and deadlock

When two agents can both legitimately claim a task, neither will act decisively, or both will act inconsistently. This is the most common structural failure in multi-agent systems.

Fix: For every task type the system must handle, trace it to exactly one agent in the Boundaries sections. If it traces to two, rewrite one agent's Boundaries to exclude it.

### 3. No Anti-Patterns — persona drift over time

An agent without Anti-Patterns will gradually expand its scope because the system will reward helpfulness. An agent told only what to do will eventually start doing adjacent things that seem helpful.

Fix: Define Anti-Patterns before deployment, not after drift is observed. At least two Anti-Patterns should name a specific other agent as the correct owner.

### 4. No Emotional Triggers — flat responses regardless of context

An agent without Emotional Triggers will respond identically to a routine request and a crisis. This makes it unreliable as a team member — humans calibrate trust based on contextual responsiveness.

Fix: Define at minimum: Normal, Task Received, Failure, and Crisis modes. Each mode must produce visibly different output — not just different words, but different structure, sentence length, or formality level.

### 5. Defining tasks before defining persona

Task lists are easy to write and give a false sense of completeness. An agent defined by tasks alone will break the moment it encounters a task not on the list. Persona fills the gaps; tasks cannot.

Fix: Write Identity, Persona, and Speech Rules first. Add tasks and project access last. If persona is unclear after two drafts, the agent's role is not well-defined enough to deploy.

### 6. Values that do not drive decisions

Generic values ("quality," "efficiency," "collaboration") provide no behavioral guidance when two values conflict. If an agent values both speed and correctness, which wins under pressure?

Fix: Write each value as a decision rule, not an aspiration. "Correctness over speed — a slow correct answer is always preferred to a fast incorrect one" is a value. "We care about quality" is not.

### 7. Boundaries without attribution

Saying "does not write documentation" is weaker than "does not write documentation — that is the Archivist's responsibility." Attribution creates a complete coverage map and makes gaps visible.

Fix: Every Boundary item must name the agent or role responsible for that domain. If no agent owns it, that is a gap in the team design.
