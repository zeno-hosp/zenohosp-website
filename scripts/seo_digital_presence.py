import os

def update_digital_presence_seo():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/digital-presence/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Update Title and Meta Description for better CTR
    content = content.replace(
        '<title>Digital Presence & Website Creation for Hospitals | ZenoHosp Services</title>',
        '<title>Hospital Website Development & Healthcare SEO Services | ZenoHosp</title>'
    )
    content = content.replace(
        '<meta name="description" content="ZenoHosp builds and manages world-class websites for hospitals. We handle technical SEO, manage daily news, and update doctor schedules.">',
        '<meta name="description" content="Boost patient footfall with ZenoHosp\'s hospital website development and local healthcare SEO services. We design medical websites that rank #1 on Google.">'
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
      "name": "How long does it take to build a custom hospital website?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically, a fully customized, responsive hospital website takes 3 to 6 weeks to design, develop, and launch, including patient portal integrations."
      }
    }, {
      "@type": "Question",
      "name": "Do you provide medical content writing and SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, our team includes healthcare copywriters who produce medically accurate, SEO-optimized content to help your hospital rank higher on Google for local searches."
      }
    }, {
      "@type": "Question",
      "name": "Is the website HIPAA and data privacy compliant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. All patient data collection forms and portals we integrate are highly secure and comply with strict healthcare data protection standards."
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
    .seo-section.alt-bg { background: #f8f9fb; }
    .seo-header { text-align: center; margin-bottom: 48px; max-width: 800px; margin-left: auto; margin-right: auto; }
    .seo-header h2 { font-size: 2.5rem; font-weight: 800; color: #111; margin-bottom: 16px; }
    .seo-header p { font-size: 1.15rem; color: #4b5563; line-height: 1.6; }
    
    .pain-point-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; }
    .pain-card { background: #fff; border: 1px solid #fee2e2; border-left: 4px solid #ef4444; padding: 32px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
    .pain-card h3 { font-size: 1.25rem; font-weight: 700; color: #111; margin-bottom: 12px; }
    .pain-card p { color: #4b5563; line-height: 1.6; }
    
    .local-seo-box { display: flex; align-items: center; gap: 48px; background: #fff; border-radius: 16px; border: 1px solid #e5e7eb; padding: 48px; }
    .local-seo-content { flex: 1; }
    .local-seo-content h3 { font-size: 2rem; font-weight: 800; color: #111; margin-bottom: 16px; }
    .local-seo-content p { font-size: 1.1rem; color: #4b5563; line-height: 1.7; margin-bottom: 24px; }
    .local-seo-content ul { list-style: none; padding: 0; margin-bottom: 32px; }
    .local-seo-content li { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; font-weight: 600; color: #111; }
    .local-seo-content li svg { color: #22c55e; }
    
    .faq-grid { max-width: 800px; margin: 0 auto; }
    .faq-item { background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; margin-bottom: 16px; padding: 24px; }
    .faq-item h3 { font-size: 1.2rem; font-weight: 700; color: #111; margin-bottom: 12px; }
    .faq-item p { color: #4b5563; line-height: 1.6; margin: 0; }
    
    @media (max-width: 768px) {
      .local-seo-box { flex-direction: column; padding: 24px; }
    }
"""
    if '.seo-section' not in content:
        content = content.replace('</style>', css + '\n  </style>')

    # 4. Inject new HTML Sections before CTA Banner
    new_html = """
  <!-- Pain Points Section -->
  <section class="seo-section alt-bg">
    <div class="container">
      <div class="seo-header">
        <h2>Why Your Hospital is Losing Patients Online</h2>
        <p>If your website isn't working as your hardest-working front desk executive, you are losing potential patients to competitors.</p>
      </div>
      <div class="pain-point-grid">
        <div class="pain-card">
          <h3>Slow Loading Speeds</h3>
          <p>Patients seeking emergency care or quick appointments abandon websites that take longer than 3 seconds to load. We build lightning-fast platforms.</p>
        </div>
        <div class="pain-card">
          <h3>Not Mobile-Friendly</h3>
          <p>Over 80% of healthcare searches happen on mobile phones. A desktop-only design frustrates patients trying to find your phone number or address.</p>
        </div>
        <div class="pain-card">
          <h3>Invisible on Google</h3>
          <p>Having a beautiful website means nothing if you don't rank for "Best Hospital Near Me." Poor SEO structure actively hurts your OPD numbers.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Local SEO Section -->
  <section class="seo-section">
    <div class="container">
      <div class="local-seo-box">
        <div class="local-seo-content">
          <h3>Dominate Local Healthcare Searches</h3>
          <p>When a patient in your city searches for a specialist, your hospital should be the first result. Our technical healthcare SEO ensures you rank #1 on Google Search and Maps.</p>
          <ul>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Google Business Profile Optimization</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Specialty-Specific Keyword Targeting</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Medically Accurate Content Writing</li>
          </ul>
          <a href="/contact-us/index.html" class="btn btn-primary">Start Ranking Today</a>
        </div>
        <div style="flex: 1; text-align: center;">
          <div style="background: #f8f9fb; border-radius: 12px; padding: 24px; border: 1px solid #e5e7eb; display: inline-block; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: center; gap: 12px; border-bottom: 1px solid #e5e7eb; padding-bottom: 16px; margin-bottom: 16px;">
              <div style="background: #e5e7eb; width: 40px; height: 40px; border-radius: 50%;"></div>
              <div style="text-align: left;">
                <div style="width: 120px; height: 12px; background: #d1d5db; border-radius: 4px; margin-bottom: 6px;"></div>
                <div style="width: 80px; height: 8px; background: #e5e7eb; border-radius: 4px;"></div>
              </div>
            </div>
            <div style="color: #22c55e; font-size: 1.5rem; font-weight: 800; margin-bottom: 4px;">#1 Position</div>
            <div style="color: #6b7280; font-size: 0.9rem;">For "Best Orthopedic in [City]"</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="seo-section alt-bg">
    <div class="container">
      <div class="seo-header">
        <h2>Frequently Asked Questions</h2>
        <p>Common questions hospital founders have about our digital presence services.</p>
      </div>
      <div class="faq-grid">
        <div class="faq-item">
          <h3>How long does it take to build a custom hospital website?</h3>
          <p>Typically, a fully customized, responsive hospital website takes 3 to 6 weeks to design, develop, and launch, including patient portal integrations.</p>
        </div>
        <div class="faq-item">
          <h3>Do you provide medical content writing and SEO?</h3>
          <p>Yes, our team includes healthcare copywriters who produce medically accurate, SEO-optimized content to help your hospital rank higher on Google for local searches.</p>
        </div>
        <div class="faq-item">
          <h3>Is the website HIPAA and data privacy compliant?</h3>
          <p>Absolutely. All patient data collection forms and portals we integrate are highly secure and comply with strict healthcare data protection standards.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Banner -->"""
    
    if '<!-- Pain Points Section -->' not in content:
        content = content.replace('  <!-- CTA Banner -->', new_html)

    with open(file_path, 'w') as f:
        f.write(content)
    print("Updated Digital Presence SEO & Sections")

if __name__ == "__main__":
    update_digital_presence_seo()
