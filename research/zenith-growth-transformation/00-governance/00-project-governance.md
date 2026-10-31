# 00 — Project Governance

**Programme:** Zenith Water Master Growth Programme · **Client:** Maharani Beverages LLP
**Appointed:** 2026-10-31 · **Working branch:** `seo-relaunch-2026` · **Production branch:** `main` (protected)
**Prior foundation:** research/seo-organic-growth-master (commit a10a010) — preserved, not modified.

---

## 1. Mandate

Design, manage and progressively execute a 12-month organic growth and digital revenue transformation. Operating standard: accountable for commercial outcomes (discoverability → clicks → trust → enquiries → qualified leads → orders → recurring revenue), not for code volume or vanity metrics.

## 2. Operating rules (binding)

| # | Rule | Enforcement |
|---|---|---|
| 1 | Research before execution — every change has a documented reason | Register IDs required on every commit message and PR |
| 2 | Business performance first — every recommendation maps to the outcome chain | Impact column mandatory in registers |
| 3 | No fabricated business information | Owner-confirmation register is the single gate; unconfirmed facts marked [U] never publish |
| 4 | No mass-page generation | Any new page needs distinct customer-need justification in the decision register |
| 5 | Protect the relaunch | Release gate includes regression suite (§6) |
| 6 | Production protection | Feature branches only; explicit owner approval for any merge/deploy |
| 7 | GA4 deferred | Analytics spec maintained; no install without real Measurement ID + approval |
| 8 | Skills honesty | Capability register updated per phase; unavailable tools stated, never simulated |

## 3. Programme structure

- 15 phases (0–14) with per-phase objectives, deliverables and completion gates.
- Monthly management reports (17-management-reports/) per Part X format.
- Month-by-month roadmap per Part V; deviations require a decision-register entry.
- Experiment system per Part VII (backlog lives in 15-experiments/).

## 4. The central project register

Single source of truth: `00-decision-register.csv`. One row per recommendation/change. Columns: id, description, strategic_objective, evidence (with class + source), priority (P0–P3), owner, dependencies, estimated_effort, risk, expected_impact, status, validation_method, rollback_procedure.

Status vocabulary: `proposed` → `approved` → `in-progress` → `implemented` → `validated` | `rejected` | `blocked` | `awaiting-owner` | `awaiting-external`.

## 5. Approval gates

| Gate | Triggers |
|---|---|
| G1 — owner fact confirmation | Any public business fact (price, SLA, deposit, MOQ, certification statement, lab data) |
| G2 — owner business approval | New page families, pricing presentation, subscription offers, distributor terms |
| G3 — legal/regulatory review | Any regulatory claim wording change (post-Phase-1 framework) |
| G4 — production deploy | Every merge to main — explicit approval, rollback path named |

## 6. Quality & release governance (Part IX)

Pre-implementation: problem, current state, expected outcome, dependencies, facts check, risk, rollback.
During: feature branch, focused commits, implementation log.
Post (automated battery, representative page per family): build/generator validation → html5lib strict parse → 721-URL crawl (0 broken) → redirect/canonical/sitemap checks → JSON-LD parse + schema/visible 1:1 → mobile emulation (menu/FAB/sticky/tel) → CTA/form/WhatsApp functional → regression vs. production baseline.
Evidence levels distinguished: local code < local browser < preview deploy < production. No claim of "preview passed" while SSO blocks preview access (current known limitation).

## 7. Evidence classification (preserved from prior research)

[F] verified fact · [O] observed · [R] research-backed · [H] hypothesis · [U] unknown. A hypothesis never becomes fact without the validation method recorded in its register row.

## 8. Current phase status

- **Phase 0 (this file set):** IN PROGRESS — baseline + registers established with Sprint 1.
- **Phase 1 regulatory:** R1 investigated → **resolved** (see 01-regulatory-compliance-review.md); claim inventory + business-facts registers established.
- Phases 2–14: not started; per Part XII, sequential from Sprint 1 outputs.
