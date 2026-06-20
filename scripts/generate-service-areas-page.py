#!/usr/bin/env python3
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

with open(os.path.join(ROOT, 'scripts/generate-landing-pages.py'), 'r', encoding='utf-8') as f:
    source = f.read()

ns = {'__file__': os.path.join(ROOT, 'scripts/generate-landing-pages.py')}
exec(source, ns)
TEMPLATE = ns['TEMPLATE']
generate_page = ns['generate_page']

page = {
    'slug': 'areas-we-serve',
    'city': 'Kolkata',
    'title': 'Areas We Serve | Packaged Drinking Water Delivery Kolkata & Howrah | Zenith',
    'meta_description': 'Zenith Water delivers packaged drinking water across Kolkata and Howrah. Check our service areas including Salt Lake, Park Street, Ballygunge, Howrah Station, and more.',
    'og_title': 'Areas We Serve | Zenith Water',
    'og_description': 'Complete list of Kolkata and Howrah areas served by Zenith Water delivery network.',
    'service_type': 'Water Delivery',
    'service_schema_description': 'Packaged drinking water delivery service covering major residential, commercial, and industrial areas in Kolkata and Howrah.',
    'breadcrumb_name': 'Areas We Serve',
    'back_link': 'packaged-drinking-water-kolkata',
    'back_label': 'Kolkata Hub',
    'eyebrow': 'Delivery Network',
    'h1': 'Areas We Serve in <span style="color: var(--color-accent);">Kolkata & Howrah</span>',
    'hero_subtitle': 'Zenith Water delivers FSSAI certified packaged drinking water to homes, offices, hotels, and industries across all major sectors of Kolkata and Howrah.',
    'cta_text': 'Check availability in your area',
    'cta_url': '/',
    'cta_button': 'Verify Pincode',
    'section1_title': 'Kolkata Service Areas',
    'section1_body': '''<p>Our Kolkata delivery network covers the full metropolitan region, from north to south and east to west. We serve:</p>
              <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-salt-lake" style="color: var(--color-accent); text-decoration: none;">Salt Lake / Bidhannagar</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-park-street" style="color: var(--color-accent); text-decoration: none;">Park Street / Esplanade</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-dum-dum" style="color: var(--color-accent); text-decoration: none;">Dum Dum</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-rajarhat" style="color: var(--color-accent); text-decoration: none;">Rajarhat / New Town</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-behala" style="color: var(--color-accent); text-decoration: none;">Behala</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-jadavpur" style="color: var(--color-accent); text-decoration: none;">Jadavpur</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-tollygunge" style="color: var(--color-accent); text-decoration: none;">Tollygunge</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-ballygunge" style="color: var(--color-accent); text-decoration: none;">Ballygunge</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-garia" style="color: var(--color-accent); text-decoration: none;">Garia / Patuli</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-kolkata" style="color: var(--color-accent); text-decoration: none;">All Kolkata Zones</a></li>
              </ul>''',
    'section2_title': 'Howrah Service Areas',
    'section2_body': '''<p>Our Howrah operations are anchored at the Ranihati Industrial Park facility, enabling fast delivery across the district:</p>
              <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-howrah-station" style="color: var(--color-accent); text-decoration: none;">Howrah Station</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Shibpur & Botanical Garden</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Bally & Liluah</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Belur & Santragachi</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Andul & Domjur</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Uluberia & Amta</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-howrah" style="color: var(--color-accent); text-decoration: none;">All Howrah Zones</a></li>
              </ul>''',
    'coverage': ['Salt Lake Sector V', 'Park Street Central', 'Ballygunge South', 'Rajarhat New Town', 'Howrah Station', 'Ranihati Industrial Belt'],
    'coverage_footer': 'If your area is not listed, contact us. We are continuously expanding our delivery network across the Kolkata metropolitan region.',
    'faqs': [
        ('Do you deliver to my area in Kolkata?', 'We deliver to all major Kolkata sectors. Use the pincode checker on our homepage or call us to confirm availability.'),
        ('Do you serve Howrah?', 'Yes, we serve all major Howrah areas from our Ranihati facility with fast local delivery.'),
        ('Can you deliver to industrial areas?', 'Yes, we specialize in bulk delivery to factories, warehouses, and labour camps across the Kolkata-Howrah industrial belt.'),
    ],
    'wa_text': 'Hello%20Zenith%2C%20I%20want%20to%20confirm%20delivery%20availability%20in%20my%20area.%20Please%20help.'
}

if __name__ == '__main__':
    generate_page(page)
    print('Done.')
