# First App Revenue — Photo-to-Report Design Tokens Draft

> 참고: 이 문서는 `docs/hq/first-app-strategy-principles.md`와 `docs/hq/first-app-doc-map.md`를 기준으로 읽는 보조 문서다.

## 목적
`사진 → 보고서 생성` 앱의 MVP UI를 일관되게 만들기 위한 토큰 초안이다.

## 원칙
- raw value를 화면마다 직접 쓰지 않는다
- 색 / 간격 / 타이포 / radius / shadow는 토큰으로 관리한다
- 이 토큰은 Figma Variables와 이름을 맞출 것을 전제로 한다
- v1은 단순하고 적은 수의 토큰만 둔다

---

## Color tokens

### Surface
- `color.bg.primary` — 앱 기본 배경
- `color.bg.secondary` — 카드 / 서브 영역
- `color.bg.elevated` — 미리보기 / 시트 / 모달

### Text
- `color.text.primary` — 본문
- `color.text.secondary` — 보조 문구
- `color.text.muted` — 빈 상태 / 힌트
- `color.text.inverse` — 어두운 배경 위 텍스트

### Accent / Action
- `color.action.primary` — 주요 CTA
- `color.action.primaryText` — 주요 CTA 텍스트
- `color.action.secondary` — 보조 CTA
- `color.action.disabled` — 비활성 상태

### Status
- `color.status.success`
- `color.status.warning`
- `color.status.danger`
- `color.status.info`

### Border
- `color.border.default`
- `color.border.subtle`
- `color.border.focus`

---

## Spacing tokens
- `space.1` — 4
- `space.2` — 8
- `space.3` — 12
- `space.4` — 16
- `space.5` — 20
- `space.6` — 24
- `space.8` — 32
- `space.12` — 48

---

## Radius tokens
- `radius.sm` — 8
- `radius.md` — 12
- `radius.lg` — 16
- `radius.xl` — 24

---

## Typography tokens
- `type.title.lg`
- `type.title.md`
- `type.body.md`
- `type.body.sm`
- `type.caption`
- `type.button`

### 권장 사용
- `title.lg` — 화면 타이틀
- `title.md` — 섹션 타이틀
- `body.md` — 본문 / 라벨
- `body.sm` — 설명 / 보조 텍스트
- `caption` — 메타 정보 / 상태
- `button` — CTA 텍스트

---

## Shadow tokens
- `shadow.sm` — 카드/칩 미세 그림자
- `shadow.md` — 모달/시트
- `shadow.lg` — 최상위 오버레이

---

## Component state tokens
- `state.hover`
- `state.pressed`
- `state.focus`
- `state.selected`
- `state.disabled`

---

## Layout tokens
- `layout.screenPadding` — 16
- `layout.sectionGap` — 24
- `layout.cardPadding` — 16
- `layout.itemGap` — 12

---

## App-specific UI mapping

### Home
- 배경: `color.bg.primary`
- CTA: `color.action.primary`
- 최근 보고서 카드: `color.bg.secondary`, `radius.md`, `shadow.sm`

### New Report
- 입력칸: `color.bg.elevated`, `color.border.default`, `radius.md`
- 시작 버튼: `color.action.primary`

### Photo Input
- 썸네일 카드: `color.bg.secondary`
- 메모 입력: `color.bg.elevated`
- 사진 추가 버튼: `color.action.secondary`

### Preview
- 미리보기 카드: `color.bg.elevated`, `radius.lg`, `shadow.md`
- PDF 내보내기 버튼: `color.action.primary`

---

## v1에서 더 필요해질 수 있는 토큰
- `color.imageOverlay`
- `color.reportStatus.good`
- `color.reportStatus.issue`
- `type.report.heading`
- `type.report.meta`

## v1에서 아직 안 넣어도 되는 것
- 애니메이션 토큰
- 복잡한 dark mode 세트
- 브랜드 테마 팩
- 다중 제품군 컬러 시스템

## 다음 액션
- 이 토큰을 기반으로 컴포넌트 인벤토리를 정리한다
- Figma Variables 이름과 1:1로 매칭한다
