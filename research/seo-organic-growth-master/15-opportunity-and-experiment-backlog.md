# 15 — Opportunity and Experiment Backlog

Ranked by (impact × confidence) ÷ effort. Each experiment has a falsifiable success criterion and a rollback. Metrics baselines from the 2026-10-30 GSC export unless noted. **[H]** = hypothesis to validate.

---

| Rank | Experiment | Hypothesis | Primary metric | Success criterion | Effort | Rollback |
|---|---|---|---|---|---|---|
| E1 | Pincode checker on 20L page (P0-4) | Household visitors convert better when availability is confirmed on-page vs homepage-only | whatsapp_click rate on 20L (post-GA4); interim: GSC CTR stability | +30% relative 20L CTR or measured CTA engagement ≥8% of page sessions | S | Remove block |
| E2 | Title rewrite: IS 14543 article (R1) | Question-form title lifts CTR on definitional queries | URL query-level CTR, ≥200 impr | +50% relative CTR, position ±1.5 | S | Revert title |
| E3 | Comparison title reframe (R2) | "Kolkata Delivery Compared" reduces self-comparison scepticism | Same protocol as E2 | +50% relative CTR | S | Revert |
| E4 | Same-day modifier on money-page title (R4) — gated 30 days post-relaunch | "instant/same-day" modifiers capture the 129-impr zero-click query class | Same protocol | +25% CTR, no position loss | S | Revert |
| E5 | GBP live + review programme (P0-2/3, P1-5) | Map-pack presence converts near-me demand independent of organic rank | GBP calls/directions; near-me cluster CTR | Near-me CTR ≥3% by day 90 | M | N/A (asset, not page) |
| E6 | Lab-report library (P1-3) | Verifiable quality evidence lifts enquiry rate and earns citations/links | generate_lead rate on affected pages; referring domains | +15% lead rate on money pages in 60 days | M | Unpublish |
| E7 | Segment WhatsApp flows + sales macros (P1-4) | Prefilled intent text improves sales qualification speed and close rate | Lead-to-reply time; sales-reported conversion | Reply <5 min in business hours ≥80%; lead quality scored +1 | S | Revert links |
| E8 | Products-page add-to-enquiry (P1-6) | Cart checkout produces larger average enquiries than single WhatsApp taps | cart_checkout_click events (post-GA4) | ≥10 checkouts/month in 60 days | S | Hide buttons |
| E9 | "Water subscription" landing test (P3) | Existing subscription demand (82 impr, pos 15.7) converts if a page targets it | GSC position/CTR on subscription queries; leads | Position ≤8 and first 5 subscription leads in 90 days | M | 301 to 20L page |
| E10 | Monsoon-content spike timing (P2) | Seasonal safety content + GBP posts capture pre-summer demand surge | Seasonal query impressions/clicks vs 2026 baseline | Documented seasonal capture ≥2026 levels despite trend | S | N/A |
| E11 | Locality differentiation wave-1 (top 20) | Locality-specific facts improve local rankings beyond template baseline | GSC per-locality position for top-20 pages | ≥30% of wave-1 pages gain ≥2 positions in 90 days | M | Revert content |
| E12 | Honest aggregateRating return (gated) | With a real review corpus, Product review snippets lift merchant CTR | Merchant listing CTR (27.4% baseline [F]) | Maintain/improve merchant CTR with valid markup | M | Strip markup |

## Backlog hygiene

- Every experiment needs the pre/post data window defined BEFORE launch (this file is that record for E1–E12).
- Quarterly pruning: anything not started in 2 quarters gets re-scored or dropped.
- All deploys through the established preview + 721-URL crawl gate.
