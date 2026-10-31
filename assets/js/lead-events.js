/* ZENITH WATER — Lead event layer (GA4-ready, no GA4 installed)
 * Pushes conversion-intent events to window.dataLayer; when GA4 is later
 * authorised, the tag picks these up with zero further code (spec:
 * research/zenith-growth-transformation/13-analytics-and-revenue/).
 * Events: whatsapp_click, phone_click (pincode_check lives in pincode-checker.js)
 * Rules: session-level dedupe per element; never blocks navigation; silent failures.
 */
(function () {
  'use strict';
  if (window.__zenLeadEvents) return;
  window.__zenLeadEvents = true;

  var fired = {};

  function family(path) {
    if (path === '/' || path === '/index.html') return 'home';
    if (path.indexOf('/blog') === 0) return 'blog';
    if (path.indexOf('/pages/product') === 0) return 'product';
    if (path.indexOf('/pages') === 0) return 'utility';
    if (/-water-supply$/.test(path)) return 'city-hub';
    if (/\/water-supply-for-/.test(path)) return 'industry';
    if (/office-|corporate-|commercial-/.test(path)) return 'corporate';
    if (/20-litre|20-liter|bisleri-|bulk-|event-/.test(path)) return 'product-city';
    if (/kolkata|howrah|hooghly|midnapore|24-parganas|durgapur|asansol|burdwan$/.test(path)) return 'city';
    if (/packaged-drinking-water-|water-delivery-|water-supplier-/.test(path)) return 'locality';
    return 'other';
  }

  function segmentFor(path) {
    if (/office-|corporate-|commercial-/.test(path)) return 'office';
    if (/water-supply-for-hotels|water-supply-for-restaurants/.test(path)) return 'hotels-restaurants';
    if (/water-supply-for-/.test(path)) return 'bulk';
    if (/bulk-|event-/.test(path)) return 'bulk';
    if (/distributor/.test(path)) return 'distributor';
    if (/pages\/products|product-\d/.test(path)) return 'retail-products';
    return 'household';
  }

  function push(evt, el, path) {
    var key = evt + ':' + path + ':' + (el.getAttribute('href') || '').slice(0, 60);
    if (fired[key]) return;
    fired[key] = true;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: evt,
      page_url: location.pathname,
      page_family: family(path),
      segment: segmentFor(path),
      cta_type: el.getAttribute('data-cta') || (evt === 'whatsapp_click' ? 'whatsapp' : 'phone')
    });
  }

  document.addEventListener('click', function (e) {
    try {
      var a = e.target && e.target.closest ? e.target.closest('a') : null;
      if (!a) return;
      var href = a.getAttribute('href') || '';
      var path = location.pathname.replace(/\.html$/, '') || '/';
      if (href.indexOf('wa.me/') !== -1 || href.indexOf('whatsapp') !== -1) {
        push('whatsapp_click', a, path);
      } else if (href.indexOf('tel:') === 0) {
        push('phone_click', a, path);
      }
    } catch (err) { /* never block navigation */ }
  }, { passive: true });
})();
