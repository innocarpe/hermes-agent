# TemperStone HQ Discord Channel Role Map

This document is the practical operating map for the current Discord workspace.

## Operating rule

- **Use channel names first.** Numeric IDs are optional.
- **Discord is the intake and coordination surface.**
- **Hermes HQ is the source of truth.**
- **Threads are the working unit** unless a channel is explicitly marked `no_thread`.

## Final channel roles

| Channel | Role | Topic / description | Mention policy | Thread policy | Primary use |
| --- | --- | --- | --- | --- | --- |
| `01-전략` | Strategy intake + direction | High-level direction, priority setting, major bets | `free_response` | `no_thread` | High-level direction, priority setting, major bets |
| `02-개인사업자-운영` | Owner operations | Business admin, process, and owner decisions | `free_response` | `auto_thread` | Business admin, process, owner decisions |
| `02-제품` | Product work | Product scope, roadmap, delivery, and review | `mention_gated` | `auto_thread` | Product scope, roadmap, delivery, review |
| `03-콘텐츠` | Content work | Drafts, publishing, feedback, and content ops | `free_response` | `auto_thread` | Drafts, publishing, feedback, and content ops |
| `04-채널` | Channel operations | Discord, Telegram, and platform operations | `mention_gated` | `no_thread` | Discord/Telegram/platform ops, channel structure |
| `05-운영` | Operations | Automation, service health, workflows, and routing | `free_response` | `auto_thread` | Automation, service health, workflows, and routing |
| `06-재무` | Finance | Cashflow, accounting, and finance decisions | `mention_gated` | `no_thread` | Cashflow, accounting, and finance decisions |
| `07-회고` | Review / retrospective | Retrospectives, lessons learned, and system review | `free_response` | `no_thread` | Retrospectives, lessons learned, and system review |
| `08-브랜딩` | Branding | Tone, naming, public presence, and presentation | `mention_gated` | `auto_thread` | Tone, naming, public presence, and presentation |
| `09-아카이브` | Archive | Closed items, historical record, and resolved threads | `read_only` | `no_thread` | Closed items, historical record, and resolved threads |

## Current recommended routing controls

### Allowed channels
Use names directly in `allowed_channels`:

- `01-전략`
- `02-개인사업자-운영`
- `02-제품`
- `03-콘텐츠`
- `04-채널`
- `05-운영`
- `06-재무`
- `07-회고`
- `08-브랜딩`

### Free-response channels
Use names directly in `free_response_channels`:

- `01-전략`
- `02-개인사업자-운영`
- `03-콘텐츠`
- `05-운영`
- `07-회고`

### No-thread channels
Use names directly in `no_thread_channels`:

- `01-전략`
- `04-채널`
- `06-재무`
- `07-회고`
- `09-아카이브`

## Skill binding guidance

Recommended baseline bindings:

- `01-전략` → `bd-intake`
- `02-제품` → `bd-review`
- `04-채널` → `hq-ops`
- `05-운영` → `hq-ops`
- `06-재무` → `finance-review`
- `07-회고` → `review-loop`
- `08-브랜딩` → `brand-review`

If a new channel is added later, choose the binding by the work it represents, not by the department label.

## Expansion rule for future channels

When you add a new channel:

1. Give it a **full, explicit name**.
2. Decide which existing axis it belongs to.
3. Prefer the same naming style as the current set.
4. Add it to `allowed_channels` only if Hermes should respond there.
5. Add it to `free_response_channels` only if it should not require mention.
6. Add it to `no_thread_channels` only if thread isolation is not wanted.
7. Add `channel_skill_bindings` only when the channel should trigger a specialized workflow.

## Practical default behavior

- New work begins in `01-전략`, `02-개인사업자-운영`, `03-콘텐츠`, or `05-운영`.
- Structural/system work goes to `04-채널`.
- Financial work goes to `06-재무`.
- Review and closure go to `07-회고` and `09-아카이브`.

## Notes

This map is designed to be stable even as the workspace grows. If the workspace expands, keep the naming explicit and extend by axis instead of by department shorthand.
