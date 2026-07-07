import os

def update_advertising_seo():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/advertising/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Update Title and Meta Description for better CTR
    content = content.replace(
        '<title>Healthcare Digital Advertising | ZenoHosp Services</title>',
        '<title>Hospital Google Ads & Patient Acquisition Agency | ZenoHosp</title>'
    )
    content = content.replace(
        '<meta name="description" content="ZenoHosp provides high-converting healthcare advertising services including Google Ads, Facebook & Instagram Ads, and YouTube Ads for hospitals.">',
        """<meta name="description" content="Maximize your hospital's patient footfall with data-driven healthcare performance marketing. We specialize in Google Ads, Facebook Ads, and high-ROI patient acquisition campaigns.">"""
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
      "name": "What is the expected ROI for hospital advertising?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ROI depends on the specialty and location, but our targeted Google and Facebook ad campaigns typically reduce Patient Acquisition Costs (CAC) by 30-50% while driving immediate high-intent OPD walk-ins."
      }
    }, {
      "@type": "Question",
      "name": "How do you handle strict Google healthcare ad policies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Healthcare advertising policies are notoriously strict. Our certified ad specialists know exactly how to structure landing pages and ad copy to ensure 100% compliance, preventing your ad accounts from getting suspended."
      }
    }, {
      "@type": "Question",
      "name": "Do you guarantee patient footfall?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "While we cannot legally guarantee specific medical outcomes, our performance marketing strategies guarantee highly targeted impressions and clicks from patients actively searching for your specific treatments in your precise locality."
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
    .seo-section { padding: 80px 0; background: #0b0f19; border-top: 1px solid rgba(255,255,255,0.05); }
    .seo-section.alt-bg { background: #151a28; }
    .seo-header { text-align: center; margin-bottom: 48px; max-width: 800px; margin-left: auto; margin-right: auto; }
    .seo-header h2 { font-size: 2.5rem; font-weight: 800; color: #fff; margin-bottom: 16px; }
    .seo-header p { font-size: 1.15rem; color: #94a3b8; line-height: 1.6; }
    
    .pain-point-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; }
    .pain-card { background: #0b0f19; border: 1px solid rgba(255,255,255,0.05); padding: 32px; border-radius: 8px; border-left: 4px solid #ef4444; }
    .pain-card h3 { font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 12px; }
    .pain-card p { color: #94a3b8; line-height: 1.6; }
    
    .faq-grid { max-width: 800px; margin: 0 auto; }
    .faq-item { background: #0b0f19; border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; margin-bottom: 16px; padding: 24px; }
    .faq-item h3 { font-size: 1.2rem; font-weight: 700; color: #fff; margin-bottom: 12px; }
    .faq-item p { color: #94a3b8; line-height: 1.6; margin: 0; }
"""
    if '.seo-section' not in content:
        content = content.replace('</style>', css + '\n  </style>')

    # 4. Inject new HTML Sections before CTA Banner
    new_html = """
  <!-- Pain Points Section -->
  <section class="seo-section alt-bg">
    <div class="container">
      <div class="seo-header">
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
  <section class="seo-section">
    <div class="container">
      <div class="seo-header">
        <h2>Frequently Asked Questions</h2>
        <p>Common questions hospital founders have about our healthcare advertising services.</p>
      </div>
      <div class="faq-grid">
        <div class="faq-item">
          <h3>What is the expected ROI for hospital advertising?</h3>
          <p>ROI depends on the specialty and location, but our targeted Google and Facebook ad campaigns typically reduce Patient Acquisition Costs (CAC) by 30-50% while driving immediate high-intent OPD walk-ins.</p>
        </div>
        <div class="faq-item">
          <h3>How do you handle strict Google healthcare ad policies?</h3>
          <p>Healthcare advertising policies are notoriously strict. Our certified ad specialists know exactly how to structure landing pages and ad copy to ensure 100% compliance, preventing your ad accounts from getting suspended.</p>
        </div>
        <div class="faq-item">
          <h3>Do you guarantee patient footfall?</h3>
          <p>While we cannot legally guarantee specific medical outcomes, our performance marketing strategies guarantee highly targeted impressions and clicks from patients actively searching for your specific treatments in your precise locality.</p>
        </div>
      </div>
    </div>
  </section>

"""
    
    if '<!-- Pain Points Section -->' not in content:
        content = content.replace('  <!-- CTA Banner -->', new_html + '  <!-- CTA Banner -->')

    with open(file_path, 'w') as f:
        f.write(content)
    print("Updated Advertising SEO & Sections")

if __name__ == "__main__":
    update_advertising_seo()
