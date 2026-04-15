# First App Revenue Playbook — Screen Spec

## 목적
와이어프레임을 구현 가능한 화면 규격으로 바꾼다.

## 공통 규칙
- 각 화면은 primary action 1개만 강하게 보여준다
- secondary action은 1개 이하로 제한한다
- loading / empty / error 상태를 고려한다
- 문구는 짧고 업무 맥락 중심이어야 한다
- 각 화면은 사용자의 **반복 비용을 줄이는 순서**로 배치한다
- 유료 기능이 있으면, 어떤 사용자가 왜 돈을 내는지 화면 맥락에 드러나야 한다
- 자세한 판정 기준은 `docs/hq/first-app-strategy-principles.md`를 따른다.

---

## 1) Home / First Screen

**Goal:** 새 점검 보고서를 바로 시작하게 만든다.

**Primary action:** `+ 새 점검 보고서 시작`

**Secondary actions:**
- 최근 보고서 열기
- 템플릿 둘러보기

**숨길 것:**
- OCR
- AI 요약
- 설정
- 계정/동기화

**States:**
- empty: 최근 보고서 없음
- loading: 최근 보고서 로딩 중
- error: 최근 기록 불러오기 실패

---

## 2) Photo Add Screen

**Goal:** 보고서 재료가 되는 사진을 빠르게 넣는다.

**Primary action:** `카메라로 찍기`

**Secondary action:** `갤러리에서 선택`

**핵심 요소:**
- 사진 썸네일 리스트
- 삭제 버튼
- 다음 단계로 이동 버튼

**States:**
- empty: 아직 사진 없음
- loading: 카메라/갤러리 접근 준비 중
- error: 저장 권한 없음 / 사진 추가 실패

---

## 3) Photo Note Input Screen

**Goal:** 각 사진에 짧은 메모와 상태를 붙인다.

**Primary action:** `다음`

**Secondary action:** `이전`

**핵심 요소:**
- 사진 미리보기
- 한 줄 메모 입력
- 상태 태그 3개 이하

**States:**
- empty: 메모 비어 있음
- loading: 사진 전환 중
- error: 입력 저장 실패

---

## 4) Template Selection Screen

**Goal:** 보고서 형식을 빠르게 고르게 한다.

**Primary action:** `계속`

**Secondary action:** `미리보기`

**템플릿 후보:**
- 간단 보고서
- 점검 보고서
- 피해 기록

**States:**
- empty: 기본 템플릿 1개 자동 선택
- loading: 템플릿 미리보기 생성 중
- error: 템플릿 불러오기 실패

---

## 5) Preview / PDF Screen

**Goal:** 결과를 최종 문서처럼 보여주고 내보내게 한다.

**Primary action:** `PDF 내보내기`

**Secondary action:** `공유하기`

**핵심 요소:**
- 제목
- 날짜
- 상태 요약
- 사진 + 메모
- 템플릿 정보

**States:**
- loading: PDF 생성 중
- empty: 보고서 항목 부족
- error: PDF 생성 실패 / 저장 실패

---

## 6) Share / Complete Screen

**Goal:** 사용자가 결과를 실제로 배포했음을 확인한다.

**Primary action:** `완료`

**Secondary action:** `새 보고서 만들기`

**핵심 요소:**
- 공유 완료 메시지
- PDF 파일 링크
- 최근 보고서로 복귀

**States:**
- loading: 공유 시트 표시 중
- error: 공유 실패

---

## Implementation priorities
1. Home
2. Photo Add
3. Photo Note Input
4. Template Selection
5. Preview / PDF
6. Share / Complete

## HQ note
이 앱의 UX는 화려함보다 **흐름의 짧음**과 **결과물의 신뢰감**이 더 중요하다.
