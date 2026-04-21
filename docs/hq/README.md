# Hermes HQ Docs

이 디렉터리는 Hermes HQ의 SSOT 문서 영역입니다.

## 빠른 입구

- `docs/hq/decision-log.md` — 중요한 판단 기록
- `docs/hq/01-전략/아카이브-인사이트-흡수-2026-04-21.md` — Threads/NaverCafe archive-to-HQ 일일 흡수 리포트
- `docs/hq/youtube-benchmark-application-2026-04-15.md` — 외부 벤치마크를 TemperStone HQ 규칙으로 번역한 메모
- `docs/hq/global-first-app-recommendation.md` — 앱 후보를 고르는 기준
- `docs/hq/first-app-revenue-app-research.md` — 사진→보고서 앱 리서치 메모
- `docs/hq/first-app-revenue-proposal.md` — 첫 앱 제안서
- `docs/hq/first-app-revenue-scope-fixed.md` — 타깃 고객과 범위 확정
- `docs/hq/first-app-revenue-implementation-tickets.md` — 구현 티켓 7개
- `docs/hq/first-app-revenue-screen-spec.md` — 화면별 구현 스펙
- `docs/hq/first-app-revenue-solo-dev-feasibility.md` — 1인 개발 가능성 판정
- `docs/hq/first-app-revenue-effort-estimate.md` — 기능별 예상 공수
- `docs/hq/first-app-revenue-release-plan.md` — 출시 기준 전체 개발 계획
- `docs/hq/first-app-revenue-execution-checklist.md` — 30일 실행 체크리스트
- `docs/hq/first-app-revenue-photo-report-exploration.md` — 현재 탐색 중인 Android-first 사진→보고서 방향 SSOT 초안
- `docs/hq/first-app-revenue-photo-report-screen-map.md` — 사진→보고서 MVP 화면 구조 / 상태 정의
- `docs/hq/first-app-revenue-photo-report-wireframe-3-screens.md` — 사진→보고서 첫 3개 화면 와이어프레임 초안
- `docs/hq/first-app-revenue-photo-report-preview-screen.md` — 보고서 미리보기 / PDF 내보내기 화면 초안
- `docs/hq/first-app-revenue-photo-report-design-tokens.md` — 사진→보고서 디자인 토큰 초안
- `docs/hq/first-app-revenue-photo-report-component-inventory.md` — 사진→보고서 컴포넌트 인벤토리 초안
- `docs/hq/first-app-revenue-photo-report-development-order.md` — 기존 HQ 플로우를 이 앱에 적용한 실행 순서
- `docs/hq/first-app-revenue-ux-tool-choice.md` — 사진→보고서 앱의 UX 초안 도구 선택( Pencil MCP 1순위 )
- `docs/hq/pencil-mcp-prompt-photo-report.md` — Pencil MCP용 사진→보고서 초안 프롬프트
- `docs/hq/initiative-card-first-app.md` — 첫 앱 이니셔티브 카드
- `docs/hq/ai-ux-development-flow.md` — AI 디자인 선행 → 기준안 고정 → 코드 구현 기본 흐름
- `docs/hq/ai-ux-product-brief-template.md` — 앱 개발 시작용 제품 브리프 템플릿
- `docs/hq/ai-ux-screen-map-template.md` — 화면/흐름 정의 템플릿
- `docs/hq/ai-ux-development-review-checklist.md` — 개발 플로우 검수 체크리스트
- `docs/hq/app-market-discovery-2026-04-14.md` — 앱 시장조사(discovery) 로그
- `docs/hq/app-market-discovery-week1-action-items-v1.md` — discovery 실행 체크리스트
- `docs/hq/discord-channel-topology.md` — Discord 채널 구조와 역할
- `docs/hq/discord-channel-routing-one-pager.md` — 채널 라우팅 빠른 규칙
- `docs/hq/discord-channel-operating-map.md` — 운영 관점 채널 역할/라우팅
- `docs/hq/discord-channel-role-map.md` — 채널 역할과 기본 정책
- `docs/hq/discord-channel-youtube-routing-checklist.md` — YouTube/콘텐츠 채널 라우팅 체크리스트

## 권장 원칙

- 운영/의사결정/클레임/증빙은 `docs/hq/` 아래에 둡니다.
- 원본 증빙(이메일, 영수증 스캔, 사진)은 사건별 폴더에 보관합니다.
- 각 사건 폴더에는 `README.md`를 두고, 무엇이 어디에 있는지 한눈에 보이게 합니다.
- 민감한 원본 파일은 파일명에 내용을 드러내지 않게 간단히 보관합니다.

## 추천 구조

```text
docs/hq/
  personal/
    claims/
      YYYY-MM-DD-incident-name/
        README.md
        evidence/
        notes/
```

필요하면 이 구조를 기준으로 새 사건 폴더를 계속 추가하면 됩니다.
