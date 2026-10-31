# 04 — Technical SEO Audit (State as of 2026-10-31, post-launch)

This audit consolidates four audit rounds (Jul–Oct 2026) + post-launch live validation, all against the CURRENT production build (deployed 2026-10-31, commit 4684ca2). Every claim **[F]** was re-verified this session unless marked "prior round, unchanged".

---

## 1. Crawlability & indexability — PASS

- 485 sitemap URLs, valid XML, real lastmods, zero redirecting/deleted URLs **[F]**.
- Homepage-rooted BFS: **every page ≤5 clicks**; zero link islands (254 eliminated in round 2) **[F]**.
- 721-URL crawl: **0 broken internal links, 0 redirect-dependent links, 0 missing local assets** **[F]**.
- 31 redirects: no loops/chains; destinations 200; .html catch-all + cleanUrls correct; junk paths (index_test, locations/) 308 to primaries **[F, live-verified]**.
- 1 bad-canonical count: 0. No accidental noindex outside intentional (success page, 404) **[F]**.
- Product migration 300ml→250ml: 308 live-verified; images renamed + 200 **[F]**.

## 2. Architecture — PASS (with documented decisions)

- 487 pages: home / 24 city-family / 195 locality / 8 hubs / ~100 segment-city / industry-city / 15 blog / utilities **[F]**.
- Breadcrumb + geographic linking hierarchical; existence-guarded generator (`href_exists`) prevents future broken related-links **[F]**.
- The 4 documented H1-overlap pairs (drinking-water vs -supplier, mineral-water vs -supplier × Kolkata/Howrah) remain the ONE open architecture decision (consolidation map prepared; owner sign-off pending). Impact is contained: GSC cannibal-stem analysis found only 2 overlap groups, both already known **[F]**.

## 3. Performance — CONDITIONAL PASS

- Mobile hero images compressed 423K→132K / 562K→178K; ~4.2MB dead assets removed; favicon/icon set optimized **[F]**.
- 12 requests on mobile homepage; render-blocking limited to fonts CSS + inline critical CSS **[F]**.
- **Known limitation:** homepage LCP ~5.5s lab — gated by the legacy slideshow's JS-timed reveal; documented since round 1, deliberately NOT redesigned (brand decision). INP/CLS pass **[F]**.
- Desktop position 11.56 vs mobile 7.05 correlates with desktop CWV/thinner engagement — monitor, don't over-rotate **[O→H]**.

## 4. Structured data — PASS (compliance-first)

- 1,428 JSON-LD blocks parse; zero fabricated review markup site-wide (removed round 1, re-verified each round) **[F]**.
- FAQ schema 1:1 visible; breadcrumbs 1:1 visible; SearchAction removed (no on-site search) **[F]**.
- Product/Offer/BreadcrumbList/Article/Organization types validated for field completeness (round 3) **[F]**.
- `hasOfferCatalog` flattened to Product-with-offers **[F]**.
- **Standing policy:** no review markup until a real review corpus exists; no LocalBusiness extras beyond verified facts.

## 5. On-page — PASS

- 0 strict HTML parse errors across 487 files (html5lib strict, round 2) **[F]**.
- Titles/metas/OG/Twitter complete post-rounds 1–3; og:title synced; og:url present; dims on media **[F]**.
- Mobile menu on all templates; FAB + sticky bar on commercial pages; valid E.164 tel links; 404 branded page live **[F, live-verified]**.

## 6. Open technical items (non-blocking, tracked)

| Item | Class | Status |
|---|---|---|
| Slideshow LCP refactor | P2 | Awaiting owner design decision |
| Font self-hosting (~200–400ms potential) | P2 | Recommended next quarter |
| Homepage inline payload 164K split | P3 | With any homepage redesign |
| Desktop experience deepening | P3 | Content-level, not technical |

## 7. Verification inventory (what "PASS" is built on)

721-URL crawl · html5lib strict parse of all files · JSON-LD parse of 1,428 blocks · CDP functional suite (menu, slideshow, modal, pincode, cart, forms) · live production probes (2026-10-31): 14 URLs, 3 redirect classes, headers, sitemap. Tools and limitations: deliverable 14.
