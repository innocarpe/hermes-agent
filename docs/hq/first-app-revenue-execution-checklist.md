# First App Revenue Playbook — Execution Checklist

> **For Hermes:** Use this as the day-by-day execution checklist. Stay locked to the release plan and do not widen scope.

**Goal:** Turn the release plan into an exact execution path for a solo developer so the app can be shipped within about 1 month.

**Operating rule:** If a task does not move the app closer to a shippable end-to-end report flow, it does not belong in v1.

---

## Before Day 1 — Setup

### Checklist
- [ ] Confirm the first customer subsegment
- [ ] Freeze v1 exclusions: no login, no sync, no collaboration, no OCR, no AI generation
- [ ] Pick the mobile stack and PDF/export approach
- [ ] Create the repo task board / TODO list
- [ ] Create a device test matrix

### Deliverable
- One-sentence product wedge
- One locked subsegment
- One locked v1 scope statement

---

## Day 1 — Scope lock

### Objective
Lock the target user and the first workflow.

### Tasks
- [ ] Write the final product wedge in one sentence
- [ ] Pick one target subsegment only
- [ ] Write the “what this is not” list
- [ ] Confirm v1 exclusions
- [ ] Define success criteria

### Done when
- The product can be explained in under 10 seconds
- No one on the team can argue for a broader platform scope

---

## Day 2 — Screen flow lock

### Objective
Freeze the screen sequence and action per screen.

### Tasks
- [ ] Confirm the 6-screen flow
- [ ] Assign one primary action per screen
- [ ] Assign loading/empty/error states per screen
- [ ] Confirm the back-navigation behavior

### Screen flow
1. Home
2. Photo Add
3. Photo Note Input
4. Template Selection
5. Preview / PDF
6. Share / Complete

### Done when
- No new screen class is needed
- The flow is linear and short

---

## Day 3 — Technical spikes for risky parts

### Objective
Prove the hardest technical risks early.

### Spikes
- [ ] Photo import / camera capture spike
- [ ] Local draft save / restore spike
- [ ] PDF export spike
- [ ] Share sheet spike

### Done when
- Each spike works in the simplest possible form
- No late surprises remain in these areas

---

## Day 4 — Visual draft finalization

### Objective
Lock the design direction before building everything.

### Tasks
- [ ] Generate first-pass drafts with AI
- [ ] Choose one visual direction
- [ ] Normalize spacing / typography / colors
- [ ] Confirm reusable components

### Components to lock
- [ ] Button
- [ ] Input
- [ ] Card
- [ ] Badge
- [ ] Empty state
- [ ] Loading state
- [ ] Error state

### Done when
- The design system is small and consistent
- Screen-specific one-off styling is avoided

---

## Days 5–7 — App shell + Home

### Objective
Create the app structure and make starting a report obvious.

### Tasks
- [ ] Build app shell and routing
- [ ] Build Home screen
- [ ] Implement recent reports placeholder
- [ ] Implement empty/loading/error states for Home
- [ ] Verify back navigation

### Done when
- `+ 새 보고서 시작` is the obvious next step
- The app opens into a clear starting point

---

## Days 8–10 — Photo capture and storage

### Objective
Make photo collection frictionless and stable.

### Tasks
- [ ] Build camera entry point
- [ ] Build gallery entry point
- [ ] Show photo thumbnails immediately
- [ ] Support photo removal
- [ ] Save photos locally
- [ ] Verify permissions and failure states

### Done when
- The user can reliably add and remove photos
- The photo flow feels fast on a real device

---

## Days 11–13 — Photo note input and status tagging

### Objective
Let the user annotate photos quickly.

### Tasks
- [ ] Build photo-by-photo note input
- [ ] Limit status tags to 2~3 options
- [ ] Add previous/next navigation
- [ ] Preserve state across navigation
- [ ] Handle empty note state

### Done when
- Each photo can be annotated in under a few seconds
- No complex text entry flow is required

---

## Days 14–15 — Template selection

### Objective
Keep report formatting choices simple.

### Tasks
- [ ] Create 2~3 templates only
- [ ] Set one default template
- [ ] Add short descriptions per template
- [ ] Connect continue action to preview

### Templates for v1
- [ ] Simple report
- [ ] Inspection report
- [ ] Damage record

### Done when
- The user can choose a template without thinking too long

---

## Days 16–18 — Preview screen

### Objective
Make the report look like a real document.

### Tasks
- [ ] Render title/date/status summary
- [ ] Render photos and notes
- [ ] Render selected template style
- [ ] Ensure preview matches export intent
- [ ] Handle report-too-empty state

### Done when
- The preview already feels like the final output

---

## Days 19–22 — PDF export and share

### Objective
Turn the preview into a shareable artifact.

### Tasks
- [ ] Implement PDF generation
- [ ] Save generated PDF locally
- [ ] Add share-sheet integration
- [ ] Handle export failure gracefully
- [ ] Verify file access on device

### Done when
- A user can export and share a PDF without confusion
- PDF layout is readable and stable

---

## Days 23–24 — Draft recovery

### Objective
Recover unfinished reports after app restart.

### Tasks
- [ ] Save in-progress drafts locally
- [ ] Restore drafts on app launch
- [ ] Re-link photos and notes correctly
- [ ] Verify behavior after forced app close

### Done when
- The user does not lose work after interruption

---

## Days 25–26 — States and edge cases

### Objective
Make the app resilient.

### Tasks
- [ ] Add loading states everywhere
- [ ] Add empty states everywhere
- [ ] Add error states everywhere
- [ ] Test permission denial
- [ ] Test no-photo / no-note / export-failure cases

### Done when
- Core screens no longer feel brittle

---

## Days 27–28 — Device QA and release prep

### Objective
Prepare for store submission and external use.

### Tasks
- [ ] Test on real devices
- [ ] Fix layout issues
- [ ] Fix export issues
- [ ] Prepare screenshots
- [ ] Prepare app description
- [ ] Prepare privacy notes
- [ ] Prepare review notes

### Done when
- The app is store-ready, not just demo-ready

---

## Release gate checklist

### Gate A — Scope
- [ ] No login
- [ ] No sync
- [ ] No collaboration
- [ ] No OCR in v1
- [ ] No AI generation in v1

### Gate B — Core flow
- [ ] Home → Photo Add → Note → Template → Preview → PDF → Share works

### Gate C — Robustness
- [ ] Drafts survive restart
- [ ] Error states exist
- [ ] Permissions are handled gracefully

### Gate D — Device pass
- [ ] Real-device tested
- [ ] Export tested
- [ ] Photo flow tested

### Gate E — Store readiness
- [ ] Screenshots ready
- [ ] Metadata ready
- [ ] Privacy notes ready

---

## What not to do
- Do not add accounts before release
- Do not add AI because it feels useful
- Do not add more templates before the first release works
- Do not build analytics dashboards in v1
- Do not convert this into a platform

---

## Final definition of done
The project is done when a real user can:
1. open the app,
2. start a report,
3. add photos,
4. add notes,
5. choose a template,
6. export a PDF,
7. share it,
8. and return later without losing the draft.
