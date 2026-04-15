# First App Revenue — UX Tool Choice

## 결론
현재 `사진 → 보고서 생성` 앱의 첫 UX 초안 도구는 **Pencil MCP**를 1순위로 쓴다.

## 이유
- 이 앱은 **Claude Code 중심 개발**과 잘 맞아야 한다.
- Pencil MCP는 디자인 캔버스를 Claude Code 작업 문맥과 직접 연결하기 좋다.
- 우리는 단순 시안 생성보다 **디자인 ↔ 코드 싱크**를 더 중요하게 본다.
- Figma만 단독으로 쓰면 디자인과 코드가 분리되기 쉽다.
- Stitch는 빠르지만, 이번 목표는 “초안 생성”보다 **개발 흐름까지 연결된 초안**이다.

## 역할 분담

### 1) Pencil MCP — primary
- 첫 UX 초안 생성
- 화면 구조 확인
- Claude Code가 읽을 수 있는 디자인 문맥 확보
- 반복 수정

### 2) Figma — secondary
- 정리 / 합의 / 변수화
- 토큰, 컴포넌트, 간격 정돈
- 최종 시각 기준안 고정

### 3) Stitch — optional
- 초반 대안 탐색이 더 필요할 때 사용
- 완전 다른 레이아웃이나 빠른 아이디어 비교용
- 최종 기준안 도구는 아님

## 이번 앱에 맞는 추천 흐름
1. HQ 문서 기준으로 브리프 / screen map / wireframe / preview / tokens / components를 고정한다.
2. Pencil MCP로 첫 UI 캔버스를 뽑는다.
3. Claude Code가 그 캔버스를 기준으로 screen shells와 shared components를 맞춘다.
4. Figma로 토큰 / 컴포넌트 정리만 최소한으로 한다.
5. 마지막에 review checklist로 검수한다.

## 첫 초안에서 확인할 것
- 홈에서 새 보고서 CTA가 바로 보이는가
- 사진 입력이 첫 행동으로 자연스러운가
- 미리보기가 결과물처럼 보이는가
- PDF export가 가장 강하게 보이는가
- Android 네비게이션 관습이 자연스러운가

## 바로 써야 할 원칙
- 디자인 초안은 여러 개일 수 있지만, 기준안은 1개만 둔다.
- 새 스타일은 추가하지 않는다.
- v1은 보고서 생성과 export에 집중한다.
- OCR / 고급 AI는 뒤로 미룬다.

## 다음 액션
- Pencil MCP용 첫 프롬프트를 작성한다.
- 그 프롬프트는 `사진 → 보고서`의 4개 화면(홈, 새 보고서, 사진 입력, 미리보기)을 한 번에 기준안으로 잡는 형태여야 한다.
