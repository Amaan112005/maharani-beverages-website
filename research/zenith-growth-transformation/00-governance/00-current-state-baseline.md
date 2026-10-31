# 00 — Current State Baseline

Baseline date: 2026-10-31 · Basis: live production + repo + four audit rounds + research package.

## 1. Repository and deployment

| Item | State |
|---|---|
| Production | `main` @ 4684ca2 — relaunch LIVE on maharanibeverages.com (deployed 2026-10-31, Vercel build success) [F] |
| Working branch | `seo-relaunch-2026` @ a10a010 (research package committed; clean tree) [F] |
| Research package | research/seo-organic-growth-master — 17 files, preserved unmodified [F] |
| Site | 487 HTML pages (421 generated + hand/protected), 485 sitemap URLs, 31 redirects [F] |
| Validation state | 0 strict HTML errors · 1,428 JSON-LD blocks valid · 0 broken links (721-URL crawl) · mobile suite green · click-depth ≤5, zero islands [F] |

## 2. Performance baseline (GSC export 29 Jul–28 Oct 2026) [F]

| Metric | Value |
|---|---|
| Clicks / Impressions / CTR / Avg pos | 871 / 35,475 / 2.46% / ~8 |
| Daily clicks Aug→Sep→Oct | 12.7 → 8.7 → 7.2 (−43% Aug→Oct) |
| Daily impressions Aug→Oct | 515 → 327 → 313 (−39%) |
| Mobile vs desktop position | 7.05 vs 11.56 |
| Near-me cluster | 331 queries · 4,351 impr · 84 clicks (~1.9% CTR) |
| Zero-click striking-distance pool | 55 queries · 3,224 impr · 0.19% CTR |
| Pricing-intent cluster | 375 impr · 0 clicks |
| Branded queries | 351 impr · 31 clicks |
| Search appearance | Product snippets 82 clicks/2,153 impr · Merchant listings 26/95 (27.4% CTR) · Review snippets 5/322 |

**Decline diagnosis (two competing mechanisms, tracked not concluded):** (a) index-then-demote after the 20-Jul mass expansion, root causes now addressed by the relaunch; (b) post-monsoon seasonal demand cooling. Test: Nov–Dec performance vs Oct baseline despite seasonality. Next GSC export is the trigger metric.

## 3. What is already complete (do not redo)

Technical relaunch (all 4 audit rounds) · favicon system · review-markup removal · SearchAction removal · FAQ/breadcrumb schema 1:1 · internal-link architecture rebuild (254→0 islands) · mobile menu everywhere · 404 page · og/twitter/metadata overhaul · font-preload/tel/noopener fixes · dead-asset removal · hero compression · visible 20L pricing · GBP/citation *strategy* spec'd (not executed — owner-side) · GA4 event spec (deferred) · keyword database + page inventory (data/) · 8 personas · competitor intelligence · 12-experiment backlog.

## 4. Open decisions awaiting owner

| ID | Decision | Blocking |
|---|---|---|
| D-1 | GBP creation/verification (needs owner identity + address confirmation) | Near-me recovery (P0-2/P0-3 of roadmap) |
| D-2 | Business facts: jar deposit/exchange, MOQ, GST invoicing, delivery SLAs, city capability list, lab reports | P1 trust/content items |
| D-3 | H1-overlap pairs (4): consolidate per earlier map or differentiate | Architecture |
| D-4 | GA4 Measurement ID + activation approval | All measurement |
| D-5 | Lab-report library: provide NABL test documents | Trust asset P1-3 |
| D-6 | Optional voluntary BIS certification (trust upside under new regime) | Brand decision |
| D-7 | WhatsApp business number formalisation + sales SLA commitment | CRO P1-4 |

## 5. Known limitations (carried from research register)

No live GSC/GA4 access (exports only) · no paid SEO suites (qualitative volumes) · SERP observations via search proxy · no backlink crawler · preview SSO blocks live preview validation (production validation possible — used 2026-10-31).

## 6. Risks snapshot (full register: 00-risk-register.csv)

R1 regulatory — **RESOLVED 2026-10-31** (site claim verified accurate; see Phase 1 review) · measurement blindness until GA4 · seasonal trough misreading · GBP absence · review-star absence · homepage LCP ~5.5s lab · WhatsApp-channel dependence · thin-page reassessment · owner-fact dependencies.
