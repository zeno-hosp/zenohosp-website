import os
import re

def add_new_sections():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/voimai/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    css_to_add = """
    /* Interactive Audio Section */
    .audio-demos { padding: 100px 0; background: #ffffff; }
    .audio-demos-header { text-align: center; max-width: 800px; margin: 0 auto 60px; }
    .audio-demos-header h2 { font-size: 2.5rem; font-weight: 800; color: #111827; margin-bottom: 16px; }
    .audio-demos-header p { font-size: 1.15rem; color: #64748b; line-height: 1.6; }
    .audio-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
    .audio-card { background: #f8fafc; border: 1px solid rgba(0,0,0,0.05); border-radius: 16px; padding: 32px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
    .audio-title { font-weight: 700; font-size: 1.2rem; color: #111827; margin-bottom: 8px; }
    .audio-desc { color: #64748b; font-size: 0.95rem; margin-bottom: 24px; }
    .audio-player { display: flex; align-items: center; gap: 16px; background: #ffffff; padding: 12px 16px; border-radius: 100px; border: 1px solid rgba(0,0,0,0.05); }
    .play-btn { width: 40px; height: 40px; border-radius: 50%; background: #2563eb; color: #fff; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; box-shadow: 0 4px 10px rgba(37,99,235,0.3); }
    .waveform { flex-grow: 1; height: 24px; background: repeating-linear-gradient(90deg, #cbd5e1 0px, #cbd5e1 3px, transparent 3px, transparent 6px); border-radius: 12px; opacity: 0.5; }
    .audio-duration { font-size: 0.85rem; font-weight: 600; color: #94a3b8; }
    
    /* Integration Ecosystem */
    .integrations { padding: 100px 0; background: #f8fafc; border-top: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); }
    .integration-grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 24px; margin-top: 48px; }
    .integration-badge { background: #ffffff; border: 1px solid rgba(0,0,0,0.08); padding: 16px 32px; border-radius: 100px; font-weight: 700; color: #111827; font-size: 1.1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03); display: flex; align-items: center; gap: 12px; }
    .integration-badge svg { color: #2563eb; }

    /* Security Section */
    .security-section { padding: 100px 0; background: #ffffff; }
    .security-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 32px; margin-top: 60px; text-align: center; }
    .security-item svg { width: 48px; height: 48px; color: #10b981; margin-bottom: 20px; }
    .security-item h3 { font-size: 1.2rem; font-weight: 700; color: #111827; margin-bottom: 12px; }
    .security-item p { color: #64748b; font-size: 0.95rem; line-height: 1.5; }

    @media (max-width: 900px) {
      .audio-grid, .security-grid { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 600px) {
      .audio-grid, .security-grid { grid-template-columns: 1fr; }
    }
"""

    html_to_add = """
  <!-- Interactive Audio Demos Section -->
  <section class="audio-demos">
    <div class="container">
      <div class="audio-demos-header">
        <div style="display:inline-block; padding: 6px 16px; background: rgba(37, 99, 235, 0.1); border: 1px solid rgba(37, 99, 235, 0.2); border-radius: 100px; color: #2563eb; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 16px;">Listen For Yourself</div>
        <h2>Undistinguishable From Humans</h2>
        <p>Press play to hear how Voim.ai handles complex, multi-turn conversations with patients naturally and empathetically.</p>
      </div>
      
      <div class="audio-grid">
        <div class="audio-card">
          <div class="audio-title">MRI Appointment Booking</div>
          <div class="audio-desc">Handling a patient requesting an urgent MRI, checking doctor availability, and securing a slot.</div>
          <div class="audio-player">
            <div class="play-btn"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg></div>
            <div class="waveform"></div>
            <div class="audio-duration">1:42</div>
          </div>
        </div>
        <div class="audio-card">
          <div class="audio-title">Post-Surgery Follow Up</div>
          <div class="audio-desc">An outbound call checking on a patient 48 hours after a knee arthroscopy to ensure no infections.</div>
          <div class="audio-player">
            <div class="play-btn"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg></div>
            <div class="waveform"></div>
            <div class="audio-duration">2:15</div>
          </div>
        </div>
        <div class="audio-card">
          <div class="audio-title">Insurance Query & Transfer</div>
          <div class="audio-desc">Answering if specific treatments are covered, and seamlessly transferring a complex claim to billing.</div>
          <div class="audio-player">
            <div class="play-btn"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg></div>
            <div class="waveform"></div>
            <div class="audio-duration">1:18</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Integration Ecosystem Section -->
  <section class="integrations">
    <div class="container" style="text-align: center;">
      <h2>Plugs Directly Into Your Tech Stack</h2>
      <p style="color: #64748b; font-size: 1.15rem; max-width: 700px; margin: 16px auto 0;">Voim.ai doesn't just talk. It listens, extracts data, and automatically updates your patient records via secure APIs in real-time.</p>
      
      <div class="integration-grid">
        <div class="integration-badge"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg> ZenoHosp HMS</div>
        <div class="integration-badge"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg> Epic Systems</div>
        <div class="integration-badge"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12h4l2-2 4 4 4-4 4 4"></path></svg> Cerner Millennium</div>
        <div class="integration-badge"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg> Salesforce Health Cloud</div>
        <div class="integration-badge"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg> AdvancedMD</div>
      </div>
    </div>
  </section>

  <!-- Security Section -->
  <section class="security-section">
    <div class="container">
      <div style="text-align: center; max-width: 800px; margin: 0 auto;">
        <h2>Enterprise-Grade Patient Data Security</h2>
        <p style="color: #64748b; font-size: 1.15rem; margin-top: 16px;">We take patient privacy as seriously as you do. Voim.ai is built from the ground up to comply with the strictest healthcare regulations globally.</p>
      </div>
      
      <div class="security-grid">
        <div class="security-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          <h3>100% HIPAA Compliant</h3>
          <p>Fully compliant with the Health Insurance Portability and Accountability Act. Business Associate Agreements (BAAs) provided.</p>
        </div>
        <div class="security-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          <h3>SOC2 Type II Certified</h3>
          <p>Audited by independent third parties to ensure the highest standards of security, availability, and processing integrity.</p>
        </div>
        <div class="security-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="14.31" y1="8" x2="20.05" y2="17.94"></line><line x1="9.69" y1="8" x2="21.17" y2="8"></line><line x1="7.38" y1="12" x2="13.12" y2="2.06"></line><line x1="9.69" y1="16" x2="3.95" y2="6.06"></line><line x1="14.31" y1="16" x2="2.83" y2="16"></line><line x1="16.62" y1="12" x2="10.88" y2="21.94"></line></svg>
          <h3>End-to-End Encryption</h3>
          <p>All data is encrypted in transit using TLS 1.3 and at rest using AES-256 military-grade encryption standards.</p>
        </div>
        <div class="security-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>
          <h3>30-Day Auto-Delete</h3>
          <p>Strict data retention policies. Call recordings and transcripts are permanently wiped after 30 days to minimize liability.</p>
        </div>
      </div>
    </div>
  </section>
"""

    if "<!-- Interactive Audio Demos Section -->" not in content:
        # Insert CSS
        content = content.replace("</style>", css_to_add + "\n  </style>")
        
        # Insert HTML before ROI Section
        target = "<!-- ROI Calculator Section -->"
        if target in content:
             content = content.replace(target, html_to_add + "\n  " + target)
        else:
             print("Could not find target to insert before")
             return
             
        with open(file_path, 'w') as f:
            f.write(content)
        print("Done")
    else:
        print("Sections already exist.")

if __name__ == "__main__":
    add_new_sections()
