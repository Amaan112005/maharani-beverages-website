# 09 — WhatsApp Conversion Specifications (as shipped, Sprint 1)

**Status:** LIVE on feature branch (D-10, commit 27d1589) · **Number:** +91 82748 37341 (wa.me/918274837341, E.164) · **Instrumentation:** every click fires `whatsapp_click` on dataLayer with page_family + segment (lead-events.js).

## Design rules (owner conditions honoured)

1. Every message names the **originating page** and the **want** — sales sees context before replying.
2. **No personal data requested** in the prefilled text; qualification happens in conversation.
3. Number and URL-encoding verified across generator + hand pages (CDP decode tests).
4. `rel="noopener noreferrer"` on all WhatsApp anchors.

## The six flows (prefilled texts, decoded)

| # | Segment | Where live | Prefilled message |
|---|---|---|---|
| 1 | Household | 20L page, hubs, locality/city pages | "Hi Zenith, I found you on your {page} page. I need {product/service} delivery in {city/locality}. Please share price and booking details." |
| 2 | Office | office-water-delivery/supply, corporate pages | "Hi Zenith, I'm on your {page} page. We need recurring office water supply in {city}. Please share a corporate quote with rates and delivery schedule." |
| 3 | Hotels & Restaurants | hotels/restaurants/hotels-restaurants industry pages | "Hi Zenith, I'm on your {page} page. I manage procurement for a {segment} in {city} and need an FSSAI-compliant water supplier. Please share compliance details and trade rates." |
| 4 | Bulk | other industry pages, event pages, /pages/bulk | "Hi Zenith, I'm on your {page} page. We need regular bulk water supply in {city}. Please share bulk pricing." |
| 5 | Retailers | /pages/products | "Hi Zenith, I'm on your products page. I run a shop and want to stock Zenith water. Please share trade pricing and supply terms." |
| 6 | Distributors | /pages/distributor (+ form dual-submit) | "Hi Zenith, I'm on your distributor page. I'm interested in a Zenith distributorship. Please share terms, territory options, and investment details." |

Pincode checker states append their own context (area + pincode) to the household flow.

## Sales-side operating spec (requires D-7 owner commitment)

- Reply SLA: <5 min in business hours (fastest controllable conversion factor [H]).
- Macros per flow: price card (household), rostered plan (office), compliance pack (HORECA), volume quote (bulk), trade pack (retail), verification pack (distributor).
- Lead log: date, flow, source page, outcome — reconciled monthly with GA4 `generate_lead` (once GA4 lands).
- Never charge "application fees" — the market is fraud-contested (Bisleri's public warning is the evidence); Zenith's transparency is the counter-position.

## Measurement

Pre-GA4: dataLayer events accumulate in-page only (no transport). Post-GA4: `whatsapp_click` → key event with parameters above; dedupe rule 1/session/element (implemented).
