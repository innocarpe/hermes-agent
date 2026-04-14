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
      topic: "High-level direction, priority setting, major bets"
    - name: "02-개인사업자-운영"
      topic: "Business admin, process, and owner decisions"
    - name: "02-제품"
      topic: "Product scope, roadmap, delivery, and review"
    - name: "03-콘텐츠"
      topic: "Drafts, publishing, feedback, and content ops"
    - name: "04-채널"
      topic: "Discord, Telegram, and platform operations"
    - name: "05-운영"
      topic: "Automation, service health, workflows, and routing"
    - name: "06-재무"
      topic: "Cashflow, accounting, and finance decisions"
    - name: "07-회고"
      topic: "Retrospectives, lessons learned, and system review"
    - name: "08-브랜딩"
      topic: "Tone, naming, public presence, and presentation"
    - name: "09-아카이브"
      topic: "Closed items, historical record, and resolved threads"
  allowed_channels:
    - "YOUR_ALLOWED_CHANNEL_IDS_OR_NAMES"
  free_response_channels:
    - "YOUR_FREE_RESPONSE_CHANNEL_ID_OR_NAME"
  no_thread_channels:
    - "YOUR_NO_THREAD_CHANNEL_IDS_OR_NAMES"
  auto_thread: true
  require_mention: true
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
