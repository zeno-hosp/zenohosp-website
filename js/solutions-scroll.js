document.addEventListener('DOMContentLoaded', () => {
  const wrapper = document.getElementById('solutions-wrapper');
  const section = document.getElementById('solutions');
  const track = document.getElementById('solutions-track');

  if (!wrapper || !section || !track) return;

  function setHeight() {
    // Disable scrolljacking on mobile completely
    if (window.innerWidth <= 992) {
      wrapper.style.height = 'auto';
      track.style.transform = 'none';
      return;
    }

    // Use clientWidth to ignore scrollbar width, and add 120px buffer for right padding
    const maxTranslate = track.scrollWidth - document.documentElement.clientWidth + 120;
    
    // If cards fit entirely on screen, no need to scrolljack
    if (maxTranslate > 0) {
      // The wrapper height equals the screen height + the amount we need to scroll horizontally
      // This means 1px of vertical scroll = 1px of horizontal scroll
      wrapper.style.height = `${window.innerHeight + maxTranslate + 100}px`; // +100 for a bit of padding at end
    } else {
      wrapper.style.height = 'auto';
    }
    updateScroll();
  }

  function updateScroll() {
    // Abort on mobile to prevent overriding the vertical stack
    if (window.innerWidth <= 992) return;

    const maxTranslate = track.scrollWidth - document.documentElement.clientWidth + 120;
    if (maxTranslate <= 0) {
      track.style.transform = `translateX(0px)`;
      return;
    }

    const wrapperRect = wrapper.getBoundingClientRect();
    const wrapperTop = wrapperRect.top;
    
    // If wrapper is below viewport, we haven't reached it yet
    if (wrapperTop > 0) {
      track.style.transform = `translateX(0px)`;
      return;
    }

    // Calculate how far we've scrolled past the top of the wrapper
    const scrolled = -wrapperTop;
    
    // Clamp the translation between 0 and maxTranslate
    let translateX = Math.max(0, Math.min(scrolled, maxTranslate));

    // Apply the translation
    track.style.transform = `translateX(-${translateX}px)`;
  }

  // Use requestAnimationFrame for smooth scrolling if preferred, but passive scroll listener is usually fine
  window.addEventListener('resize', setHeight);
  window.addEventListener('scroll', updateScroll, { passive: true });
  
  // Initial setup after fonts/images load
  window.addEventListener('load', setHeight);
  setHeight(); // run immediately as well
});
