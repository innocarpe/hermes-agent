# TemperStone HQ Discord channel operating map

This document is the practical operating view for the current workspace. It is meant to stay readable and to serve as the default reference when new channels are added later.

## Channel roles

| Channel | Role | Thread policy | Response policy | Suggested skill binding |
| --- | --- | --- | --- | --- |
|| `01-전략` | Strategy, direction setting, and market discovery intake | No thread | Free response | `bd-intake` |
|| `02-개인사업자-운영` | Solo-business operations | Auto-thread | Free response | `bd-intake` |
|| `02-제품` | Product decisions and scope | Auto-thread | Mention-gated | `bd-review` |
|| `03-콘텐츠` | Content planning and production | Auto-thread | Free response | `bd-review` |
|| `04-채널` | Content channel strategy and platform distribution | Auto-thread | Free response | no default binding |
| `05-운영` | Automation and service operations | Auto-thread | Free response | `hq-ops` |
| `06-재무` | Finance and accounting | No thread | Mention-gated | `hq-ops` |
| `07-회고` | Retrospectives, decision review, and improvement actions | No thread | Free response | `review-loop` |
| `08-브랜딩` | Brand, tone, naming, public presence | Auto-thread | Mention-gated | `brand-review` |
| `09-아카이브` | Closed and historical items | No thread | Read-only | none |

## Default policy summary
- **allowed_channels**: all working channels except archive unless you explicitly want archive responses.
- **free_response_channels**: `01-전략`, `02-개인사업자-운영`, `03-콘텐츠`, `04-채널`, `05-운영`, `07-회고`
- **no_thread_channels**: `01-전략`, `06-재무`, `07-회고`, `09-아카이브`
- **channel_skill_bindings**: use channel names first; numeric IDs are optional.

## Operating rule

- Starting work -> intake-style channels
- Structuring work -> product / operations channels
- Changing work -> review-style channels
- Closing work -> decision / archive flow
- Measuring work -> metrics or operations summaries
- Channel system / distribution work -> `04-채널`
- Platform or automation issues -> `05-운영`

## Routing emphasis

- `04-채널` is for channel architecture and routing rules, not draft content.
- `05-운영` is for incident handling, automation, and verification loops, not product or content planning.
- If a request mixes content and channel-system work, split it: content goes to `03-콘텐츠`, structure goes to `04-채널`, runtime issues go to `05-운영`.

## 04-채널 guidance for YouTube/content

- Use `04-채널` when the question is **what position should this channel take**.
- Classify a YouTube niche first as `news`, `analysis`, `how-to`, `expert`, or `archive/repackaging` before naming the channel.
- If a label is crowded, rewrite the position instead of clinging to the label. Example: `AI 뉴스` → `AI 실무/도구/산업 해설`.
- If the topic is high-risk (medical, legal, finance-adjacent, crime), require source quality, disclosure, and review ownership before launch.
- If the benchmark says the market is large but polluted, default to `reframe` or `gate`, not immediate launch.
- End every channel decision with a clear routing outcome: `launch`, `reframe`, `gate`, or `drop`.

## Growth rule

When new channels are added later:
1. Keep the naming convention explicit and non-abbreviated.
2. Decide whether the channel is free-response or mention-gated.
3. Decide whether it should auto-thread.
4. Add a skill binding only if the channel has a stable workflow.
5. Prefer names first; add numeric IDs only if you need strict routing.
