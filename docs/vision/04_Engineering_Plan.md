# [Engineering Plan] neotoc: 마켓플레이스 기반 프론트/백엔드 기획 (Advanced Engineering Plan)

## 1. 프론트엔드 기획 (Frontend Swarm)

### 1.1. 듀얼 네이티브 앱 (Dual Native Experience)

- **Use Laptop (macOS)**:
  - **SwiftUI** 기반의 메인 지휘소.
  - n8n 로컬 엔진 관리, 모델 서빙(Ollama/MLX) 및 전문 데이터 분석용 대화면 지원.
- **Use Smartphone (iOS)**:
  - **SwiftUI / WidgetKit** 기반의 기동형 모니터.
  - 리얼타임 알림, 간편한 G-1 주관적 상태 보고 및 주요 KPI 위젯 제공.

### 1.2. WebApp Bridge (The StoreFront)

- **Web UI**: Next.js 기반의 마켓플레이스.
  - 제작자가 **(a)-(d) 패키지**를 업로드하고 검증 점수를 공개하는 전술 시장.
  - 지휘관이 신규 병사를 탐색하고 자신의 로컬 레지스트리에 영입하는 인터페이스.
- **Agent Sync**: 마켓플레이스의 병사 설정을 로컬 `neocog` 인스턴스로 즉시 주입 및 훈련 시작.

---

## 2. 백엔드 기획 (Distributed Intelligence)

### 2.1. Prof Provisioning Engine (in n8n)

- **The Arbiter (D2A)**: n8n의 복잡한 절차적 로직을 에이전트의 '도구 호출(Function Calling)'이 아닌 '교리 해석(Arbiter)' 단계로 진화시킴.
- **Context Swapping**: 복수의 모델이 아닌, 병사별 LoRA/프롬프트/메모리 레이어를 비트 단위로 교체하여 자원 극소화.
- **Mastery Testing (neolat)**: 모든 병사의 행위(Action)를 `neolat`이 감시하며, 교리 준수율이 떨어질 경우 지휘관에게 재훈련 권고.

---

## 3. 유통 및 수익 모델 (Distribution & Revenue)

### 3.1. Prof Package Format (.perk)

- n8n JSON 워크플로우, 프롬프트 텍스트, 아이콘, 메타데이터를 하나의 압축 파일 형태로 표준화.
- WebApp 서버에서 무결성 검증 및 서명 날인 후 배포.

### 3.2. Revenue Sharing System

- **WebApp Backend**: 스트라이프(Stripe) 등 결제 연동.
- **Payout Logic**: 지휘관의 결제 금액이 확정되면 플랫폼 수수료를 제외한 금액을 제작자 지갑으로 정산.

## 4. R&D: Active Sensing & Calibration

- **Feature**: `iphoneLogger`의 고주파 데이터를 기반으로 에이전트의 'Saccadic Attention'을 보정.
- **Goal**: 하드웨어 가열/배터리 상태에 따라 에이전트의 연산 강도(Ticks)를 능동적으로 조절하는 프로프라이오셉션(Proprioception) 보정 알고리즘 개발.

## 5. 구동 및 설치 시나리오 (Ecosystem Flow)

1. **Explore**: 지휘관이 WebApp에서 '부동산 투자 분석 Prof'를 발견.
2. **Purchase**: 구매 완료 후 "Laptop에 즉시 설치" 버튼 클릭.
3. **Provision**: Laptop 앱이 실행되며 n8n에 해당 Prof의 전술 로직과 전문 지식(2-3B용 프롬프트)을 자동 배포.
4. **Interact**: DailyRoom에 새로운 참모(Prof)가 합류하여 지휘관의 부동산 관련 데이터를 분석하기 시작.
