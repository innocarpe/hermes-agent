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

## Recent entries

```yaml
- timestamp: "2026-04-21T08:32:00+09:00"
  initiative_id: "thread-collector-archive-insight-sync-2026-04-21"
  decision: applied
  actor: "Hermes"
  rationale: "Absorbed the already-collected Threads/NaverCafe archive into the daily 01-전략 HQ report; signal remained stable around distribution-first funnels, AI-as-operating-system workflows, and low-cost repeatable revenue loops, with no meaningful new delta"
  source: "docs/hq/01-전략/아카이브-인사이트-흡수-2026-04-21.md"
  follow_up: "Watch for any new raw corpus delta or a shift from repeatable small-outcome loops toward larger product bets"
- timestamp: "2026-04-20T08:31:00+09:00"
  initiative_id: "thread-collector-archive-insight-sync-2026-04-20"
  decision: applied
  actor: "Hermes"
  rationale: "Absorbed already-collected Threads/NaverCafe archive signals into the 01-전략 daily HQ report; emphasized distribution-first, funnel-oriented operators, AI-as-operating-system workflows, and low-cost repeatable revenue loops"
  source: "docs/hq/01-전략/아카이브-인사이트-흡수-2026-04-20.md"
  follow_up: "Use the next archive sync to check whether distribution-first and workflow-OS signals strengthen or flatten"
- timestamp: "2026-04-15T11:29:00+09:00"
  initiative_id: "youtube-benchmark-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Applied YouTube niche signals into HQ channel/content rules; kept high-risk BODY topics gated, reframed TECH toward practical/analysis angles, and treated benchmark style as a positioning input rather than a copy target"
  source: "03-콘텐츠/메트릭/벤치마킹-2026-04-15.md"
  follow_up: "Review whether CASE/TAX/ATLAS/TECH priority should shift after the next benchmark run"
- timestamp: "2026-04-15T12:37:00+09:00"
  initiative_id: "threads-benchmark-agenpreneur-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Translated the benchmark into TemperStone HQ business rules: prefer already-monetized but inefficient markets, judge products by repeated cost reduction and operating simplicity, and keep channel/ops docs focused on decision criteria rather than writing style"
  source: "Discord thread / message.txt"
  follow_up: "Patch the market discovery and global-first app docs with the same decision criteria if they drift"
- timestamp: "2026-04-15T12:40:00+09:00"
  initiative_id: "youtube-benchmark-2026-04-15-hq-translation"
  decision: applied
  actor: "Hermes"
  rationale: "Expanded the YouTube benchmark into direct 03-콘텐츠 judgment rules and 04-채널 routing rules for crowded/high-risk niches"
  source: "03-콘텐츠/메트릭/벤치마킹-2026-04-15.md, docs/hq/discord-channel-operating-map.md"
  follow_up: "Use the new routing outcomes (launch/reframe/gate/drop) on the next channel decision"
- timestamp: "2026-04-15T12:50:00+09:00"
  initiative_id: "youtube-benchmark-2026-04-15-expand"
  decision: applied
  actor: "Hermes"
  rationale: "Split the benchmark rules into a shared 03-콘텐츠 principle file and a dedicated 04-채널 YouTube routing checklist so the guidance can be reused across future docs"
  source: "03-콘텐츠/메트릭/공통-판단원칙.md, docs/hq/discord-channel-youtube-routing-checklist.md"
  follow_up: "Keep future benchmark docs linked to the shared principle file and routing checklist"
- timestamp: "2026-04-15T12:58:00+09:00"
  initiative_id: "discord-channel-routing-one-pager-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Added a compact routing 1-pager and tightened 04-채널 / 05-운영 guidance so structural channel decisions stay separate from runtime incident handling"
  source: "docs/hq/discord-channel-routing-one-pager.md"
  follow_up: "Use 04-채널 for routing/architecture and 05-운영 for verification/recovery loops"
- timestamp: "2026-04-15T13:23:33+0900"
  initiative_id: "first-app-strategy-translation-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Translated the app benchmark into first-app strategy rules: prefer repeated-cost workflow problems, require clear payer and small-operating-model fit, and keep the first app scoped to one narrow job"
  source: "docs/hq/initiative-card-first-app.md, docs/hq/first-app-revenue-market-research.md, docs/hq/first-app-revenue-scope-fixed.md, docs/hq/app-idea-exploration-shortlist.md"
  follow_up: "Use the repeated-cost/clear-payer rule when reviewing any new app candidate"
- timestamp: "2026-04-15T13:33:00+09:00"
  initiative_id: "content-card-template-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Created a reusable 03-콘텐츠 content decision card template and linked it from the shared principle file so benchmark notes can be standardized"
  source: "03-콘텐츠/메트릭/콘텐츠-판단카드.md"
  follow_up: "Use the card template for future content/benchmark notes when comparing niches or routing decisions"
- timestamp: "2026-04-15T13:45:00+09:00"
  initiative_id: "content-card-example-ai-news-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Created a concrete AI news example card to show how the shared 03-콘텐츠 template handles reframe decisions for crowded niches"
  source: "03-콘텐츠/메트릭/콘텐츠-판단카드-예시-ai-news.md"
  follow_up: "Reuse the example structure for future niche cards when testing reframe vs gate decisions"
- timestamp: "2026-04-15T13:52:00+09:00"
  initiative_id: "content-card-examples-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Created three reusable 03-콘텐츠 example cards for gate/launch/reframe patterns so the template can be exercised on high-risk and low-risk niches"
  source: "03-콘텐츠/메트릭/콘텐츠-판단카드-예시-health-gate.md, 03-콘텐츠/메트릭/콘텐츠-판단카드-예시-world-history-launch.md, 03-콘텐츠/메트릭/콘텐츠-판단카드-예시-tax-gate.md"
  follow_up: "Use these examples as the default reference when adding new content judgment cards"
- timestamp: "2026-04-15T13:36:46+0900"
  initiative_id: "first-app-principles-aggregation-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Created a consolidated first-app strategy principles doc that ties the review, shortlist, scope, MVP, tickets, flow, and screen specs back to repeated-cost / clear-payer / small-operating-model criteria"
  source: "docs/hq/first-app-strategy-principles.md"
  follow_up: "Use this consolidated principle file as the first stop when revisiting the first-app line"
- timestamp: "2026-04-15T13:42:47+0900"
  initiative_id: "first-app-document-map-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Added a first-app document map and redirected strategy/research/implementation files to the shared principle file so the product chain has a clear canonical entry point"
  source: "docs/hq/first-app-doc-map.md, docs/hq/first-app-revenue-proposal.md, docs/hq/first-app-revenue-photo-report-exploration.md, docs/hq/first-app-revenue-solo-dev-feasibility.md, docs/hq/first-app-revenue-competitor-benchmark.md, docs/hq/first-app-revenue-mvp-priority-recalibration.md, docs/hq/first-app-revenue-first-3-screens-benchmark.md"
  follow_up: "Keep future first-app notes pointing at the principles doc and document map instead of re-stating the same criteria"
- timestamp: "2026-04-15T14:16:00+0900"
  initiative_id: "first-app-playbook-review-archive-2026-04-15"
  decision: applied
  actor: "Hermes"
  rationale: "Marked the evidence review as a legacy archive note because the authoritative criteria now live in the shared strategy principles doc and document map"
  source: "docs/hq/first-app-revenue-playbook-review.md, docs/hq/first-app-doc-map.md"
  follow_up: "When the review pattern appears again, keep it as an archive note and avoid rebuilding another parallel review layer"
```

