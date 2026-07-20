#!/usr/bin/env python3
"""Generate additional keyword-specific landing pages for Zenith Water."""
import os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, 'scripts/generate-landing-pages.py'), 'r', encoding='utf-8') as f:
    source = f.read()

# Extract TEMPLATE and helper functions by executing the source in a controlled namespace
ns = {'__file__': os.path.join(ROOT, 'scripts/generate-landing-pages.py')}
exec(source, ns)
TEMPLATE = ns['TEMPLATE']
generate_page = ns['generate_page']

PAGES = [
    {
        'slug': 'drinking-water-kolkata',
        'city': 'Kolkata',
        'title': 'Drinking Water Kolkata | Packaged Drinking Water Delivery | Zenith',
        'meta_description': 'Get pure drinking water in Kolkata. Zenith Water delivers FSSAI certified packaged drinking water to homes, offices, hotels, and events across Kolkata. Call +91 82748 37341.',
        'og_title': 'Drinking Water Kolkata | Zenith Water',
        'og_description': 'Safe and reliable drinking water delivery across Kolkata. FSSAI certified packaged water.',
        'service_type': 'Drinking Water Supply',
        'service_schema_description': 'FSSAI certified drinking water supply and delivery service in Kolkata for residential, commercial, and industrial use.',
        'breadcrumb_name': 'Drinking Water Kolkata',
        'back_link': 'packaged-drinking-water-kolkata',
        'back_label': 'Kolkata Hub',
        'eyebrow': 'Safe Drinking Water',
        'h1': 'Drinking Water Supplier in <span style="color: var(--color-accent);">Kolkata</span>',
        'hero_subtitle': 'Zenith Water provides safe, FSSAI certified drinking water across Kolkata. Reliable delivery for homes, offices, hotels, and events.',
        'cta_text': 'Need regular drinking water supply?',
        'cta_url': '/bulk-water-supply-kolkata',
        'cta_button': 'Schedule Supply',
        'section1_title': 'Why Choose Zenith for Drinking Water in Kolkata',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Purity Guaranteed</strong>7-stage purification including RO, UV, and ozonation ensures every drop is safe to drink.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Certified Safe</strong>FSSAI certified and compliant with BIS IS 14543 packaged drinking water standards.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Citywide Delivery</strong>We deliver drinking water to all major Kolkata sectors with flexible schedules.</li>
              </ul>''',
        'section2_title': 'Drinking Water for Every Setting',
        'section2_body': '''<p>From household daily consumption to corporate offices, hotel buffets, and large events, Zenith supplies drinking water that meets the highest safety standards. Our fleet ensures timely delivery so you never run short.</p>
              <p style="margin-top: 1.5rem;">Explore our <a href="/water-delivery-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">drinking water delivery service in Kolkata ↗</a>.</p>''',
        'coverage': ['Salt Lake & New Town', 'Park Street & Esplanade', 'Ballygunge & Alipore', 'Behala & New Alipore', 'Garia & Jadavpur', 'Dum Dum & North'],
        'coverage_footer': 'We also supply drinking water across Howrah from our local plant. <a href="/drinking-water-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Howrah drinking water ↗</a>',
        'faqs': [
            ('Who supplies drinking water in Kolkata?', 'Zenith Water supplies FSSAI certified packaged drinking water across Kolkata for homes, offices, and commercial use.'),
            ('Is delivered drinking water safe in Kolkata?', 'Yes, Zenith drinking water undergoes 7-stage purification and is sealed at source to maintain safety.'),
            ('What is the price of drinking water in Kolkata?', 'Pricing depends on bottle/jar size and order volume. Contact us for a customized quote.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20need%20drinking%20water%20supply%20in%20Kolkata.%20Please%20share%20details.'
    },
    {
        'slug': 'drinking-water-howrah',
        'city': 'Howrah',
        'title': 'Drinking Water Howrah | Packaged Drinking Water Delivery | Zenith',
        'meta_description': 'Get pure drinking water in Howrah. Zenith Water delivers FSSAI certified packaged drinking water to homes, offices, factories, and events across Howrah. Call +91 82748 37341.',
        'og_title': 'Drinking Water Howrah | Zenith Water',
        'og_description': 'Safe and reliable drinking water delivery across Howrah. Locally manufactured FSSAI certified water.',
        'service_type': 'Drinking Water Supply',
        'service_schema_description': 'FSSAI certified drinking water supply and delivery service in Howrah for residential, commercial, and industrial use.',
        'breadcrumb_name': 'Drinking Water Howrah',
        'back_link': 'packaged-drinking-water-howrah',
        'back_label': 'Howrah Hub',
        'eyebrow': 'Safe Drinking Water',
        'h1': 'Drinking Water Supplier in <span style="color: var(--color-accent);">Howrah</span>',
        'hero_subtitle': 'Zenith Water provides safe, FSSAI certified drinking water across Howrah. Locally manufactured with reliable delivery for homes, offices, and factories.',
        'cta_text': 'Need regular drinking water supply?',
        'cta_url': '/bulk-water-supply-howrah',
        'cta_button': 'Schedule Supply',
        'section1_title': 'Why Choose Zenith for Drinking Water in Howrah',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Local Manufacturing</strong>Made at Ranihati Industrial Park, Howrah, ensuring freshness and fast delivery.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Certified Quality</strong>FSSAI certified and BIS IS 14543 compliant for complete safety assurance.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Industrial Focus</strong>We supply factories, labour camps, and warehouses with high-volume drinking water.</li>
              </ul>''',
        'section2_title': 'Drinking Water for Homes & Industry',
        'section2_body': '''<p>Whether you need drinking water for a residence in Shibpur or a factory in Domjur, Zenith has the logistics and production capacity to serve you. Our Howrah facility enables same-day and next-day deliveries across the district.</p>
              <p style="margin-top: 1.5rem;">Learn more about our <a href="/water-delivery-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">Howrah water delivery service ↗</a>.</p>''',
        'coverage': ['Howrah Station & Salkia', 'Shibpur & Botanical Garden', 'Bally & Liluah', 'Belur & Santragachi', 'Andul & Domjur', 'Uluberia & Amta'],
        'coverage_footer': 'We also supply drinking water to Kolkata. <a href="/drinking-water-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Kolkata drinking water ↗</a>',
        'faqs': [
            ('Who supplies drinking water in Howrah?', 'Zenith Water supplies FSSAI certified packaged drinking water across Howrah from its Ranihati facility.'),
            ('Do you supply drinking water to factories?', 'Yes, we specialize in bulk drinking water supply for factories, warehouses, and labour camps in Howrah.'),
            ('How fast is delivery in Howrah?', 'Most Howrah deliveries are completed within 24 to 48 hours due to local manufacturing.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20need%20drinking%20water%20supply%20in%20Howrah.%20Please%20share%20details.'
    },
    {
        'slug': 'mineral-water-kolkata',
        'city': 'Kolkata',
        'title': 'Mineral Water Kolkata | Premium Packaged Drinking Water | Zenith',
        'meta_description': 'Buy premium mineral water in Kolkata. Zenith Water delivers FSSAI certified packaged mineral water for homes, offices, hotels, and events. Call +91 82748 37341.',
        'og_title': 'Mineral Water Kolkata | Zenith Water',
        'og_description': 'Premium mineral water supplier in Kolkata. 7-stage purified water delivered across the city.',
        'service_type': 'Mineral Water Supply',
        'service_schema_description': 'Premium mineral water supplier in Kolkata offering FSSAI certified packaged drinking water for home, office, and event use.',
        'breadcrumb_name': 'Mineral Water Kolkata',
        'back_link': 'packaged-drinking-water-kolkata',
        'back_label': 'Kolkata Hub',
        'eyebrow': 'Premium Mineral Water',
        'h1': 'Mineral Water Supplier in <span style="color: var(--color-accent);">Kolkata</span>',
        'hero_subtitle': 'Zenith Water supplies premium mineral-balanced packaged drinking water across Kolkata for homes, offices, hotels, and events.',
        'cta_text': 'Need mineral water for your business?',
        'cta_url': '/bulk-water-supply-kolkata',
        'cta_button': 'Get Bulk Quote',
        'section1_title': 'What Makes Zenith Mineral Water Different',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Balanced Minerals</strong>Our water retains essential minerals while removing impurities, delivering both taste and health benefits.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">7-Stage Purification</strong>Advanced filtration, RO, UV, and ozonation ensure purity in every bottle.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Multiple Sizes</strong>Choose from 250ml, 500ml, 1L, 2L bottles, and 20L jars for every need.</li>
              </ul>''',
        'section2_title': 'Mineral Water for Homes & Businesses',
        'section2_body': '''<p>Our mineral water is trusted by hotels, restaurants, corporate offices, and households across Kolkata. The mineral balance is carefully maintained to provide a clean, refreshing taste that complements any dining or hydration setting.</p>
              <p style="margin-top: 1.5rem;">Browse our product collection to choose your preferred mineral water size. <a href="/pages/products" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View products ↗</a>.</p>''',
        'coverage': ['Salt Lake & Sector V', 'Park Street & Central', 'Ballygunge & South', 'Rajarhat & New Town', 'Behala & West', 'Dum Dum & North'],
        'coverage_footer': 'We deliver mineral water across Kolkata and Howrah. <a href="/mineral-water-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Howrah mineral water ↗</a>',
        'faqs': [
            ('Where can I buy mineral water in Kolkata?', 'Zenith supplies premium mineral water across Kolkata. Contact us for home delivery or bulk supply.'),
            ('Is Zenith mineral water FSSAI certified?', 'Yes, all Zenith mineral water is FSSAI certified and complies with BIS IS 14543 standards.'),
            ('What sizes of mineral water are available?', 'We offer 250ml, 500ml, 1L, 2L bottles, and 20L jars.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20want%20to%20buy%20mineral%20water%20in%20Kolkata.%20Please%20share%20details.'
    },
    {
        'slug': 'mineral-water-howrah',
        'city': 'Howrah',
        'title': 'Mineral Water Howrah | Premium Packaged Drinking Water | Zenith',
        'meta_description': 'Buy premium mineral water in Howrah. Zenith Water delivers FSSAI certified packaged mineral water for homes, offices, factories, and events. Call +91 82748 37341.',
        'og_title': 'Mineral Water Howrah | Zenith Water',
        'og_description': 'Premium mineral water supplier in Howrah. Locally manufactured and delivered across the district.',
        'service_type': 'Mineral Water Supply',
        'service_schema_description': 'Premium mineral water supplier in Howrah offering FSSAI certified packaged drinking water for home, office, and event use.',
        'breadcrumb_name': 'Mineral Water Howrah',
        'back_link': 'packaged-drinking-water-howrah',
        'back_label': 'Howrah Hub',
        'eyebrow': 'Premium Mineral Water',
        'h1': 'Mineral Water Supplier in <span style="color: var(--color-accent);">Howrah</span>',
        'hero_subtitle': 'Zenith Water supplies premium mineral-balanced packaged drinking water across Howrah for homes, offices, factories, and events.',
        'cta_text': 'Need mineral water for your business?',
        'cta_url': '/bulk-water-supply-howrah',
        'cta_button': 'Get Bulk Quote',
        'section1_title': 'What Makes Zenith Mineral Water Different',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Locally Bottled</strong>Our Ranihati facility bottles mineral water fresh for the Howrah market.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Balanced Composition</strong>Essential minerals are retained for taste and hydration benefits.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Certified Quality</strong>FSSAI certified and BIS IS 14543 compliant.</li>
              </ul>''',
        'section2_title': 'Mineral Water for Howrah Homes & Industry',
        'section2_body': '''<p>From residential complexes in Bally to factories in Uluberia, Zenith supplies mineral water that meets strict safety standards. Local production ensures shorter lead times and fresher product for Howrah customers.</p>
              <p style="margin-top: 1.5rem;">Learn about our purification process. <a href="/pages/compliance" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View compliance ↗</a>.</p>''',
        'coverage': ['Howrah Station & Salkia', 'Shibpur & Bally', 'Liluah & Belur', 'Santragachi & Andul', 'Domjur & Jagacha', 'Uluberia Industrial'],
        'coverage_footer': 'We also supply mineral water to Kolkata. <a href="/mineral-water-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Kolkata mineral water ↗</a>',
        'faqs': [
            ('Where can I buy mineral water in Howrah?', 'Zenith supplies mineral water across Howrah. Call or WhatsApp for home or bulk delivery.'),
            ('Do you supply mineral water to factories?', 'Yes, we provide bulk mineral water and 20L jars for factories and industrial units in Howrah.'),
            ('Is Zenith mineral water certified?', 'Yes, it is FSSAI certified and complies with BIS IS 14543 standards.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20want%20to%20buy%20mineral%20water%20in%20Howrah.%20Please%20share%20details.'
    },
    {
        'slug': 'water-supply-for-hotels-restaurants-kolkata',
        'city': 'Kolkata',
        'title': 'Hotel & Restaurant Water Supply Kolkata | Zenith Water',
        'meta_description': 'Reliable water supply for hotels, restaurants, banquets & cafes in Kolkata. Zenith Water provides FSSAI certified packaged drinking water with scheduled delivery. Call +91 82748 37341.',
        'og_title': 'Hotel & Restaurant Water Supply Kolkata | Zenith',
        'og_description': 'Premium packaged drinking water supply for Kolkata hospitality businesses.',
        'service_type': 'HORECA Water Supply',
        'service_schema_description': 'Packaged drinking water supply service for hotels, restaurants, banquets, and cafes in Kolkata.',
        'breadcrumb_name': 'Hotel & Restaurant Water Supply Kolkata',
        'back_link': 'packaged-drinking-water-kolkata',
        'back_label': 'Kolkata Hub',
        'eyebrow': 'HORECA Water Solutions',
        'h1': 'Water Supply for Hotels & Restaurants in <span style="color: var(--color-accent);">Kolkata</span>',
        'hero_subtitle': 'Zenith Water partners with Kolkata hotels, restaurants, banquets, and cafes to deliver premium FSSAI certified packaged drinking water with reliable logistics.',
        'cta_text': 'Set up hotel or restaurant supply?',
        'cta_url': '/bulk-water-supply-kolkata',
        'cta_button': 'Get HORECA Quote',
        'section1_title': 'Why Kolkata Hospitality Businesses Choose Zenith',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Guest-Ready Presentation</strong>Elegant bottle designs that complement fine-dining tables, hotel minibars, and banquet settings.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Consistent Supply</strong>Scheduled deliveries ensure your stock never runs low during peak service hours.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Size Flexibility</strong>250ml and 500ml for guest tables, 1L and 2L for room service, 20L jars for staff and kitchen use.</li>
              </ul>''',
        'section2_title': 'Serving Kolkata\'s HORECA Sector',
        'section2_body': '''<p>We supply premium packaged drinking water to hotels near Park Street, restaurants in Salt Lake, banquet halls in Rajarhat, and cafes across South Kolkata. Our delivery schedules align with your business operations, and our pricing supports high-volume contracts.</p>
              <p style="margin-top: 1.5rem;">For large events and weddings, explore our <a href="/event-water-supply-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">event water supply service ↗</a>.</p>''',
        'coverage': ['Park Street & Central Hotels', 'Salt Lake & Sector V', 'Ballygunge & South Restaurants', 'Rajarhat & New Town Banquets', 'Behala & West Kolkata', 'Garia & Jadavpur Cafes'],
        'coverage_footer': 'We also supply hotels and restaurants in Howrah. <a href="/packaged-drinking-water-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Howrah supply ↗</a>',
        'faqs': [
            ('Do you supply water to restaurants in Kolkata?', 'Yes, Zenith supplies packaged drinking water to restaurants, cafes, and cloud kitchens across Kolkata.'),
            ('What bottle sizes are best for hotels?', 'Hotels typically use 250ml/500ml for guest tables, 1L/2L for room service, and 20L jars for staff areas.'),
            ('Do you offer credit billing for hotels?', 'Yes, we offer bulk invoicing and credit terms for verified hotel and restaurant clients.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20need%20water%20supply%20for%20my%20hotel%2Frestaurant%20in%20Kolkata.%20Please%20share%20details.'
    },
    {
        'slug': 'water-supply-for-factories-industries-kolkata-howrah',
        'city': 'Howrah',
        'title': 'Factory & Industrial Water Supply Kolkata-Howrah | Zenith',
        'meta_description': 'Bulk water supply for factories, industries & labour camps in Kolkata and Howrah. Zenith Water delivers FSSAI certified packaged drinking water at scale. Call +91 82748 37341.',
        'og_title': 'Factory & Industrial Water Supply Kolkata-Howrah | Zenith',
        'og_description': 'Industrial-scale packaged drinking water supply for factories and labour camps across Kolkata and Howrah.',
        'service_type': 'Industrial Water Supply',
        'service_schema_description': 'Bulk packaged drinking water supply for factories, industries, warehouses, and labour camps in Kolkata and Howrah.',
        'breadcrumb_name': 'Factory & Industrial Water Supply',
        'back_link': 'bulk-water-supply-howrah',
        'back_label': 'Bulk Hub',
        'eyebrow': 'Industrial Water Solutions',
        'h1': 'Factory & Industrial Water Supply in <span style="color: var(--color-accent);">Kolkata & Howrah</span>',
        'hero_subtitle': 'Zenith Water provides industrial-scale packaged drinking water supply for factories, warehouses, and labour camps across the Kolkata-Howrah industrial belt.',
        'cta_text': 'Need industrial bulk water supply?',
        'cta_url': '/bulk-water-supply-howrah',
        'cta_button': 'Get Industrial Quote',
        'section1_title': 'Why Industries Trust Zenith for Bulk Water',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">High Volume Capacity</strong>We supply thousands of litres daily through 20L jars and bottles for large workforces.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Local Howrah Plant</strong>Our Ranihati facility is strategically located to serve the Howrah industrial belt with minimal transit time.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Worker Safety</strong>FSSAI certified water ensures your workforce stays hydrated with safe, purified drinking water.</li>
              </ul>''',
        'section2_title': 'Industrial Coverage Across the Belt',
        'section2_body': '''<p>We serve manufacturing units, warehouses, and labour camps in Howrah\'s industrial zones as well as Kolkata\'s factory areas. Our fleet handles scheduled bulk deliveries, emergency top-ups, and long-term supply contracts.</p>
              <p style="margin-top: 1.5rem;">For office-specific supply, see our <a href="/office-water-delivery-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">office water delivery service ↗</a>.</p>''',
        'coverage': ['Ranihati & Domjur', 'Bally & Liluah Industrial', 'Santragachi & Andul', 'Uluberia & Amta', 'Kolkata Industrial Belt', ' labour Camps & Warehouses'],
        'coverage_footer': 'We cover the entire Kolkata-Howrah industrial corridor. Contact us for a site visit and volume assessment.',
        'faqs': [
            ('Do you supply water to factories in Howrah?', 'Yes, Zenith specializes in bulk packaged drinking water supply for factories and labour camps in Howrah and Kolkata.'),
            ('What is the minimum bulk order for industries?', 'We offer flexible industrial contracts. Contact us for a volume-based quote.'),
            ('Is the water safe for factory workers?', 'Yes, all Zenith water is FSSAI certified and processed through 7-stage purification.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20need%20bulk%20water%20supply%20for%20my%20factory%20in%20Kolkata%2FHowrah.%20Please%20share%20details.'
    },
    {
        'slug': 'office-water-delivery-kolkata',
        'city': 'Kolkata',
        'title': 'Office Water Delivery Kolkata | 20L Jars & Bottles | Zenith',
        'meta_description': 'Reliable office water delivery in Kolkata. Zenith Water supplies FSSAI certified 20L jars and bottled water for corporate offices, co-working spaces & IT parks. Call +91 82748 37341.',
        'og_title': 'Office Water Delivery Kolkata | Zenith',
        'og_description': 'Scheduled office water delivery across Kolkata. 20L jars and bottled water for workplaces.',
        'service_type': 'Office Water Delivery',
        'service_schema_description': 'Scheduled packaged drinking water delivery service for offices, corporate parks, and co-working spaces in Kolkata.',
        'breadcrumb_name': 'Office Water Delivery Kolkata',
        'back_link': 'water-delivery-kolkata',
        'back_label': 'Delivery Hub',
        'eyebrow': 'Corporate Hydration',
        'h1': 'Office Water Delivery in <span style="color: var(--color-accent);">Kolkata</span>',
        'hero_subtitle': 'Keep your Kolkata office hydrated with scheduled delivery of FSSAI certified 20L jars and bottled water. Flexible plans for teams of any size.',
        'cta_text': 'Set up office water delivery?',
        'cta_url': '/bulk-water-supply-kolkata',
        'cta_button': 'Get Office Quote',
        'section1_title': 'Why Offices Choose Zenith Water Delivery',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Scheduled Deliveries</strong>Fixed weekly or bi-weekly delivery windows that match your office consumption.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Multiple Formats</strong>20L jars for dispensers, 500ml bottles for meeting rooms, and 1L bottles for executive cabins.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">GST Invoicing</strong>We provide proper tax invoices and bulk pricing for corporate accounts.</li>
              </ul>''',
        'section2_title': 'Offices We Serve in Kolkata',
        'section2_body': '''<p>We deliver to IT parks in Salt Lake and Rajarhat, corporate offices near Park Street and Sector V, co-working spaces in Ballygunge, and startups across New Town. Our delivery team understands office security protocols and delivers during business hours.</p>
              <p style="margin-top: 1.5rem;">For larger corporate campuses, see our <a href="/bulk-water-supply-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">bulk water supply service ↗</a>.</p>''',
        'coverage': ['Salt Lake & Sector V', 'Rajarhat & New Town', 'Park Street & Central', 'Ballygunge & South', 'Behala & West', 'Dum Dum & North'],
        'coverage_footer': 'We deliver office water across Kolkata and Howrah. Contact us to set up a recurring delivery plan.',
        'faqs': [
            ('Do you deliver 20L jars to offices in Kolkata?', 'Yes, we supply 20L water jars and bottles to offices across Kolkata on scheduled delivery plans.'),
            ('Can you provide daily office water delivery?', 'Yes, we offer daily, alternate-day, or weekly delivery schedules based on your office size.'),
            ('Do you offer corporate billing?', 'Yes, we provide GST invoices and corporate billing for office water supply contracts.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20need%20office%20water%20delivery%20in%20Kolkata.%20Please%20share%20details.'
    },
    {
        'slug': 'event-water-supply-kolkata',
        'city': 'Kolkata',
        'title': 'Event Water Supply Kolkata | Bulk Bottled Water for Events | Zenith',
        'meta_description': 'Bulk water supply for events, weddings, conferences & exhibitions in Kolkata. Zenith Water delivers FSSAI certified bottled water on time. Call +91 82748 37341.',
        'og_title': 'Event Water Supply Kolkata | Zenith',
        'og_description': 'Reliable bulk bottled water supply for events and weddings across Kolkata.',
        'service_type': 'Event Water Supply',
        'service_schema_description': 'Bulk packaged drinking water supply for events, weddings, conferences, and exhibitions in Kolkata.',
        'breadcrumb_name': 'Event Water Supply Kolkata',
        'back_link': 'packaged-drinking-water-kolkata',
        'back_label': 'Kolkata Hub',
        'eyebrow': 'Event Hydration Logistics',
        'h1': 'Event Water Supply in <span style="color: var(--color-accent);">Kolkata</span>',
        'hero_subtitle': 'Zenith Water provides bulk bottled water supply for weddings, conferences, exhibitions, and corporate events across Kolkata with on-time delivery.',
        'cta_text': 'Planning an event?',
        'cta_url': '/bulk-water-supply-kolkata',
        'cta_button': 'Get Event Quote',
        'section1_title': 'Why Event Planners Choose Zenith',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">On-Time Delivery</strong>We coordinate delivery with your event schedule, ensuring water is available before guests arrive.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Bulk Pricing</strong>Special event pricing for large orders of 250ml and 500ml bottles.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Branded Options</strong>Premium packaging that looks elegant on banquet tables and conference setups.</li>
              </ul>''',
        'section2_title': 'Events We Cover in Kolkata',
        'section2_body': '''<p>We supply water for weddings at banquet halls, corporate conferences at hotels, exhibitions at convention centres, college fests, and private celebrations. Our team can handle last-minute volume changes and deliver to multiple event venues.</p>
              <p style="margin-top: 1.5rem;">For hotel-specific supply, see our <a href="/water-supply-for-hotels-restaurants-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">HORECA water supply ↗</a>.</p>''',
        'coverage': ['Park Street Banquet Halls', 'Salt Lake Convention Centres', 'Rajarhat Wedding Venues', 'Ballygunge Hotels', 'New Town Exhibition Spaces', 'Outdoor Event Grounds'],
        'coverage_footer': 'We deliver event water across Kolkata. Book at least 48 hours in advance for large events.',
        'faqs': [
            ('Do you supply water for weddings in Kolkata?', 'Yes, we provide bulk bottled water supply for weddings and banquets across Kolkata.'),
            ('How much water do I need for my event?', 'A typical event uses 1-2 bottles per guest. Contact us and we will help you estimate volume.'),
            ('Can you deliver on the event day?', 'Yes, we coordinate delivery timing with your event schedule.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20need%20water%20supply%20for%20an%20event%20in%20Kolkata.%20Please%20share%20details.'
    },
    {
        'slug': '20-liter-water-jar-delivery-kolkata',
        'city': 'Kolkata',
        'title': '20 Litre Water Jar Delivery Kolkata | Office & Home | Zenith',
        'meta_description': '20 litre water jar delivery in Kolkata for homes and offices. Zenith Water supplies FSSAI certified 20L jars with dispenser compatibility. Call +91 82748 37341.',
        'og_title': '20 Litre Water Jar Delivery Kolkata | Zenith',
        'og_description': 'Reliable 20L water jar delivery across Kolkata for offices and homes.',
        'service_type': '20L Jar Water Delivery',
        'service_schema_description': '20 litre packaged drinking water jar delivery service for homes and offices in Kolkata.',
        'breadcrumb_name': '20L Water Jar Delivery Kolkata',
        'back_link': 'water-delivery-kolkata',
        'back_label': 'Delivery Hub',
        'eyebrow': '20L Jar Delivery',
        'h1': '20 Litre Water Jar Delivery in <span style="color: var(--color-accent);">Kolkata</span>',
        'hero_subtitle': 'Get FSSAI certified 20 litre water jars delivered to your home or office in Kolkata. Compatible with standard dispensers and available on subscription.',
        'cta_text': 'Need 20L jars delivered regularly?',
        'cta_url': '/bulk-water-supply-kolkata',
        'cta_button': 'Set Up Jar Delivery',
        'section1_title': 'Why Choose Zenith 20L Jar Delivery',
        'section1_body': '''<ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Dispenser Ready</strong>Our 20L jars fit standard water dispensers used in homes and offices.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Subscription Plans</strong>Choose weekly, bi-weekly, or monthly delivery based on your consumption.</li>
                <li style="margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;"><strong style="color: white; display: block; margin-bottom: 0.5rem;">Sealed & Safe</strong>Every jar is sealed at source and processed through 7-stage purification.</li>
              </ul>''',
        'section2_title': '20L Jar Delivery Across Kolkata',
        'section2_body': '''<p>We deliver 20L jars to apartments, independent homes, corporate offices, co-working spaces, schools, and clinics across Kolkata. Our delivery team handles jars carefully and replaces empty jars on request.</p>
              <p style="margin-top: 1.5rem;">For office-specific delivery, visit <a href="/office-water-delivery-kolkata" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">office water delivery Kolkata ↗</a>.</p>''',
        'coverage': ['Salt Lake & New Town', 'Park Street & Esplanade', 'Ballygunge & Alipore', 'Behala & New Alipore', 'Garia & Jadavpur', 'Dum Dum & North'],
        'coverage_footer': 'We also deliver 20L jars in Howrah. <a href="/bulk-water-supply-howrah" style="color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);">View Howrah bulk supply ↗</a>',
        'faqs': [
            ('Do you deliver 20L water jars in Kolkata?', 'Yes, Zenith delivers 20L water jars across Kolkata for homes and offices.'),
            ('Are your 20L jars compatible with dispensers?', 'Yes, our 20L jars are compatible with standard water dispensers.'),
            ('What is the delivery schedule for 20L jars?', 'We offer flexible schedules including weekly, bi-weekly, and monthly deliveries.'),
        ],
        'wa_text': 'Hello%20Zenith%2C%20I%20need%2020%20litre%20water%20jar%20delivery%20in%20Kolkata.%20Please%20share%20details.'
    },
]

if __name__ == '__main__':
    for page in PAGES:
        generate_page(page)
    print('Done.')
