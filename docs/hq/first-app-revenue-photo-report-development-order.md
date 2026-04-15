# First App Revenue — Photo-to-Report Development Order

> 참고: 이 문서는 `docs/hq/first-app-strategy-principles.md`와 `docs/hq/first-app-doc-map.md`를 기준으로 읽는 보조 문서다.

## 목적
`사진 → 보고서 생성` 앱을 TemperStone HQ의 AI UX 플로우에 맞춰 실제 개발로 넘기기 위한 실행 순서를 고정한다.

## 이 문서의 위치
이 문서는 아래 기존 HQ 플로우 문서들을 이 앱에 맞게 적용한 실행 순서다.
- `docs/hq/ai-ux-development-flow.md`
- `docs/hq/ai-ux-app-development-workflow-order.md`
- `docs/hq/ai-ux-app-start-10min-checklist.md`
- `docs/hq/ai-ux-product-brief-template.md`
- `docs/hq/ai-ux-screen-map-template.md`
- `docs/hq/ai-ux-development-review-checklist.md`

## 이번 앱에 맞는 운영 원칙
- discovery 신호가 먼저다
- 타깃 고객 1개를 먼저 고정한다
- 경쟁 앱은 3~5개만 깊게 본다
- 화면보다 작업 흐름을 먼저 고정한다
- AI 초안은 빠르게 만들되, 기준안은 사람이 잠근다
- 구현은 tokens → components → screens → states → polish 순으로 간다
- 각 단계마다 HQ 문서가 하나씩 남아야 한다

## 권장 순서

### 1) Product Brief를 짧게 고정
이미 정리한 문서:
- `docs/hq/first-app-revenue-photo-report-exploration.md`

확인할 것:
- 한 문장 정의
- 타겟 사용자
- 핵심 작업 1~3개
- MVP 포함 / 제외
- 플랫폼 우선순위: Android-first

### 2) Screen Map으로 작업 흐름 고정
이미 정리한 문서:
- `docs/hq/first-app-revenue-photo-report-screen-map.md`

핵심 흐름:
- 홈
- 새 보고서 만들기
- 사진 + 메모
- 미리보기
- PDF 내보내기 / 공유

### 3) 첫 3개 화면 와이어프레임 고정
이미 정리한 문서:
- `docs/hq/first-app-revenue-photo-report-wireframe-3-screens.md`

이 단계에서 확인할 것:
- 첫 화면에서 새 보고서 CTA가 바로 보이는가
- 입력이 너무 많지 않은가
- 사진 입력 흐름이 빠른가

### 4) 미리보기 / 내보내기 화면 고정
이미 정리한 문서:
- `docs/hq/first-app-revenue-photo-report-preview-screen.md`

이 단계에서 확인할 것:
- 결과물이 곧 결과물처럼 보이는가
- PDF 내보내기가 가장 명확한가
- 공유는 보조 행동으로 충분한가

### 5) Design Tokens 확정
이미 정리한 문서:
- `docs/hq/first-app-revenue-photo-report-design-tokens.md`

확인할 것:
- 색 / 간격 / radius / typography / shadow
- Figma Variables와 1:1로 맞출 이름
- raw value 사용 금지

### 6) Component Inventory 확정
이미 정리한 문서:
- `docs/hq/first-app-revenue-photo-report-component-inventory.md`

우선순위:
1. PrimaryButton
2. TextField
3. PhotoPicker
4. PhotoThumbCard
5. PreviewCard
6. ExportBar
7. EmptyState

### 7) AI 초안 도구 선택
현재 후보:
- Stitch
- Pencil MCP
- Figma AI

권장 운영:
- 초안 생성: Stitch 또는 Pencil MCP
- 정리 / 조정: Figma
- 코드 연결: Claude Code

### 8) Claude Code 구현 프롬프트 작성
기준:
- 기준 디자인 밖 스타일 추가 금지
- tokens → shared components → screen shells → states → polish 순서
- loading / empty / error / disabled 상태 포함

### 9) 실제 구현 시작
구현 우선순위:
1. design tokens
2. shared components
3. screen shells
4. interactions
5. states
6. polish

### 10) Review Checklist로 검수
사용 문서:
- `docs/hq/ai-ux-development-review-checklist.md`

판정:
- green: ship-ready
- yellow: 가능하지만 수정 필요
- red: 구조 재조정 필요

## 사진→보고서 앱에 맞는 특이사항
- Android-first로 시작한다
- OCR은 v1에서 과하게 넣지 않는다
- 폼 빌더는 넣지 않는다
- 보고서 미리보기 품질을 우선시한다
- PDF export를 핵심 가치로 둔다

## 한 줄 요약
> **브리프 → 화면 흐름 → 와이어프레임 → 미리보기 → 토큰 → 컴포넌트 → AI 초안 → Claude Code 구현 → 검수**
