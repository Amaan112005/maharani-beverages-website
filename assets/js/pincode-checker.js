/* ZENITH WATER — Pincode availability checker (standalone embed)
 * Data source: /assets/data/pincodes.json (owner-approved serviceability DB).
 * Three honest states per owner condition:
 *   available      — exact pincode match in the database
 *   region         — pincode prefix matches a served region (confirm exact slot)
 *   unconfirmed    — anything else (NO delivery promises; WhatsApp enquiry only)
 * Accessibility: labelled input, aria-live result, numeric input mode.
 * Analytics-ready: fires window.dataLayer event `pincode_check` (no GA4 installed).
 */
(function () {
  'use strict';

  var DB = null;
  var loading = null;

  var REGION_PREFIXES = [
    ['700', 'Kolkata'],
    ['711', 'Howrah'],
    ['712', 'Hooghly'],
    ['721', 'Midnapore'],
    ['743', '24 Parganas'],
    ['713', 'Durgapur / Asansol / Burdwan region']
  ];

  function loadDB() {
    if (DB) return Promise.resolve(DB);
    if (!loading) {
      loading = fetch('assets/data/pincodes.json')
        .then(function (r) { return r.json(); })
        .then(function (d) { DB = d || {}; return DB; })
        .catch(function () { DB = {}; return DB; });
    }
    return loading;
  }

  function waLink(text) {
    return 'https://wa.me/918274837341?text=' + encodeURIComponent(text);
  }

  function render(res, html) {
    res.innerHTML = html;
    if (window.dataLayer) {
      window.dataLayer.push({ event: 'pincode_check' });
    }
  }

  window.zenithPincodeCheck = function (e) {
    e.preventDefault();
    var form = e.target;
    var input = form.querySelector('.zc-input');
    var res = form.parentNode.querySelector('.zc-result');
    var val = (input.value || '').trim();

    if (!/^\d{6}$/.test(val)) {
      res.innerHTML = '<div class="pincode-result-msg error" role="alert">⚠ Please enter a valid 6-digit pincode.</div>';
      return;
    }
    res.innerHTML = '<div class="pincode-result-msg checking" aria-live="polite">🔍 Checking availability…</div>';
    loadDB().then(function (db) {
      var area = db[val];
      if (area) {
        render(res,
          '<div class="pincode-result-card available">' +
          '<div class="pincode-area-name">📍 ' + area + '</div>' +
          '<div class="pincode-status">✅ Zenith delivers to your area</div>' +
          '<div class="pincode-actions"><a href="' + waLink('Hi Zenith, I want to order 20L jar water in ' + area + ' (pincode ' + val + '). Please share price and delivery slot.') +
          '" target="_blank" rel="noopener noreferrer" class="pincode-btn-primary">💬 Order on WhatsApp</a></div></div>');
        return;
      }
      var region = null;
      for (var i = 0; i < REGION_PREFIXES.length; i++) {
        if (val.indexOf(REGION_PREFIXES[i][0]) === 0) { region = REGION_PREFIXES[i][1]; break; }
      }
      if (region) {
        render(res,
          '<div class="pincode-result-card available">' +
          '<div class="pincode-area-name">📍 ' + region + ' region</div>' +
          '<div class="pincode-status">✅ Zenith delivers across the ' + region + ' region</div>' +
          '<div class="pincode-delivery">Confirm your exact delivery slot on WhatsApp</div>' +
          '<div class="pincode-actions"><a href="' + waLink('Hi Zenith, my pincode is ' + val + ' (' + region + ' region). Please confirm delivery to my exact address and share prices.') +
          '" target="_blank" rel="noopener noreferrer" class="pincode-btn-primary">💬 Confirm on WhatsApp</a></div></div>');
        return;
      }
      render(res,
        '<div class="pincode-result-card unavailable">' +
        '<div class="pincode-status">⚠ Delivery to ' + val + ' is not confirmed yet</div>' +
        '<div class="pincode-delivery">We will verify serviceability and reply with exact details.</div>' +
        '<div class="pincode-actions"><a href="' + waLink('Hi Zenith, please confirm whether you deliver to pincode ' + val + ', and share prices if available.') +
        '" target="_blank" rel="noopener noreferrer" class="pincode-btn-secondary">📩 Check availability on WhatsApp</a></div></div>');
    });
  };
})();
