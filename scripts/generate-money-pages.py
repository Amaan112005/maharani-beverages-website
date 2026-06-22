#!/usr/bin/env python3
"""Generate P0 money pages for Zenith Water SEO domination."""
import os
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

LOCALITIES_KOLKATA = [
    "Salt Lake", "Sector V", "Rajarhat", "New Town", "Ballygunge",
    "Park Street", "Behala", "Alipore", "Dum Dum", "Lake Town",
    "Baguiati", "Jadavpur", "Garia", "Tollygunge", "Esplanade"
]

LOCALITIES_HOWRAH = [
    "Howrah Station", "Shibpur", "Bally", "Liluah", "Belur",
    "Santragachi", "Andul", "Domjur", "Jagacha", "Uluberia", "Kona"
]

PRODUCTS = [
    {"size": "300ml", "name": "300ml Travel Bottle", "use": "Events, travel, retail"},
    {"size": "500ml", "name": "500ml Office Bottle", "use": "Offices, meetings, retail"},
    {"size": "1L", "name": "1L Home Bottle", "use": "Families, home use"},
    {"size": "2L", "name": "2L Family Pack", "use": "Families, hospitality"},
    {"size": "20L", "name": "20L Bulk Jar", "use": "Offices, factories, homes"},
]

WHO_WE_SERVE = [
    ("Offices", "Corporate parks and IT companies"),
    ("Hotels", "Hotels, guest houses and resorts"),
    ("Restaurants", "Restaurants, cafes and cloud kitchens"),
    ("Factories", "Manufacturing units and plants"),
    ("Warehouses", "Logistics and storage facilities"),
    ("Events", "Weddings, conferences and exhibitions"),
]

FAQS_COMMON = [
    ("Do you supply water jars in Kolkata?", "Yes, Zenith Water supplies 20-litre water jars across Kolkata and Howrah for offices, homes, factories and events."),
    ("Is Zenith Water FSSAI certified?", "Yes. Zenith Water is manufactured by Maharani Beverages LLP and holds a valid FSSAI license. Every unit follows BIS IS 14543 standards."),
    ("What is the minimum order quantity?", "We accept both small retail orders and large bulk contracts. Contact us for a customised quote based on your monthly consumption."),
    ("Do you offer same-day delivery?", "Same-day delivery is available for select localities and bulk corporate orders. Scheduled delivery is available across all service areas."),
    ("Which bottle sizes do you offer?", "We offer 300ml, 500ml, 1L, 2L bottles and 20-litre dispenser-compatible jars."),
    ("Can you supply water for events?", "Yes, we provide bulk water supply for weddings, conferences, exhibitions, banquets and corporate events."),
]


def build_faq_schema(questions):
    items = [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in questions
    ]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}, indent=2)


def build_faq_html(questions):
    return "\n              ".join(
        f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>'
        for q, a in questions
    )


def build_locality_links(localities):
    links = []
    for loc in localities:
        slug = loc.lower().replace(" ", "-")
        links.append(f'<a href="/packaged-drinking-water-{slug}" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid rgba(181,158,109,0.3);">{loc}</a>')
    return ", ".join(links)


def build_who_we_serve():
    cards = []
    for title, desc in WHO_WE_SERVE:
        cards.append(
            f'''<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.5rem; text-align: center;">
                <h4 style="color: white; font-family: var(--font-heading); font-size: 1.1rem; margin-bottom: 0.5rem;">{title}</h4>
                <p style="color: var(--color-muted); font-size: 0.85rem; line-height: 1.5;">{desc}</p>
            </div>'''
        )
    return "\n            ".join(cards)


def build_product_cards():
    cards = []
    for p in PRODUCTS:
        cards.append(
            f'''<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.5rem; text-align: center;">
                <div style="font-family: var(--font-heading); font-size: 1.8rem; color: white; margin-bottom: 0.5rem;">{p["size"]}</div>
                <div style="color: var(--color-accent); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0.75rem;">{p["name"]}</div>
                <p style="color: var(--color-muted); font-size: 0.85rem; line-height: 1.5;">{p["use"]}</p>
            </div>'''
        )
    return "\n            ".join(cards)


TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="author" content="Maharani Beverages LLP">
  <title>{title}</title>
  <meta name="description" content="{meta_description}">
  <link rel="canonical" href="https://maharanibeverages.com/{slug}">

  <meta property="og:type" content="website">
  <meta property="og:url" content="https://maharanibeverages.com/{slug}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_description}">
  <meta property="og:image" content="https://maharanibeverages.com/zenith_logo_compact.png">
  <meta property="og:site_name" content="Zenith Water">
  <meta property="og:locale" content="en_IN">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{og_description}">
  <meta name="twitter:image" content="https://maharanibeverages.com/zenith_logo_compact.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: blob: *; connect-src 'self' https://formspree.io; frame-src 'none'; object-src 'none;">

  <script type="application/ld+json">
  {faq_schema}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "name": "Maharani Beverages LLP",
        "alternateName": "Zenith Water",
        "url": "https://maharanibeverages.com",
        "telephone": "+918274837341",
        "email": "marketing@maharanibeverages.com",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "Ranihati Industrial Park, Mallick Bagan",
          "addressLocality": "Howrah",
          "addressRegion": "West Bengal",
          "postalCode": "711322",
          "addressCountry": "IN"
        }},
        "areaServed": [{city_list}],
        "sameAs": [
          "https://www.instagram.com/zenithwater",
          "https://www.facebook.com/zenithwater",
          "https://www.linkedin.com/company/zenith-water"
        ]
      }},
      {{
        "@type": "Service",
        "serviceType": "{service_type}",
        "provider": {{ "@type": "Organization", "name": "Maharani Beverages LLP" }},
        "areaServed": {{ "@type": "Place", "name": "{primary_city}" }},
        "description": "{service_schema_description}"
      }}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://maharanibeverages.com/" }},
      {{ "@type": "ListItem", "position": 2, "name": "{breadcrumb_parent}", "item": "https://maharanibeverages.com/{parent_slug}" }},
      {{ "@type": "ListItem", "position": 3, "name": "{breadcrumb_name}", "item": "https://maharanibeverages.com/{slug}" }}
    ]
  }}
  </script>

  <link rel="stylesheet" href="assets/css/variables.css">
  <link rel="stylesheet" href="assets/css/main.css">
  <link rel="stylesheet" href="assets/css/mobile-perfection.css?v=1.1">
  <style>.visually-hidden{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;}}</style>
  <style>
    .faq-item {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; margin-bottom: 1rem; overflow: hidden; }}
    .faq-q {{ padding: 1.5rem 2rem; cursor: pointer; color: white; font-weight: 700; user-select: none; }}
    .faq-a {{ padding: 0 2rem 2rem 2rem; color: var(--color-muted); line-height: 1.8; }}
    .footer-link {{ color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: color 0.3s, padding-left 0.3s; display: inline-block; }}
    .footer-link:hover {{ color: var(--color-accent); padding-left: 5px; }}
  </style>
</head>
<body>

  <!-- Header -->
  <header class="header" style="position: sticky; top: 0; z-index: 1000; background: rgba(8,14,32,0.95); backdrop-filter: blur(20px);">
    <nav class="container" style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 0;">
      <a href="/" aria-label="Zenith Water Home"><img decoding="async" src="zenith_logo_compact.png" alt="Zenith Water Logo" class="logo" style="width: 80px; height: auto;" width="80" height="66" loading="lazy"></a>
      <div style="display: flex; gap: 2rem; align-items: center;">
        <a href="/" style="color: rgba(255,255,255,0.7); text-decoration: none; font-weight: 600; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px;">Home</a>
        <a href="/{parent_slug}" style="color: rgba(255,255,255,0.7); text-decoration: none; font-weight: 600; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px;">{breadcrumb_parent}</a>
        <a href="/pages/bulk" style="color: rgba(255,255,255,0.7); text-decoration: none; font-weight: 600; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px;">Bulk Quote</a>
        <a href="/pages/contact" style="color: rgba(255,255,255,0.7); text-decoration: none; font-weight: 600; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px;">Contact</a>
      </div>
    </nav>
  </header>

  <main>
    <!-- Breadcrumb -->
    <div class="container" style="padding-top: 2rem;">
      <nav aria-label="breadcrumb" style="font-size: 0.7rem; color: var(--color-muted);">
        <a href="/" style="color: var(--color-muted); text-decoration: none;">Home</a>
        <span style="margin: 0 0.5rem;">/</span>
        <a href="/{parent_slug}" style="color: var(--color-muted); text-decoration: none;">{breadcrumb_parent}</a>
        <span style="margin: 0 0.5rem;">/</span>
        <span style="color: var(--color-accent);">{breadcrumb_name}</span>
      </nav>
    </div>

    <!-- Hero -->
    <section style="padding: 6rem 0 4rem; text-align: center; background: var(--color-bg);">
      <div class="container">
        <p style="color: var(--color-accent); font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 1.5rem;">{eyebrow}</p>
        <h1 style="font-family: var(--font-heading); font-size: clamp(2.5rem, 7vw, 4.5rem); color: white; line-height: 1.05; margin-bottom: 1.5rem;">{h1}</h1>
        <p style="color: var(--color-muted); font-size: 1.1rem; max-width: 700px; margin: 0 auto 2rem; line-height: 1.8;">{hero_subtitle}</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="/pages/bulk" class="btn-ultimate" style="background: var(--color-accent); color: var(--color-primary); border: none; padding: 1rem 2.5rem;">Get Bulk Quote</a>
          <a href="tel:+918274837341" class="btn-ultimate" style="padding: 1rem 2.5rem;">Call +91 82748 37341</a>
        </div>
      </div>
    </section>

    <!-- Trust Signals -->
    <section style="padding: 3rem 0; background: rgba(255,255,255,0.02); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; text-align: center;">
          <div><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🏆</div><div style="color: white; font-weight: 700; font-size: 0.9rem;">FSSAI Certified</div></div>
          <div><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">✓</div><div style="color: white; font-weight: 700; font-size: 0.9rem;">BIS IS 14543</div></div>
          <div><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🚚</div><div style="color: white; font-weight: 700; font-size: 0.9rem;">Bulk Supply</div></div>
          <div><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⚡</div><div style="color: white; font-weight: 700; font-size: 0.9rem;">Same Day Delivery</div></div>
        </div>
      </div>
    </section>

    <!-- Main Content -->
    <section style="padding: 6rem 0; background: var(--color-bg);">
      <div class="container">
        <div style="display: grid; grid-template-columns: 3fr 2fr; gap: 4rem;">
          <div style="color: var(--color-muted); line-height: 1.9;">

            <div style="margin-bottom: 4rem;">
              <h2 style="color: white; font-family: var(--font-heading); font-size: 2rem; margin-bottom: 1.5rem;">{section1_title}</h2>
              {section1_body}
            </div>

            <div style="margin-bottom: 4rem;">
              <h2 style="color: white; font-family: var(--font-heading); font-size: 2rem; margin-bottom: 1.5rem;">Who We Serve</h2>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem;">
                {who_we_serve}
              </div>
            </div>

            <div style="margin-bottom: 4rem;">
              <h2 style="color: white; font-family: var(--font-heading); font-size: 2rem; margin-bottom: 1.5rem;">Products Available</h2>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem;">
                {product_cards}
              </div>
            </div>

            <div style="margin-bottom: 4rem;">
              <h2 style="color: white; font-family: var(--font-heading); font-size: 2rem; margin-bottom: 1.5rem;">Delivery Areas</h2>
              <p style="margin-bottom: 1.5rem;">We supply packaged drinking water across {primary_city} including:</p>
              <p style="line-height: 2; margin-bottom: 1.5rem;">{locality_links}</p>
              <p>{coverage_footer}</p>
            </div>

            <div style="margin-bottom: 4rem;">
              <h2 style="color: white; font-family: var(--font-heading); font-size: 2rem; margin-bottom: 1.5rem;">Frequently Asked Questions</h2>
              {faq_html}
            </div>

          </div>

          <aside>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 2rem; position: sticky; top: 100px;">
              <h3 style="color: white; font-family: var(--font-heading); font-size: 1.5rem; margin-bottom: 1rem;">Request a Quote</h3>
              <p style="font-size: 0.9rem; margin-bottom: 1.5rem; opacity: 0.7;">Get bulk pricing for your home, office or business.</p>
              <a href="https://wa.me/918274837341?text={wa_text}" class="btn-ultimate" style="display: block; width: 100%; text-align: center; background: #25D366; border: none; margin-bottom: 1rem;">Order on WhatsApp</a>
              <a href="tel:+918274837341" class="btn-ultimate" style="display: block; width: 100%; text-align: center; margin-bottom: 1rem;">Call Now</a>
              <a href="/pages/bulk" class="btn-ultimate" style="display: block; width: 100%; text-align: center;">Bulk Enquiry Form</a>
              <p style="margin-top: 2rem; font-size: 0.75rem; color: var(--color-accent); text-transform: uppercase; letter-spacing: 2px;">Executive Line</p>
              <p style="color: white; font-weight: 800; font-size: 1.25rem;">+91 82748 37341</p>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <!-- Entity Reinforcement -->
    <section style="padding: 4rem 0; background: rgba(255,255,255,0.02); border-top: 1px solid rgba(255,255,255,0.05);">
      <div class="container" style="max-width: 900px; text-align: center;">
        <p style="color: var(--color-muted); line-height: 1.8; font-size: 1rem;">
          <strong style="color: white;">Zenith Water by Maharani Beverages LLP</strong> is a packaged drinking water manufacturer, bulk water supplier, corporate water supplier, office water supplier and hotel water supplier serving <strong style="color: white;">Kolkata and Howrah</strong>.
        </p>
      </div>
    </section>

    <!-- CTA Section -->
    <section style="padding: 6rem 0; text-align: center; background: var(--color-bg);">
      <div class="container">
        <h2 style="font-family: var(--font-heading); color: white; font-size: clamp(1.8rem, 4vw, 2.5rem); margin-bottom: 1.5rem;">Ready to Order?</h2>
        <p style="color: var(--color-muted); max-width: 600px; margin: 0 auto 2rem; line-height: 1.8;">Speak to our sales team for bulk pricing, delivery schedules and customised water supply plans.</p>
        <a href="/pages/bulk" class="btn-ultimate" style="background: var(--color-accent); color: var(--color-primary); border: none; padding: 1rem 3rem;">Get Your Bulk Quote</a>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer style="background: var(--section-dark); border-top: 1px solid rgba(255,255,255,0.08); padding: 5rem 0 3rem;">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 3rem; margin-bottom: 4rem;">
        <div>
          <a href="/"><img decoding="async" src="zenith_logo_compact.png" alt="Zenith Water Official Logo" loading="lazy" style="width: 120px; height: auto; margin-bottom: 1rem;" width="120" height="99"></a>
          <p style="color: rgba(255,255,255,0.6); font-size: 0.9rem; line-height: 1.7;">FSSAI certified packaged drinking water supplier in Kolkata & Howrah.</p>
        </div>
        <div>
          <h4 style="color: white; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem;">Products</h4>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.75rem;">
            <li><a href="/pages/product-300ml" class="footer-link">300ml Bottle</a></li>
            <li><a href="/pages/product-500ml" class="footer-link">500ml Bottle</a></li>
            <li><a href="/pages/product-1l" class="footer-link">1L Bottle</a></li>
            <li><a href="/pages/product-2l" class="footer-link">2L Bottle</a></li>
            <li><a href="/water-jar-supplier-kolkata" class="footer-link">20L Jar</a></li>
          </ul>
        </div>
        <div>
          <h4 style="color: white; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem;">Services</h4>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.75rem;">
            <li><a href="/corporate-water-supply-kolkata" class="footer-link">Corporate Water</a></li>
            <li><a href="/office-water-supply-kolkata" class="footer-link">Office Water</a></li>
            <li><a href="/hotel-water-supplier-kolkata" class="footer-link">Hotel Water</a></li>
            <li><a href="/industrial-water-supplier-kolkata" class="footer-link">Industrial Water</a></li>
            <li><a href="/event-water-supply-kolkata" class="footer-link">Event Water</a></li>
          </ul>
        </div>
        <div>
          <h4 style="color: white; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem;">Locations</h4>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.75rem;">
            <li><a href="/packaged-drinking-water-kolkata" class="footer-link">Kolkata</a></li>
            <li><a href="/packaged-drinking-water-howrah" class="footer-link">Howrah</a></li>
            <li><a href="/areas-we-serve" class="footer-link">Areas We Serve</a></li>
          </ul>
        </div>
      </div>
      <div style="border-top: 1px solid rgba(255,255,255,0.06); padding-top: 2rem; text-align: center;">
        <p style="color: rgba(255,255,255,0.4); font-size: 0.8rem;">&copy; 2026 Maharani Beverages LLP — Zenith Water. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="assets/js/aos.js" defer></script>
  <script src="assets/js/main.js" defer></script>
</body>
</html>
'''


def make_page(slug, title, h1, subtitle, meta, og, service_type, service_desc,
              section1_title, section1_body, parent_slug, parent_name,
              breadcrumb_name, eyebrow, city="Kolkata", both_cities=False,
              coverage_footer=None, extra_faqs=None):
    localities = LOCALITIES_KOLKATA + LOCALITIES_HOWRAH if both_cities else (LOCALITIES_HOWRAH if city == "Howrah" else LOCALITIES_KOLKATA)
    locality_links = build_locality_links(localities[:12])

    faqs = list(FAQS_COMMON)
    if extra_faqs:
        faqs.extend(extra_faqs)

    return TEMPLATE.format(
        title=title,
        meta_description=meta,
        slug=slug,
        og_title=og,
        og_description=meta[:150],
        service_type=service_type,
        primary_city=city,
        city_list='"Kolkata", "Howrah"' if both_cities else f'"{city}"',
        service_schema_description=service_desc,
        breadcrumb_parent=parent_name,
        parent_slug=parent_slug,
        breadcrumb_name=breadcrumb_name,
        eyebrow=eyebrow,
        h1=h1,
        hero_subtitle=subtitle,
        section1_title=section1_title,
        section1_body=section1_body,
        who_we_serve=build_who_we_serve(),
        product_cards=build_product_cards(),
        locality_links=locality_links,
        coverage_footer=coverage_footer or f'Custom delivery plans are available for bulk orders across {city}.',
        faq_schema=build_faq_schema(faqs),
        faq_html=build_faq_html(faqs),
        wa_text=f"Hello%20Zenith%2C%20I%20am%20interested%20in%20{slug.replace('-', '%20')}.%20Please%20share%20details."
    )


PAGES = [
    # PRODUCT CLUSTER
    {
        "slug": "water-jar-supplier-kolkata",
        "title": "Water Jar Supplier Kolkata | 20L Jar Delivery | Zenith",
        "h1": "Water Jar Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies FSSAI certified 20-litre water jars across Kolkata. Ideal for offices, homes, factories and events with scheduled delivery.",
        "meta": "Looking for a water jar supplier in Kolkata? Zenith Water delivers FSSAI certified 20-litre jars for offices, homes & factories. Call +91 82748 37341.",
        "og": "Water Jar Supplier Kolkata | Zenith Water",
        "service_type": "Water Jar Supply",
        "service_desc": "Water jar supplier in Kolkata providing 20-litre FSSAI certified packaged drinking water jars for offices, homes and industries.",
        "section1_title": "Reliable Water Jar Supply Across Kolkata",
        "section1_body": "<p>Our 20-litre water jars are the preferred choice for offices, factories, schools and homes across Kolkata. Each jar is sealed under hygienic conditions and passes through a 7-stage purification process including RO, UV and ozonation.</p><p style='margin-top:1.5rem;'>We offer scheduled delivery, dispenser-compatible jars and flexible monthly plans. Whether you need 5 jars or 500, Zenith scales with your requirement.</p>",
        "parent_slug": "packaged-drinking-water-kolkata",
        "parent_name": "Kolkata Hub",
        "breadcrumb_name": "Water Jar Supplier Kolkata",
        "eyebrow": "20L Water Jar Supply",
        "extra_faqs": [
            ("What is the price of a 20 litre water jar in Kolkata?", "Pricing depends on quantity and delivery frequency. Contact us for bulk rates and monthly subscription plans."),
            ("Do you provide water dispensers?", "Yes, we can arrange dispenser-compatible 20L jars and assist with dispenser placement for corporate clients."),
        ]
    },
    {
        "slug": "20-litre-water-jar-supplier-kolkata",
        "title": "20 Litre Water Jar Supplier Kolkata | Zenith Water",
        "h1": "20 Litre Water Jar Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Buy 20 litre water jars in Kolkata from Zenith Water. FSSAI certified, dispenser-compatible and delivered on schedule for offices and homes.",
        "meta": "Buy 20 litre water jars in Kolkata from Zenith Water. FSSAI certified, dispenser-compatible jars for offices & homes. Call +91 82748 37341.",
        "og": "20 Litre Water Jar Supplier Kolkata | Zenith Water",
        "service_type": "20 Litre Water Jar Supply",
        "service_desc": "20 litre water jar supplier in Kolkata delivering FSSAI certified dispenser-compatible jars to offices, homes and factories.",
        "section1_title": "20 Litre Jars for Every Need",
        "section1_body": "<p>Our 20-litre jars are designed for high-volume consumption. The sealed cap preserves freshness, while the sturdy handle makes replacement easy. Every jar is BIS IS 14543 compliant and processed through multi-stage purification.</p><p style='margin-top:1.5rem;'>We serve offices in Sector V, hotels near Park Street, factories in Howrah and residential complexes across Kolkata with punctual delivery.</p>",
        "parent_slug": "water-jar-supplier-kolkata",
        "parent_name": "Water Jar Supplier",
        "breadcrumb_name": "20 Litre Jar Supplier",
        "eyebrow": "Bulk Jar Specialist",
        "extra_faqs": [
            ("How many 20L jars do I need for my office?", "A typical 10-person office consumes 2-3 jars per week. We help you calculate based on headcount and usage."),
            ("Are your 20L jars reusable?", "Yes, our jars are returnable and sanitized before refilling to maintain hygiene standards."),
        ]
    },
    {
        "slug": "water-bottle-supplier-kolkata",
        "title": "Water Bottle Supplier Kolkata | 300ml to 2L | Zenith",
        "h1": "Water Bottle Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies 300ml, 500ml, 1L and 2L packaged drinking water bottles across Kolkata for retail, hospitality and events.",
        "meta": "Water bottle supplier in Kolkata. Zenith Water supplies 300ml, 500ml, 1L & 2L FSSAI certified bottles for offices, hotels & events. Call us.",
        "og": "Water Bottle Supplier Kolkata | Zenith Water",
        "service_type": "Water Bottle Supply",
        "service_desc": "Water bottle supplier in Kolkata offering 300ml, 500ml, 1L and 2L FSSAI certified packaged drinking water bottles.",
        "section1_title": "Packaged Drinking Water Bottles in All Sizes",
        "section1_body": "<p>From pocket-sized 300ml bottles for events to 2L family packs, Zenith Water supplies the full range of packaged drinking water bottles across Kolkata. Each bottle is sealed, labelled and quality-tested before dispatch.</p><p style='margin-top:1.5rem;'>We support retailers, restaurants, hotels, event organisers and corporate canteens with case-based bulk pricing and reliable delivery.</p>",
        "parent_slug": "packaged-drinking-water-kolkata",
        "parent_name": "Kolkata Hub",
        "breadcrumb_name": "Water Bottle Supplier Kolkata",
        "eyebrow": "Bottled Water Supply",
        "extra_faqs": [
            ("Can I order water bottles in bulk?", "Yes, we offer bulk case pricing for 300ml, 500ml, 1L and 2L bottles. Ideal for events, retail and hospitality."),
            ("Do you supply branded bottles for hotels?", "Yes, we supply standard Zenith branded bottles suitable for hotel rooms, restaurants and banquet service."),
        ]
    },
    {
        "slug": "mineral-water-supplier-kolkata",
        "title": "Mineral Water Supplier Kolkata | FSSAI Certified | Zenith",
        "h1": "Mineral Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water is a trusted mineral water supplier in Kolkata. FSSAI certified packaged drinking water delivered to homes, offices and businesses.",
        "meta": "Mineral water supplier in Kolkata. Zenith Water delivers FSSAI certified packaged drinking water for homes, offices & events. Call +91 82748 37341.",
        "og": "Mineral Water Supplier Kolkata | Zenith Water",
        "service_type": "Mineral Water Supply",
        "service_desc": "Mineral water supplier in Kolkata providing FSSAI certified packaged drinking water with balanced minerals for homes and businesses.",
        "section1_title": "Why Choose Zenith as Your Mineral Water Supplier",
        "section1_body": "<p>Our water retains essential minerals while removing impurities through RO, UV and ozonation. The result is clean, safe drinking water that tastes fresh and meets FSSAI and BIS standards.</p><p style='margin-top:1.5rem;'>We deliver across Kolkata and Howrah with flexible plans for homes, offices, hotels, hospitals and events.</p>",
        "parent_slug": "packaged-drinking-water-kolkata",
        "parent_name": "Kolkata Hub",
        "breadcrumb_name": "Mineral Water Supplier Kolkata",
        "eyebrow": "Certified Mineral Water",
        "extra_faqs": [
            ("Is Zenith mineral water or packaged drinking water?", "Zenith is packaged drinking water with essential minerals retained, processed through 7-stage purification and certified by FSSAI and BIS."),
            ("Do you deliver mineral water to homes?", "Yes, we provide home delivery of bottled mineral water across Kolkata and Howrah."),
        ]
    },
    {
        "slug": "water-can-supplier-kolkata",
        "title": "Water Can Supplier Kolkata | 20L Can Delivery | Zenith",
        "h1": "Water Can Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Order 20-litre water cans in Kolkata from Zenith Water. FSSAI certified, dispenser-friendly and delivered to offices, homes and factories.",
        "meta": "Water can supplier in Kolkata. Zenith Water delivers FSSAI certified 20L water cans for offices, homes & factories. Call +91 82748 37341.",
        "og": "Water Can Supplier Kolkata | Zenith Water",
        "service_type": "Water Can Supply",
        "service_desc": "Water can supplier in Kolkata delivering 20-litre FSSAI certified water cans for offices, homes and industrial use.",
        "section1_title": "20L Water Cans Delivered Across Kolkata",
        "section1_body": "<p>Water cans are essential for offices, factories and homes that use dispensers. Zenith supplies robust 20-litre cans with sealed caps and quality assurance.</p><p style='margin-top:1.5rem;'>Our delivery network covers Salt Lake, Sector V, Park Street, Ballygunge, Howrah Station, Shibpur and surrounding areas with scheduled drops.</p>",
        "parent_slug": "water-jar-supplier-kolkata",
        "parent_name": "Water Jar Supplier",
        "breadcrumb_name": "Water Can Supplier Kolkata",
        "eyebrow": "20L Water Can Supply",
        "extra_faqs": [
            ("What is the difference between water jar and water can?", "Both are 20-litre containers for dispensers. 'Can' is a common term in offices; we supply both jars and cans with the same quality standards."),
            ("How do I place a recurring order for water cans?", "Contact our sales team to set up a weekly or bi-weekly delivery schedule tailored to your consumption."),
        ]
    },
    {
        "slug": "packaged-drinking-water-jar-kolkata",
        "title": "Packaged Drinking Water Jar Kolkata | 20L Delivery | Zenith",
        "h1": "Packaged Drinking Water Jar in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Buy packaged drinking water jars in Kolkata from Zenith Water. 20L FSSAI certified jars for offices, homes, hotels and factories.",
        "meta": "Packaged drinking water jar supplier in Kolkata. Zenith Water delivers 20L FSSAI certified jars for offices & homes. Call +91 82748 37341.",
        "og": "Packaged Drinking Water Jar Kolkata | Zenith Water",
        "service_type": "Packaged Drinking Water Jar Supply",
        "service_desc": "Packaged drinking water jar supplier in Kolkata providing 20-litre FSSAI certified jars for offices, homes and industries.",
        "section1_title": "Certified Packaged Drinking Water Jars",
        "section1_body": "<p>Our 20-litre packaged drinking water jars are the standard for safe hydration in Kolkata offices and homes. Each jar undergoes multi-stage purification and is sealed immediately after filling to prevent contamination.</p><p style='margin-top:1.5rem;'>We offer single-jar retail orders as well as bulk monthly subscriptions with priority delivery.</p>",
        "parent_slug": "packaged-drinking-water-kolkata",
        "parent_name": "Kolkata Hub",
        "breadcrumb_name": "Packaged Drinking Water Jar",
        "eyebrow": "20L Packaged Water Jar",
        "extra_faqs": [
            ("Is packaged drinking water jar safe?", "Yes, when sourced from an FSSAI certified supplier like Zenith, 20L jars are safe, hygienic and regularly tested."),
            ("Can I get same-day jar delivery?", "Same-day delivery is available in select zones for bulk orders. Contact us to confirm coverage for your pincode."),
        ]
    },

    # CORPORATE CLUSTER
    {
        "slug": "corporate-water-supply-kolkata",
        "title": "Corporate Water Supply Kolkata | Office Water Delivery | Zenith",
        "h1": "Corporate Water Supply in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water provides corporate water supply across Kolkata. Scheduled delivery, bulk pricing and FSSAI certified water for offices and business parks.",
        "meta": "Corporate water supply in Kolkata. Zenith Water delivers FSSAI certified packaged drinking water to offices & business parks. Call +91 82748 37341.",
        "og": "Corporate Water Supply Kolkata | Zenith Water",
        "service_type": "Corporate Water Supply",
        "service_desc": "Corporate water supply service in Kolkata providing FSSAI certified packaged drinking water to offices, business parks and corporate campuses.",
        "section1_title": "Corporate Water Solutions for Kolkata Businesses",
        "section1_body": "<p>Keep your employees hydrated with scheduled corporate water delivery from Zenith. We supply 20-litre jars and bottled water to offices, IT parks, co-working spaces and corporate campuses across Kolkata and Howrah.</p><p style='margin-top:1.5rem;'>Our corporate plans include GST invoicing, dedicated account management, flexible payment terms and priority support.</p>",
        "parent_slug": "kolkata-water-supply",
        "parent_name": "Kolkata Water Supply",
        "breadcrumb_name": "Corporate Water Supply",
        "eyebrow": "B2B Water Supply",
        "extra_faqs": [
            ("Do you provide corporate water supply with GST invoice?", "Yes, we provide GST-compliant invoices for all corporate orders."),
            ("Can you deliver daily to our office?", "Yes, we offer daily, alternate-day and weekly delivery schedules based on your office size and consumption."),
        ]
    },
    {
        "slug": "office-water-supply-kolkata",
        "title": "Office Water Supply Kolkata | 20L Jar Delivery | Zenith",
        "h1": "Office Water Supply in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water delivers packaged drinking water to offices across Kolkata. 20L jars, 500ml bottles and scheduled supply for workplaces of all sizes.",
        "meta": "Office water supply in Kolkata. Zenith Water delivers 20L jars & bottled water to offices across Kolkata. FSSAI certified. Call +91 82748 37341.",
        "og": "Office Water Supply Kolkata | Zenith Water",
        "service_type": "Office Water Supply",
        "service_desc": "Office water supply in Kolkata providing 20-litre jars and bottled water to workplaces with scheduled delivery and bulk pricing.",
        "section1_title": "Hassle-Free Office Water Supply",
        "section1_body": "<p>Never run out of drinking water at work. Zenith supplies offices across Kolkata with 20-litre jars for dispensers and 500ml bottles for meetings and guests. Our delivery team follows a fixed schedule so your pantry stays stocked.</p><p style='margin-top:1.5rem;'>We serve small offices, mid-size companies and large corporate campuses with scalable plans.</p>",
        "parent_slug": "corporate-water-supply-kolkata",
        "parent_name": "Corporate Water Supply",
        "breadcrumb_name": "Office Water Supply",
        "eyebrow": "Workplace Hydration",
        "extra_faqs": [
            ("How many jars does a 20-person office need?", "A 20-person office typically needs 4-6 twenty-litre jars per week. We adjust quantities based on actual consumption."),
            ("Do you supply water for office meetings?", "Yes, we supply 300ml and 500ml bottles perfect for boardrooms, conferences and client meetings."),
        ]
    },
    {
        "slug": "commercial-water-supplier-kolkata",
        "title": "Commercial Water Supplier Kolkata | Business Water | Zenith",
        "h1": "Commercial Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water is a commercial water supplier in Kolkata. FSSAI certified packaged drinking water for businesses, institutions and commercial complexes.",
        "meta": "Commercial water supplier in Kolkata. Zenith Water supplies FSSAI certified packaged drinking water to businesses & institutions. Call us.",
        "og": "Commercial Water Supplier Kolkata | Zenith Water",
        "service_type": "Commercial Water Supply",
        "service_desc": "Commercial water supplier in Kolkata delivering FSSAI certified packaged drinking water to businesses, institutions and commercial complexes.",
        "section1_title": "Commercial Water Supply You Can Rely On",
        "section1_body": "<p>Commercial establishments need consistent, compliant water supply. Zenith delivers to retail stores, malls, educational institutions, gyms, salons and commercial complexes across Kolkata with documented quality assurance.</p><p style='margin-top:1.5rem;'>Our commercial clients benefit from volume discounts, scheduled deliveries and single-point invoicing.</p>",
        "parent_slug": "kolkata-water-supply",
        "parent_name": "Kolkata Water Supply",
        "breadcrumb_name": "Commercial Water Supplier",
        "eyebrow": "Business Water Supply",
        "extra_faqs": [
            ("Do you supply water to retail stores?", "Yes, we supply packaged drinking water bottles to retail stores, kirana shops and supermarkets across Kolkata."),
            ("What documents do you provide for commercial orders?", "We provide FSSAI certificate copy, GST invoice and delivery challan for all commercial orders."),
        ]
    },
    {
        "slug": "industrial-water-supplier-kolkata",
        "title": "Industrial Water Supplier Kolkata | Factory Water | Zenith",
        "h1": "Industrial Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to industries and factories across Kolkata. Bulk 20L jars, scheduled delivery and FSSAI certification.",
        "meta": "Industrial water supplier in Kolkata. Zenith Water delivers FSSAI certified packaged drinking water to factories & industrial units. Call us.",
        "og": "Industrial Water Supplier Kolkata | Zenith Water",
        "service_type": "Industrial Water Supply",
        "service_desc": "Industrial water supplier in Kolkata providing bulk packaged drinking water to factories, plants and industrial estates.",
        "section1_title": "Bulk Water Supply for Industries",
        "section1_body": "<p>Factories and industrial units require high-volume drinking water for workers, canteens and visitors. Zenith supplies 20-litre jars and bottled water in bulk with scheduled drops and quality documentation.</p><p style='margin-top:1.5rem;'>We serve industrial belts across Kolkata and Howrah including Domjur, Jagacha, Uluberia, Kona and Ranihati.</p>",
        "parent_slug": "kolkata-water-supply",
        "parent_name": "Kolkata Water Supply",
        "breadcrumb_name": "Industrial Water Supplier",
        "eyebrow": "Factory Water Supply",
        "extra_faqs": [
            ("Do you supply water for factory labour camps?", "Yes, we provide bulk 20L jar supply for labour camps, construction sites and factory canteens."),
            ("Can you handle large daily volumes?", "Yes, we can supply hundreds of jars per day for large industrial clients with dedicated logistics."),
        ]
    },
    {
        "slug": "factory-water-supplier-kolkata",
        "title": "Factory Water Supplier Kolkata | Bulk Jar Delivery | Zenith",
        "h1": "Factory Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water is a factory water supplier in Kolkata. Bulk 20L jars and bottled water for manufacturing units with scheduled delivery.",
        "meta": "Factory water supplier in Kolkata. Zenith Water delivers bulk 20L jars & bottles to manufacturing units. FSSAI certified. Call +91 82748 37341.",
        "og": "Factory Water Supplier Kolkata | Zenith Water",
        "service_type": "Factory Water Supply",
        "service_desc": "Factory water supplier in Kolkata delivering bulk packaged drinking water to manufacturing units and industrial plants.",
        "section1_title": "Water Supply for Manufacturing Units",
        "section1_body": "<p>Manufacturing floors need reliable drinking water for workers. Zenith supplies factories across Kolkata with bulk 20-litre jars and bottled water, ensuring compliance with workplace safety and hygiene standards.</p><p style='margin-top:1.5rem;'>We align delivery schedules with shift timings and offer monthly billing for ease of accounting.</p>",
        "parent_slug": "industrial-water-supplier-kolkata",
        "parent_name": "Industrial Water Supplier",
        "breadcrumb_name": "Factory Water Supplier",
        "eyebrow": "Manufacturing Water",
        "extra_faqs": [
            ("What is the minimum order for factory water supply?", "We accept factory orders starting from 20 jars per day. Larger volumes receive preferential bulk pricing."),
            ("Do you deliver during factory working hours?", "Yes, we coordinate delivery timings with your factory schedule, including early morning or evening slots."),
        ]
    },
    {
        "slug": "warehouse-water-supplier-kolkata",
        "title": "Warehouse Water Supplier Kolkata | Bulk Water | Zenith",
        "h1": "Warehouse Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to warehouses and logistics hubs across Kolkata. Bulk jars and bottles with reliable delivery.",
        "meta": "Warehouse water supplier in Kolkata. Zenith Water delivers bulk packaged drinking water to warehouses & logistics hubs. Call +91 82748 37341.",
        "og": "Warehouse Water Supplier Kolkata | Zenith Water",
        "service_type": "Warehouse Water Supply",
        "service_desc": "Warehouse water supplier in Kolkata providing bulk packaged drinking water to logistics hubs, warehouses and distribution centres.",
        "section1_title": "Hydration Solutions for Warehouses",
        "section1_body": "<p>Warehouse staff work long shifts and need constant access to safe drinking water. Zenith supplies 20-litre jars and 500ml bottles to warehouses and logistics parks across Kolkata with bulk pricing.</p><p style='margin-top:1.5rem;'>Our delivery network covers major logistics corridors including Rajarhat, New Town, Kona and Domjur.</p>",
        "parent_slug": "industrial-water-supplier-kolkata",
        "parent_name": "Industrial Water Supplier",
        "breadcrumb_name": "Warehouse Water Supplier",
        "eyebrow": "Logistics Water Supply",
        "extra_faqs": [
            ("Do you supply water to e-commerce warehouses?", "Yes, we supply packaged drinking water to e-commerce, 3PL and cold storage warehouses across Kolkata."),
            ("Can you deliver to warehouse loading docks?", "Yes, our delivery team can drop water at designated loading docks or storage areas as per your instructions."),
        ]
    },
    {
        "slug": "business-park-water-supplier-kolkata",
        "title": "Business Park Water Supplier Kolkata | Zenith Water",
        "h1": "Business Park Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to business parks across Kolkata. Multiple tenants, single vendor, scheduled delivery.",
        "meta": "Business park water supplier in Kolkata. Zenith Water delivers FSSAI certified water to multi-tenant business parks. Call +91 82748 37341.",
        "og": "Business Park Water Supplier Kolkata | Zenith Water",
        "service_type": "Business Park Water Supply",
        "service_desc": "Business park water supplier in Kolkata delivering packaged drinking water to multi-tenant commercial parks and IT centres.",
        "section1_title": "Single Vendor for Entire Business Parks",
        "section1_body": "<p>Business parks with multiple tenants need a reliable water vendor. Zenith serves entire business parks in Salt Lake, Sector V, Rajarhat and New Town with consolidated billing and dedicated delivery routes.</p><p style='margin-top:1.5rem;'>We supply 20L jars for common areas and bottled water for individual offices.</p>",
        "parent_slug": "corporate-water-supply-kolkata",
        "parent_name": "Corporate Water Supply",
        "breadcrumb_name": "Business Park Water Supplier",
        "eyebrow": "Business Park Supply",
        "extra_faqs": [
            ("Can you supply multiple tenants in one business park?", "Yes, we can deliver to multiple offices within the same business park with separate or consolidated invoicing."),
            ("Do you provide water for business park cafeterias?", "Yes, we supply both 20L jars and bottled water for cafeterias, food courts and common areas."),
        ]
    },
    {
        "slug": "it-company-water-supplier-kolkata",
        "title": "IT Company Water Supplier Kolkata | Office Water | Zenith",
        "h1": "IT Company Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to IT companies in Kolkata. 20L jars, meeting bottles and scheduled pantry delivery.",
        "meta": "IT company water supplier in Kolkata. Zenith Water delivers FSSAI certified water to software offices & IT parks. Call +91 82748 37341.",
        "og": "IT Company Water Supplier Kolkata | Zenith Water",
        "service_type": "IT Company Water Supply",
        "service_desc": "IT company water supplier in Kolkata providing packaged drinking water to software companies, IT parks and tech offices.",
        "section1_title": "Water Supply for IT Offices",
        "section1_body": "<p>IT companies in Salt Lake, Sector V and New Town trust Zenith for scheduled drinking water delivery. We provide 20L jars for pantry dispensers and 500ml bottles for conference rooms and client meetings.</p><p style='margin-top:1.5rem;'>Our service includes online coordination, flexible timing and professional delivery staff.</p>",
        "parent_slug": "corporate-water-supply-kolkata",
        "parent_name": "Corporate Water Supply",
        "breadcrumb_name": "IT Company Water Supplier",
        "eyebrow": "Tech Office Water",
        "extra_faqs": [
            ("Do you supply water to startups and small IT offices?", "Yes, we cater to startups, SMEs and large IT enterprises with flexible order sizes."),
            ("Can delivery happen outside 9-5 hours?", "Yes, we can schedule early morning or evening deliveries to match your office timings."),
        ]
    },

    # INDUSTRY CLUSTER
    {
        "slug": "hotel-water-supplier-kolkata",
        "title": "Hotel Water Supplier Kolkata | Bottled Water for Hotels | Zenith",
        "h1": "Hotel Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to hotels across Kolkata. In-room bottles, banquet supply and 20L jars for staff areas.",
        "meta": "Hotel water supplier in Kolkata. Zenith Water supplies FSSAI certified bottled water to hotels, guest houses & resorts. Call +91 82748 37341.",
        "og": "Hotel Water Supplier Kolkata | Zenith Water",
        "service_type": "Hotel Water Supply",
        "service_desc": "Hotel water supplier in Kolkata providing FSSAI certified packaged drinking water to hotels, guest houses and resorts.",
        "section1_title": "Water Supply for Hotels and Hospitality",
        "section1_body": "<p>Hotels need premium bottled water for guest rooms, restaurants, banquets and staff areas. Zenith supplies hotels across Kolkata with 300ml, 500ml, 1L and 2L bottles plus 20L jars for back-of-house use.</p><p style='margin-top:1.5rem;'>We serve boutique hotels near Park Street, business hotels in Salt Lake and banquet venues across the city.</p>",
        "parent_slug": "kolkata-water-supply",
        "parent_name": "Kolkata Water Supply",
        "breadcrumb_name": "Hotel Water Supplier",
        "eyebrow": "Hospitality Water",
        "extra_faqs": [
            ("Do you supply water for hotel banquets?", "Yes, we provide bulk bottled water for hotel banquets, weddings and corporate events."),
            ("Can you match hotel branding requirements?", "We supply standard Zenith branded bottles. Custom labelling can be discussed for large volumes."),
        ]
    },
    {
        "slug": "restaurant-water-supplier-kolkata",
        "title": "Restaurant Water Supplier Kolkata | Bottled Water | Zenith",
        "h1": "Restaurant Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to restaurants, cafes and cloud kitchens across Kolkata. 500ml, 1L bottles and 20L jars.",
        "meta": "Restaurant water supplier in Kolkata. Zenith Water supplies FSSAI certified bottled water to restaurants, cafes & cloud kitchens. Call us.",
        "og": "Restaurant Water Supplier Kolkata | Zenith Water",
        "service_type": "Restaurant Water Supply",
        "service_desc": "Restaurant water supplier in Kolkata delivering packaged drinking water to restaurants, cafes and cloud kitchens.",
        "section1_title": "Water Supply for Restaurants and Cafes",
        "section1_body": "<p>Restaurants need a steady supply of bottled water for dine-in guests, takeaway orders and kitchen use. Zenith supplies 500ml and 1L bottles for tables plus 20L jars for cooking and staff hydration.</p><p style='margin-top:1.5rem;'>We deliver daily to restaurants in Park Street, Ballygunge, Salt Lake, New Town and across Kolkata.</p>",
        "parent_slug": "hotel-water-supplier-kolkata",
        "parent_name": "Hotel Water Supplier",
        "breadcrumb_name": "Restaurant Water Supplier",
        "eyebrow": "F&B Water Supply",
        "extra_faqs": [
            ("What bottle size is best for restaurants?", "500ml bottles are ideal for dine-in tables, while 20L jars work well for kitchen and staff use."),
            ("Do you offer daily delivery to restaurants?", "Yes, we offer daily and alternate-day delivery schedules for high-volume restaurant clients."),
        ]
    },
    {
        "slug": "hospital-water-supplier-kolkata",
        "title": "Hospital Water Supplier Kolkata | Safe Drinking Water | Zenith",
        "h1": "Hospital Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to hospitals, clinics and diagnostic centres across Kolkata. FSSAI certified and hygienically sealed.",
        "meta": "Hospital water supplier in Kolkata. Zenith Water delivers FSSAI certified packaged drinking water to hospitals & clinics. Call +91 82748 37341.",
        "og": "Hospital Water Supplier Kolkata | Zenith Water",
        "service_type": "Hospital Water Supply",
        "service_desc": "Hospital water supplier in Kolkata providing FSSAI certified packaged drinking water to hospitals, clinics and diagnostic centres.",
        "section1_title": "Safe Water for Healthcare Facilities",
        "section1_body": "<p>Hospitals and clinics require the highest standards of water safety. Zenith supplies FSSAI certified packaged drinking water in sealed bottles and jars to healthcare facilities across Kolkata.</p><p style='margin-top:1.5rem;'>We maintain batch records, follow hygienic handling protocols and offer scheduled delivery for patient areas, canteens and staff rooms.</p>",
        "parent_slug": "kolkata-water-supply",
        "parent_name": "Kolkata Water Supply",
        "breadcrumb_name": "Hospital Water Supplier",
        "eyebrow": "Healthcare Water",
        "extra_faqs": [
            ("Is your water safe for hospital use?", "Yes, our packaged drinking water is FSSAI certified, BIS compliant and processed through 7-stage purification."),
            ("Do you supply small clinics?", "Yes, we supply both small clinics and large hospitals with flexible order sizes."),
        ]
    },
    {
        "slug": "school-water-supplier-kolkata",
        "title": "School Water Supplier Kolkata | Safe Water for Students | Zenith",
        "h1": "School Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to schools and educational institutions across Kolkata. Safe, certified and affordable.",
        "meta": "School water supplier in Kolkata. Zenith Water delivers FSSAI certified packaged drinking water to schools & institutions. Call +91 82748 37341.",
        "og": "School Water Supplier Kolkata | Zenith Water",
        "service_type": "School Water Supply",
        "service_desc": "School water supplier in Kolkata providing FSSAI certified packaged drinking water to schools, colleges and educational institutions.",
        "section1_title": "Trusted Water Supply for Schools",
        "section1_body": "<p>Schools need safe, affordable drinking water for students and staff. Zenith supplies 500ml bottles and 20L jars to schools across Kolkata with quality certificates and reliable delivery.</p><p style='margin-top:1.5rem;'>We understand institutional procurement processes and provide GST invoices and compliance documents.</p>",
        "parent_slug": "kolkata-water-supply",
        "parent_name": "Kolkata Water Supply",
        "breadcrumb_name": "School Water Supplier",
        "eyebrow": "Institutional Water",
        "extra_faqs": [
            ("Do you supply water for school events?", "Yes, we provide bulk bottled water for school events, sports days and excursions."),
            ("Can you provide quality certificates?", "Yes, we provide FSSAI and BIS compliance documents for institutional orders."),
        ]
    },
    {
        "slug": "college-water-supplier-kolkata",
        "title": "College Water Supplier Kolkata | Campus Water Supply | Zenith",
        "h1": "College Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to colleges and universities across Kolkata. Bulk jars and bottles for campuses.",
        "meta": "College water supplier in Kolkata. Zenith Water delivers FSSAI certified packaged drinking water to colleges & campuses. Call +91 82748 37341.",
        "og": "College Water Supplier Kolkata | Zenith Water",
        "service_type": "College Water Supply",
        "service_desc": "College water supplier in Kolkata providing bulk packaged drinking water to colleges, universities and campuses.",
        "section1_title": "Campus-Wide Water Supply",
        "section1_body": "<p>Colleges and universities need high-volume water supply for classrooms, hostels, canteens and events. Zenith supplies 20L jars and bottled water across Kolkata campuses with scheduled delivery.</p><p style='margin-top:1.5rem;'>We serve institutions in Jadavpur, Salt Lake, Rajarhat and other education hubs.</p>",
        "parent_slug": "school-water-supplier-kolkata",
        "parent_name": "School Water Supplier",
        "breadcrumb_name": "College Water Supplier",
        "eyebrow": "Campus Water",
        "extra_faqs": [
            ("Do you supply water for college hostels?", "Yes, we supply 20L jars and bottles to college hostels, canteens and common areas."),
            ("Can you handle large campus events?", "Yes, we can supply bulk bottled water for college fests, seminars and sports events."),
        ]
    },
    {
        "slug": "corporate-event-water-supplier-kolkata",
        "title": "Corporate Event Water Supplier Kolkata | Zenith Water",
        "h1": "Corporate Event Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to corporate events, conferences and seminars across Kolkata. 300ml and 500ml bottles.",
        "meta": "Corporate event water supplier in Kolkata. Zenith Water delivers bottled water for conferences, seminars & corporate events. Call us.",
        "og": "Corporate Event Water Supplier Kolkata | Zenith Water",
        "service_type": "Corporate Event Water Supply",
        "service_desc": "Corporate event water supplier in Kolkata providing packaged drinking water bottles for conferences, seminars and business events.",
        "section1_title": "Water for Corporate Events and Conferences",
        "section1_body": "<p>Corporate events, AGMs, product launches and conferences need branded hydration. Zenith supplies 300ml and 500ml bottled water for corporate events across Kolkata with on-time delivery to the venue.</p><p style='margin-top:1.5rem;'>We coordinate delivery based on guest count and event timing.</p>",
        "parent_slug": "event-water-supply-kolkata",
        "parent_name": "Event Water Supply",
        "breadcrumb_name": "Corporate Event Water Supplier",
        "eyebrow": "Event Hydration",
        "extra_faqs": [
            ("How much water do I need for a 100-person event?", "Plan for 1-2 bottles per guest. We recommend 150 bottles for a 100-person half-day event."),
            ("Can you deliver directly to the event venue?", "Yes, we deliver directly to event venues across Kolkata including hotels, convention centres and offices."),
        ]
    },
    {
        "slug": "construction-site-water-supplier-kolkata",
        "title": "Construction Site Water Supplier Kolkata | Zenith Water",
        "h1": "Construction Site Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to construction sites and labour camps across Kolkata. Bulk 20L jars with daily delivery.",
        "meta": "Construction site water supplier in Kolkata. Zenith Water delivers bulk 20L jars to construction sites & labour camps. Call +91 82748 37341.",
        "og": "Construction Site Water Supplier Kolkata | Zenith Water",
        "service_type": "Construction Site Water Supply",
        "service_desc": "Construction site water supplier in Kolkata providing bulk 20-litre packaged drinking water jars to construction sites and labour camps.",
        "section1_title": "Bulk Water for Construction Sites",
        "section1_body": "<p>Construction workers need constant access to safe drinking water. Zenith supplies 20-litre jars in bulk to construction sites and labour camps across Kolkata and Howrah with daily or alternate-day delivery.</p><p style='margin-top:1.5rem;'>We offer competitive bulk rates and can scale supply as your workforce grows.</p>",
        "parent_slug": "industrial-water-supplier-kolkata",
        "parent_name": "Industrial Water Supplier",
        "breadcrumb_name": "Construction Site Water Supplier",
        "eyebrow": "Site Water Supply",
        "extra_faqs": [
            ("Do you deliver to remote construction sites?", "Yes, we deliver to construction sites across Kolkata, Howrah and surrounding areas including Rajarhat, New Town and Domjur."),
            ("What is the rate for 100 jars per day?", "We offer special bulk rates for high-volume daily orders. Contact us for a customised quote."),
        ]
    },
    {
        "slug": "manufacturing-plant-water-supplier-kolkata",
        "title": "Manufacturing Plant Water Supplier Kolkata | Zenith Water",
        "h1": "Manufacturing Plant Water Supplier in <span style='color: var(--color-accent);'>Kolkata</span>",
        "subtitle": "Zenith Water supplies packaged drinking water to manufacturing plants across Kolkata. Bulk jars and bottles for workers and visitors.",
        "meta": "Manufacturing plant water supplier in Kolkata. Zenith Water delivers FSSAI certified water to factories & plants. Call +91 82748 37341.",
        "og": "Manufacturing Plant Water Supplier Kolkata | Zenith Water",
        "service_type": "Manufacturing Plant Water Supply",
        "service_desc": "Manufacturing plant water supplier in Kolkata providing bulk packaged drinking water to factories and production facilities.",
        "section1_title": "Water Supply for Manufacturing Plants",
        "section1_body": "<p>Manufacturing plants require reliable drinking water for production staff, supervisors and visitors. Zenith supplies 20L jars and bottled water to plants across Kolkata's industrial belt with quality documentation.</p><p style='margin-top:1.5rem;'>We align deliveries with plant shifts and provide monthly consolidated invoices.</p>",
        "parent_slug": "factory-water-supplier-kolkata",
        "parent_name": "Factory Water Supplier",
        "breadcrumb_name": "Manufacturing Plant Water Supplier",
        "eyebrow": "Plant Water Supply",
        "extra_faqs": [
            ("Can you supply water for 24x7 manufacturing units?", "Yes, we can arrange multiple daily deliveries for round-the-clock manufacturing operations."),
            ("Do you provide quality test reports?", "Yes, we can share batch-wise quality records and compliance certificates for manufacturing plant orders."),
        ]
    },
]


def generate():
    generated = []
    for page in PAGES:
        content = make_page(**page)
        path = ROOT / f"{page['slug']}.html"
        path.write_text(content, encoding='utf-8')
        generated.append(page['slug'])
        print(f"Created {path}")
    return generated


if __name__ == '__main__':
    generate()
