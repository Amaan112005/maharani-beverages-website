/* Zenith Water — Service Worker v1.0 */
const CACHE_NAME = 'zenith-v1';
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/assets/css/variables.css',
  '/assets/css/main.css',
  '/assets/css/mobile-perfection.css',
  '/assets/js/main.js',
  '/assets/js/aos.js',
  '/assets/js/enquiry-cart.js',
  '/zenith_logo_compact.png'
];

// Install: Pre-cache critical assets
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS))
  );
  self.skipWaiting();
});

// Activate: Clean old caches
self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch: Cache-first for static assets, network-first for HTML
self.addEventListener('fetch', (e) => {
  const { request } = e;
  const url = new URL(request.url);
  
  // Cache static assets (CSS, JS, images, fonts)
  if (request.destination === 'style' || request.destination === 'script' || 
      request.destination === 'image' || request.destination === 'font') {
    e.respondWith(
      caches.match(request).then((cached) => {
        const fetchPromise = fetch(request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
          }
          return networkResponse;
        }).catch(() => cached);
        return cached || fetchPromise;
      })
    );
    return;
  }
  
  // Network-first for HTML pages
  if (request.destination === 'document' || request.mode === 'navigate') {
    e.respondWith(
      fetch(request).catch(() => caches.match(request))
    );
    return;
  }
  
  // Default: try cache, then network
  e.respondWith(
    caches.match(request).then((cached) => cached || fetch(request))
  );
});
