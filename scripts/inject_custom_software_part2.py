import os

def update_custom_software_part2():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/custom-software/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    new_css = """
    /* What We Build Section */
    .portfolio-section {
      padding: 100px 0;
      background: #fff;
    }
    .portfolio-header {
      text-align: center;
      margin-bottom: 60px;
    }
    .portfolio-header h2 {
      font-size: 2.5rem;
      font-weight: 800;
      color: #111;
      margin-bottom: 16px;
    }
    .portfolio-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 40px;
    }
    .portfolio-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      overflow: hidden;
      transition: transform 0.3s;
    }
    .portfolio-card:hover {
      transform: translateY(-8px);
    }
    .portfolio-img {
      height: 240px;
      background: #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 4rem;
      color: #cbd5e1;
      position: relative;
    }
    .portfolio-img.patient { background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: rgba(255,255,255,0.3); }
    .portfolio-img.teleicu { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); color: rgba(255,255,255,0.3); }
    .portfolio-img.pharma { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: rgba(255,255,255,0.3); }
    .portfolio-img.triage { background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); color: rgba(255,255,255,0.3); }
    .portfolio-content {
      padding: 32px;
    }
    .portfolio-content h3 {
      font-size: 1.5rem;
      font-weight: 700;
      color: #111;
      margin-bottom: 12px;
    }
    .portfolio-content p {
      color: #4b5563;
      line-height: 1.6;
    }

    /* Security Architecture Section */
    .security-section {
      padding: 100px 0;
      background: #040814;
      color: #fff;
      position: relative;
      overflow: hidden;
    }
    .security-section::after {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: radial-gradient(circle at 50% -20%, rgba(16, 185, 129, 0.15), transparent 70%);
      pointer-events: none;
    }
    .security-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }
    .sec-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: 100px;
      color: #10b981;
      font-weight: 700;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 24px;
    }
    .security-content h2 {
      font-size: 2.8rem;
      font-weight: 800;
      margin-bottom: 24px;
      line-height: 1.1;
    }
    .security-features {
      margin-top: 40px;
      display: grid;
      gap: 24px;
    }
    .sec-feature {
      display: flex;
      gap: 16px;
    }
    .sec-icon {
      width: 40px; height: 40px;
      background: rgba(255,255,255,0.05);
      border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      color: #10b981;
      flex-shrink: 0;
    }
    .sec-text h4 { font-size: 1.1rem; font-weight: 700; margin-bottom: 4px; }
    .sec-text p { color: #94a3b8; font-size: 0.95rem; line-height: 1.5; }

    /* Tech Stack Section */
    .stack-section {
      padding: 80px 0;
      background: #fafafa;
      border-top: 1px solid #eaeaea;
    }
    .stack-header { text-align: center; margin-bottom: 40px; }
    .stack-header h3 { font-size: 1.5rem; font-weight: 700; color: #111; }
    .stack-marquee {
      display: flex;
      gap: 40px;
      justify-content: center;
      flex-wrap: wrap;
      align-items: center;
      opacity: 0.7;
    }
    .stack-item {
      font-size: 1.2rem;
      font-weight: 800;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    @media (max-width: 900px) {
      .portfolio-grid, .security-grid { grid-template-columns: 1fr; }
    }
"""
    
    # Inject CSS
    content = content.replace("</style>", new_css + "\n  </style>")

    html_portfolio = """
  <!-- What We Build Section -->
  <section class="portfolio-section">
    <div class="container">
      <div class="portfolio-header">
        <h2>Custom Software Ecosystems</h2>
        <p style="color: #64748b; font-size: 1.15rem; max-width: 700px; margin: 0 auto;">We don't just build apps; we engineer comprehensive healthcare ecosystems. Here are a few examples of what we can develop for you.</p>
      </div>
      <div class="portfolio-grid">
        <div class="portfolio-card">
          <div class="portfolio-img patient"><svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg></div>
          <div class="portfolio-content">
            <h3>White-Label Patient Apps</h3>
            <p>Premium iOS and Android applications allowing your patients to book appointments, view lab reports, access telemedicine, and securely message doctors, all under your own hospital brand.</p>
          </div>
        </div>
        <div class="portfolio-card">
          <div class="portfolio-img teleicu"><svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line><polyline points="4 10 8 10 10 14 14 6 16 10 20 10"></polyline></svg></div>
          <div class="portfolio-content">
            <h3>TeleICU & Remote Monitoring</h3>
            <p>Real-time clinical dashboards that integrate directly with IoT medical devices and bedside monitors, allowing your top intensivists to monitor multiple critical patients remotely.</p>
          </div>
        </div>
        <div class="portfolio-card">
          <div class="portfolio-img pharma"><svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
          <div class="portfolio-content">
            <h3>Custom Pharmacy ERPs</h3>
            <p>Scalable inventory and supply chain management software built for large multi-branch hospital pharmacies. Features automated expiry alerts, vendor integrations, and predictive restocking.</p>
          </div>
        </div>
        <div class="portfolio-card">
          <div class="portfolio-img triage"><svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="12 2 22 8.5 22 15.5 12 22 2 15.5 2 8.5 12 2"></polygon><line x1="12" y1="22" x2="12" y2="15.5"></line><polyline points="22 8.5 12 15.5 2 8.5"></polyline><polyline points="2 15.5 12 8.5 22 15.5"></polyline><line x1="12" y1="2" x2="12" y2="8.5"></line></svg></div>
          <div class="portfolio-content">
            <h3>AI-Driven Triage Systems</h3>
            <p>Smart, algorithm-based patient flow optimization modules that automatically categorize Emergency Department arrivals based on clinical severity scores, reducing wait times and saving lives.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

    html_security = """
  <!-- Enterprise Security Section -->
  <section class="security-section">
    <div class="container">
      <div class="security-grid">
        <div class="security-content">
          <div class="sec-badge"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0110 0v4"></path></svg> Enterprise-Grade Security</div>
          <h2>Your Patient Data is Bulletproof.</h2>
          <p style="color: #94a3b8; font-size: 1.15rem; line-height: 1.6;">We don't take chances with PHI (Protected Health Information). Our custom architectures are deployed with banking-level security protocols that protect your hospital from ransomware, breaches, and data loss.</p>
          
          <div class="security-features">
            <div class="sec-feature">
              <div class="sec-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
              <div class="sec-text">
                <h4>Zero-Trust Architecture</h4>
                <p>Every internal and external access request is heavily authenticated and authorized dynamically. No default trust.</p>
              </div>
            </div>
            <div class="sec-feature">
              <div class="sec-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0110 0v4"></path></svg></div>
              <div class="sec-text">
                <h4>AES-256 Data Encryption</h4>
                <p>All databases and transit layers are encrypted using military-grade AES-256, ensuring data is unreadable if intercepted.</p>
              </div>
            </div>
            <div class="sec-feature">
              <div class="sec-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"></path></svg></div>
              <div class="sec-text">
                <h4>Automated Threat Detection</h4>
                <p>We deploy WAFs (Web Application Firewalls) and DDoS protection to actively monitor and block malicious traffic in real-time.</p>
              </div>
            </div>
          </div>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 32px; position: relative;">
          <div style="font-family: monospace; color: #10b981; font-size: 0.9rem; line-height: 1.8;">
            > Initiating Secure Connection...<br>
            > [SUCCESS] SSL Handshake Verified<br>
            > Encrypting Payload (AES-256)...<br>
            > [SUCCESS] Data Encrypted<br>
            > Pushing to Secure AWS HealthLake...<br>
            > [SUCCESS] Stored securely.<br>
            <br>
            <span style="color: #64748b;">// Automated daily cloud backups active</span><br>
            <span style="color: #64748b;">// Intrusion detection systems online</span><br>
            <span style="color: #64748b;">// 99.99% Uptime SLA guaranteed</span>
          </div>
        </div>
      </div>
    </div>
  </section>
  
  <!-- Tech Stack Section -->
  <section class="stack-section">
    <div class="container">
      <div class="stack-header">
        <h3>Powered by Modern Cloud Infrastructure</h3>
      </div>
      <div class="stack-marquee">
        <span class="stack-item">React & Next.js</span>
        <span class="stack-item">Node.js</span>
        <span class="stack-item">Python AI</span>
        <span class="stack-item">AWS Healthcare</span>
        <span class="stack-item">Google Cloud</span>
        <span class="stack-item">Kubernetes</span>
        <span class="stack-item">PostgreSQL</span>
      </div>
    </div>
  </section>
"""

    # Inject Portfolio before <!-- How We Manage Flow -->
    parts = content.split("<!-- How We Manage Flow -->")
    if len(parts) == 2:
        content = parts[0] + html_portfolio + "\n  <!-- How We Manage Flow -->" + parts[1]
    
    # Inject Security and Stack before <!-- CTA Banner -->
    parts = content.split("<!-- CTA Banner -->")
    if len(parts) == 2:
        content = parts[0] + html_security + "\n  <!-- CTA Banner -->" + parts[1]

    with open(file_path, 'w') as f:
        f.write(content)
    print("Injected part 2 sections successfully.")

if __name__ == "__main__":
    update_custom_software_part2()
