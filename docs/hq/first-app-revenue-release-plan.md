# First App Revenue Playbook — Release Development Plan

> **For Hermes:** Use this plan task-by-task. Keep the product local-first, release-ready, and small enough for a 1-person build.

**Goal:** Ship a globally relevant, 1-person-buildable photo-to-report mobile app that can be released to real users within about 1 month.

**Architecture:** Build a narrow mobile workflow with local storage, fixed templates, and PDF export as the core artifact. Avoid login, collaboration, sync, OCR, and AI generation in v1. Use AI for drafts, scaffolding, and repetitive UI, but keep product decisions, state handling, and release gates human-controlled.

**Tech Stack:** Mobile app stack of choice, local persistence, PDF generation/export, system share sheet, template-driven UI, analytics/telemetry, crash reporting, optional later backend for sync/subscription.

---

## 1) Product decision

### Final product wedge
> Users take photos, add short notes and status tags, choose a template, and export a shareable PDF report.

### Target customer
Primary:
- property managers
- facility maintenance teams
- field inspectors
- small contractors / repair teams

Secondary:
- home inspection
- insurance / damage documentation
- small fleet / equipment checks

### What this is not
- not a generic note app
- not a full inspection SaaS platform
- not a collaboration product
- not an OCR product in v1
- not an AI auto-writing product in v1
- not a large workflow platform

### Release constraint
The app must be small enough that one person can build, test, and ship it without adding backend complexity.

---

## 2) Release definition

A release candidate is ready only when all of these are true:
- a first report can be created end-to-end
- the report looks like a real work document
- PDF export works on real devices
- the app survives app restart with draft recovery
- loading / empty / error states exist for core screens
- the app can be used without login
- the app feels usable in under 30 seconds for the first report

### Release gates
- **Gate A: Scope locked** — no new feature classes can enter v1
- **Gate B: Core flow works** — create → add photos → note → template → preview → export
- **Gate C: Device pass** — tested on at least one real Android device and one real iPhone/device target if applicable
- **Gate D: Store-ready** — privacy, permissions, screenshots, metadata, and review text complete
- **Gate E: Failure handling** — export, storage, and permission failures have graceful paths

---

## 3) Product scope for v1

### Must have
- new report entry
- photo add
- photo note input
- status tag selection
- template selection
- report preview
- PDF export
- share sheet integration
- local draft save / restore
- loading / empty / error states

### Not in v1
- OCR automation
- AI summary generation
- team collaboration
- sync / accounts / roles
- multi-user permissions
- dashboards / analytics views
- complex form builder
- subscription/paywall complexity beyond a simple unlock placeholder

---

## 4) AI-assisted development model

### What AI should do
Use AI to accelerate:
- product brief drafts
- screen drafts / wireframes
- repetitive component scaffolding
- template variations
- copy variants
- bug triage summaries
- test case generation

### What humans should control
Keep these decisions human-owned:
- product scope
- data model
- error handling strategy
- permission model
- export behavior
- release criteria
- pricing / monetization decision
- store submission decision

### Operating rule
AI can generate options, but the human chooses the final product path.

---

## 5) Recommended architecture

### Core approach
- **Local-first MVP**: core flow works without backend
- **Template-based reports**: avoid building a generic form engine
- **Single artifact output**: PDF is the primary output
- **Minimal state**: draft, preview, exported
- **Small component library**: button, input, card, badge, empty state, loading state, error state

### Why this architecture
- lowers build time
- lowers failure risk
- makes release testing possible for one person
- keeps the app from becoming a platform

### Later-only architecture
These can be deferred until after release:
- account sync
- team sharing
- cloud storage
- subscriptions
- AI processing
- OCR pipeline
- collaborative templates

---

## 6) 4-week release plan

## Week 1 — Scope, UX, and technical spike

**Outcome:** The release path is frozen and the hardest technical risks are proven early.

### Task 1.1 — Freeze the first customer subsegment
**Objective:** Choose one initial user group only.

**Recommended choice:** property managers / facility maintenance / field inspection users.

**Done when:**
- the app can be described in one sentence
- the first customer is explicit
- the app is not trying to serve everyone

### Task 1.2 — Freeze the screen flow
**Objective:** Lock the 6-screen flow.

Flow:
1. Home
2. Photo Add
3. Photo Note Input
4. Template Selection
5. Preview / PDF
6. Share / Complete

**Done when:**
- each screen has one primary action
- each screen has a state list
- no extra screen class is added

### Task 1.3 — Prototype the hard parts first
**Objective:** Reduce the risk of late surprises.

Prototype these in isolation:
- photo capture/import
- local draft save/restore
- PDF export
- share sheet

**Done when:**
- each risky area works in a minimal spike
- no decision is blocked by unknown platform behavior

### Task 1.4 — AI draft the initial UI
**Objective:** Get visual drafts quickly.

Recommended tools:
- Stitch for first-pass screen drafts
- Figma for refinement and component alignment
- Pencil MCP only if you need design context bridged into coding

**Done when:**
- there is a clear draft for all 6 screens
- one visual direction is chosen

---

## Week 2 — Core build

**Outcome:** The end-to-end flow works on device.

### Task 2.1 — Build app shell and navigation
**Objective:** Create the basic app structure and screen routing.

**Done when:**
- all six screens can be reached
- screen transitions are stable
- back navigation behaves predictably

### Task 2.2 — Build Home
**Objective:** Make starting a new report obvious.

**Done when:**
- `+ 새 보고서 시작` is the main action
- recent reports are visible
- empty state works

### Task 2.3 — Build Photo Add
**Objective:** Add photos quickly with minimal friction.

**Done when:**
- camera and gallery entry points exist
- thumbnails show immediately
- photo deletion works

### Task 2.4 — Build Photo Note Input
**Objective:** Let the user annotate each photo fast.

**Done when:**
- each photo has a short note input
- status tags are limited to 2~3 choices
- previous/next navigation works

### Task 2.5 — Build Template Selection
**Objective:** Keep the formatting decision simple.

**Done when:**
- 2~3 templates are available
- one default template exists
- the continue action works

---

## Week 3 — Output, recovery, and polish

**Outcome:** The report is a believable work document.

### Task 3.1 — Build Preview
**Objective:** Show the report exactly as users expect to export it.

**Done when:**
- title/date/status/photos/notes render correctly
- preview matches export intent

### Task 3.2 — Build PDF export
**Objective:** Produce a real shareable document.

**Done when:**
- PDF generates on device
- PDF saves successfully
- export errors are handled gracefully

### Task 3.3 — Build share flow
**Objective:** Let the user send the PDF out.

**Done when:**
- system share sheet works
- exported file is accessible
- user returns to the app cleanly

### Task 3.4 — Draft save / restore
**Objective:** Recover work after app close or interruption.

**Done when:**
- unfinished reports survive relaunch
- photos and notes remain mapped
- restore path is reliable

### Task 3.5 — Add states
**Objective:** Make every screen robust.

States required:
- loading
- empty
- error
- read-only / disabled where needed

---

## Week 4 — Release prep

**Outcome:** The app is ready for external users.

### Task 4.1 — Device QA
**Objective:** Verify the real-world experience.

**Done when:**
- the flow works on at least one real device per target platform
- performance is acceptable
- image handling is stable

### Task 4.2 — Copy / onboarding polish
**Objective:** Make the first-time experience understandable.

**Done when:**
- the value proposition is clear in one sentence
- first-use instructions are minimal
- the user knows what to do next

### Task 4.3 — Privacy and store metadata
**Objective:** Prepare for store submission.

**Done when:**
- privacy policy is ready
- permission prompts are explained
- app description and screenshots are ready

### Task 4.4 — Release candidate review
**Objective:** Decide whether to ship, delay, or cut scope.

**Done when:**
- all release gates are passed or consciously waived
- known issues are documented
- rollout plan is clear

---

## 7) Recommended build order

1. Product wedge and subsegment
2. Screen flow
3. Technical spikes for photo/PDF/storage
4. Home
5. Photo Add
6. Photo Note Input
7. Template Selection
8. Preview
9. PDF Export
10. Share
11. Draft restore
12. State handling
13. QA and store prep

---

## 8) Risk register

### Risk 1: PDF export is harder than expected
**Mitigation:** spike it before building the rest.

### Risk 2: Photo handling becomes messy
**Mitigation:** keep image operations simple and test on real devices early.

### Risk 3: Scope creep into platform features
**Mitigation:** hard-ban login, sync, collaboration, OCR, AI generation in v1.

### Risk 4: Template explosion
**Mitigation:** only ship 2~3 templates.

### Risk 5: Release feels incomplete
**Mitigation:** define the first release as a narrow but complete workflow, not a platform.

---

## 9) Definition of done

This project is done when:
- a real user can create a report from photos
- the report can be exported as PDF
- the app can be used without an account
- the app is stable on a real device
- the first use is understandable without a long explanation
- the scope is still small enough that one person can maintain it

---

## 10) Decision summary

### Recommended path
> Ship the smallest end-to-end photo-to-report workflow possible.

### What to resist
- adding enterprise features
- turning it into a platform
- adding AI because it feels modern
- broadening the target audience too early

### Why this is the right plan
- it is release-oriented
- it is solo-dev feasible
- it respects the 1-month constraint
- it leaves room for v2 after real usage proves the workflow

## Next step
Create a concrete day-by-day execution checklist from this release plan, then start with the hardest technical spike: PDF export + local draft save.
