# TemperStone HQ Discord channel operating map

This document is the practical operating view for the current workspace. It is meant to stay readable and to serve as the default reference when new channels are added later.

## Channel roles

| Channel | Role | Thread policy | Response policy | Suggested skill binding |
| --- | --- | --- | --- | --- |
| `01-전략` | Strategy and direction setting | No thread | Free response | `bd-intake` |
| `02-개인사업자-운영` | Solo-business operations | Auto-thread | Free response | `bd-intake` |
| `02-제품` | Product decisions and scope | Auto-thread | Mention-gated | `bd-review` |
| `03-콘텐츠` | Content planning and production | Auto-thread | Free response | `bd-review` |
| `04-채널` | Channel and platform operations | No thread | Mention-gated | `hq-ops` |
| `05-운영` | Automation and service operations | Auto-thread | Free response | `hq-ops` |
| `06-재무` | Finance and accounting | No thread | Mention-gated | `hq-ops` |
| `07-회고` | Retrospectives and lessons learned | No thread | Free response | `review-loop` |
| `08-브랜딩` | Brand, tone, naming, public presence | Auto-thread | Mention-gated | `brand-review` |
| `09-아카이브` | Closed and historical items | No thread | Read-only | none |

## Default policy summary

- **allowed_channels**: all working channels except archive unless you explicitly want archive responses.
- **free_response_channels**: `01-전략`, `02-개인사업자-운영`, `03-콘텐츠`, `05-운영`, `07-회고`
- **no_thread_channels**: `01-전략`, `04-채널`, `06-재무`, `07-회고`, `09-아카이브`
- **channel_skill_bindings**: use channel names first; numeric IDs are optional.

## Operating rule

- Starting work -> intake-style channels
- Structuring work -> product / operations channels
- Changing work -> review-style channels
- Closing work -> decision / archive flow
- Measuring work -> metrics or operations summaries
- System issues -> `04-채널` or `05-운영`

## Growth rule

When new channels are added later:
1. Keep the naming convention explicit and non-abbreviated.
2. Decide whether the channel is free-response or mention-gated.
3. Decide whether it should auto-thread.
4. Add a skill binding only if the channel has a stable workflow.
5. Prefer names first; add numeric IDs only if you need strict routing.
