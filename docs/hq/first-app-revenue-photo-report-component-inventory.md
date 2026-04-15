# First App Revenue — Photo-to-Report Component Inventory

> 참고: 이 문서는 `docs/hq/first-app-strategy-principles.md`와 `docs/hq/first-app-doc-map.md`를 기준으로 읽는 보조 문서다.

## 목적
`사진 → 보고서 생성` 앱에서 v1에 필요한 컴포넌트만 뽑아, Figma / Stitch / Claude Code / Storybook 기준으로 재사용 가능하게 만든다.

## 원칙
- 화면별로 새로 만들지 말고 컴포넌트를 조합한다
- v1은 적은 수의 컴포넌트로 끝낸다
- 상태별 변형을 먼저 정의한다
- 이름은 토큰과 맞춰서 간다

---

## 1. Navigation / Shell

### AppHeader
- 화면 타이틀
- 뒤로가기
- 우측 액션(옵션)

### BottomNav (optional)
- 홈
- 새 보고서
- 최근 보고서

> v1에서는 BottomNav 없이 단순 흐름으로 시작해도 됨

---

## 2. Primary actions

### PrimaryButton
- 가장 중요한 CTA
- 예: 새 보고서 만들기, PDF 내보내기

### SecondaryButton
- 보조 행동
- 예: 공유하기, 갤러리에서 선택

### IconButton
- 카메라, 추가, 삭제, 재정렬용

---

## 3. Input components

### TextField
- 프로젝트명
- 위치 / 작업명
- 메모

### DatePickerField
- 날짜 선택

### PhotoPicker
- 카메라 촬영
- 갤러리 선택

### MemoField
- 사진별 1줄 메모

---

## 4. Content components

### RecentReportCard
- 홈에서 최근 보고서 표시
- 제목 / 날짜 / 사진 수 / 상태

### PhotoThumbCard
- 사진 썸네일
- 순서 표시
- 삭제 / 이동 가능

### ReportSection
- 보고서 미리보기에서 섹션 단위 표시
- 사진 + 메모 묶음

### StatusChip
- 조치 필요 / 주의 / 완료 같은 상태 표시

### EmptyState
- 첫 실행 / 사진 없음 / 보고서 없음

---

## 5. Preview / Export components

### PreviewCard
- 최종 보고서 미리보기 블록
- 이미지, 메모, 상태, 제목 포함

### ExportBar
- PDF 내보내기
- 공유하기
- 저장 상태 표시

### ExportProgress
- PDF 생성 중
- 진행률 또는 스피너

---

## 6. Feedback components

### InlineError
- 입력 오류
- 권한 거부
- 저장 실패

### Toast / Snackbar
- 저장 완료
- 공유 완료
- PDF 생성 성공

### PermissionPrompt
- 카메라 권한
- 저장 권한

---

## 7. Layout components

### ScreenSection
- 화면 내 구역
- title + content

### Card
- 리스트 / 미리보기 / 최근 보고서

### Divider
- 사진/섹션 구분

### Spacer
- 간격 유지

---

## MVP 상태별 필요 컴포넌트

### Home
- AppHeader
- PrimaryButton
- RecentReportCard
- EmptyState

### New Report
- TextField
- DatePickerField
- PhotoPicker
- PrimaryButton

### Photo Input
- PhotoThumbCard
- MemoField
- IconButton
- PrimaryButton

### Preview
- PreviewCard
- StatusChip
- ExportBar
- ExportProgress

---

## 컴포넌트 우선순위
### 반드시 먼저 만들어야 하는 것
1. PrimaryButton
2. TextField
3. PhotoPicker
4. PhotoThumbCard
5. PreviewCard
6. ExportBar
7. EmptyState

### 나중에 해도 되는 것
- BottomNav
- Advanced status components
- Fancy animation wrappers
- Multi-template UI
- Complex filter/search components

---

## Storybook용 우선 상태
- Button / primary / default / disabled
- TextField / empty / filled / error
- PhotoThumbCard / one photo / multiple photos
- PreviewCard / with images / without images
- EmptyState / no reports / no photos
- ExportBar / idle / exporting / success / error

## 다음 액션
- 이 인벤토리를 바탕으로 **Pencil MCP 또는 Stitch에 넣을 프롬프트**를 만든다
- 그리고 기능 우선순위를 기준으로 실제 화면에 매핑한다
