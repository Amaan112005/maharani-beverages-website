#!/usr/bin/env python3
"""Generate keyword-specific landing pages for Zenith Water SEO architecture."""
import os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Base template derived from packaged-drinking-water-kolkata.html
TEMPLATE = '''<!DOCTYPE html>
<html lang="en">

<head>
  <link rel="icon" type="image/png" href="https://maharanibeverages.com/zenith_logo_compact.png"> 
  <link rel="shortcut icon" href="https://maharanibeverages.com/zenith_logo_compact.png">
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="author" content="Maharani Beverages LLP">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="dns-prefetch" href="https://fonts.gstatic.com">
  <meta name="description" content="{meta_description}">

  <!-- SEO / Canonical -->
  <link rel="canonical" href="https://maharanibeverages.com/{slug}">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://maharanibeverages.com/{slug}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_description}">
  <meta property="og:image" content="https://maharanibeverages.com/zenith_logo_compact.png">

  <!-- Performance Preloads -->
  <link rel="preload" href="https://fonts.gstatic.com/s/syne/v22/8vIJ7w0mNX08UamX_3vN.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="https://fonts.gstatic.com/s/dmsans/v14/rP2Fp2K8zQ2zzL_8oA7EFRXU.woff2" as="font" type="font/woff2" crossorigin>

  <!-- Content Security Policy -->
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: blob: *; connect-src 'self' https://formspree.io; frame-src 'none'; object-src 'none';">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">

  <!-- FAQ Schema -->
  <script type="application/ld+json">
  {faq_schema}
  </script>

  <!-- Multi-Layer Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "name": "Maharani Beverages LLP",
        "url": "https://maharanibeverages.com",
        "telephone": "8274837341",
        "email": "marketing@maharanibeverages.com",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "Ranihati Industrial Park",
          "addressLocality": "Howrah",
          "addressRegion": "West Bengal",
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

  <!-- Breadcrumb Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://maharanibeverages.com/" }},
      {{ "@type": "ListItem", "position": 2, "name": "{breadcrumb_name}", "item": "https://maharanibeverages.com/{slug}" }}
    ]
  }}
  </script>
  <style>.visually-hidden{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;}}</style>

  <!-- CSS -->
  <link rel="stylesheet" href="assets/css/variables.css">
  <link rel="stylesheet" href="assets/css/main.css">
  <link rel="stylesheet" href="assets/css/mobile-perfection.css?v=1.1">
  
  <style>
    .faq-item {{
      background: rgba(255,255,255,0.02);
      border: 1px solid rgba(255,255,255,0.05);
      border-radius: 12px;
      margin-bottom: 1rem;
      overflow: hidden;
    }}
    .faq-q {{ padding: 1.5rem 2rem; cursor: pointer; color: white; font-weight: 700; user-select: none; }}
    .faq-a {{ padding: 0 2rem 2rem 2rem; color: var(--color-muted); line-height: 1.8; }}
  </style>
</head>

<body>

  <!-- ================= STEALTH HEADER ================= -->
  <header class="header">
    <nav class="container">
      <div style="display: flex; align-items: center; gap: 1rem;">
        <a href="/"><img decoding="async" src="zenith_logo_compact.png" alt="Zenith Water Logo" class="logo" style="width: 80px; height: auto;" decoding="async" width="80" height="66" loading="lazy"></a>
      </div>
      <div style="display: flex; gap: 3rem; align-items: center;">
        <a href="/" style="color: rgba(255,255,255,0.6); text-decoration: none; font-weight: 600; font-size: 0.6rem; text-transform: uppercase; letter-spacing: 3px;">Home</a>
        <a href="/{back_link}" style="color: rgba(255,255,255,0.6); text-decoration: none; font-weight: 600; font-size: 0.6rem; text-transform: uppercase; letter-spacing: 3px;">{back_label}</a>
      </div>
    </nav>
  </header>

  <main>
    <!-- ================= SEO HERO ================= -->
    <section id="hero-{slug_short}" style="position: relative; padding: 10rem 0 6rem 0; overflow: hidden; background: #040916;">
       <div class="container" style="position: relative; z-index: 2; text-align: center;">
         <p style="color: var(--color-accent); font-size: 0.75rem; font-weight: 800; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 2rem;">{eyebrow}</p>
         <h1 style="font-family: var(--font-heading); font-size: clamp(2.5rem, 8vw, 4.5rem); color: white; line-height: 1; margin-bottom: 2.5rem;">{h1}</h1>
         <p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; max-width: 700px; margin: 0 auto 3rem auto; line-height: 1.8;">
           {hero_subtitle}
         </p>
         
         <!-- INTENT-DRIVEN CTA -->
         <div style="background: rgba(181,158,109,0.1); border: 1px solid var(--color-accent); padding: 1.5rem; display: inline-block; border-radius: 8px; margin-bottom: 3rem;">
           <p style="color: white; font-weight: 700; margin-bottom: 1rem; font-size: 0.9rem;">{cta_text}</p>
           <a href="{cta_url}" class="btn-ultimate" style="background: var(--color-accent); color: var(--color-primary); border: none;">{cta_button}</a>
         </div>
       </div>
    </section>

    <!-- ================= CONTENT GRID ================= -->
    <section style="padding: 10rem 0; background: var(--color-bg);">
      <div class="container">
        <div style="display: grid; grid-template-columns: 3fr 2fr; gap: 6rem;">
          
          <div class="main-content" style="color: var(--color-muted); line-height: 2;">
            
            <div data-aos="fade-up" style="margin-bottom: 6rem;">
              <h2 style="color: white; font-family: var(--font-heading); font-size: 2.5rem; margin-bottom: 2.5rem;">{section1_title}</h2>
              {section1_body}
            </div>

            <div data-aos="fade-up" style="margin-bottom: 6rem;">
              <h3 style="color: white; font-family: var(--font-heading); font-size: 1.75rem; margin-bottom: 1.5rem;">{section2_title}</h3>
              {section2_body}
            </div>

            <div data-aos="fade-up" style="margin-bottom: 6rem;">
              <h3 style="color: white; font-family: var(--font-heading); font-size: 1.75rem; margin-bottom: 1.5rem;">Service Coverage</h3>
              <p>Our logistical fleet delivers precision purity across {primary_city}'s critical sectors:</p>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                {coverage_items}
              </div>
              <p style="margin-top: 2rem;">{coverage_footer}</p>
            </div>

            <!-- FAQ Section -->
            <div data-aos="fade-up" style="margin-bottom: 6rem;">
              <h3 style="color: white; font-family: var(--font-heading); font-size: 1.75rem; margin-bottom: 2rem;">Frequently Asked Questions</h3>
              {faq_html}
            </div>

          </div>

          <aside>
            <div class="glass-card" style="padding: 3rem; position: sticky; top: 120px;" data-aos="fade-left">
              <h4 style="color: white; font-family: var(--font-heading); font-size: 1.5rem; margin-bottom: 1.5rem;">Contact Support</h4>
              <p style="font-size: 0.9rem; margin-bottom: 2rem; opacity: 0.7;">Initialize your premium hydration setup.</p>
              
              <div style="margin-bottom: 2rem;">
                <p style="font-size: 0.75rem; color: var(--color-accent); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0.5rem;">Executive Line</p>
                <a href="tel:+918274837341" style="color: white; font-weight: 800; font-size: 1.5rem; text-decoration: none; font-family: var(--font-body);">8274837341</a>
              </div>

              <div style="margin-bottom: 3rem;">
                <p style="font-size: 0.75rem; color: var(--color-accent); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0.5rem;">Corporate Email</p>
                <p style="color: white; font-weight: 600;">marketing@maharanibeverages.com</p>
              </div>

              <a href="https://wa.me/918274837341?text={wa_text}" class="btn-ultimate" style="display: block; width: 100%; text-align: center; background: #25D366; border: none;">Order on WhatsApp</a>
              
              <p style="margin-top: 3rem; font-style: italic; font-size: 0.8rem; text-align: center; opacity: 0.4;">Zenith – Delivering Purity with Trust.</p>
            </div>
          </aside>

        </div>
      </div>
    </section>
  </main>

  <!-- ================= V3.1 ARCHITECTURAL FOOTER ================= -->
  <footer style="background: var(--section-dark); border-top: 1px solid rgba(255,255,255,0.08); padding: 8rem 0 4rem 0; position: relative; z-index: 10; margin-top: 10rem;">
    <div class="container">
      
      <!-- Footer Grid: High Authority Architecture -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 4rem; margin-bottom: 6rem;">
        
        <!-- Col 1: Brand & Contact -->
        <div style="grid-column: span 1.5;">
          <a href="/">
            <img decoding="async" src="zenith_logo_compact.png" alt="Zenith Water Official Logo" loading="lazy" style="width: 140px; height: auto; margin-bottom: 1.5rem;" width="140" height="115">
          </a>
          <p style="color: var(--color-accent); font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem;">
            Premium Packaged Drinking Water Supplier in Kolkata & Howrah
          </p>
          <p style="color: rgba(255,255,255,0.6); font-size: 0.95rem; line-height: 1.8; margin-bottom: 2.5rem; max-width: 320px;">
            The gold standard of premium mineral water. Engineered for absolute molecular purity and architectural elegance.
          </p>
          <div style="margin-bottom: 2rem;">
            <p style="color: white; font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1rem;">Direct Line</p>
            <a href="tel:+918274837341" style="color: var(--color-accent); font-size: 1.25rem; font-weight: 800; text-decoration: none; font-family: var(--font-body); display: block; margin-bottom: 0.5rem;">+91 82748 37341</a>
            <a href="mailto:marketing@maharanibeverages.com" style="color: rgba(255,255,255,0.5); font-size: 0.9rem; text-decoration: none; font-weight: 500;">marketing@maharanibeverages.com</a>
          </div>
          <div style="display: inline-flex; align-items: center; gap: 0.6rem; background: rgba(181,158,109,0.05); border: 1px solid rgba(181,158,109,0.2); padding: 0.6rem 1.2rem; border-radius: 4px;">
            <span style="color: var(--color-accent); font-weight: 800;">✓</span>
            <span style="color: rgba(255,255,255,0.8); font-size: 0.7rem; font-weight: 700; letter-spacing: 1px;">FSSAI CERTIFIED: 12825999000938</span>
          </div>
        </div>

        <!-- Col 2: Company -->
        <div>
          <h4 style="font-family: var(--font-heading); font-size: 1rem; color: white; margin-bottom: 2.5rem; text-transform: uppercase; letter-spacing: 3px;">Company</h4>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem;">
            <li><a href="/pages/vision" class="footer-link">About Us</a></li>
            <li><a href="/pages/contact" class="footer-link">Contact Us</a></li>
            <li><a href="/pages/distributor" class="footer-link">Distribution Network</a></li>
            <li><a href="/areas-we-serve" class="footer-link">Areas We Serve</a></li>
            <li><a href="/packaged-drinking-water-kolkata" class="footer-link">Kolkata Hub</a></li>
          </ul>
        </div>

        <!-- Col 3: WATER SUPPLY -->
        <div>
          <h4 style="font-family: var(--font-heading); font-size: 1rem; color: var(--color-accent); margin-bottom: 2.5rem; text-transform: uppercase; letter-spacing: 3px;">Water Supply</h4>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem;">
            <li><a href="/packaged-drinking-water-kolkata" class="footer-link">Packaged Drinking Water Kolkata</a></li>
            <li><a href="/water-supplier-kolkata" class="footer-link">Water Supplier Kolkata</a></li>
            <li><a href="/water-delivery-kolkata" class="footer-link">Water Delivery Kolkata</a></li>
            <li><a href="/bulk-water-supply-kolkata" class="footer-link">Bulk Water Supply Kolkata</a></li>
            <li><a href="/packaged-drinking-water-howrah" class="footer-link">Packaged Drinking Water Howrah</a></li>
            <li><a href="/bulk-water-supply-howrah" class="footer-link">Bulk Water Supply Howrah</a></li>
          </ul>
        </div>

        <!-- Col 4: Legal -->
        <div>
          <h4 style="font-family: var(--font-heading); font-size: 1rem; color: white; margin-bottom: 2.5rem; text-transform: uppercase; letter-spacing: 3px;">Legal</h4>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem;">
            <li><a href="/pages/shipping" class="footer-link">Shipping Policy</a></li>
            <li><a href="/pages/returns" class="footer-link">Returns Policy</a></li>
            <li><a href="/pages/terms" class="footer-link">Terms & Conditions</a></li>
            <li><a href="/pages/privacy" class="footer-link">Privacy Policy</a></li>
          </ul>
        </div>

        <!-- Col 5: Explore -->
        <div>
          <h4 style="font-family: var(--font-heading); font-size: 1rem; color: white; margin-bottom: 2.5rem; text-transform: uppercase; letter-spacing: 3px;">Explore Zenith</h4>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem;">
            <li><a href="/pages/products" class="footer-link">The Collection</a></li>
            <li><a href="/pages/compliance" class="footer-link">Compliance</a></li>
            <li><a href="/pages/comparison" class="footer-link">Superiority Matrix</a></li>
            <li><a href="/blog/" class="footer-link">Scientific Archive</a></li>
          </ul>
        </div>

      </div>

      <!-- Footer Baseline -->
      <div style="border-top: 1px solid rgba(255,255,255,0.06); padding-top: 3rem; text-align: center;">
        <p style="color: rgba(255,255,255,0.3); font-size: 0.8rem; margin: 0 0 1.5rem 0; letter-spacing: 1px; font-weight: 500;">
          &copy; 2026 Maharani Beverages LLP — Zenith Water. All rights reserved.
        </p>
        <!-- SEO Power Line -->
        <p style="opacity: 0.6; font-size: 0.65rem; color: rgba(255,255,255,0.4); max-width: 700px; margin: 0 auto; line-height: 1.6; letter-spacing: 0.5px;">
          Zenith by Maharani Beverages is a premium packaged drinking water supplier in Kolkata and Howrah, offering bulk water supply for homes, offices, hotels, and events with fast and reliable delivery.
        </p>
      </div>

    </div>
  </footer>

  <style> .footer-link{{color:rgba(255,255,255,0.6);text-decoration:none;font-size:0.95rem;transition:color 0.3s,padding-left 0.3s;display:inline-block;}}.footer-link:hover{{color:var(--color-accent);padding-left:5px;}}.social-icon{{display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,0.05);color:white;text-decoration:none;transition:background 0.3s,transform 0.3s;}}.social-icon:hover{{background:var(--color-accent);color:var(--color-primary);transform:translateY(-3px);}}.legal-link{{color:rgba(255,255,255,0.4);text-decoration:none;transition:color 0.3s;}}.legal-link:hover{{color:white;}}</style>

  <script src="assets/js/aos.js" defer></script>
  <script src="assets/js/main.js" defer></script>
</body>

</html>
'''


def build_faq_schema(questions):
    items = []
    for q, a in questions:
        items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}, indent=2)


def build_faq_html(questions):
    out = []
    for q, a in questions:
        out.append(f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>')
    return '\n              '.join(out)


def build_coverage_items(items):
    return '\n                '.join(
        f'<div style="border-left: 1px solid rgba(255,255,255,0.1); padding-left: 1rem;">• {x}</div>' for x in items
    )


def generate_page(page):
    slug = page['slug']
    city = page['city']
    city_list = '"Kolkata", "Howrah"' if page.get('both_cities') else f'"{city}"'
    
    faq_schema = build_faq_schema(page['faqs'])
    faq_html = build_faq_html(page['faqs'])
    coverage_items = build_coverage_items(page['coverage'])
    
    content = TEMPLATE.format(
        title=page['title'],
        meta_description=page['meta_description'],
        slug=slug,
        og_title=page['og_title'],
        og_description=page['og_description'],
        service_type=page['service_type'],
        primary_city=city,
        city_list=city_list,
        service_schema_description=page['service_schema_description'],
        breadcrumb_name=page['breadcrumb_name'],
        back_link=page['back_link'],
        back_label=page['back_label'],
        slug_short=slug.replace('-', ''),
        eyebrow=page['eyebrow'],
        h1=page['h1'],
        hero_subtitle=page['hero_subtitle'],
        cta_text=page['cta_text'],
        cta_url=page['cta_url'],
        cta_button=page['cta_button'],
        section1_title=page['section1_title'],
        section1_body=page['section1_body'],
        section2_title=page['section2_title'],
        section2_body=page['section2_body'],
        coverage_items=coverage_items,
        coverage_footer=page['coverage_footer'],
        faq_schema=faq_schema,
        faq_html=faq_html,
        wa_text=page['wa_text']
    )
    
    path = os.path.join(ROOT, f'{slug}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created {path}')


PAGES = [
    {
        'slug': 'water-supplier-kolkata',
        'city': 'Kolkata',
        'title': 'Water Supplier Kolkata | FSSAI Certified Packaged Drinking Water | Zenith',
        'meta_description': 'Looking for a reliable water supplier in Kolkata? Zenith Water delivers FSSAI certified packaged drinking water to homes, offices, hotels & factories across Kolkata. Call +91 82748 37341.',
        'og_title': 'Water Supplier Kolkata | Zenith Water',
        'og_description': 'Trusted packaged drinking water supplier covering all major Kolkata sectors with scheduled delivery.',
        'service_type': 'Packaged Drinking Water Supply',
        'service_schema_description': 'Reliable water supplier in Kolkata providing FSSAI certified packaged drinking water for homes, offices, hotels, and industrial clients.',
        'breadcrumb_name': 'Water Supplier Kolkata',
        'back_link': 'packaged-drinking-water-kolkata',
        'back_label': 'Kolkata Hub',
        'eyebrow': 'Authorized Water Supplier',
        'h1': 'Trusted Water Supplier in <span style="color: var(--color-accent);">Kolkata</span>',
        'hero_subtitle': 'Zenith Water supplies premium, FSSAI certified packaged drinking water across Kolkata with dependable logistics for homes, offices, hotels, and industries.',
        'cta_text': 'Need bulk water for your premises?',
        'cta_url': '/bulk-water-supply-kolkata',
        'cta_button': 'Get Bulk Supply Quote',
        'section1_title': 'Why Businesses Choose Zenith as Their Water Supplier',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Certified Quality</strong>Every batch is processed through a 7-stage purification system and complies with FSSAI, BIS IS 14543, and ISO standards.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Scheduled Deliveries</strong>We maintain fixed delivery windows so offices, hotels, and restaurants never run out of drinking water.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Flexible Volumes</strong>From retail bottles to 20-litre jars and palletized bulk orders, we scale with your consumption.</li>
              </ul>''',
        'section2_title': 'Industries We Serve in Kolkata',
        'section2_body': '''<p>Our client base spans corporate parks in Salt Lake, hotels near Park Street, educational institutions in Jadavpur, factories along the Kolkata industrial belt, and residential societies across the city. We also support events, banquets, and healthcare facilities with on-time hydration logistics.</p>
              <p style="margin-top: 1.5rem;">Whether you need daily office water delivery or large-volume industrial supply, Zenith acts as your single-source <a href="/packaged-drinking-water-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">packaged drinking water partner in Kolkata ↗</a>.</p>''',
        'coverage': ['Salt Lake & Sector V', 'Park Street & Esplanade', 'Ballygunge & Alipore', 'Rajarhat & New Town', 'Dum Dum & North Kolkata', 'Howrah Extended Corridor'],
        'coverage_footer': 'Custom supply schedules are available for enterprise clients requiring daily or alternate-day fulfillment. <a href="/packaged-drinking-water-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">Also serving Howrah ↗</a>',
        'faqs': [
            ('Which is the best water supplier in Kolkata for offices?', 'Zenith Water is a preferred water supplier for Kolkata offices due to scheduled delivery, FSSAI certification, and flexible bottle/jar sizes.'),
            ('Do you supply water to hotels and restaurants in Kolkata?', 'Yes, we provide packaged drinking water for hotels, restaurants, banquets, and catering operations across Kolkata.'),
            ('What is the minimum order quantity?', 'We cater to both small retail orders and large bulk contracts. Contact us for a customized quote based on your volume.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20am%20looking%20for%20a%20water%20supplier%20in%20Kolkata.%20Please%20share%20details.'
    },
    {
        'slug': 'water-supplier-howrah',
        'city': 'Howrah',
        'title': 'Water Supplier Howrah | Packaged Drinking Water Delivery | Zenith',
        'meta_description': 'Reliable water supplier in Howrah. Zenith Water delivers FSSAI certified packaged drinking water for homes, offices, factories, and events across Howrah. Call +91 82748 37341.',
        'og_title': 'Water Supplier Howrah | Zenith Water',
        'og_description': 'FSSAI certified packaged drinking water supplier covering Howrah Station, Shibpur, Bally, Liluah, and industrial zones.',
        'service_type': 'Packaged Drinking Water Supply',
        'service_schema_description': 'Reliable water supplier in Howrah providing FSSAI certified packaged drinking water for homes, offices, factories, and events.',
        'breadcrumb_name': 'Water Supplier Howrah',
        'back_link': 'packaged-drinking-water-howrah',
        'back_label': 'Howrah Hub',
        'eyebrow': 'Authorized Water Supplier',
        'h1': 'Trusted Water Supplier in <span style="color: var(--color-accent);">Howrah</span>',
        'hero_subtitle': 'Zenith Water supplies premium, FSSAI certified packaged drinking water across Howrah with dependable logistics for homes, offices, factories, and events.',
        'cta_text': 'Need bulk water for your premises?',
        'cta_url': '/bulk-water-supply-howrah',
        'cta_button': 'Get Bulk Supply Quote',
        'section1_title': 'Why Howrah Chooses Zenith as Its Water Supplier',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Local Production</strong>Manufactured at Ranihati Industrial Park, Howrah, ensuring freshness and shorter lead times for local clients.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Industrial Supply</strong>We support factories, warehouses, and labour camps with high-volume 20-litre jar and bottle supply.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Quality Assured</strong>7-stage purification, FSSAI certified, and compliant with BIS IS 14543 standards.</li>
              </ul>''',
        'section2_title': 'Industries We Serve in Howrah',
        'section2_body': '''<p>From commercial complexes near Howrah Station to industrial belts in Bally, Liluah, and Domjur, Zenith supplies packaged drinking water to factories, offices, hospitals, schools, and residential complexes throughout Howrah.</p>
              <p style="margin-top: 1.5rem;">Our Howrah-based production facility allows us to offer competitive pricing and rapid turnaround for bulk contracts. <a href="/bulk-water-supply-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">Explore bulk supply options ↗</a>.</p>''',
        'coverage': ['Howrah Station & Salkia', 'Shibpur & Botanical Garden', 'Bally & Liluah', 'Santragachi & Andul', 'Domjur & Jagacha', 'Ranihati Industrial Belt'],
        'coverage_footer': 'We also deliver to Uluberia, Amta, and surrounding Howrah districts for large bulk orders. <a href="/packaged-drinking-water-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">Also serving Kolkata ↗</a>',
        'faqs': [
            ('Who is the best water supplier in Howrah?', 'Zenith Water is a leading Howrah water supplier with local manufacturing, FSSAI certification, and scheduled delivery across the district.'),
            ('Do you supply water to factories in Howrah?', 'Yes, we specialize in bulk packaged drinking water supply for factories, warehouses, and labour camps across Howrah.'),
            ('What is the delivery time in Howrah?', 'Most Howrah deliveries are completed within 24 to 48 hours depending on order size and location.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20am%20looking%20for%20a%20water%20supplier%20in%20Howrah.%20Please%20share%20details.'
    },
    {
        'slug': 'water-delivery-kolkata',
        'city': 'Kolkata',
        'title': 'Water Delivery Kolkata | Home & Office Packaged Drinking Water | Zenith',
        'meta_description': 'Fast water delivery in Kolkata for homes, offices, hotels & events. Zenith Water delivers FSSAI certified packaged drinking water across all major Kolkata pincodes. Call +91 82748 37341.',
        'og_title': 'Water Delivery Kolkata | Zenith Water',
        'og_description': 'Reliable home and office water delivery across Kolkata. FSSAI certified packaged drinking water delivered on schedule.',
        'service_type': 'Drinking Water Delivery',
        'service_schema_description': 'Scheduled drinking water delivery service in Kolkata for homes, offices, hotels, and events with FSSAI certified packaged water.',
        'breadcrumb_name': 'Water Delivery Kolkata',
        'back_link': 'packaged-drinking-water-kolkata',
        'back_label': 'Kolkata Hub',
        'eyebrow': 'Scheduled Water Delivery',
        'h1': 'Reliable Water Delivery in <span style="color: var(--color-accent);">Kolkata</span>',
        'hero_subtitle': 'Get FSSAI certified packaged drinking water delivered to your home, office, hotel, or event anywhere in Kolkata. Same-day and scheduled delivery options available.',
        'cta_text': 'Need regular water delivery?',
        'cta_url': '/bulk-water-supply-kolkata',
        'cta_button': 'Set Up Delivery Schedule',
        'section1_title': 'How Our Kolkata Water Delivery Works',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Place Your Order</strong>Call, WhatsApp, or submit an enquiry with your pincode and monthly consumption.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Schedule Delivery</strong>Choose a one-time delivery or recurring schedule that matches your household or office needs.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Receive Pure Water</strong>Our fleet delivers sealed, FSSAI certified bottles and 20L jars directly to your address.</li>
              </ul>''',
        'section2_title': 'Delivery Coverage Across Kolkata',
        'section2_body': '''<p>We deliver to Salt Lake, Park Street, Ballygunge, Behala, Garia, Jadavpur, Tollygunge, Dum Dum, Rajarhat, New Town, and most surrounding pincodes. Our pincode checker helps you confirm availability instantly.</p>
              <p style="margin-top: 1.5rem;">For offices and hotels, we offer dedicated delivery windows and bulk invoicing. <a href="/office-water-delivery-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">Explore office water delivery ↗</a>.</p>''',
        'coverage': ['Salt Lake & New Town', 'Park Street & Esplanade', 'Ballygunge & Alipore', 'Behala & New Alipore', 'Garia & Jadavpur', 'Dum Dum & North Kolkata'],
        'coverage_footer': 'We also cover Howrah Station and nearby Howrah localities from our Ranihati facility. <a href="/water-delivery-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Howrah delivery ↗</a>',
        'faqs': [
            ('Do you provide home water delivery in Kolkata?', 'Yes, Zenith delivers packaged drinking water to homes across Kolkata. You can order bottles or 20L jars on a one-time or subscription basis.'),
            ('How fast is water delivery in Kolkata?', 'Standard delivery is within 24 to 48 hours. Same-day delivery may be available for select central Kolkata locations on bulk orders.'),
            ('What is the minimum order for delivery?', 'We have no strict minimum for home delivery, though bulk and scheduled orders receive better pricing.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20need%20water%20delivery%20in%20Kolkata.%20Please%20share%20details.'
    },
    {
        'slug': 'water-delivery-howrah',
        'city': 'Howrah',
        'title': 'Water Delivery Howrah | Home & Office Packaged Drinking Water | Zenith',
        'meta_description': 'Fast water delivery in Howrah. Zenith Water delivers FSSAI certified packaged drinking water for homes, offices, factories, and events across Howrah. Call +91 82748 37341.',
        'og_title': 'Water Delivery Howrah | Zenith Water',
        'og_description': 'Reliable home and office water delivery across Howrah. Locally manufactured FSSAI certified packaged drinking water.',
        'service_type': 'Drinking Water Delivery',
        'service_schema_description': 'Scheduled drinking water delivery service in Howrah for homes, offices, factories, and events with FSSAI certified packaged water.',
        'breadcrumb_name': 'Water Delivery Howrah',
        'back_link': 'packaged-drinking-water-howrah',
        'back_label': 'Howrah Hub',
        'eyebrow': 'Scheduled Water Delivery',
        'h1': 'Reliable Water Delivery in <span style="color: var(--color-accent);">Howrah</span>',
        'hero_subtitle': 'Get FSSAI certified packaged drinking water delivered across Howrah. Local manufacturing at Ranihati means faster delivery and fresher water.',
        'cta_text': 'Need regular water delivery?',
        'cta_url': '/bulk-water-supply-howrah',
        'cta_button': 'Set Up Delivery Schedule',
        'section1_title': 'How Our Howrah Water Delivery Works',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Local Dispatch</strong>Orders are dispatched from our Ranihati Industrial Park facility, reducing transit time across Howrah.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Flexible Scheduling</strong>Choose daily, alternate-day, or weekly delivery based on your consumption pattern.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Sealed & Certified</strong>Every unit is sealed at source and certified under FSSAI and BIS IS 14543 standards.</li>
              </ul>''',
        'section2_title': 'Delivery Coverage Across Howrah',
        'section2_body': '''<p>We deliver to Howrah Station, Salkia, Shibpur, Bally, Liluah, Belur, Santragachi, Andul, Domjur, Jagacha, Uluberia, and surrounding industrial and residential areas.</p>
              <p style="margin-top: 1.5rem;">Factory and industrial clients benefit from dedicated bulk delivery routes. <a href="/water-supply-for-factories-industries-kolkata-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View industrial supply ↗</a>.</p>''',
        'coverage': ['Howrah Station & Salkia', 'Shibpur & Botanical Garden', 'Bally & Liluah', 'Belur & Santragachi', 'Andul & Domjur', 'Uluberia & Amta'],
        'coverage_footer': 'We also deliver to Kolkata localities near the Howrah bridge corridor. <a href="/water-delivery-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Kolkata delivery ↗</a>',
        'faqs': [
            ('Do you deliver water to homes in Howrah?', 'Yes, Zenith provides home water delivery across Howrah including bottles and 20L jars.'),
            ('How fast is delivery in Howrah?', 'Most Howrah deliveries are completed within 24 hours due to our local manufacturing facility.'),
            ('Do you deliver to factories in Howrah?', 'Yes, we offer bulk water delivery for factories, warehouses, and labour camps across Howrah.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20need%20water%20delivery%20in%20Howrah.%20Please%20share%20details.'
    },
    {
        'slug': 'bottled-water-kolkata',
        'city': 'Kolkata',
        'title': 'Bottled Water Kolkata | Premium Packaged Drinking Water | Zenith',
        'meta_description': 'Buy premium bottled water in Kolkata. Zenith Water offers 300ml, 500ml, 1L, 2L & 20L jars delivered to homes, offices, hotels & events. FSSAI certified. Call +91 82748 37341.',
        'og_title': 'Bottled Water Kolkata | Zenith Water',
        'og_description': 'Premium bottled water supplier in Kolkata. Multiple sizes for home, office, hotel, and event use.',
        'service_type': 'Bottled Water Supply',
        'service_schema_description': 'Premium bottled water supplier in Kolkata offering 300ml, 500ml, 1L, 2L bottles and 20L jars for home, office, and event use.',
        'breadcrumb_name': 'Bottled Water Kolkata',
        'back_link': 'packaged-drinking-water-kolkata',
        'back_label': 'Kolkata Hub',
        'eyebrow': 'Premium Bottled Water',
        'h1': 'Bottled Water Supplier in <span style="color: var(--color-accent);">Kolkata</span>',
        'hero_subtitle': 'Zenith Water supplies premium bottled water in 300ml, 500ml, 1L, 2L, and 20L jar sizes for homes, offices, hotels, and events across Kolkata.',
        'cta_text': 'Need bulk bottled water?',
        'cta_url': '/bulk-water-supply-kolkata',
        'cta_button': 'Get Bulk Pricing',
        'section1_title': 'Bottled Water Sizes for Every Need',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">300ml & 500ml</strong>Ideal for conferences, hotels, airlines, retail, and events where convenience and portability matter.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">1L & 2L</strong>Perfect for family use, hospitality tables, gymnasiums, and premium retail shelves.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">20L Jars</strong>The office and factory favourite for dispenser-based hydration with scheduled refill delivery.</li>
              </ul>''',
        'section2_title': 'Why Zenith Bottled Water Stands Out',
        'section2_body': '''<p>Our water goes through a rigorous 7-stage purification process including sand filtration, activated carbon, micron filtration, reverse osmosis, UV treatment, mineral infusion, and ozonation. The result is balanced, great-tasting water that meets BIS IS 14543 and FSSAI standards.</p>
              <p style="margin-top: 1.5rem;">Browse our full product range to find the right bottle size for your needs. <a href="/pages/products" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View all products ↗</a>.</p>''',
        'coverage': ['Salt Lake & Sector V', 'Park Street & Central', 'Ballygunge & South', 'Rajarhat & New Town', 'Behala & West', 'Dum Dum & North'],
        'coverage_footer': 'We deliver bottled water across Kolkata and Howrah. <a href="/bottled-water-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Howrah bottled water ↗</a>',
        'faqs': [
            ('Where can I buy bottled water in bulk in Kolkata?', 'Zenith supplies bottled water in bulk to offices, hotels, and events across Kolkata. Contact us for wholesale pricing.'),
            ('What bottle sizes are available?', 'We offer 300ml, 500ml, 1L, 2L bottles, and 20L jars for dispensers.'),
            ('Is Zenith bottled water FSSAI certified?', 'Yes, all Zenith packaged drinking water is FSSAI certified and complies with BIS IS 14543 standards.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20want%20to%20buy%20bottled%20water%20in%20Kolkata.%20Please%20share%20details.'
    },
    {
        'slug': 'bottled-water-howrah',
        'city': 'Howrah',
        'title': 'Bottled Water Howrah | Premium Packaged Drinking Water | Zenith',
        'meta_description': 'Buy premium bottled water in Howrah. Zenith Water offers 300ml, 500ml, 1L, 2L & 20L jars delivered to homes, offices, factories & events. FSSAI certified. Call +91 82748 37341.',
        'og_title': 'Bottled Water Howrah | Zenith Water',
        'og_description': 'Premium bottled water supplier in Howrah. Locally manufactured and delivered across the district.',
        'service_type': 'Bottled Water Supply',
        'service_schema_description': 'Premium bottled water supplier in Howrah offering 300ml, 500ml, 1L, 2L bottles and 20L jars for home, office, and event use.',
        'breadcrumb_name': 'Bottled Water Howrah',
        'back_link': 'packaged-drinking-water-howrah',
        'back_label': 'Howrah Hub',
        'eyebrow': 'Premium Bottled Water',
        'h1': 'Bottled Water Supplier in <span style="color: var(--color-accent);">Howrah</span>',
        'hero_subtitle': 'Zenith Water supplies premium bottled water in 300ml, 500ml, 1L, 2L, and 20L jar sizes for homes, offices, factories, and events across Howrah.',
        'cta_text': 'Need bulk bottled water?',
        'cta_url': '/bulk-water-supply-howrah',
        'cta_button': 'Get Bulk Pricing',
        'section1_title': 'Bottled Water Sizes for Every Need',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">300ml & 500ml</strong>Ideal for conferences, hotels, retail counters, and events across Howrah.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">1L & 2L</strong>Great for family packs, hospitality tables, and premium retail in Howrah.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">20L Jars</strong>Popular for offices, factories, and institutions with dispenser setups.</li>
              </ul>''',
        'section2_title': 'Locally Manufactured for Howrah',
        'section2_body': '''<p>Our Ranihati Industrial Park facility produces and bottles water specifically for the Howrah market. Local manufacturing means shorter delivery routes, fresher product, and competitive bulk pricing for Howrah businesses.</p>
              <p style="margin-top: 1.5rem;">All bottles are sealed at source and processed through 7-stage purification. <a href="/pages/compliance" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View compliance standards ↗</a>.</p>''',
        'coverage': ['Howrah Station & Salkia', 'Shibpur & Bally', 'Liluah & Belur', 'Santragachi & Andul', 'Domjur & Jagacha', 'Uluberia Industrial'],
        'coverage_footer': 'We also supply bottled water to Kolkata from our Howrah facility. <a href="/bottled-water-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Kolkata bottled water ↗</a>',
        'faqs': [
            ('Where can I buy bottled water in Howrah?', 'Zenith supplies bottled water across Howrah. Call or WhatsApp us to place an order for home or bulk delivery.'),
            ('Do you supply bottled water to factories in Howrah?', 'Yes, we provide bulk bottled water and 20L jars for factories, warehouses, and industrial units.'),
            ('What certifications does Zenith bottled water have?', 'Zenith bottled water is FSSAI certified and complies with BIS IS 14543 packaged drinking water standards.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20want%20to%20buy%20bottled%20water%20in%20Howrah.%20Please%20share%20details.'
    },
]

if __name__ == '__main__':
    for page in PAGES:
        generate_page(page)
    print('Done.')
