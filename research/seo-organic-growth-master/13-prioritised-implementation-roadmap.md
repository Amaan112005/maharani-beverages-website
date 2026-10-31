# 13 — Prioritised Implementation Roadmap

Prioritisation framework (per brief §17): impact × commercial intent × confidence ÷ (effort + risk). Relaunch deployed 2026-10-31; roadmap Day 0 = 2026-11-01.

---

## P0 — Critical (this fortnight)

| # | Action | Why | Effort | Evidence |
|---|---|---|---|---|
| P0-1 | **Verify BIS/FSSAI legal position + site FAQ claim** (Risk R1) | Multiple 2026 sources say BIS IS 14543 certification is legally required to SELL packaged drinking water; the site's FAQ says it is "no longer mandatory" — one of these is wrong, and a public legal misstatement is a trust/compliance exposure | Owner + counsel | [R/F conflict, deliverable 03] |
| P0-2 | **Google Business Profile** creation + verification | Map pack owns near-me SERPs; 4,351-impression cluster is the biggest recovery pool | Owner (2–3h) + verification wait | [F/O, deliverable 09] |
| P0-3 | **Citations**: Justdial, Sulekha, IndiaMART, Bing, Apple, Facebook (NAP-consistent) | Directory positions dominate local commercial SERPs; currently invisible | 1 day | [O] |
| P0-4 | **Add pincode checker block to 20L + top city pages** | Household journey fails at "do you deliver to me" on the exact pages earning the near-me impressions | Code, 0.5 day | [F journeys, deliverable 08] |
| P0-5 | **Owner confirmations log**: jar deposit policy, MOQ, GST invoicing, delivery SLAs, lab reports, BIS status | Multiple P1 items are blocked on real business facts — never invent | Owner async | [U] |

## P1 — High impact (days 15–60)

| # | Action | Why | Effort |
|---|---|---|---|
| P1-1 | Title rewrites R1–R3 (07) with GSC A/B protocol | Zero-click pool 3,224 impr at 0.19% CTR — pure recovery | 0.5 day + 30-day measurement |
| P1-2 | IS 14543 plain-language hub update (answer-first block for "14543") | 239+463 impr definitional demand, owned ranking | 0.5 day |
| P1-3 | Lab-report library page (owner docs) | Unique trust asset; no competitor has it | 1 day + owner docs |
| P1-4 | WhatsApp flows per segment (08.4) + sales macros | Fastest controllable conversion factor | 1 day |
| P1-5 | Review acquisition programme (GBP first, then Justdial) | Social proof is the unknown-brand gap | Ongoing, process |
| P1-6 | Add "Add to enquiry" buttons to products page (feature exists) | Dead feature → live conversion path | 0.5 day |
| P1-7 | Local press pitch (monsoon-safety data story) | First earned-authority links | Outreach |
| P1-8 | Products-page price guidance + MOQ language | Commercial-price cluster: 375 impr, 0 clicks | 0.5 day |

## P2 — Medium (days 61–120)

- Content Cluster A completions (TDS, label guide, jar hygiene) — 2 posts/month.
- Office-page strengthening (billing/roster content after owner confirms).
- Hotel vetting checklist + distributor economics piece (owner numbers).
- Font self-hosting + homepage payload reduction (with LCP decision).
- Citation expansion + GBP posts cadence.
- Locality differentiation wave 1 (top-20 localities by pincode/GSC demand).

## P3 — Experimental / validation-gated (days 121–180)

- Subscription landing test ("water subscription" demand: 82 impr, pos 15.7 [F]) — build only if operations can fulfil.
- Desktop experience deepening.
- Distributor-page verification widgets (document gallery) — after P0-1 clarity.
- AI-search visibility audit re-run (AI Overview presence on brand/category queries — Google AI features now in ~43% of searches [O]).

## 180-day north star (targets, not promises **[H]**)

| Metric | Baseline (Oct export) | 180-day target |
|---|---|---|
| Monthly organic clicks | ~290 | 600–800 |
| Near-me cluster CTR | ~1.9% | 4%+ (with GBP live) |
| Zero-click pool | 3,224 impr / 0.19% CTR | <1,500 impr / 3% CTR (recovered to clicks + position gains) |
| generate_lead events | unmeasured (GA4 deferred) | baseline + trend after GA4 lands |
| GBP calls + direction requests | 0 | monthly tracked, growing |
| Referring domains | unmeasured | +20 from defined channels |

## Governing rules

No mass page generation · no invented facts/policies/prices · every deploy through preview + crawl gate (established release process) · relaunch branch discipline preserved · production main protected by the same validation battery that shipped 2026-10-31.
