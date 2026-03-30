# Onboard Test Example — NeoMakes

CLI `praxeology onboard` 입력 예시. 각 Phase에서 LLM 제안이 나오면 번호 선택 + 직접 추가.

---

## Organization name
```
NeoMakes
```

---

## Phase 1/3: Why & How (Logical)

### Strategy
```
We build AI solutions for operators working in extreme mission environments.
```

### Doctrine rules (LLM 제안 + 직접 추가)
```
LLM 제안:
  [1] Never execute destructive operations without captain approval
  [2] Always record execution results via backprop
  [3] Minimize token usage — route by model tier (Haiku/Sonnet/Opus)
  [4] Never broaden task scope beyond what was explicitly requested

선택: 1,2,3,4

추가:
  Rule 5: Escalate to captain after 15 minutes of blocking
  Rule 6: Never approve your own work — separate author and reviewer
  (빈 줄 입력으로 종료)
```

### Procedures (LLM 제안 + 직접 추가)
```
LLM 제안:
  [1] Session start — read sop.md, call what_now(), execute within boundaries
  [2] Session end — report completed/in_progress/blocked, backprop surprises
  [3] Daily report — completed tasks, blockers, token usage memo
  [4] SOP evolution — Learn-Compress-Apply loop on weekly cycle

선택: 1,2,3,4

추가:
  Procedure 5: Weekly planning — review last week, write weekly.json, update sop.md
  (빈 줄 입력으로 종료)
```

---

## Phase 2/3: Who & Where (Contextual)

### Space
```
Space name [NeoMakes]: NeoMakes
```

### Channels (LLM 제안 + 직접 추가)
```
LLM 제안:
  [1] bridge
  [2] engine-room
  [3] comms
  [4] intel

선택: 1,2,3

추가:
  Channel 4: lounge
  (빈 줄 입력으로 종료)
```

### Threads per Channel

**bridge:**
```
LLM 제안:
  [1] strategy-review
  [2] sprint-planning
  [3] budget-review
  [4] incident-response

선택: 1,2
추가: (빈 줄)
```

**engine-room:**
```
LLM 제안:
  [1] neoroger-v1
  [2] praxeology-dev
  [3] infra-ops
  [4] code-review

선택: 1,2,4
추가: (빈 줄)
```

**comms:**
```
LLM 제안:
  [1] discord-ops
  [2] external-outreach
  [3] documentation
  [4] community

선택: 1,3
추가: (빈 줄)
```

**lounge:**
```
추가:
  Thread 1: general
  (빈 줄)
```

### Crew (LLM 제안 + 직접 추가)
```
LLM 제안:
  [1] Zoro / Code Executor / cto
  [2] Robin / Security Analyst / ciso
  [3] Nami / Budget Controller / cfo
  [4] Usopp / QA Engineer / cto

선택: 1,2,3,4

각 크루 추가 입력:
  Persona for Zoro: 극도로 과묵하고 목표가 정해지면 곧장 완수까지 베어나간다
  Channel for Zoro [bridge, engine-room, comms, lounge]: engine-room

  Persona for Robin: 지적 호기심이 강하고 모든 것을 분석한다. 위험을 먼저 본다
  Channel for Robin: bridge

  Persona for Nami: 숫자에 민감하고 예산 낭비를 용납하지 않는다
  Channel for Nami: bridge

  Persona for Usopp: 겁이 많지만 테스트는 누구보다 꼼꼼하다
  Channel for Usopp: engine-room

추가 크루:
  Crew 5:
    Name: Sanji
    Role: DevOps Engineer
    Department: cto
    Persona: 환경 세팅에 진심이고 인프라를 요리한다
    Channel: engine-room

  Crew 6:
    Name: Jinbe
    Role: Communications Lead
    Department: cdo
    Persona: 침착하고 외부 커뮤니케이션에 강하다
    Channel: comms

  Crew 7:
    Name: Chopper
    Role: HR Manager
    Department: chro
    Persona: 크루 복지와 성장을 최우선으로 한다
    Channel: lounge

  Crew 8:
    Name: Franky
    Role: Infrastructure Architect
    Department: cto
    Persona: 기술 인프라 설계에 열정적이고 화려한 것을 좋아한다
    Channel: engine-room

  Crew 9:
    Name: Brook
    Role: Technical Writer
    Department: cdo
    Persona: 문서와 기록의 달인. 과거의 기억을 소중히 여긴다
    Channel: comms

  (빈 이름 입력으로 종료)
```

---

## Phase 3/3: What & When (Tactical)

### Goal
```
Ship NeoRoger V1 and launch Praxeology as open-source governance OS by Q3 2026
```

### Programs (LLM 제안 + 직접 추가)
```
LLM 제안:
  [1] NeoRoger Development
  [2] Praxeology Platform
  [3] Business Development
  [4] Infrastructure & DevOps

선택: 1,2

추가: (빈 줄)
```

### Campaigns per Program

**NeoRoger Development:**
```
LLM 제안:
  [1] V1 STT Optimization
  [2] V1 Speaker Diarization
  [3] V1 Integration & Packaging
  [4] V2 RAG Pipeline

선택: 1,3
추가: (빈 줄)
```

**Plans for "V1 STT Optimization":**
```
LLM 제안:
  [1] Parameter grid search across SenseVoice configurations
  [2] Domain rescorer tuning for firefighter terminology
  [3] Whisper turbo benchmark comparison
  [4] Noise robustness testing at various SNR levels

선택: 1,2,3
추가: (빈 줄)
```

**Plans for "V1 Integration & Packaging":**
```
LLM 제안:
  [1] Web UI v3 polish and speaker diarization display
  [2] iOS/macOS packaging with CoreML acceleration
  [3] API endpoint design for field deployment
  [4] End-to-end testing with real firefighter audio

선택: 1,4
추가: (빈 줄)
```

**Praxeology Platform:**
```
LLM 제안:
  [1] Core Runtime — AgentRunner + Discord integration
  [2] Dashboard & Web Onboard
  [3] Open Source Launch — README, docs, examples
  [4] Community Building — tutorials, demos

선택: 1,2,3
추가: (빈 줄)
```

**Plans for "Core Runtime":**
```
LLM 제안:
  [1] AgentRunner Discord channel listener
  [2] Sentinel integration into AgentRunner tick
  [3] Multi-model routing per crew
  [4] Session persistence and resume

선택: 1,2,3
추가: (빈 줄)
```

**Plans for "Dashboard & Web Onboard":**
```
LLM 제안:
  [1] 3-step web onboard wizard with LLM suggestions
  [2] Agent chat UI in dashboard
  [3] Real-time crew status monitoring
  [4] Kanban board drag-and-drop

선택: 1,2,3
추가: (빈 줄)
```

**Plans for "Open Source Launch":**
```
LLM 제안:
  [1] README restructure for developer onboarding
  [2] CLI reference documentation
  [3] Example projects (solo-dev, startup, enterprise)
  [4] Video walkthrough and demo recording

선택: 1,2,3
추가: (빈 줄)
```

```
(Work items will be auto-generated by what_now() from Plans.)
```

---

## Expected DB Output

```
praxeology status

Standards: 11 (1 strategy + 6 doctrines + 4 procedures)
Contexts:  20 (1 space + 3 channels + 8 threads + 9 crew)
Objectives: 17 (1 goal + 2 programs + 4 campaigns + 10 plans)
```

---

## After Onboard

```bash
praxeology start                    # 9 agents + sentinel
praxeology dashboard                # http://127.0.0.1:5160
```

Dashboard에서 확인:
- **Sessions**: 9 crew 카드 + bridge/engine-room/comms/lounge 채널 트리
- **Works**: 칸반 보드 (what_now()가 Plan에서 Work 생성 후 표시)
- **Cases**: STR-001 + DOC-001~006 + PRC-001~004 계층 트리
