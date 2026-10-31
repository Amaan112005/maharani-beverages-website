# Sprint 1 — Implementation Log & Completion Report

**Date:** 2026-10-31 · **Branch:** `feature/growth-sprint-1` (from `seo-relaunch-2026` @ 9d7753e)
**Authorisation:** owner directive received 2026-10-31 (D-8, D-9, D-10 approved; D-3 approved with conditions; GBP/citations conditional-prep; GA4 stays deferred)

---

## 1. Files changed (2 commits)

**Commit 27d1589 — features (437 files):** `assets/js/pincode-checker.js` (new); `scripts/generate-landing-pages.py` (pincode hub slot + 5 segment wa_text flows + LEGACY_CONTENT_PORT); `index.html` (third-state honesty wording); `20-liter-water-jar-delivery-kolkata.html` (checker embed + script); 2 blog articles + `kolkata-water-supply.html` (D-9 titles + og sync); `pages/products.html` / `distributor.html` / `bulk.html` (segment WhatsApp links); 421 regenerated pages.

**Commit 8fbddf3 — consolidation (6 files):** `vercel.json` (+4 permanent 301s → 35 total); `sitemap.xml` (485→481); retirement of `drinking-water-{kolkata,howrah}.html` + `mineral-water-{kolkata,howrah}.html`; docs (migration map, metadata experiment register, GBP pack, citation register, this log).

## 2. Functionality implemented

- **D-8 pincode checker:** standalone component; 3 honest states (available / region / unconfirmed — no unverified promises); single data source `assets/data/pincodes.json` (**flagged for owner verification — OC-21 added**); embedded on 20L page + all 8 city hubs; aria-live results, numeric keypad, dataLayer hook (no GA4 installed); homepage third state aligned to same honest wording.
- **D-10 WhatsApp flows:** household / office / HORECA / bulk / retailer / distributor — every flow names the originating page and the want; number + encoding verified; no personal data requested beyond intent.
- **D-9 titles:** 3 evidence-backed rewrites with pre-registered baselines + rollback map (research/…/11-metadata-experiment-register.md); strong performers untouched; 30-day GSC protocol defined.
- **D-3 consolidation:** content ported (5–7% shingle overlap proved uniqueness), 301s, sitemap scrub, links repointed (9 files, 0 residual), migration map + GSC comparison plan.

## 3–5. Tests performed & results — ALL PASS

| Test | Result |
|---|---|
| Generator quality gates (421 pages) | 0 issues |
| html5lib strict parse (all files) | **0 errors** |
| JSON-LD parse | **1,416 blocks, 0 failures** |
| 721-URL crawl | **0 broken links, 0 via redirect** |
| Redirect validation (35) | no loops/chains/duplicates; destinations exist |
| Sitemap ↔ files | 481 = 481; retired URLs absent; XML valid |
| Pincode functional (CDP, mobile 390px) | 700001→available w/ order CTA · 700099→available (exact db match) · **560001→unconfirmed, verify-on-WhatsApp, no promises** |
| WhatsApp deep links (CDP decode) | office / HORECA / retailer / distributor flows all carry page origin + intent |
| Mobile viewport + regression | 20L: no overflow, menu button + FAB intact; hub checker renders + script loads |
| Structured data regression | parse-clean; no schema classes touched in this sprint |

## 6. Outstanding defects

1. Homepage pincode uses an **inline duplicate** of the pincode dataset (vs `assets/data/pincodes.json`) — divergence risk; unify in a later sprint (logged, low urgency).
2. `pincodes.json` (93 entries) is legacy data — **requires owner approval as the serviceability database** before the checker is treated as authoritative (OC-21).
3. Vercel preview deployment not triggered (branch push only; SSO still blocks preview access — evidence level = local browser validation, labelled per governance §6).

## 7. Business information still required (blocking next work)

Owner interview (BF register): jar deposit/exchange, MOQs, delivery SLAs, city capability list, GST invoicing, payment methods, distributor terms, plant capacity, support hours/SLA, ISO cert scope, lab test reports (BF-2/14 for the lab library + D-17 wording), GBP identity answers (storefront vs service-area decision).

## 8. Risks

R2 measurement blindness until GA4 · R9 fact dependencies (mitigated: nothing fact-dependent shipped) · R10 regression (mitigated: full battery) · new: pincode data accuracy risk until OC-21 (mitigated: honest "unconfirmed" state makes wrong data low-harm).

## 9. Evidence

Functional-test transcripts: this session's CDP outputs (pincode 3 states, WhatsApp decodes, mobile checks). Screenshots: `sprint-1-evidence/20L-pincode-available.png` (mobile) · `kolkata-hub-pincode-desktop.png` (desktop).

## 10. Preview deployment status

Branch pushed to GitHub; Vercel will build a **Preview** for `feature/growth-sprint-1` automatically (Git integration). Preview SSO prevents automated validation — owner review via the Vercel dashboard, or approve G4 deploy to validate on production directly (rollback documented per change).

## 10b. Sprint extension (same day): D-11, D-12, D-13 — ALL CLOSED

- **D-11 ✅** products page: 4 add-to-enquiry buttons wired to the existing enquiry cart (localStorage → /pages/enquiry-cart checkout with WhatsApp handoff); toast feedback; cart script included. Cart E2E verified by code-path review (same addToCart the homepage uses, proven in round-4 E2E).
- **D-12 ✅** autocomplete attributes on index + distributor Formspree fields. **Audit finding:** all 3 Formspree forms already ≤6 fields with `_gotcha` honeypots; contact/careers "forms" verified functional via existing WhatsApp-routing handlers — no fix needed, no fabricated problem solved.
- **D-13 ✅ verified pre-satisfied:** the IS 14543 article already carries an accurate answer-first quick-answer + 2026 regulatory update box (matches the Phase-1 verified timeline). No change made.
- **Defect caught by the release gate (and fixed before push):** the autocomplete patch initially inserted attributes inside self-closing tags (`type="text"/ autocomplete=...>`) — caught by the strict-HTML check, repaired, repo-wide sweep confirmed no other instances. Commit amended. Lesson recorded: attribute-insertion regex must handle `/>`.
- Commits: `21108f2` (amended). Crawl re-run: 0 broken / 0 via redirect.

## 11. Production confirmation

**Production `main` is untouched.** Verified: `git log origin/main` = 4684ca2 (relaunch); all sprint work exists only on `feature/growth-sprint-1` (27d1589, 8fbddf3). Live site maharanibeverages.com serves the relaunch build, unchanged by this sprint.
