# Discord Channel Topology for TemperStone HQ

This is the recommended Discord partition for operating Hermes as a TemperStone-style business-development OS.

## Operating principle

- **Discord is the intake surface.**
- **Hermes HQ is the source of truth.**
- **Threads are the working unit.**
- **Decisions, reviews, and metrics live in HQ artifacts, not in ad-hoc chat.**

Prefer a small number of purpose-specific channels instead of one noisy general-purpose channel.

## Recommended channel map

| Channel | Purpose | Bot behavior | Thread policy |
| --- | --- | --- | --- |
| `#bd-intake` | New opportunities, raw requests, unstructured ideas | Bot may respond freely and should auto-thread | Auto-thread on by default |
| `#bd-triage` | Classify, scope, and convert intake into an initiative | Mention-gated by default | Auto-thread on |
| `#bd-review` | Review, rework, and evidence gathering | Mention-gated by default | Auto-thread on |
| `#bd-decisions` | Final approvals, rework calls, parking, archives | Minimal bot chatter; keep conclusions concise | No thread by default |
| `#bd-metrics` | Status, latency, throughput, and review-cycle tracking | Mention-gated or summary-only | No thread by default |
| `#hq-ops` | Hermes config, routing, bugs, and operational issues | Mention-gated by default | No thread by default |

## Channel topic writing rule

Use channel topics as short operating contracts, not as generic descriptions.

Good channel topics should say:
- what belongs here
- what should not belong here
- what outcome Hermes should help produce

Avoid topics that only name a platform or department without saying how the channel is used.

## What each channel should contain

### `#bd-intake`
Use this for:
- new leads
- product ideas
- customer requests
- “can we do this?” messages
- raw notes that need triage

Do not use this channel for final decisions.

### `#bd-triage`
Use this for:
- turning raw input into an initiative card
- clarifying the target customer
- identifying the value proposition
- deciding whether the item belongs in review

This is where Hermes should help structure the work.

### `#bd-review`
Use this for:
- reviewing an initiative against the contract
- collecting missing evidence
- asking for revisions
- re-running the review loop after rework

All rework should also write a new decision-log entry.

### `#bd-decisions`
Use this for:
- approved
- rework
- blocked
- archived
- scope changes

This channel should stay compact and factual. It should read like an operational log, not a discussion board.

### `#bd-metrics`
Use this for:
- throughput
- latency
- review cycles
- bottlenecks
- channel health snapshots

This channel exists to make the system visible, not to replace the decision log.

### `#hq-ops`
Use this for:
- routing problems
- config changes
- automation issues
- channel policy updates
- platform bugs

Keep HQ operations separate from BD work.

## Recommended Hermes behavior

### Intake
- Allow intake in `#bd-intake`
- Auto-create threads for new items
- Mirror the first message into HQ artifacts

### Triage and review
- Keep `#bd-triage` and `#bd-review` mention-gated unless explicitly allowed
- Use threads for each initiative so the working context stays isolated
- Attach channel-specific skills if needed

### Decisions and metrics
- Keep `#bd-decisions` and `#bd-metrics` mostly summary-only
- Prefer short, structured posts
- Avoid long back-and-forth in those channels

## Suggested config shape

```yaml
discord:
bootstrap_guild_id: "YOUR_GUILD_ID"
bootstrap_channels:
- name: "01-전략"
      topic: |
        TemperStone HQ의 전략 입구.
        이 채널은 큰 방향을 정하고, 무엇이 중요한지 우선순위를 고르며, 해야 할 일과 하지 않을 일을 가르고,
        새 요청을 어디로 보낼지 판단하는 곳이다.

        여기서는 결론을 빠르게 내리는 것이 핵심이다.
        방향, 범위, 타이밍, 리스크, 기대효과, 다음 액션을 짧고 명확하게 정리한다.

        세부 실행 계획, 제품 설계, 콘텐츠 초안, 운영 디버깅, 재무 정산, 회고는 각 전용 채널로 넘긴다.
        질문은 ‘이걸 할까?’, ‘지금 이게 맞나?’, ‘먼저 할 게 뭔가?’, ‘어디로 보내야 하나?’에 맞춘다.
- name: "02-개인사업자-운영"
topic: "개인사업자 운영, 행정, 반복 프로세스, 오너 결정을 다룬다."
- name: "02-제품"
topic: "제품 범위, 로드맵, 요구사항, 우선순위, 리뷰를 다룬다."
- name: "03-콘텐츠"
topic: "콘텐츠 기획, 초안, 발행, 피드백, 성과를 다룬다."
    - name: "04-채널"
      topic: |
        채널 전략, 계정 구조, 배포/전환 설계 전용 채널.

        YouTube·Instagram·TikTok·X·뉴스레터·앱·SaaS처럼 외부 유입과 확산이 일어나는 접점을 여기서 설계한다.

        이 채널에서는 다음을 정한다.
        1) 어떤 채널을 열지/닫을지
        2) 개인·브랜드·실험 계정을 어떻게 나눌지
        3) 각 채널의 역할이 유입·신뢰·전환·수익화 중 무엇인지
        4) 어떤 콘텐츠/오퍼가 어떤 채널에서 작동하는지
        5) 운영 정책·권한·봇·라우팅·토픽 설정을 어떻게 둘지

        제작 초안이나 원고 자체는 `03-콘텐츠`로, 실행 결과와 운영 이슈는 `05-운영`으로 넘긴다.
        목표는 채널별로 ‘무엇을 올릴까’가 아니라 ‘어떤 구조로 유입·전환·확산을 만들까’를 결정하는 것이다.
        최종 산출물은 여기서 만들지 않고, 다른 채널로 넘길 판단 기준만 남긴다.

    - name: "05-운영"
      topic: "자동화, 서비스 상태, 워크플로우, 장애/경보, 운영 라우팅을 다룬다. 이 채널에서는 문제가 재발하지 않도록 원인→조치→검증→재발방지 순서로 정리한다."
      activities:
        - "자동화 규칙을 추가하거나 고친다"
        - "운영 이슈와 상태를 기록한다"
        - "반복 작업의 개선안을 정리한다"

    - name: "06-재무"
      topic: |
        재무 전용.
        이 채널은 현금흐름, 매출/비용, 정산, 회계, 세금, 예산, 마진, 수익성을 다룬다.
        돈의 흐름과 비용 구조를 숫자로 정리하고, 판단 근거를 함께 남긴다.
        기록할 때는 금액·기간·대상·사유를 같이 적는다.
        비용 절감, 투자, 지출 우선순위, 정산 상태, 세무/증빙 누락을 점검한다.
        다른 축의 토론은 여기로 끌고 오지 말고, 재무에 영향을 주는 지점만 남긴다.
        결론은 짧게, 근거는 구체적으로, 다음 액션은 명시적으로 적는다.
- name: "07-회고"
topic: "Repository/workflow retrospectives. Use this lane only for completed work, operational incidents, and decision review. Summarize what happened, why the decision was made, what the outcome was, what surprised us, what should change next, and what operating rule should be updated. Do not start new work here; send new planning, scope expansion, or execution breakdown to the appropriate channel."
- name: "08-브랜딩"
topic: "Hermes / TemperStone HQ의 브랜딩, 톤, 네이밍, 소개 문구, 대외 인상을 정리하는 채널. 여기서는 말투와 표현의 기준을 세우고, 내부용 표현과 외부용 표현을 구분하며, 코드/운영/재무는 다른 채널로 보낸다."
- name: "09-아카이브"
topic: "완료·종료된 항목과 참고용 이력을 보관한다."
allowed_channels:
- "01-전략"
- "02-개인사업자-운영"
- "02-제품"
- "03-콘텐츠"
- "04-채널"
- "05-운영"
- "06-재무"
- "07-회고"
- "08-브랜딩"
- "09-아카이브"
free_response_channels:
- "01-전략"
- "02-개인사업자-운영"
- "02-제품"
- "03-콘텐츠"
- "04-채널"
- "05-운영"
- "06-재무"
- "07-회고"
- "08-브랜딩"
- "09-아카이브"
no_thread_channels:
- "01-전략"
- "04-채널"
- "06-재무"
- "07-회고"
- "09-아카이브"
auto_thread: true
require_mention: false
channel_skill_bindings:
- id: "YOUR_INTAKE_CHANNEL_ID"
skills: ["bd-intake"]
```

### Bootstrap behavior

When `bootstrap_channels` is set and the bot has `Manage Channels`, Hermes will create any missing channels on startup and leave existing ones untouched. That lets you define the workspace once and let the bot finish the setup for you.

After the channels exist, fill in:
- `docs/hq/discord-channel-id-mapping.template.yaml`
- `docs/hq/discord-channel-policy.yaml`
- `docs/hq/discord-channel-topics.yaml`

Channel names are accepted directly in policy config, so you can operate by name first and add numeric IDs later if you want stricter routing.

## Bot permissions required

For the bootstrap flow, the bot should have the minimum permissions needed to create and route channels:

- View Channels
- Send Messages
- Read Message History
- Create Public Threads
- Send Messages in Threads
- Manage Channels

If you only want Hermes to read/respond in existing channels and never create new ones, you can skip `Manage Channels` and leave `bootstrap_channels` unset.

## If the bot already exists and you want to add permissions

1. Open the **Discord Developer Portal**.
2. Select your application.
3. Go to **OAuth2 → URL Generator**.
4. Under **Scopes**, select `bot`.
5. Under **Bot Permissions**, check the permissions you want to add.
6. Copy the generated invite URL.
7. Re-invite the bot with that URL, or use the new URL for a fresh server install.

If the bot is already in the server, the cleanest path is usually:
- update the invite URL with the new permission set
- kick and re-invite the bot, or
- change the bot role permissions in the server if your setup uses role-based permissions

For channel bootstrap specifically, `Manage Channels` is the key permission.

## Operational rule of thumb

If a message is about **starting** work, it belongs in intake.
If it is about **classifying** work, it belongs in triage.
If it is about **changing** work, it belongs in review.
If it is about **closing** work, it belongs in decisions.
If it is about **measuring** work, it belongs in metrics.
If it is about the system itself, it belongs in HQ ops.
