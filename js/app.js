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

  function animateCounters() {
    const counters = document.querySelectorAll('.stat-number, .zd-stat-number');

    counters.forEach((counter) => {
      const rawText = counter.textContent || '';
      const target = Number.parseInt(rawText.replace(/[^0-9]/g, ''), 10);

      if (Number.isNaN(target)) return;

      const suffix = rawText.replace(/[0-9]/g, '');
      const duration = 2000;
      const step = target / (duration / 16);
      let current = 0;

      const update = () => {
        current += step;

        if (current < target) {
          counter.textContent = `${Math.floor(current)}${suffix}`;
          window.requestAnimationFrame(update);
          return;
        }

        counter.textContent = `${target}${suffix}`;
      };

      update();
    });
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
  }

  window.ZenoApp = {
    init,
    animateCounters,
  };

  onReady(init);
})();
