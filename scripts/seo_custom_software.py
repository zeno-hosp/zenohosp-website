import os

def update_custom_software_seo():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/custom-software/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Update Title and Meta Description for better CTR
    content = content.replace(
        '<title>Customized Hospital Software Development | ZenoHosp Services</title>',
        '<title>Custom Healthcare Software Development & HMS | ZenoHosp</title>'
    )
    content = content.replace(
        '<meta name="description" content="ZenoHosp creates bespoke healthcare software and customized hospital modules tailored to your unique operational requirements.">',
        '<meta name="description" content="Build bespoke healthcare software and custom clinic management modules tailored to your exact workflows. 100% HIPAA and NABH compliant custom HMS development.">'
    )

    # 2. Inject JSON-LD Schema
    schema_json = """
  <!-- FAQ Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
      "@type": "Question",
      "name": "Can you integrate custom modules with our existing Hospital Management System?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, we specialize in building bespoke modules via APIs (HL7, FHIR) that integrate directly with your existing HMS, lab equipment, and third-party billing portals."
      }
    }, {
      "@type": "Question",
      "name": "Is the custom healthcare software HIPAA and NABH compliant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. Security is our top priority. All our bespoke healthcare software architectures include robust data encryption, role-based access control, and complete audit trails to ensure 100% compliance."
      }
    }, {
      "@type": "Question",
      "name": "Why choose custom hospital software over off-the-shelf solutions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generic software forces your hospital to adapt its workflows to the system. Custom software adapts to your unique processes, saving doctors time, reducing errors, and dramatically improving operational efficiency."
      }
    }]
  }
  </script>
"""
    if 'application/ld+json' not in content:
        content = content.replace('</head>', schema_json + '</head>')

    # 3. Add CSS for new sections
    css = """
    /* SEO Sections CSS */
    .seo-section { padding: 80px 0; background: #fff; }
    .seo-section.alt-bg { background: #f9fafb; }
    .seo-header { text-align: center; margin-bottom: 48px; max-width: 800px; margin-left: auto; margin-right: auto; }
    .seo-header h2 { font-size: 2.5rem; font-weight: 800; color: #111; margin-bottom: 16px; }
    .seo-header p { font-size: 1.15rem; color: #4b5563; line-height: 1.6; }
    
    .comparison-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 32px; }
    .comparison-card { padding: 40px; border-radius: 16px; border: 1px solid #e5e7eb; background: #fff; }
    .comparison-card.bad { border-top: 4px solid #ef4444; }
    .comparison-card.good { border-top: 4px solid #22c55e; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .comparison-card h3 { font-size: 1.5rem; font-weight: 800; margin-bottom: 24px; color: #111; }
    .comparison-card ul { list-style: none; padding: 0; }
    .comparison-card li { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 16px; color: #4b5563; line-height: 1.6; }
    .comparison-card.bad li svg { color: #ef4444; flex-shrink: 0; margin-top: 4px; }
    .comparison-card.good li svg { color: #22c55e; flex-shrink: 0; margin-top: 4px; }
    
    .integration-logos { display: flex; flex-wrap: wrap; justify-content: center; gap: 24px; margin-top: 40px; }
    .integration-pill { background: #fff; border: 1px solid #e5e7eb; padding: 12px 24px; border-radius: 100px; font-weight: 700; color: #111; display: flex; align-items: center; gap: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    
    .faq-grid { max-width: 800px; margin: 0 auto; }
    .faq-item { background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; margin-bottom: 16px; padding: 24px; }
    .faq-item h3 { font-size: 1.2rem; font-weight: 700; color: #111; margin-bottom: 12px; }
    .faq-item p { color: #4b5563; line-height: 1.6; margin: 0; }
    
    @media (max-width: 768px) {
      .comparison-grid { grid-template-columns: 1fr; }
    }
"""
    if '.seo-section' not in content:
        content = content.replace('</style>', css + '\n  </style>')

    # 4. Inject new HTML Sections before the CTA Section (which starts with <section class="cta-section)
    new_html = """
  <!-- Comparison Section -->
  <section class="seo-section alt-bg">
    <div class="container">
      <div class="seo-header">
        <h2>Off-The-Shelf vs. Custom Built HMS</h2>
        <p>Why forcing your doctors and staff to adapt to generic software is costing your hospital time and money.</p>
      </div>
      <div class="comparison-grid">
        <div class="comparison-card bad">
          <h3>Generic Hospital Software</h3>
          <ul>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg> Rigid workflows that slow doctors down during peak OPD hours.</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg> Bloated with hundreds of features you pay for but never use.</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg> Impossible to integrate with specific lab machinery or local insurance APIs.</li>
          </ul>
        </div>
        <div class="comparison-card good">
          <h3>Bespoke ZenoHosp Software</h3>
          <ul>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Built entirely around your hospital's unique operational processes.</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Streamlined interfaces designed specifically for your doctors and nurses.</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Seamlessly integrated with any hardware, machinery, or third-party portal.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Integration Section -->
  <section class="seo-section">
    <div class="container">
      <div class="seo-header">
        <h2>Unrestricted Integration Capabilities</h2>
        <p>Our custom software developers build robust APIs (HL7, FHIR compliant) to ensure your new module speaks directly with your existing infrastructure.</p>
      </div>
      <div class="integration-logos">
        <div class="integration-pill">💻 Legacy HMS Integration</div>
        <div class="integration-pill">🔬 Lab Equipment & LIS</div>
        <div class="integration-pill">💸 TPA & Insurance Portals</div>
        <div class="integration-pill">📲 WhatsApp API & SMS</div>
        <div class="integration-pill">💳 Payment Gateways</div>
        <div class="integration-pill">🏥 PACS & Radiology</div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="seo-section alt-bg">
    <div class="container">
      <div class="seo-header">
        <h2>Frequently Asked Questions</h2>
        <p>Common questions hospital founders have about our custom development services.</p>
      </div>
      <div class="faq-grid">
        <div class="faq-item">
          <h3>Can you integrate custom modules with our existing Hospital Management System?</h3>
          <p>Yes, we specialize in building bespoke modules via APIs (HL7, FHIR) that integrate directly with your existing HMS, lab equipment, and third-party billing portals.</p>
        </div>
        <div class="faq-item">
          <h3>Is the custom healthcare software HIPAA and NABH compliant?</h3>
          <p>Absolutely. Security is our top priority. All our bespoke healthcare software architectures include robust data encryption, role-based access control, and complete audit trails to ensure 100% compliance.</p>
        </div>
        <div class="faq-item">
          <h3>Why choose custom hospital software over off-the-shelf solutions?</h3>
          <p>Generic software forces your hospital to adapt its workflows to the system. Custom software adapts to your unique processes, saving doctors time, reducing errors, and dramatically improving operational efficiency.</p>
        </div>
      </div>
    </div>
  </section>

"""
    
    if '<!-- Comparison Section -->' not in content:
        # We need to find the CTA banner which is <section class="cta-section">
        content = content.replace('<section class="cta-section">', new_html + '\n  <section class="cta-section">')

    with open(file_path, 'w') as f:
        f.write(content)
    print("Updated Custom Software SEO & Sections")

if __name__ == "__main__":
    update_custom_software_seo()
