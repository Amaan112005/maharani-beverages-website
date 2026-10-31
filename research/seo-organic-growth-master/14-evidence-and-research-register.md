# 14 — Evidence and Research Register

## Capability Register (Section 2 requirement)

### Skills discovered
| Skill | Scope | Used? |
|---|---|---|
| check-kimi-code-docs | Kimi Code product docs only | No — irrelevant to SEO research |
| update-config | Kimi Code config only | No — irrelevant |
| write-goal | Goal-mode objectives only | No — irrelevant |

**Honest finding:** the installed skill library contains NO specialist SEO/keyword/CRO research skills. No fabrication: this register states that plainly. All research was executed with the general toolset below.

### Tools available and actually used
| Tool | Used for |
|---|---|
| Python 3 + openpyxl | GSC Excel export analysis, keyword database, page inventory |
| Python + PIL | Image/asset verification |
| html5lib / lxml | Strict HTML validation (prior rounds, cited as evidence) |
| WebSearch | Market research, competitor discovery, Google documentation, consumer research, SERP observation |
| FetchURL | Primary-source reading (Google Search Central, competitor sites, regulatory sources) |
| Custom crawler (721 URLs, Vercel-semantics resolver) | Technical evidence (prior rounds) |
| CDP headless Chrome | Functional testing (prior rounds) |
| Local repo access | Full source inspection across 4 audit rounds |

### Data sources accessed
| Source | Detail |
|---|---|
| GSC export 2026-10-30 (xlsx) | 29 Jul–28 Oct 2026: 871 clicks, 35,475 impressions, Chart/Pages/Queries/Devices/Search-appearance sheets |
| GSC export 2026-08-19 (xlsx) | Earlier period export for trend comparison |
| Live production site | Post-launch validation 2026-10-31 |
| Official Google Search Central documentation | Fetched and cited per-claim |
| Competitor websites | Fetched directly |
| FSSAI/IS-14543 regulatory references | Via official-adjacent sources + existing site research |

### Data sources UNAVAILABLE (stated, not worked around)
| Source | Status |
|---|---|
| Live Google Search Console API/dashboard | No OAuth access — analysis limited to the two owner-provided exports |
| GA4 | Explicitly deferred by owner directive; no property exists |
| Paid SEO suites (Ahrefs, Semrush, Similarweb) | No subscription — search volumes are QUALITATIVE ( labelled in deliverable 05) |
| Real Google SERP scraping at Kolkata geo | WebSearch used as SERP proxy; observations labelled as such, not as geo-precise SERP captures |
| Consumer surveys / interviews | None conducted — personas are research-backed constructions with hypotheses labelled |
| Backlink crawlers (Ahrefs/Majestic/Moz) | Unavailable — backlink section is strategy-only, no profile claims |

### Evidence hierarchy used (per brief Section 16)
- **Tier 1:** GSC exports, Google Search Central pages, live site source, official competitor sites.
- **Tier 2:** Reputable market/industry publications found via search (cited individually).
- **Tier 3:** SERP observations via WebSearch, review-style sources, public discussions.

Every material claim in the deliverables carries an evidence class:
**[F]** verified fact · **[O]** observed market behaviour · **[R]** research-backed conclusion · **[H]** hypothesis requiring validation · **[U]** unknown.

## Source log (key sources; research date 2026-10-31 unless noted)

| # | Source | URL | Date | Class | Used in |
|---|---|---|---|---|---|
| 1 | GSC Performance export | local: ~/Downloads/...2026-10-30.xlsx | export 30 Oct 2026 | F | 01,05,06,07,13 |
| 2 | GSC Performance export | local: ~/Downloads/...2026-08-19.xlsx | export 19 Aug 2026 | F | 13 |
| 3 | Google Search Central — SEO Starter / Ranking | developers.google.com/search/docs | fetched 31 Oct 2026 | F | 01,04 |
| 4 | Google Search Central — Structured data intro | developers.google.com/search/docs/appearance/structured-data/intro | fetched 31 Oct 2026 | F | 04 |
| 5 | Google Search Central — AI features + SEO | developers.google.com/search/docs/appearance/ai-features | fetched 31 Oct 2026 | F | 01,15-equivalent section |
| 6 | FSSAI — packaged drinking water requirements | fssai.gov.in / regulations via search | fetched 31 Oct 2026 | F | 02,03 |
| 7 | Bisleri official site | bisleri.com | fetched 31 Oct 2026 | O | 03 |
| 8 | Kolkata/local supplier SERP observations | via WebSearch queries (logged in 03) | 31 Oct 2026 | O | 03 |
| 9 | Prior audit rounds 1–4 (this project) | repo history + session reports | Jul–Oct 2026 | F | 04,06 |

*Full per-claim sourcing appears inline in each deliverable. Limitations: WebSearch SERP proxy cannot reproduce Kolkata-localised SERPs exactly; where this matters, the claim is marked [O] with the query recorded rather than presented as a precise local SERP capture.*
