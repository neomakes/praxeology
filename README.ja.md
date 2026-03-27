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

## 🌐 言語

[English](README.md) · [한국어](README.ko.md) · **日本語** · [中文](README.zh.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md)

他のドキュメント: [QUICKSTART](docs/quickstart.md) ([한국어](docs/quickstart.ko.md) · [日本語](docs/quickstart.ja.md) · [中文](docs/quickstart.zh.md) · [FR](docs/quickstart.fr.md) · [DE](docs/quickstart.de.md) · [ES](docs/quickstart.es.md)) · [ROLE-DESIGN](docs/role-design.md) ([한국어](docs/role-design.ko.md) · [日本語](docs/role-design.ja.md) · [中文](docs/role-design.zh.md) · [FR](docs/role-design.fr.md) · [DE](docs/role-design.de.md) · [ES](docs/role-design.es.md))

---

## なぜ Praxeology なのか？

[gstack](https://github.com/gstack-io/gstack) や [oh-my-claudecode](https://github.com/anthropics/claude-code) といったツールは、個々の AIエージェントの生産性向上——ブラウジング、コーディング、テスト、デプロイ——に優れている。しかし**1つのエージェント**から**多数のエージェントが協働する**規模になると、新たな問題が浮上する。それが**ガバナンス**だ。

ガバナンスがなければ、エージェントは作業を重複させ、互いに矛盾し、領域を越境し、時間とともに本来の役割から逸脱していく。プロンプトエンジニアリングだけではこの問題は解決できない——セッションをまたいで持続し、実際の使用を通じて進化し、最も効果的な人間組織が何世紀もかけて築いてきたガバナンスの構造を反映した仕組みが必要だ。

Praxeology はその構造を提供する。あなたのコーディングツールの代替ではなく、それらの上に置かれる**憲法レイヤー**だ。エージェント群が、独立したチャットボットの寄せ集めではなく、一貫した組織として機能することを保証する。

---

## これは何か？

**Praxeology** は、普遍的な 4+1 階層ガバナンス構造に基づく、人間と AIの協働オペレーティングシステムだ。人間が戦略と原則を定め、AIエージェントはその範囲内で実行し、経験から学び、改善提案を返す。すべての目的ある行動——国家からAIエージェントまで——が同じ構造パターンに従うという観察から生まれた。

```
Strategy（なぜ）→ Doctrine（何を）→ Procedure（どうやって）→ Playbook（パターン）→ Execution（今すぐ）
```

上位階層は常に下位階層より優先される。例外なし。

---

## 同型性

同じ 4+1 階層構造が、組織された行動のあらゆる領域に現れる：

| 階層 | 国家法 | 軍事 | 企業 | 個人 | AIエージェント |
|------|--------|------|------|------|----------------|
| **1 Strategy** | 憲法 | 作戦目標 | ミッション・ビジョン | 個人の価値観 | システムプロンプト / 最高指令 |
| **2 Doctrine** | 制定法 | 交戦規則 | 企業方針 | 人生の原則 | 行動ガイドライン |
| **3 Procedure** | 規則 | 標準作業手順 | SOP / プロトコル | 習慣とルーティン | タスク指示 |
| **4 Playbook** | 判例法 / 先例 | 戦術・訓練 | ベストプラクティス | 学習済みパターン | Few-shot 例 |
| **実行作業計画** | 大統領令 | 作戦命令 | スプリント / 作業計画 | 日次 To-Do | アクティブコンテキスト |

この同型性こそが核心的テーゼだ——ガバナンスはドメイン固有ではない。パターンは普遍的だ。軍事部隊に機能するフレームワークは、スタートアップ、研究所、AIエージェントフリートにも機能する。

---

## クイックスタート

**Step 1 — クローン**

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
```

**Step 2 — セットアップ実行**

```bash
bash setup.sh
```

インタラクティブウィザードが組織名、ミッション、部門、エージェント、プロジェクトを質問する。完全なディレクトリ構造とすべてのブートストラップドキュメントを生成する。

**Step 3 — 起動**

```bash
bash launch.sh
```

ガバナンスシステムが稼働する。ルートの `CLAUDE.md` を開いて、AIエージェント向けに生成されたコンテキストを確認する。

> **Praxeology が初めての方は？** [docs/quickstart.md](docs/quickstart.md) の3ステップガイドから始め、エージェント設計については [docs/role-design.md](docs/role-design.md) を参照してほしい。

---

## 主な機能

| 機能 | 説明 |
|------|------|
| **SafetyGate** | 上位階層ドキュメントは、下位階層ドキュメントが上書きできないハードリミットを宣言できる |
| **Proposal Flow** | エージェントまたはチームメンバーは、構造化された Proposal フォーマットで修正案を提案できる |
| **SOP Evolution** | Procedure と Playbook は Review Cascade を経て昇格することで進化する |
| **Review Cascade** | 変更は上方へ伝播する：Playbook → Procedure → Doctrine → Strategy の一貫性チェック |
| **Reverse Flow** | Strategy の変更は下方へカスケードされる：下位階層はすべてレビュー対象としてフラグが立つ |
| **Department Codes** | 数値コード体系を持つ部門（NeoMakes インスタンスでは 1xx–7xx）とロール配置 |

---

## ディレクトリ構造

```
your-org/
├── CLAUDE.md                  # AIエージェント向けルートコンテキスト（生成済み）
├── launch.sh                  # 日次起動スクリプト（生成済み）
├── _standard/                 # ガバナンスドキュメント
│   ├── README.md              # すべてのガバナンス成果物のマスターインデックス
│   ├── {department}/          # 部門ごとのフォルダ（例: strategy, operations, finance, ...）
│   │   ├── STR-{NNN}.md      #   NeoMakes インスタンス: ceo, coo, cfo, cto, cdo, chro, ciso
│   │   ├── DOC-{NNN}.md
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # エージェント / チームメンバー定義
│   ├── CLAUDE.md              # 共有クルールール
│   └── {agent}/               # エージェントごとのサブディレクトリ
│       ├── CLAUDE.md          # エージェントのコンテキストとペルソナ
│       └── sop.md             # エージェントの SOP
├── _project/                  # アクティブプロジェクト
│   ├── .praxe/                # プロジェクトカード（ガバナンスメタデータ）
│   │   └── {project}.md       # ステータス、優先度、クルーアサイン、マイルストーン
│   └── {project}/             # 各プロジェクトディレクトリ（コード）
├── _setting/                  # 運用設定
│   ├── permissions.md         # アクセス制御マトリクス
│   └── integrations.md        # 外部サービス設定
├── docs/                      # フレームワークドキュメント
├── templates/                 # 再利用可能なドキュメントテンプレート
└── examples/                  # リファレンス実装
```

---

## ドメイン別適用例

### 企業

部門を組織の役割にマッピングする。各部門が自身のガバナンススタックを所有する。最上位の Strategy ドキュメントが組織の憲法となる。（NeoMakes インスタンスは CEO/COO/CFO/CTO/CDO/CHRO/CISO 部門を使用しているが、あなたのものはどんな名称でも構わない。）

### 研究所

役割を PI、ラボマネージャー、財務リード、システムリード、パートナーシップ、HR、セキュリティにマッピングする。同じ階層構造を使用する。Strategy ドキュメントにラボの研究ミッションと倫理上の制約を記述する。完全な研究所ウォークスルーは [docs/tutorial.md](docs/tutorial.md) を参照。

### 個人の生産性

1人での実装。CEO = あなた自身。Strategy = あなたの人生ミッション。Doctrine = 絶対に曲げられない原則。Procedure = 毎週のルーティン。Playbook = 蓄積されたベストプラクティス。Work Plan = 日次リスト。

### AIエージェントチーム

各 AIエージェントは `_crew/{agent}/CLAUDE.md` を持ち、役割、権限レベル、運用上の制約を定義する。ルートの `CLAUDE.md` がチームの共有憲法となる。上位階層ドキュメントは実行前にエージェントのコンテキストに先頭から付加される。

---

## フレームワークドキュメント

| ドキュメント | 説明 |
|-------------|------|
| [docs/architecture.md](docs/architecture.md) | 設計思想、コアメカニズム、普遍的なガバナンスパターン |
| [docs/getting-started.md](docs/getting-started.md) | 前提条件、インストール、最初のステップ |
| [docs/standard-system.md](docs/standard-system.md) | 4+1 階層ドキュメントシステムの詳細 |
| [docs/crew-system.md](docs/crew-system.md) | エージェント管理、SOP 自己進化、Review Cascade |
| [docs/tutorial.md](docs/tutorial.md) | ガバナンスされた AIエージェントチームを構築する完全ウォークスルー |

---

## サンプル

- [examples/solo-dev/](examples/solo-dev/) — ソロ開発者 + 3エージェント（最小構成）
- [examples/tech-startup/](examples/tech-startup/) — 初期段階のソフトウェア企業
- [examples/one-piece-crew/](examples/one-piece-crew/) — 完全なペルソナシステムを持つフィクションクルー（デモンストレーション）

---

## 本番運用事例 — NeoMakes（実インスタンス）

Praxeology は理論ではない。毎日実際の会社を動かしている。NeoMakes はこのフレームワークの1つのインスタンスであり、あなたのものは異なる形になる。

**[NeoMakes, Inc.](https://neomakes.com)** は、Praxeology によって統治された9つの AIエージェントを持つ1人法人として運営されている：

| 指標 | 値 |
|------|-----|
| エージェント数 | 9（7つの C-level 部門に組織化） |
| 制定済み規定 | 38件（全部門にわたる STR/DOC/PRC/PLY） |
| 日次運用 | Todo 管理、日次報告、週次計画、月次レビュー |
| インテグレーション | Claude Code + Discord（4チャンネル）+ Google Drive + Notion + Calendar |
| 自己進化 | エージェントが毎日 Standard Gap を検出 → 週次 Proposal → 月次改訂 |

エージェントは**Speech Rules**（文章数制限、トーン）、**Anti-Patterns**（禁止行動）、**Emotional Triggers**（状況依存の応答変化）を持つ定義済みペルソナを備えており、9エージェント全体で一貫した識別可能な行動を保証する。

### インテグレーションガイド

| ガイド | 説明 |
|-------|------|
| [Discord Integration](docs/discord-integration.md) | チャンネル構造、ボットメンション、ループ防止、ボット間通信 |
| [Google Drive Integration](docs/drive-integration.md) | シンボリックリンク設定、規定保存、ルームベースのワークスペース |
| [Crew Manager Dashboard](docs/crew-manager.md) | セッション監視、Todo 管理、権限承認のための Webダッシュボード |
| [Claude Code Setup](docs/claude-code-setup.md) | CLAUDE.md 階層、MCPサーバー、エージェントごとのセッション設定 |
| [Work Cycle](docs/work-cycle.md) | weekly.json/todo.json スキーマ、報告サイクル、Standard Gap 逆方向フロー |

---

## 背景

Praxeology は **[NeoMakes](https://neomakes.com)** が構築した——極限環境における人間と AIの相互作用の基盤技術を開発する1人法人だ。このフレームワークは、人間組織と同等の厳格さで、増え続ける AIエージェント群を統治する必要性から生まれた。

名称は「人間の行動の研究」を意味するプラクセオロジーに由来する。その洞察——目的ある行動には構造がある。その構造は普遍的だ。それを明示化すれば、あらゆるものを統治できる。

---

## ライセンス

MIT License — [LICENSE](LICENSE) を参照。

Copyright (c) 2026 NeoMakes
