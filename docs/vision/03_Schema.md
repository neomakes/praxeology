# [Schema] neotoc: 통합 데이터 및 마켓플레이스 스키마 (Unified & Marketplace Schema)

## 1. 개요 (Schema Scope)

**neotoc**의 스키마는 지휘관(Use)의 개인 데이터뿐만 아니라, 외부에서 유입되는 전문 에이전트(Prof)의 메타데이터와 마켓플레이스(WebApp) 연동 정보를 통합 관리합니다.

## 2. 핵심 엔티티 스키마 (Core Entities)

### 2.1. Prof (Marketplace Perk Metadata)

Webapp에서 지휘관의 환경으로 배포되는 전문 에이전트의 정보입니다.

```json
{
  "prof_id": "string (UUID)",
  "version": "semver",
  "author_id": "string",
  "pricing": { "currency": "USD | KRW", "amount": number },
  "agent_specs": {
    "a_io": { "input_schema": "object", "triggers": ["n8n_webhook", "grpc_stream"] },
    "b_backbone": { "model_family": "Llama | Phi | Gemma", "quantization": "4bit | 8bit" },
    "c_ksm": { "knowledge_base": "vector_id", "skills": ["n8n_nodes", "scripts"], "memory_tier": "long_term" },
    "d_roe": { "behavior_tree": "json_logic", "critical_threshold": number }
  },
  "mastery_score": { "cognitive": number, "operational": number, "social": number, "personality": number },
  "required_permissions": ["calendar", "health", "files", "network"]
}
```

### 2.2. Use (User Device Context)

Laptop 및 Smartphone 기기 간의 동기화와 지휘관의 설정을 관리합니다.

```json
{
  "user_id": "string (UUID)",
  "devices": [
    { "device_id": "string", "type": "laptop | smartphone", "os": "macOS | iOS" }
  ],
  "installed_profs": [
    { "prof_id": "string", "install_date": "ISO8601", "is_active": boolean }
  ],
  "preference": { "theme": "warm_peaceful | dark", "sync_enabled": boolean }
}
```

### 2.3. Agent Memory & Metrics

임포트된 Prof와 기본 Agent들이 사용하는 동적 데이터 저장소입니다.

```json
{
  "entity_id": "string",
  "type": "agent_memory",
  "owner_prof_id": "string (null for system agent)",
  "working_memory": { "current_task": "text", "context_window": ["text"] },
  "episodic_memory_keys": ["string (vector_ids)"],
  "metrics": [
    { "metric_id": "string", "current_value": "any", "target": "any" }
  ]
}
```

## 3. 데이터 동기화 및 보안 (Sync & Security)

### 3.1. WebApp Synchronization

- WebApp은 Prof의 **'정의(Manifest)'**만을 관리하며, 실제 구동 데이터는 Use의 Laptop/Smartphone 로컬 DB에만 존재합니다.
- 동기화 시 Prof의 식별자와 라이선스 정보만을 대조합니다.

### 3.2. Data Extraction with Prof Expertise

- 2~3B 모델을 활용한 비정형 데이터 추출 시, 현재 대화에 참여 중인 Prof의 전문 지식(System Prompt)을 주입하여 추출의 정확도를 높입니다.
- 추출된 데이터는 지휘관의 승인 하에 `Semantic Memory` 레이어로 확정됩니다.

## 4. 메모리 계층 구조 (Memory Layers Revisited)

- **Local Working Memory**: 개별 장치(Laptop/Smartphone)의 실시간 대화 상태.
- **Synced Episodic Memory**: 여러 기기 간에 암호화되어 동기화되는 과거 사건의 서사적 기록.
- **Marketplace Knowledge**: WebApp을 통해 업데이트되는 전문 지식 및 툴셋(Profs).
