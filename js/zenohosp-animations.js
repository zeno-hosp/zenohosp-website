/**
 * Zeno Hosp - zenohosp-Style Animations & Interactions
 */

document.addEventListener('DOMContentLoaded', function () {
    initNavbar();
    initRevealAnimations();
    initHeroSwitcher();
    initMobileMenu();
    initSmoothScroll();
    initHoverEffects();
    initParallax();
});

/**
 * Navbar scroll effect
 */
function initNavbar() {
    const navbar = document.querySelector('.zd-navbar, .navbar');
    if (!navbar) return;

    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;

        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });
}

/**
 * Scroll reveal animations
 */
function initRevealAnimations() {
    const revealElements = document.querySelectorAll('.zd-reveal, .reveal');

    if (!revealElements.length) return;

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');

                // Trigger stagger animation for children
                if (entry.target.classList.contains('zd-stagger')) {
                    entry.target.querySelectorAll('*').forEach((child, i) => {
                        child.style.transitionDelay = `${i * 0.1}s`;
                    });
                }
            }
        });
    }, observerOptions);

    revealElements.forEach(el => observer.observe(el));
}

/**
 * Hero product switcher
 */
function initHeroSwitcher() {
    const buttons = document.querySelectorAll('.switcher-btn, .zd-switcher-btn');
    const views = document.querySelectorAll('.hero-view, .zd-hero-view');

    if (!buttons.length) return;

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const target = btn.dataset.target;

            // Update buttons
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Update views with animation
            views.forEach(view => {
                view.classList.remove('active');
                view.style.opacity = '0';
                view.style.transform = 'translateY(20px)';
            });

            const activeView = document.getElementById(`view-${target}`);
            if (activeView) {
                setTimeout(() => {
                    activeView.classList.add('active');
                    activeView.style.opacity = '1';
                    activeView.style.transform = 'translateY(0)';
                }, 150);
            }
        });
    });
}

/**
 * Mobile menu toggle
 */
function initMobileMenu() {
    const toggle = document.querySelector('.mobile-toggle, .zd-mobile-toggle');
    const menu = document.querySelector('.nav-links, .zd-nav-links');

    if (!toggle || !menu) return;

    toggle.addEventListener('click', () => {
        menu.classList.toggle('active');
        toggle.classList.toggle('active');
    });

    // Close on link click
    menu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            menu.classList.remove('active');
            toggle.classList.remove('active');
        });
    });
}

/**
 * Smooth scroll for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const navHeight = document.querySelector('.navbar, .zd-navbar')?.offsetHeight || 80;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Button and card hover effects
 */
function initHoverEffects() {
    // Magnetic button effect
    const buttons = document.querySelectorAll('.zd-btn-primary');

    buttons.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            btn.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px)`;
        });

        btn.addEventListener('mouseleave', () => {
            btn.style.transform = 'translate(0, 0)';
        });
    });

    // Card tilt effect
    const cards = document.querySelectorAll('.zd-card, .solution-bento-card');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width;
            const y = (e.clientY - rect.top) / rect.height;

            const tiltX = (y - 0.5) * 5;
            const tiltY = (x - 0.5) * -5;

            card.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateZ(10px)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateZ(0)';
        });
    });
}

/**
 * Parallax scrolling effects
 */
function initParallax() {
    const parallaxElements = document.querySelectorAll('.zd-parallax, .zd-float');

    if (!parallaxElements.length) return;

    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;

        parallaxElements.forEach(el => {
            const speed = el.dataset.speed || 0.1;
            const yPos = scrollY * speed;
            el.style.transform = `translateY(${yPos}px)`;
        });
    });
}

/**
 * Counter animation for stats
 */
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number, .zd-stat-number');

    counters.forEach(counter => {
        const target = parseInt(counter.textContent.replace(/[^0-9]/g, ''));
        const suffix = counter.textContent.replace(/[0-9]/g, '');
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += step;
            if (current < target) {
                counter.textContent = Math.floor(current) + suffix;
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target + suffix;
            }
        };

        updateCounter();
    });
}

// Export for external use
window.ZenoAnimations = {
    initRevealAnimations,
    animateCounters,
    initHoverEffects
};
