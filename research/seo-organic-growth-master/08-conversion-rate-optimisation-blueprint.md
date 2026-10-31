# 08 — Conversion Rate Optimisation Blueprint

Journey: GOOGLE LISTING → LANDING → TRUST → CONTACT → QUALIFIED LEAD → CUSTOMER.
Evidence: GSC export [F], prior functional audits [F], competitor fetches [O], consumer research (02) [R/H].

---

## 1. Current conversion assets (audited, functional [F])

- WhatsApp FAB on all 487 pages; page-specific pre-filled messages; number consistent (wa.me/918274837341).
- Sticky Call/WhatsApp bar on commercial landing pages (mobile).
- tel: links E.164-valid everywhere.
- 3 Formspree forms (contact/bulk, distributor ×2, careers, enquiry-cart checkout) + pincode checker (real data, verified E2E).
- Visible 20L pricing tiers (post-relaunch), pricing FAQ, jar-policy language.
- Mobile menu, breadcrumbs, 404 recovery page — all live and tested.

**The machinery works. The strategy doesn't differentiate by segment yet.**

## 2. CTA architecture (segment-differentiated)

| Page type | Audience | Primary CTA (above fold) | Secondary CTA | CTA wording principle |
|---|---|---|---|---|
| 20L money page | Household | WhatsApp: "Get 20L jar price + delivery slot" | Call | Price-first (proven query intent) |
| Water-delivery city | Household/office | "Check delivery in your area" (pincode) | WhatsApp | Availability-first |
| Office/corporate pages | Office admin | "Get office supply quote" (form) | WhatsApp with roster intent | Continuity-first ("never run out") |
| Industry pages (hotel/hospital/school) | Purchasing mgr | "Request compliance pack" (FSSAI/BIS docs + quote) | WhatsApp | Audit-first |
| Bulk pages | Procurement | "Get bulk pricing" | Email | Volume-first |
| Distributor page | Prospect distributor | "Apply for distributorship" + verification elements | WhatsApp | Trust-first (fraud-aware audience) |
| Products page | Mixed retail/household | **ADD "Add to enquiry" per product** (gap — feature exists, buttons absent) | WhatsApp | Bundle-first |
| Blog/regulatory | Researcher | Soft CTA: "Questions? WhatsApp our team" | — | No hard sell |
| Homepage | All | WhatsApp + pincode checker (exists) | — | Two-path split by need |

Placement rules: primary CTA visible in first viewport on mobile (measured 390px); secondary CTA after trust block; never more than 2 competing CTAs per viewport.

## 3. Trust architecture — what's answered vs missing

| Question a buyer has | Answered? | Gap action |
|---|---|---|
| Is the water safe? | ✓ FSSAI number + 7-stage process + lab language | Add actual lab test summary/report PDF (owner-provided) |
| Is the company real? | ✓ address, Udyam PDF, compliance page | Add team/factory photos (genuine) |
| What does it cost? | ✓ 20L tiers visible | Extend price guidance to bottle SKUs on products page |
| Do you deliver to me? | ✓ pincode checker + coverage lists | Add delivery SLA per city (24–48h claims exist — make consistent) |
| What are jar deposit/exchange terms? | Partial | **Owner confirmation needed** → publish policy table [U] |
| Minimum order? | Partial | Publish per-segment MOQ [U — owner] |
| Billing/GST invoice for office? | ✗ | Add to corporate pages [U — owner confirms capability] |
| Can I trust reviews? | ✗ (markup removed for compliance) | Real-review programme (GBP/Justdial/WhatsApp screenshots with consent) |
| Is BIS mandatory/held? | ⚠️ FAQ claim conflicts with 2026 industry sources | **Owner verification — P0 (see Risk R1)** |

## 4. WhatsApp journey (per-segment flows — spec for implementation)

All flows: deep link + prefilled text + page-context parameter (for later GA4 `whatsapp_click` with `page_family`, `segment` params).

1. **Household**: "Hi Zenith, I need 20L jar delivery at [pincode]. Please share price and first-delivery slot." → sales macro: price card + slot options.
2. **Office**: "Hi Zenith, I need recurring office water supply (approx __ staff) at __. Please share a corporate quote." → rostered plan offer.
3. **Retail**: "Hi Zenith, I run a shop at __ and want to stock Zenith. Please share trade pricing." → trade pack.
4. **Distributor**: "Hi Zenith, I'm interested in a distributorship for __ area. Please share terms." → verification pack (Udyam + FSSAI + terms).
5. **Bulk/events**: "Hi Zenith, I need bulk water for an event on [date] at [venue], approx __ jars." → capacity check + quote.
6. **Hotel/restaurant**: "Hi Zenith, I manage procurement at __ and need an FSSAI-compliant supplier. Please share your compliance pack and trade rates."

Sales-side requirements: reply SLA <5 min business hours [H: fastest controllable conversion factor]; saved macros per flow; lead log (source=organic, page=URL) — feeds deliverable 12 attribution.

## 5. Forms & friction

- Keep Formspree forms at ≤6 fields (current: 7–9). Trim: merge name/organisation; make phone the only required contact + optional WhatsApp-opt-in checkbox.
- Add `autocomplete` attributes (name, tel, email) — mobile keyboards.
- Add Formspree honeypot (`_gotcha`) — 4 forms lack it [F from round-4 audit].
- Success path: redirect to /pages/success (exists, noindexed) + WhatsApp fallback link on success page.
- Distributor form: current dual-submit (Formspree + WhatsApp redirect) is correct — keep.

## 6. Conversion journeys (walk-through analysis per brief §19)

**Household near-me journey**: Google "20 litre water supply near me" → sees Zenith (pos 5.5, post-relaunch snippet) → lands on 20L page → immediate: H1 matches query, price visible, FAB. Friction: **must confirm "near me"** — pincode checker is on homepage but NOT on the 20L page. **Fix: embed pincode checker block on 20L + top city pages.** Estimated impact: high (matches the #1 intent cluster: 4,351 impr) [H].

**Office journey**: searches "office water supply kolkata" → office page → needs: capacity guidance, billing, reliability proof. Current page answers generically. Add: "How office supply works" (roster, dispenser jar exchange, invoice) + corporate CTA [H].

**Distributor journey**: searches brand+distributorship (competitor fraud warnings prime scepticism) → distributor page → needs legitimacy PROOF above the form: Udyam registration PDF link, FSSAI licence, factory address, "we never charge application fees" statement (mirrors Bisleri's warning — turns competitor's defensive move into our trust asset) [O → H].

## 7. Conversion events to instrument (GA4-ready spec)

`whatsapp_click` {page, page_family, segment, city} · `phone_click` {page} · `form_submit` {form_type} · `pincode_check` {result: available|region|expansion} · `add_to_enquiry` {product} · `cart_checkout_click` {items} · `generate_lead` (form or WhatsApp, deduped). No event fires twice (dedupe by session+element). Full spec in deliverable 12.

## 8. What NOT to do

- No fake countdowns/pressure widgets (trust-destroying for a safety product).
- No interstitial popups (mobile UX + GBP quality guidelines).
- No generic "Submit" — every button names the outcome ("Get bulk quote").
- No adding CTAs to regulatory blog content beyond soft contact.
