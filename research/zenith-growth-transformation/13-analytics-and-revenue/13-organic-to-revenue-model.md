# 13 — Organic-to-Revenue Model (attribution design)

**Purpose:** connect the chain the brief demands (impressions → clicks → visits → trust → contact → qualified lead → order → repeat) without pretending to more precision than the data supports.

## The model (monthly)

```
GSC impressions (by cluster)
  × cluster CTR            → organic clicks
  × landing survival        → engaged visits (proxy until GA4: scroll/pincode events)
  × CTA engagement          → whatsapp_click + form_submit + phone_click
  × qualification           → generate_lead (lead_type split)
  × close rate (sales log)  → orders
  × avg order value + repeat rate → organic-attributed revenue
```

## Attribution honesty

- **Last non-direct click** by default; WhatsApp-initiated leads self-report source in the prefilled message ("I'm on your X page") — the strongest attribution signal we have, captured in the sales log.
- UTM reserved for future campaigns; internal links never tagged.
- Monthly reconciliation: GA4 `generate_lead` count vs sales-log lead count; variance >15% triggers an instrumentation audit rather than silent acceptance.
- Confidence labelling: click→visit numbers are [F] (GSC/GA4); visit→lead is [F] post-GA4; lead→order remains sales-reported [O] until invoicing integration (Month-12 review item).

## Revenue connection paths (in order of feasibility)

1. **Now:** sales-log lead counting (source self-reported) — zero tech, starts at interview.
2. **Month 2–3 (post-GA4):** lead counts + lead_type + source_page in GA4 vs log reconciliation.
3. **Month 6+:** order-value tagging in the sales log (manual per converted lead).
4. **Month 12 review:** invoicing/CRM integration decision with real cost-benefit data.

## Anti-gaming rules

Revenue targets never retro-justify traffic tactics; no channel gets credit for leads it can't evidence; "organic revenue" is reported only with the reconciliation note attached.
