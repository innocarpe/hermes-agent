# First App Revenue Playbook — App Research Memo

> 참고: 이 문서는 `docs/hq/first-app-strategy-principles.md`와 `docs/hq/first-app-doc-map.md`를 기준으로 읽는 보조 문서다.

## 결론
**실제 고객이 있는 앱 방향 맞습니다.**
다만 결론은 “범용 보고서 앱”이 아니라, **현장 사진 + 메모 + PDF 보고서**가 반복되는 워크플로를 가진 고객군으로 좁혀야 합니다.

## 선택한 기회 공간
- 부동산 관리
- 시설 유지보수
- 현장 점검
- 보험 / 피해 기록
- 소규모 건설 / 수리 현장

이 고객군은 공통적으로:
- 현장에서 사진을 찍고
- 짧은 메모를 붙이고
- 상태를 표시하고
- 외부에 공유할 보고서를 만들어야 합니다.

즉, 문제는 “메모 앱”이 아니라 **문서화/증빙/보고 흐름**입니다.

---

## 왜 이 고객이 실제로 존재하는가

### 공개 시장 신호
다음 범주의 앱들은 이미 유저와 매출 구조가 존재합니다.

- field inspection / audit
- field data collection
- work order / maintenance note
- report generation
- PDF export / share

### 내부 벤치마크 근거
- `docs/hq/app-idea-market-benchmark-all-10.md`
  - `Photo-to-report generator for field work`는 실제 유저가 있고, 템플릿 기반이면 1개월 MVP가 가능하다고 정리됨
  - `Frontline safety / compliance inspections`와 `Fleet / equipment inspection and maintenance notes`도 실사용 시장이 확인됨
- `docs/hq/first-app-revenue-market-research.md`
  - 광고 단독보다 `freemium + Pro unlock`이 현실적
  - 범용 유틸리티는 포화지만, 반복 사용 니치 워크플로는 돈이 됨
- `docs/hq/global-first-app-recommendation.md`
  - 글로벌-first, 유저 명확, 벤치마크 존재, 1개월 MVP 가능 조건에 부합

---

## 경쟁 앱 / 대체재

아래는 현재 기준으로 확인한 경쟁 앱과 공식 링크입니다.

### 1) SafetyCulture iAuditor
- 공식 링크: https://safetyculture.com/iauditor
- 무엇을 하는가: 검사, 체크리스트, 현장 보고, 작업 증빙
- 왜 중요하나: 이 시장의 대표적인 상위 플레이어
- 시사점: 사용자는 이미 “사진 + 점검 + 보고서” 흐름에 익숙함

### 2) Fulcrum
- 공식 링크: https://www.fulcrumapp.com/
- 무엇을 하는가: field process / data collection platform
- 왜 중요하나: 점검, 현장 수집, 반복 입력 업무를 다룸
- 시사점: 템플릿 기반 데이터 수집 + 보고 흐름이 실제 수요가 있음

### 3) GoCanvas
- 공식 링크: https://www.gocanvas.com/
- 무엇을 하는가: mobile field work management / workflow digitization
- 왜 중요하나: 현장 업무 디지털화의 대표 앱
- 시사점: 현장 업무용 폼, 리포트, 워크플로가 돈이 되는 구조

### 4) TrueContext (ProntoForms)
- 공식 링크: https://truecontext.com/
- 무엇을 하는가: field service data collection
- 왜 중요하나: 사진/폼/현장 데이터 수집에 강함
- 시사점: 사진 기반 보고서가 단순 소비자 앱이 아니라 B2B/SMB 문제임

### 5) FastField
- 공식 링크: https://www.fastfieldforms.com/
- 무엇을 하는가: mobile data collection and analytics
- 왜 중요하나: 현장 데이터 수집과 리포팅을 함께 다룸
- 시사점: “입력 → 정리 → 내보내기” 흐름이 핵심

### 6) Fleetio
- 공식 링크: https://www.fleetio.com/
- 무엇을 하는가: fleet / maintenance operations
- 왜 중요하나: 장비/차량 점검, 유지보수 이력 관리
- 시사점: 사진·점검·이력은 반복 사용 가치가 강함

### 7) Whip Around
- 공식 링크: https://whiparound.com/
- 무엇을 하는가: fleet management / inspection workflow
- 왜 중요하나: 검사, 유지보수, 보고 루프가 명확
- 시사점: 반복 점검 업무는 구독형과 잘 맞음

### 8) CamScanner / Adobe Scan 같은 스캐너 앱
- CamScanner: https://www.camscanner.com/
- Adobe Scan: https://www.adobe.com/acrobat/mobile/scanner-app.html
- 왜 중요하나: “문서화”에 대한 사용자 기대치가 이미 높음
- 시사점: 우리가 가야 할 건 스캐너 복제본이 아니라 **현장 보고 문서화**

---

## 시장 해석

### 1) 고객은 있다
있습니다. 다만 그 고객은 일반 소비자가 아니라:
- 현장 업무를 하는 사람
- 반복 점검을 하는 사람
- 사진을 증빙으로 남겨야 하는 사람
- PDF/공유 가능한 보고서를 자주 만드는 사람
입니다.

### 2) 경쟁도 있다
매우 강합니다. 그래서 **범용 앱**이면 지기 쉽습니다.

### 3) 그래서 좁혀야 한다
우리가 잡아야 하는 건 “모든 보고서”가 아니라:
- 사진 추가
- 짧은 메모
- 상태 태그
- 템플릿 2~3개
- PDF 내보내기
로 끝나는 좁은 흐름입니다.

### 4) 고객 가치가 분명하다
사용자는 “멋진 앱”을 원하지 않고,
- 빨리 기록하고
- 빨리 보고서를 만들고
- 빨리 공유하고
- 다시 현장으로 돌아가고
싶어합니다.

---

## 리스크
- 너무 범용으로 가면 경쟁 앱에 밀림
- OCR / AI 요약을 앞세우면 범위가 커짐
- 협업 / 권한 / 동기화가 붙으면 1개월 MVP를 넘김
- 스캐너 앱과 정면충돌하면 차별화가 어려움

---

## 추천 방향
**최종 추천:**
> 현장 사진 + 짧은 메모 + 상태 태그 + 템플릿 기반 PDF 보고서 앱

**이유:**
- 실제 고객이 있다
- 경쟁이 존재한다
- 반복 사용 가치가 있다
- 1개월 MVP로 자를 수 있다
- 글로벌-first가 가능하다

---

## 관련 문서
- `docs/hq/first-app-revenue-market-research.md`
- `docs/hq/first-app-revenue-playbook-review.md`
- `docs/hq/first-app-revenue-playbook-top-5.md`
- `docs/hq/first-app-revenue-niche-3.md`
- `docs/hq/global-first-app-recommendation.md`
- `docs/hq/first-app-revenue-scope-fixed.md`
- `docs/hq/first-app-revenue-implementation-tickets.md`
- `docs/hq/first-app-revenue-competitor-comparison.md`
- `docs/hq/first-app-revenue-repeated-complaints.md`
- `docs/hq/first-app-revenue-benchmark-summary.md`

## 다음 액션
1. 경쟁 앱별 첫 3개 화면을 더 자세히 비교한다.
2. 실제 사용자 리뷰에서 반복 불만만 추린다.
3. MVP를 더 좁은 첫 시장 1개로 고정한다.
