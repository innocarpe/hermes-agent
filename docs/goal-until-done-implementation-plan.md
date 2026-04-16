# Goal-Until-Done Implementation Plan

> **For Hermes:** implement this plan in small, reversible steps. Verify each step before moving on.

**Goal:** Hermes에 `goal-until-done` 실행 모드를 추가해, 명시된 완료 조건을 만족할 때까지 attempt를 이어가고 blocker를 분류하게 만든다.

**Architecture:** `run_conversation()`은 그대로 두고, 새 controller가 여러 attempt를 orchestration한다. `cli.py`는 entrypoint와 command surface를 제공하고, persistence는 lightweight state store로 시작한다.

**Tech Stack:** Python, `run_agent.py`, `cli.py`, `hermes_cli/commands.py`, optional `cron/scheduler.py` reuse, pytest

---

## Task 1: 목표 상태 저장 위치 고정
**Objective:** goal-run state를 저장할 위치와 구조를 결정한다.

**Files:**
- Create: `agent/goal_until_done.py`
- Create: `tests/test_goal_until_done_state.py`

**Step 1: 상태 모델 정의**
- `GoalContract`
- `AttemptRecord`
- `GoalRunState`

**Step 2: sidecar 저장 함수 추가**
- `save_goal_state()`
- `load_goal_state()`
- base path: `get_hermes_home() / "goals"`

**Step 3: 테스트**
Run:
```bash
python -m pytest tests/test_goal_until_done_state.py -q
```
Expected: state save/load roundtrip pass

## Task 2: attempt outcome classifier 추가
**Objective:** attempt 결과를 completed/retryable/terminal 등으로 분류한다.

**Files:**
- Modify: `agent/goal_until_done.py`
- Create: `tests/test_goal_until_done_classifier.py`

**Step 1: classifier enum/labels 정의**
- `completed`
- `retryable_failure`
- `wait_and_retry`
- `approval_required`
- `terminal_blocker`
- `budget_exhausted`

**Step 2: 입력 신호 정의**
- `run_conversation()` 반환값
- iteration budget exhaustion
- inactivity timeout
- tool permission denial
- explicit done criteria match

**Step 3: 테스트**
Run:
```bash
python -m pytest tests/test_goal_until_done_classifier.py -q
```
Expected: label classification pass

## Task 3: goal loop controller 추가
**Objective:** 여러 attempt를 관리하는 상위 루프를 구현한다.

**Files:**
- Modify: `agent/goal_until_done.py`
- Create: `tests/test_goal_until_done_loop.py`

**Step 1: `run_until_done()` 구현**
입력:
- contract
- attempt callback
- retry policy

출력:
- final state
- final label

**Step 2: backoff/sleep 정책 추가**
- immediate retry
- simple sleep retry
- approval pause

**Step 3: 테스트**
Run:
```bash
python -m pytest tests/test_goal_until_done_loop.py -q
```
Expected: retry/pause/complete flows pass

## Task 4: `AIAgent`와 연결하기
**Objective:** 기존 `run_conversation()`을 변경 최소화로 attempt executor에 연결한다.

**Files:**
- Modify: `run_agent.py`
- Create: `tests/test_run_agent_goal_until_done.py`

**Step 1: thin adapter 추가**
- `AIAgent.run_until_done(...)`
또는 helper로 controller 호출

**Step 2: activity/iteration summary 노출 재사용**
- existing activity summary 재사용
- iteration budget exhaustion signal 연결

**Step 3: 테스트**
Run:
```bash
python -m pytest tests/test_run_agent_goal_until_done.py -q
```
Expected: fake agent attempt orchestration pass

## Task 5: CLI surface 추가
**Objective:** 사용자가 기능을 실제로 켤 수 있게 한다.

**Files:**
- Modify: `hermes_cli/commands.py`
- Modify: `cli.py`
- Create: `tests/cli/test_goal_until_done_command.py`

**Step 1: slash command 정의**
후보:
- `/until-done`
- `/goal-status`
- `/goal-stop`

**Step 2: CLI handler 구현**
- active session에서 contract 생성
- background or foreground 실행 선택

**Step 3: 테스트**
Run:
```bash
python -m pytest tests/cli/test_goal_until_done_command.py -q
```
Expected: command registration and basic dispatch pass

## Task 6: config surface 추가
**Objective:** 기본 정책을 config로 제어한다.

**Files:**
- Modify: `hermes_cli/config.py`
- Modify: `cli.py`
- Create: `tests/test_goal_until_done_config.py`

**Settings:**
- `goal_until_done.enabled`
- `goal_until_done.default_max_attempts`
- `goal_until_done.default_max_idle_seconds`
- `goal_until_done.default_backoff_seconds`

**Step 1: DEFAULT_CONFIG 추가**
**Step 2: loader wiring**
**Step 3: 테스트**
Run:
```bash
python -m pytest tests/test_goal_until_done_config.py -q
```
Expected: config defaults/load precedence pass

## Task 7: cron/background convergence 점검
**Objective:** cron inactivity logic와 중복을 줄인다.

**Files:**
- Modify: `cron/scheduler.py`
- Modify: `agent/goal_until_done.py`
- Create: `tests/cron/test_goal_until_done_cron_bridge.py`

**Step 1: inactivity helper 공용화 여부 판단**
**Step 2: shared helper 추출 또는 comment-level integration**
**Step 3: 테스트**
Run:
```bash
python -m pytest tests/cron/test_goal_until_done_cron_bridge.py -q
```
Expected: cron path unaffected / helper reuse safe

## Task 8: targeted regression suite
**Objective:** 핵심 변경이 기존 agent loop를 깨지 않는지 확인한다.

**Files:**
- No new functional files required

Run:
```bash
python -m pytest tests/test_run_agent_goal_until_done.py tests/cli/test_goal_until_done_command.py tests/test_goal_until_done_config.py tests/cron/test_goal_until_done_cron_bridge.py -q
```
Expected: all pass

## Task 9: user-facing docs / help text
**Objective:** 기능이 discoverable 하게 만든다.

**Files:**
- Modify: `hermes_cli/commands.py` help text
- Modify: relevant user docs if repo has CLI reference pages

**Verification:**
- command help shows new surface
- config docs mention defaults

## Notes
- 최소 변경 원칙: 기존 `run_conversation()` bounded loop는 유지
- first version은 CLI 중심으로 출시하고 gateway/cron deep integration은 2차로 둔다
- done_when matching은 초반엔 단순 checklist evaluation + explicit final response markers로 시작해도 된다
