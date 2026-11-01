# 06 — Information Architecture (as-shipped assessment)

**Date:** 2026-11-01 · **Basis:** 06-page-experience-inventory.csv (485 pages, programmatic) + relaunch architecture

## Verdict: the architecture serves both audiences

**Search engines:** hierarchical (home → hub → family → locality ≤5 clicks, zero islands), existence-guarded links, 1:1 schema-visible breadcrumbs, clean sitemap. **Users:** segment-appropriate CTAs on every page class (09-cta-architecture.csv), availability checking where intent peaks (20L + hubs), consistent mobile chrome (menu/FAB/sticky).

## Type map (485 pages)

locality 234 · industry 103 · city/segment 76 · corporate 26 · blog 17 · utility 13 · hubs 8 · products 5 · home 1 (+404). The weighting is deliberate: long-tail local coverage is the moat; commercial depth lives in a compact, well-linked core (money page + hubs + segment clusters).

## Findings from the experience inventory

1. **FAB gap on 21 protected pages — found and fixed this session.** The protected hand-built commercial pages predated FAB propagation; they now carry context-aware floating WhatsApp buttons (each inheriting its own page's prefilled message). Strict-parse verified.
2. `/pages/success` intentionally has no menu (post-submit landing) — documented, not a defect.
3. Blog: 17 articles all carry Article schema + soft CTAs; two new authority pieces (label guide, can-vs-jar) extend Cluster A/B.
4. Every commercial page class has both a primary and secondary CTA; no orphan conversion paths.

## Rules preserved (from relaunch)

One page = one dominant intent · hubs own geography, families own intent, localities own near-me · no new families without a decision-register entry · PROTECTED_PATHS + generator as single source of truth.
