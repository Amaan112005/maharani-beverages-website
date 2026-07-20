#!/usr/bin/env python3
"""
Zenith Water / Maharani Beverages — Programmatic SEO Landing Page Engine (2026).
Generates intent-specific, schema-rich HTML landing pages across product, corporate,
industry, and locality clusters, and updates the sitemap.xml.

Usage:
    python3 scripts/generate-landing-pages.py
"""
import os
import re
import json
import html
from datetime import date

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOMAIN = "https://maharanibeverages.com"
TODAY = "2026-06-21"

# Brand constants
BRAND = "Maharani Beverages LLP"
BRAND_SHORT = "Zenith Water"
PHONE = "+91 82748 37341"
PHONE_E164 = "918274837341"
EMAIL = "marketing@maharanibeverages.com"
FSSAI = "12825999000938"
SIZE_PRICES = {
    "300ml": "6.00",
    "500ml": "10.00",
    "1L": "20.00",
    "2L": "30.00",
    "20L": "80.00",  # indicative MRP for 20L jar; update if needed
}
SIZE_RATINGS = {
    "300ml": ("4.9", "156"),
    "500ml": ("4.9", "243"),
    "1L": ("4.8", "187"),
    "2L": ("4.9", "92"),
    "20L": ("4.9", "318"),
}
PRODUCT_URLS = {
    "300ml": f"{DOMAIN}/pages/product-300ml",
    "500ml": f"{DOMAIN}/pages/product-500ml",
    "1L": f"{DOMAIN}/pages/product-1l",
    "2L": f"{DOMAIN}/pages/product-2l",
    "20L": f"{DOMAIN}/20-liter-water-jar-delivery-kolkata",
}
PRODUCT_IMAGES = {
    "300ml": f"{DOMAIN}/product-300ml-optimized.jpg",
    "500ml": f"{DOMAIN}/product-500ml-optimized.jpg",
    "1L": f"{DOMAIN}/product-1l-optimized.jpg",
    "2L": f"{DOMAIN}/product-2l-optimized.jpg",
    "20L": f"{DOMAIN}/zenith_logo_compact.png",
}
ADDRESS = {
    "street": "Ranihati Industrial Park",
    "locality": "Howrah",
    "region": "West Bengal",
    "country": "IN",
}
SOCIALS = [
    "https://www.instagram.com/zenithwater",
    "https://www.facebook.com/zenithwater",
    "https://www.linkedin.com/company/zenith-water",
]

# Asset paths
LOGO = "zenith_logo_compact.png"
LOGO_DATA_URI = "data:image/webp;base64,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"
CSS_FILES = ["assets/css/variables.min.css", "assets/css/main.min.css", "assets/css/mobile-perfection.min.css?v=1.1"]
JS_FILES = ["assets/js/landing.js"]

# =============================================================================
# CONTENT DATA
# =============================================================================

KOLKATA_LOCALITIES = [
    ("salt-lake", "Salt Lake", "Kolkata", ["Sector V", "Bidhannagar", "Karunamoyee"]),
    ("park-street", "Park Street", "Kolkata", ["Esplanade", "Camac Street", "Theatre Road"]),
    ("ballygunge", "Ballygunge", "Kolkata", ["Rashbehari", "Gariahat", "Hindustan Park"]),
    ("behala", "Behala", "Kolkata", ["New Alipore", "Thakurpukur", "Sarsuna"]),
    ("garia", "Garia", "Kolkata", ["Narendrapur", "New Garia", "Ashaban Housing"]),
    ("jadavpur", "Jadavpur", "Kolkata", ["Ganguly Bagan", "Baghajatin", "Santoshpur"]),
    ("tollygunge", "Tollygunge", "Kolkata", ["Ranikuthi", "Regent Park", "Bansdroni"]),
    ("dum-dum", "Dum Dum", "Kolkata", ["Netaji Subhash Chandra Bose International Airport area", "Dum Dum Cantonment"]),
    ("rajarhat", "Rajarhat", "Kolkata", ["New Town", "Action Area", "Unitech"]),
    ("new-town", "New Town", "Kolkata", ["Rajarhat", "Action Area I", "Eco Park"]),
    ("alipore", "Alipore", "Kolkata", ["New Alipore", "Chetla", "Bhowanipore"]),
    ("camac-street", "Camac Street", "Kolkata", ["Park Street", "AJC Bose Road", "Minto Park"]),
    ("bhawanipore", "Bhowanipore", "Kolkata", ["Hazra", "Kalighat", "Alipore"]),
    ("kasba", "Kasba", "Kolkata", ["East Kolkata Township", "Rubi", "Haltu"]),
    ("sonarpur", "Sonarpur", "Kolkata", ["Narendrapur", "Baruipur", "Rajpur"]),
    ("barasat", "Barasat", "Kolkata", ["Madhyamgram", "New Barrackpore", "Duttapukur"]),
    ("bidhannagar", "Bidhannagar", "Kolkata", ["Salt Lake", "Sector V", "Karunamoyee"]),
    ("kankurgachi", "Kankurgachi", "Kolkata", ["Maniktala", "Phoolbagan", "Salt Lake"]),
    ("maniktala", "Maniktala", "Kolkata", ["Girish Park", "Shobhabazar", "Kankurgachi"]),
    ("shyambazar", "Shyambazar", "Kolkata", ["Hatibagan", "Bagbazar", "Gariahat"]),
]

HOWRAH_LOCALITIES = [
    ("howrah-station", "Howrah Station", "Howrah", ["Salkia", "Howrah Maidan", "Bara Bazaar"]),
    ("shibpur", "Shibpur", "Howrah", ["Botanical Garden", "Mandirtala", "Salkia"]),
    ("bally", "Bally", "Howrah", ["Uttarpara", "Belur", "Liluah"]),
    ("liluah", "Liluah", "Howrah", ["Bally", "Belur", "Kona"]),
    ("belur", "Belur", "Howrah", ["Liluah", "Bally", "Shibpur"]),
    ("santragachi", "Santragachi", "Howrah", ["Andul", "Domjur", "Kona"]),
    ("andul", "Andul", "Howrah", ["Santragachi", "Mourigram", "Bakultala"]),
    ("domjur", "Domjur", "Howrah", ["Jagacha", "Makardaha", "Bargachia"]),
    ("uluberia", "Uluberia", "Howrah", ["Amta", "Bagnan", "Dasnagar"]),
    ("amt", "Amta", "Howrah", ["Uluberia", "Bagnan", "Khalisani"]),
]

ALL_LOCALITIES = KOLKATA_LOCALITIES + HOWRAH_LOCALITIES

INDUSTRY_CONTEXT = {
    "hotels": {
        "label": "Hotels",
        "audience": "hotels, lodges, and guest houses",
        "pain": "high-volume room service, banquet hydration, and lobby dispenser needs",
        "benefit": "consistent supply of sealed premium water that elevates guest experience and brand perception",
        "sizes": "300ml and 500ml room bottles, 1L table bottles, and 20L dispenser jars",
        "cities": ["Kolkata", "Howrah"],
    },
    "restaurants": {
        "label": "Restaurants",
        "audience": "restaurants, cafés, fast-food outlets, and cloud kitchens",
        "pain": "steady table-water availability and take-away packs during peak hours",
        "benefit": "reliable refill cycles so you never run dry during lunch and dinner rushes",
        "sizes": "500ml, 1L, and 2L bottles plus 20L jars for kitchen and dispenser use",
        "cities": ["Kolkata", "Howrah"],
    },
    "hospitals": {
        "label": "Hospitals",
        "audience": "hospitals, nursing homes, clinics, and diagnostic centres",
        "pain": "safe hydration for patients, visitors, and staff with strict hygiene standards",
        "benefit": "FSSAI-certified, sealed-at-source water that supports infection-control protocols",
        "sizes": "300ml patient bottles, 500ml visitor bottles, and 20L jars for staff areas",
        "cities": ["Kolkata", "Howrah"],
    },
    "schools": {
        "label": "Schools",
        "audience": "schools, day-care centres, and coaching institutes",
        "pain": "safe drinking water for children during school hours and events",
        "benefit": "certified purity and child-safe sealed bottles for canteens and dispensers",
        "sizes": "300ml and 500ml bottles plus 20L jars for staff and common areas",
        "cities": ["Kolkata", "Howrah"],
    },
    "colleges": {
        "label": "Colleges",
        "audience": "colleges, universities, and training institutes",
        "pain": "hydration across large campuses, canteens, hostels, and events",
        "benefit": "bulk-capacity supply with scheduled delivery aligned to academic calendars",
        "sizes": "500ml, 1L, and 2L bottles plus 20L jars for hostels and departments",
        "cities": ["Kolkata"],
    },
    "factories": {
        "label": "Factories",
        "audience": "factories, warehouses, and manufacturing units",
        "pain": "high-volume hydration for workers across shifts with minimal downtime",
        "benefit": "palletized bulk supply and 20L jar programs designed for shop-floor use",
        "sizes": "20L jars, 2L bottles, and bulk pallet options",
        "cities": ["Kolkata", "Howrah"],
    },
    "construction-sites": {
        "label": "Construction Sites",
        "audience": "construction sites, builder camps, and civil contractors",
        "pain": "dusty environments require abundant safe water for labour welfare",
        "benefit": "large-volume jar and bottle delivery directly to site gates on recurring schedules",
        "sizes": "20L jars and 1L/2L bottles for on-site distribution",
        "cities": ["Kolkata", "Howrah"],
    },
    "banquet-halls": {
        "label": "Banquet Halls",
        "audience": "banquet halls, wedding venues, and party lawns",
        "pain": "large one-day or weekend events need hundreds of sealed bottles quickly",
        "benefit": "event-size bottled water delivery with coordinated timing for caterers and hosts",
        "sizes": "300ml, 500ml, and 1L bottles plus 20L jars for buffet stations",
        "cities": ["Kolkata"],
    },
    "event-management": {
        "label": "Event Management",
        "audience": "event management companies, conferences, exhibitions, and marathons",
        "pain": "temporary venues need branded or plain bottled water on exact event dates",
        "benefit": "just-in-time bulk delivery across multiple venues with flexible invoicing",
        "sizes": "300ml and 500ml for delegates, 1L/2L for crew, 20L jars for back offices",
        "cities": ["Kolkata"],
    },
    "gyms": {
        "label": "Gyms",
        "audience": "gyms, fitness centres, yoga studios, and sports clubs",
        "pain": "members expect chilled, safe hydration before and after workouts",
        "benefit": "regular supply of premium bottles and jars that align with membership traffic",
        "sizes": "500ml and 1L bottles plus 20L jars for dispenser stations",
        "cities": ["Kolkata"],
    },
}

CORPORATE_CONTEXT = {
    "office-water-supply": {
        "label": "Office Water Supply",
        "audience": "offices and corporate premises",
        "pain": "dependable drinking water for employees without interruption",
        "benefit": "scheduled 20L jar and bottle supply with monthly invoicing",
        "cities": ["Kolkata", "Howrah"],
    },
    "office-water-delivery": {
        "label": "Office Water Delivery",
        "audience": "offices and co-working spaces",
        "pain": "regular delivery windows that match office hours",
        "benefit": "on-time delivery fleet covering all major business districts",
        "cities": ["Kolkata", "Howrah"],
    },
    "corporate-water-supply": {
        "label": "Corporate Water Supply",
        "audience": "corporate campuses and enterprise clients",
        "pain": "centralized hydration across multiple floors and buildings",
        "benefit": "dedicated account management and consolidated billing",
        "cities": ["Kolkata"],
    },
    "commercial-water-supplier": {
        "label": "Commercial Water Supplier",
        "audience": "commercial complexes and business hubs",
        "pain": "multi-tenant buildings need consistent vendor quality",
        "benefit": "scalable supply agreements with FSSAI-certified quality assurance",
        "cities": ["Kolkata"],
    },
    "water-supply-for-it-parks": {
        "label": "IT Parks",
        "audience": "IT parks and technology campuses",
        "pain": "24x7 operations require uninterrupted dispenser water",
        "benefit": "scheduled refills and emergency replenishment for round-the-clock facilities",
        "cities": ["Kolkata"],
    },
    "water-supply-for-co-working-spaces": {
        "label": "Co-working Spaces",
        "audience": "co-working spaces and shared offices",
        "pain": "fluctuating headcount makes inventory planning hard",
        "benefit": "flexible weekly or bi-weekly plans that scale with occupancy",
        "cities": ["Kolkata"],
    },
    "water-supply-for-banks": {
        "label": "Banks",
        "audience": "banks, NBFCs, and financial institutions",
        "pain": "premium customer experience requires premium amenities",
        "benefit": "branded bottled water for branches and staff hydration programs",
        "cities": ["Kolkata"],
    },
    "water-supply-for-call-centers": {
        "label": "Call Centers",
        "audience": "call centres and BPOs",
        "pain": "voice professionals need constant hydration during long shifts",
        "benefit": "high-volume 20L jar programs with frequent refill cycles",
        "cities": ["Kolkata"],
    },
    "water-supply-for-government-offices": {
        "label": "Government Offices",
        "audience": "government offices and public-sector undertakings",
        "pain": "compliant procurement with proper documentation and taxation",
        "benefit": "FSSAI-certified supply with GST invoices and transparent pricing",
        "cities": ["Kolkata"],
    },
}

PRODUCT_CONTEXT = {
    "20-litre-water-jar": {
        "label": "20 Litre Water Jar",
        "headline_city": "{city}",
        "desc": "office and home dispenser jars",
        "sizes": ["20L"],
        "has_product_schema": True,
        "cities": ["Kolkata", "Howrah"],
    },
    "20-litre-jar-supplier": {
        "label": "20 Litre Jar Supplier",
        "headline_city": "{city}",
        "desc": "scheduled 20L jar supply",
        "sizes": ["20L"],
        "has_product_schema": True,
        "cities": ["Kolkata", "Howrah"],
    },
    "water-jar-supplier": {
        "label": "Water Jar Supplier",
        "headline_city": "{city}",
        "desc": "dispenser jar supply",
        "sizes": ["20L"],
        "has_product_schema": True,
        "cities": ["Kolkata", "Howrah"],
    },
    "water-bottle-supplier": {
        "label": "Water Bottle Supplier",
        "headline_city": "{city}",
        "desc": "retail and bulk bottled water",
        "sizes": ["300ml", "500ml", "1L", "2L"],
        "has_product_schema": True,
        "cities": ["Kolkata", "Howrah"],
    },
    "mineral-water-supplier": {
        "label": "Mineral Water Supplier",
        "headline_city": "{city}",
        "desc": "premium packaged mineral water",
        "sizes": ["300ml", "500ml", "1L", "2L", "20L"],
        "has_product_schema": True,
        "cities": ["Kolkata", "Howrah"],
    },
    "drinking-water-supplier": {
        "label": "Drinking Water Supplier",
        "headline_city": "{city}",
        "desc": "safe packaged drinking water",
        "sizes": ["300ml", "500ml", "1L", "2L", "20L"],
        "has_product_schema": True,
        "cities": ["Kolkata", "Howrah"],
    },
    "packaged-water-supplier": {
        "label": "Packaged Water Supplier",
        "headline_city": "{city}",
        "desc": "IS 14543 packaged drinking water",
        "sizes": ["300ml", "500ml", "1L", "2L", "20L"],
        "has_product_schema": True,
        "cities": ["Kolkata", "Howrah"],
    },
    "bisleri-alternative": {
        "label": "Bisleri Alternative",
        "headline_city": "{city}",
        "desc": "affordable premium alternative to Bisleri",
        "sizes": ["300ml", "500ml", "1L", "2L", "20L"],
        "has_product_schema": True,
        "cities": ["Kolkata", "Howrah"],
    },
}

# Existing slugs we should not skip; these are the authoritative pages we always want fresh.
ALWAYS_GENERATE = {
    "index",
    "areas-we-serve",
}

# Paths to protect from accidental overwrite (we never write these via this script).
PROTECTED_PATHS = {
    "index.html",
    "areas-we-serve.html",
    "googlee01cd75741d33e02.html",
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def esc(s):
    """HTML escape a string."""
    return html.escape(str(s), quote=True)


def slugify(name):
    """Convert a display name to a URL-safe slug."""
    s = name.lower()
    s = re.sub(r"[^a-z0-9\s-]+", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s


def truncate(text, length):
    """Truncate text to a target length, ending at a word boundary."""
    if len(text) <= length:
        return text
    return text[: length - 3].rsplit(" ", 1)[0] + "..."


def fit_meta(text, target_min=150, target_max=155):
    """Return a meta description that fits the 150–155 char window.

    Avoids awkward mid-word truncation by trimming at sentence or word boundaries.
    """
    if target_min <= len(text) <= target_max:
        return text

    if len(text) > target_max:
        # Try to trim to a sentence boundary within the window
        for marker in (". ", "; ", ", "):
            # Find the rightmost marker that leaves us inside the window
            pos = text.rfind(marker, target_min - 1, target_max + 1)
            if pos != -1:
                return text[: pos + 1].rstrip()
        # Word-boundary fallback
        trimmed = text[: target_max].rsplit(" ", 1)[0].rstrip(".,;")
        if target_min <= len(trimmed) <= target_max:
            return trimmed + "."
        # Hard trim with ellipsis guard
        return text[: target_max - 1].rstrip() + "."

    # Too short: append clean suffixes
    suffixes = [
        " Order online or call today.",
        " Get same-day delivery across the city.",
        " Trusted by offices, hotels & homes.",
        " FSSAI license 12825999000938.",
        " BIS IS 14543 certified purity.",
    ]
    base = text.rstrip(".")
    for suffix in suffixes:
        candidate = base + suffix
        if target_min <= len(candidate) <= target_max:
            return candidate
        if len(candidate) > target_max:
            # Trim suffix at word boundary, not mid-word
            allowed = target_max - len(base)
            if allowed < 4:
                continue
            trimmed_suffix = suffix[: allowed].rsplit(" ", 1)[0]
            candidate2 = base + trimmed_suffix
            if target_min <= len(candidate2) <= target_max:
                return candidate2
    return text.ljust(target_min)


def city_coverage(city, exclude=None):
    """Return a list of coverage areas for a city."""
    exclude = exclude or []
    if city == "Kolkata":
        base = [
            "Salt Lake & Sector V",
            "Park Street & Esplanade",
            "Ballygunge & Alipore",
            "Behala & New Alipore",
            "Garia & Jadavpur",
            "Tollygunge & Bansdroni",
            "Dum Dum & North Kolkata",
            "Rajarhat & New Town",
            "Shyambazar & Maniktala",
            "Kasba & EM Bypass",
        ]
    else:
        base = [
            "Howrah Station & Salkia",
            "Shibpur & Botanical Garden",
            "Bally & Liluah",
            "Belur & Santragachi",
            "Andul & Domjur",
            "Uluberia & Amta",
            "Ranihati Industrial Belt",
            "Jagacha & Bargachia",
        ]
    return [b for b in base if b not in exclude]


def nearby_localities(locality_slug, city, count=5):
    """Return nearby locality slugs for internal linking."""
    pool = [l for l in ALL_LOCALITIES if l[2] == city and l[0] != locality_slug]
    # Deterministic selection based on index in the original list
    idx = next((i for i, l in enumerate(pool) if l[0] == locality_slug), 0)
    selected = []
    for i in range(1, count + 1):
        selected.append(pool[(idx + i) % len(pool)])
    return selected


def build_faq_schema(faqs):
    """Build FAQPage JSON-LD."""
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


def build_catalog_items():
    """Build OfferCatalog itemListElement with valid Product offers."""
    catalog = [
        ("Zenith 300ml Water", "300ml", "4.9", "156"),
        ("Zenith 500ml Water", "500ml", "4.9", "243"),
        ("Zenith 1L Water", "1L", "4.8", "187"),
        ("Zenith 2L Water", "2L", "4.9", "92"),
        ("Zenith 20L Jar", "20L", "4.9", "318"),
    ]
    items = []
    for name, size, rating, count in catalog:
        items.append({
            "@type": "Offer",
            "itemOffered": {
                "@type": "Product",
                "name": name,
                "image": PRODUCT_IMAGES[size],
                "description": f"FSSAI-certified {name.lower()} delivered across Kolkata and Howrah.",
                "brand": {"@type": "Brand", "name": BRAND_SHORT},
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": rating,
                    "reviewCount": count,
                },
                "offers": {
                    "@type": "Offer",
                    "url": PRODUCT_URLS[size],
                    "price": SIZE_PRICES[size],
                    "priceCurrency": "INR",
                    "priceValidUntil": "2027-12-31",
                    "availability": "https://schema.org/InStock",
                    "seller": {"@type": "Organization", "name": BRAND},
                },
            },
        })
    return items


def build_graph_schema(page):
    """Build the full @graph schema for a page."""
    # Normalize city field
    if "primary_city" not in page and "city" in page:
        page["primary_city"] = page["city"]
    graph = []

    # WebSite
    graph.append({
        "@type": "WebSite",
        "name": f"{BRAND_SHORT} — {BRAND}",
        "url": DOMAIN,
        "potentialAction": {
            "@type": "SearchAction",
            "target": {"@type": "EntryPoint", "urlTemplate": f"{DOMAIN}/?s={{search_term_string}}"},
            "query-input": "required name=search_term_string",
        },
    })

    # Organization / LocalBusiness
    graph.append({
        "@type": ["Organization", "LocalBusiness"],
        "@id": f"{DOMAIN}/#organization",
        "name": BRAND,
        "url": DOMAIN,
        "logo": f"{DOMAIN}/{LOGO}",
        "image": f"{DOMAIN}/{LOGO}",
        "telephone": PHONE,
        "email": EMAIL,
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ADDRESS["street"],
            "addressLocality": ADDRESS["locality"],
            "addressRegion": ADDRESS["region"],
            "addressCountry": ADDRESS["country"],
        },
        "areaServed": ["Kolkata", "Howrah"],
        "sameAs": SOCIALS,
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Packaged Drinking Water",
            "itemListElement": build_catalog_items(),
        },
    })

    # Service
    graph.append({
        "@type": "Service",
        "name": page["service_type"],
        "serviceType": page["service_type"],
        "provider": {"@type": "Organization", "@id": f"{DOMAIN}/#organization"},
        "areaServed": {"@type": "Place", "name": page["primary_city"]},
        "description": page["service_schema_description"],
        "url": f"{DOMAIN}/{page['slug']}",
    })

    # Product + Offer for product-size pages
    if page.get("has_product_schema"):
        for size in page.get("product_sizes", []):
            rating = SIZE_RATINGS.get(size, ("4.9", "100"))
            graph.append({
                "@type": "Product",
                "name": f"Zenith {size} Packaged Drinking Water",
                "image": PRODUCT_IMAGES.get(size, f"{DOMAIN}/{LOGO}"),
                "description": f"FSSAI-certified {size} packaged drinking water supplied across {page['primary_city']}.",
                "brand": {"@type": "Brand", "name": BRAND_SHORT},
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": rating[0],
                    "reviewCount": rating[1],
                },
                "offers": {
                    "@type": "Offer",
                    "url": f"{DOMAIN}/{page['slug']}",
                    "price": SIZE_PRICES.get(size, "0.00"),
                    "priceCurrency": "INR",
                    "priceValidUntil": "2027-12-31",
                    "availability": "https://schema.org/InStock",
                    "seller": {"@type": "Organization", "name": BRAND},
                },
            })

    # BreadcrumbList
    graph.append({
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
            {"@type": "ListItem", "position": 2, "name": page["breadcrumb_name"], "item": f"{DOMAIN}/{page['slug']}"},
        ],
    })

    return {"@context": "https://schema.org", "@graph": graph}


# =============================================================================
# CONTENT GENERATORS
# =============================================================================

def make_generic_faqs(page_name, city, audience="homes and offices"):
    """Generate a robust FAQ list for generic pages."""
    c = city
    return [
        (f"Who is the best {page_name.lower()} in {c}?", f"Zenith Water is a leading {page_name.lower()} in {c}, offering FSSAI-certified packaged drinking water with scheduled delivery and transparent pricing."),
        (f"Do you deliver packaged drinking water to {audience} in {c}?", f"Yes, we supply sealed, certified packaged drinking water to {audience} across {c} with flexible order sizes."),
        (f"What bottle and jar sizes are available in {c}?", f"We offer 300ml, 500ml, 1L, 2L bottles and 20L dispenser jars for {audience} in {c}."),
        (f"Is your water FSSAI and BIS IS 14543 certified?", "Yes, every batch is FSSAI certified and complies with BIS IS 14543 packaged drinking water standards."),
        (f"How fast is delivery in {c}?", f"Most {c} orders are delivered within 24 to 48 hours, with same-day options for select central areas on bulk orders."),
        (f"What is the minimum order quantity?", "We have no strict minimum for retail orders; bulk and subscription plans receive better per-unit pricing."),
        (f"Can I schedule recurring deliveries?", "Yes, you can set daily, alternate-day, weekly, or custom schedules based on your consumption."),
        (f"Do you serve both Kolkata and Howrah?", "Yes, our Ranihati facility and Kolkata distribution network cover both cities."),
        (f"How do I place an order?", "Call +91 82748 37341, WhatsApp, or submit the enquiry form for a quick quote and delivery slot."),
        (f"Do you provide GST invoices for businesses?", "Yes, all B2B deliveries come with proper GST invoices and compliance documentation."),
    ]


def make_industry_faqs(slug, city, ctx):
    label = ctx["label"]
    audience = ctx["audience"]
    sizes = ctx["sizes"]
    return [
        (f"Do you supply water to {audience} in {city}?", f"Yes, Zenith Water provides FSSAI-certified packaged drinking water specifically for {audience} across {city}."),
        (f"What bottle sizes do you recommend for {label.lower()}?", f"For {label.lower()}, we recommend {sizes}. Custom combinations are available on request."),
        (f"Can you handle large-volume orders for {label.lower()}?", f"Yes, we supply palletized bulk orders and recurring 20L jar programs suitable for {label.lower()}."),
        (f"Is same-day delivery available for {audience} in {city}?", f"Same-day delivery may be available for central {city} locations; standard delivery is 24–48 hours."),
        (f"Do you provide GST invoices and compliance documents?", "Yes, every B2B delivery includes GST invoices, FSSAI license details, and batch traceability."),
        (f"How do I set up a recurring supply contract?", "Contact us with your monthly volume and schedule; we will draft a supply agreement with fixed delivery windows."),
        (f"Is the water safe for patients and children?", "Yes, our 7-stage purification and sealed packaging make it safe for all age groups and sensitive settings."),
        (f"Do you cover both Kolkata and Howrah?", "Yes, we deliver across Kolkata and Howrah from our Ranihati manufacturing facility."),
        (f"What is the shelf life of Zenith bottled water?", "Sealed bottles are best consumed before the expiry date printed on the cap, typically 6 months from packing."),
        (f"Can I get a free sample for my premises?", "Yes, sample bottles or jars can be arranged for qualified business enquiries in Kolkata and Howrah."),
    ]


def make_corporate_faqs(slug, city, ctx):
    label = ctx["label"]
    audience = ctx["audience"]
    return [
        (f"Do you provide {label.lower()} in {city}?", f"Yes, Zenith Water specializes in {label.lower()} for {audience} across {city}."),
        (f"What is the minimum order for {audience}?", "We cater to small offices as well as large campuses; monthly plans are tailored to headcount."),
        (f"Can you deliver 20L jars on a recurring schedule?", "Yes, recurring 20L jar delivery is our most popular corporate plan with fixed weekly or bi-weekly slots."),
        (f"Do you offer corporate billing and GST invoices?", "Yes, we provide GST-compliant invoices, purchase orders, and credit terms for eligible enterprises."),
        (f"Which areas in {city} do you cover?", f"We cover all major business districts and industrial zones in {city}, plus extended suburbs on request."),
        (f"Is the water FSSAI certified?", "Yes, Zenith Water is FSSAI certified with license number 12825999000938 and meets BIS IS 14543 standards."),
        (f"Can you support multiple office locations?", "Yes, we can set up multi-location delivery schedules under a single corporate account."),
        (f"How do I request a quotation?", "Call +91 82748 37341 or WhatsApp us with your location and monthly volume for an instant quote."),
        (f"Do you supply branded or plain bottles?", "We primarily supply Zenith-branded sealed bottles; custom labelling can be discussed for large event orders."),
        (f"What makes Zenith different from other vendors?", "Local manufacturing, certified quality, scheduled delivery, and dedicated account support set us apart."),
    ]


def make_locality_faqs(locality, city, nearby):
    loc = locality
    c = city
    nearby_name = nearby[0][1] if nearby else "the next zone"
    return [
        (f"Where can I get packaged drinking water in {loc}, {c}?", f"Zenith Water delivers FSSAI-certified packaged drinking water directly to homes, offices, and businesses in {loc}, {c}."),
        (f"Do you provide home water delivery in {loc}?", f"Yes, we offer home delivery of bottles and 20L jars in {loc} with scheduled slots."),
        (f"Is same-day water delivery available in {loc}?", f"Same-day delivery may be available for bulk orders in {loc}; standard delivery is typically within 24–48 hours."),
        (f"What sizes are available for delivery in {loc}?", f"We deliver 300ml, 500ml, 1L, 2L bottles and 20L dispenser jars in {loc}."),
        (f"Do you supply offices and shops in {loc}?", f"Yes, offices, shops, clinics, and institutions in {loc} can set up recurring supply plans."),
        (f"Is Zenith water FSSAI certified?", "Yes, all Zenith packaged drinking water is FSSAI certified and complies with BIS IS 14543."),
        (f"How do I order water in {loc}?", f"Call +91 82748 37341 or WhatsApp us with your {loc} address for quick confirmation and scheduling."),
        (f"Do you deliver to nearby areas like {nearby_name}?", f"Yes, our fleet also covers {nearby_name} and surrounding {c} localities from our local dispatch centre."),
        (f"What is the minimum order for {loc}?", "Retail orders are accepted with no strict minimum; bulk orders receive discounted per-unit pricing."),
        (f"Can I set up a monthly subscription?", f"Yes, monthly and quarterly subscription plans are available for {loc} residents and businesses."),
    ]


def make_product_faqs(slug, city, ctx):
    label = ctx["label"]
    sizes = ctx["sizes"]
    return [
        (f"Where can I buy {label.lower()} in {city}?", f"Zenith Water supplies {label.lower()} across {city}. Call or WhatsApp +91 82748 37341 to place an order."),
        (f"What sizes do you offer?", f"We offer {', '.join(sizes)} sizes to match home, office, and event requirements."),
        (f"Is the 20L jar compatible with standard dispensers?", "Yes, our 20L jars fit all standard top-load and bottom-load water dispensers."),
        (f"Do you offer bulk pricing for {label.lower()}?", f"Yes, bulk and recurring orders receive discounted pricing for {label.lower()} in {city}."),
        (f"Is Zenith water safe for daily consumption?", "Yes, it is processed through 7-stage purification and is FSSAI and BIS IS 14543 certified."),
        (f"How fast is delivery in {city}?", f"Standard delivery in {city} is 24–48 hours; same-day options may be available for central areas."),
        (f"Do you supply 20L jars to offices?", "Yes, 20L jars are our most popular office hydration solution with scheduled refill delivery."),
        (f"Can I order a mix of bottle sizes?", "Yes, mixed-size orders are welcome for hotels, events, and offices."),
        (f"What is the shelf life?", "Sealed bottles and jars have a shelf life of approximately 6 months from the packing date."),
        (f"Do you deliver to Howrah as well?", "Yes, we manufacture at Ranihati, Howrah, and deliver across both Kolkata and Howrah."),
    ]


# =============================================================================
# PAGE DEFINITION BUILDERS
# =============================================================================

def make_product_pages():
    pages = []
    for key, ctx in PRODUCT_CONTEXT.items():
        for city in ctx["cities"]:
            city_slug = slugify(city)
            if key in ("20-litre-water-jar",):
                slug = f"{key}-{city_slug}" if city == "Kolkata" else f"{key}-{city_slug}"
            elif key == "bisleri-alternative":
                slug = f"{key}-{city_slug}"
            else:
                slug = f"{key}-{city_slug}"

            # Special existing slug handling
            if key == "20-litre-water-jar" and city == "Kolkata":
                slug = "20-liter-water-jar-delivery-kolkata"

            label = ctx["label"]
            display = label.replace("20 Litre", "20 Litre").replace("Water Jar", "Water Jar")
            title = truncate(f"{label} {city} | FSSAI Certified Packaged Water | Zenith", 60)
            meta = fit_meta(
                f"Buy {label.lower()} in {city}. Zenith Water delivers FSSAI certified packaged drinking water "
                f"for homes, offices & events. Call +91 82748 37341."
            )
            h1 = f"{label} Supplier in <span style='color: var(--color-accent);'>{city}</span>"
            eyebrow = f"{label} {city}"
            service_type = f"{label} Supply"

            pages.append({
                "slug": slug,
                "city": city,
                "title": title,
                "meta_description": meta,
                "og_title": title,
                "og_description": truncate(f"Trusted {label.lower()} in {city}. Scheduled delivery of certified packaged drinking water.", 200),
                "twitter_title": title,
                "twitter_description": truncate(f"Trusted {label.lower()} in {city}. Scheduled delivery of certified packaged drinking water.", 200),
                "service_type": service_type,
                "service_schema_description": truncate(f"{label} supply in {city} providing FSSAI certified packaged drinking water for homes, offices, and events.", 250),
                "breadcrumb_name": f"{label} {city}",
                "eyebrow": eyebrow,
                "h1": h1,
                "hero_subtitle": f"Zenith Water supplies {label.lower()} in {city} with FSSAI-certified quality, flexible sizes, and dependable delivery.",
                "section1_title": f"Why Choose Zenith for {label} in {city}",
                "section1_body": _product_section1(ctx, city),
                "section2_title": f"Delivery & Sizes Available",
                "section2_body": _product_section2(ctx, city),
                "coverage": city_coverage(city),
                "coverage_footer": f"We deliver {label.lower()} across {city} and surrounding areas. <a href='/bulk-water-supply-{city_slug}' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>Get bulk pricing ↗</a>",
                "faqs": make_product_faqs(slug, city, ctx),
                "wa_text": f"Hello%20Zenith%2C%20I%20am%20looking%20for%20{label.lower().replace(' ', '%20')}%20in%20{city}.%20Please%20share%20details.",
                "has_product_schema": ctx["has_product_schema"],
                "product_sizes": ctx["sizes"],
                "cluster": "product",
            })
    return pages


def _product_section1(ctx, city):
    lines = []
    for size in ctx["sizes"]:
        if size == "20L":
            lines.append(f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>20L Dispenser Jars</strong>Ideal for offices, factories, and homes in {city} that use water dispensers.</li>")
        elif size == "300ml":
            lines.append(f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>300ml Bottles</strong>Compact serves for conferences, hotels, and retail counters in {city}.</li>")
        elif size == "500ml":
            lines.append(f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>500ml Bottles</strong>The everyday choice for offices, gyms, and events across {city}.</li>")
        elif size == "1L":
            lines.append(f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>1L Bottles</strong>Great for hospitality tables, family use, and premium retail in {city}.</li>")
        elif size == "2L":
            lines.append(f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>2L Bottles</strong>Perfect for gyms, canteens, and households that need more volume.</li>")
    return "<ul style='list-style: none; padding: 0;'>" + "".join(lines) + "</ul>"


def _product_section2(ctx, city):
    sizes = ", ".join(ctx["sizes"])
    return (
        f"<p>Our {city} distribution network carries {sizes} options so you can choose the right pack for every use case. "
        f"All units are sealed at our Ranihati facility and processed through 7-stage purification.</p>"
        f"<p style='margin-top: 1.5rem;'>For offices and recurring needs, we recommend the 20L jar program with scheduled refills. "
        f"<a href='/office-water-delivery-{slugify(city)}' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>View office delivery options ↗</a>.</p>"
    )


def make_corporate_pages():
    pages = []
    for key, ctx in CORPORATE_CONTEXT.items():
        for city in ctx["cities"]:
            city_slug = slugify(city)
            slug = f"{key}-{city_slug}" if key not in ("office-water-delivery", "office-water-supply") else f"{key}-{city_slug}"
            # Preserve existing slug for Kolkata office-water-delivery
            if key == "office-water-delivery" and city == "Kolkata":
                slug = "office-water-delivery-kolkata"
            label = ctx["label"]
            title = truncate(f"{label} {city} | Bulk Office Water Delivery | Zenith", 60)
            meta = fit_meta(
                f"{label} in {city}. Zenith Water delivers FSSAI certified packaged drinking water to {ctx['audience']} with scheduled supply. Call +91 82748 37341."
            )
            h1 = f"{label} in <span style='color: var(--color-accent);'>{city}</span>"
            pages.append({
                "slug": slug,
                "city": city,
                "title": title,
                "meta_description": meta,
                "og_title": title,
                "og_description": truncate(f"Reliable {label.lower()} in {city}. Scheduled delivery for {ctx['audience']}.", 200),
                "twitter_title": title,
                "twitter_description": truncate(f"Reliable {label.lower()} in {city}. Scheduled delivery for {ctx['audience']}.", 200),
                "service_type": label,
                "service_schema_description": truncate(f"{label} services in {city} for {ctx['audience']} with FSSAI certified packaged drinking water.", 250),
                "breadcrumb_name": f"{label} {city}",
                "eyebrow": f"Corporate Hydration Solutions",
                "h1": h1,
                "hero_subtitle": f"Zenith Water provides {label.lower()} in {city} for {ctx['audience']}. FSSAI-certified, scheduled delivery, and GST billing.",
                "section1_title": f"Why {ctx['audience'].capitalize()} Choose Zenith",
                "section1_body": _corporate_section1(ctx, city),
                "section2_title": f"How {label} Works in {city}",
                "section2_body": _corporate_section2(ctx, city),
                "coverage": city_coverage(city),
                "coverage_footer": f"Custom supply schedules are available for enterprise clients across {city}. <a href='/bulk-water-supply-{city_slug}' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>Explore bulk options ↗</a>",
                "faqs": make_corporate_faqs(slug, city, ctx),
                "wa_text": f"Hello%20Zenith%2C%20I%20need%20{label.lower().replace(' ', '%20')}%20in%20{city}.%20Please%20share%20details.",
                "has_product_schema": False,
                "cluster": "corporate",
            })
    return pages


def _corporate_section1(ctx, city):
    return (
        "<ul style='list-style: none; padding: 0;'>"
        f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Solves {ctx['pain'].capitalize()}</strong>We design schedules that prevent stock-outs and keep hydration points full.</li>"
        f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Certified Quality</strong>FSSAI and BIS IS 14543 compliant water sealed at our Ranihati plant.</li>"
        f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Business Friendly</strong>GST invoices, purchase-order support, and flexible payment terms.</li>"
        "</ul>"
    )


def _corporate_section2(ctx, city):
    cslug = slugify(ctx['cities'][0])
    return (
        f"<p>Start with a quick call or WhatsApp to discuss your headcount, premises, and preferred delivery frequency. "
        f"Our team drafts a supply plan, confirms rates, and activates scheduled delivery across {city}.</p>"
        f"<p style='margin-top: 1.5rem;'>For larger campuses, we assign a dedicated account manager. "
        f"<a href='/water-supply-for-factories-industries-kolkata-howrah' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>See industrial supply ↗</a>.</p>"
    )


def make_industry_pages():
    pages = []
    for key, ctx in INDUSTRY_CONTEXT.items():
        for city in ctx["cities"]:
            city_slug = slugify(city)
            # Build slug from key
            slug = f"water-supply-for-{key}-{city_slug}"
            # Preserve existing long slugs for known pages
            if key == "hotels" and city == "Kolkata":
                slug = "water-supply-for-hotels-restaurants-kolkata"
            if key == "factories" and city == "Kolkata":
                slug = "water-supply-for-factories-industries-kolkata-howrah"
            label = ctx["label"]
            title = truncate(f"Water Supply for {label} {city} | Zenith Water", 60)
            meta = fit_meta(
                f"Water supply for {label.lower()} in {city}. Zenith delivers FSSAI certified packaged drinking water to {ctx['audience']}. Call +91 82748 37341."
            )
            h1 = f"Water Supply for {label} in <span style='color: var(--color-accent);'>{city}</span>"
            pages.append({
                "slug": slug,
                "city": city,
                "title": title,
                "meta_description": meta,
                "og_title": title,
                "og_description": truncate(f"Reliable water supply for {label.lower()} in {city}. FSSAI certified delivery.", 200),
                "twitter_title": title,
                "twitter_description": truncate(f"Reliable water supply for {label.lower()} in {city}. FSSAI certified delivery.", 200),
                "service_type": f"Water Supply for {label}",
                "service_schema_description": truncate(f"Water supply services for {ctx['audience']} in {city} with FSSAI certified packaged drinking water.", 250),
                "breadcrumb_name": f"Water Supply for {label} {city}",
                "eyebrow": f"Industry-Specific Hydration",
                "h1": h1,
                "hero_subtitle": f"Zenith Water supplies {label.lower()} in {city} with {ctx['sizes']}. FSSAI certified, scheduled delivery, and bulk pricing.",
                "section1_title": f"Hydration Solutions for {label} in {city}",
                "section1_body": _industry_section1(ctx, city),
                "section2_title": f"Why {label} Trust Zenith",
                "section2_body": _industry_section2(ctx, city),
                "coverage": city_coverage(city),
                "coverage_footer": f"We serve {ctx['audience']} across {city} and surrounding districts. <a href='/bulk-water-supply-{city_slug}' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>Get bulk pricing ↗</a>",
                "faqs": make_industry_faqs(slug, city, ctx),
                "wa_text": f"Hello%20Zenith%2C%20I%20need%20water%20supply%20for%20{label.lower().replace(' ', '%20')}%20in%20{city}.%20Please%20share%20details.",
                "has_product_schema": False,
                "cluster": "industry",
            })
    return pages


def _industry_section1(ctx, city):
    return (
        "<ul style='list-style: none; padding: 0;'>"
        f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Built for {ctx['label']}</strong>We understand the {ctx['pain']} and tailor supply frequency accordingly.</li>"
        f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Recommended Sizes</strong>{ctx['sizes']}.</li>"
        f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Quality Assurance</strong>Every batch is tested and sealed at our Ranihati facility under FSSAI and BIS IS 14543.</li>"
        "</ul>"
    )


def _industry_section2(ctx, city):
    return (
        f"<p>{ctx['benefit'].capitalize()}. Our team plans delivery routes, inventory cycles, and emergency refills so you can focus on operations.</p>"
        f"<p style='margin-top: 1.5rem;'>We also support related sectors such as offices, events, and factories. "
        f"<a href='/office-water-delivery-{slugify(city)}' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>Explore office delivery ↗</a>.</p>"
    )


def make_hub_pages():
    """Generate city hub pages that act as SEO silo homepages."""
    pages = []
    for city in ["Kolkata", "Howrah"]:
        city_slug = slugify(city)
        slug = f"{city_slug}-water-supply"
        title = truncate(f"Water Supply {city} | Packaged Drinking Water | Zenith", 60)
        meta = fit_meta(
            f"Zenith Water is the trusted water supply partner in {city}. "
            f"FSSAI certified packaged drinking water for homes, offices, hotels & industries. Call +91 82748 37341."
        )
        pages.append({
            "slug": slug,
            "city": city,
            "title": title,
            "meta_description": meta,
            "og_title": title,
            "og_description": truncate(f"Complete water supply solutions in {city}. FSSAI certified, scheduled delivery.", 200),
            "twitter_title": title,
            "twitter_description": truncate(f"Complete water supply solutions in {city}. FSSAI certified, scheduled delivery.", 200),
            "service_type": f"Packaged Drinking Water Supply {city}",
            "service_schema_description": truncate(
                f"Zenith Water supplies FSSAI certified packaged drinking water across {city} for residential, commercial, and industrial clients.", 250
            ),
            "breadcrumb_name": f"Water Supply {city}",
            "eyebrow": f"{city} Water Supply Hub",
            "h1": f"Packaged Drinking Water Supply in <span style='color: var(--color-accent);'>{city}</span>",
            "hero_subtitle": f"The complete guide to certified water supply in {city}. Bottles, 20L jars, bulk delivery, and industry-specific solutions — all from Zenith Water.",
            "section1_title": f"Every Water Solution You Need in {city}",
            "section1_body": _hub_section1(city),
            "section2_title": f"Why {city} Chooses Zenith Water",
            "section2_body": _hub_section2(city),
            "coverage": city_coverage(city),
            "coverage_footer": f"We deliver to every major neighbourhood and industrial belt in {city}. <a href='/areas-we-serve' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>View all service areas ↗</a>",
            "faqs": make_generic_faqs("water supply", city),
            "wa_text": f"Hello%20Zenith%2C%20I%20need%20water%20supply%20in%20{city}.%20Please%20share%20details.",
            "has_product_schema": False,
            "cluster": "hub",
        })
    return pages


def _hub_section1(city):
    cslug = slugify(city)
    if city == "Kolkata":
        corporate_link = "<a href='/corporate-water-supply-kolkata'>corporate supply</a>"
        it_parks_link = "<a href='/water-supply-for-it-parks-kolkata'>IT park supply</a>"
        hotels_link = "<a href='/water-supply-for-hotels-restaurants-kolkata'>hotels</a>"
        factories_link = "<a href='/water-supply-for-factories-industries-kolkata-howrah'>factories</a>"
    else:  # Howrah
        corporate_link = "<a href='/office-water-supply-howrah'>office supply</a>"
        it_parks_link = "<a href='/water-supply-for-it-parks-kolkata'>IT park supply</a>"
        hotels_link = "<a href='/water-supply-for-hotels-howrah'>hotels</a>"
        factories_link = "<a href='/water-supply-for-factories-howrah'>factories</a>"
    return (
        f"<p>Whether you need a single home delivery or a recurring bulk contract, Zenith Water covers every segment of the {city} market. "
        f"Explore our product pages for <a href='/water-bottle-supplier-{cslug}'>bottled water</a>, "
        f"<a href='/20-litre-jar-supplier-{cslug}'>20L dispenser jars</a>, and "
        f"<a href='/mineral-water-supplier-{cslug}'>mineral water</a> options.</p>"
        f"<p style='margin-top: 1.5rem;'>For businesses, our corporate cluster includes "
        f"<a href='/office-water-delivery-{cslug}'>office water delivery</a>, "
        f"{corporate_link}, and "
        f"{it_parks_link}. "
        f"Industry-specific solutions cover {hotels_link}, "
        f"<a href='/water-supply-for-restaurants-{cslug}'>restaurants</a>, "
        f"<a href='/water-supply-for-hospitals-{cslug}'>hospitals</a>, "
        f"<a href='/water-supply-for-schools-{cslug}'>schools</a>, and "
        f"{factories_link}.</p>"
    )


def _hub_section2(city):
    cslug = slugify(city)
    return (
        f"<p>Our Ranihati plant and {city} distribution fleet give us the shortest lead times in the region. "
        f"Every batch is FSSAI certified (license 12825999000938) and meets BIS IS 14543 standards.</p>"
        f"<p style='margin-top: 1.5rem;'>Ready to start? "
        f"<a href='/bulk-water-supply-{cslug}' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>Get a bulk quote ↗</a>, "
        f"<a href='/pages/contact' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>send an enquiry ↗</a>, or "
        f"call +91 82748 37341 for immediate assistance.</p>"
    )


def make_locality_pages():
    pages = []
    for slug, loc_name, city, nearby_areas in ALL_LOCALITIES:
        city_slug = slugify(city)
        for intent in ("packaged-drinking-water", "water-delivery", "water-supplier"):
            page_slug = f"{intent}-{slug}"
            if intent == "packaged-drinking-water":
                title = truncate(f"Packaged Drinking Water {loc_name} {city} | Zenith", 60)
                meta = fit_meta(f"Buy packaged drinking water in {loc_name}, {city}. FSSAI certified 300ml, 500ml, 1L, 2L bottles & 20L jars with same-day delivery. Call +91 82748 37341.")
                eyebrow = "Local Packaged Water"
                h1 = f"Packaged Drinking Water in <span style='color: var(--color-accent);'>{loc_name}</span>, {city}"
                hero = f"Zenith Water delivers FSSAI-certified packaged drinking water in {loc_name}, {city}. Bottles and 20L jars delivered to your door."
                service = "Packaged Drinking Water Delivery"
                sdesc = f"Packaged drinking water delivery in {loc_name}, {city} for homes, offices, and shops."
                sec1_title = f"Why {loc_name} Chooses Zenith"
                sec1_body = (
                    "<ul style='list-style: none; padding: 0;'>"
                    f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Neighbourhood Delivery</strong>We route deliveries through {loc_name} and nearby sectors daily.</li>"
                    f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Certified Purity</strong>FSSAI and BIS IS 14543 certified water sealed at source.</li>"
                    f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Flexible Orders</strong>From a single bottle to monthly 20L jar plans for {loc_name} households and offices.</li>"
                    "</ul>"
                )
                sec2_title = f"Coverage Around {loc_name}"
                sec2_body = (
                    f"<p>Our fleet covers {loc_name}, {', '.join(nearby_areas[:3])}, and surrounding neighbourhoods in {city}. "
                    f"Whether you live in a housing complex or run a shop, we can schedule regular deliveries.</p>"
                    f"<p style='margin-top: 1.5rem;'>For bulk requirements, explore <a href='/bulk-water-supply-{city_slug}' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>{city} bulk supply ↗</a>.</p>"
                )
                wa = f"Hello%20Zenith%2C%20I%20need%20packaged%20drinking%20water%20in%20{loc_name.replace(' ', '%20')}%2C%20{city}."
            elif intent == "water-delivery":
                title = truncate(f"Water Delivery {loc_name} {city} | Zenith Water", 60)
                meta = fit_meta(f"Fast water delivery in {loc_name}, {city}. Zenith delivers FSSAI certified bottled water & 20L jars for home, office & shop. Call +91 82748 37341.")
                eyebrow = "Scheduled Water Delivery"
                h1 = f"Water Delivery in <span style='color: var(--color-accent);'>{loc_name}</span>, {city}"
                hero = f"Reliable water delivery in {loc_name}, {city}. Order bottles or 20L jars for home, office, or shop with scheduled slots."
                service = "Drinking Water Delivery"
                sdesc = f"Drinking water delivery service in {loc_name}, {city} for homes and offices."
                sec1_title = f"How Delivery Works in {loc_name}"
                sec1_body = (
                    "<ul style='list-style: none; padding: 0;'>"
                    f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Place Your Order</strong>Call or WhatsApp with your {loc_name} address and preferred quantity.</li>"
                    f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Choose a Slot</strong>Select one-time or recurring delivery that fits your schedule.</li>"
                    f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Receive Sealed Water</strong>Our delivery team brings FSSAI-certified bottles and jars to your {loc_name} location.</li>"
                    "</ul>"
                )
                sec2_title = f"Areas We Deliver Near {loc_name}"
                sec2_body = (
                    f"<p>We deliver to {loc_name}, {', '.join(nearby_areas[:3])}, and nearby {city} localities. "
                    f"Bulk orders for apartments and offices are delivered on priority.</p>"
                    f"<p style='margin-top: 1.5rem;'><a href='/water-delivery-{city_slug}' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>View all {city} delivery areas ↗</a>.</p>"
                )
                wa = f"Hello%20Zenith%2C%20I%20need%20water%20delivery%20in%20{loc_name.replace(' ', '%20')}%2C%20{city}."
            else:  # water-supplier
                title = truncate(f"Water Supplier {loc_name} {city} | Zenith Water", 60)
                meta = fit_meta(f"Trusted water supplier in {loc_name}, {city}. FSSAI certified packaged drinking water for homes, offices, hotels & shops. Call +91 82748 37341.")
                eyebrow = "Authorised Local Supplier"
                h1 = f"Water Supplier in <span style='color: var(--color-accent);'>{loc_name}</span>, {city}"
                hero = f"Zenith Water is a trusted water supplier in {loc_name}, {city}. We deliver certified packaged drinking water to homes, offices, and shops."
                service = "Packaged Drinking Water Supply"
                sdesc = f"Water supplier in {loc_name}, {city} providing certified packaged drinking water for residential and commercial clients."
                sec1_title = f"Why {loc_name} Relies on Zenith"
                sec1_body = (
                    "<ul style='list-style: none; padding: 0;'>"
                    f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Local Availability</strong>We maintain regular supply routes through {loc_name} and surrounding sectors.</li>"
                    f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>Quality Certified</strong>FSSAI license {FSSAI} and BIS IS 14543 compliance for every unit.</li>"
                    f"<li style='margin-bottom: 2rem; border-left: 2px solid var(--color-accent); padding-left: 2rem;'><strong style='color: white; display: block; margin-bottom: 0.5rem;'>All Sizes</strong>300ml to 20L jars for households, offices, and commercial users in {loc_name}.</li>"
                    "</ul>"
                )
                sec2_title = f"Supply Coverage Near {loc_name}"
                sec2_body = (
                    f"<p>Zenith supplies water to {loc_name}, {', '.join(nearby_areas[:3])}, and nearby neighbourhoods in {city}. "
                    f"Recurring plans help households and businesses never run out.</p>"
                    f"<p style='margin-top: 1.5rem;'><a href='/water-supplier-{city_slug}' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>See {city} supplier page ↗</a>.</p>"
                )
                wa = f"Hello%20Zenith%2C%20I%20am%20looking%20for%20a%20water%20supplier%20in%20{loc_name.replace(' ', '%20')}%2C%20{city}."

            coverage = [f"{loc_name} core area"] + [f"{a}" for a in nearby_areas[:5]]
            nearby = nearby_localities(slug, city, count=5)
            faqs = make_locality_faqs(loc_name, city, nearby)
            pages.append({
                "slug": page_slug,
                "city": city,
                "title": title,
                "meta_description": meta,
                "og_title": title,
                "og_description": truncate(f"Trusted {intent.replace('-', ' ')} in {loc_name}, {city}. FSSAI certified delivery.", 200),
                "twitter_title": title,
                "twitter_description": truncate(f"Trusted {intent.replace('-', ' ')} in {loc_name}, {city}. FSSAI certified delivery.", 200),
                "service_type": service,
                "service_schema_description": truncate(sdesc, 250),
                "breadcrumb_name": f"{intent.replace('-', ' ').title()} {loc_name}",
                "eyebrow": eyebrow,
                "h1": h1,
                "hero_subtitle": hero,
                "section1_title": sec1_title,
                "section1_body": sec1_body,
                "section2_title": sec2_title,
                "section2_body": sec2_body,
                "coverage": coverage,
                "coverage_footer": f"We also deliver to nearby {city} localities. <a href='/areas-we-serve' style='color: var(--color-accent); text-decoration: none; border-bottom: 1px solid var(--color-accent);'>View all service areas ↗</a>",
                "faqs": faqs,
                "wa_text": wa,
                "has_product_schema": False,
                "cluster": "locality",
                "locality": loc_name,
                "nearby_localities": nearby,
            })
    return pages


# =============================================================================
# RELATED PAGE MAPS
# =============================================================================

CORE_LINKS = [
    ("/", "Home"),
    ("/pages/products", "Our Products"),
    ("/packaged-drinking-water-kolkata", "Packaged Drinking Water Kolkata"),
    ("/bulk-water-supply-kolkata", "Bulk Water Supply Kolkata"),
    ("/packaged-drinking-water-howrah", "Packaged Drinking Water Howrah"),
    ("/bulk-water-supply-howrah", "Bulk Water Supply Howrah"),
    ("/areas-we-serve", "Areas We Serve"),
    ("/pages/contact", "Contact Us"),
    ("/pages/compliance", "Compliance"),
    ("/blog", "Blog"),
    ("/office-water-delivery-kolkata", "Office Water Delivery Kolkata"),
    ("/water-supply-for-hotels-restaurants-kolkata", "Water Supply for Hotels & Restaurants"),
    ("/water-supply-for-factories-industries-kolkata-howrah", "Water Supply for Factories & Industries"),
]

PRODUCT_LINKS = [
    ("/20-liter-water-jar-delivery-kolkata", "20L Jar Delivery Kolkata"),
    ("/20-litre-jar-supplier-kolkata", "20L Jar Supplier Kolkata"),
    ("/water-jar-supplier-kolkata", "Water Jar Supplier Kolkata"),
    ("/water-bottle-supplier-kolkata", "Water Bottle Supplier Kolkata"),
    ("/mineral-water-supplier-kolkata", "Mineral Water Supplier Kolkata"),
    ("/drinking-water-supplier-kolkata", "Drinking Water Supplier Kolkata"),
    ("/packaged-water-supplier-kolkata", "Packaged Water Supplier Kolkata"),
    ("/bisleri-alternative-kolkata", "Bisleri Alternative Kolkata"),
    ("/bottled-water-kolkata", "Bottled Water Kolkata"),
    ("/water-delivery-kolkata", "Water Delivery Kolkata"),
]

CORPORATE_LINKS = [
    ("/office-water-supply-kolkata", "Office Water Supply Kolkata"),
    ("/office-water-delivery-kolkata", "Office Water Delivery Kolkata"),
    ("/corporate-water-supply-kolkata", "Corporate Water Supply Kolkata"),
    ("/commercial-water-supplier-kolkata", "Commercial Water Supplier Kolkata"),
    ("/water-supply-for-it-parks-kolkata", "Water Supply for IT Parks"),
    ("/water-supply-for-co-working-spaces-kolkata", "Water Supply for Co-working Spaces"),
    ("/water-supply-for-banks-kolkata", "Water Supply for Banks"),
    ("/water-supply-for-call-centers-kolkata", "Water Supply for Call Centers"),
    ("/water-supply-for-government-offices-kolkata", "Water Supply for Government Offices"),
    ("/bulk-water-supply-kolkata", "Bulk Water Supply Kolkata"),
]

INDUSTRY_LINKS = [
    ("/water-supply-for-hotels-restaurants-kolkata", "Water Supply for Hotels & Restaurants"),
    ("/water-supply-for-hospitals-kolkata", "Water Supply for Hospitals"),
    ("/water-supply-for-schools-kolkata", "Water Supply for Schools"),
    ("/water-supply-for-colleges-kolkata", "Water Supply for Colleges"),
    ("/water-supply-for-factories-industries-kolkata-howrah", "Water Supply for Factories"),
    ("/water-supply-for-construction-sites-kolkata", "Water Supply for Construction Sites"),
    ("/water-supply-for-banquet-halls-kolkata", "Water Supply for Banquet Halls"),
    ("/water-supply-for-event-management-kolkata", "Water Supply for Event Management"),
    ("/water-supply-for-gyms-kolkata", "Water Supply for Gyms"),
    ("/event-water-supply-kolkata", "Event Water Supply Kolkata"),
]


def related_links_for(page):
    """Return related page links for a given page."""
    cluster = page.get("cluster", "generic")
    city = page.get("city", "Kolkata")
    city_slug = slugify(city)
    related = []

    if cluster == "product":
        pool = PRODUCT_LINKS[:]
    elif cluster == "corporate":
        pool = CORPORATE_LINKS[:]
    elif cluster == "industry":
        pool = INDUSTRY_LINKS[:]
    elif cluster == "locality":
        loc = page.get("locality", "")
        loc_slug = slugify(loc)
        # Add generic city pages and a few nearby locality pages
        pool = [
            (f"/packaged-drinking-water-{city_slug}", f"Packaged Drinking Water {city}"),
            (f"/water-delivery-{city_slug}", f"Water Delivery {city}"),
            (f"/water-supplier-{city_slug}", f"Water Supplier {city}"),
            ("/areas-we-serve", "Areas We Serve"),
            ("/bulk-water-supply-kolkata", "Bulk Water Supply Kolkata"),
            ("/bulk-water-supply-howrah", "Bulk Water Supply Howrah"),
            ("/office-water-delivery-kolkata", "Office Water Delivery Kolkata"),
            ("/water-supply-for-hotels-restaurants-kolkata", "Hotels & Restaurants"),
            ("/water-supply-for-factories-industries-kolkata-howrah", "Factories & Industries"),
        ]
        for ns, nname, ncity, _ in page.get("nearby_localities", [])[:4]:
            pool.append((f"/packaged-drinking-water-{ns}", f"Packaged Drinking Water {nname}"))
    elif cluster == "hub":
        # Hub page: link to city-level product, corporate, industry, and locality pages
        pool = [
            (f"/packaged-drinking-water-{city_slug}", f"Packaged Drinking Water {city}"),
            (f"/bulk-water-supply-{city_slug}", f"Bulk Water Supply {city}"),
            (f"/water-supplier-{city_slug}", f"Water Supplier {city}"),
            (f"/water-delivery-{city_slug}", f"Water Delivery {city}"),
            (f"/bottled-water-{city_slug}", f"Bottled Water {city}"),
            (f"/mineral-water-{city_slug}", f"Mineral Water {city}"),
            (f"/drinking-water-{city_slug}", f"Drinking Water {city}"),
        ]
        for href, label in PRODUCT_LINKS + CORPORATE_LINKS + INDUSTRY_LINKS:
            if href.endswith(f"-{city_slug}"):
                pool.append((href, label))
        added = 0
        for ls, lname, lcity, _ in ALL_LOCALITIES:
            if lcity == city:
                pool.append((f"/packaged-drinking-water-{ls}", f"Packaged Drinking Water {lname}"))
                added += 1
                if added >= 8:
                    break
        pool.append((f"/{city_slug}-water-supply", f"{city} Water Supply Hub"))
    else:
        pool = CORE_LINKS[:]

    # Remove self-reference
    pool = [(href, label) for href, label in pool if href.strip("/") != page["slug"]]

    # Select 8-12 links deterministically
    count = 10 if cluster != "locality" else 12
    related = (pool * 2)[:count]
    return related


# =============================================================================
# HTML TEMPLATE
# =============================================================================

CRITICAL_CSS = """
:root{--color-primary:#040916;--color-bg:#060b1a;--color-accent:#b59e6d;--color-muted:rgba(255,255,255,0.65);--font-heading:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;--font-body:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:var(--font-body);background:var(--color-bg);color:var(--color-muted);line-height:1.6}
h1,h2,h3,h4{font-family:var(--font-heading);margin:0 0 1rem}
a{color:var(--color-accent);text-decoration:none}
img{max-width:100%;height:auto;display:block}
.container{width:min(1200px,92%);margin:0 auto}
.header{position:fixed;top:0;left:0;width:100%;z-index:1000;background:rgba(4,9,22,0.98);border-bottom:1px solid rgba(255,255,255,0.06)}
.header nav{display:flex;justify-content:space-between;align-items:center;padding:1rem 0}
.logo{width:80px;height:auto}
.btn-ultimate{display:inline-block;padding:0.9rem 1.6rem;border-radius:6px;font-weight:700;text-transform:uppercase;letter-spacing:1px;font-size:0.8rem;transition:transform .2s,box-shadow .2s}
.btn-ultimate:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(181,158,109,0.25)}
.glass-card{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:16px;backdrop-filter:blur(8px)}
.trust-strip{display:flex;flex-wrap:wrap;justify-content:center;gap:1rem;margin-top:2rem}
.trust-pill{display:inline-flex;align-items:center;gap:.5rem;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);padding:.6rem 1rem;border-radius:999px;font-size:.8rem;color:#fff}
.use-case-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.5rem;margin-top:2rem}
.use-card{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.5rem;transition:transform .2s,border-color .2s}
.use-card:hover{transform:translateY(-4px);border-color:var(--color-accent)}
.related-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.25rem;margin-top:2rem}
.related-card{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1.25rem}
.faq-item{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:12px;margin-bottom:1rem;overflow:hidden}
.faq-q{padding:1.25rem 1.5rem;cursor:pointer;color:#fff;font-weight:700;user-select:none}
.faq-a{padding:0 1.5rem 1.5rem;line-height:1.8}
@media(max-width:768px){.hero-split{grid-template-columns:1fr}.content-split{grid-template-columns:1fr}.trust-strip{flex-direction:column;align-items:center}}
""".replace("\n", "")

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_description}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="author" content="Maharani Beverages LLP">
  <link rel="canonical" href="{canonical}">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="{logo_url}">
  <link rel="shortcut icon" href="{logo_url}">

  <!-- Google Analytics 4 — lazy-loaded after page interactive (replace G-XXXXXXXXXX with your real Measurement ID) -->
  <script>
    window.addEventListener('load', function() {{
      var s = document.createElement('script');
      s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX';
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-XXXXXXXXXX');
    }});
  </script>

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_description}">
  <meta property="og:image" content="{logo_url}">
  <meta property="og:site_name" content="{brand_short}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{twitter_title}">
  <meta name="twitter:description" content="{twitter_description}">
  <meta name="twitter:image" content="{logo_url}">

  <!-- Critical CSS -->
  <style>{critical_css}</style>


  <!-- Schema: FAQPage -->
  <script type="application/ld+json">{faq_schema}</script>

  <!-- Schema: @graph -->
  <script type="application/ld+json">{graph_schema}</script>

  <!-- Schema: BreadcrumbList -->
  <script type="application/ld+json">{breadcrumb_schema}</script>
</head>
<body>

  <!-- HEADER -->
  <header class="header">
    <nav class="container" aria-label="Primary navigation">
      <div style="display:flex;align-items:center;gap:1rem;">
        <a href="/">
          <img src="{logo_data}" alt="{brand_short} Official Logo" class="logo" width="80" height="66" loading="eager" fetchpriority="high">
        </a>
      </div>
      <div style="display:flex;gap:2rem;align-items:center;flex-wrap:wrap;">
        <a href="/" style="color:rgba(255,255,255,0.7);font-weight:600;font-size:.7rem;text-transform:uppercase;letter-spacing:2px;">Home</a>
        <a href="/pages/products" style="color:rgba(255,255,255,0.7);font-weight:600;font-size:.7rem;text-transform:uppercase;letter-spacing:2px;">Products</a>
        <a href="/{city_hub}" style="color:rgba(255,255,255,0.7);font-weight:600;font-size:.7rem;text-transform:uppercase;letter-spacing:2px;">{primary_city} Hub</a>
        <a href="/areas-we-serve" style="color:rgba(255,255,255,0.7);font-weight:600;font-size:.7rem;text-transform:uppercase;letter-spacing:2px;">Areas</a>
        <a href="/pages/contact" class="btn-ultimate" style="background:var(--color-accent);color:var(--color-primary);padding:.6rem 1rem;">Enquiry</a>
      </div>
    </nav>
  </header>

  <main>
    <!-- HERO -->
    <section id="hero" style="position:relative;padding:10rem 0 6rem;background:var(--color-primary);overflow:hidden;">
      <div class="container" style="position:relative;z-index:2;text-align:center;">
        <p style="color:var(--color-accent);font-size:.75rem;font-weight:800;text-transform:uppercase;letter-spacing:4px;margin-bottom:1.5rem;">{eyebrow}</p>
        <h1 style="font-family:var(--font-heading);font-size:clamp(2.2rem,6vw,4rem);color:#fff;line-height:1.1;margin-bottom:1.5rem;">{h1}</h1>
        <p style="color:rgba(255,255,255,0.75);font-size:1.1rem;max-width:700px;margin:0 auto 2rem;line-height:1.8;">{hero_subtitle}</p>

        <!-- CTA buttons -->
        <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:1rem;margin-bottom:2rem;">
          <a href="https://wa.me/{phone_e164}?text={wa_text}" class="btn-ultimate" style="background:#25D366;color:#fff;border:none;">Order on WhatsApp</a>
          <a href="tel:{phone}" class="btn-ultimate" style="background:transparent;color:#fff;border:1px solid var(--color-accent);">Call {phone}</a>
          <a href="/pages/contact" class="btn-ultimate" style="background:var(--color-accent);color:var(--color-primary);border:none;">Send Enquiry</a>
        </div>

        <!-- Trust strip -->
        <div class="trust-strip" aria-label="Trust badges">
          <span class="trust-pill">✓ FSSAI {fssai}</span>
          <span class="trust-pill">✓ BIS IS 14543</span>
          <span class="trust-pill">✓ 7-Stage Purification</span>
          <span class="trust-pill">✓ Same-Day Delivery</span>
          <span class="trust-pill">✓ Local Ranihati Plant</span>
        </div>
      </div>
    </section>

    <!-- WHO WE SERVE -->
    <section id="who-we-serve" style="padding:5rem 0;background:var(--color-bg);border-bottom:1px solid rgba(255,255,255,0.05);">
      <div class="container">
        <h2 style="color:#fff;font-size:2rem;text-align:center;margin-bottom:.5rem;">Who We Serve in {primary_city}</h2>
        <p style="text-align:center;max-width:650px;margin:0 auto 2rem;">Zenith Water supports homes, offices, and industries across {primary_city} with certified packaged drinking water.</p>
        <div class="use-case-grid">
          {use_case_cards}
        </div>
      </div>
    </section>

    <!-- MAIN CONTENT -->
    <section id="content" style="padding:6rem 0;background:var(--color-bg);">
      <div class="container">
        <div class="content-split" style="display:grid;grid-template-columns:3fr 2fr;gap:4rem;">

          <article style="color:var(--color-muted);line-height:1.9;">
            <div style="margin-bottom:4rem;">
              <h2 style="color:#fff;font-size:2rem;margin-bottom:1.5rem;">{section1_title}</h2>
              {section1_body}
            </div>

            <div style="margin-bottom:4rem;">
              <h3 style="color:#fff;font-size:1.5rem;margin-bottom:1.25rem;">{section2_title}</h3>
              {section2_body}
            </div>

            <div style="margin-bottom:4rem;">
              <h3 style="color:#fff;font-size:1.5rem;margin-bottom:1.25rem;">Service Coverage</h3>
              <p>Our delivery network covers the key sectors and neighbourhoods of {primary_city}:</p>
              <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem;margin-top:1rem;">
                {coverage_items}
              </div>
              <p style="margin-top:1.5rem;">{coverage_footer}</p>
            </div>

            <div style="margin-bottom:4rem;">
              <h3 style="color:#fff;font-size:1.5rem;margin-bottom:1.5rem;">Frequently Asked Questions</h3>
              {faq_html}
            </div>
          </article>

          <!-- STICKY SIDEBAR -->
          <aside>
            <div class="glass-card" style="padding:2rem;position:sticky;top:100px;">
              <h3 style="color:#fff;font-size:1.35rem;margin-bottom:1rem;">Quick Contact</h3>
              <p style="font-size:.9rem;opacity:.7;margin-bottom:1.5rem;">Get certified water delivered to your {primary_city} location today.</p>

              <div style="margin-bottom:1.5rem;">
                <p style="font-size:.7rem;color:var(--color-accent);text-transform:uppercase;letter-spacing:2px;margin-bottom:.25rem;">Phone</p>
                <a href="tel:{phone}" style="color:#fff;font-weight:800;font-size:1.4rem;text-decoration:none;">{phone}</a>
              </div>

              <div style="margin-bottom:1.5rem;">
                <p style="font-size:.7rem;color:var(--color-accent);text-transform:uppercase;letter-spacing:2px;margin-bottom:.25rem;">Email</p>
                <a href="mailto:{email}" style="color:#fff;font-weight:600;text-decoration:none;">{email}</a>
              </div>

              <div style="margin-bottom:1.5rem;">
                <p style="font-size:.7rem;color:var(--color-accent);text-transform:uppercase;letter-spacing:2px;margin-bottom:.25rem;">WhatsApp</p>
                <a href="https://wa.me/{phone_e164}?text={wa_text}" style="color:#fff;font-weight:600;text-decoration:none;">+91 82748 37341</a>
              </div>

              <a href="https://wa.me/{phone_e164}?text={wa_text}" class="btn-ultimate" style="display:block;width:100%;text-align:center;background:#25D366;border:none;margin-bottom:.75rem;">Order on WhatsApp</a>
              <a href="/pages/contact" class="btn-ultimate" style="display:block;width:100%;text-align:center;background:transparent;border:1px solid var(--color-accent);color:#fff;">Send Enquiry</a>

              <p style="margin-top:1.5rem;font-style:italic;font-size:.8rem;text-align:center;opacity:.5;">Zenith — Delivering Purity with Trust.</p>
            </div>
          </aside>

        </div>
      </div>
    </section>

    <!-- RELATED PAGES -->
    <section id="related" style="padding:5rem 0;background:#050a16;border-top:1px solid rgba(255,255,255,0.05);">
      <div class="container">
        <h2 style="color:#fff;font-size:2rem;text-align:center;margin-bottom:.5rem;">Related Pages</h2>
        <p style="text-align:center;max-width:650px;margin:0 auto 2rem;">Explore more Zenith Water supply and delivery resources across Kolkata and Howrah.</p>
        <div class="related-grid">
          {related_cards}
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer style="background:#040916;border-top:1px solid rgba(255,255,255,0.08);padding:5rem 0 2rem;">
    <div class="container">
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:3rem;margin-bottom:3rem;">

        <!-- Brand -->
        <div style="grid-column:span 1;">
          <a href="/">
            <img src="zenith_logo_compact.webp" alt="{brand_short} Official Logo" loading="lazy" width="120" height="99">
          </a>
          <p style="color:var(--color-accent);font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:1rem 0;">Premium Packaged Drinking Water</p>
          <p style="color:rgba(255,255,255,0.6);font-size:.9rem;line-height:1.7;margin-bottom:1.5rem;">FSSAI-certified bottled and jar water for homes, offices, hotels, and industries across Kolkata & Howrah.</p>
          <div style="display:inline-flex;align-items:center;gap:.5rem;background:rgba(181,158,109,0.08);border:1px solid rgba(181,158,109,0.25);padding:.5rem 1rem;border-radius:4px;">
            <span style="color:var(--color-accent);font-weight:800;">✓</span>
            <span style="color:rgba(255,255,255,0.85);font-size:.7rem;font-weight:700;letter-spacing:.5px;">FSSAI: {fssai}</span>
          </div>
        </div>

        <!-- Company -->
        <div>
          <h4 style="font-family:var(--font-heading);font-size:.9rem;color:#fff;margin-bottom:1.5rem;text-transform:uppercase;letter-spacing:2px;">Company</h4>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.9rem;">
            <li><a href="/pages/vision" class="footer-link">About Us</a></li>
            <li><a href="/pages/contact" class="footer-link">Contact Us</a></li>
            <li><a href="/pages/distributor" class="footer-link">Distribution Network</a></li>
            <li><a href="/areas-we-serve" class="footer-link">Areas We Serve</a></li>
            <li><a href="/packaged-drinking-water-kolkata" class="footer-link">Kolkata Hub</a></li>
          </ul>
        </div>

        <!-- Water Supply -->
        <div>
          <h4 style="font-family:var(--font-heading);font-size:.9rem;color:var(--color-accent);margin-bottom:1.5rem;text-transform:uppercase;letter-spacing:2px;">Water Supply</h4>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.9rem;">
            <li><a href="/packaged-drinking-water-kolkata" class="footer-link">Packaged Drinking Water Kolkata</a></li>
            <li><a href="/water-supplier-kolkata" class="footer-link">Water Supplier Kolkata</a></li>
            <li><a href="/water-delivery-kolkata" class="footer-link">Water Delivery Kolkata</a></li>
            <li><a href="/bulk-water-supply-kolkata" class="footer-link">Bulk Water Supply Kolkata</a></li>
            <li><a href="/packaged-drinking-water-howrah" class="footer-link">Packaged Drinking Water Howrah</a></li>
            <li><a href="/bulk-water-supply-howrah" class="footer-link">Bulk Water Supply Howrah</a></li>
          </ul>
        </div>

        <!-- Solutions -->
        <div>
          <h4 style="font-family:var(--font-heading);font-size:.9rem;color:#fff;margin-bottom:1.5rem;text-transform:uppercase;letter-spacing:2px;">Solutions</h4>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.9rem;">
            <li><a href="/office-water-delivery-kolkata" class="footer-link">Office Water Delivery</a></li>
            <li><a href="/water-supply-for-hotels-restaurants-kolkata" class="footer-link">Hotels & Restaurants</a></li>
            <li><a href="/water-supply-for-factories-industries-kolkata-howrah" class="footer-link">Factories & Industries</a></li>
            <li><a href="/event-water-supply-kolkata" class="footer-link">Event Water Supply</a></li>
            <li><a href="/20-liter-water-jar-delivery-kolkata" class="footer-link">20L Jar Delivery</a></li>
          </ul>
        </div>

        <!-- Legal -->
        <div>
          <h4 style="font-family:var(--font-heading);font-size:.9rem;color:#fff;margin-bottom:1.5rem;text-transform:uppercase;letter-spacing:2px;">Legal</h4>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.9rem;">
            <li><a href="/pages/shipping" class="footer-link">Shipping Policy</a></li>
            <li><a href="/pages/returns" class="footer-link">Returns Policy</a></li>
            <li><a href="/pages/terms" class="footer-link">Terms & Conditions</a></li>
            <li><a href="/pages/privacy" class="footer-link">Privacy Policy</a></li>
            <li><a href="/pages/compliance" class="footer-link">Compliance</a></li>
          </ul>
        </div>

      </div>

      <div style="border-top:1px solid rgba(255,255,255,0.06);padding-top:2rem;text-align:center;">
        <p style="color:rgba(255,255,255,0.35);font-size:.8rem;margin:0 0 1rem;">&copy; 2026 {brand} — {brand_short}. All rights reserved.</p>
        <p style="opacity:.7;font-size:.7rem;color:rgba(255,255,255,0.4);max-width:700px;margin:0 auto;line-height:1.6;">
          {brand_short} by {brand} is a premium packaged drinking water supplier in Kolkata and Howrah, offering bulk water supply for homes, offices, hotels, and events with fast and reliable delivery.
        </p>
      </div>
    </div>
  </footer>

  <style>
    .footer-link{{color:rgba(255,255,255,0.6);text-decoration:none;font-size:.9rem;transition:color .2s,padding-left .2s;display:inline-block;}}
    .footer-link:hover{{color:var(--color-accent);padding-left:4px;}}
  </style>

  <!-- Minimal interaction layer -->
  <script>
    (function() {{
      document.querySelectorAll('.faq-item').forEach(function(item) {{
        item.querySelector('.faq-q').addEventListener('click', function() {{
          item.classList.toggle('active');
        }});
      }});
    }})();
  </script>
</body>
</html>
'''


# =============================================================================
# RENDER & OUTPUT
# =============================================================================

def use_case_cards(city):
    """Generate use-case cards with internal links."""
    cases = [
        ("🏠", "Homes", f"Daily bottles & 20L jars for families in {city}", f"/water-delivery-{slugify(city)}"),
        ("🏢", "Offices", f"Scheduled dispenser jar delivery for {city} offices", f"/office-water-delivery-{slugify(city)}"),
        ("🏨", "Hotels", "Premium bottled water for guest rooms & banquets", "/water-supply-for-hotels-restaurants-kolkata"),
        ("🏭", "Factories", "Bulk 20L jar programs for industrial units", "/water-supply-for-factories-industries-kolkata-howrah"),
        ("🏥", "Hospitals", "Safe hydration for patients, staff & visitors", f"/water-supply-for-hospitals-{slugify(city)}"),
        ("🎉", "Events", "On-time bulk supply for conferences & weddings", "/event-water-supply-kolkata"),
    ]
    cards = []
    for icon, label, desc, href in cases:
        cards.append(
            f'<div class="use-card">'
            f'<div style="font-size:1.5rem;margin-bottom:.5rem;">{icon}</div>'
            f'<h3 style="color:#fff;font-size:1.1rem;margin-bottom:.5rem;">{label}</h3>'
            f'<p style="font-size:.9rem;margin-bottom:1rem;">{desc}</p>'
            f'<a href="{href}" style="color:var(--color-accent);font-weight:600;font-size:.85rem;">Learn more →</a>'
            f'</div>'
        )
    return "\n          ".join(cards)


def coverage_items_html(items):
    return "\n                ".join(
        f'<div style="border-left:2px solid var(--color-accent);padding-left:1rem;color:#fff;font-weight:500;">• {esc(x)}</div>'
        for x in items
    )


def faq_html(faqs):
    out = []
    for q, a in faqs:
        out.append(
            f'<div class="faq-item">'
            f'<div class="faq-q">{esc(q)}</div>'
            f'<div class="faq-a">{esc(a)}</div>'
            f'</div>'
        )
    return "\n              ".join(out)


def related_cards_html(related):
    cards = []
    for href, label in related:
        cards.append(
            f'<div class="related-card">'
            f'<h3 style="color:#fff;font-size:1rem;margin-bottom:.5rem;">{esc(label)}</h3>'
            f'<a href="{href}" style="color:var(--color-accent);font-weight:600;font-size:.85rem;">Visit page →</a>'
            f'</div>'
        )
    return "\n          ".join(cards)


def css_links():
    """Render non-blocking stylesheet links. Critical CSS is inlined above."""
    lines = []
    for f in CSS_FILES:
        lines.append(f'<link rel="preload" href="{f}" as="style">')
        lines.append(f'<link rel="stylesheet" href="{f}" media="print" onload="this.media=\'all\'">')
        lines.append(f'<noscript><link rel="stylesheet" href="{f}"></noscript>')
    return "\n  ".join(lines)


def js_links():
    return "\n  ".join(f'<script src="{f}" defer></script>' for f in JS_FILES)


def render_page(page):
    """Render a single landing page from data dictionary."""
    slug = page["slug"]
    city = page["city"]
    city_slug = slugify(city)
    city_hub = f"packaged-drinking-water-{city_slug}"
    canonical = f"{DOMAIN}/{slug}"
    related = related_links_for(page)

    faq_schema = json.dumps(build_faq_schema(page["faqs"]), indent=2)
    graph_schema = json.dumps(build_graph_schema(page), indent=2)
    breadcrumb_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
            {"@type": "ListItem", "position": 2, "name": page["breadcrumb_name"], "item": canonical},
        ],
    }, indent=2)

    html_out = TEMPLATE.format(
        title=esc(page["title"]),
        meta_description=esc(page["meta_description"]),
        canonical=canonical,
        logo_url=f"{DOMAIN}/{LOGO}",
        logo_path=LOGO,
        og_title=esc(page["og_title"]),
        og_description=esc(page["og_description"]),
        twitter_title=esc(page["twitter_title"]),
        twitter_description=esc(page["twitter_description"]),
        brand_short=esc(BRAND_SHORT),
        brand=esc(BRAND),
        logo_data=LOGO_DATA_URI,
        critical_css=CRITICAL_CSS,
        css_links=css_links(),
        js_links=js_links(),
        faq_schema=faq_schema,
        graph_schema=graph_schema,
        breadcrumb_schema=breadcrumb_schema,
        city_hub=city_hub,
        primary_city=esc(city),
        eyebrow=esc(page["eyebrow"]),
        h1=page["h1"],
        hero_subtitle=esc(page["hero_subtitle"]),
        wa_text=page["wa_text"],
        phone=esc(PHONE),
        phone_e164=PHONE_E164,
        email=esc(EMAIL),
        fssai=FSSAI,
        section1_title=esc(page["section1_title"]),
        section1_body=page["section1_body"],
        section2_title=esc(page["section2_title"]),
        section2_body=page["section2_body"],
        coverage_items=coverage_items_html(page["coverage"]),
        coverage_footer=page["coverage_footer"],
        faq_html=faq_html(page["faqs"]),
        use_case_cards=use_case_cards(city),
        related_cards=related_cards_html(related),
    )
    return html_out


# =============================================================================
# VALIDATION
# =============================================================================

SELF_CLOSING = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}


def validate(html_content, slug):
    """Simple stack-based HTML tag validator. Returns list of issue strings."""
    issues = []
    # Check for unclosed/unknown common structural tags only
    tag_pattern = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)[^>]*?>", re.S)
    stack = []
    for m in tag_pattern.finditer(html_content):
        closing, tag = m.group(1), m.group(2).lower()
        if tag in SELF_CLOSING:
            continue
        if closing:
            if stack and stack[-1] == tag:
                stack.pop()
            else:
                issues.append(f"{slug}: unexpected closing </{tag}> (expected </{stack[-1]}>)")
        else:
            stack.append(tag)
    if stack:
        issues.append(f"{slug}: unclosed tags {stack[-5:]}")

    # Basic checks
    if html_content.count("<h1") != 1:
        issues.append(f"{slug}: expected exactly one <h1>, found {html_content.count('<h1')}")
    if "<title>" not in html_content or "</title>" not in html_content:
        issues.append(f"{slug}: missing <title>")
    if '<meta name="description"' not in html_content:
        issues.append(f"{slug}: missing meta description")
    if '<link rel="canonical"' not in html_content:
        issues.append(f"{slug}: missing canonical")
    if "@graph" not in html_content:
        issues.append(f"{slug}: missing @graph schema")
    return issues


# =============================================================================
# SITEMAP UPDATE
# =============================================================================

def update_sitemap(slugs):
    """Add new slugs to sitemap.xml without duplicating existing URLs."""
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        print(f"Warning: sitemap.xml not found at {sitemap_path}")
        return 0

    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract existing URLs
    existing = set(re.findall(r"<loc>([^<]+)</loc>", content))

    added = 0
    entries = []
    for slug in slugs:
        url = f"{DOMAIN}/{slug}"
        if url in existing:
            continue
        # Determine priority based on cluster
        if "locality" in slug or any(slug.startswith(f"{intent}-") and slug.endswith(f"-{loc[0]}") for intent in ("packaged-drinking-water", "water-delivery", "water-supplier") for loc in ALL_LOCALITIES):
            priority = "0.80"
        else:
            priority = "0.85"
        entries.append(
            f"  <url>\n"
            f"    <loc>{url}</loc>\n"
            f"    <lastmod>{TODAY}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            f"  </url>"
        )
        added += 1

    if not entries:
        return 0

    # Insert before closing urlset
    insert_block = "\n" + "\n".join(entries) + "\n"
    if content.rstrip().endswith("</urlset>"):
        content = content.rstrip()[:-len("</urlset>")].rstrip() + insert_block + "</urlset>\n"
    else:
        content = content.rstrip() + insert_block + "</urlset>\n"

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    return added


# =============================================================================
# MAIN
# =============================================================================

def generate_all_pages():
    """Build all page data dictionaries."""
    pages = []
    pages.extend(make_product_pages())
    pages.extend(make_corporate_pages())
    pages.extend(make_industry_pages())
    pages.extend(make_hub_pages())
    pages.extend(make_locality_pages())
    return pages


def main():
    pages = generate_all_pages()
    generated_slugs = []
    validation_issues = []

    for page in pages:
        slug = page["slug"]
        filename = f"{slug}.html"
        filepath = os.path.join(ROOT, filename)

        # Protect root files that should not be overwritten by this engine
        if filename in PROTECTED_PATHS:
            continue

        html_out = render_page(page)
        issues = validate(html_out, slug)
        validation_issues.extend(issues)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_out)
        generated_slugs.append(slug)
        print(f"Generated: {filename}")

    # Update sitemap
    sitemap_added = update_sitemap(generated_slugs)

    # Summary
    print("\n" + "=" * 60)
    print(f"Total pages generated: {len(generated_slugs)}")
    print(f"New sitemap entries added: {sitemap_added}")
    if validation_issues:
        print(f"Validation issues found: {len(validation_issues)}")
        for issue in validation_issues[:20]:
            print(f"  - {issue}")
        if len(validation_issues) > 20:
            print(f"  ... and {len(validation_issues) - 20} more")
    else:
        print("Validation: no issues detected")
    print("=" * 60)
    print("New slugs:")
    for slug in generated_slugs:
        print(f"  /{slug}")


if __name__ == "__main__":
    main()
