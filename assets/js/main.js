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

  let PINCODE_MAP = null;
  let loadPromise = null;
  function loadPincodeMap() {
    if (PINCODE_MAP) return Promise.resolve(PINCODE_MAP);
    if (loadPromise) return loadPromise;
    loadPromise = fetch('assets/data/pincodes.json')
      .then(r => r.json())
      .then(data => { PINCODE_MAP = data; return data; })
      .catch(() => { PINCODE_MAP = {}; return {}; });
    return loadPromise;
  }
  // Prefetch on first interaction
  input.addEventListener('focus', loadPincodeMap, { once: true });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const value = input.value.trim();

    if (value.length !== 6 || !/^\d{6}$/.test(value)) {
      result.innerHTML = `<div class="pincode-result-msg error">⚠ Please enter a valid 6-digit pincode.</div>`;
      return;
    }

    result.innerHTML = `<div class="pincode-result-msg checking">🔍 Checking availability...</div>`;
    await loadPincodeMap();

    const areaName = PINCODE_MAP[value];
    const isKolkata = value.startsWith('700');
    const isHowrah = value.startsWith('711');

    if (areaName) {
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
(function initAll(){
  try {
    initAdvancedPincode();
    initFAQ();
    initDistributorForm();
    initLiquidParallax();
    initHeaderScroll();
    if (window.AOS) {
      window.AOS.init({ threshold: 0.1, once: true, duration: 1800, easing: 'ease-out-expo' });
    }
  } catch (err) {
    console.error('ZENITH CORE ERROR:', err);
  }
})();
