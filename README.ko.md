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
  <a href="README.ko.md"><strong>한국어</strong></a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.es.md">Español</a>
</p>

<p align="center">
  <a href="docs/quickstart.md">Quick Start</a> (<a href="docs/quickstart.ko.md">한국어</a> · <a href="docs/quickstart.ja.md">日本語</a> · <a href="docs/quickstart.zh.md">中文</a> · <a href="docs/quickstart.fr.md">FR</a> · <a href="docs/quickstart.de.md">DE</a> · <a href="docs/quickstart.es.md">ES</a>) ·
  <a href="docs/role-design.md">Role Design</a> (<a href="docs/role-design.ko.md">한국어</a> · <a href="docs/role-design.ja.md">日本語</a> · <a href="docs/role-design.zh.md">中文</a> · <a href="docs/role-design.fr.md">FR</a> · <a href="docs/role-design.de.md">DE</a> · <a href="docs/role-design.es.md">ES</a>)
</p>

---

## 문제

**병렬화는 해결됐다.** Today's AI coding tools 이 도구들은 이미 개별 AI 에이전트를 믿기 어려울 만큼 생산적으로 만든다. 5개 에이전트를 병렬로 실행하는 것은 해결된 문제다.

**조율은 아니다.** 그 5개의 에이전트가 작업을 마쳤을 때, 누가 충돌을 해결하는가? 누가 일관성을 검증하는가? 누가 에이전트 A가 에이전트 B의 결정을 덮어쓰는 것을 막는가? 누가 세션 간 역할 이탈을 막는가? 멀티에이전트 프레임워크는 *시작*을 해결한다 — Praxeology는 그 이후를 해결한다: **조율, 상태 추적, 충돌 해소, 진화적 정렬.**

**Praxeology는 빠진 거버넌스 레이어다.** 코딩 도구 위에 위치하며, 대체하는 것이 아니라 — 에이전트들이 독립된 챗봇의 집합이 아닌 일관된 조직으로 운영되도록 보장한다.

---

## 프로덕션 증거

이론이 아니다. [NeoMakes](https://neomakes.com)는 이것을 매일 운영한다.

> **1인 + 9 AI 에이전트 · 38개 거버넌스 규칙 · 7개 부서**
> 일일 할일 → 주간 리뷰 → 월간 개정
> 에이전트들이 갭을 감지하고, 수정안을 제안하며, 자체 SOP를 진화시킨다.

각 에이전트에는 **Speech Rules**(문장 제한, 어조), **Anti-Patterns**(금지 행동), **Emotional Triggers**(상황별 응답 변화)가 정의되어 있어 — 9개 에이전트 전반에 걸쳐 일관되고 구별 가능한 행동을 보장한다. NeoMakes는 하나의 사례다. 당신의 것은 다르게 보일 것이다.

---

## 작동 방식

4+1 계층 거버넌스 구조. 단순하다. 범용적이다.

```
전략 (WHY) → 독트린 (WHAT) → 절차 (HOW) → 플레이북 (PATTERNS) → 실행 (NOW)
```

상위 계층은 항상 하위 계층을 재정의한다. 예외 없다. 에이전트는 상황을 커버하는 첫 번째 레벨에서 멈추며 계층을 올라가면서 결정을 해소한다.

---

## 무엇이 다른가

기능 목록이 아니다. 조율 문제 해결사다.

| 당신의 문제 | Praxeology의 답변 |
|---|---|
| 에이전트가 세션 간 역할에서 벗어난다 | **ConstitutionalGuard** — 4계층 행동 검증 |
| 에이전트 행동을 안전하게 제한할 방법이 없다 | **SafetyGate** — 상위 계층이 하위 계층이 재정의할 수 없는 중요 규칙을 잠근다 |
| 에이전트가 자체 프로세스를 개선할 수 없다 | **SOP Evolution** — Learn-Compress-Apply 루프. 거버넌스를 위한 경사 하강법 |
| 한 곳의 변경이 다른 곳을 망친다 | **Review Cascade** — 양방향 전파(계층 위아래로) |
| 에이전트가 규칙이 잘못됐을 때 표시할 수 없다 | **Proposal Flow** — 모든 에이전트에서 창업자에게 구조화된 개정 요청 |
| 세션 간 기관 기억이 없다 | **Work Cycle** — 일일 갭 → 주간 제안 → 월간 개정 → 분기 리뷰 |

---

## 빠른 시작

```bash
git clone https://github.com/neomakes/praxeology.git my-org
cd my-org
bash setup.sh    # 대화형 마법사: 조직명, 미션, 부서, 에이전트
bash launch.sh   # 거버넌스 시스템 가동
```

> **처음이라면?** [빠른 시작 가이드](docs/quickstart.md)와 [역할 설계 가이드](docs/role-design.md)부터 시작하세요.

---

## 에이전트 설계 시스템

모든 에이전트는 *무엇*을 하는지뿐만 아니라 *어떻게* 행동하는지를 정의하는 `CLAUDE.md`를 받는다:

```
Identity → Persona → Speech Rules → Anti-Patterns → Emotional Triggers → Values → Boundaries
```

이것은 에이전트를 **구별 가능하고, 일관적이며, 경계가 있게** 만든다. QA 에이전트는 실행자와 다르게 들린다. 플래너는 절대 코드를 작성하지 않는다. 리뷰어는 자신의 작업을 절대 승인하지 않는다. 전체 템플릿과 확장 전략(3명에서 15명 이상의 에이전트)은 [역할 설계 가이드](docs/role-design.md)를 참조하라.

---

## 예제

- [examples/solo-dev/](examples/solo-dev/) — 솔로 개발자 + 3개 에이전트 (최소 구성)
- [examples/tech-startup/](examples/tech-startup/) — 초기 단계 소프트웨어 회사
- [examples/one-piece-crew/](examples/one-piece-crew/) — 완전한 페르소나 시스템을 갖춘 가상 크루

---

<details>
<summary><strong>이론 — 왜 이것이 작동하는가 (동형성)</strong></summary>

동일한 4+1 계층 구조가 조직적 행동의 모든 영역에 걸쳐 나타난다:

| 계층 | 국가 법률 | 군사 | 기업 | 개인 | AI 에이전트 |
|------|-------------|----------|-----------|------------|----------|
| **1 전략** | 헌법 | 작전 목표 | 미션 & 비전 | 개인 가치관 | System Prompt / Prime Directive |
| **2 독트린** | 성문법 | 교전 규칙 | 기업 정책 | 삶의 원칙 | 행동 지침 |
| **3 절차** | 규정 | 표준 운영 절차 | SOP / 프로토콜 | 습관 & 루틴 | 태스크 지침 |
| **4 플레이북** | 판례법 / 선례 | 전술 & 훈련 | 모범 사례 | 학습된 패턴 | Few-shot 예제 |
| **실행** | 행정 명령 | 임무 명령 | 스프린트 / 작업 계획 | 일일 할일 | 활성 컨텍스트 |

거버넌스는 도메인 특화적이지 않다. 패턴은 보편적이다. 군사 부대에 작동하는 프레임워크는 스타트업, 연구소, AI 에이전트 플릿에도 작동한다.

</details>

---

## 디렉토리 구조

```
your-org/
├── CLAUDE.md                  # AI 에이전트용 루트 컨텍스트 (생성됨)
├── launch.sh                  # 일일 실행 스크립트 (생성됨)
├── _standard/                 # 거버넌스 문서
│   ├── README.md              # 모든 거버넌스 산출물의 마스터 인덱스
│   ├── {department}/          # 부서당 하나의 폴더
│   │   ├── STR-{NNN}.md      #   (예: 전략, 운영, 재무, 엔지니어링)
│   │   ├── DOC-{NNN}.md
│   │   ├── PRC-{NNN}.md
│   │   └── PLY-{NNN}.md
├── _crew/                     # 에이전트 / 팀원 정의
│   ├── CLAUDE.md              # 공유 크루 규칙
│   └── {agent}/               # 에이전트별 서브디렉토리
│       ├── CLAUDE.md          # 에이전트 컨텍스트 및 페르소나
│       └── sop.md             # 에이전트 SOP
├── _project/                  # 활성 프로젝트
├── _setting/                  # 운영 설정
├── docs/                      # 프레임워크 문서
├── templates/                 # 재사용 가능한 문서 템플릿
└── examples/                  # 참조 구현
```

---

## 통합 가이드

| 가이드 | 설명 |
|-------|-------------|
| [Discord 통합](docs/discord-integration.md) | 채널 구조, 봇 멘션, 루프 방지 |
| [Google Drive 통합](docs/drive-integration.md) | 심볼릭 링크 설정, 규정 저장, 작업 공간 |
| [Crew Manager 대시보드](docs/crew-manager.md) | 세션 모니터링용 웹 대시보드 |
| [Claude Code 설정](docs/claude-code-setup.md) | CLAUDE.md 계층, MCP 서버, 에이전트별 세션 |
| [Work Cycle](docs/work-cycle.md) | Todo/weekly 스키마, 보고 사이클, Standard Gap 흐름 |

## 문서

| 문서 | 설명 |
|----------|-------------|
| [docs/architecture.md](docs/architecture.md) | 설계 철학 및 핵심 메커니즘 |
| [docs/getting-started.md](docs/getting-started.md) | 사전 요구사항, 설치, 첫 단계 |
| [docs/standard-system.md](docs/standard-system.md) | 4+1 계층 문서 시스템 심화 |
| [docs/crew-system.md](docs/crew-system.md) | 에이전트 관리, SOP 자기 진화 |
| [docs/tutorial.md](docs/tutorial.md) | 거버넌스 에이전트 팀 구축 전체 안내 |

---

## 기원

**[NeoMakes](https://neomakes.com)**가 만들었다 — 극한 환경을 위한 온디바이스 AI를 개발하는 1인 회사. 이 프레임워크는 군사 지휘 구조에 적용되는 것과 동일한 엄격함으로 AI 에이전트 플릿을 통치하면서 탄생했다.

이름은 인간 행동 연구인 실천학(praxeology)에서 왔다. 목적 있는 행동에는 구조가 있다. 그 구조는 보편적이다. 명시적으로 만들면, 무엇이든 통치할 수 있다.

---

## 라이선스

MIT 라이선스 — [LICENSE](LICENSE) 참조.

Copyright (c) 2026 NeoMakes
