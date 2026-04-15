# First App Revenue Playbook — Proposal

## One-line proposal
Build a **photo-to-report mobile app** for field work: users take photos, add short notes and status tags, choose a template, and export a shareable PDF report.

This proposal is read under `docs/hq/first-app-strategy-principles.md` and `docs/hq/first-app-doc-map.md`.

## Target customer
Primary:
- property managers
- facility maintenance teams
- field inspectors
- small contractors / repair teams

Secondary:
- home inspection
- insurance / damage documentation
- small fleet / equipment checks

## Problem
These users already do the same repetitive workflow manually:
1. capture photos
2. write short notes
3. decide what matters
4. assemble a report
5. export/share it

Current pain:
- too much manual整理
- reporting is slow
- photos and notes stay scattered
- existing enterprise tools are heavier than needed
- generic scanner/note apps do not solve the workflow end-to-end

## Proposed product
A narrow mobile workflow with only the needed steps:
- photo capture / upload
- short note per photo
- status tag per photo
- 2~3 templates
- preview
- PDF export
- share

## Why this is worth building
- real users already exist
- competitors already exist, which proves demand
- the workflow is narrow enough for a 1-month MVP
- the output is easy to understand: a PDF report
- monetization can be direct via Pro unlock / credits / subscription

## Why this wedge
We are **not** building:
- a full field service platform
- a collaboration suite
- a generic scanner app
- an AI auto-writing product
- a complex form builder

We are building the smallest useful reporting loop.

## Competitive position
Our wedge should be:
- simpler than SafetyCulture / Fulcrum / GoCanvas
- more workflow-specific than generic scanner apps
- more visual and report-oriented than note apps
- faster to start than heavy enterprise tools

## MVP scope
### Must have
- new report entry
- photo add
- photo note input
- status tag selection
- template selection
- PDF preview / export
- share

### Not in MVP
- OCR automation
- AI summary generation
- team collaboration
- sync / accounts / roles
- complex forms
- analytics dashboards

## Solo-dev feasibility
This MVP is intentionally designed to be **1-person buildable** within about a month if we keep it local-first and template-based.

### Solo-dev constraints
- no login
- no collaboration
- no real-time sync
- no complex backend workflows
- no OCR in v1
- no AI generation in v1
- only 2~3 templates
- export-first delivery

### Why this is feasible solo
- the core flow is only 5~6 screens
- the output is a single PDF/report artifact
- most of the value is in workflow clarity, not platform complexity
- local storage can carry the MVP before any server work is added

## Success criteria
- first report can be created in under 30 seconds
- report output looks like a real work document
- user understands why to pay
- there is an obvious repeat-use case

## Monetization
Preferred options:
- free tier with limited reports
- Pro unlock for templates / exports / batch features
- credits for advanced processing later
- subscription only after the workflow proves repeat usage

## Risks
- generic positioning will fail
- scope creep into enterprise features
- too much AI too early
- unclear target user
- trying to compete head-on with broad inspection platforms

## Recommendation
Proceed with the photo-to-report wedge, but keep the market definition tight:
> photo + note + status + template + PDF

## Review assets
- Research memo: `docs/hq/first-app-revenue-app-research.md`
- Competitor comparison: `docs/hq/first-app-revenue-competitor-comparison.md`
- Repeated complaints: `docs/hq/first-app-revenue-repeated-complaints.md`
- Benchmark summary: `docs/hq/first-app-revenue-benchmark-summary.md`
- Scope fixed: `docs/hq/first-app-revenue-scope-fixed.md`
- Tickets: `docs/hq/first-app-revenue-implementation-tickets.md`
- Screen spec: `docs/hq/first-app-revenue-screen-spec.md`

## External competitor links
- SafetyCulture iAuditor: https://safetyculture.com/iauditor
- Fulcrum: https://www.fulcrumapp.com/
- GoCanvas: https://www.gocanvas.com/
- TrueContext: https://truecontext.com/
- FastField: https://www.fastfieldforms.com/
- Fleetio: https://www.fleetio.com/
- Whip Around: https://whiparound.com/
- CamScanner: https://www.camscanner.com/
- Adobe Scan: https://www.adobe.com/acrobat/mobile/scanner-app.html

## Next step
Pick one first customer subsegment and benchmark the first 3 onboarding/report screens of the closest competitors.
