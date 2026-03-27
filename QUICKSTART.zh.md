# Praxeology — 快速入门指南

3 步构建你自己的自演化 AI agent 治理系统。

---

## 第 1 步：定义你的使命（STR）

在 `_standard/{department}/STR-101.md` 中写下你的组织的"为何存在"。

模板位于 `templates/_standard/`。填写以下内容：

- **Mission（使命）** — 一句话说明你存在的目的
- **Values（价值观）** — 指导每项决策的 3-5 条原则
- **Non-negotiables（不可谈判项）** — agent 无论收到何种指令都绝不可逾越的硬性限制

这是你的 agent 的宪法。每条治理规则、每个 agent 行为以及每项修正案提案都必须与之保持一致。当规则冲突时，STR 胜出。

---

## 第 2 步：设计你的团队

决定你需要多少个 agent。最少 2 个，推荐 3-9 个。每个 agent 映射到一个领域（工程、财务、安全、运营等）。

为每个 agent 创建 `_crew/{name}/CLAUDE.md`，包含以下章节：

- **Identity（身份）** — 名称、角色头衔、部门
- **Persona & Character（人格与性格）** — 在压力下驱动行为的个性特征
- **Speech Rules（说话规则）** — 句数上限、语气、禁用词组、独特表达
- **Anti-Patterns（禁止行为）** — 此 agent 绝不可做的事情的明确清单
- **Emotional Triggers（情感触发器）** — 响应风格如何随情境变化（常规 vs. 危机 vs. 冲突）
- **Values（价值观）** — 当规则未能覆盖某情况时，此 agent 优先遵循的原则
- **Boundaries（边界）** — 哪些领域属于其他 agent（防止职责重叠冲突）

然后创建 `_crew/CLAUDE.md`，写入对所有 agent 同等适用的规则：共享通信标准、上报协议、跨 agent 提及规则和报告节奏。

详细指导和实例参见 `ROLE-DESIGN.md`。

---

## 第 3 步：初始化治理

运行交互式向导：

```bash
bash setup.sh
```

或手动创建四份核心文件：

| 文档 | 路径 | 用途 |
|------|------|------|
| DOC-101 | `_standard/{department}/DOC-101.md` | 治理守卫 — agent 可以和不可以覆盖的内容 |
| DOC-102 | `_standard/{department}/DOC-102.md` | 安全 — 破坏性或不可逆操作的审批要求 |
| PRC-201 | `_standard/{department}/PRC-201.md` | Session 管理 — session 如何开始、运行和结束 |
| PLY-203 | `_standard/{department}/PLY-203.md` | 自演化 — agent 如何检测 gap 并提出改进建议 |

全部四份文件的模板位于 `templates/_standard/`。

---

## 接下来会发生什么

部署后，你的 agent 将：

1. **遵循治理层级**做出每个决策：先查 PLY（playbook），再查 PRC（procedure），再查 DOC（doctrine），最后查 STR（strategy）。如果当前层级能解决问题，就停止并行动；否则升级到下一层级。
2. **记录 Standard Gap** — 当某个情况未被现有规则覆盖时，而不是悄悄地即兴发挥。
3. **通过 Proposal 机制提出修正案** — 当某个 gap 反复出现时，让治理随实际使用而演化。
4. **通过 Learn-Compress-Apply 循环演化自己的 SOP** — 该循环在 PLY-203 中定义。

该系统的设计使治理随使用而不断收紧，而不是依赖手动审计。

---

## 扩展参考

| 配置 | 参考 |
|------|------|
| 1 人 + 初创团队 | `examples/tech-startup/` |
| 9 agent 完整团队 | `examples/one-piece-crew/` |

两个示例均包含预填充的 STR、团队 CLAUDE.md 文件以及可直接改编的已初始化治理文档。
