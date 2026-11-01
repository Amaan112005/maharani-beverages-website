# G4 Deploy Request — feature/growth-sprint-1 → main

**Date:** 2026-11-01 · **Requestor:** Growth Programme Office · **Approver: [OWNER SIGNATURE REQUIRED]**
**Rollback:** per-change revert documented below; Vercel instant rollback to 4684ca2 (relaunch) as master fallback.

## Release contents (7 commits since relaunch)

| Change | Value | Risk | Rollback |
|---|---|---|---|
| Pincode availability checker (20L + 8 hubs) | Converts near-me intent on-site; honest 3 states | Low (additive; tested) | Remove blocks + script |
| Segment WhatsApp flows (6) | Qualified enquiries with context | Low | Revert wa_text/links |
| Title rewrites ME-1..3 + og sync | CTR recovery on 9,126 impressions of laggards | Low-Medium (pre-registered revert rules) | Revert 3 files |
| H1-pair consolidation (4×301 + content port) | Cannibalisation closure, equity consolidation | Medium (measured plan in place) | Revert commit; files restore byte-identical; sitemap re-add |
| Add-to-enquiry buttons + cart script | New conversion path | Low | Hide buttons |
| Form autocomplete layer | Mobile completion friction ↓ | Low | Revert attrs |
| lead-events.js measurement layer (483 pages) | GA4-ready events; zero UX impact | Low | Remove script tags |
| FAB completion (21 protected pages) | Closes floating-contact gap | Low | Remove anchors |
| 2 new authority articles (label guide, can-vs-jar) | Cluster A/B demand capture; internal-link value | Low | Unpublish + sitemap scrub |

## Test evidence (full log: 00-governance/sprint-1-implementation-log.md)

- 0 strict HTML errors (487 files) · 1,416+ JSON-LD valid · 0 broken links (721-URL crawl, re-run at final commit) · 35 redirects no loops/chains · sitemap↔files consistent (483) · pincode 3-state CDP pass · WhatsApp decode pass · mobile viewport + menu/FAB suite · Lighthouse: commercial pages 92–97, homepage 65 (no regression; pre-existing debt gated D-16).
- Evidence level: local validation (preview SSO limits cloud validation) — production probes will run immediately post-deploy as standard.

## Post-deploy monitoring (pre-committed)

Day 0: live probes (pages/redirects/sitemap/headers). Day 1–7: GSC anomaly watch (coverage + the 4 consolidated URLs → "Page with redirect"). Day 30/60: ME-1..3 verdicts; E1 read; D-3 GSC comparison vs 2026-10-30 baseline.

## Deploy mechanics

Merge `feature/growth-sprint-1` → `main` (fast-forward), push; Vercel auto-deploys; verify via live probes. Any red → revert merge commit + Vercel rollback.

**DECISION: ☐ APPROVED ☐ CHANGES REQUESTED ☐ DEFERRED** — date/signature: ______
