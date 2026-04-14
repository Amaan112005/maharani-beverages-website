/**
 * ZENITH Water - Old Money Minimalist Engine
 * Characterized by: Discreet luxury, native performance, and architectural silence.
 */

'use strict';

/**
 * 0. LUXURY PRELOADER (Minimal Silence)
 */
function initPreloader() {
  const preloader = document.getElementById('preloader');
  const bar = document.querySelector('.pl-bar');
  
  if (!preloader) return;

  document.body.style.overflow = 'hidden'; 
  
  const finishLoading = () => {
    if (preloader.classList.contains('hidden')) return; 
    if (bar) bar.style.width = '100%';
    
    setTimeout(() => {
      preloader.classList.add('hidden');
      document.body.style.overflow = 'auto'; 
      // Force AOS refresh if needed
      if (window.AOS) window.AOS.init();
    }, 600);
  };

  let progress = 0;
  const interval = setInterval(() => {
    progress += (Math.random() * 15) + 5;
    if (progress >= 100) {
      clearInterval(interval);
      finishLoading();
    } else if (bar) {
      bar.style.width = progress + '%';
    }
  }, 50);

  // Safety Net 1: Loaded Event
  window.addEventListener('load', () => {
    clearInterval(interval);
    finishLoading();
  });

  // Safety Net 2: Maximum Wait Time (3 seconds)
  setTimeout(() => {
    clearInterval(interval);
    finishLoading();
  }, 3000);
}

/**
 * 1. ADVANCED PINCODE SYSTEM (Discreet Search)
 */
async function initAdvancedPincode() {
  const form = document.getElementById('pincode-form');
  const input = document.getElementById('pincode-input');
  const result = document.getElementById('pincode-result');

  if (!form || !input || !result) return;

  function renderPincode(el, text, status) {
    el.textContent = text;
    el.className = `pincode-result-msg ${status}`;
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const value = input.value.trim();

    result.textContent = 'VERIFYING...';
    result.className = 'pincode-result-msg';

    try {
      const resp = await fetch('data/pincodes.json');
      const data = await resp.json();
      const resultData = data[value];

      setTimeout(() => {
        if (resultData && resultData.available) {
          renderPincode(result, `AVAILABILITY: ${resultData.area}`, "success");
        } else if (resultData) {
          renderPincode(result, `STATUS: COMING SOON TO ${resultData.area}`, "warning");
        } else {
          renderPincode(result, `STATUS: OUT OF NETWORK`, "error");
        }
      }, 1000);
    } catch (err) {
      renderPincode(result, 'SYSTEM ERROR: PLEASE TRY LATER', 'error');
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
    // Initiating the preloader immediately
    initPreloader();
    
    // Logic modules for high-class interaction
    initAdvancedPincode();
    initFAQ();
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
    // Emergency reveal if JS suite fails
    const preloader = document.getElementById('preloader');
    if (preloader) preloader.classList.add('hidden');
    document.body.style.overflow = 'auto';
  }
});
