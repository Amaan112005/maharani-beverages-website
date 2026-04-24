/**
 * ZENITH Water - Conversion Engine v3
 * Characterized by: Discreet luxury, native performance, and architectural silence.
 */



/**
 * 1. ADVANCED PINCODE SYSTEM (High-Conversion Area Lookup)
 */
function initAdvancedPincode() {
  const form = document.getElementById('pincode-form');
  const input = document.getElementById('pincode-input');
  const result = document.getElementById('pincode-result');

  if (!form || !input || !result) return;

  // Pincode → Area name map (Kolkata & Howrah)
  const PINCODE_MAP = {
    '700001': 'Dalhousie, Kolkata',
    '700002': 'Cossipore, Kolkata',
    '700003': 'Baghbazar, Kolkata',
    '700005': 'Shyambazar, Kolkata',
    '700006': 'Shyampur, Kolkata',
    '700007': 'Burrabazar, Kolkata',
    '700009': 'Garden Reach, Kolkata',
    '700010': 'Kasba, Kolkata',
    '700012': 'Bowbazar, Kolkata',
    '700013': 'Esplanade, Kolkata',
    '700014': 'Karaya, Kolkata',
    '700015': 'Kalighat, Kolkata',
    '700016': 'Park Street, Kolkata',
    '700017': 'Rash Behari, Kolkata',
    '700018': 'Hazra, Kolkata',
    '700019': 'Ballygunge, Kolkata',
    '700020': 'Bhowanipore, Kolkata',
    '700022': 'Ekbalpore, Kolkata',
    '700023': 'Manicktala, Kolkata',
    '700025': 'Behala, Kolkata',
    '700026': 'Parnasree, Kolkata',
    '700027': 'Alipore, Kolkata',
    '700028': 'Chetla, Kolkata',
    '700029': 'Jadavpur, Kolkata',
    '700030': 'Thakurpukur, Kolkata',
    '700031': 'Garia, Kolkata',
    '700032': 'Dum Dum, Kolkata',
    '700033': 'Tollygunge, Kolkata',
    '700034': 'New Barrackpore, Kolkata',
    '700036': 'Baguiati, Kolkata',
    '700039': 'Salt Lake, Kolkata',
    '700040': 'Biddhanagar, Kolkata',
    '700041': 'Sarsuna, Kolkata',
    '700047': 'Golpark, Kolkata',
    '700048': 'Regent Park, Kolkata',
    '700053': 'New Alipore, Kolkata',
    '700054': 'Naktala, Kolkata',
    '700055': 'Santoshpur, Kolkata',
    '700059': 'Kankurgachi, Kolkata',
    '700060': 'Phoolbagan, Kolkata',
    '700064': 'Bangur, Kolkata',
    '700065': 'Bansdroni, Kolkata',
    '700067': 'Patuli, Kolkata',
    '700068': 'Mukundapur, Kolkata',
    '700071': 'Kolkata Mall, Kolkata',
    '700074': 'Haridevpur, Kolkata',
    '700075': 'Purba Jadavpur, Kolkata',
    '700078': 'Tiljala, Kolkata',
    '700080': 'Baranagar, Kolkata',
    '700082': 'Shobhabazar, Kolkata',
    '700084': 'Belgachia, Kolkata',
    '700086': 'Narendrapur, Kolkata',
    '700088': 'Sonarpur, Kolkata',
    '700089': 'Rajpur, Kolkata',
    '700090': 'Noapara, Kolkata',
    '700091': 'Dum Dum Airport, Kolkata',
    '700094': 'Habra, Kolkata',
    '700095': 'Khardah, Kolkata',
    '700097': 'Nibra, Kolkata',
    '700099': 'Kamarhati, Kolkata',
    '700100': 'Ghola, Kolkata',
    '700101': 'Naihati, Kolkata',
    '700108': 'Newtown, Kolkata',
    '700104': 'Rajarhat, Kolkata',
    '711101': 'Howrah Station / Kadam Tala, Howrah',
    '711102': 'Salkia, Howrah',
    '711103': 'Shibpur, Howrah',
    '711104': 'Ramrajatala, Howrah',
    '711105': 'Bally, Howrah',
    '711106': 'Liluah, Howrah',
    '711107': 'Belur, Howrah',
    '711108': 'Dasnagar, Howrah',
    '711109': 'Santragachi, Howrah',
    '711110': 'Andul, Howrah',
    '711111': 'Domjur, Howrah',
    '711112': 'Jagacha, Howrah',
    '711113': 'Panchla, Howrah',
    '711114': 'Bagnan, Howrah',
    '711201': 'Uluberia, Howrah',
    '711202': 'Shyampur, Howrah',
    '711302': 'Amta, Howrah',
    '711303': 'Udaynarayanpur, Howrah',
    '711304': 'Jagatballavpur, Howrah',
    '711305': 'Uluberia North, Howrah',
    '711306': 'Bagnan South, Howrah',
    '711309': 'Nalpur, Howrah',
    '711310': 'Deulpur, Howrah',
    '711315': 'Kolaghat, Howrah',
    '711316': 'Panskura, Howrah',
    '711317': 'Kolaghat Industrial, Howrah',
    '711322': 'Ranihati, Howrah',
    '711401': 'Arambagh, Howrah',
    '711409': 'Goghat, Howrah',
  };

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const value = input.value.trim();

    if (value.length !== 6 || !/^\d{6}$/.test(value)) {
      result.innerHTML = `<div class="pincode-result-msg error">⚠ Please enter a valid 6-digit pincode.</div>`;
      return;
    }

    result.innerHTML = `<div class="pincode-result-msg checking">🔍 Checking availability...</div>`;

    setTimeout(() => {
      const areaName = PINCODE_MAP[value];
      const isKolkata = value.startsWith('700');
      const isHowrah = value.startsWith('711');

      if (areaName) {
        // Exact match in our known list
        const waMsg = encodeURIComponent(`Hi, I want to order ZENITH water in ${areaName} (${value})`);
        result.innerHTML = `
          <div class="pincode-result-card available">
            <div class="pincode-area-name">📍 ${areaName}</div>
            <div class="pincode-status">✅ ZENITH is available in your area</div>
            <div class="pincode-delivery">⚡ Priority delivery available</div>
            <div class="pincode-actions">
              <a href="https://wa.me/918274837341?text=${waMsg}" target="_blank" class="pincode-btn-primary">
                💬 Order on WhatsApp
              </a>
            </div>
          </div>`;
      } else if (isKolkata || isHowrah) {
        // In region but not in our exact list yet — still serve them
        const approxArea = isKolkata ? 'Kolkata' : 'Howrah';
        const waMsg = encodeURIComponent(`Hi, I want to order ZENITH water. My area pincode is ${value} (${approxArea})`);
        result.innerHTML = `
          <div class="pincode-result-card available">
            <div class="pincode-area-name">📍 ${approxArea} Region</div>
            <div class="pincode-status">✅ ZENITH is available in your region</div>
            <div class="pincode-delivery">⚡ Priority delivery available</div>
            <div class="pincode-actions">
              <a href="https://wa.me/918274837341?text=${waMsg}" target="_blank" class="pincode-btn-primary">
                💬 Order on WhatsApp
              </a>
            </div>
          </div>`;
      } else {
        // Out of range
        const waMsg = encodeURIComponent(`Hi, please start ZENITH water supply in my area (${value})`);
        result.innerHTML = `
          <div class="pincode-result-card unavailable">
            <div class="pincode-status">🚀 We're expanding to your area soon!</div>
            <div class="pincode-delivery">Be the first to get ZENITH in <strong>${value}</strong></div>
            <div class="pincode-actions">
              <a href="https://wa.me/918274837341?text=${waMsg}" target="_blank" class="pincode-btn-secondary">
                📩 Request Availability
              </a>
            </div>
          </div>`;
      }
    }, 700);
  });
}

/**
 * 2. FAQ ACCORDION (Pure Interaction)
 */
function initFAQ() {
  document.querySelectorAll(".faq-item").forEach(item => {
    const btn = item.querySelector(".faq-question");
    if (!btn) return;

    btn.addEventListener("click", () => {
      item.classList.toggle("active");
    });
  });
}

/**
 * 3. DISTRIBUTOR FORM — Smart WhatsApp Redirect
 * Intercepts submit, shows flash confirmation, then redirects to WhatsApp
 */
function initDistributorForm() {
  const form = document.getElementById('distributor-form');
  if (!form) return;

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    // Capture name for personalized message
    const nameInput = form.querySelector('input[name="name"]');
    const areaInput = form.querySelector('input[name="area"]');
    const name = nameInput ? nameInput.value.trim() : 'a potential partner';
    const area = areaInput ? areaInput.value.trim() : 'my area';

    // Show flash overlay
    const overlay = document.createElement('div');
    overlay.id = 'submission-overlay';
    overlay.innerHTML = `
      <div class="submission-flash">
        <div class="submission-check">✅</div>
        <div class="submission-title">Application Submitted!</div>
        <div class="submission-sub">Redirecting you to WhatsApp...</div>
      </div>
    `;
    document.body.appendChild(overlay);

    // Submit to Formspree silently in background
    const formData = new FormData(form);
    fetch(form.action, {
      method: 'POST',
      body: formData,
      headers: { 'Accept': 'application/json' }
    }).catch(() => {}); // Silent fail — WhatsApp is the primary CTA

    // After 1.5s, redirect to WhatsApp with personalized message
    const waMsg = encodeURIComponent(
      `Hi, I am ${name}. I just submitted a ZENITH distributor application for ${area}. Please confirm receipt.`
    );

    setTimeout(() => {
      window.location.href = `https://wa.me/918274837341?text=${waMsg}`;
    }, 1500);
  });
}

/**
 * 3. LIQUID PARALLAX (Elite Interaction)
 */
function initLiquidParallax() {
  const heroBlock = document.querySelector('.hero-visual-block');
  const bottle = heroBlock?.querySelector('img');
  
  if (!heroBlock || !bottle) return;

  window.addEventListener('mousemove', (e) => {
    const { clientX, clientY } = e;
    const { innerWidth, innerHeight } = window;
    
    // Subtle refraction movement
    const xMove = (clientX - innerWidth / 2) / 50;
    const yMove = (clientY - innerHeight / 2) / 50;
    
    bottle.style.transform = `translate(${xMove}px, ${yMove}px) scale(1.05)`;
  });
}

/**
 * 4. STEALTH HEADER TRANSITION (Discovery UX)
 */
function initHeaderScroll() {
  const header = document.querySelector('.header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
}

/**
 * START SUITE
 */
document.addEventListener('DOMContentLoaded', () => {
  try {
    
    // Logic modules for high-class interaction
    initAdvancedPincode();
    initFAQ();
    initDistributorForm();
    initLiquidParallax();
    initHeaderScroll();

    // AOS Initialization (Handling the Discovery Fade-ups)
    if (window.AOS) {
      window.AOS.init({ 
        threshold: 0.1,
        once: true,
        duration: 1800,
        easing: 'ease-out-expo'
      });
    }

    console.log('🏛️ ZENITH ELITE BRAND ENGINE LOADED');
  } catch (err) {
    console.error('ZENITH CORE ERROR:', err);
  }
});
