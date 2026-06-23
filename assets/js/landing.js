/* Zenith landing-page lightweight interaction layer */
(function(){
  'use strict';

  // Header scroll state (passive + rAF throttled)
  const header = document.querySelector('.header');
  if (header) {
    let ticking = false;
    window.addEventListener('scroll', function() {
      if (!ticking) {
        window.requestAnimationFrame(function() {
          header.classList.toggle('scrolled', window.scrollY > 50);
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  // FAQ accordion for generated landing pages (.faq-q / .faq-a)
  document.querySelectorAll('.faq-item').forEach(function(item) {
    const q = item.querySelector('.faq-q');
    if (!q) return;
    q.addEventListener('click', function() {
      const isOpen = item.classList.contains('active');
      document.querySelectorAll('.faq-item.active').forEach(function(open) {
        if (open !== item) open.classList.remove('active');
      });
      item.classList.toggle('active', !isOpen);
    });
  });

  // AOS removed from generated pages to reduce main-thread work
})();
