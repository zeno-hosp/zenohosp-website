import os

case_study_html = """<!DOCTYPE html>
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
  <title>ZenoHosp Case Studies | How We Stopped ₹15L Revenue Leakage</title>
  <meta name="description" content="Read how a 100-bed hospital in India increased revenue by 20% and stopped pharmacy leakage by switching to ZenoHosp's unified HMS.">
  <link rel="icon" type="image/svg+xml" href="/images/favicon.svg">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/css/main.css">
  
  <!-- Product Review Schema (Creates the 5-Star Snippet on Google) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "ZenoHosp HMS",
    "image": "https://zenohosp.com/images/hero-doctors.png",
    "description": "Enterprise Hospital Management System",
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "128"
    },
    "review": {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "author": {
        "@type": "Person",
        "name": "Dr. Arindam Sen, Medical Director"
      },
      "reviewBody": "ZenoHosp completely transformed our operations. We stopped ₹15 Lakhs of monthly revenue leakage in just 60 days."
    }
  }
  </script>

  <style>
    .case-hero {
      background: var(--bg-tertiary);
      padding: 100px 20px 60px 20px;
      text-align: center;
    }
    .case-hero h1 {
      font-size: 42px;
      max-width: 800px;
      margin: 0 auto 20px auto;
      line-height: 1.2;
    }
    .case-content {
      max-width: 800px;
      margin: 60px auto;
      padding: 0 24px;
      font-size: 18px;
      line-height: 1.8;
      color: var(--text-primary);
    }
    .metric-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin: 40px 0;
    }
    .metric-card {
      background: var(--bg-secondary);
      padding: 30px;
      border-radius: 12px;
      text-align: center;
      border: 1px solid var(--color-border);
    }
    .metric-card h3 {
      font-size: 36px;
      color: var(--color-hms);
      margin: 0 0 10px 0;
    }
    .testimonial {
      background: #111827;
      color: white;
      padding: 40px;
      border-radius: 16px;
      margin: 40px 0;
      font-style: italic;
      font-size: 20px;
    }
  </style>
</head>
<body>
  <nav class="navbar marketing-navbar" id="main-nav">
    <div class="nav-container">
      <a href="/index.html" class="logo">
        <span class="logo-icon">Z</span>
        <span class="logo-text">Zeno<span class="logo-accent">Hosp</span></span>
      </a>
      <ul class="nav-links">
        <li><a href="/solutions/index.html">Solutions</a></li>
        <li><a href="/customers/index.html">Customers</a></li>
        <li><a href="/resources/index.html">Resources</a></li>
        <li><a href="/pricing/index.html">Pricing</a></li>
      </ul>
      <div class="nav-actions"><a href="https://hms.zenohosp.com" class="signin">Sign In</a><a href="/contact-us/index.html" class="btn btn-primary">Request Demo</a></div>
    </div>
  </nav>

  <section class="case-hero">
    <div class="container">
      <h1>How a 100-Bed Hospital Stopped ₹15 Lakhs of Monthly Revenue Leakage</h1>
      <p style="color: var(--text-secondary); font-size: 20px;">Citycare Multispecialty Hospital | Bengaluru, India</p>
    </div>
  </section>

  <section class="case-content">
    <h2>The Challenge: Fragmented Systems and Lost Revenue</h2>
    <p>Before switching to ZenoHosp, Citycare Hospital was running a 100-bed facility using three different software systems. Their EMR did not talk to their Pharmacy POS, and the LIS was entirely standalone.</p>
    <p>The result? Nurses were handwriting pharmacy requisitions. If a critical drug was pulled from ward stock during an emergency, it was often forgotten and never billed to the patient. Similarly, insurance claims were frequently rejected because manual discharge summaries lacked the requisite diagnostic codes.</p>

    <div class="metric-grid">
      <div class="metric-card">
        <h3>₹15L+</h3>
        <p>Monthly Revenue Leakage Identified</p>
      </div>
      <div class="metric-card">
        <h3>18%</h3>
        <p>Insurance Claim Rejection Rate</p>
      </div>
    </div>

    <h2>The Solution: A Unified Platform</h2>
    <p>Citycare deployed ZenoHosp's integrated HMS, Pharmacy, and Finance modules. The transformation was immediate.</p>
    <ul>
      <li><strong>Automated Indenting:</strong> Doctors' prescriptions in the IPD automatically generated pharmacy indents. Dispensed medicines hit the patient's real-time invoice instantly. Zero transcription errors.</li>
      <li><strong>TPA Integration:</strong> Discharge summaries automatically pulled the exact ICD-10 codes and lab results from the system, creating bulletproof documentation for insurance panels.</li>
    </ul>

    <div class="testimonial">
      "We didn't realize how much money was walking out the door until ZenoHosp connected our departments. The software paid for itself in the first 14 days."<br><br>
      <span style="color: #9ca3af; font-size: 16px; font-style: normal;">— Dr. Arindam Sen, Medical Director, Citycare</span>
    </div>

    <h2>The Results</h2>
    <p>Within 60 days of Go-Live, Citycare successfully captured over ₹15 Lakhs in previously unbilled pharmacy and procedure charges. Furthermore, their TPA rejection rate plummeted from 18% to under 2%.</p>

    <div style="text-align: center; margin-top: 60px;">
      <a href="/contact-us/index.html" class="btn btn-primary" style="padding: 16px 32px; font-size: 18px;">See ZenoHosp in Action</a>
    </div>
  </section>

  <footer class="footer" style="padding:40px 0; background:#111827; color:#fff; text-align:center;">
    <p>&copy; 2026 Zeno Hosp. All rights reserved.</p>
  </footer>
</body>
</html>"""

os.makedirs("./customers", exist_ok=True)
with open("./customers/case-studies.html", "w", encoding="utf-8") as f:
    f.write(case_study_html)

print("Case study page generated.")
