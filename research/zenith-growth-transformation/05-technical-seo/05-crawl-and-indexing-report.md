# 05 — Crawl and Indexing Report (baseline, 2026-11-01)

**Tool:** custom 721-URL crawler (Vercel-semantics resolver) + generator gates + sitemap forensics.

| Metric | Value | Status |
|---|---|---|
| Sitemap URLs | 483 | valid XML, real lastmods, none future-dated |
| Pages crawled | 721 (incl. alias forms) | full graph |
| Broken internal links | 0 | ✅ |
| Links via redirect | 0 | ✅ |
| Redirects (vercel.json) | 35 | no loops/chains; destinations exist |
| Click depth from home | ≤5 for all pages | zero islands (post-D3: 481 reachable + noindexed success) |
| Strict HTML errors | 0 (487 files) | ✅ |
| JSON-LD blocks valid | 1,416 | ✅ |
| Indexation bloat candidates | none open | 4 H1-pairs consolidated 2026-10-31 |
| Canonical consistency | 0 bad canonicals | self-canonical primaries |

**Comparison points:** relaunch validation (2026-10-31) and every sprint gate re-ran the same battery — no regressions at any commit. Next full re-crawl: at G4 deploy (pre) and +7 days (post), then monthly.

**Known environment limitation:** Vercel preview SSO prevents cloud-side crawl evidence for the branch; production validation used for the relaunch applies at deploy time.
