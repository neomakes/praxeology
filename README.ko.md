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

## 🌐 언어

[English](README.md) · **한국어** · [日本語](README.ja.md) · [中文](README.zh.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md)

다른 문서: [QUICKSTART](docs/quickstart.md) ([한국어](docs/quickstart.ko.md) · [日本語](docs/quickstart.ja.md) · [中文](docs/quickstart.zh.md)) · [ROLE-DESIGN](docs/role-design.md) ([한국어](docs/role-design.ko.md) · [日本語](docs/role-design.ja.md) · [中文](docs/role-design.zh.md))

---

## 왜 Praxeology인가?

[gstack](https://github.com/gstack-io/gstack)과 [oh-my-claudecode](https://github.com/anthropics/claude-code) 같은 도구들은 개별 AI 에이전트의 생산성 — 검색, 코딩, 테스트, 배포 — 을 높이는 데 탁월하다. 그러나 **에이전트 하나**에서 **여러 에이전트가 함께 일하는 구조**로 확장되는 순간, 새로운 문제가 생긴다: **거버넌스**.

거버넌스 없이는 에이전트들이 작업을 중복하고, 서로 모순된 결과를 내고, 경계를 침범하고, 시간이 지나면서 본래 역할에서 벗어난다. 프롬프트 엔지니어링만으로는 해결되지 않는다 — 세션을 넘어 지속되고, 사용하면서 진화하며, 수백 년간 인간 조직이 행동을 통제해온 방식을 반영하는 구조가 필요하다.

Praxeology가 그 구조를 제공한다. 기존 코딩 도구를 대체하는 것이 아니다 — 그 위에 올라가는 **헌법 계층**으로, 에이전트들이 독립적인 챗봇의 집합이 아닌 일관된 조직으로 작동하도록 보장한다.

---

## 무엇인가?

**Praxeology**는 보편적인 4+1 계층 거버넌스 체계를 기반으로 한 인간-AI 협업 운영 체제다. 인간이 전략과 원칙을 설정하면, 에이전틱 AI가 그 범위 안에서 실행하고, 경험으로부터 배우고, 개선안을 역방향으로 제안한다. 국가에서 에이전틱 AI에 이르기까지 모든 목적 있는 행동은 동일한 구조적 패턴을 따른다는 관찰에서 출발한다.

```
Strategy (WHY) → Doctrine (WHAT) → Procedure (HOW) → Playbook (PATTERNS) → Execution (NOW)
```

상위 계층은 항상 하위 계층보다 우선한다. 예외 없음.

---

## 동형성 (The Isomorphism)

동일한 4+1 계층 구조가 조직화된 행동의 모든 영역에 나타난다:

| 계층 | 국가 법체계 | 군사 | 기업 | 개인 | AI 에이전트 |
|------|------------|------|------|------|------------|
| **1 Strategy** | 헌법 | 작전 목표 | 미션 & 비전 | 개인 가치관 | System Prompt / Prime Directive |
| **2 Doctrine** | 성문법 | 교전 규칙 | 기업 정책 | 삶의 원칙 | 행동 지침 |
| **3 Procedure** | 시행령 | 표준 운영 절차 | SOP / 프로토콜 | 습관 & 루틴 | 작업 지침 |
| **4 Playbook** | 판례법 | 전술 & 훈련 | 모범 사례 | 학습된 패턴 | Few-shot 예제 |
| **Exec Work Plan** | 행정 명령 | 임무 명령 | Sprint / 업무 계획 | 일일 할일 | Active Context |

이 동형성이 핵심 명제다: 거버넌스는 특정 도메인에 종속되지 않는다. 패턴은 보편적이다. 군사 부대에 작동하는 체계는 스타트업, 연구소, 또는 AI 에이전트 팀에도 작동한다.

---

## 빠른 시작

**1단계 — Clone**

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
```

**2단계 — 설정 실행**

```bash
bash setup.sh
```

대화형 마법사가 조직 이름, 미션, 부서, 에이전트, 프로젝트를 물어본다. 전체 디렉토리 구조와 모든 부트스트랩 문서를 생성한다.

**3단계 — 시작**

```bash
bash launch.sh
```

거버넌스 시스템이 활성화된다. 루트의 `CLAUDE.md`를 열어 AI 에이전트용으로 생성된 컨텍스트를 확인한다.

> **Praxeology가 처음이라면?** [docs/quickstart.md](docs/quickstart.md)의 3단계 가이드와 에이전트 설계를 위한 [docs/role-design.md](docs/role-design.md)를 먼저 읽는다.

---

## 주요 기능

| 기능 | 설명 |
|------|------|
| **SafetyGate** | 상위 계층 문서가 하위 계층에서 절대 재정의할 수 없는 하드 리밋을 선언한다 |
| **Proposal Flow** | 모든 에이전트 또는 팀원이 구조화된 Proposal 형식으로 개정안을 제안할 수 있다 |
| **SOP Evolution** | Procedure와 Playbook이 Review Cascade를 통해 승격 전에 진화한다 |
| **Review Cascade** | 변경사항이 상향 전파된다: Playbook → Procedure → Doctrine → Strategy 일관성 검토 |
| **Reverse Flow** | Strategy 변경이 하향 전파된다: 모든 하위 계층이 검토 대상으로 표시된다 |
| **Department Codes** | 숫자 코드 체계를 가진 부서 (NeoMakes 인스턴스 기준 1xx–7xx) 및 역할 배정 |

---

## 디렉토리 구조

```
your-org/
├── CLAUDE.md                  # AI 에이전트용 루트 컨텍스트 (생성됨)
├── launch.sh                  # 일일 시작 스크립트 (생성됨)
├── _standard/                 # 거버넌스 문서
│   ├── README.md              # 모든 거버넌스 산출물의 마스터 인덱스
│   ├── {department}/          # 부서별 폴더 (예: strategy, operations, finance, ...)
│   │   ├── STR-{NNN}.md      #   NeoMakes 인스턴스: ceo, coo, cfo, cto, cdo, chro, ciso
│   │   ├── DOC-{NNN}.md
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # 에이전트 / 팀원 정의
│   ├── CLAUDE.md              # 공유 크루 규칙
│   └── {agent}/               # 에이전트별 서브디렉토리
│       ├── CLAUDE.md          # 에이전트 컨텍스트 및 페르소나
│       └── sop.md             # 에이전트 SOP
├── _project/                  # 활성 프로젝트
│   ├── .praxe/                # 프로젝트 카드 (거버넌스 메타데이터)
│   │   └── {project}.md       # 상태, 우선순위, 크루 배정, 마일스톤
│   └── {project}/             # 각 프로젝트 디렉토리 (코드)
├── _setting/                  # 운영 설정
│   ├── permissions.md         # 접근 제어 매트릭스
│   └── integrations.md        # 외부 서비스 설정
├── docs/                      # 프레임워크 문서
├── templates/                 # 재사용 가능한 문서 템플릿
└── examples/                  # 참조 구현
```

---

## 도메인별 적용

### 기업

부서를 조직 역할에 매핑한다. 각 부서가 자체 거버넌스 스택을 소유한다. 최상위 Strategy 문서가 조직의 헌법이다. (NeoMakes 인스턴스는 CEO/COO/CFO/CTO/CDO/CHRO/CISO 부서를 사용하지만, 어떤 구성도 가능하다.)

### 연구소

역할을 PI, 랩 매니저, 재무 책임자, 시스템 책임자, 파트너십, HR, 보안으로 매핑한다. 동일한 계층 구조를 사용한다. Strategy 문서가 랩의 연구 미션과 윤리적 제약을 담는다. 전체 연구소 walkthrough는 [docs/tutorial.md](docs/tutorial.md)를 참조한다.

### 개인 생산성

1인 구현. CEO = 자신. Strategy = 삶의 미션. Doctrine = 절대 포기하지 않는 원칙. Procedure = 주간 의식. Playbook = 축적된 모범 사례. Work Plan = 일일 할일.

### AI 에이전트 팀

각 AI 에이전트는 역할, 권한 수준, 운영 제약을 정의하는 `_crew/{agent}/CLAUDE.md`를 가진다. 루트 `CLAUDE.md`가 팀의 공유 헌법이다. 상위 계층 문서가 실행 전에 에이전트 컨텍스트에 앞붙임된다.

---

## 프레임워크 문서

| 문서 | 설명 |
|------|------|
| [docs/architecture.md](docs/architecture.md) | 설계 철학, 핵심 메커니즘, 보편적 거버넌스 패턴 |
| [docs/getting-started.md](docs/getting-started.md) | 사전 요구사항, 설치, 첫 단계 |
| [docs/standard-system.md](docs/standard-system.md) | 4+1 계층 문서 시스템 심층 분석 |
| [docs/crew-system.md](docs/crew-system.md) | 에이전트 관리, SOP 자기 진화, Review Cascade |
| [docs/tutorial.md](docs/tutorial.md) | 거버넌스 AI 에이전트 팀 구축 전체 walkthrough |

---

## 예제

- [examples/solo-dev/](examples/solo-dev/) — 솔로 개발자 + 에이전트 3개 (최소 설정)
- [examples/tech-startup/](examples/tech-startup/) — 초기 단계 소프트웨어 회사
- [examples/one-piece-crew/](examples/one-piece-crew/) — 완전한 페르소나 시스템을 갖춘 가상 크루 (데모)

---

## 실제 운영 사례 — NeoMakes

Praxeology는 이론이 아니다. 매일 실제 회사를 운영한다. NeoMakes는 이 프레임워크의 한 인스턴스다 — 여러분의 것은 다르게 보일 것이다.

**[NeoMakes, Inc.](https://neomakes.com)**는 Praxeology로 관리되는 9개의 AI 에이전트를 가진 1인 회사로 운영된다:

| 지표 | 값 |
|------|---|
| 에이전트 | 9개 (7개 C-level 부서에 편성) |
| 시행 규정 | 38건 (전 부서에 걸친 STR/DOC/PRC/PLY) |
| 일상 운영 | 할일 추적, 일일 보고, 주간 계획, 월간 리뷰 |
| 통합 | Claude Code + Discord (채널 4개) + Google Drive + Notion + Calendar |
| 자기 진화 | 에이전트가 매일 Standard Gap 감지 → 주간 Proposal → 월간 개정 |

에이전트들은 **Speech Rules** (문장 제한, 어조), **Anti-Patterns** (금지 행동), **Emotional Triggers** (상황별 응답 변화)를 갖춘 정의된 페르소나를 가진다 — 9개 에이전트 전반에 걸쳐 일관되고 구별 가능한 행동을 보장한다.

### 통합 가이드

| 가이드 | 설명 |
|--------|------|
| [Discord Integration](docs/discord-integration.md) | 채널 구조, 봇 멘션, 루프 방지, 봇 간 소통 |
| [Google Drive Integration](docs/drive-integration.md) | 심링크 설정, 규정 저장, 룸 기반 업무 공간 |
| [Crew Manager Dashboard](docs/crew-manager.md) | 세션 모니터링, 할일 관리, 권한 승인 웹 대시보드 |
| [Claude Code Setup](docs/claude-code-setup.md) | CLAUDE.md 계층, MCP 서버, 에이전트별 세션 설정 |
| [Work Cycle](docs/work-cycle.md) | weekly.json/todo.json 스키마, 보고 사이클, Standard Gap 역방향 흐름 |

---

## 기원

Praxeology는 **[NeoMakes](https://neomakes.com)**가 만들었다 — 극한 환경에서의 인간-AI 상호작용 원천 기술을 개발하는 1인 회사. 인간 조직에 적용하는 것과 동일한 엄격함으로 증가하는 AI 에이전트 집단을 거버넌스할 필요에서 이 프레임워크가 탄생했다.

이름은 인간 행동을 연구하는 학문인 praxeology(행동학)에서 왔다. 핵심 통찰: 목적 있는 행동에는 구조가 있다. 그 구조는 보편적이다. 명시적으로 만들면 무엇이든 거버넌스할 수 있다.

---

## 라이선스

MIT License — [LICENSE](LICENSE) 참조.

Copyright (c) 2026 NeoMakes
