document.addEventListener('DOMContentLoaded', () => {
  const steps = document.querySelectorAll('.journey-step');
  const progressLine = document.getElementById('journey-progress');
  const container = document.querySelector('.patient-journey-container');

  if (!steps.length || !progressLine || !container) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
        } else {
          // Optional: remove active class when scrolling up to replay animation
          entry.target.classList.remove('active');
        }
      });
    },
    {
      root: null,
      threshold: 0.5,
      rootMargin: "0px 0px -100px 0px"
    }
  );

  steps.forEach(step => observer.observe(step));

  // Animate the central green glowing line based on scroll depth inside the container
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        const rect = container.getBoundingClientRect();
        const windowHeight = window.innerHeight;
        
        // Calculate how far the container has been scrolled through
        const startOffset = windowHeight * 0.7; // Start drawing line when container is 70% in view
        let scrolled = startOffset - rect.top;
        let totalScrollable = rect.height;
        
        let percentage = (scrolled / totalScrollable) * 100;
        
        // Clamp between 0 and 100
        percentage = Math.max(0, Math.min(100, percentage));
        
        progressLine.style.height = `${percentage}%`;
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
});
