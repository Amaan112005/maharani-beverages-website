# 02 — Purchase Journey Maps (segment journeys, as-designed after Sprint 1)

**Household (P1)** — Google near-me → snippet with locality + price signal → 20L page → **pincode check (E1)** → visible pricing → FAB WhatsApp with context message → sales macro reply (<5 min target, D-7) → slot booked → first delivery → review request (GBP) → recurring rhythm. *Failure points: unconfirmed pincode without verify path (fixed — honest unconfirmed state), slow reply.*

**Office (P2)** — "office water supply kolkata" → office/corporate page → corporate quote form (≤6 fields) or office WhatsApp flow → rostered plan + GST question answered (BF-10 gated) → contract rhythm. *Failure points: billing info absent (gated), no capacity signal.*

**HORECA (P5)** — industry page → compliance-pack request (HORECA flow) → documents + trade rates → audit-ready supply. *Failure points: pack contents not yet assembled (lab library gated).*

**Event (P6)** — urgent near-me → event page → WhatsApp with date/venue/qty → capacity check → quote. *Failure points: no stated capacity (BF-15 gated).*

**Distributor (P8)** — distributorship search → distributor page → verification elements (Udyam/FSSAI visible) → form dual-submit + distributor flow → verification pack → terms call. *Failure points: terms thin (BF-13); fraud fear countered by no-fee stance + documents.*

**Retail (P4)** — referral/Justdial → products page → trade-pricing WhatsApp flow → trade pack. *Failure points: trade terms unconfirmed (BF-13 shared).*

Common design rules: every journey names origin+intent in WhatsApp; every failure point either shipped-fixed this programme or has a named owner-gated register row; measurement per journey = lead_type parameter post-GA4.
