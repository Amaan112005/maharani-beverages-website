/**
 * ZENITH Water - Old Money Minimalist Engine
 * Characterized by: Discreet luxury, native performance, and architectural silence.
 */

'use strict';

/**
 * 1. ADVANCED PINCODE SYSTEM (Discreet Search)
 */

/**
 * 1. ADVANCED PINCODE SYSTEM (Instant Regional Approval)
 */
function initAdvancedPincode() {
  const form = document.getElementById('pincode-form');
  const input = document.getElementById('pincode-input');
  const result = document.getElementById('pincode-result');

  if (!form || !input || !result) return;

  function renderPincode(el, text, status) {
    el.textContent = text;
    el.className = `pincode-result-msg ${status}`;
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const value = input.value.trim();

    if (value.length < 6) {
      renderPincode(result, "INVALID CODE ARCHITECTURE", "error");
      return;
    }

    result.textContent = 'VERIFYING SECTOR...';
    result.className = 'pincode-result-msg';

    setTimeout(() => {
      // Instant Approval for Howrah (711) and Kolkata (700)
      if (value.startsWith('700') || value.startsWith('711')) {
        renderPincode(result, "AVAILABILITY: CORE REGIONAL NETWORK [ACTIVE]", "success");
      } else {
        renderPincode(result, "OUTSIDE SECTOR: CONNECT WITH SUPPORT", "error");
      }
    }, 600);
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
  }
});
