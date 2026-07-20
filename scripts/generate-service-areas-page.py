#!/usr/bin/env python3
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

with open(os.path.join(ROOT, 'scripts/generate-landing-pages.py'), 'r', encoding='utf-8') as f:
    source = f.read()

ns = {'__file__': os.path.join(ROOT, 'scripts/generate-landing-pages.py')}
exec(source, ns)
TEMPLATE = ns['TEMPLATE']
render_page = ns['render_page']

page = {
    'slug': 'areas-we-serve',
    'city': 'Kolkata',
    'title': 'Areas We Serve | Packaged Drinking Water Delivery Across Southern West Bengal | Zenith',
    'meta_description': 'Zenith Water delivers packaged drinking water across Kolkata, Howrah, Hooghly, Midnapore, 24 Parganas, Durgapur, Asansol & Burdwan. Check service areas & order now.',
    'og_title': 'Areas We Serve | Zenith Water',
    'og_description': 'Complete list of areas served by Zenith Water delivery network across Southern West Bengal.',
    'twitter_title': 'Areas We Serve | Zenith Water',
    'twitter_description': 'Complete list of areas served by Zenith Water delivery network across Southern West Bengal.',
    'service_type': 'Water Delivery',
    'service_schema_description': 'Packaged drinking water delivery service covering major residential, commercial, and industrial areas across Kolkata, Howrah, Hooghly, Midnapore, 24 Parganas, Durgapur, Asansol and Burdwan.',
    'breadcrumb_name': 'Areas We Serve',
    'back_link': 'packaged-drinking-water-kolkata',
    'back_label': 'Kolkata Hub',
    'eyebrow': 'Delivery Network',
    'h1': 'Areas We Serve Across <span style="color: var(--color-accent);">Southern West Bengal</span>',
    'hero_subtitle': 'Zenith Water delivers FSSAI certified packaged drinking water to homes, offices, hotels, and industries across Kolkata, Howrah, Hooghly, Midnapore, 24 Parganas, Durgapur, Asansol and Burdwan.',
    'cta_text': 'Check availability in your area',
    'cta_url': '/',
    'cta_button': 'Verify Pincode',
    'section1_title': 'Kolkata, Hooghly, Midnapore & 24 Parganas',
    'section1_body': '''<p>Our Kolkata Metropolitan and extended district delivery network covers the full region from north to south and east to west.</p>
              <h3 style="color:#fff;font-size:1.25rem;margin:1.5rem 0 1rem;">Kolkata</h3>
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
              </ul>
              <h3 style="color:#fff;font-size:1.25rem;margin:1.5rem 0 1rem;">Hooghly</h3>
              <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-chandannagar" style="color: var(--color-accent); text-decoration: none;">Chandannagar</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-chinsurah" style="color: var(--color-accent); text-decoration: none;">Chinsurah</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-serampore" style="color: var(--color-accent); text-decoration: none;">Serampore</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-bandel" style="color: var(--color-accent); text-decoration: none;">Bandel</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-uttarpara" style="color: var(--color-accent); text-decoration: none;">Uttarpara</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-baidyabati" style="color: var(--color-accent); text-decoration: none;">Baidyabati</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-rishra" style="color: var(--color-accent); text-decoration: none;">Rishra</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/hooghly-water-supply" style="color: var(--color-accent); text-decoration: none;">All Hooghly Zones</a></li>
              </ul>
              <h3 style="color:#fff;font-size:1.25rem;margin:1.5rem 0 1rem;">Midnapore (Midnapur)</h3>
              <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-midnapore" style="color: var(--color-accent); text-decoration: none;">Midnapore / Midnapur</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-kharagpur" style="color: var(--color-accent); text-decoration: none;">Kharagpur</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-haldia" style="color: var(--color-accent); text-decoration: none;">Haldia</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-tamluk" style="color: var(--color-accent); text-decoration: none;">Tamluk</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-contai" style="color: var(--color-accent); text-decoration: none;">Contai</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-ghatal" style="color: var(--color-accent); text-decoration: none;">Ghatal</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-jhargram" style="color: var(--color-accent); text-decoration: none;">Jhargram</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/midnapore-water-supply" style="color: var(--color-accent); text-decoration: none;">All Midnapore Zones</a></li>
              </ul>
              <h3 style="color:#fff;font-size:1.25rem;margin:1.5rem 0 1rem;">24 Parganas</h3>
              <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-barasat" style="color: var(--color-accent); text-decoration: none;">Barasat</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-barrackpore" style="color: var(--color-accent); text-decoration: none;">Barrackpore</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-basirhat" style="color: var(--color-accent); text-decoration: none;">Basirhat</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-bidhannagar" style="color: var(--color-accent); text-decoration: none;">Bidhannagar / Salt Lake</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-rajarhat-24-parganas" style="color: var(--color-accent); text-decoration: none;">Rajarhat / New Town</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-sonarpur-24-parganas" style="color: var(--color-accent); text-decoration: none;">Sonarpur / Baruipur</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-diamond-harbour" style="color: var(--color-accent); text-decoration: none;">Diamond Harbour</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/24-parganas-water-supply" style="color: var(--color-accent); text-decoration: none;">All 24 Parganas Zones</a></li>
              </ul>''',
    'section2_title': 'Howrah, Durgapur, Asansol & Burdwan',
    'section2_body': '''<p>Our Howrah plant and expanding Southern West Bengal distribution network enable fast, reliable delivery across industrial and residential zones.</p>
              <h3 style="color:#fff;font-size:1.25rem;margin:1.5rem 0 1rem;">Howrah</h3>
              <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-howrah-station" style="color: var(--color-accent); text-decoration: none;">Howrah Station</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Shibpur & Botanical Garden</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Bally & Liluah</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Belur & Santragachi</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Andul & Domjur</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;">Uluberia & Amta</li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-howrah" style="color: var(--color-accent); text-decoration: none;">All Howrah Zones</a></li>
              </ul>
              <h3 style="color:#fff;font-size:1.25rem;margin:1.5rem 0 1rem;">Durgapur, Asansol & Burdwan</h3>
              <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-durgapur-city-centre" style="color: var(--color-accent); text-decoration: none;">Durgapur City Centre</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-benachity" style="color: var(--color-accent); text-decoration: none;">Benachity</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-durgapur-steel-township" style="color: var(--color-accent); text-decoration: none;">Durgapur Steel Township</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-asansol-city" style="color: var(--color-accent); text-decoration: none;">Asansol City</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-burnpur" style="color: var(--color-accent); text-decoration: none;">Burnpur</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-raniganj" style="color: var(--color-accent); text-decoration: none;">Raniganj</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-bardhaman-city" style="color: var(--color-accent); text-decoration: none;">Bardhaman / Burdwan City</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/packaged-drinking-water-katwa" style="color: var(--color-accent); text-decoration: none;">Katwa</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/durgapur-water-supply" style="color: var(--color-accent); text-decoration: none;">Durgapur Hub</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/asansol-water-supply" style="color: var(--color-accent); text-decoration: none;">Asansol Hub</a></li>
                <li style="border-left: 2px solid var(--color-accent); padding-left: 1rem;"><a href="/burdwan-water-supply" style="color: var(--color-accent); text-decoration: none;">Burdwan Hub</a></li>
              </ul>''',
    'coverage': ['Salt Lake Sector V', 'Park Street Central', 'Ballygunge South', 'Rajarhat New Town', 'Howrah Station', 'Ranihati Industrial Belt', 'Chandannagar', 'Kharagpur', 'Durgapur City Centre', 'Asansol City', 'Bardhaman City', 'Barasat'],
    'coverage_footer': 'If your area is not listed, contact us. We are continuously expanding our delivery network across Kolkata, Howrah, Hooghly, Midnapore, 24 Parganas, Durgapur, Asansol and Burdwan.',
    'faqs': [
        ('Do you deliver to my area in Kolkata?', 'We deliver to all major Kolkata sectors. Use the pincode checker on our homepage or call us to confirm availability.'),
        ('Do you serve Howrah?', 'Yes, we serve all major Howrah areas from our Ranihati facility with fast local delivery.'),
        ('Do you deliver to Hooghly, Midnapore, 24 Parganas, Durgapur, Asansol and Burdwan?', 'Yes, Zenith Water now delivers FSSAI-certified packaged drinking water across all these districts and cities. Use our district hub pages or WhatsApp us to confirm your pincode.'),
        ('Can you deliver to industrial areas?', 'Yes, we specialize in bulk delivery to factories, warehouses, and labour camps across the Kolkata-Howrah industrial belt and beyond into Durgapur, Asansol and Burdwan.'),
    ],
    'wa_text': 'Hello%20Zenith%2C%20I%20want%20to%20confirm%20delivery%20availability%20in%20my%20area.%20Please%20help.'
}

if __name__ == '__main__':
    html_out = render_page(page)
    output_path = os.path.join(ROOT, 'areas-we-serve.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_out)
    print(f'Generated: {output_path}')
