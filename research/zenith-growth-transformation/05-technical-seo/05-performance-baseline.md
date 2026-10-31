# 05 — Performance Baseline (post-Sprint-1, 2026-11-01)

**Method:** Lighthouse 13.6.0, mobile form factor, local static server (lab conditions — NOT field data; no CrUX exists at this traffic level). Re-run monthly with identical flags; deltas >10% investigated.

| Page | Perf score | LCP | INP | CLS | TBT | FCP | Verdict |
|---|---|---|---|---|---|---|---|
| Homepage | 65 | 3.40s | 0ms | 0.081 | 957ms | 1.48s | PASS with debt |
| 20L money page | 95 | 1.10s | 0ms | 0.000 | 255ms | 1.10s | Excellent |
| Water-delivery-kolkata | 92 | 1.84s | 0ms | 0.000 | 282ms | 1.84s | Excellent |
| Kolkata hub (pincode block live) | 93 | 1.10s | 0ms | 0.000 | 324ms | 1.10s | Excellent — checker caused no regression |
| Products page | 97 | 1.74s | 0ms | 0.000 | 144ms | 1.74s | Excellent |

## Reading

1. **Sprint additions are performance-neutral:** lead-events.js (3KB, deferred) + pincode blocks appear on zero-metric deltas (hub 93 with the checker live).
2. **Homepage improvement is real:** LCP 5.5s (round-1 audit) → 3.4s after hero compression — but remains the only sub-90 page. Residual debt: TBT 957ms (hero slideshow letter-animation JS + inline payload) and the JS-timed reveal. The LCP decision (D-16) remains with the owner — any redesign must protect the CLS 0.081 and the brand visual identity.
3. **All money/commercial paths are fast:** the pages that carry conversion (20L, city, products) sit at 92–97 with zero layout shift.
4. **INP 0ms** across pages reflects the passive-listener architecture (landing.js/lead-events) — interaction cost is minimal.

## Targets (lab, monthly re-measure)

Commercial pages ≥90 (met); homepage ≥75 by Month 3 via either D-16 decision or TBT surgery (defer-prioritized inline scripts, letter-animation throttling — scoped only with owner approval). CLS ≤0.1 everywhere (met: max 0.081).
