# First App Revenue Playbook — First 3 Screens Benchmark

## 목적
경쟁 앱들이 첫 진입에서 어떤 흐름으로 사용자를 잡는지 보고, 우리 앱의 첫 3개 화면을 더 날카롭게 만든다.

이 문서는 `docs/hq/first-app-strategy-principles.md`를 따른 **상위 3개 화면 벤치마크**다.

## Benchmark 대상
- SafetyCulture iAuditor: https://safetyculture.com/iauditor
- Fulcrum: https://www.fulcrumapp.com/
- GoCanvas: https://www.gocanvas.com/

> 이 문서는 제품 웹사이트와 공개 제품 설명을 기준으로 한 **첫 진입 흐름 벤치마크**다. 실제 앱 내부 UI의 완전한 스크린샷 대체가 아니라, 사용자가 처음 접하는 경험의 구조를 보는 용도다.

---

## 1) SafetyCulture iAuditor

### Screen 1 — Hero / Value Proposition
- 가장 먼저 보여주는 것은 inspection / checklist / report 가치를 한 문장으로 압축한 메시지
- 사용자가 바로 이해하는 키워드: inspection, forms, reports, safety
- CTA는 보통 데모/시작/가입 계열

### Screen 2 — Use-case proof
- 현장 점검, 안전, 품질, 운영 같은 실제 사용 시나리오를 보여준다
- 템플릿 / 체크리스트 / 리포트 이미지로 신뢰를 만든다

### Screen 3 — Conversion path
- demo / trial / contact sales / get started 로 유도
- 제품 사용보다 “조직 도입” 느낌이 강하다

### 우리에게 주는 교훈
- 시장은 이미 “점검 → 보고서” 흐름에 익숙하다
- 그러나 우리는 도입형 플랫폼이 아니라 **즉시 결과를 만드는 단일 작업 앱**이어야 한다

---

## 2) Fulcrum

### Screen 1 — Hero / Platform framing
- field process and data collection platform이라는 범용 프레임을 먼저 건다
- 데이터 수집, 모바일 입력, 자동화가 강조된다

### Screen 2 — Workflow / feature blocks
- 폼 작성, 모바일 데이터, 워크플로 자동화, 리포트 같은 모듈을 나눠 보여준다
- 플랫폼형 가치가 강하다

### Screen 3 — Proof / integration / enterprise cue
- 고객 사례, 통합, 보안, 확장성을 보여주며 B2B 신뢰를 만든다

### 우리에게 주는 교훈
- 현장 앱은 “기능 묶음”보다 “작업 흐름”으로 이해시키는 게 중요하다
- 하지만 우리는 플랫폼이 아니라 **보고서 산출물 중심의 좁은 UX**로 가야 한다

---

## 3) GoCanvas

### Screen 1 — Hero / digitize work
- mobile field work management, digitize workflows 같은 언어로 진입
- 업무를 디지털화한다는 큰 약속을 먼저 건다

### Screen 2 — Template / workflow examples
- 다양한 업무 템플릿과 폼 예시를 보여준다
- 사용자는 "우리 업무도 이걸로 바꿀 수 있겠네"를 느낀다

### Screen 3 — Sales conversion
- trial, demo, contact, use case expansion으로 이어진다
- 다용도 플랫폼 느낌이 강하다

### 우리에게 주는 교훈
- 템플릿의 힘은 분명하다
- 하지만 템플릿을 너무 많이 보여주면 오히려 범용 플랫폼이 된다
- 우리는 2~3개 템플릿만 보여주는 편이 더 낫다

---

## 우리 앱의 권장 첫 3개 화면

### Screen 1 — Home
- `+ 새 보고서 시작`
- 최근 보고서
- 템플릿 둘러보기

### Screen 2 — Photo Add
- 카메라로 찍기
- 갤러리에서 선택
- 추가된 사진 썸네일

### Screen 3 — Photo Note Input
- 사진 미리보기
- 짧은 메모
- 상태 태그 3개 이하

## 왜 이 구조가 다른가
- 경쟁 앱은 플랫폼/도입/데모 중심
- 우리는 **단일 작업 완료** 중심
- 경쟁 앱은 넓게 판다
- 우리는 좁고 빠르게 끝낸다

## UX 벤치마크 요약
- **경쟁사**: 문제를 넓게 정의하고, 도입과 확장을 유도한다
- **우리**: 문제를 좁게 정의하고, 첫 결과물을 빠르게 만든다

## 구현 우선순위에 반영할 것
1. 첫 화면에서 시작 버튼을 가장 크게 둔다
2. 사진 추가는 카메라/갤러리 2개만 둔다
3. 메모 입력은 한 줄 중심으로 만든다
4. 템플릿은 2~3개만 보여준다
5. PDF 내보내기를 결과 화면의 첫 행동으로 둔다

## 다음 액션
- 이 벤치마크를 바탕으로 `Home`, `Photo Add`, `Photo Note Input` 화면을 실제 구현 스펙으로 더 세분화한다.
