# Common Metrics Schema

This layer standardizes the telemetry emitted by BD work, decision handling, and review loops.

## Shared dimensions

- `initiative_id`
- `stage`
- `decision_count`
- `review_cycles`
- `latency_ms`
- `status`

## Principles

- Keep the schema small and stable.
- Prefer the same metric names across all Hermes HQ surfaces.
- Emit metrics at boundaries, not inside every tiny helper.
- If a metric changes meaning, version the schema instead of reusing the name ambiguously.

## Example payload

```json
{
  "initiative_id": "bd-ai-trend-ray",
  "stage": "review",
  "decision_count": 3,
  "review_cycles": 2,
  "latency_ms": 1842,
  "status": "approved"
}
```
