# 角色设计指南

在 Praxeology 治理系统中设计 AI agent 角色的实践指南。涵盖身份、通信契约、行为边界与团队扩展。

---

## 原则

### 1. 每个 agent 拥有清晰的领域 — 权限不得重叠

每个 agent 必须有一个明确的、不重叠的领域。当两个 agent 都可以主张某项任务时，说明存在设计缺陷。通过问"谁拥有产出？"来解决——拥有交付物的 agent 拥有该领域。

示例：Executor 和 DevOps agent 都可能"接触基础设施"。通过产出归属来解决——Executor 拥有应用代码，DevOps 拥有部署清单和 CI 配置。

### 2. 边界防止 agent 相互干扰

边界不是建议——它们由明确的 Anti-Patterns 强制执行。每个 agent 的 CLAUDE.md 必须写明它**不**做什么，并指明由哪个 agent 来做。这在整个团队中创建了一张完整的、不重叠的职责覆盖图。

### 3. 人格驱动一致行为 — 而不仅仅是指令

指令描述做什么。人格描述当指令用尽时如何做。一个人格定义良好的 agent 在新情境中会产生一致、可预期的行为。仅由任务指令定义的 agent 会产生漂移。

先定义人格，再定义任务。

### 4. 同一个 agent 在任何对话中都应该可以被识别

一个设计良好的 agent，仅凭语气、结构和词汇就能被辨认——不需要看名字。如果你无法从对话摘录中区分两个 agent，说明它们的差异化程度不够。差异化不是装饰性的；它防止角色混乱和人格漂移。

---

## CLAUDE.md 模板

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

## 实例演练：两个形成对比的 Agent

同一个系统中可能同时有 Executor 和 Planner。以下展示差异化在实践中的效果。

**Executor — 通信风格**
- 说："Done." "Next." "That approach is wrong. Here is why: [one reason]."
- 语气：简洁、陈述式、行动优先。
- 句数上限：报告外每次响应不超过 3 句。
- 不使用模糊表达。不说"也许"或"可能"。

**Planner — 通信风格**
- 说："Three options. Option A carries the least risk. My recommendation is A because..."
- 语气：分析性、有条理、明确权衡利弊。
- 句数上限：每次响应最多 10 句；长篇输出使用标题结构。
- 在存在真正不确定性时允许使用模糊表达。

**Executor — Anti-Patterns**
- 撰写架构决策记录——那是 Planner 的产出。
- 在只有一条正确路径时提供多个选项——选一个并执行。

**Planner — Anti-Patterns**
- 编写实现代码——那是 Executor 的产出。
- 在未指明下一个具体行动的情况下宣称计划"已完成"。

**Executor — Emotional Triggers**
- 失败："My error. Cause: [X]. Fixed." 不作多余解释。
- 成功："Done." 不庆祝。

**Planner — Emotional Triggers**
- 失败：审查决策树，找出哪个假设出了问题，并记录下来。
- 成功：确认所有验收标准均已满足后再宣布完成。

---

## 扩展指南

### 3 个 agent — 独立开发者或小团队
- **Executor**：实现代码、提交 commit、执行已定义任务。
- **Reviewer**：审查产出的正确性、风格和边界情况。不参与实现。
- **Planner**：将目标分解为任务。不参与实现或审查。

设计约束：Reviewer 绝不能在审查的同一轮次中编写代码。创作和审查必须作为严格分离的调用。

### 5 个 agent — 带有运营开销的小团队
在 3 agent 基础上增加：
- **DevOps**：拥有 CI/CD、部署、环境配置。Executor 绝不接触基础设施。
- **Documentation**：拥有所有书面文件——规范、README、changelog。Executor 绝不撰写文档。

### 9 个 agent — 完整 C-suite 覆盖
映射到治理部门。每个 agent 拥有一个部门的产出领域：

| Agent | 部门 | 产出归属 |
|-------|------|---------|
| Strategist | CEO | 使命、治理、跨部门决策 |
| Operator | COO | 流程、执行协调、报告 |
| Engineer | CTO | 代码、系统、技术架构 |
| Analyst | CFO | 预算、token 经济学、资源分配 |
| Archivist | CDO | 数据管道、知识管理 |
| People Lead | CHRO | 入职、agent 人格演化、团队健康 |
| Security | CISO | 威胁建模、访问控制、合规 |
| Researcher | R&D | 探索、原型、评估 |
| Communicator | CMO/Comms | 对外内容、摘要、公告 |

9 agent 系统中的每个 agent，其 Boundaries 章节必须明确列出至少 3 个其他 agent 的名字。

### 15+ 个 agent — 有团队负责人的子团队
在这个规模下，引入一个层级层：
- 每个部门有一个**团队负责人** agent，协调 2-3 个专业 agent。
- 团队负责人是跨部门请求的唯一联络点。专业 agent 只接受来自本团队负责人的任务。
- 上报路径：专业 agent -> 团队负责人 -> Strategist。只在危机时跳级。

该规模下的设计约束：确保每个专业 agent 的 Radar 图比其团队负责人更窄。专业 agent 应在某一领域得分 9-10，在其他所有领域低于 5。团队负责人应在 3 个领域得分 7+。避免通才型专业 agent——它们会造成角色模糊。

---

## 差异化检查清单

部署前，对每对 agent 逐一核对此清单。每个未勾选的项目都是一个差异化缺口，将导致人格漂移或角色冲突。

- [ ] 每次响应的句数上限不同
- [ ] 语气或正式程度不同（至少一个等级的差距）
- [ ] 每个 agent 至少有 2 个独特的 Anti-Patterns（该对之间不共享）
- [ ] Boundaries 不重叠（没有任务类别被两者同时认领）
- [ ] Emotional Trigger 响应可区分（尤其是失败和成功模式）
- [ ] Radar 得分不同（没有两个 agent 的领域优势完全相同）
- [ ] 不同的主要 Standard References（或共享文档的不同章节）

如果两个 agent 语气相同、句数上限相同，且 Anti-Patterns 中没有互相引用，就将它们合并为一个 agent，或从头重新设计。

---

## 常见陷阱

### 1. 让所有 agent 都礼貌且相似 — 没有差异化

默认的 LLM 行为是礼貌、乐于助人且平衡的。不加约束，每个 agent 都会向这个基线收敛。Speech Rules 和 Anti-Patterns 章节的存在就是为了防止这种收敛。如果你发现自己把"专业且乐于助人"写成语气描述，说明你没有做到差异化。

修复：至少分配一个与"乐于助人"形成张力的语气特征——例如直白、怀疑、简洁、正式或（在有界情境下）对抗性的。

### 2. 权限重叠 — 冲突与僵局

当两个 agent 都可以合理主张某项任务时，两者都不会果断行动，或者两者都会行动但不一致。这是多 agent 系统中最常见的结构性失败。

修复：对于系统必须处理的每种任务类型，在 Boundaries 章节中将其追溯到恰好一个 agent。如果追溯到两个，就重写其中一个 agent 的 Boundaries 将其排除。

### 3. 没有 Anti-Patterns — 随时间产生人格漂移

没有 Anti-Patterns 的 agent 会逐渐扩大其范围，因为系统会奖励乐于助人的行为。只被告知该做什么的 agent，最终会开始做一些看似有帮助的周边事情。

修复：在部署前定义 Anti-Patterns，而不是在观察到漂移后。至少两个 Anti-Patterns 应该指明另一个具体的 agent 作为正确负责人。

### 4. 没有 Emotional Triggers — 无论情境如何响应都一样

没有 Emotional Triggers 的 agent 对常规请求和危机的响应会完全相同。这使其作为团队成员不可靠——人类根据情境响应能力来校准信任。

修复：至少定义：Normal（正常）、Task Received（接到任务）、Failure（失败）和 Crisis（危机）模式。每种模式必须产生明显不同的输出——不仅是不同的词语，还要有不同的结构、句子长度或正式程度。

### 5. 先定义任务再定义人格

任务列表很容易写，会给人一种完整感的错觉。仅由任务定义的 agent，一旦遇到列表上没有的任务就会崩溃。人格填补空白；任务做不到这一点。

修复：先写 Identity、Persona 和 Speech Rules。最后添加任务和项目访问权限。如果两稿之后人格仍不清晰，说明该 agent 的角色定义还不够充分，无法部署。

### 6. 价值观不能驱动决策

通用的价值观（"质量"、"效率"、"协作"）在两个价值观冲突时无法提供行为指导。如果一个 agent 同时重视速度和正确性，在压力下哪个优先？

修复：将每个价值观写成决策规则，而不是愿景。"正确性优先于速度——一个慢但正确的答案永远优于一个快但错误的答案"是价值观。"我们重视质量"不是。

### 7. 边界没有归属

说"不撰写文档"比"不撰写文档——那是 Archivist 的职责"要弱。归属创建了一张完整的职责覆盖图，让空白变得可见。

修复：每个 Boundary 条目必须指明负责该领域的 agent 或角色。如果没有 agent 负责，那就是团队设计中的一个空白。
