// 👑 ZENITH Custom AOS (Lightweight Scroll Animation Engine)
// Built for performance + mobile + zero dependencies

(function () {
  "use strict";

  const DEFAULTS = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
    duration: 700,
    once: true
  };

  let observer;

  function init(options = {}) {
    const settings = { ...DEFAULTS, ...options };

    const elements = document.querySelectorAll("[data-aos]");

    if (!elements.length) return;

    observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animate(entry.target, settings);

          if (settings.once) {
            observer.unobserve(entry.target);
          }
        }
      });
    }, settings);

    elements.forEach((el) => {
      el.classList.add("aos-init");
      observer.observe(el);
    });
  }

  function prepare(el) {
    // Initial hidden states are handled via CSS (.aos-init[data-aos])
    // to ensure visibility if JS fails.
  }

  function animate(el, settings) {
    const delay = el.dataset.aosDelay || 0;
    const duration = el.dataset.aosDuration || settings.duration;

    el.style.transitionDelay = `${delay}ms`;
    el.style.transitionDuration = `${duration}ms`;

    el.classList.add("aos-animate");
  }

  // Expose globally
  window.AOS = {
    init
  };

})();