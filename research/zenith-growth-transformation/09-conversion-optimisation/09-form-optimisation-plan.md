# Form Optimisation Plan

**Audit basis:** round-4 form inventory + Sprint-1 D-12.

## State
| Form | Fields | Honeypot | Autocomplete | Transport | Status |
|---|---|---|---|---|---|
| Homepage bulk-quote (Formspree) | 4 + gotcha | ✅ | ✅ (shipped) | Formspree | ✅ |
| Bulk page (Formspree) | 6 + gotcha | ✅ | ✅ (pre-existing) | Formspree | ✅ |
| Distributor (Formspree, dual-submit JS) | 5 + gotcha | ✅ | ✅ (shipped) | Formspree + WhatsApp redirect | ✅ |
| Contact (WhatsApp-routing handler) | 4 required | n/a (no server submit) | ✅ pre-existing | WhatsApp + success redirect | ✅ verified functional |
| Careers (WhatsApp-routing handler) | 8 required | n/a | partial | WhatsApp | ⚠ 8 fields — trim candidate |
| Enquiry cart | JS cart → WhatsApp checkout | n/a | n/a | WhatsApp | ✅ |

## Actions
1. Careers trim (8→6): merge location+role into one field; drop portfolio link to optional-inline. [Queued — next branch touch]
2. Universal: error messaging via inline validation (currently alert()-based on handlers). [Queued]
3. Post-GA4: form_submit + abandonment instrumentation per spec.
4. Rule: no form grows without a decision-register entry; every new field must justify itself against lead quality.
