# NeoTOC - Claude Code 글로벌 설정

## 프레임워크 컨텍스트

이 프로젝트는 NeoTOC 프레임워크를 사용합니다.
Claude Code 에이전트는 `crew/` 디렉토리의 페르소나 정의와 `RULES.md`의 BT 규칙을 따라야 합니다.

## 행동 규칙

### 필수 준수 사항

1. **페르소나 준수**: 활성화된 크루 멤버의 역할 범위 내에서만 작업
2. **BT 규칙 준수**: `RULES.md`에 정의된 Behavior Tree를 따를 것
3. **Root Guard 활성**: 허용 범위를 벗어나는 작업은 즉시 중단하고 보고
4. **AAR 필수**: 중요 변경사항은 반드시 AAR 보고서를 생성

### 안전 제한

- 프로덕션 데이터베이스에 직접 접근 금지
- 인증 정보를 코드에 하드코딩 금지
- 파괴적 git 명령(force push, reset --hard) 실행 전 반드시 확인
- 외부 서비스 호출 시 사전 승인 필요

### 작업 흐름

1. 작업 수신 → 해당 크루 멤버 활성화
2. BT 규칙에 따라 실행 계획 수립
3. Root Guard 체크 통과 후 실행
4. 완료 후 AAR 보고서 생성
5. 인간 승인 대기

## 커밋 컨벤션

```
[crew] 작업 설명

예시:
[zoro] 인증 모듈 리팩토링
[chopper] 로그인 버그 수정
[robin] API 엔드포인트 코드 리뷰
[nami] Q3 마일스톤 계획 수립
[franky] CI/CD 파이프라인 구축
[brook] API 문서 업데이트
```

## 템플릿 사용

- 작업 추적: `templates/TASKS.md`
- 세션 기록: `templates/SESSION.md`
