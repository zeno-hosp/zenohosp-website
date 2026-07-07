import os

def recreate_adv():
    base_dir = "/Users/iniyananbu/Documents/ZenoHosp Website"
    adv_file = os.path.join(base_dir, "services/advertising/index.html")
    index_file = os.path.join(base_dir, "index.html")
    
    with open(index_file, "r") as f:
        index_content = f.read()
        
    start_str = '<!DOCTYPE html>'
    end_str = '  <!-- Hero Section -->'
    head_and_nav = index_content.split(end_str)[0]
    
    # Update title and meta description
    title_start = '<title>'
    title_end = '</title>'
    head_and_nav = head_and_nav.replace(
        head_and_nav[head_and_nav.find(title_start):head_and_nav.find(title_end)+len(title_end)],
        '<title>Healthcare Digital Advertising | ZenoHosp Services</title>'
    )
    
    parts = head_and_nav.split('<meta name="description" content="')
    if len(parts) > 1:
        rest = parts[1].split('">', 1)
        head_and_nav = parts[0] + '<meta name="description" content="ZenoHosp provides high-converting healthcare advertising services including Google Ads, Facebook & Instagram Ads, and YouTube Ads for hospitals.">' + rest[1]

    # Inject CSS for the Advertising page
    new_css = """
  <style>
    body {
      background-color: #0b0f19;
      color: #fff;
    }
    /* Override navbar for dark theme */
    .navbar {
      background: rgba(11, 15, 25, 0.9) !important;
      border-bottom: 1px solid rgba(255,255,255,0.05) !important;
    }
    .navbar a:not(.btn) {
      color: #fff !important;
    }
    .dp-hero {
      padding: 120px 0 80px;
      text-align: center;
      position: relative;
    }
    .dp-hero h1 {
      font-size: clamp(3rem, 5vw, 4.5rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: -.03em;
      margin-bottom: 24px;
      line-height: 1.1;
    }
    .dp-hero p {
      font-size: 1.25rem;
      color: rgba(255, 255, 255, 0.6);
      max-width: 700px;
      margin: 0 auto 40px;
      line-height: 1.6;
    }
    .ads-section {
      padding: 60px 0 100px;
      background: #0b0f19;
    }
    .ads-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    .ad-card {
      background: #151a28;
      border: 1px solid rgba(255,255,255,0.05);
      border-radius: 16px;
      padding: 32px;
      transition: all 0.3s ease;
    }
    .ad-card:hover {
      border-color: rgba(168, 85, 247, 0.4);
      transform: translateY(-5px);
      box-shadow: 0 10px 30px rgba(168, 85, 247, 0.1);
    }
    .ad-icon {
      width: 48px;
      height: 48px;
      background: #1e2436;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 24px;
      font-size: 1.5rem;
    }
    .ad-card h3 {
      font-size: 1.3rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 12px;
    }
    .ad-card p {
      color: #94a3b8;
      line-height: 1.6;
      font-size: 0.95rem;
    }
    
    @media (max-width: 900px) {
      .ads-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .ads-grid { grid-template-columns: 1fr; }
    }
    .cta-banner {
      background: linear-gradient(135deg, #3b82f6, #8b5cf6, #ec4899);
      padding: 80px 0;
      text-align: center;
      color: #fff;
    }
    .cta-banner h2 { font-size: 3rem; font-weight: 800; margin-bottom: 24px; }
  </style>
"""
    head_and_nav = head_and_nav.replace('</head>', new_css + '\n</head>')

    new_body = """  <!-- Hero Section -->
  <section class="dp-hero">
    <div class="container">
      <div style="display:inline-block; padding: 6px 16px; background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 100px; color: #60a5fa; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Performance Marketing</div>
      <h1>High-Converting Ads<br>for Healthcare.</h1>
      <p>Stop wasting money on generic campaigns. We run highly targeted, data-driven advertising specifically designed for hospitals to acquire high-intent patients.</p>
      <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: #3b82f6; color: #fff; border-color: #3b82f6;">Launch Your Campaign</a>
    </div>
  </section>

  <!-- Ads Grid Section -->
  <section class="ads-section">
    <div class="container">
      <div class="ads-grid">
        <!-- 1 -->
        <div class="ad-card">
          <div class="ad-icon">🔍</div>
          <h3>Google Search Ads</h3>
          <p>Capture high-intent patients searching for "best cardiologist near me," "dental clinic in Chennai," and other medical queries.</p>
        </div>
        <!-- 2 -->
        <div class="ad-card">
          <div class="ad-icon">📸</div>
          <h3>Instagram &amp; Facebook Ads</h3>
          <p>Visually engaging carousel, video, and story ads targeting patients by age, location, interests, and health conditions.</p>
        </div>
        <!-- 3 -->
        <div class="ad-card">
          <div class="ad-icon">📺</div>
          <h3>YouTube Ads</h3>
          <p>Pre-roll and discovery ads showcasing doctor expertise, patient testimonials, and procedure explainers to build trust.</p>
        </div>
        <!-- 4 -->
        <div class="ad-card">
          <div class="ad-icon">🔄</div>
          <h3>Retargeting Campaigns</h3>
          <p>Re-engage website visitors who didn't book. Dynamic ads remind them of your services across the web and social media.</p>
        </div>
        <!-- 5 -->
        <div class="ad-card">
          <div class="ad-icon">📍</div>
          <h3>Local Service Ads</h3>
          <p>Google-guaranteed local service ads that put your practice at the very top — with verified badge, reviews, and click-to-call.</p>
        </div>
        <!-- 6 -->
        <div class="ad-card">
          <div class="ad-icon">📊</div>
          <h3>A/B Testing &amp; Optimization</h3>
          <p>Continuous ad creative testing, bidding strategy optimization, and audience refinement to maximize every rupee spent.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Banner -->
  <section class="cta-banner">
    <div class="container">
      <h2>Ready to scale your patient acquisitions?</h2>
      <p style="font-size: 1.2rem; margin-bottom: 32px; max-width: 600px; margin-left: auto; margin-right: auto;">Our performance marketing team guarantees the highest ROI on your ad spend.</p>
      <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: #fff; color: #8b5cf6; border-color: #fff;">Get a Free Audit</a>
    </div>
  </section>

  <!-- Footer -->
  <zeno-footer></zeno-footer>
  <script src="/js/components/footer.js"></script>

  <demo-modal></demo-modal>
  <script src="/js/components/demo-modal.js"></script>

  <script src="/js/app.js" defer></script>
</body>
</html>"""

    final_content = head_and_nav + new_body
    with open(adv_file, "w") as f:
        f.write(final_content)
        
    print(f"Created clean {adv_file}")

if __name__ == "__main__":
    recreate_adv()
