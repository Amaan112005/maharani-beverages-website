# 04 — Search Intent Taxonomy (as classified in the keyword engine)

| Intent class | Definition | Example | Funnel | Value weight |
|---|---|---|---|---|
| local-nearme | proximity-led discovery | "water delivery near me" | bottom | 5 |
| transactional | ordering action | "order water online 20l" | bottom | 5 |
| commercial-price | cost comparison before contact | "20 litre water jar price kolkata" | bottom | 5 |
| product | size/format-led | "mineral water 20 litre" | bottom | 4 |
| local-geo | city-named service | "water supply howrah" | bottom | 4 |
| b2b | organisational supply | "office water supply kolkata" | mid | 5 |
| comparison | brand evaluation | "kinley vs bisleri" | mid | 3 |
| informational-regulatory | standards/verification | "is 14543" | top | 2 |
| informational-general | category education | "benefits of drinking water" | top | 1 |

Classification rules live in the master analysis script; the full 1,000-query classification is `data/keyword-database.csv`. Language register (formal vs everyday) is a cross-cutting axis — see can-vs-jar article for the bridge pattern.
