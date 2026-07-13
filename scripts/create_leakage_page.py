import os

output_file = './solutions/stop-revenue-leakage/index.html'
os.makedirs(os.path.dirname(output_file), exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-27WDP0T7BZ"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-27WDP0T7BZ');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Discover how ZenoHosp plugs revenue, inventory, and data leaks in your hospital. Recover lost billings, stop pharmacy pilferage, and secure patient data.">
  <meta name="keywords" content="Hospital Revenue Leakage, Stop Inventory Pilferage, Hospital Data Security, ZenoHosp">

  <link rel="icon" type="image/svg+xml" href="/images/favicon.svg">
  <link rel="canonical" href="https://zenohosp.com/solutions/stop-revenue-leakage/">

  <title>Stop Revenue, Inventory & Data Leakage | ZenoHosp</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/css/main.css">
  <link rel="stylesheet" href="/css/pages/solutions.css">

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Stop Revenue, Inventory & Data Leakage | ZenoHosp",
    "description": "Discover how ZenoHosp plugs revenue, inventory, and data leaks in your hospital.",
    "url": "https://zenohosp.com/solutions/stop-revenue-leakage/"
  }
  </script>
  <meta name="theme-color" content="#111827">

  <style>
    .leakage-hero {
      background: #0a0a08;
      padding: 100px 0 80px;
      position: relative;
      overflow: hidden;
      text-align: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .leakage-bg-glow {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: radial-gradient(ellipse at 50% 50%, rgba(209, 244, 112, 0.06) 0%, transparent 65%);
      pointer-events: none;
    }
    .leakage-hero h1 {
      font-size: clamp(3rem, 5vw, 4.5rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: -.03em;
      margin-bottom: 24px;
      line-height: 1.1;
    }
    .leakage-hero p {
      font-size: 1.25rem;
      color: rgba(255, 255, 255, 0.6);
      max-width: 700px;
      margin: 0 auto 40px;
      line-height: 1.6;
    }
    .leakage-section {
      padding: 100px 0;
      background: #fafafa;
    }
    .leakage-section.dark {
      background: #11110d;
      color: #fff;
    }
    .leakage-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }
    .leakage-grid.reverse .leakage-content {
      order: 2;
    }
    .leakage-grid.reverse .leakage-visual {
      order: 1;
    }
    @media (max-width: 900px) {
      .leakage-grid { grid-template-columns: 1fr; gap: 40px; }
      .leakage-grid.reverse .leakage-content, .leakage-grid.reverse .leakage-visual { order: initial; }
    }
    .leakage-label {
      display: inline-block;
      padding: 6px 14px;
      border-radius: 100px;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 20px;
    }
    .label-red { background: rgba(239, 68, 68, 0.1); color: #ef4444; }
    .label-blue { background: rgba(59, 130, 246, 0.1); color: #3b82f6; }
    .label-green { background: rgba(16, 185, 129, 0.1); color: #10b981; }
    
    .leakage-content h2 {
      font-size: 2.5rem;
      font-weight: 700;
      margin-bottom: 24px;
      letter-spacing: -0.02em;
    }
    .leakage-content p {
      font-size: 1.1rem;
      line-height: 1.7;
      margin-bottom: 30px;
      color: #4b5563;
    }
    .dark .leakage-content p { color: rgba(255, 255, 255, 0.7); }
    
    .example-box {
      background: #fff;
      border: 1px solid #e5e7eb;
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 20px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .dark .example-box {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .example-box h4 {
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .example-box p {
      margin-bottom: 0;
      font-size: 0.95rem;
    }
    .leakage-visual {
      background: #f3f4f6;
      border-radius: 20px;
      height: 400px;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      position: relative;
    }
    .dark .leakage-visual {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .cta-banner {
      background: #d1f470;
      padding: 80px 0;
      text-align: center;
      color: #11110d;
    }
    .cta-banner h2 {
      font-size: 3rem;
      font-weight: 800;
      margin-bottom: 24px;
      letter-spacing: -0.03em;
    }
    .cta-banner p {
      font-size: 1.2rem;
      max-width: 600px;
      margin: 0 auto 40px;
      font-weight: 500;
    }
  </style>
</head>
<body>

  <!-- Navbar -->
  <nav class="navbar marketing-navbar" id="main-nav">
    <div class="nav-container">
      <a href="/index.html" class="logo">
        <span class="logo-icon">Z</span>
        <span class="logo-text">Zeno<span class="logo-accent">Hosp</span></span>
      </a>
      <ul class="nav-links">
        <li><a href="/solutions/index.html">Solutions</a></li>
        <li><a href="/pricing/index.html">Pricing</a></li>
        <li><a href="/contact-us/index.html">Contact Us</a></li>
      </ul>
      <div class="nav-actions">
        <a href="https://hms.zenohosp.com" class="signin">Sign In</a>
        <a href="/contact-us/index.html" class="btn btn-primary">Request Demo</a>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="leakage-hero">
    <div class="leakage-bg-glow"></div>
    <div class="container">
      <h1>Plug the leaks in your <br>hospital's operations.</h1>
      <p>Hospitals lose up to 15% of their revenue through unbilled procedures, pharmacy expiry, and operational inefficiencies. Here is exactly how ZenoHosp recovers it.</p>
      <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: #d1f470; color: #111; border-color: #d1f470;">Book a Demo</a>
    </div>
  </section>

  <!-- Section 1: Financial & Billing Leakage -->
  <section class="leakage-section">
    <div class="container">
      <div class="leakage-grid">
        <div class="leakage-content">
          <span class="leakage-label label-red">Financial Leakage</span>
          <h2>Never miss a billable charge again.</h2>
          <p>When doctors, nurses, and billing operate in silos, services get delivered but not billed. ZenoHosp connects every clinical action directly to the patient's folio.</p>
          
          <div class="example-box">
            <h4><span style="color:#ef4444">✕</span> The IPD Round Leak</h4>
            <p><strong>The Problem:</strong> A specialist completes 15 IPD rounds, but the ward nurse forgets to manually add the ₹1,000 consult fee to the billing sheet.</p>
            <p style="margin-top:12px"><strong>The ZenoHosp Solution:</strong> The doctor logs the round on the ZenoHosp Mobile App at the bedside. The fee is instantly auto-posted to the live bill.</p>
          </div>

          <div class="example-box">
            <h4><span style="color:#ef4444">✕</span> The Unbilled Consumables</h4>
            <p><strong>The Problem:</strong> OT nurses grab extra sutures and gloves during an emergency but forget to record them. The hospital pays for the stock, but the patient is never billed.</p>
            <p style="margin-top:12px"><strong>The ZenoHosp Solution:</strong> Scanning items in the OT automatically deducts them from Inventory and adds them to the surgical bill simultaneously.</p>
          </div>

          <div class="example-box">
            <h4><span style="color:#ef4444">✕</span> The Siloed Software Gap</h4>
            <p><strong>The Problem:</strong> The Lab, Pharmacy, and OPD use different standalone software systems. The cashier has to manually copy totals from three different screens to generate a final bill, leading to calculation errors and missed items.</p>
            <p style="margin-top:12px"><strong>The ZenoHosp Solution:</strong> One Centralized Finance Module. Every single app (Pharmacy, Lab, OT, OPD) is natively linked to a single Finance Engine. The moment a test is ordered or a drug is dispensed, it automatically hits the central patient ledger. Zero manual entry, zero missed charges.</p>
          </div>
        </div>
        <div class="leakage-visual">
          <!-- Placeholder for dashboard visual -->
          <div style="padding: 40px; text-align: center;">
            <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
            </svg>
            <h3 style="margin-top: 20px; color: #333;">Live IPD Billing Engine</h3>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 2: Inventory & Pharmacy Leakage -->
  <section class="leakage-section dark">
    <div class="container">
      <div class="leakage-grid reverse">
        <div class="leakage-content">
          <span class="leakage-label label-blue">Pharmacy & Inventory Leakage</span>
          <h2>Stop throwing expired drugs in the bin.</h2>
          <p>Pharmacy stock expiry and pilferage are massive silent killers of hospital margins. ZenoHosp brings enterprise-grade supply chain controls to your pharmacy.</p>
          
          <div class="example-box">
            <h4><span style="color:#3b82f6">✕</span> The Expiry Wastage</h4>
            <p><strong>The Problem:</strong> Pharmacists dispense newer batches that are easy to reach, leaving older batches at the back of the shelf to expire (averaging 3% revenue loss).</p>
            <p style="margin-top:12px; color: rgba(255,255,255,0.7)"><strong>The ZenoHosp Solution:</strong> The system enforces FEFO (First Expire, First Out) at the POS. It strictly prevents dispensing newer batches if an older batch exists, and alerts managers 60 days before expiry to return stock.</p>
          </div>

          <div class="example-box">
            <h4><span style="color:#3b82f6">✕</span> The Silent Pilferage</h4>
            <p><strong>The Problem:</strong> High-value drugs slowly disappear from the pharmacy without being billed, and it takes months to notice during an annual physical audit.</p>
            <p style="margin-top:12px; color: rgba(255,255,255,0.7)"><strong>The ZenoHosp Solution:</strong> Shift-wise stock reconciliation. Every tablet dispensed is tracked via barcode. At the end of a shift, physical stock must match digital stock before the next pharmacist logs in.</p>
          </div>
        </div>
        <div class="leakage-visual">
          <!-- Placeholder for dashboard visual -->
          <div style="padding: 40px; text-align: center;">
            <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
              <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
              <line x1="12" y1="22.08" x2="12" y2="12"/>
            </svg>
            <h3 style="margin-top: 20px; color: #fff;">Automated FEFO Controls</h3>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3: Data & Security Leakage -->
  <section class="leakage-section">
    <div class="container">
      <div class="leakage-grid">
        <div class="leakage-content">
          <span class="leakage-label label-green">Data Security Leakage</span>
          <h2>Total control over who sees what.</h2>
          <p>Patient data is your most valuable asset. Data leaks destroy reputation and violate ABDM compliance. ZenoHosp locks down your system with bank-grade security.</p>
          
          <div class="example-box">
            <h4><span style="color:#10b981">✕</span> Unauthorized Access</h4>
            <p><strong>The Problem:</strong> Junior staff viewing VIP patient records or unauthorized cashiers modifying discounts on past bills.</p>
            <p style="margin-top:12px"><strong>The ZenoHosp Solution:</strong> Strict Role-Based Access Control (RBAC). A receptionist can book an appointment but cannot see clinical notes. A cashier can process payments but cannot delete a finalized bill without an admin OTP.</p>
          </div>

          <div class="example-box">
            <h4><span style="color:#10b981">✕</span> The "Ghost" Edits</h4>
            <p><strong>The Problem:</strong> A patient's diagnosis or bill amount changes, and nobody knows who did it or when.</p>
            <p style="margin-top:12px"><strong>The ZenoHosp Solution:</strong> Immutable Audit Logs. Every click, view, edit, and deletion is recorded permanently. The admin dashboard shows exactly which user made the change, from which IP address, at what second.</p>
          </div>
        </div>
        <div class="leakage-visual">
          <!-- Placeholder for dashboard visual -->
          <div style="padding: 40px; text-align: center;">
            <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
            </svg>
            <h3 style="margin-top: 20px; color: #333;">Immutable Audit Trails</h3>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Banner -->
  <section class="cta-banner">
    <div class="container">
      <h2>Stop the leaks today.</h2>
      <p>Every day on a legacy system is money lost. Switch to ZenoHosp and watch your margins instantly improve.</p>
      <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: #111; color: #fff; border-color: #111;">Request a Custom Demo</a>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/index.html" class="logo">
            <span class="logo-icon">Z</span>
            <span class="logo-text">Zeno<span class="logo-accent">Hosp</span></span>
          </a>
          <p>Hospital software built in Chennai, used by 75+ facilities across India.</p>
          <div class="social-links">
            <a href="#" aria-label="LinkedIn"><svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
              </svg></a>
            <a href="#" aria-label="Twitter"><svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
              </svg></a>
            <a href="#" aria-label="Facebook"><svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
              </svg></a>
            <a href="mailto:hi@zenohosp.com" aria-label="Email"><svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" />
              </svg></a>
          </div>
        </div>
        <div class="footer-links">
          <h4>Solutions</h4>
          <ul>
            <li><a href="/apps/hms/index.html">Hospital Management</a></li>
            <li><a href="/apps/ot-room/index.html">Operation Theatre</a></li>
            <li><a href="/apps/pharmacy/index.html">Pharmacy</a></li>
            <li><a href="/apps/inventory/index.html">Inventory</a></li>
            <li><a href="/apps/asset/index.html">Asset Management</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Company</h4>
          <ul>
            <li><a href="/about-us/index.html">About Us</a></li>
            <li><a href="/careers/index.html">Careers</a></li>
            <li><a href="/blog/index.html">Blog</a></li>
            <li><a href="/contact-us/index.html">Contact Us</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Support</h4>
          <ul>
            <li><a href="/help/index.html">Help Center</a></li>
            <li><a href="/help/index.html">Documentation</a></li>
            <li><a href="#">API Reference</a></li>
            <li><a href="/status/index.html">Status</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Zeno Hosp. All rights reserved.</p>
        <div class="footer-legal">
          <a href="/privacy-policy/index.html">Privacy Policy</a>
          <a href="/terms-of-service/index.html">Terms of Service</a>
          <a href="/cookie-policy/index.html">Cookies</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="/js/app.js" defer></script>
</body>
</html>"""

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {output_file}")
