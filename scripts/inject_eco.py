import os

def update_homepage():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    new_css = """
  .ecosystem-section {
    padding: 100px 0;
    background: #0a0a08;
    color: #fff;
    border-top: 1px solid rgba(255,255,255,0.05);
  }
  .ecosystem-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 32px;
    margin-top: 60px;
  }
  .eco-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 40px;
    transition: all 0.3s ease;
    text-decoration: none;
    color: #fff;
    display: flex;
    flex-direction: column;
    height: 100%;
    position: relative;
    overflow: hidden;
  }
  .eco-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at top right, var(--eco-color), transparent 70%);
    opacity: 0;
    transition: opacity 0.4s ease;
    z-index: 0;
  }
  .eco-card:hover {
    transform: translateY(-8px);
    border-color: rgba(255,255,255,0.2);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
  }
  .eco-card:hover::before {
    opacity: 0.15;
  }
  .eco-content {
    position: relative;
    z-index: 1;
    flex: 1;
  }
  .eco-icon {
    width: 60px;
    height: 60px;
    background: rgba(255,255,255,0.05);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
    color: var(--eco-color);
    transition: all 0.3s ease;
  }
  .eco-card:hover .eco-icon {
    background: var(--eco-color);
    color: #fff;
    transform: scale(1.1);
  }
  .eco-card h3 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 12px;
  }
  .eco-card p {
    color: #9ca3af;
    line-height: 1.6;
    margin-bottom: 24px;
  }
  .eco-link {
    margin-top: auto;
    font-weight: 600;
    color: var(--eco-color);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .eco-link svg {
    transition: transform 0.3s ease;
  }
  .eco-card:hover .eco-link svg {
    transform: translateX(5px);
  }
</style>
"""
    if "ecosystem-section" not in content:
        content = content.replace("</style>", new_css)
    
    new_section = """
  <!-- Services Ecosystem Section -->
  <section class="ecosystem-section">
    <div class="container">
      <div style="text-align: center; max-width: 800px; margin: 0 auto;">
        <div style="display:inline-block; padding: 6px 16px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 100px; color: #10b981; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">ZenoHosp Digital Services</div>
        <h2 style="font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 800; margin-bottom: 24px; line-height: 1.1;">End-to-End Hospital<br><span style="color: #10b981;">Growth Engine</span></h2>
        <p style="font-size: 1.2rem; color: #9ca3af;">Beyond software, we provide the elite digital infrastructure your hospital needs to attract patients, build authority, and scale revenue.</p>
      </div>

      <div class="ecosystem-grid">
        <!-- Websites -->
        <a href="/services/digital-presence/index.html" class="eco-card" style="--eco-color: #10b981;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            </div>
            <h3>Hospital Websites</h3>
            <p>Premium, high-speed websites with local SEO optimization to dominate Google searches.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>

        <!-- Custom Software -->
        <a href="/services/custom-software/index.html" class="eco-card" style="--eco-color: #f97316;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>
            </div>
            <h3>Custom Software</h3>
            <p>Bespoke medical modules, patient portals, and integrations tailored to your workflows.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>

        <!-- Social Media -->
        <a href="/services/social-media/index.html" class="eco-card" style="--eco-color: #a855f7;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
            </div>
            <h3>Social Media</h3>
            <p>Viral, highly professional content and reels that position your doctors as thought leaders.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>

        <!-- Advertising -->
        <a href="/services/advertising/index.html" class="eco-card" style="--eco-color: #3b82f6;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            </div>
            <h3>Healthcare Ads</h3>
            <p>Targeted Google and Meta ad campaigns that drive high-intent patients to your OPD.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>
        
        <!-- Voim.ai -->
        <a href="/services/voimai/index.html" class="eco-card" style="--eco-color: #ec4899;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
            </div>
            <h3>Voim.ai Agent</h3>
            <p>AI-powered voice receptionist that handles calls, schedules appointments, and follows up automatically.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>
      </div>
    </div>
  </section>

  <!-- Footer -->"""

    if "ecosystem-section" not in content:
        content = content.replace("  <!-- Footer -->", new_section)

    with open(file_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    update_homepage()
    print("Done")
