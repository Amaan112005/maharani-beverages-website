# 13 — KPI Dashboard Specification (monthly, one page)

**Data sources:** GSC export (owner pulls or grants access) · GA4 (post-activation) · GBP insights (post-verification) · sales lead log (manual sheet) · crawl/technical battery (programme runs).

## Acquisition (top block)

| KPI | Baseline (2026-10-30 export) | Source |
|---|---|---|
| Organic clicks / month | ~290 | GSC |
| Organic impressions / month | ~11,825 | GSC |
| Site CTR | 2.46% | GSC |
| Avg position | ~8 | GSC |
| Non-brand clicks share | ~83% of query clicks | GSC (computed) |
| Mobile vs desktop clicks | 719 / 150 | GSC |

## Landing-page performance

Clicks/impr/CTR/position for the top-15 URLs (page-inventory.csv is the full list); watch-list: money page, hubs, W1 localities, the two new blog posts.

## Customer acquisition (conversion)

| KPI | Instrumentation | Status |
|---|---|---|
| whatsapp_click / phone_click | dataLayer → GA4 on activation | LIVE (staged) |
| form_submit | Formspree success events | SPEC ready |
| generate_lead (by lead_type) | GA4 key event | SPEC ready |
| Distributor / corporate / bulk enquiry counts | lead_type parameter + sales log | SPEC ready |
| Pincode check distribution (available/region/unconfirmed) | dataLayer event | LIVE (staged) |

## Commercial outcomes (manual until invoicing integration)

Lead-to-order rate by lead_type (sales log) · repeat-order rate (sales log) · revenue attributed to organic (owner finance input) — reported qualitatively until GA4 + CRM discipline exist.

## Local authority

GBP: calls, direction requests, website clicks, review count/rating · Local pack presence for the 12 near-me seed queries (manual monthly check, logged in SERP observation DB).

## Experience & health

CWV field data (GSC CrUX) · 404 rate · index coverage deltas · release-gate battery results.

## Reporting rule

No metric is reported without its baseline and its measurement source next to it. Targets are set only after two post-relaunch data points exist (per Part VI: baseline first, then conservative/expected/ambitious).
