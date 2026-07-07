import os

def update_social_media_seo():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/social-media/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Update Title and Meta Description
    content = content.replace(
        '<title>Hospital Social Media & Video Management | ZenoHosp Services</title>',
        '<title>Healthcare Social Media Marketing & Doctor Branding | ZenoHosp</title>'
    )
    content = content.replace(
        '<meta name="description" content="ZenoHosp handles hospital social media content, including professional video shoots and editing through our exclusive tie-up with Zesignworks.">',
        """<meta name="description" content="Elevate your hospital's digital presence with ZenoHosp's healthcare social media marketing. We provide professional video shoots, Reels editing, and doctor branding.">"""
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
      "name": "Who writes the medical content for our hospital's social media?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All medical content is drafted by healthcare-certified copywriters and verified by doctors before publishing to ensure 100% medical accuracy and compliance."
      }
    }, {
      "@type": "Question",
      "name": "Do you send a team to our hospital for video shoots?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, through our exclusive collaboration with Zesignworks, our professional in-house video team travels to your hospital to shoot high-quality Reels, YouTube videos, and patient testimonials."
      }
    }, {
      "@type": "Question",
      "name": "Can you post content in regional languages?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. We specialize in localized healthcare marketing and create native posts in Tamil, Hindi, Telugu, and Malayalam to deeply connect with your local patient demographic."
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
    .seo-section { padding: 80px 0; background: #0a0a08; border-top: 1px solid rgba(255,255,255,0.05); }
    .seo-section.alt-bg { background: #0f1218; }
    .seo-header { text-align: center; margin-bottom: 48px; max-width: 800px; margin-left: auto; margin-right: auto; }
    .seo-header h2 { font-size: 2.5rem; font-weight: 800; color: #fff; margin-bottom: 16px; }
    .seo-header p { font-size: 1.15rem; color: rgba(255,255,255,0.6); line-height: 1.6; }
    
    .stats-block { display: flex; flex-wrap: wrap; justify-content: center; gap: 40px; margin-bottom: 60px; }
    .stat-card { background: linear-gradient(145deg, #161b22, #0a0a08); border: 1px solid rgba(236,72,153,0.2); padding: 40px; border-radius: 16px; text-align: center; width: 280px; }
    .stat-card h3 { font-size: 3.5rem; font-weight: 800; background: linear-gradient(135deg, #f43f5e, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 8px; }
    .stat-card p { color: rgba(255,255,255,0.8); font-size: 1.1rem; font-weight: 600; }
    
    .faq-grid { max-width: 800px; margin: 0 auto; }
    .faq-item { background: #161b22; border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; margin-bottom: 16px; padding: 24px; }
    .faq-item h3 { font-size: 1.2rem; font-weight: 700; color: #fff; margin-bottom: 12px; }
    .faq-item p { color: rgba(255,255,255,0.6); line-height: 1.6; margin: 0; }
"""
    if '.seo-section' not in content:
        content = content.replace('</style>', css + '\n  </style>')

    # 4. Inject new HTML Sections before Footer
    new_html = """
  <!-- Doctor Branding Section -->
  <section class="seo-section">
    <div class="container">
      <div class="seo-header">
        <h2>Doctor Personal Branding</h2>
        <p>Patients connect with doctors, not buildings. We build the personal brand of your lead consultants to establish them as thought leaders in their specialties.</p>
      </div>
      <div class="stats-block">
        <div class="stat-card">
          <h3>35%</h3>
          <p>Average Growth in Digital Metrics</p>
        </div>
        <div class="stat-card">
          <h3>40+</h3>
          <p>Hospitals Partnered With</p>
        </div>
        <div class="stat-card">
          <h3>60+</h3>
          <p>Doctor Profiles Managed</p>
        </div>
      </div>
      <div style="text-align: center; max-width: 700px; margin: 0 auto;">
        <p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; line-height: 1.7; margin-bottom: 32px;">Our dedicated in-house team handles everything from script-writing to professional video shoots and editing. We create educational YouTube content and viral Instagram Reels that humanize your doctors and build massive patient trust before they even book an appointment.</p>
        <a href="/contact-us/index.html" class="btn btn-primary" style="background: linear-gradient(135deg, #ec4899, #8b5cf6); border: none;">Start Building Your Brand</a>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="seo-section alt-bg">
    <div class="container">
      <div class="seo-header">
        <h2>Frequently Asked Questions</h2>
        <p>Everything you need to know about our healthcare social media services.</p>
      </div>
      <div class="faq-grid">
        <div class="faq-item">
          <h3>Who writes the medical content for our hospital's social media?</h3>
          <p>All medical content is drafted by healthcare-certified copywriters and verified by doctors before publishing to ensure 100% medical accuracy and compliance.</p>
        </div>
        <div class="faq-item">
          <h3>Do you send a team to our hospital for video shoots?</h3>
          <p>Yes, through our exclusive collaboration with Zesignworks, our professional in-house video team travels to your hospital to shoot high-quality Reels, YouTube videos, and patient testimonials.</p>
        </div>
        <div class="faq-item">
          <h3>Can you post content in regional languages?</h3>
          <p>Absolutely. We specialize in localized healthcare marketing and create native posts in Tamil, Hindi, Telugu, and Malayalam to deeply connect with your local patient demographic.</p>
        </div>
      </div>
    </div>
  </section>
"""
    
    if '<!-- Doctor Branding Section -->' not in content:
        # In social media, we can put it right before the Footer
        content = content.replace('  <!-- Footer -->', new_html + '\n  <!-- Footer -->')

    with open(file_path, 'w') as f:
        f.write(content)
    print("Updated Social Media SEO & Sections")

if __name__ == "__main__":
    update_social_media_seo()
