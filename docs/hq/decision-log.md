# Decision Log

This log is append-only.

## Purpose

Record every important BD routing, override, approval, rework, and archive decision so Hermes HQ can reconstruct why something happened.

## Required fields

- `timestamp`
- `initiative_id`
- `decision`
- `actor`
- `rationale`
- `source`
- `follow_up`

## Rules

- Never edit past entries in place.
- Never delete entries to hide history.
- If a decision changes, add a new entry that references the earlier one.
- Keep the entry small and factual.

## Example entry

```yaml
- timestamp: "2026-04-13T22:35:00+09:00"
  initiative_id: "bd-ai-trend-ray"
  decision: approved
  actor: "Hermes"
  rationale: "Fits current BD focus and has clear channel fit"
  source: "Discord thread"
  follow_up: "Create review checkpoint and metrics baseline"
```
