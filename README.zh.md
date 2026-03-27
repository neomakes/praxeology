<p align="center">
  <img src="assets/banner.svg" alt="Praxeology — The governance layer that keeps your AI agent team aligned, evolving, and accountable." width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/version-0.1.0-green.svg" alt="v0.1.0">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg" alt="Active">
  <img src="https://img.shields.io/badge/built%20by-NeoMakes-black.svg" alt="NeoMakes">
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.zh.md"><strong>中文</strong></a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.es.md">Español</a>
</p>

<p align="center">
  <a href="docs/quickstart.md">Quick Start</a> (<a href="docs/quickstart.ko.md">한국어</a> · <a href="docs/quickstart.ja.md">日本語</a> · <a href="docs/quickstart.zh.md">中文</a> · <a href="docs/quickstart.fr.md">FR</a> · <a href="docs/quickstart.de.md">DE</a> · <a href="docs/quickstart.es.md">ES</a>) ·
  <a href="docs/role-design.md">Role Design</a> (<a href="docs/role-design.ko.md">한국어</a> · <a href="docs/role-design.ja.md">日本語</a> · <a href="docs/role-design.zh.md">中文</a> · <a href="docs/role-design.fr.md">FR</a> · <a href="docs/role-design.de.md">DE</a> · <a href="docs/role-design.es.md">ES</a>)
</p>

---

## 问题

**并行化已经解决了。** Claude Code、Codex、gstack、oh-my-claudecode——这些工具已经让单个 AI 智能体变得极具生产力。并行运行 5 个智能体是一个已解决的问题。

**协调却不是。** 当这 5 个智能体完成工作后，谁来解决冲突？谁来验证一致性？谁来阻止智能体 A 覆盖智能体 B 的决策？谁来防止跨会话的角色漂移？多智能体框架解决的是*开始*——Praxeology 解决的是之后的问题：**协调、状态追踪、冲突解决和演进对齐。**

**Praxeology 是缺失的治理层。** 它位于你的编码工具之上，而非取代它们——确保你的智能体作为一个有机整体运作，而不是一群独立聊天机器人的集合。

---

## 生产环境验证

这不是理论。[NeoMakes](https://neomakes.com) 每天都在运行它。

> **1 人 + 9 个 AI 智能体 · 38 条治理规则 · 7 个部门**
> 每日待办 → 每周回顾 → 每月修订
> 智能体检测差距、提出修复方案、自主演进各自的 SOP。

每个智能体都定义了 **Speech Rules**（句子限制、语调）、**Anti-Patterns**（禁止行为）和 **Emotional Triggers**（情境依赖的响应变化）——确保所有 9 个智能体行为一致且可区分。NeoMakes 只是一个实例，你的系统看起来会有所不同。

---

## 工作原理

4+1 层治理层级。简单。通用。

```
战略 (WHY) → 教义 (WHAT) → 程序 (HOW) → 手册 (PATTERNS) → 执行 (NOW)
```

上层始终覆盖下层。无一例外。智能体通过向上遍历层级来解决决策——在第一个覆盖该情况的层级停止。

---

## 有何不同

不是功能列表。是协调问题的解决者。

| 你的问题 | Praxeology 的答案 |
|---|---|
| 智能体在会话间偏离其角色 | **ConstitutionalGuard** — 4 层行为验证 |
| 没有办法安全地约束智能体行为 | **SafetyGate** — 上层锁定下层无法覆盖的关键规则 |
| 智能体无法改进自身流程 | **SOP Evolution** — Learn-Compress-Apply 循环。治理的梯度下降 |
| 一处变更破坏另一处 | **Review Cascade** — 双向传播（层级上下） |
| 智能体无法标记规则存在问题时 | **Proposal Flow** — 任何智能体向创始人发送的结构化修订请求 |
| 会话间没有机构记忆 | **Work Cycle** — 每日差距 → 每周提案 → 每月修订 → 每季度回顾 |

---

## 快速开始

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
bash setup.sh    # 交互式向导：组织名称、使命、部门、智能体
bash launch.sh   # 你的治理系统已上线
```

> **新手？** 从[快速开始指南](docs/quickstart.md)和[角色设计指南](docs/role-design.md)开始。

---

## 智能体设计系统

每个智能体都会获得一个 `CLAUDE.md`，不仅定义它*做什么*，还定义它*如何*行为：

```
Identity → Persona → Speech Rules → Anti-Patterns → Emotional Triggers → Values → Boundaries
```

这使智能体**可区分、一致且有边界**。QA 智能体听起来与执行者不同。规划者从不写代码。审查者从不审批自己的工作。完整模板和扩展策略（3 到 15+ 个智能体）请参见[角色设计指南](docs/role-design.md)。

---

## 示例

- [examples/solo-dev/](examples/solo-dev/) — 独立开发者 + 3 个智能体（最小配置）
- [examples/tech-startup/](examples/tech-startup/) — 早期阶段软件公司
- [examples/one-piece-crew/](examples/one-piece-crew/) — 具有完整角色系统的虚构团队

---

<details>
<summary><strong>理论 — 为何有效（同构性）</strong></summary>

相同的 4+1 层结构出现在有组织行动的每个领域：

| 层级 | 国家法律 | 军事 | 企业 | 个人 | AI 智能体 |
|------|-------------|----------|-----------|------------|----------|
| **1 战略** | 宪法 | 战役目标 | 使命与愿景 | 个人价值观 | System Prompt / Prime Directive |
| **2 教义** | 成文法 | 交战规则 | 企业政策 | 人生原则 | 行为指南 |
| **3 程序** | 法规 | 标准作战程序 | SOP / 协议 | 习惯与例程 | 任务指令 |
| **4 手册** | 判例法 / 先例 | 战术与演练 | 最佳实践 | 习得模式 | Few-shot 示例 |
| **执行** | 行政令 | 任务命令 | Sprint / 工作计划 | 每日待办 | 活跃上下文 |

治理不是特定领域的。这个模式是普遍的。适用于军事单位的框架同样适用于初创公司、研究实验室或 AI 智能体群。

</details>

---

## 目录结构

```
your-org/
├── CLAUDE.md                  # AI 智能体的根上下文（生成的）
├── launch.sh                  # 每日启动脚本（生成的）
├── _standard/                 # 治理文档
│   ├── README.md              # 所有治理产出物的主索引
│   ├── {department}/          # 每个部门一个文件夹
│   │   ├── STR-{NNN}.md      #   （例如：战略、运营、财务、工程）
│   │   ├── DOC-{NNN}.md
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # 智能体 / 团队成员定义
│   ├── CLAUDE.md              # 共享团队规则
│   └── {agent}/               # 每个智能体的子目录
│       ├── CLAUDE.md          # 智能体上下文和角色
│       └── sop.md             # 智能体 SOP
├── _project/                  # 活跃项目
├── _setting/                  # 运营设置
├── docs/                      # 框架文档
├── templates/                 # 可复用文档模板
└── examples/                  # 参考实现
```

---

## 集成指南

| 指南 | 说明 |
|-------|-------------|
| [Discord 集成](docs/discord-integration.md) | 频道结构、机器人提及、循环防止 |
| [Google Drive 集成](docs/drive-integration.md) | 符号链接设置、规范存储、工作区 |
| [Crew Manager 仪表板](docs/crew-manager.md) | 用于会话监控的 Web 仪表板 |
| [Claude Code 设置](docs/claude-code-setup.md) | CLAUDE.md 层级、MCP 服务器、每智能体会话 |
| [Work Cycle](docs/work-cycle.md) | Todo/weekly 架构、报告周期、Standard Gap 流程 |

## 文档

| 文档 | 说明 |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | 设计理念和核心机制 |
| [docs/getting-started.md](docs/getting-started.md) | 前提条件、安装、第一步 |
| [docs/standard-system.md](docs/standard-system.md) | 4+1 层文档系统深度解析 |
| [docs/crew-system.md](docs/crew-system.md) | 智能体管理、SOP 自我演进 |
| [docs/tutorial.md](docs/tutorial.md) | 构建治理智能体团队的完整教程 |

---

## 起源

由 **[NeoMakes](https://neomakes.com)** 构建——一家开发极端环境设备端 AI 的单人公司。该框架源于以军事指挥结构相同的严格性治理 AI 智能体群的实践。

名称来自 praxeology（行为学），即人类行为的研究。有目的的行动具有结构。该结构是普遍的。将其明确化，你就可以治理任何事物。

---

## 许可证

MIT 许可证 — 参见 [LICENSE](LICENSE)。

Copyright (c) 2026 NeoMakes
