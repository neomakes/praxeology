# NeoTOC

> **AI 에이전트에게 구체적인 페르소나와 Behavior Tree를 부여하여, 안전하게 통제하면서 팀처럼 운영하는 오픈소스 프레임워크**

원피스의 밀짚모자 해적단에서 영감을 받았습니다. 각 에이전트는 고유한 성격, 역할, 행동 규칙을 가지고 있습니다. 단순히 작업을 실행하는 것이 아니라 — 역할에 몰입하고, 경계를 존중하며, 진짜 크루처럼 보고합니다.

## 비전

### v1 — 현재 아키텍처

```
루피 (나) → OMC 오케스트레이터 → 에이전트 배정 → 텔레그램 단방향 보고
```

선장이 명령을 내리면, 오케스트레이터(oh-my-claudecode)가 적절한 크루를 배정합니다. 각 에이전트는 Behavior Tree 규칙 안에서 실행하고 텔레그램으로 보고합니다.

### v2 — 꿈 (로드맵)

**사우전드 써니호**: 텔레그램 그룹에 작업을 던지면 크루가 스스로 조직화합니다.

```
루피:    "베이지안 서치 알고리즘 구현 필요"
Robin:   "관련 논문 3편 찾았어. 먼저 분석할게."
Zoro:    "구현 준비 완료. Robin 끝나면 바로 시작."
Nami:    "예상 토큰 비용 $2.30. 오프피크 추천."
Usopp:   "테스트 준비할게! 버그 하나라도 나오면 가만 안 둬!"
Sanji:   "의존성 잠금 완료. 환경 서빙 준비됐어."
```

각 크루가 자율적으로 논의하고, 역할을 나누고, 실행하고, 보고합니다. 선장은 필요할 때만 개입합니다.

## 철학 — NeoRoger

NeoTOC는 **NeoRoger** 기반 위에 세워졌습니다:

| 기둥 | 기원 | 적용 |
|------|------|------|
| **행위론 (Praxeology)** | 미제스 — 인간 행위의 논리 | 에이전트는 정의된 제약 안에서 목적적으로 행동 |
| **심성론 (Thymology)** | 미제스 — 인간 가치의 이해 | 각 페르소나는 행동을 이끄는 가치관을 보유 |
| **Behavior Tree** | 게임 AI — 구조화된 의사결정 트리 | 행동은 통제 가능하고, 예측 가능하며, 디버깅 가능 |
| **Ralph Loop** | 지속성 엔진 | 진짜 완료될 때까지 반복 — 조용한 실패 없음 |
| **Root Guard** | 안전 장치 | 매 틱마다 루트 노드가 경계를 강제 |
| **AAR** | 군사 — 사후행동검토 | 중요한 행동은 반드시 인간의 검토와 승인 필요 |

## 크루

| 멤버 | 역할 | 전문 영역 |
|------|------|----------|
| **Zoro** | 코드 실행자 | 핵심 구현, 리팩토링, 커밋 |
| **Nami** | 항해사 & CFO | 프로젝트 계획, 토큰 비용, 리소스 관리 |
| **Usopp** | QA 엔지니어 & 테스터 | 테스트, 버그 사냥, 엣지 케이스 탐지 |
| **Sanji** | DevOps & 의존성 관리자 | 패키지, 환경, 공급망 |
| **Chopper** | 건강 & 웰빙 모니터 | 사용자 번아웃 감지, 건강 체크 |
| **Robin** | 정보 & 리서치 분석가 | 연구, 아키텍처 분석, 경쟁 인텔리전스 |
| **Franky** | 인프라 엔지니어 | CI/CD, 빌드, 배포, 인프라 |
| **Brook** | 문서 & 세션 아키비스트 | 로그, 리포트, 체인지로그, 지식 보존 |
| **Jinbe** | 통합 & 안정성 엔지니어 | MCP 커넥터, 외부 서비스, 시스템 안정성 |

## 현재 스택

- **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** — AI 에이전트 런타임
- **[oh-my-claudecode (OMC)](https://github.com/nicobailon/oh-my-claudecode)** — 멀티 에이전트 오케스트레이션 레이어
- **[gstack](https://github.com/anthropics/claude-code)** — 개발 도구
- **Telegram G-Staff** — 크루 보고 채널

## 프로젝트 구조

```
neotoc/
├── README.md              # 영어 버전
├── README.ko.md           # 이 파일 (한국어)
├── CLAUDE.md              # Claude Code 글로벌 설정
├── RULES.md               # Behavior Tree 규칙
├── crew/                  # 크루 멤버 페르소나 정의
│   ├── zoro.md            # 코드 실행자
│   ├── nami.md            # 항해사 & CFO
│   ├── usopp.md           # QA 엔지니어 & 테스터
│   ├── sanji.md           # DevOps & 의존성 관리자
│   ├── chopper.md         # 건강 & 웰빙 모니터
│   ├── robin.md           # 정보 & 리서치 분석가
│   ├── franky.md          # 인프라 엔지니어
│   ├── brook.md           # 문서 & 세션 아키비스트
│   └── jinbe.md           # 통합 & 안정성 엔지니어
├── templates/             # 작업 및 세션 템플릿
│   ├── TASKS.md
│   └── SESSION.md
└── docs/                  # 설계 문서
    └── neeroger-blueprint.md
```

## 시작하기

```bash
# 저장소 클론
git clone https://github.com/neomakes/neotoc.git
cd neotoc

# 크루 탐색
ls crew/

# 규칙 확인
cat RULES.md

# 블루프린트 확인
cat docs/neeroger-blueprint.md
```

## 기여하기

NeoTOC는 오픈소스 프로젝트입니다. 이슈와 PR을 환영합니다.

크루 멤버의 페르소나 개선, 새로운 BT 규칙 추가, 새로운 크루 멤버 제안 — 무엇이든 환영합니다. 사우전드 써니호에는 모두를 위한 자리가 있습니다.

## 라이선스

MIT License
