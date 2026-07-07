import os

def update_social_media_page():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/social-media/index.html"
    
    with open(file_path, "r") as f:
        content = f.read()

    parts = content.split('  <!-- Hero Section -->')
    if len(parts) < 2:
        print("Could not find <!-- Hero Section -->")
        return
        
    head_and_nav = parts[0]
    
    # We also need to inject some CSS into the <style> block inside head_and_nav
    # We can replace </style> with our new styles + </style>
    new_css = """
    .social-mockup {
      background: #fff;
      border-radius: 20px;
      padding: 16px;
      width: 320px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.2);
      border: 1px solid rgba(255,255,255,0.1);
      transform: rotate(2deg);
      position: relative;
    }
    .social-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }
    .social-avatar {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: linear-gradient(45deg, #f09433, #dc2743, #bc1888);
      padding: 2px;
    }
    .social-avatar img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: #fff;
      object-fit: cover;
    }
    .social-name {
      font-weight: 700;
      color: #111;
      font-size: 0.95rem;
    }
    .social-loc {
      font-size: 0.75rem;
      color: #666;
    }
    .social-image {
      width: 100%;
      height: 320px;
      border-radius: 12px;
      background: #f3f4f6;
      margin-bottom: 16px;
      position: relative;
      overflow: hidden;
    }
    .social-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .play-btn {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 50px;
      height: 50px;
      background: rgba(255,255,255,0.9);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .social-actions {
      display: flex;
      gap: 16px;
      margin-bottom: 12px;
      color: #111;
    }
    .social-caption {
      font-size: 0.9rem;
      color: #111;
      line-height: 1.4;
    }
    .social-caption span {
      color: #00376b;
    }
    .regional-fonts {
      font-size: 1.25rem;
      font-weight: 600;
      color: #a855f7;
      margin-top: 12px;
      letter-spacing: 0.05em;
    }
    .doctor-pull-section {
      padding: 100px 0;
      background: #fff;
    }
    .doctor-pull-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }
    .doctor-pull-content h2 {
      font-size: 2.5rem;
      font-weight: 800;
      color: #111;
      margin-bottom: 24px;
      line-height: 1.2;
    }
    .doctor-pull-content p {
      font-size: 1.15rem;
      color: #4b5563;
      line-height: 1.7;
      margin-bottom: 20px;
    }
    .stat-box {
      background: #fafafa;
      border-left: 4px solid #a855f7;
      padding: 24px;
      border-radius: 0 12px 12px 0;
      margin-top: 32px;
    }
    .stat-box h4 {
      font-size: 1.2rem;
      color: #111;
      margin-bottom: 8px;
    }
    .roi-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 60px;
      border-top: 1px solid #e5e7eb;
      padding-top: 60px;
    }
    .roi-card text-align: center;
    .roi-card h3 { font-size: 3rem; color: #a855f7; font-weight: 800; margin-bottom: 8px; }
    .roi-card p { font-size: 1.1rem; color: #4b5563; font-weight: 600; }
    
    @media (max-width: 900px) {
      .doctor-pull-grid { grid-template-columns: 1fr; }
      .roi-grid { grid-template-columns: 1fr; }
    }
    """
    
    # Clean up any previously injected css if we run this multiple times by replacing it purely in head_and_nav if it's not already there.
    # To be safe, we will just rely on the original script logic, but since we are replacing </style> we might duplicate if we run twice on the same file.
    # Since we are reading from the modified file, let's just do a multi-replace safely on a pristine file, or just use the current head_and_nav.
    # Actually, `head_and_nav` might already contain `.social-mockup`. Let's remove our old injected CSS to prevent duplication.
    if ".social-mockup" in head_and_nav:
        head_and_nav = head_and_nav.split(".social-mockup")[0] + "  </style>"
        
    head_and_nav = head_and_nav.replace('  </style>', new_css + '  </style>')

    new_body = """  <!-- Hero Section -->
  <section class="dp-hero">
    <div class="container" style="display: flex; align-items: center; justify-content: space-between; gap: 40px; text-align: left; flex-wrap: wrap;">
      <div style="flex: 1; min-width: 300px;">
        <div style="display:inline-block; padding: 6px 16px; background: rgba(168, 85, 247, 0.15); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 100px; color: #d8b4fe; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Social Media Growth Engine</div>
        <h1>Increase Patient Flow &<br>Spread Your Brand.</h1>
        <p>This page tells doctors and hospital founders the truth: consistent, high-quality social media content drastically increases patient footfall. We handle your content end-to-end, so your brand spreads locally and nationally.</p>
        <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: #fff; border: none; box-shadow: 0 4px 15px rgba(220, 39, 67, 0.4);">Grow Your Brand</a>
      </div>
      
      <div class="social-mockup">
        <div class="social-header">
          <div class="social-avatar">
            <img src="/images/zenohosp-logo.png" alt="Avatar" onerror="this.src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iI2NjYyI+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTAiLz48L3N2Zz4='">
          </div>
          <div>
            <div class="social-name">city_hospital_official</div>
            <div class="social-loc">Expert Cardiology Center</div>
          </div>
        </div>
        <div class="social-image">
          <div style="background: linear-gradient(135deg, #a855f7, #ec4899); width: 100%; height: 100%;"></div>
          <div class="play-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#111"><path d="M8 5v14l11-7z"></path></svg>
          </div>
        </div>
        <div class="social-actions">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
        </div>
        <div class="social-caption">
          <strong>city_hospital_official</strong> Learn the 3 signs of a healthy heart! ❤️ <span>#Cardiology #HealthTips #HospitalLife</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Doctor Pull Section (New) -->
  <section class="doctor-pull-section">
    <div class="container">
      <div class="doctor-pull-grid">
        <div class="doctor-pull-image" style="position: relative;">
          <!-- Using a generic placeholder for the doctor image with modern borders -->
          <div style="width: 100%; height: 500px; background: url('https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=800&q=80') center/cover; border-radius: 20px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);"></div>
          
          <!-- Floating UI card -->
          <div style="position: absolute; bottom: -20px; right: -20px; background: #fff; padding: 24px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); width: 250px; border: 1px solid #e5e7eb;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
              <div style="width: 12px; height: 12px; background: #10b981; border-radius: 50%;"></div>
              <strong style="color: #111; font-size: 1.1rem;">+45% New Patients</strong>
            </div>
            <p style="color: #6b7280; font-size: 0.9rem; margin:0;">From Instagram & YouTube in Month 1</p>
          </div>
        </div>
        
        <div class="doctor-pull-content">
          <div style="color: #a855f7; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 16px;">For Founders &amp; Chief Doctors</div>
          <h2>Stop Being the Best Kept Secret in Your City.</h2>
          <p>As a doctor, your primary focus is treating patients, not writing video scripts or figuring out Instagram algorithms. But today, if patients can't find your hospital's expertise online, they will go to the competitor who is visible.</p>
          <p>We position you and your senior doctors as <strong>Key Opinion Leaders (KOLs)</strong>. By producing highly professional, educational, and ethical medical content, we build immense trust in your community before the patient even walks through your hospital doors.</p>
          
          <div class="stat-box">
            <h4>Zero Hassle for Your Staff</h4>
            <p style="margin:0; font-size: 1rem;">You give us 2 hours a month. We bring the cameras, the lighting, the teleprompters, and the scripts. We shoot, edit, and post everything for the next 30 days. You just focus on medicine.</p>
          </div>
        </div>
      </div>
      
      <!-- ROI Grid -->
      <div class="roi-grid">
        <div class="roi-card" style="text-align: center;">
          <div style="background: rgba(168, 85, 247, 0.1); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; color: #a855f7;">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          </div>
          <h3>Brand Trust</h3>
          <p>Patients trust hospitals with faces. Video humanizes your doctors.</p>
        </div>
        <div class="roi-card" style="text-align: center;">
          <div style="background: rgba(168, 85, 247, 0.1); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; color: #a855f7;">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
          </div>
          <h3>Higher OPD</h3>
          <p>Educational Reels directly drive local patients to book consultations.</p>
        </div>
        <div class="roi-card" style="text-align: center;">
          <div style="background: rgba(168, 85, 247, 0.1); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; color: #a855f7;">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          </div>
          <h3>Top of Mind</h3>
          <p>Stay visible in your city so you're the first choice during emergencies.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Benefits Grid -->
  <section class="dp-sections" style="background: #fafafa;">
    <div class="container">
      <div style="text-align: center; margin-bottom: 60px;">
        <h2 style="font-size: 2.5rem; font-weight: 800; color: #111;">Custom Content for Maximum Impact</h2>
        <p style="color: #4b5563; font-size: 1.1rem; max-width: 600px; margin: 16px auto 0;">We do the research so you don't have to. Every piece of content is crafted specifically for your hospital.</p>
      </div>
      <div class="dp-grid">
        <div class="feature-card">
          <div class="feature-icon" style="background: rgba(236, 72, 153, 0.1); color: #ec4899;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
          </div>
          <h3>Location &amp; Specialization Focus</h3>
          <p>We analyze your local demographics and your hospital's top specialties to create highly relevant content that attracts patients from your exact catchment area.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon" style="background: rgba(14, 165, 233, 0.1); color: #0ea5e9;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <h3>Seasonal &amp; Medical R&amp;D</h3>
          <p>Our team conducts proper R&amp;D on seasonal health trends (e.g., flu season, summer heat strokes, monsoon dengue) to publish timely, educational content that patients are actively searching for.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon" style="background: rgba(168, 85, 247, 0.1); color: #a855f7;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14v-4z"></path><rect x="3" y="6" width="12" height="12" rx="2" ry="2"></rect></svg>
          </div>
          <h3>In-house Zesignworks Collaboration</h3>
          <p>We have an in-house team to write content, while our exclusive collaboration with <a href="https://www.zesignworks.com" target="_blank" style="color: #a855f7; text-decoration: underline;">Zesignworks</a> ensures cinematic video shoots and top-tier Reels/Shorts editing.</p>
        </div>
        <div class="feature-card" style="background: #faf5ff; border-color: #e9d5ff;">
          <div class="feature-icon" style="background: #f3e8ff; color: #9333ea;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
          </div>
          <h3>Regional Language Support</h3>
          <p>Speak to your patients in their mother tongue. We create high-quality multilingual captions, subtitles, and graphics in regional languages to maximize trust.</p>
          <div class="regional-fonts">தமிழ் &nbsp;&nbsp; हिन्दी &nbsp;&nbsp; తెలుగు &nbsp;&nbsp; മലയാളം</div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Banner -->
  <section class="cta-banner" style="background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);">
    <div class="container">
      <h2>Transform your doctors into thought leaders.</h2>
      <p>Partner with ZenoHosp &amp; Zesignworks to fill your waiting rooms through powerful social media.</p>
      <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: #fff; color: #dc2743; border-color: #fff;">Get a Content Strategy</a>
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

    # Combine everything
    final_content = head_and_nav + new_body
    
    with open(file_path, "w") as f:
        f.write(final_content)
        
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_social_media_page()
