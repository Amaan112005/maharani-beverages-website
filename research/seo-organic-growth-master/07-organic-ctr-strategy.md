# 07 — Organic CTR Strategy

Built from the 2026-10-30 GSC export (29 Jul–28 Oct 2026, 871 clicks / 35,475 impr / 2.46% CTR). **[F]** = from export; rewrite proposals are **[H]** until A/B-validated by GSC query-data deltas. Research date 2026-10-31.

---

## 1. Where clicks are lost (measured)

**A. CTR laggard pages** (≥150 impressions, CTR <1.5%) [F]:

| URL | Clicks | Impr | Pos | Diagnosis |
|---|---|---|---|---|
| /blog/is-14543-vs-is-10500… | 39 | 5,267 | 7.2 | Informational intent; snippet answers the question → searchers satisfied on SERP; title is acronym-speak |
| /blog/bisleri-vs-kinley-vs-zenith-kolkata | 8 | 2,356 | 7.6 | Comparison intent partially served; national-brand searchers may distrust a brand self-comparison |
| /kolkata-water-supply | 22 | 1,503 | 10.4 | Hub page; title "Kolkata Water Supply" reads like a utility, not a supplier |
| /packaged-drinking-water-new-town | 6 | 693 | 21.7 | Position 21 — most "impressions" are page-2+; CTR ceiling until ranking improves |
| /packaged-drinking-water-salt-lake | 6 | 485 | 7.5 | Local intent strong; snippet lacks locality/delivery hook |

**B. Zero-click striking-distance queries** (pos 4–20, ≥100 impr, 0 clicks) [F] — the single biggest recovery pool:

| Query | Impr | Pos | Recommended target page action |
|---|---|---|---|
| 14543 | 239 | 7.2 | Article already ranks; snippet-target the definitional answer |
| water supply near me | 176 | 8.2 | **No dedicated target** → strengthen homepage local signals / 20L page near-me block |
| order water online 20l | 153 | 7.2 | 20L page — add "order online" language + WhatsApp-first CTA |
| kinley vs bisleri | 147 | 9.2 | Comparison article — retitle to include brand pair first |
| kinley or bisleri which is better | 120 | 8.5 | Same — question-format H2 already exists; improve snippet |
| 20 litre water instant delivery | 129 | 9.8 | 20L page — "instant/same-day" wording absent from title |
| mineral water 20 litre | 109 | 9.4 | 20L page — add "mineral water" synonym variant |
| water 20 litre bottle | 77 | 5.7 | Products page |

Aggregate zero-click pool: 55 queries, 3,224 impressions, 6 clicks (0.19% CTR) [F]. Recovering to a modest 3% on this pool ≈ **+95 clicks/quarter at current positions** — before any ranking gains. [H arithmetic, F inputs]

**C. Commercial-price cluster: 375 impressions, 0 clicks.** Pricing queries are the highest-intent class on the site and the worst-served. The relaunch already added visible 20L pricing (live 2026-10-31) — **expected to change this cohort first**; verify in the next GSC window.

## 2. Rewrite programme (proposals = [H], risks noted)

### R1 — IS 14543 article title
- Now: "IS 14543 vs IS 10500: Packaged Drinking Water Standards India (2026) | Zenith" (69ch — over display, brand truncated)
- Proposed: "IS 14543 vs IS 10500: Which Water Standard Matters?" (52ch)
- Why: the 5,267 impressions show Google trusts the page; the acronym-first title only attracts people who already know the term, while 239 impressions on the bare query "14543" show definitional demand. Put the question form first.
- Risk: the current title's "India (2026)" modifier may rank for year-modified queries; mitigate by keeping "2026" in the H1/meta, not the title.

### R2 — Comparison article title
- Now: "Bisleri vs Kinley vs Zenith Kolkata (2026) | Price, Delivery & Purity"
- Proposed: "Bisleri vs Kinley vs Zenith: Kolkata Delivery Compared (2026)"
- Why: 2,356 impressions / 8 clicks = 0.34% CTR [F]. Self-comparison titles invite scepticism; "Kolkata Delivery Compared" reframes as local service evidence. Add a visible "How we compare" methodology note to counter bias perception.
- Risk: CTR gain could come from lower-intent browsers; watch enquiry rate per session in GA4 later.

### R3 — Kolkata hub
- Now: "Kolkata Water Supply | Zenith" class titles
- Proposed pattern: "Drinking Water Supply in Kolkata | Home, Office & 20L Jars | Zenith"
- Why: hub serves supplier intent; current title describes a utility. Segment-inclusive modifiers widen eligible queries.
- Risk: none material (position 10.4 has headroom).

### R4 — Money page (already strong; protect + sharpen)
- Now: "20 Litre Water Jar Kolkata | Home & Office Delivery | Zenith" — 115 clicks, 2.2% CTR [F]
- Proposed test: add same-day signal: "20 Litre Water Jar Kolkata | Same-Day Home & Office Delivery"
- Why: "20 litre water instant delivery" (129 impr, pos 9.8, 0 clicks) proves the modifier; the page already promises fast delivery.
- Risk: title currently excellent; change ONLY via GSC A/B observation — hold for 30 days post-relaunch first (relaunch already changed this page's content; stacking another variable confounds measurement).

### R5 — Meta description principles (site-wide)
1. Front-load the locality + service + proof point within the first 120 chars (mobile truncation).
2. Include a number where truthful: price-from, licence number, delivery window.
3. Match the dominant intent of the target query class (per keyword DB intent column).
4. No clickbait; every claim must be visible on the page.

## 3. Rich-result and SERP-feature levers

| Lever | Evidence | Action |
|---|---|---|
| FAQ rich results | FAQ schema now 1:1 visible post-relaunch [F from audit 4] | Eligible again; monitor Search-appearance "FAQ" rows in GSC |
| Product snippets | Already 82 clicks / 2,153 impr (3.8% CTR) [F] | Feed real price/availability; Merchant Center review |
| Merchant listings | 27.4% CTR when shown [F] | Product feed + GMC verification — highest-leverage existing channel |
| GBP map pack | Absent for brand [O] | P0 — transforms near-me CTR independent of organic position |
| Review stars (organic) | Markup removed for compliance [F] | Path back = REAL reviews corpus on products → reintroduce honest aggregateRating |
| Breadcrumb display | Implemented 1:1 [F] | Improves snippet readability for deep URLs |

## 4. Measurement protocol (no false certainty)

- Baseline: current export stored in `data/`.
- Re-export GSC at +30, +60, +90 days post-relaunch (relaunch = 2026-10-31).
- For each rewritten title: compare query-level CTR for the URL's top 10 queries, min. 200 impressions before/after, seasonality-adjusted against the Aug→Oct trend.
- Claim "win" only if CTR delta >50% relative AND position stable ±1.5. Otherwise revert — titles are single-variable, fast to roll back.
