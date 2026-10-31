# 13 — Analytics Architecture

**Status:** architecture complete and partially LIVE (dataLayer events on 483 pages); GA4 itself remains DEFERRED per Rule 7 — no property, no placeholder ID, no install.

## Layers

```
User interaction
  └─ lead-events.js / pincode-checker.js  → window.dataLayer events   [LIVE]
  └─ (future) GA4 tag, loaded lazily post-load, id from owner           [GATED: OC-20]
        └─ GA4 key events → GA4 reports
              └─ monthly reconciliation with sales lead log (attribution reality-check)
```

Deliberately no GTM in phase 1: two lightweight custom layers cover the spec; GTM only when marketing tags multiply.

## Design principles

1. **Measurement-first naming** — events named in business language (`whatsapp_click`, not `cta_1`), parameters carry context (page_family, segment, cta_type).
2. **Zero duplicate events** — session+element dedupe in both live layers; `generate_lead` dedupes form→whatsapp sequences.
3. **Navigation-safe** — passive listeners, try/catch everywhere; instrumentation can never break a conversion.
4. **Deferred transport** — until GA4 lands, events accumulate in-page (no exfiltration, no cookies beyond existing, GDPR-light posture by construction).

## Consent & privacy notes (pre-install checklist for owner)

- GA4 with IP anonymisation + cookie consent banner if required by traffic profile; document retention settings.
- WhatsApp prefilled messages contain intent text only — no personal data collected by the site.
- Pincode checker logs pincode prefixes (first 2 digits) in analytics — area-level only.

## Dependencies for activation (owner)

GA4 Measurement ID + web stream (OC-20) → 5-minute change (audited: single generator template line + hand pages; activation documented in deliverable 12 spec of the master research package) → DebugView verification against the event table in `13-event-tracking-specification.csv`.
