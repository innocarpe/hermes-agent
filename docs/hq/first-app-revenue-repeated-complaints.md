# First App Revenue — Repeated Complaint Patterns

## 목적
경쟁 앱/대체재의 공개 페이지와 앱 설명에서 반복되는 불만 신호를 추려서, 우리 MVP가 피해야 할 범위를 정한다.

## 스코프 주의
이 문서는 완전한 전수 리뷰 분석이 아니라, **공개 페이지와 앱 설명에서 반복적으로 드러나는 문제 신호**를 정리한 것이다. 그래서 아래 항목은 "사용자 불만"과 "시장에 이미 널리 알려진 불편"을 함께 본다.

---

## 반복 불만 패턴 1: 종이/스프레드시트/수기 작업이 너무 느리다
### 신호
- SafetyCulture: checklist forms, inspections, reports
- Fulcrum: inefficient field data collection software, process management
- GoCanvas: no more chasing paperwork, scrambling for details
- TrueContext: no more paperwork, mobile forms

### 해석
사용자는 본질적으로
- 종이 작성
- 사진 따로 저장
- 메모 따로 정리
- 나중에 보고서 편집
을 하기 싫어한다.

### 우리에게 주는 의미
입력에서 결과까지를 **한 번에 끝내는 짧은 흐름**이 중요하다.

---

## 반복 불만 패턴 2: 폼/워크플로가 너무 복잡하다
### 신호
- SafetyCulture: over-complicated forms를 우회하기 위해 observations/hazards를 빠르게 보고
- GoCanvas: drag-and-drop templates, simple to use
- Fulcrum: old/inefficient tools 대신 field-first 플랫폼 강조
- TrueContext: guided workflows, structured capture

### 해석
많은 현장 앱은 강력하지만, 초기 설정과 사용법이 복잡하다.

### 우리에게 주는 의미
- 템플릿 2~3개만 시작
- 복잡한 폼 빌더는 v1에서 제외
- 사용자가 설명 없이 바로 쓸 수 있어야 한다

---

## 반복 불만 패턴 3: 사진과 메모가 흩어진다
### 신호
- CompanyCam: 중요한 사진이나 문서를 잃어버릴 일이 없다
- SafetyCulture: photos/video evidence, reports, assets
- GoCanvas: image/video capture, project management
- Fulcrum: field data collection + sync

### 해석
사진이 여러 군데 흩어지고, 나중에 맥락을 잃는 문제가 크다.

### 우리에게 주는 의미
우리 앱은 **사진 + 1줄 메모 + 상태 태그**를 기본 단위로 잡아야 한다.

---

## 반복 불만 패턴 4: 현장과 사무실 사이의 handoff가 느리다
### 신호
- Fulcrum: field and office systems 연결
- GoCanvas: connecting office and field
- TrueContext: results shared automatically with back office systems
- SafetyCulture: share reports and collaborate across teams

### 해석
현장 데이터가 사무실에 전달되는 과정이 느리고, 다시 수정되는 일이 많다.

### 우리에게 주는 의미
즉시 공유 가능한 **PDF 결과물**이 핵심이다.

---

## 반복 불만 패턴 5: 기존 도구는 너무 무겁거나 엔터프라이즈다
### 신호
- SafetyCulture: inspections + tasks + comms + analytics + assets + training
- Fulcrum: GIS, integrations, enterprise security
- GoCanvas: all-in-one digital solution
- TrueContext: workflow platform, integrations, analytics, enterprise security
- CompanyCam: photo-first이지만 팀/통합/페이지/AI까지 확장

### 해석
대부분의 경쟁사는 매우 강하지만, 기능이 많아질수록 가벼운 사용성이 사라진다.

### 우리에게 주는 의미
우리는 플랫폼이 아니라 **좁은 워크플로 도구**여야 한다.

---

## 반복 불만 패턴 6: 보고서를 예쁘고 빠르게 만드는 게 어렵다
### 신호
- SafetyCulture: professional reports
- CompanyCam: photo report builder
- GoCanvas: forms + analytics
- TrueContext: reporting and analysis

### 해석
결국 사용자가 원하는 건 "데이터 저장"이 아니라 **쓸 만한 보고서**다.

### 우리에게 주는 의미
미리보기가 결과물처럼 보여야 하고, PDF export가 1차 액션이어야 한다.

---

## 반복 불만 패턴 7: 오프라인/현장 환경이 핵심이다
### 신호
- SafetyCulture: offline inspections
- Fulcrum: offline maps and forms
- GoCanvas: offline access
- TrueContext: field work with mobile device access

### 해석
현장 앱은 네트워크가 불안정해도 돌아가야 한다.

### 우리에게 주는 의미
오프라인/weak network 상태를 MVP에서 무시하면 안 된다.

---

## 반복 불만 패턴 8: 사용자는 "설치 후 바로 이해"를 원한다
### 신호
- 각 앱의 hero 메시지들이 모두 짧고 직접적임
- inspect / collect / digitize / share / report 같은 즉시 이해 가능한 동사 사용

### 해석
사용자는 복잡한 설명보다 작업 시작점을 찾고 있다.

### 우리에게 주는 의미
첫 화면은 "새 보고서 만들기" 같은 직접 행동이어야 한다.

---

## 요약: 이번 주에 유지할 불만 클러스터
1. 종이/수기/스프레드시트가 느리다
2. 폼이 복잡하다
3. 사진과 메모가 흩어진다
4. 현장→사무실 handoff가 느리다
5. 엔터프라이즈 플랫폼이 무겁다
6. 예쁜 보고서 만들기가 어렵다
7. 오프라인이 중요하다
8. 설치 후 바로 이해돼야 한다

## 우리 제품에 대한 적용
우리 앱은 아래 조건을 만족해야 한다.
- 사진 입력이 가장 빠를 것
- 메모는 1줄일 것
- 템플릿은 2~3개만 둘 것
- 미리보기는 결과물처럼 보일 것
- PDF export가 핵심일 것
- 오프라인 실패를 대비할 것

## 다음 액션
이 불만 패턴을 기준으로
- 첫 시장 1개를 고정하고
- 그 시장만 더 깊게 조사한다.
