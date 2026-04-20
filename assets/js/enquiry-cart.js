/**
 * ZENITH WATER — SERVERLESS ENQUIRY CART
 * Handles localStorage aggregation and floating UI elements.
 */

const CART_KEY = 'zenithEnquiryCart';

function initCart() {
  const cart = getCart();
  updateCartBadge(cart);
  injectCartToastContainer();
}

function getCart() {
  try {
    const raw = localStorage.getItem(CART_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch (e) {
    console.warn("Cleared corrupted cart data.");
    localStorage.removeItem(CART_KEY);
    return [];
  }
}

function addToCart(productName, defaultQty = 1, unit = 'cases') {
  let cart = getCart();
  
  // Check if item already exists with the same unit
  let existingItem = cart.find(item => item.product === productName && (item.unit || 'cases') === unit);
  if (existingItem) {
    existingItem.qty += defaultQty;
    existingItem.unit = unit; // ensure backwards compatibility
  } else {
    cart.push({ product: productName, qty: defaultQty, unit: unit });
  }
  
  localStorage.setItem(CART_KEY, JSON.stringify(cart));
  updateCartBadge(cart);
  showToast(`Added ${defaultQty} ${unit} of ${productName}.`);
}

function addCustomToCart(productName, qtyId, unitId) {
  const qtyInput = document.getElementById(qtyId);
  const unitSelect = document.getElementById(unitId);
  
  const qty = qtyInput ? parseInt(qtyInput.value, 10) || 1 : 1;
  const unit = unitSelect ? unitSelect.value : 'cases';
  
  addToCart(productName, qty, unit);
}

function updateCartBadge(cart) {
  const totalTypes = cart.length;
  // Find all badge elements on the page and update them
  const badges = document.querySelectorAll('.cart-badge-count');
  badges.forEach(badge => {
    badge.innerText = totalTypes;
    if (totalTypes > 0) {
      badge.style.display = 'flex';
      badge.classList.add('pulse-badge');
    } else {
      badge.style.display = 'none';
      badge.classList.remove('pulse-badge');
    }
  });
}

function injectCartToastContainer() {
  if (document.getElementById('zenith-toast-container')) return;
  const container = document.createElement('div');
  container.id = 'zenith-toast-container';
  container.style.cssText = 'position:fixed; bottom:30px; left:50%; transform:translateX(-50%); z-index:99999; display:flex; flex-direction:column; gap:10px; pointer-events:none;';
  document.body.appendChild(container);
}

function showToast(message) {
  const container = document.getElementById('zenith-toast-container');
  const toast = document.createElement('div');
  toast.style.cssText = 'background:rgba(10, 61, 107, 0.95); color:white; padding:12px 24px; border-radius:30px; font-size:0.8rem; font-weight:600; letter-spacing:1px; border:1px solid rgba(181,158,109,0.3); box-shadow:0 10px 30px rgba(0,0,0,0.5); backdrop-filter:blur(10px); opacity:0; transform:translateY(20px); transition:all 0.3s cubic-bezier(0.16, 1, 0.3, 1); display:flex; align-items:center; gap:10px;';
  
  toast.innerHTML = `<span style="font-size:1.2em;">✓</span> ${message}`;
  container.appendChild(toast);
  
  // Animate in
  setTimeout(() => {
    toast.style.opacity = '1';
    toast.style.transform = 'translateY(0)';
  }, 10);
  
  // Animate out
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(-20px)';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// Initialize on load
document.addEventListener('DOMContentLoaded', initCart);
