import os
import re

def redesign_advertising():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/advertising/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    # Split into top (up to Hero Section) and bottom (scripts at the end)
    parts = content.split('<!-- Hero Section -->')
    if len(parts) < 2:
        print("Hero section not found")
        return
        
    top_html = parts[0]
    
    # Extract bottom html starting from <!-- Footer -->
    footer_idx = parts[1].find('<!-- Footer -->')
    if footer_idx == -1:
        print("Footer not found")
        return
    bottom_html = parts[1][footer_idx:]
    
    # We also need to replace the <style> block in top_html to include our new styles.
    style_regex = re.compile(r'<style>.*?</style>', re.DOTALL)
    
    new_style = """<style>
    :root {
      --ad-bg: #040814;
      --ad-card: #0a0f25;
      --ad-blue: #3b82f6;
      --ad-purple: #8b5cf6;
      --ad-pink: #ec4899;
      --glass-bg: rgba(10, 15, 37, 0.6);
      --glass-border: rgba(255, 255, 255, 0.05);
    }
    body {
      background-color: var(--ad-bg);
      color: #fff;
      overflow-x: hidden;
    }

    /* Hero Section */
    .ad-hero {
      padding: 160px 0 100px;
      position: relative;
    }
    .ad-hero::before {
      content: '';
      position: absolute;
      top: -20%;
      left: -10%;
      width: 70vw;
      height: 70vw;
      background: radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, transparent 60%);
      z-index: -1;
    }
    .ad-hero-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      background: rgba(59, 130, 246, 0.1);
      border: 1px solid rgba(59, 130, 246, 0.3);
      border-radius: 100px;
      color: #93c5fd;
      font-weight: 700;
      font-size: 0.85rem;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 24px;
    }
    .hero-badge span {
      width: 8px;
      height: 8px;
      background: #3b82f6;
      border-radius: 50%;
      box-shadow: 0 0 10px #3b82f6;
    }
    .ad-hero h1 {
      font-size: clamp(3.5rem, 5vw, 5rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: -.03em;
      margin-bottom: 24px;
      line-height: 1.1;
    }
    .text-gradient {
      background: linear-gradient(135deg, var(--ad-blue), var(--ad-purple), var(--ad-pink));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .ad-hero p {
      font-size: 1.25rem;
      color: #94a3b8;
      margin-bottom: 40px;
      line-height: 1.6;
      max-width: 500px;
    }

    /* Glass Mockup */
    .glass-dashboard {
      background: var(--glass-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--glass-border);
      border-radius: 24px;
      padding: 32px;
      box-shadow: 0 30px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
      position: relative;
      transform: perspective(1000px) rotateY(-5deg);
      transition: transform 0.5s ease;
    }
    .glass-dashboard:hover {
      transform: perspective(1000px) rotateY(0deg);
    }
    .dash-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px; }
    .dash-title { font-weight: 700; font-size: 1.2rem; }
    .dash-metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 32px; }
    .metric-card { background: rgba(255,255,255,0.03); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); }
    .metric-val { font-size: 2rem; font-weight: 800; color: #fff; margin-bottom: 4px; }
    .metric-val.green { color: #10b981; }
    .metric-label { font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; }
    
    .chart-bar { height: 8px; border-radius: 4px; background: rgba(255,255,255,0.1); margin-bottom: 12px; overflow: hidden; }
    .chart-fill { height: 100%; background: linear-gradient(90deg, var(--ad-blue), var(--ad-purple)); width: 75%; border-radius: 4px; }
    .chart-fill.secondary { background: linear-gradient(90deg, var(--ad-pink), var(--ad-purple)); width: 45%; }

    /* Ads Grid Section */
    .ads-section {
      padding: 100px 0;
      position: relative;
      border-top: 1px solid var(--glass-border);
    }
    .section-title {
      text-align: center;
      margin-bottom: 60px;
    }
    .section-title h2 { font-size: 3rem; font-weight: 800; margin-bottom: 16px; }
    .section-title p { font-size: 1.15rem; color: #94a3b8; max-width: 600px; margin: 0 auto; }
    
    .ads-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 32px;
    }
    .ad-card {
      background: var(--ad-card);
      border: 1px solid var(--glass-border);
      border-radius: 20px;
      padding: 40px;
      position: relative;
      overflow: hidden;
      transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .ad-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: radial-gradient(circle at top right, rgba(139, 92, 246, 0.1), transparent 50%);
      opacity: 0;
      transition: opacity 0.4s ease;
    }
    .ad-card:hover {
      transform: translateY(-10px);
      border-color: rgba(139, 92, 246, 0.3);
      box-shadow: 0 20px 40px rgba(0,0,0,0.3), 0 0 20px rgba(139, 92, 246, 0.1);
    }
    .ad-card:hover::before { opacity: 1; }
    .ad-icon {
      width: 60px;
      height: 60px;
      background: rgba(255,255,255,0.03);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 24px;
      color: var(--ad-blue);
      transition: transform 0.3s ease;
    }
    .ad-card:hover .ad-icon {
      transform: scale(1.1) rotate(5deg);
      color: var(--ad-purple);
      background: rgba(139, 92, 246, 0.1);
      border-color: rgba(139, 92, 246, 0.3);
    }
    .ad-card h3 { font-size: 1.4rem; font-weight: 700; color: #fff; margin-bottom: 12px; position: relative; }
    .ad-card p { color: #94a3b8; line-height: 1.6; position: relative; }

    /* Pain Points */
    .pain-point-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
    .pain-card { 
      background: rgba(239, 68, 68, 0.03); 
      border: 1px solid rgba(239, 68, 68, 0.1); 
      padding: 40px; 
      border-radius: 20px; 
      border-top: 4px solid #ef4444; 
      backdrop-filter: blur(10px);
    }
    .pain-card h3 { font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 16px; }
    .pain-card p { color: #94a3b8; line-height: 1.6; }

    /* FAQ Accordion */
    .faq-container { max-width: 800px; margin: 0 auto; }
    details {
      background: var(--ad-card);
      border: 1px solid var(--glass-border);
      border-radius: 16px;
      margin-bottom: 16px;
      overflow: hidden;
      transition: border-color 0.3s ease;
    }
    details:hover { border-color: rgba(139, 92, 246, 0.3); }
    summary {
      padding: 24px;
      font-size: 1.2rem;
      font-weight: 700;
      color: #fff;
      cursor: pointer;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    summary::-webkit-details-marker { display: none; }
    summary::after {
      content: '+';
      font-size: 1.5rem;
      color: var(--ad-purple);
      transition: transform 0.3s ease;
    }
    details[open] summary::after { transform: rotate(45deg); }
    .faq-content {
      padding: 0 24px 24px;
      color: #94a3b8;
      line-height: 1.7;
    }

    .cta-banner {
      background: linear-gradient(135deg, var(--ad-blue), var(--ad-purple), var(--ad-pink));
      padding: 100px 0;
      text-align: center;
      color: #fff;
      position: relative;
      overflow: hidden;
    }
    .cta-banner h2 { font-size: 3.5rem; font-weight: 800; margin-bottom: 24px; }
    .cta-banner p { font-size: 1.25rem; margin-bottom: 40px; color: rgba(255,255,255,0.9); }
    .cta-banner .btn { background: #fff; color: var(--ad-purple); border: none; padding: 16px 40px; font-size: 1.1rem; font-weight: 700; border-radius: 100px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: transform 0.3s ease; }
    .cta-banner .btn:hover { transform: scale(1.05); }

    @media (max-width: 1024px) {
      .ad-hero-grid { grid-template-columns: 1fr; text-align: center; }
      .ad-hero p { margin: 0 auto 40px; }
      .ads-grid, .pain-point-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px) {
      .ads-grid, .pain-point-grid { grid-template-columns: 1fr; }
      .ad-hero h1 { font-size: 3rem; }
    }
  </style>"""
    
    top_html = style_regex.sub(new_style, top_html)

    new_html = """
  <!-- Hero Section -->
  <section class="ad-hero">
    <div class="container">
      <div class="ad-hero-grid">
        <div>
          <div class="hero-badge"><span></span> Healthcare Performance Marketing</div>
          <h1>High-Converting <br><span class="text-gradient">Medical Ads.</span></h1>
          <p>Stop wasting money on generic campaigns. We run highly targeted, data-driven advertising specifically designed for hospitals to acquire high-intent patients and lower acquisition costs.</p>
          <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: linear-gradient(90deg, #3b82f6, #8b5cf6); border: none; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.3);">Launch Your Campaign</a>
        </div>
        
        <div class="glass-dashboard">
          <div class="dash-header">
            <div class="dash-title">Campaign Performance</div>
            <div style="background: rgba(16,185,129,0.1); color: #10b981; padding: 4px 12px; border-radius: 100px; font-size: 0.8rem; font-weight: 700;">LIVE</div>
          </div>
          <div class="dash-metrics">
            <div class="metric-card">
              <div class="metric-val">+342</div>
              <div class="metric-label">OPD Walk-ins</div>
            </div>
            <div class="metric-card">
              <div class="metric-val green">-45%</div>
              <div class="metric-label">Patient CAC</div>
            </div>
          </div>
          <div>
            <div class="metric-label" style="margin-bottom: 12px;">Search Ads Traffic</div>
            <div class="chart-bar"><div class="chart-fill"></div></div>
            <div class="metric-label" style="margin-bottom: 12px; margin-top: 24px;">Meta Ads Retargeting</div>
            <div class="chart-bar"><div class="chart-fill secondary"></div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Ads Grid Section -->
  <section class="ads-section">
    <div class="container">
      <div class="section-title">
        <h2>Targeted Acquisition Channels</h2>
        <p>We deploy omni-channel strategies ensuring your hospital appears exactly when and where patients are searching for care.</p>
      </div>
      <div class="ads-grid">
        <!-- 1 -->
        <div class="ad-card">
          <div class="ad-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
          <h3>Google Search Ads</h3>
          <p>Capture high-intent patients searching for "best cardiologist near me," "dental clinic in Chennai," and other medical queries.</p>
        </div>
        <!-- 2 -->
        <div class="ad-card">
          <div class="ad-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></div>
          <h3>Meta (FB/IG) Ads</h3>
          <p>Visually engaging carousel, video, and story ads targeting patients by age, location, interests, and health conditions.</p>
        </div>
        <!-- 3 -->
        <div class="ad-card">
          <div class="ad-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg></div>
          <h3>YouTube Ads</h3>
          <p>Pre-roll and discovery ads showcasing doctor expertise, patient testimonials, and procedure explainers to build trust.</p>
        </div>
        <!-- 4 -->
        <div class="ad-card">
          <div class="ad-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M2.13 15.57a10 10 0 1 0 5.66-11.45l-4.14 4.14"></path></svg></div>
          <h3>Retargeting Campaigns</h3>
          <p>Re-engage website visitors who didn't book. Dynamic ads remind them of your services across the web and social media.</p>
        </div>
        <!-- 5 -->
        <div class="ad-card">
          <div class="ad-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg></div>
          <h3>Local Service Ads</h3>
          <p>Google-guaranteed local service ads that put your practice at the very top — with verified badge, reviews, and click-to-call.</p>
        </div>
        <!-- 6 -->
        <div class="ad-card">
          <div class="ad-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>
          <h3>A/B Testing & Optimization</h3>
          <p>Continuous ad creative testing, bidding strategy optimization, and audience refinement to maximize every rupee spent.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Pain Points Section -->
  <section class="ads-section" style="background: rgba(255,255,255,0.01);">
    <div class="container">
      <div class="section-title">
        <h2>The Cost of Empty OPDs</h2>
        <p>Hospitals lose lakhs in potential revenue every month because patients simply do not know they exist when an emergency strikes.</p>
      </div>
      <div class="pain-point-grid">
        <div class="pain-card">
          <h3>High Patient Acquisition Costs</h3>
          <p>Running ads without specialized healthcare tracking leads to massive budget wastage. We optimize your campaigns to drop your CAC (Customer Acquisition Cost) drastically.</p>
        </div>
        <div class="pain-card">
          <h3>Ad Account Suspensions</h3>
          <p>Google and Facebook have extreme restrictions on medical ads. If you aren't using a certified healthcare agency, your ad account is constantly at risk of permanent bans.</p>
        </div>
        <div class="pain-card">
          <h3>Zero Lead Quality Control</h3>
          <p>Getting 100 calls means nothing if none of them actually book a consultation. Our targeting strategies filter out junk leads, ensuring your reception only speaks to high-intent patients.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="ads-section">
    <div class="container">
      <div class="section-title">
        <h2>Frequently Asked Questions</h2>
        <p>Common questions hospital founders have about our healthcare advertising services.</p>
      </div>
      <div class="faq-container">
        <details open>
          <summary>What is the expected ROI for hospital advertising?</summary>
          <div class="faq-content">
            ROI depends on the specialty and location, but our targeted Google and Facebook ad campaigns typically reduce Patient Acquisition Costs (CAC) by 30-50% while driving immediate high-intent OPD walk-ins. We focus on high-margin procedures to maximize your returns.
          </div>
        </details>
        <details>
          <summary>How do you handle strict Google healthcare ad policies?</summary>
          <div class="faq-content">
            Healthcare advertising policies are notoriously strict. Our certified ad specialists know exactly how to structure landing pages and ad copy to ensure 100% compliance, preventing your ad accounts from getting suspended while still delivering compelling messages.
          </div>
        </details>
        <details>
          <summary>Do you guarantee patient footfall?</summary>
          <div class="faq-content">
            While we cannot legally guarantee specific medical outcomes, our performance marketing strategies guarantee highly targeted impressions and clicks from patients actively searching for your specific treatments in your precise locality. We measure success by actual appointments booked.
          </div>
        </details>
      </div>
    </div>
  </section>

  <!-- CTA Banner -->
  <section class="cta-section cta-banner">
    <div class="container">
      <h2>Ready to Dominate Local Searches?</h2>
      <p>Partner with the only digital agency built exclusively for Indian hospitals.</p>
      <a href="/contact-us/index.html" class="btn">Get a Free Marketing Audit</a>
    </div>
  </section>

"""
    
    final_content = top_html + new_html + bottom_html
    
    with open(file_path, 'w') as f:
        f.write(final_content)
    print("Redesigned Advertising UI")

if __name__ == "__main__":
    redesign_advertising()
