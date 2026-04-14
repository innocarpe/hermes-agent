# BD Pipeline Contract

This document defines the shared shape for a BD item inside Hermes.

## Core fields

- `name`: human-readable initiative name
- `stage`: current lifecycle stage (`explore`, `build`, `review`, `pause`, `archive`)
- `target_customer`: who the initiative is for
- `value_proposition`: the specific value being delivered
- `decision_state`: current operating decision (`pending`, `approved`, `rework`, `blocked`, `archived`)
- `metrics`: the small set of signals used to judge progress

## Operating rule

Every BD item must be representable as a single initiative card and must be able to move through the same pipeline without custom handling.
