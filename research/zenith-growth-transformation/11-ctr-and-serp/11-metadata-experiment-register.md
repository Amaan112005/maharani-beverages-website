# 11 — Metadata Experiment Register (Sprint 1: D-9)

Protocol (per owner condition + master-research §07.4): pre-registered baselines, 30-day GSC window, claim = +50% relative CTR with position stable ±1.5, else revert. Baseline source: GSC export 2026-10-30.

| id | URL | Target queries (evidence) | Baseline clicks/impr/pos [F] | Before (rollback) | After | Rationale | Status |
|---|---|---|---|---|---|---|---|
| ME-1 | /blog/is-14543-vs-is-10500-drinking-water-standards | "14543" (239 impr, 0 clk, pos 7.2); "is 14543" (463, 2, 8.5) — definitional demand | 39 / 5,267 / 7.2 | IS 14543 vs IS 10500: Packaged Drinking Water Standards India (2026) \| Zenith | IS 14543 vs IS 10500: Which Water Standard Matters? | Acronym-first title only attracts people who already know the term; question form captures definitional intent; 69ch→52ch stops truncation | implemented-on-branch |
| ME-2 | /blog/bisleri-vs-kinley-vs-zenith-kolkata | "kinley vs bisleri" (147, 1, 9.2); "kinley or bisleri which is better" (120, 0, 8.5) | 8 / 2,356 / 7.6 | Bisleri vs Kinley vs Zenith Kolkata (2026) \| Price, Delivery & Purity | Bisleri vs Kinley vs Zenith: Kolkata Delivery Compared (2026) | 0.34% CTR — self-comparison titles invite scepticism; "compared" frames as evidence-led local analysis | implemented-on-branch |
| ME-3 | /kolkata-water-supply | "kolkata water supply" class; hub for supplier intent | 22 / 1,503 / 10.4 | Kolkata Water Supply \| Zenith Water (check live) | Drinking Water Supply Kolkata \| Home, Office & 20L Jars \| Zenith | Hub title reads like a utility; segment modifiers widen eligible queries at position 10.4 headroom | implemented-on-branch |

Rollback map: git history of this branch holds before-states; revert = single commit revert per file. og:title synced to match each new title. **Excluded by owner condition:** pages with strong performance (20L money page title R4 is held 30 days post-relaunch per pre-registered protocol), all remaining 482 pages unchanged.
