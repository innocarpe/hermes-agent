# BD Pipeline Foundation Implementation Plan

> **For Hermes:** Execute this plan one task at a time. Use the BD pipeline first, then add the decision log, then the Hermes review loop, and only after that unify the common metrics layer.

**Goal:** Turn BD work into a first-class, tracked pipeline inside Hermes so that every initiative has the same intake, routing, decision, review, and measurement path.

**Architecture:**
A BD item enters through a single normalized event schema, gets routed into an initiative registry, writes append-only decisions to a log, and emits metrics through a shared layer. The early-stage shape should stay shallow: one canonical schema, one persistence model, one review loop, and one metrics adapter. Hermes remains the orchestrator; the portfolio/BD layer is just a structured operating surface.

**Tech Stack:** Python, repository-local markdown/YAML templates, existing Hermes session/config utilities, pytest.

---

## Implementation Order

### Task 1: Define the BD pipeline contract and registry shape

**Objective:** Establish the canonical data model for a BD item so every later subsystem has a shared language.

**Files:**
- Create: `docs/hq/bd-pipeline-contract.md`
- Create: `docs/hq/templates/initiative-card.md`
- Create: `tests/docs/test_bdpipeline_contract.py`

**Step 1: Write failing test**

```python
from pathlib import Path


def test_initiative_card_template_exists():
    assert Path("docs/hq/templates/initiative-card.md").exists()


def test_bd_pipeline_contract_mentions_core_fields():
    text = Path("docs/hq/bd-pipeline-contract.md").read_text()
    for field in ["name", "stage", "target_customer", "value_proposition", "decision_state", "metrics"]:
        assert field in text
```

**Step 2: Run test to verify failure**

Run: `pytest tests/docs/test_bdpipeline_contract.py -v`
Expected: FAIL — files do not exist yet.

**Step 3: Write minimal implementation**

Create a concise contract document that defines the shared fields and a reusable initiative card template.

**Step 4: Run test to verify pass**

Run: `pytest tests/docs/test_bdpipeline_contract.py -v`
Expected: PASS

---

### Task 2: Add the append-only decision log

**Objective:** Make every major BD routing choice durable and auditable.

**Files:**
- Create: `docs/hq/decision-log.md`
- Create: `tests/docs/test_decision_log.md`

**Step 1: Write failing test**

```python
from pathlib import Path


def test_decision_log_is_append_only_by_policy():
    text = Path("docs/hq/decision-log.md").read_text()
    assert "append-only" in text
    assert "timestamp" in text
    assert "decision" in text
```

**Step 2: Run test to verify failure**

Run: `pytest tests/docs/test_decision_log.py -v`
Expected: FAIL — document missing.

**Step 3: Write minimal implementation**

Document the log format, required metadata, and the rule that decisions are never overwritten.

**Step 4: Run test to verify pass**

Run: `pytest tests/docs/test_decision_log.py -v`
Expected: PASS

---

### Task 3: Add the Hermes review loop

**Objective:** Define how BD items are reviewed, approved, rejected, or sent back for revision.

**Files:**
- Create: `docs/hq/review-loop.md`
- Create: `tests/docs/test_review_loop.md`

**Step 1: Write failing test**

```python
from pathlib import Path


def test_review_loop_mentions_states():
    text = Path("docs/hq/review-loop.md").read_text()
    for state in ["pending", "reviewing", "approved", "rework", "blocked"]:
        assert state in text
```

**Step 2: Run test to verify failure**

Run: `pytest tests/docs/test_review_loop.py -v`
Expected: FAIL — document missing.

**Step 3: Write minimal implementation**

Document the lifecycle, the reviewer role, and the handoff contract back to Hermes HQ.

**Step 4: Run test to verify pass**

Run: `pytest tests/docs/test_review_loop.py -v`
Expected: PASS

---

### Task 4: Add the common metrics layer

**Objective:** Standardize the telemetry emitted by BD, decision, and review workflows.

**Files:**
- Create: `docs/hq/metrics-schema.md`
- Create: `tests/docs/test_metrics_schema.py`

**Step 1: Write failing test**

```python
from pathlib import Path


def test_metrics_schema_mentions_shared_dimensions():
    text = Path("docs/hq/metrics-schema.md").read_text()
    for key in ["initiative_id", "stage", "decision_count", "review_cycles", "latency_ms"]:
        assert key in text
```

**Step 2: Run test to verify failure**

Run: `pytest tests/docs/test_metrics_schema.py -v`
Expected: FAIL — document missing.

**Step 3: Write minimal implementation**

Define the shared dimensions and note which future components emit them.

**Step 4: Run test to verify pass**

Run: `pytest tests/docs/test_metrics_schema.py -v`
Expected: PASS

---

## Verification After All Tasks

Run:

```bash
pytest tests/docs -q
```

Expected: all documentation-contract tests pass.

## Notes

- Keep this layer intentionally shallow at first.
- Do not split into separate systems per initiative yet.
- Do not add metrics before the contract and review states are stable.
- This plan is the first step of the larger Hermes infra sequence.
