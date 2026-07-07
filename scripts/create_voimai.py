import os

def create_voimai_page():
    base_dir = "/Users/iniyananbu/Documents/ZenoHosp Website"
    voimai_file = os.path.join(base_dir, "services/voimai/index.html")
    index_file = os.path.join(base_dir, "index.html")
    
    with open(index_file, "r") as f:
        index_content = f.read()
        
    start_str = '<!DOCTYPE html>'
    end_str = '  <!-- Hero Section -->'
    head_and_nav = index_content.split(end_str)[0]
    
    # Update title and meta
    title_start = '<title>'
    title_end = '</title>'
    head_and_nav = head_and_nav.replace(
        head_and_nav[head_and_nav.find(title_start):head_and_nav.find(title_end)+len(title_end)],
        '<title>Voim.ai | Healthcare AI Voice Agent by ZenoHosp</title>'
    )
    
    parts = head_and_nav.split('<meta name="description" content="')
    if len(parts) > 1:
        rest = parts[1].split('">', 1)
        head_and_nav = parts[0] + '<meta name="description" content="Voim.ai is an advanced AI Voice Agent for hospitals that handles 1000 calls simultaneously for appointments, follow-ups, and more. Powered by Zesignworks.">' + rest[1]

    # Inject Voim.ai link into desktop dropdown of head_and_nav
    desktop_search = '<span>Google, FB & YouTube Ads</span>\n                </div>\n              </a>'
    desktop_insert = """
              <a href="/services/voimai/index.html" class="dropdown-item">
                <div class="dropdown-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px;">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20">
                    <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path>
                    <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
                    <line x1="12" y1="19" x2="12" y2="23"></line>
                    <line x1="8" y1="23" x2="16" y2="23"></line>
                  </svg>
                </div>
                <div class="dropdown-info">
                  <strong>Voim.ai Agent</strong>
                  <span>AI Voice Caller & Scheduler</span>
                </div>
              </a>"""
    if desktop_search in head_and_nav:
        head_and_nav = head_and_nav.replace(desktop_search, desktop_search + desktop_insert)
    
    # Inject Voim.ai into mobile nav
    mobile_search = '<a href="/services/advertising/index.html">Advertising</a>'
    mobile_insert = '\n          <a href="/services/voimai/index.html">Voim.ai</a>'
    if mobile_search in head_and_nav:
        head_and_nav = head_and_nav.replace(mobile_search, mobile_search + mobile_insert)

    # CSS for Voimai page
    new_css = """
  <style>
    body {
      background-color: #050a12;
      color: #fff;
    }
    .navbar {
      background: rgba(5, 10, 18, 0.9) !important;
      border-bottom: 1px solid rgba(255,255,255,0.05) !important;
    }
    .navbar a:not(.btn) {
      color: #fff !important;
    }
    .voim-hero {
      padding: 120px 0 80px;
      text-align: center;
      position: relative;
      background: radial-gradient(circle at center, rgba(16, 185, 129, 0.15) 0%, transparent 60%);
    }
    .voim-hero h1 {
      font-size: clamp(3rem, 5vw, 4.5rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: -.03em;
      margin-bottom: 24px;
      line-height: 1.1;
    }
    .voim-hero h1 span {
      background: linear-gradient(135deg, #10b981, #3b82f6);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .voim-hero p {
      font-size: 1.25rem;
      color: rgba(255, 255, 255, 0.7);
      max-width: 700px;
      margin: 0 auto 40px;
      line-height: 1.6;
    }
    .voim-features {
      padding: 60px 0 100px;
      background: #050a12;
    }
    .voim-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 32px;
    }
    .v-card {
      background: #0f1623;
      border: 1px solid rgba(16, 185, 129, 0.1);
      border-radius: 16px;
      padding: 40px;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
    }
    .v-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 100%; height: 4px;
      background: linear-gradient(90deg, #10b981, #3b82f6);
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .v-card:hover::before { opacity: 1; }
    .v-icon {
      width: 56px;
      height: 56px;
      background: rgba(16, 185, 129, 0.1);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 24px;
      color: #10b981;
    }
    .v-card h3 {
      font-size: 1.4rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 16px;
    }
    .v-card p {
      color: #94a3b8;
      line-height: 1.6;
      font-size: 1.05rem;
    }
    .voim-stats {
      background: #0f1623;
      border-top: 1px solid rgba(255,255,255,0.05);
      border-bottom: 1px solid rgba(255,255,255,0.05);
      padding: 60px 0;
    }
    .stats-container {
      display: flex;
      justify-content: space-around;
      text-align: center;
      flex-wrap: wrap;
      gap: 32px;
    }
    .stat-item h4 {
      font-size: 3rem;
      font-weight: 800;
      color: #fff;
      margin-bottom: 8px;
    }
    .stat-item p {
      font-size: 1.1rem;
      color: #10b981;
      font-weight: 600;
    }
    .cta-banner {
      background: linear-gradient(135deg, #10b981, #059669, #047857);
      padding: 80px 0;
      text-align: center;
      color: #fff;
    }
    .cta-banner h2 { font-size: 3rem; font-weight: 800; margin-bottom: 24px; }
    @media (max-width: 768px) {
      .voim-grid { grid-template-columns: 1fr; }
    }
  </style>
"""
    head_and_nav = head_and_nav.replace('</head>', new_css + '\n</head>')

    new_body = """  <!-- Hero Section -->
  <section class="voim-hero">
    <div class="container">
      <div style="display:inline-block; padding: 6px 16px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 100px; color: #10b981; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Powered by Zesignworks</div>
      <h1>Meet <span>Voim.ai</span></h1>
      <p>The ultimate AI Voice Agent for hospitals. Seamlessly handle incoming inquiries, automate appointment bookings, and conduct proactive post-treatment follow-up calls without adding a single human to your payroll.</p>
      <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: #10b981; color: #fff; border-color: #10b981; font-weight: 700;">Deploy Voim.ai Today</a>
    </div>
  </section>

  <!-- Stats Section -->
  <section class="voim-stats">
    <div class="container stats-container">
      <div class="stat-item">
        <h4>1000+</h4>
        <p>Simultaneous Calls</p>
      </div>
      <div class="stat-item">
        <h4>400+</h4>
        <p>Regional Languages</p>
      </div>
      <div class="stat-item">
        <h4>100%</h4>
        <p>HIPAA/Data Compliant</p>
      </div>
    </div>
  </section>

  <!-- Features Grid Section -->
  <section class="voim-features">
    <div class="container">
      <div style="text-align: center; margin-bottom: 60px;">
        <h2 style="font-size: 2.5rem; font-weight: 800; color: #fff;">Automate Your Telephony Operations</h2>
      </div>
      <div class="voim-grid">
        <div class="v-card">
          <div class="v-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          </div>
          <h3>Incoming &amp; Outgoing Agent</h3>
          <p>Voim.ai operates in both directions. It can receive hundreds of incoming calls for general inquiries, while simultaneously dialing out to existing patients for crucial post-treatment checkups.</p>
        </div>
        <div class="v-card">
          <div class="v-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          </div>
          <h3>Appointment &amp; Follow-up Master</h3>
          <p>Never miss a patient follow-up again. Voim.ai actively calls patients to check on their recovery, answers their basic health questions, and seamlessly books their next consultation into your HMS.</p>
        </div>
        <div class="v-card">
          <div class="v-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M2 12h20"></path><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
          </div>
          <h3>400+ Regional Languages</h3>
          <p>Healthcare is local. Voim.ai speaks directly to your patients in their native mother tongue with a natural accent, establishing immense trust and ensuring they clearly understand instructions.</p>
        </div>
        <div class="v-card">
          <div class="v-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"></path></svg>
          </div>
          <h3>Strict Data Privacy &amp; Auto-Delete</h3>
          <p>We prioritize patient confidentiality. All calls are securely recorded for quality analysis and are automatically purged from our servers after 30 days to strictly adhere to data protection regulations.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Banner -->
  <section class="cta-banner">
    <div class="container">
      <h2>Transform Your Front Desk Operations</h2>
      <p style="font-size: 1.2rem; margin-bottom: 32px; max-width: 600px; margin-left: auto; margin-right: auto;">Never let a patient call go to voicemail again. Implement Voim.ai and scale your patient engagement infinitely.</p>
      <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: #fff; color: #10b981; border-color: #fff; font-weight: 700;">Listen to a Demo Call</a>
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
    with open(voimai_file, "w") as f:
        f.write(final_content)
        
    print(f"Created {voimai_file}")

if __name__ == "__main__":
    create_voimai_page()
