# Zenith Water — South Bengal Expansion Changelog

**Date:** 2026-07-20  
**Scope:** Expand delivery network from Kolkata & Howrah to full South Bengal corridor:  
`Kolkata, Howrah, Hooghly, Midnapore (Midnapur), 24 Parganas, Durgapur, Asansol, Burdwan`

---

## 1. Summary of Changes

| Deliverable | What Changed |
|-------------|--------------|
| **Generated SEO pages** | 465 intent-specific landing pages (was ~200). Every page has unique title, meta, H1, canonical, schema, FAQ, and internal links. |
| **District hub pages** | 6 new hub pages: `/hooghly-water-supply`, `/midnapore-water-supply`, `/24-parganas-water-supply`, `/durgapur-water-supply`, `/asansol-water-supply`, `/burdwan-water-supply`. |
| **City intent pages** | 7 core intent pages per new district: `/packaged-drinking-water-{city}`, `/water-delivery-{city}`, `/water-supplier-{city}`, `/bulk-water-supply-{city}`, `/bottled-water-{city}`, `/drinking-water-{city}`, `/mineral-water-{city}`. |
| **Locality pages** | 3 intent pages per locality across 59 new localities (Chandannagar, Chinsurah, Serampore, Kharagpur, Haldia, Durgapur City Centre, Asansol City, Bardhaman City, etc.). |
| **Product / Corporate / Industry pages** | City-specific pages now generated for all 8 districts (e.g., `/mineral-water-supplier-durgapur`, `/office-water-delivery-asansol`, `/water-supply-for-factories-hooghly`). |
| **Homepage (`index.html`)** | Updated title, meta, OG/Twitter, geo tags, hero H1, brand authority section, service network, footer, schema `areaServed`, pincode checker (100+ new pincodes), and FAQs. Added a new visual "South Bengal Service Network" section with elegant district cards so the full city list appears in one professional place instead of crammed throughout the page. |
| **Areas We Serve (`areas-we-serve.html`)** | Fully rewritten with all 8 districts, locality grids, hub links, and expanded FAQs. |
| **Sitemap** | 507 unique URLs (no duplicates), all new district/city/locality/corporate/product pages included with proper priorities. |
| **Generator scripts** | `scripts/generate-landing-pages.py` updated with new locality arrays, city coverage maps, schema areaServed, and generic hub/link logic. `scripts/generate-service-areas-page.py` rewritten to use the shared template engine. |

---

## 2. New Districts & Localities Added

### Hooghly
- Chandannagar, Chinsurah, Serampore, Bandel, Uttarpara, Baidyabati, Rishra, Hooghly Industrial Belt

### Midnapore (Midnapur)
- Midnapore, Kharagpur, Haldia, Tamluk, Contai, Ghatal, Jhargram

### 24 Parganas
- Barasat, Barrackpore, Basirhat, Bidhannagar, Rajarhat, New Town, Sonarpur, Diamond Harbour, Behala, Garia

### Durgapur
- Durgapur City Centre, Benachity, Durgapur Steel Township, Bidhan Nagar Durgapur, Fuljhore, ABL Township, Andal

### Asansol
- Asansol City, Burnpur, Raniganj, Kulti, Barabani, Chittaranjan

### Burdwan
- Bardhaman City, Katwa, Kalna, Durgapur, Memari, Panagarh

---

## 3. SEO Architecture per New Page

Every generated page includes:

- **Unique `<title>`** (50–60 chars)
- **Unique `<meta name="description">`** (150–160 chars)
- **Canonical URL**
- **Open Graph + Twitter Card**
- **Single H1** with primary keyword + location
- **Keyword-rich H2/H3** subheadings
- **Semantic HTML5** landmarks
- **JSON-LD Schema:**
  - `Organization` / `LocalBusiness`
  - `WebSite` + `SearchAction`
  - `Service`
  - `Product` + `Offer` (where applicable)
  - `FAQPage`
  - `BreadcrumbList`
- **Expanded `areaServed`** covering all 8 districts
- **Internal linking** via related-pages grid, use-case cards, coverage footer, and navigation
- **WhatsApp-first CTAs** with location-aware pre-filled messages
- **Critical CSS inlined**, non-blocking stylesheet loading, lazy-loaded images

---

## 4. Homepage Enhancements

- **Title:** `Premium Packaged Drinking Water Kolkata, Howrah & South Bengal | Zenith`
- **Meta description** now lists all 8 districts.
- **Geo tags** updated to include all service districts.
- **Hero H1** updated to "Kolkata, Howrah & South Bengal".
- **Pincode checker** expanded with 100+ new pincodes for Hooghly (`712xxx`), Midnapore (`721xxx`), 24 Parganas (`743xxx`), Durgapur/Asansol/Burdwan (`713xxx`).
- **Service Network section** now links to all 8 district hub pages.
- **Footer** includes new "District Hubs" column.
- **Schema:** `areaServed` updated to include Kolkata, Howrah, Hooghly, Paschim & Purba Medinipur, North & South 24 Parganas, Durgapur, Asansol, Bardhaman.
- **FAQs** updated to confirm delivery outside Kolkata/Howrah.

---

## 5. Validation Results

```
Python syntax: OK
Total pages generated: 465
Validation: no issues detected
Sample new pages checked: 19/19 passed
  - h1: exactly 1
  - title, meta description, canonical present
  - @graph, FAQPage, BreadcrumbList schema present
  - OG/Twitter tags present
Internal link audit: 0 broken links on new hub pages
Sitemap: 507 unique URLs, 0 duplicates
```

---

## 6. Files Modified

- `scripts/generate-landing-pages.py`
- `scripts/generate-service-areas-page.py`
- `index.html`
- `areas-we-serve.html`
- `sitemap.xml`
- New generated `.html` pages (474 total root-level pages)

---

## 7. How to Regenerate

```bash
cd /Users/Amaan/Desktop/zenith-water-website
python3 scripts/generate-landing-pages.py
python3 scripts/generate-service-areas-page.py
```

`index.html` is protected from overwrite by the generator (`PROTECTED_PATHS`).

---

## 8. Next Recommended Steps

1. **Replace `G-XXXXXXXXXX`** with a real Google Analytics 4 Measurement ID across all pages.
2. **Add real product images** for the new district pages if geo-specific photography is available.
3. **Create Google Business Profile** listings or service-area pages for Hooghly, Midnapore, Durgapur, Asansol, Burdwan.
4. **Build backlinks** from local directories in the new districts.
5. **Submit updated sitemap** to Google Search Console after deployment.
6. **Run Lighthouse** on the new hub pages to confirm 100/100 scores.

---

*Prepared for Maharani Beverages LLP / Zenith Water.*
