import os
import re

def update_custom_software():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/custom-software/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    new_css = """
    /* Global Experience Section */
    .global-section {
      padding: 100px 0;
      background: #0a0a08;
      color: #fff;
      border-top: 1px solid rgba(255,255,255,0.05);
    }
    .global-header {
      text-align: center;
      margin-bottom: 60px;
    }
    .global-header h2 {
      font-size: 2.5rem;
      font-weight: 800;
      margin-bottom: 16px;
    }
    .global-header p {
      color: rgba(255,255,255,0.6);
      font-size: 1.15rem;
      max-width: 600px;
      margin: 0 auto;
    }
    .global-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 32px;
    }
    .global-card {
      background: #111;
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 16px;
      padding: 40px;
      position: relative;
      overflow: hidden;
      transition: border-color 0.3s;
    }
    .global-card:hover {
      border-color: #10b981;
    }
    .flag-icon {
      font-size: 2.5rem;
      margin-bottom: 24px;
      display: inline-block;
    }
    .global-card h3 {
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .global-card h3 span {
      font-size: 0.85rem;
      background: rgba(16, 185, 129, 0.15);
      color: #10b981;
      padding: 4px 12px;
      border-radius: 100px;
      font-weight: 600;
    }
    .global-card p {
      color: rgba(255,255,255,0.7);
      line-height: 1.6;
    }

    /* Healthcare Expertise Section */
    .expertise-section {
      padding: 100px 0;
      background: #f8fafc;
    }
    .expertise-header {
      text-align: center;
      margin-bottom: 60px;
    }
    .expertise-header h2 {
      font-size: 2.5rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 16px;
    }
    .expertise-header p {
      color: #64748b;
      font-size: 1.15rem;
      max-width: 700px;
      margin: 0 auto;
    }
    .expertise-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
    }
    .expertise-card {
      background: #fff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 32px 24px;
      text-align: center;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
      transition: transform 0.3s, box-shadow 0.3s;
    }
    .expertise-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
      border-color: #10b981;
    }
    .expertise-icon {
      width: 48px;
      height: 48px;
      margin: 0 auto 20px;
      background: rgba(16, 185, 129, 0.1);
      color: #10b981;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .expertise-card h4 {
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 8px;
      font-size: 1.1rem;
    }
    .expertise-card p {
      color: #64748b;
      font-size: 0.9rem;
      line-height: 1.5;
    }

    @media (max-width: 900px) {
      .global-grid { grid-template-columns: 1fr; }
      .expertise-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .expertise-grid { grid-template-columns: 1fr; }
    }
"""
    
    # Inject CSS
    content = content.replace("</style>", new_css + "\n  </style>")

    new_html = """
  <!-- Global Experience Section -->
  <section class="global-section">
    <div class="container">
      <div class="global-header">
        <h2>Global Standards. Local Implementation.</h2>
        <p>We build software that scales internationally while strictly adhering to the complex compliance frameworks of your specific region.</p>
      </div>
      <div class="global-grid">
        <div class="global-card">
          <div class="flag-icon">🇺🇸</div>
          <h3>United States <span>HIPAA Compliant</span></h3>
          <p>We engineer secure telemedicine portals, specialized EHR integrations (HL7), and robust medical billing modules designed strictly for the US market, ensuring 100% HIPAA compliance and encrypted patient data management.</p>
        </div>
        <div class="global-card">
          <div class="flag-icon">🇦🇪</div>
          <h3>United Arab Emirates <span>DHA Standards</span></h3>
          <p>Delivering premium patient concierge applications, multilingual queue management systems, and high-end hospital administration panels tailored for luxury private clinics and major hospital chains in Dubai and Abu Dhabi.</p>
        </div>
        <div class="global-card">
          <div class="flag-icon">🇮🇳</div>
          <h3>India <span>ABDM Integrated</span></h3>
          <p>Building high-volume OPD management tools, scalable HMS deployments, and ABHA ID integrations for massive multi-specialty hospitals, conforming strictly to the Ayushman Bharat Digital Mission (ABDM) and NABH guidelines.</p>
        </div>
        <div class="global-card">
          <div class="flag-icon">🇬🇧🇸🇬</div>
          <h3>UK & Singapore <span>Data Residency (GDPR/PDPA)</span></h3>
          <p>Developing highly secure electronic medical records (EMR) and cross-hospital referral networks with rigid access controls, designed ground-up for European GDPR and Singapore PDPA data residency laws.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Deep Healthcare Expertise Section -->
  <section class="expertise-section">
    <div class="container">
      <div class="expertise-header">
        <h2>We Speak Your Language.</h2>
        <p>Generic dev shops don't understand medical workflows. We bring deep, proven domain expertise in healthcare protocols, saving you months of expensive onboarding.</p>
      </div>
      <div class="expertise-grid">
        <div class="expertise-card">
          <div class="expertise-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
          <h4>Compliance First</h4>
          <p>Built-in HIPAA, GDPR, and ABDM compliance from day one. Audit logging and RBAC included standard.</p>
        </div>
        <div class="expertise-card">
          <div class="expertise-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg></div>
          <h4>HL7 & FHIR Native</h4>
          <p>We build modules that converse effortlessly with existing EHRs and third-party systems using modern HL7/FHIR APIs.</p>
        </div>
        <div class="expertise-card">
          <div class="expertise-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg></div>
          <h4>DICOM & PACS</h4>
          <p>Integration capabilities for radiology imaging directly into your custom patient portals and doctor dashboards.</p>
        </div>
        <div class="expertise-card">
          <div class="expertise-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
          <h4>Clinical Workflows</h4>
          <p>We understand triaging, ICD-10 coding, prescription pathways, and the nuances of doctor-patient interactions.</p>
        </div>
      </div>
    </div>
  </section>
"""
    
    # Inject HTML right before <!-- How We Manage Flow -->
    # We will split at <!-- How We Manage Flow --> and insert the new_html in between.
    
    parts = content.split("<!-- How We Manage Flow -->")
    if len(parts) == 2:
        final_content = parts[0] + new_html + "\n  <!-- How We Manage Flow -->" + parts[1]
    else:
        print("Could not find insertion point.")
        return

    with open(file_path, 'w') as f:
        f.write(final_content)
    print("Injected new sections successfully.")

if __name__ == "__main__":
    update_custom_software()
