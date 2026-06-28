/**
 * Zeno Hosp Frontend App
 * Single entrypoint for shared UI behavior across all pages.
 */
(function () {
  'use strict';

  if (window.__zenoAppBooted) return;
  window.__zenoAppBooted = true;

  const prefersReducedMotion =
    typeof window.matchMedia === 'function' &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function onReady(callback) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', callback, { once: true });
      return;
    }

    callback();
  }

  function initNavbar() {
    const navbar = document.querySelector('#main-nav, .navbar, .zd-navbar');
    if (!navbar) return;

    const update = () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    };

    update();
    window.addEventListener('scroll', update, { passive: true });
  }

  function initMobileMenu() {
    const idToggle = document.getElementById('mobile-toggle');
    const idMenu = document.getElementById('mobile-menu');
    const idOverlay = document.getElementById('mobile-overlay');
    const solutionsToggle = document.getElementById('solutions-toggle');
    const solutionsDropdown = document.getElementById('solutions-dropdown');

    if (idToggle && idMenu) {
      const setMenuOpen = (isOpen) => {
        idToggle.classList.toggle('active', isOpen);
        idMenu.classList.toggle('active', isOpen);
        if (idOverlay) idOverlay.classList.toggle('active', isOpen);
        document.body.style.overflow = isOpen ? 'hidden' : '';
        idToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      };

      idToggle.addEventListener('click', () => {
        setMenuOpen(!idMenu.classList.contains('active'));
      });

      if (idOverlay) {
        idOverlay.addEventListener('click', () => setMenuOpen(false));
      }

      if (solutionsToggle && solutionsDropdown) {
        solutionsToggle.addEventListener('click', () => {
          solutionsToggle.classList.toggle('active');
          solutionsDropdown.classList.toggle('active');
        });
      }

      idMenu.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => setMenuOpen(false));
      });

      return;
    }

    const classToggle = document.querySelector('.mobile-toggle, .zd-mobile-toggle');
    const classMenu = document.querySelector('.nav-links, .zd-nav-links');
    if (!classToggle || !classMenu) return;

    classToggle.addEventListener('click', () => {
      classMenu.classList.toggle('active');
      classToggle.classList.toggle('active');
    });

    classMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        classMenu.classList.remove('active');
        classToggle.classList.remove('active');
      });
    });
  }

  function initSmoothScroll() {
    const nav = document.querySelector('#main-nav, .navbar, .zd-navbar');

    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener('click', (event) => {
        const targetId = anchor.getAttribute('href');
        if (!targetId || targetId === '#') return;

        const target = document.querySelector(targetId);
        if (!target) return;

        event.preventDefault();

        const navHeight = nav ? nav.offsetHeight : 80;
        const targetTop = target.getBoundingClientRect().top + window.pageYOffset - navHeight;

        window.scrollTo({
          top: targetTop,
          behavior: prefersReducedMotion ? 'auto' : 'smooth',
        });
      });
    });
  }

  function initRevealAnimations() {
    const revealElements = document.querySelectorAll('.reveal, .zd-reveal');
    if (!revealElements.length) return;

    if (typeof IntersectionObserver !== 'function') {
      revealElements.forEach((el) => el.classList.add('active'));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;

          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        });
      },
      {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px',
      }
    );

    revealElements.forEach((el) => observer.observe(el));
  }

  function initDataAosAnimations() {
    const aosElements = document.querySelectorAll('[data-aos]');
    if (!aosElements.length) return;

    if (typeof IntersectionObserver !== 'function') {
      aosElements.forEach((el) => el.classList.add('aos-animate'));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;

          entry.target.classList.add('aos-animate');
          observer.unobserve(entry.target);
        });
      },
      {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px',
      }
    );

    aosElements.forEach((el) => observer.observe(el));
  }

  function initSolutionTabs() {
    const tabs = document.querySelectorAll('.solution-tab');
    const panels = document.querySelectorAll('.solution-panel');

    if (!tabs.length || !panels.length) return;

    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        const target = tab.dataset.target;
        if (!target) return;

        tabs.forEach((item) => item.classList.remove('active'));
        panels.forEach((panel) => panel.classList.remove('active'));

        tab.classList.add('active');

        const panel = document.getElementById(target);
        if (panel) panel.classList.add('active');
      });
    });
  }

  function initHeroSwitcher() {
    const buttons = document.querySelectorAll('.switcher-btn, .zd-switcher-btn');
    const views = document.querySelectorAll('.hero-view, .zd-hero-view');

    if (!buttons.length || !views.length) return;

    buttons.forEach((button) => {
      button.addEventListener('click', () => {
        const target = button.dataset.target;
        if (!target) return;

        buttons.forEach((item) => item.classList.remove('active'));
        button.classList.add('active');

        views.forEach((view) => {
          view.classList.remove('active');
          view.style.opacity = '0';
          view.style.transform = 'translateY(20px)';
        });

        const activeView = document.getElementById(`view-${target}`);
        if (!activeView) return;

        const activateView = () => {
          activeView.classList.add('active');
          activeView.style.opacity = '1';
          activeView.style.transform = 'translateY(0)';
        };

        if (prefersReducedMotion) {
          activateView();
          return;
        }

        window.setTimeout(activateView, 150);
      });
    });
  }

  function initHoverEffects() {
    if (prefersReducedMotion) return;

    const buttons = document.querySelectorAll('.zd-btn-primary');
    buttons.forEach((button) => {
      button.addEventListener('mousemove', (event) => {
        const rect = button.getBoundingClientRect();
        const x = event.clientX - rect.left - rect.width / 2;
        const y = event.clientY - rect.top - rect.height / 2;

        button.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px)`;
      });

      button.addEventListener('mouseleave', () => {
        button.style.transform = 'translate(0, 0)';
      });
    });

    const cards = document.querySelectorAll('.zd-card, .solution-bento-card');
    cards.forEach((card) => {
      card.addEventListener('mousemove', (event) => {
        const rect = card.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width;
        const y = (event.clientY - rect.top) / rect.height;

        const tiltX = (y - 0.5) * 5;
        const tiltY = (x - 0.5) * -5;

        card.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateZ(10px)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateZ(0)';
      });
    });
  }

  function initParallax() {
    if (prefersReducedMotion) return;

    const parallaxElements = document.querySelectorAll('.zd-parallax, .zd-float');
    if (!parallaxElements.length) return;

    let ticking = false;

    const update = () => {
      const scrollY = window.scrollY;

      parallaxElements.forEach((element) => {
        const speed = Number.parseFloat(element.dataset.speed || '0.1');
        if (Number.isNaN(speed)) return;

        element.style.transform = `translateY(${scrollY * speed}px)`;
      });

      ticking = false;
    };

    const onScroll = () => {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(update);
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    update();
  }

  function animateCounters(counters) {
    counters = counters || document.querySelectorAll('.stat-number, .zd-stat-number');

    counters.forEach((counter) => {
      const rawText = (counter.textContent || '').trim();

      // Skip values that aren't simple counts (e.g. "24/7")
      if (rawText.includes('/')) return;

      // Extract optional prefix, numeric value (inc. decimal), and suffix
      const match = rawText.match(/^([^0-9]*)(\d+(?:\.\d+)?)(.*)$/);
      if (!match) return;

      const prefix = match[1];
      const target = Number.parseFloat(match[2]);
      const suffix = match[3];
      const isDecimal = rawText.includes('.');

      if (Number.isNaN(target)) return;

      const step = target / (2000 / 16);
      let current = 0;

      const update = () => {
        current = Math.min(current + step, target);
        const display = isDecimal ? current.toFixed(1) : Math.floor(current);
        counter.textContent = `${prefix}${display}${suffix}`;
        if (current < target) window.requestAnimationFrame(update);
      };

      update();
    });
  }

  function initCounterAnimation() {
    const section = document.querySelector('.home-stats-section, .zd-stats-section');
    if (!section) return;

    if (typeof IntersectionObserver !== 'function') {
      animateCounters(section.querySelectorAll('.stat-number, .zd-stat-number'));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          observer.unobserve(entry.target);
          animateCounters(entry.target.querySelectorAll('.stat-number, .zd-stat-number'));
        });
      },
      { threshold: 0.4 }
    );

    observer.observe(section);
  }

  function initPlatformStrip() {
    const switcher = document.querySelector('.module-switcher');
    if (!switcher) return;

    // Derive the active module from the URL path, e.g. /apps/hms/ → 'hms'
    const segments = window.location.pathname.split('/').filter(Boolean);
    const module = segments[1]; // apps/<module>/
    if (!module) return;

    switcher.querySelectorAll('a').forEach((link) => {
      const href = link.getAttribute('href') || '';
      if (href.includes(`apps/${module}`)) link.classList.add('active');
    });
  }

  function initScrollExpand() {
    const expandSection = document.querySelector('.home-integration-section');
    if (!expandSection) return;

    let ticking = false;
    const update = () => {
      const rect = expandSection.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      const start = windowHeight; 
      const end = windowHeight * 0.3; 
      
      let progress = (start - rect.top) / (start - end);
      progress = Math.max(0, Math.min(1, progress));
      
      expandSection.style.setProperty('--expand-progress', progress.toFixed(3));
      ticking = false;
    };

    const onScroll = () => {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(update);
      }
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    update();
  }


  function initBottomMobileNav() {
    // Ensure we are on mobile/tablet view
    if (window.innerWidth > 992) return;
    
    // Skip on documentation pages
    if (window.location.pathname.includes('/docs/')) return;
    
    // Don't inject multiple times
    if (document.getElementById('mobile-bottom-bar')) return;
    
    const toggle = document.getElementById('mobile-toggle');
    const menu = document.getElementById('mobile-menu');
    if (!toggle || !menu) return;

    // Create the bottom bar
    const bottomBar = document.createElement('div');
    bottomBar.className = 'mobile-bottom-bar';
    bottomBar.id = 'mobile-bottom-bar';

    // Move toggle button into the bottom bar
    bottomBar.appendChild(toggle);

    // Create and append the Sign In link (Bubble 2)
    let signinLink = document.querySelector('.nav-actions .signin') || document.querySelector('.ps-right a:not(.btn-primary)');
    if (signinLink) {
      const mobileSignIn = document.createElement('a');
      mobileSignIn.className = 'bottom-bar-signin';
      mobileSignIn.innerText = 'Sign In';
      mobileSignIn.href = signinLink.getAttribute('href') || 'javascript:void(0)';
      bottomBar.appendChild(mobileSignIn);
    }

    // Create and append the Request Demo CTA (Bubble 3)
    let ctaLink = document.querySelector('.nav-actions .btn-primary') || document.querySelector('.ps-right .btn-primary');
    let href = ctaLink ? ctaLink.getAttribute('href') : '/contact-us/index.html';
    
    const mobileCta = document.createElement('a');
    mobileCta.className = 'bottom-bar-cta';
    mobileCta.innerText = 'Request Demo';
    mobileCta.href = href;
    bottomBar.appendChild(mobileCta);

    document.body.appendChild(bottomBar);
  }

  function initDemoModal() {
    document.addEventListener('click', function (e) {
      const link = e.target.closest('a');
      if (!link) return;
      
      const href = link.getAttribute('href') || '';
      const text = (link.textContent || '').trim().toLowerCase();
      
      // If the link points to contact us and has the word "demo"
      if (href.includes('contact-us') && text.includes('demo')) {
        const modal = document.querySelector('demo-modal');
        if (modal && typeof modal.open === 'function') {
          e.preventDefault();
          modal.open();
        }
      }
    });
  }

  function initAnalyticsTracking() {
    // Track clicks on 'Request Demo' buttons
    document.querySelectorAll('a[href*="/contact-us"]').forEach((btn) => {
      btn.addEventListener('click', () => {
        if (typeof gtag === 'function') {
          gtag('event', 'request_demo_click', {
            'event_category': 'engagement',
            'event_label': window.location.pathname
          });
        }
      });
    });

    // Track clicks on Pricing links
    document.querySelectorAll('a[href*="/pricing"]').forEach((btn) => {
      btn.addEventListener('click', () => {
        if (typeof gtag === 'function') {
          gtag('event', 'pricing_view_click', {
            'event_category': 'engagement',
            'event_label': window.location.pathname
          });
        }
      });
    });
  }

  function initIdlePopup() {
    var IDLE_MS = 60000;
    var timer = null;
    var shown = false;
    var dismissed = sessionStorage.getItem('zeno_idle_dismissed');

    if (dismissed) return;

    var overlay = document.createElement('div');
    overlay.className = 'idle-popup-overlay';
    overlay.innerHTML =
      '<div class="idle-popup">' +
        '<button class="idle-popup-close" aria-label="Close">&times;</button>' +
        '<div class="idle-popup-badge">Limited Offer</div>' +
        '<h3>Start with <span class="idle-popup-highlight">₹0 payment</span></h3>' +
        '<p>Pay as per bed count and patient flow after each month. No upfront costs, no lock-in.</p>' +
        '<a href="/contact-us/index.html" class="idle-popup-cta">Book a Free Demo</a>' +
        '<span class="idle-popup-note">75+ hospitals already onboarded</span>' +
      '</div>';

    var style = document.createElement('style');
    style.textContent =
      '.idle-popup-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);z-index:10000;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s}' +
      '.idle-popup-overlay.active{opacity:1;visibility:visible}' +
      '.idle-popup{background:#fff;border-radius:20px;padding:40px 36px;max-width:420px;width:90%;text-align:center;position:relative;box-shadow:0 24px 64px rgba(0,0,0,.2);transform:translateY(20px) scale(.96);transition:transform .35s cubic-bezier(.4,0,.2,1)}' +
      '.idle-popup-overlay.active .idle-popup{transform:translateY(0) scale(1)}' +
      '.idle-popup-close{position:absolute;top:14px;right:14px;background:none;border:none;font-size:1.5rem;color:#999;cursor:pointer;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;transition:background .2s,color .2s}' +
      '.idle-popup-close:hover{background:#f5f5f2;color:#11110d}' +
      '.idle-popup-badge{display:inline-block;padding:5px 14px;background:rgba(13,148,136,.1);border:1px solid rgba(13,148,136,.25);border-radius:100px;font-size:.75rem;font-weight:700;color:#0d9488;text-transform:uppercase;letter-spacing:.08em;margin-bottom:16px}' +
      '.idle-popup h3{font-size:1.75rem;font-weight:800;color:#11110d;margin:0 0 12px;line-height:1.25}' +
      '.idle-popup-highlight{color:#0d9488}' +
      '.idle-popup p{font-size:1rem;color:#4a4a45;line-height:1.65;margin:0 0 24px}' +
      '.idle-popup-cta{display:inline-block;padding:14px 32px;background:#11110d;color:#fff;font-size:.9375rem;font-weight:700;border-radius:100px;text-decoration:none;transition:background .2s,transform .15s}' +
      '.idle-popup-cta:hover{background:#0d9488;transform:translateY(-2px)}' +
      '.idle-popup-note{display:block;margin-top:14px;font-size:.8rem;color:#6b6b66}';
    document.head.appendChild(style);
    document.body.appendChild(overlay);

    var closeBtn = overlay.querySelector('.idle-popup-close');

    function show() {
      if (shown || sessionStorage.getItem('zeno_idle_dismissed')) return;
      shown = true;
      overlay.classList.add('active');
    }

    function dismiss() {
      overlay.classList.remove('active');
      sessionStorage.setItem('zeno_idle_dismissed', '1');
      clearTimeout(timer);
    }

    function resetTimer() {
      clearTimeout(timer);
      if (!shown) timer = setTimeout(show, IDLE_MS);
    }

    closeBtn.addEventListener('click', dismiss);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) dismiss();
    });

    ['mousemove', 'keydown', 'scroll', 'touchstart', 'click'].forEach(function (evt) {
      document.addEventListener(evt, resetTimer, { passive: true });
    });

    document.addEventListener('visibilitychange', function () {
      if (document.visibilityState === 'visible') show();
    });

    resetTimer();
  }

  function init() {
    initNavbar();
    initMobileMenu();
    initSmoothScroll();
    initRevealAnimations();
    initDataAosAnimations();
    initSolutionTabs();
    initHeroSwitcher();
    initHoverEffects();
    initParallax();
    initPlatformStrip();
    initCounterAnimation();
    initScrollExpand();
    initBottomMobileNav();
    initDemoModal();
    initAnalyticsTracking();
    initIdlePopup();
  }

  window.ZenoApp = {
    init,
    animateCounters,
  };

  onReady(init);
})();
