<p align="center">
  <img src="assets/banner.svg" alt="praxeology — Human–AI Collaborative Governance for Purposeful Action" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/version-0.1.0-green.svg" alt="v0.1.0">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg" alt="Active">
  <img src="https://img.shields.io/badge/built%20by-NeoMakes-black.svg" alt="NeoMakes">
</p>

---

## 🌐 语言

[English](README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · **中文** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md)

也提供：[QUICKSTART](docs/quickstart.md) ([한국어](docs/quickstart.ko.md) · [日本語](docs/quickstart.ja.md) · [中文](docs/quickstart.zh.md)) · [ROLE-DESIGN](docs/role-design.md) ([한국어](docs/role-design.ko.md) · [日本語](docs/role-design.ja.md) · [中文](docs/role-design.zh.md))

---

## 为什么选择 Praxeology？

[gstack](https://github.com/gstack-io/gstack) 和 [oh-my-claudecode](https://github.com/anthropics/claude-code) 等工具非常擅长提升单个 AI agent 的生产力——浏览、编码、测试、部署。但当你从**一个 agent** 扩展到**多个 agent 协同工作**时，一个新问题出现了：**治理**。

没有治理，agent 会重复工作、相互矛盾、越权行事，并随着时间推移偏离各自的预定角色。单靠 prompt engineering 无法解决这个问题——你需要一种能够跨 session 持续存在、随使用而演化、并反映人类最有效组织数百年来治理行动方式的结构。

Praxeology 提供了这种结构。它不是你编码工具的替代品——它是凌驾于它们之上的**宪法层**，确保你的 agent 作为一个有凝聚力的组织运作，而不仅仅是一批独立的聊天机器人。

---

## 这是什么？

**Praxeology** 是一个基于通用 4+1 层治理层级的人机协作操作系统。人类制定战略和原则；agentic AI 在这些边界内执行，从经验中学习，并反向提出改进建议。它捕捉到这样一个洞察：所有有目的的行动——从国家到 agentic AI——都遵循相同的结构模式。

```
Strategy（为何） → Doctrine（做什么） → Procedure（如何做） → Playbook（模式） → Execution（现在）
```

高层级文件始终优先于低层级文件。没有例外。

---

## 同构性

相同的 4+1 层结构出现在有组织行动的每个领域：

| 层级 | 国家法律 | 军事 | 企业 | 个人 | AI Agent |
|------|---------|------|------|------|----------|
| **1 Strategy（战略）** | 宪法 | 战役目标 | 使命与愿景 | 个人价值观 | System Prompt / Prime Directive |
| **2 Doctrine（准则）** | 成文法 | 交战规则 | 公司政策 | 人生原则 | 行为指南 |
| **3 Procedure（程序）** | 法规 | 标准操作程序 | SOPs / 规程 | 习惯与常规 | 任务指令 |
| **4 Playbook（手册）** | 判例法 | 战术与演练 | 最佳实践 | 习得模式 | Few-shot 示例 |
| **执行工作计划** | 行政命令 | 任务命令 | Sprint / 工作计划 | 每日待办 | Active Context |

这种同构性是核心论点：治理不是领域特定的。这一模式是普遍的。适用于军事单位的框架同样适用于初创公司、研究实验室或 AI agent 集群。

---

## 快速开始

**第 1 步 — 克隆**

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
```

**第 2 步 — 运行安装**

```bash
bash setup.sh
```

交互式向导会询问你的组织名称、使命、部门、agent 和项目，并生成完整的目录结构及所有初始化文档。

**第 3 步 — 启动**

```bash
bash launch.sh
```

你的治理系统已上线。打开根目录的 `CLAUDE.md`，查看为 AI agent 生成的上下文。

> **初次接触 Praxeology？** 从 [docs/quickstart.md](docs/quickstart.md) 开始，获取 3 步指南；通过 [docs/role-design.md](docs/role-design.md) 设计你的 agent。

---

## 核心特性

| 特性 | 说明 |
|------|------|
| **SafetyGate** | 高层级文件可声明硬性限制，任何低层级文件均不可覆盖 |
| **Proposal Flow** | 任何 agent 或团队成员均可通过结构化 Proposal 格式提出修正案 |
| **SOP Evolution** | Procedure 和 Playbook 在提升前通过 Review Cascade 演化 |
| **Review Cascade** | 变更向上传播：Playbook → Procedure → Doctrine → Strategy 进行一致性检查 |
| **Reverse Flow** | Strategy 变更向下级联：所有低层级文档被标记以供审查 |
| **Department Codes** | 带有数字代码系列的部门（例如 NeoMakes 实例中的 1xx–7xx），含角色与人员分配 |

---

## 目录结构

```
your-org/
├── CLAUDE.md                  # AI agent 的根上下文（生成）
├── launch.sh                  # 每日启动脚本（生成）
├── _standard/                 # 治理文件
│   ├── README.md              # 所有治理文件的主索引
│   ├── {department}/          # 每个部门一个文件夹（例如 strategy, operations, finance, ...）
│   │   ├── STR-{NNN}.md      #   NeoMakes 实例使用：ceo, coo, cfo, cto, cdo, chro, ciso
│   │   ├── DOC-{NNN}.md      #   你的可以是任何名称
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # Agent / 团队成员定义
│   ├── CLAUDE.md              # 共享成员规则
│   └── {agent}/               # 每个 agent 的子目录
│       ├── CLAUDE.md          # Agent 上下文与人格
│       └── sop.md             # Agent SOPs
├── _project/                  # 活跃项目
│   ├── .praxe/                # 项目卡（治理元数据）
│   │   └── {project}.md       # 状态、优先级、成员分配、里程碑
│   └── {project}/             # 每个项目目录（代码）
├── _setting/                  # 运营设置
│   ├── permissions.md         # 访问控制矩阵
│   └── integrations.md        # 外部服务配置
├── docs/                      # 框架文档
├── templates/                 # 可复用文档模板
└── examples/                  # 参考实现
```

---

## 领域应用

### 企业

将部门映射到组织角色。每个部门拥有自己的治理栈。顶层 Strategy 文件是组织的宪法。（NeoMakes 实例使用 CEO/COO/CFO/CTO/CDO/CHRO/CISO 部门——你的可以是任何名称。）

### 研究实验室

将角色映射到 PI（首席研究员）、实验室主任、财务负责人、系统负责人、合作关系、人力资源和安全。使用相同的层级结构。Strategy 文件记录实验室的研究使命和伦理约束。完整的研究实验室演练参见 [docs/tutorial.md](docs/tutorial.md)。

### 个人生产力

单人实现。CEO = 你自己。Strategy = 你的人生使命。Doctrine = 你的不可谈判原则。Procedure = 你的每周仪式。Playbook = 你积累的最佳实践。Work Plan = 你的每日清单。

### AI Agent 团队

每个 AI agent 都有一个 `_crew/{agent}/CLAUDE.md`，定义其角色、权限级别和操作约束。根 `CLAUDE.md` 是团队的共同宪法。高层级文件在执行前被预置到 agent 上下文中。

---

## 框架文档

| 文档 | 说明 |
|------|------|
| [docs/architecture.md](docs/architecture.md) | 设计哲学、核心机制与通用治理模式 |
| [docs/getting-started.md](docs/getting-started.md) | 前提条件、安装与初始步骤 |
| [docs/standard-system.md](docs/standard-system.md) | 深入解析 4+1 层文档系统 |
| [docs/crew-system.md](docs/crew-system.md) | Agent 管理、SOP 自演化与 review cascade |
| [docs/tutorial.md](docs/tutorial.md) | 构建受治理 AI agent 团队的完整演练 |

---

## 示例

- [examples/solo-dev/](examples/solo-dev/) — 独立开发者 + 3 个 agent（最小化配置）
- [examples/tech-startup/](examples/tech-startup/) — 早期软件公司
- [examples/one-piece-crew/](examples/one-piece-crew/) — 带有完整人格系统的虚构团队（演示用）

---

## 生产环境使用 — NeoMakes（一个实例）

Praxeology 不是理论。它每天在运营一家真实的公司。NeoMakes 是该框架的一个实例——你的实例会有所不同。

**[NeoMakes, Inc.](https://neomakes.com)** 作为一家 1 人公司，由 9 个受 Praxeology 治理的 AI agent 运营：

| 指标 | 数值 |
|------|------|
| Agent 数量 | 9 个（分布在 7 个 C-level 部门） |
| 已颁布法规 | 38 条（覆盖所有部门的 STR/DOC/PRC/PLY） |
| 日常运营 | 待办跟踪、每日报告、每周规划、每月回顾 |
| 集成 | Claude Code + Discord（4 个频道）+ Google Drive + Notion + Calendar |
| 自演化 | Agent 每日检测 Standard Gap → 每周提出 Proposal → 每月提交修正案 |

这些 agent 拥有定义好的人格，包括**Speech Rules**（句数上限、语气）、**Anti-Patterns**（禁止行为）和**Emotional Triggers**（情境响应变化）——确保 9 个 agent 之间行为一致且可区分。

### 集成指南

| 指南 | 说明 |
|------|------|
| [Discord Integration](docs/discord-integration.md) | 频道结构、bot 提及、循环防止、bot 间通信 |
| [Google Drive Integration](docs/drive-integration.md) | 符号链接设置、法规存储、基于 room 的工作空间 |
| [Crew Manager Dashboard](docs/crew-manager.md) | 用于 session 监控、待办管理、权限审批的 Web 仪表盘 |
| [Claude Code Setup](docs/claude-code-setup.md) | CLAUDE.md 层级、MCP server、每个 agent 的 session 配置 |
| [Work Cycle](docs/work-cycle.md) | weekly.json/todo.json schema、报告周期、Standard Gap 反向流 |

---

## 起源

Praxeology 由 **[NeoMakes](https://neomakes.com)** 构建——一家专注于极端环境下人机交互基础技术研发的 1 人公司。该框架源于对以与人类组织同等严谨程度治理不断扩大的 AI agent 集群的需求。

这个名字来自于 praxeology（行动学）——研究人类行动的学科。洞察在于：有目的的行动具有结构。这种结构是普遍的。将其明确化，你就可以治理任何事物。

---

## 许可证

MIT License — 参见 [LICENSE](LICENSE)。

Copyright (c) 2026 NeoMakes
