# 14 — Brand Entity Consistency Audit

**Date:** 2026-10-31 · **Method:** programmatic scan of all 483 site pages (visible text + markup) · **[F]**

## Findings

| Entity | Variants found | Verdict |
|---|---|---|
| Business name | "Maharani Beverages LLP" (935), "Maharani Beverages" (16), "Zenith Water" (3,151), "Zenith" (1,889) | ✅ Consistent hierarchy: legal entity + brand used correctly; the 16 bare "Maharani Beverages" are footer/menu shortenings — acceptable, no action |
| Phone | "+91 82748 37341" (1,728), bare "8274837341" (13 visible national-format), "+91 8274837341" (**1 — schema `telephone` field**) | ✅ Display formats fine; **fix queued: normalise the 1 schema occurrence** to "+91 82748 37341" for citation-parity |
| Email | marketing@maharanibeverages.com (481); complaints@fssai.gov.in (1 — legitimate regulatory reference) | ✅ Single business email, consistent |
| Address | "Ranihati Plant" (436) / "Ranihati plant" (99) / "Ranihati facility…" variants / "Ranihati Industrial Park" (10) | ✅ No conflicting addresses anywhere (single site of operation); variant phrasing is descriptive, not NAP data. **NAP canonical form for citations (from GBP pack): Ranihati Industrial Park, Howrah — exact unit/PIN pending OC-15** |
| FSSAI licence | 12825999000938 — single format site-wide | ✅ |

## AI-search / entity implications [O→H]

Consistent name/phone/licence across 483 pages gives search engines and AI answer systems a clean entity graph: one brand, one legal entity, one licence, one number, one location family. When GBP + citations ship with the identical NAP, the entity consolidation is complete. Residual entity gaps that remain: no Wikipedia/Wikidata presence (unnecessary at this scale), no GBP (P0 pending), no third-party corroboration yet (Month-9 PR workstream).

## Actions

1. Normalise the single schema `telephone` occurrence (queued code fix, trivial).
2. On GBP/citation publication, reuse the exact NAP from the GBP pack §1 — never introduce a new variant.
3. Re-run this scan quarterly (Phase-14 cadence).
