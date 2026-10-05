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
      const servicesToggle = document.getElementById('services-toggle');
      const servicesDropdown = document.getElementById('services-dropdown');

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
        
        if (servicesToggle && servicesDropdown) {
          servicesToggle.addEventListener('click', () => {
            servicesToggle.classList.toggle('active');
            servicesDropdown.classList.toggle('active');
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

  function initFloatingVideoPopup() {
    var path = window.location.pathname.toLowerCase();
    
    // Do not show on docs, careers, legal, or contact pages where focused reading / form filling is key
    if (path.includes('/docs/') || path.includes('/privacy-policy') || path.includes('/terms-of-service') || path.includes('/cookie-policy') || path.includes('/thank-you') || path.includes('/contact-us')) {
      return;
    }

    var videoId = 'jpeR7DkQoGI'; // Default: high-impact Zip Discharge hook
    var videoTitle = 'Why does hospital discharge take half a day?';
    var isShort = true;

    if (path.includes('/pharmacy')) {
      videoId = '1YKVAczmq6I';
      videoTitle = 'Prescription to Pharmacy Sale';
      isShort = false;
    } else if (path.includes('/appointments') || path.includes('/hms')) {
      videoId = 'EQ4B7e3-tN0';
      videoTitle = 'End Double-Booked Appointments';
      isShort = false;
    } else if (path.includes('/lab')) {
      videoId = 'R7q9IrMpx-0';
      videoTitle = 'Lab Investigations & Reports';
      isShort = true;
    } else if (path.includes('/zip-discharge')) {
      videoId = 'jpeR7DkQoGI';
      videoTitle = 'Instant Zip Discharge in Action';
      isShort = true;
    }

    var widget = document.createElement('aside');
    widget.className = 'zeno-video-widget' + (isShort ? ' is-short' : '');
    widget.setAttribute('aria-label', 'Featured video demonstration');

    var originParam = (window.location.origin && window.location.origin !== 'null') ? '&origin=' + encodeURIComponent(window.location.origin) : '';
    // Note: mute=1 is required by modern browser autoplay policies so video autoplays immediately without a play button
    var iframeSrc = 'https://www.youtube.com/embed/' + videoId +
      '?autoplay=1' +
      '&mute=1' +
      '&playsinline=1' +
      '&controls=0' +
      '&modestbranding=1' +
      '&rel=0' +
      '&iv_load_policy=3' +
      '&enablejsapi=1' +
      originParam;

    widget.innerHTML =
      '<div class="zeno-widget-header">' +
        '<div class="zeno-widget-badge"><span class="zeno-widget-dot"></span> Live Demo</div>' +
        '<button class="zeno-widget-close" aria-label="Close video popup" title="Close video">&times;</button>' +
      '</div>' +
      '<div class="zeno-widget-media">' +
        '<iframe ' +
          'id="zeno-widget-iframe" ' +
          'src="' + iframeSrc + '" ' +
          'title="' + videoTitle + '" ' +
          'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" ' +
          'allowfullscreen>' +
        '</iframe>' +
        '<div class="zeno-widget-overlay" role="button" aria-label="Toggle sound" title="Click to toggle sound"></div>' +
      '</div>' +
      '<div class="zeno-widget-footer">' +
        '<div class="zeno-widget-title" title="' + videoTitle + '">' + videoTitle + '</div>' +
        '<div class="zeno-widget-actions">' +
          '<button class="zeno-widget-sound-btn" aria-label="Unmute audio">' +
            '<span class="zeno-sound-icon">🔊</span> <span class="zeno-sound-text">Unmute</span>' +
          '</button>' +
          '<a href="/contact-us/index.html" class="zeno-widget-cta-btn">Book Demo &rarr;</a>' +
        '</div>' +
      '</div>';

    var style = document.createElement('style');
    style.textContent =
      '.zeno-video-widget{position:fixed;bottom:24px;right:24px;z-index:9995;width:290px;background:#11110d;border:1px solid rgba(209,244,112,.35);border-radius:18px;box-shadow:0 16px 40px rgba(0,0,0,.6),0 0 24px rgba(209,244,112,.12);overflow:hidden;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;opacity:0;transform:translateY(30px) scale(.94);visibility:hidden;transition:opacity .4s cubic-bezier(.16,1,.3,1),transform .4s cubic-bezier(.16,1,.3,1),visibility .4s}' +
      '.zeno-video-widget.is-visible{opacity:1;transform:translateY(0) scale(1);visibility:visible}' +
      '.zeno-video-widget.is-short{width:220px}' +
      '.zeno-widget-header{display:flex;justify-content:space-between;align-items:center;padding:8px 12px;background:#11110d;border-bottom:1px solid rgba(255,255,255,.08)}' +
      '.zeno-widget-badge{display:inline-flex;align-items:center;gap:6px;font-size:.72rem;font-weight:700;color:#fff;letter-spacing:.03em}' +
      '.zeno-widget-dot{width:7px;height:7px;border-radius:50%;background:#d1f470;box-shadow:0 0 8px #d1f470;animation:zenoPulse 1.8s infinite}' +
      '@keyframes zenoPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.85)}}' +
      '.zeno-widget-close{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);color:#fff;width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:1.1rem;line-height:1;transition:background .2s,transform .15s,color .2s}' +
      '.zeno-widget-close:hover{background:#dc2626;border-color:#dc2626;color:#fff;transform:scale(1.1)}' +
      '.zeno-widget-media{position:relative;width:100%;background:#000;aspect-ratio:16/9;overflow:hidden}' +
      '.zeno-video-widget.is-short .zeno-widget-media{aspect-ratio:9/16}' +
      '.zeno-widget-media iframe{width:100%;height:100%;border:0;display:block}' +
      '.zeno-widget-overlay{position:absolute;top:0;left:0;right:0;bottom:0;z-index:2;cursor:pointer}' +
      '.zeno-widget-footer{padding:10px 12px;background:#11110d}' +
      '.zeno-widget-title{color:#fff;font-size:.82rem;font-weight:700;line-height:1.35;margin-bottom:8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
      '.zeno-widget-actions{display:flex;align-items:center;justify-content:space-between;gap:8px}' +
      '.zeno-widget-sound-btn{display:inline-flex;align-items:center;gap:4px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);color:#e5e5e5;font-size:.72rem;font-weight:600;padding:5px 9px;border-radius:8px;cursor:pointer;transition:background .2s,color .2s}' +
      '.zeno-widget-sound-btn:hover{background:rgba(209,244,112,.18);color:#d1f470;border-color:rgba(209,244,112,.35)}' +
      '.zeno-widget-cta-btn{display:inline-flex;align-items:center;background:#d1f470;color:#11110d;font-size:.72rem;font-weight:700;padding:5px 11px;border-radius:8px;text-decoration:none;transition:background .2s,transform .15s}' +
      '.zeno-widget-cta-btn:hover{background:#e2f995;transform:translateY(-1px)}' +
      '@media (max-width:768px){.zeno-video-widget{bottom:96px;right:14px;width:210px}.zeno-video-widget.is-short{width:170px}}';

    document.head.appendChild(style);
    document.body.appendChild(widget);

    var iframe = widget.querySelector('iframe');
    var overlay = widget.querySelector('.zeno-widget-overlay');
    var isMuted = true;
    var userManuallyMuted = false;
    var soundBtn = widget.querySelector('.zeno-widget-sound-btn');
    var soundText = widget.querySelector('.zeno-sound-text');
    var soundIcon = widget.querySelector('.zeno-sound-icon');
    var closeBtn = widget.querySelector('.zeno-widget-close');

    function sendCommand(func, args) {
      if (iframe && iframe.contentWindow) {
        var msg = {
          event: 'command',
          func: func,
          args: args !== undefined ? args : ''
        };
        iframe.contentWindow.postMessage(JSON.stringify(msg), '*');
      }
    }

    function unmuteAudio() {
      sendCommand('unMute');
      sendCommand('setVolume', [100]);
      sendCommand('playVideo');
      isMuted = false;
      if (soundText) soundText.textContent = 'Mute';
      if (soundIcon) soundIcon.textContent = '🔇';
      if (soundBtn) soundBtn.setAttribute('aria-label', 'Mute audio');
    }

    function muteAudio() {
      sendCommand('mute');
      isMuted = true;
      if (soundText) soundText.textContent = 'Unmute';
      if (soundIcon) soundIcon.textContent = '🔊';
      if (soundBtn) soundBtn.setAttribute('aria-label', 'Unmute audio');
    }

    // Toggle mute/unmute on user action
    function toggleSound(e) {
      if (e) e.stopPropagation();
      if (isMuted) {
        unmuteAudio();
      } else {
        muteAudio();
      }
    }

    if (soundBtn) {
      soundBtn.addEventListener('click', toggleSound);
    }

    if (overlay) {
      overlay.addEventListener('click', toggleSound);
    }

    if (iframe) {
      iframe.addEventListener('load', function () {
        iframe.contentWindow.postMessage('{"event":"listening"}', '*');
      });
    }

    // Handle seamless looping without playlist parameter & detect YouTube events
    window.addEventListener('message', function (event) {
      try {
        var data = typeof event.data === 'string' ? JSON.parse(event.data) : event.data;
        if (!data) return;

        if (data.event === 'onStateChange') {
          if (data.info === 0) { // 0 = ended -> seamless loop without playlist controls
            sendCommand('seekTo', [0, true]);
            sendCommand('playVideo');
            if (!isMuted) {
              sendCommand('unMute');
            } else {
              sendCommand('mute');
            }
          }
        }
      } catch (e) {}
    });

    // Close / Dismiss: immediately pause, mute and remove
    function dismiss(e) {
      if (e) e.stopPropagation();
      sendCommand('mute');
      sendCommand('pauseVideo');
      widget.classList.remove('is-visible');
      setTimeout(function () {
        if (widget && widget.parentNode) {
          widget.parentNode.removeChild(widget);
        }
      }, 400);
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', dismiss);
    }

    // Show with smooth slide-up after brief 600ms delay
    setTimeout(function () {
      widget.classList.add('is-visible');
    }, 600);
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
    initFloatingVideoPopup();
  }

  window.ZenoApp = {
    init,
    animateCounters,
  };

  onReady(init);
})();
