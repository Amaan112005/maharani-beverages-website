# D-3 H1-Overlap Consolidation — Migration Map

**Date:** 2026-10-31 · **Branch:** feature/growth-sprint-1 · **Approved by:** owner (consolidation strategy reaffirmed)
**Isolation:** implemented as a separate task from metadata experiments (no title/meta changes in this migration's page set beyond what D-9 specified for other URLs).

## Migration mapping

| Retiring URL (301) | Primary URL (200, self-canonical) | Content disposition |
|---|---|---|
| /drinking-water-kolkata | /drinking-water-supplier-kolkata | Unique blocks ported: "Why Choose Zenith for Drinking Water in Kolkata" (3-item list) + "Drinking Water for Every Setting" paragraph → appended via generator LEGACY_CONTENT_PORT (persistent across regenerations) |
| /mineral-water-kolkata | /mineral-water-supplier-kolkata | Ported: "What Makes Zenith Mineral Water Different" (Balanced Minerals / 7-Stage / Multiple Sizes) + "Mineral Water for Homes & Businesses" paragraph |
| /drinking-water-howrah | /drinking-water-supplier-howrah | Ported: "Why Choose Zenith for Drinking Water in Howrah" (Local Manufacturing Ranihati / Certified Quality / Industrial Focus) + homes-&-industry paragraph |
| /mineral-water-howrah | /mineral-water-supplier-howrah | Ported: "What Makes Zenith Mineral Water Different" (Locally Bottled / Balanced Composition / Certified Quality) + Howrah homes-&-industry paragraph |

**Evidence for porting:** shingle analysis showed only 5–7% overlap between each legacy page and its primary — the legacy hand content was substantially unique (e.g., mineral-water-kolkata 423 words vs supplier 851 visible). Full text loss would have been a genuine content regression; the port preserves it durably in the generator (not hand-edited HTML).

## Checklist (owner conditions)

| # | Condition | Status |
|---|---|---|
| 1 | Preserve unique/useful content | ✅ via LEGACY_CONTENT_PORT (verified on all 4 primaries post-regen) |
| 2 | Update internal links | ✅ 9 files repointed; 0 residual links verified |
| 3 | Direct 301 redirects | ✅ 4 added (vercel.json 31→35), permanent |
| 4 | Update canonicals | ✅ primaries self-canonical (unchanged); retiring pages removed |
| 5 | Remove retired URLs from sitemap | ✅ 485→481, XML re-validated |
| 6 | Redirect chains/loops check | ✅ validated in release battery (35 redirects, no loops/chains) |
| 7 | Record migration mapping | ✅ this document |
| 8 | GSC comparison after migration | 🟡 plan: compare primary-page clicks/impressions at +30/+60 days vs the 2026-10-30 export baseline (legacy + primary combined vs primary alone); also monitor Coverage for the 4 retiring URLs (expect "Page with redirect" classification) |

## Rollback (independently reversible per owner condition)

1. Re-add the 4 HTML files (git revert of the retirement commit restores them byte-identical).
2. Remove the 4 redirect entries from vercel.json.
3. Re-add the 4 sitemap entries (regenerate lastmod = original file dates preserved in git history).
4. Re-run release battery.
Rollback time: <15 minutes. The content port on primaries is harmless either way (additive section) and needs no rollback.
