/**
 * Vercel Speed Insights - Initialization
 * Tracks Core Web Vitals and performance metrics
 */

// Import and initialize Speed Insights from Vercel CDN
import { injectSpeedInsights } from 'https://cdn.jsdelivr.net/npm/@vercel/speed-insights@1/+esm';

// Initialize Speed Insights with the current route
injectSpeedInsights({
  route: window.location.pathname,
  framework: 'vanilla'
});
