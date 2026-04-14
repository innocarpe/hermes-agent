# Hermes Review Loop

This is the operating loop for BD decisions.

## States

- `pending`: item created but not yet examined
- `reviewing`: Hermes or a reviewer is actively checking the item
- `approved`: ready to move forward
- `rework`: changes are required before approval
- `blocked`: external dependency or missing signal prevents progress
- `archived`: completed or intentionally parked

## Loop

1. Intake the BD item.
2. Attach the current decision log context.
3. Review against the initiative card and metrics baseline.
4. Emit one of the states above.
5. If `rework`, write a new decision log entry and re-run review.
6. If `approved`, hand off to the next execution stage.

## Reviewer responsibilities

- Keep the review factual.
- Point to the exact missing field or contradiction.
- Do not silently fix the item during review.
- If a decision changes, record it in the decision log first.

## Output format

```yaml
state: reviewing
initiative_id: ""
summary: ""
action_required: ""
```
