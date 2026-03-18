# [SDS] 프로젝트 neotoc: 소프트웨어 설계 사양서 (Software Design Specification)

## 1. 시스템 아키텍처 (The Agent Ecosystem: Laptop, Smartphone & WebApp)

**neotoc**은 분산된 경량 지능(Agent)과 중앙화된 전문 에이전트 마켓플레이스(WebApp)가 결합된 하이브리드 지능형 생태계입니다.

### 1.1. 구성도 (Architectural Swarm)

```mermaid
graph TD
    User([Use: Commander]) <--> Hub[neotoc macOS Hub]
    Hub <--> Registry[Agent Registry: (a)-(d) Mgmt]
    Registry -- "Spawn" --> Agent[neocog Agent: Software-Defined]
    Agent <--> Body[iphoneLogger: Sensory Context]
    Agent <--> Verify[neolat: Mastery Verification]
    Agent -- "Surprise/Action" --> D2A[D2A Engine: Arbiter]
    D2A -- "Tooling" --> Tools[n8n / Native APIs]
    Hub --> UI[Briefing Stream UI]
```

## 2. 모듈 및 컴포넌트 설계

### 2.1. Prof (Professional Agent / Perk) 규격

마켓플레이스에서 공유되는 'Prof'는 다음과 같은 표준 인터페이스를 가집니다.

- **Standard Profile (a)-(d)**:
  - **(a) I/O Protocol**: 데이터 입출력 및 트리거 규격.
  - **(b) Backbone Swapper**: sLLM 가중치 설정.
  - **(c) K-S-M Cluster**: 지식, 기능, 기억 레이어.
  - **(d) Tactical Doctrine**: Behavior Tree 기반 ROE.
- **Manifest**: 이름, 초상화, 저작자 정보 등 마켓플레이스 메타데이터.

### 2.2. WebApp Integration (The Bridge)

Laptop 앱은 WebApp API와 통신하여 다음 기능을 수행합니다.

- **Authentication**: 지휘관(Use)의 계정 인증 및 구매한 Prof 목록 동기화.
- **Provisioning**: 구매한 Prof의 리소스(모델 설정, 워크플로우)를 로컬 n8n 환경으로 자동 배포.
- **Update**: 제작자가 Prof를 업데이트할 때 버전 관리 및 동기화.

## 3. 기술 스택 (Technical Stack)

- **Frontend (Laptop/Mobile)**: SwiftUI (macOS / iOS)
- **Marketplace (WebApp)**: Next.js / Node.js (Web platform for sharing/selling)
- **Orchestration**: n8n (Embedded or Local Service)
- **Intelligence**: Ollama / Apple MLX (optimized for 2-3B models)
- **Storage**: Vector DB (Qdrant/Chroma) & Local SQLite

## 4. 데이터 및 보안 설계 (Security & Data)

- **Prof Sandbox**: 외부 제작자가 만든 Prof는 격리된 환경에서 실행되며, 로컬 시스템 자원에 접근 시 지휘관의 명시적 승인이 필요함.

### 2.3. Self-Modification Loop (System 2)

- **Error Detection**: `eigenllm`이 자신의 예측 오차($VFE$)가 지속적으로 높거나 지휘관의 교정(Correction)이 빈번할 경우, '지적 모델 불일치' 상태로 정의.
- **Distillation**: n8n은 외부 지식(RAG) 또는 상위 모델의 사고 체인을 로컬 2-3B 모델에 주입하여 가중치(LoRA)를 미세 조정하거나 프롬프트를 자가 수정함.
- **Safety**: 모든 자가 수정 결과는 `neolat` 샌드박스에서 기존 성능(KPI) 유지 여부를 검증받은 후 시스템에 적용됨.

### 2.4. Sensory-Actuator Loop

- **Active Sensing**: 불확실성이 높은 상황에서 에이전트는 `iphoneLogger`를 통해 Flash 광량을 조절하거나 Haptic 피드백을 발생시켜 더 명확한 주위 환경 데이터를 획득함.

## 5. UI/UX 디자인 (Warm & Peaceful Theme)

- **Persona Consistency**: 각 Prof는 고유의 페르소나를 가지지만, 전체 UI는 'Warm & Peaceful' 디자인 시스템을 따름.
- **Transparency**: 현재 어떤 Prof가 어떤 데이터에 접근하고 있는지 지휘관이 직관적으로 알 수 있도록 표시.
- **Seamless Flow**: Laptop(작전 수립)과 Smartphone(상황 확인 및 간이 명령) 간의 끊김 없는 컨텍스트 이동 지원.
