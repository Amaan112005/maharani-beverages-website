# 12 — Analytics and Measurement Blueprint

**Status:** GA4 installation is deferred by owner directive. This is the implementation SPECIFICATION only — nothing is installed, no Measurement ID invented. **[F] facts from audits; spec items [H] until live.**

---

## 1. Measurement philosophy (per brief §14)

Rankings and traffic are means. The measured outcome chain: organic visit → contact event → qualified lead → customer. Every metric in this blueprint rolls up to that chain.

## 2. Event specification (GA4-ready)

| Event | Trigger | Parameters | Dedupe rule |
|---|---|---|---|
| `page_view` | automatic | — | default |
| `whatsapp_click` | any wa.me link click | page_url, page_family, segment, city, cta_position | 1/session/element |
| `phone_click` | tel: click | page_url, page_family | 1/session |
| `form_submit` | Formspree success | form_type (contact/bulk/distributor/careers), page_family | server-side via `fetch` response |
| `pincode_check` | checker result render | result (available/region/expansion), pincode_prefix (first 2 digits — not full PII) | log every check, dedupe analysis-side |
| `add_to_enquiry` | addToCart/addCustomToCart | product, unit, qty | per add |
| `cart_checkout_click` | cart WhatsApp send | items_count, total_qty | per checkout |
| `generate_lead` | form OR whatsapp with intent class | lead_type (household/office/b2b/distributor), source_page | cross-event dedupe: if form_submit then whatsapp within 10 min same session → one lead |
| `scroll_50` / `scroll_90` | depth | page_family | per page/session |

CTA-position and page_family params require the CTA architecture from deliverable 08 (each CTA tagged with data attributes at build time).

## 3. Implementation plan (for when GA4 is authorised)

1. Owner provides GA4 Measurement ID + web stream.
2. Replace `G-XXXXXXXXXX` placeholder (single generator template line + hand pages — audited: 486 files, one sed + regen) with the consent-aware loader (lazy-load after `load` event — existing pattern preserved).
3. Implement events via the existing inline JS layer (no GTM needed initially; migrate to GTM only when marketing tags multiply).
4. Mark `generate_lead` as a GA4 KEY EVENT; import nothing else as conversion.
5. WhatsApp number-level tracking already possible: wa.me links carry `text` — add a source tag inside prefilled messages ("via website") so sales can self-report source.

## 4. Attribution & lead-source discipline

- UTM convention (for any future paid/campaign use): `utm_source=google&utm_medium=organic` is implicit; external campaigns use `utm_campaign=YYYYMM-theme`. Never tag internal links.
- Sales-team feedback loop: WhatsApp-first sales logs lead source ("organic-20L-page") in a sheet → monthly reconciliation with GA4 key events (attribution reality-check).
- CRM: later-phase; a structured sheet beats no CRM (lead_type, source_page, date, outcome).

## 5. KPI dashboard specification (monthly, one page)

**Acquisition:** organic clicks, impressions, CTR, non-brand clicks share, near-me cluster clicks. **Behaviour:** landing-page engagement, pincode checks, scroll-90 on money pages. **Conversion:** whatsapp_click, phone_click, form_submit, generate_lead (by lead_type). **Commerce (manual until invoicing integration):** leads marked converted by sales. **Health:** index coverage (GSC), CWV field data (GSC CrUX), 404 rate. Baselines for every metric = the 2026-10-30 GSC export + first 30 days post-GA4.

## 6. Anti-patterns prohibited

No auto-tracking of every click as a lead; no duplicate events from template + inline handlers; no bot-inflated engagement metrics reported upward; no ranking reports as the primary KPI.
