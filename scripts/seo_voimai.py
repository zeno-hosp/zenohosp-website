import os

def update_voimai_seo():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/voimai/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Update Title and Meta Description for better CTR
    content = content.replace(
        '<title>Voim.ai | Healthcare AI Voice Agent by ZenoHosp</title>',
        '<title>Hospital AI Voice Assistant & Automated Caller | Voim.ai</title>'
    )
    content = content.replace(
        '<meta name="description" content="Voim.ai is an advanced AI Voice Agent for hospitals that handles 1000 calls simultaneously for appointments, follow-ups, and more. Powered by Zesignworks.">',
        """<meta name="description" content="Automate your hospital's reception with Voim.ai. Our AI Voice Assistant handles 1000+ simultaneous incoming and outgoing calls in 400+ languages to boost patient satisfaction.">"""
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
      "name": "How does Voim.ai handle complex medical queries from patients?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voim.ai is trained to handle administrative tasks like appointment booking and post-treatment follow-ups. If a patient asks a complex medical question, the AI seamlessly transfers the call to a human medical professional."
      }
    }, {
      "@type": "Question",
      "name": "Can Voim.ai speak multiple regional languages in the same call?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, Voim.ai can automatically detect the caller's language and switch instantly. It supports over 400 languages including Tamil, Hindi, Telugu, and Malayalam natively."
      }
    }, {
      "@type": "Question",
      "name": "Is patient data recorded by Voim.ai secure?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Patient privacy is paramount. Voim.ai operates with a strict 30-day auto-delete policy for all call recordings to ensure data protection and regulatory compliance."
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
    .seo-section { padding: 80px 0; background: #050a12; border-top: 1px solid rgba(255,255,255,0.05); }
    .seo-section.alt-bg { background: #0a101d; }
    .seo-header { text-align: center; margin-bottom: 48px; max-width: 800px; margin-left: auto; margin-right: auto; }
    .seo-header h2 { font-size: 2.5rem; font-weight: 800; color: #fff; margin-bottom: 16px; }
    .seo-header p { font-size: 1.15rem; color: #94a3b8; line-height: 1.6; }
    
    .usecase-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 40px; }
    .usecase-card { background: #050a12; border: 1px solid rgba(16,185,129,0.2); padding: 40px; border-radius: 16px; position: relative; overflow: hidden; }
    .usecase-card::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #10b981, #3b82f6); }
    .usecase-card h3 { font-size: 1.5rem; font-weight: 700; color: #fff; margin-bottom: 24px; display: flex; align-items: center; gap: 12px; }
    .usecase-card ul { list-style: none; padding: 0; }
    .usecase-card li { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 16px; color: #94a3b8; line-height: 1.6; }
    .usecase-card li svg { color: #10b981; flex-shrink: 0; margin-top: 4px; }
    
    .bottleneck-box { background: linear-gradient(145deg, #1e1b4b, #050a12); border: 1px solid rgba(99,102,241,0.2); border-radius: 16px; padding: 48px; text-align: center; margin-top: 40px; }
    .bottleneck-box h3 { font-size: 2rem; color: #fff; margin-bottom: 16px; }
    .bottleneck-box p { font-size: 1.1rem; color: #a5b4fc; max-width: 700px; margin: 0 auto; line-height: 1.6; }
    
    .faq-grid { max-width: 800px; margin: 0 auto; }
    .faq-item { background: #050a12; border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; margin-bottom: 16px; padding: 24px; }
    .faq-item h3 { font-size: 1.2rem; font-weight: 700; color: #fff; margin-bottom: 12px; }
    .faq-item p { color: #94a3b8; line-height: 1.6; margin: 0; }
    
    @media (max-width: 768px) {
      .usecase-grid { grid-template-columns: 1fr; }
    }
"""
    if '.seo-section' not in content:
        content = content.replace('</style>', css + '\n  </style>')

    # 4. Inject new HTML Sections before the CTA Section
    new_html = """
  <!-- The Staffing Bottleneck Section -->
  <section class="seo-section alt-bg">
    <div class="container">
      <div class="bottleneck-box">
        <h3>The Receptionist Bottleneck</h3>
        <p>During peak hours (9 AM - 12 PM), human receptionists handle an overwhelming volume of calls. Patients get put on hold, hang up in frustration, and book appointments with your competitors. Voim.ai completely eliminates this bottleneck by handling thousands of concurrent calls effortlessly.</p>
      </div>
    </div>
  </section>

  <!-- Use Cases Deep Dive -->
  <section class="seo-section">
    <div class="container">
      <div class="seo-header">
        <h2>Comprehensive Call Management</h2>
        <p>Voim.ai acts as your hospital's 24/7 intelligent front desk, seamlessly managing both inbound queries and proactive outbound follow-ups.</p>
      </div>
      <div class="usecase-grid">
        <div class="usecase-card">
          <h3><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path><polyline points="15 3 21 9 15 15"></polyline></svg> Incoming Agent</h3>
          <ul>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Automatically books, reschedules, or cancels appointments through WhatsApp integration.</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Answers routine queries (hospital timings, doctor availability, insurance accepted).</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Routes emergency calls directly to the casualty department instantly.</li>
          </ul>
        </div>
        <div class="usecase-card">
          <h3><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path><polyline points="9 15 3 9 9 3"></polyline></svg> Outgoing Agent</h3>
          <ul>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Calls patients for post-discharge feedback and health check-ups.</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Automated appointment confirmation and pre-surgery instruction reminders.</li>
            <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Proactive medicine refill reminders to improve patient adherence.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="seo-section alt-bg">
    <div class="container">
      <div class="seo-header">
        <h2>Frequently Asked Questions</h2>
        <p>Common questions hospital administrators ask about Voim.ai.</p>
      </div>
      <div class="faq-grid">
        <div class="faq-item">
          <h3>How does Voim.ai handle complex medical queries from patients?</h3>
          <p>Voim.ai is trained to handle administrative tasks like appointment booking and post-treatment follow-ups. If a patient asks a complex medical question, the AI seamlessly transfers the call to a human medical professional.</p>
        </div>
        <div class="faq-item">
          <h3>Can Voim.ai speak multiple regional languages in the same call?</h3>
          <p>Yes, Voim.ai can automatically detect the caller's language and switch instantly. It supports over 400 languages including Tamil, Hindi, Telugu, and Malayalam natively.</p>
        </div>
        <div class="faq-item">
          <h3>Is patient data recorded by Voim.ai secure?</h3>
          <p>Patient privacy is paramount. Voim.ai operates with a strict 30-day auto-delete policy for all call recordings to ensure data protection and regulatory compliance.</p>
        </div>
      </div>
    </div>
  </section>

"""
    
    if '<!-- The Staffing Bottleneck Section -->' not in content:
        # In voimai, we can put it right before the CTA Banner
        content = content.replace('  <!-- CTA Banner -->', new_html + '  <!-- CTA Banner -->')

    with open(file_path, 'w') as f:
        f.write(content)
    print("Updated Voimai SEO & Sections")

if __name__ == "__main__":
    update_voimai_seo()
