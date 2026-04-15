# First App Revenue Playbook — Market Research Notes

> 참고: 이 문서는 `docs/hq/first-app-strategy-principles.md`와 `docs/hq/first-app-doc-map.md`를 기준으로 읽는 보조 문서다.

## 질문
- 실제로 돈을 벌 수 있는가?
- 실제 유저가 있는가?
- Android / iOS 중 어디가 더 맞는가?
- 광고만으로 가능한가, 아니면 다른 수익화가 필요한가?

## 결론
- **유저는 있다.** 특히 Android는 전세계 모바일 점유율이 높고, 워크플로/자동화/유틸리티 앱에 실제 수요가 존재한다.
- **하지만 범용 유틸리티는 포화 상태다.**
- **광고 단독 모델은 작은 앱에서 약하다.**
- **가장 현실적인 수익화는 freemium + Pro unlock** 이고, 반복 사용이 있는 니치 앱일수록 유리하다.

---

## 데이터 기반 근거

### 1) Android는 실제로 큰 시장이다
- StatCounter 글로벌 모바일 OS 점유율에서 Android는 대략 70%+ 수준.
- 의미: **도달 가능한 사용자 풀이 매우 크다.**

URL:
- https://gs.statcounter.com/os-market-share/mobile/worldwide

### 2) 니치 워크플로 앱은 실제로 설치 규모가 나온다
공개 Google Play 예시:
- MacroDroid — 10M+ installs
- Tasker — 1M+ installs
- Solid Explorer — 5M+ installs
- Files by Google — 5B+ installs

의미:
- 워크플로/유틸리티 영역 자체가 죽은 시장은 아님.
- 다만 **범용 기능은 이미 강한 선점자**가 많다.

URLs:
- https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid
- https://play.google.com/store/apps/details?id=net.dinglisch.android.tasker
- https://play.google.com/store/apps/details?id=pl.solidexplorer2
- https://play.google.com/store/apps/details?id=com.google.android.apps.nbu.files

### 3) 시장은 매우 크고 경쟁도 강하다
- Appfigures: Google Play는 여전히 multi-million app market.
- 의미: **그냥 유틸리티 하나로는 발견되기 어렵다.**

URL:
- https://appfigures.com/resources/insights/how-many-apps-are-in-the-app-store-and-google-play

### 4) 수익은 소수 앱에 집중된다
- RevenueCat의 subscription benchmark류 자료는 수익 분포가 매우 치우쳐 있음을 보여줌.
- 의미: **대부분의 작은 앱은 크게 못 번다.**

URL:
- https://www.revenuecat.com/state-of-subscription-apps/

### 5) Android vs iOS 경제성
- 일반적으로 Android는 **다운로드/도달**이 유리.
- iOS는 **ARPU / 구독 전환**이 더 유리한 편.
- 의미: 
  - **Android-first = 실험과 도달에 유리**
  - **iOS-first = 유료화 효율에 유리**

URL:
- https://sensortower.com/blog/state-of-mobile-2024

---

## 수익화 벤치마크 해석

### 광고 단독
- 작은 유틸리티 앱은 세션이 짧고 광고 노출이 적어서 약함.
- 배너 eCPM은 많은 지역에서 낮고, impressions/user가 충분하지 않으면 의미 있는 수익이 안 나온다.

### freemium + pro unlock
- 작은 유틸리티/생산성 앱에 가장 무난한 모델.
- 사용자가 즉시 가치를 느끼고, 제한 해제의 이유를 이해하기 쉬움.

### subscription
- 반복 사용, sync, automation, collaboration, AI/processing이 있을 때 유리.
- pure utility인데 가끔 쓰는 앱이라면 subscription보다 lifetime unlock이 더 나을 수 있음.

---

## 현재 전략에 대한 데이터 기반 판정

### 추천되는 방향
- **Android-first specific-job workflow tool**
- 이유: 실제 수요가 있고, Android의 강점(도달성, 저비용 실험, 장치 접근성)을 활용 가능
- 다만 범용 유틸리티보다 **반복 비용이 큰 특정 워크플로**에 좁힌다.
- 수익화는 광고보다 **freemium + Pro unlock** 우선으로 본다.
- 제품 평가 시 **누가 돈을 내는지**를 먼저 적는다.

### 피해야 할 방향
- 범용 계산기
- 범용 클리너
- 광고만 잔뜩 넣은 유틸리티
- 고비용 API 의존 앱
- 포화된 메인스트림 유틸리티 정면승부

---

## 시장 조사 관점 최종 문장
- **유저는 있다.**
- **돈도 벌 수 있다.**
- 하지만 그 돈은 **범용 유틸리티 광고앱**이 아니라,
  **반복 사용되는 니치 워크플로 앱 + freemium/pro unlock**에서 더 현실적이다.

---

## 참고 링크
- StatCounter Android share: https://gs.statcounter.com/os-market-share/mobile/worldwide
- Appfigures app market size: https://appfigures.com/resources/insights/how-many-apps-are-in-the-app-store-and-google-play
- RevenueCat subscription benchmarks: https://www.revenuecat.com/state-of-subscription-apps/
- Sensor Tower State of Mobile 2024: https://sensortower.com/blog/state-of-mobile-2024
- Google Play app examples: see URLs above
