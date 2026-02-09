/**
 * Legacy compatibility bridge.
 * Loads the consolidated frontend runtime.
 */
(function () {
  'use strict';

  if (window.__zenoAppBooted || window.__zenoLegacyBridgeBooted) return;
  window.__zenoLegacyBridgeBooted = true;

  var existing = document.querySelector('script[src="js/app.js"], script[src$="/js/app.js"]');
  if (existing) return;

  var script = document.createElement('script');
  script.src = 'js/app.js';
  script.defer = true;
  document.head.appendChild(script);
})();
