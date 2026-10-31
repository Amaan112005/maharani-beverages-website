# Locality Differentiation — Wave 1 Selection & Brief

**Date:** 2026-10-31 · **Method:** demand-ranked from GSC page data (3 core families × locality) + pincode-coverage cross-check · **[F]**

## Selection logic (pre-registered)

Rank = GSC impressions across the locality's three family pages (packaged-drinking-water / water-delivery / water-supplier), clicks as tiebreak. Wave-1 = top-30 with impressions ≥20 OR clicks ≥1 OR pincode coverage ≥2. Full ranking: `locality-wave1-selection.csv`.

## Headline findings

1. **Demand concentrates in ~12 localities** (Dum Dum 1,000 impr / 23 clicks → Howrah Station 875/19 → Salt Lake 761/12 → New Town 732/10 → Park Street 442/7…). Wave-1 effort maps exactly here.
2. **The protected hand-tuned pages are the demand winners** (Dum Dum, Rajarhat, Garia were protected in the relaunch and now lead the ranking) — evidence the protection strategy + differentiation thesis was right.
3. **Pincode-data gaps** [F]: Howrah Station, New Town, Chandannagar, Raniganj (among the highest-demand) have **zero pincode coverage** in `pincodes.json` — the checker can't confirm them. → Extend the dataset for these with OC-21 (owner-verified).

## Wave-1 differentiation brief (per locality, owner-fact slots marked)

For each W1 locality, add ONLY verified facts in three slots (nothing invented — Rule 3):
1. **Delivery window / route detail** for this locality — [U: owner]
2. **Landmark reference** (office park, station, market the route serves) — [U: owner]
3. **One genuine locality FAQ** (e.g., Salt Lake: "Do you deliver to Sector V office buildings?") — [U: owner]

Plus already-safe (data-derived): nearby-areas sentence (exists), cross-link density check.

**Implementation path:** generator `LOCALITY_FACTS` dict (slug → 3 slots) injected into section2_body; empty slots render nothing (no placeholders). Facts enter only via the owner register (confirmed status).

## Effort estimate

30 localities × ~15 min owner fact-check + one generator injection = ~1 day total. Expected effect measured per E11 protocol (≥30% of wave-1 pages gain ≥2 positions in 90d).

## What this does NOT do

No new pages · no expansion beyond existing localities · no unverified locality claims · no mass regeneration beyond the injection.
