import os
import re

def update_digital_presence():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/digital-presence/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    # Change blue colors to green colors
    content = content.replace("#3b82f6", "#10b981") # Primary blue -> Primary green
    content = content.replace("rgba(59, 130, 246", "rgba(16, 185, 129") # rgba blue -> rgba green
    content = content.replace("#60a5fa", "#34d399") # Light blue -> Light green
    
    # New Premium Hero Section
    new_hero = """  <!-- Hero Section -->
  <section class="dp-hero">
    <div class="container" style="display: flex; align-items: center; justify-content: space-between; gap: 40px; text-align: left; flex-wrap: wrap;">
      <div style="flex: 1; min-width: 300px; z-index: 2;">
        <div style="display:inline-block; padding: 6px 16px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 100px; color: #10b981; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Managed Digital Presence</div>
        <h1>Hospital Websites<br>that Drive <span style="color: #10b981;">Patient Growth.</span></h1>
        <p>We build beautiful, fast, and secure websites tailored for healthcare. Plus, we handle your ongoing SEO, daily news updates, and doctor profiles—so you can focus on care.</p>
        <div style="display: flex; gap: 16px; margin-top: 32px; flex-wrap: wrap;">
          <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="background: #10b981; color: #fff; border: none; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);">Get a Free Audit</a>
          <a href="#features" class="btn btn-outline btn-lg" style="border-color: rgba(255,255,255,0.2); color: #fff;">See Features</a>
        </div>
      </div>
      <div style="flex: 1; position: relative; min-width: 300px; display: flex; justify-content: center;">
        <!-- Browser Mockup -->
        <div style="background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); width: 100%; max-width: 500px; border: 1px solid rgba(255,255,255,0.1); transform: perspective(1000px) rotateY(-5deg) rotateX(2deg); transition: transform 0.3s ease;">
          <div style="background: #f1f5f9; padding: 12px; display: flex; gap: 6px; border-bottom: 1px solid #e2e8f0;">
            <div style="width: 12px; height: 12px; border-radius: 50%; background: #ef4444;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background: #eab308;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background: #22c55e;"></div>
          </div>
          <div style="padding: 0;">
            <img src="/images/hero-doctors.png" alt="Hospital Website Preview" style="width: 100%; display: block; border-bottom: 1px solid #f1f5f9;">
            <div style="padding: 24px; text-align: left;">
              <div style="width: 60%; height: 24px; background: #e2e8f0; border-radius: 4px; margin-bottom: 12px;"></div>
              <div style="width: 100%; height: 12px; background: #f1f5f9; border-radius: 4px; margin-bottom: 8px;"></div>
              <div style="width: 80%; height: 12px; background: #f1f5f9; border-radius: 4px;"></div>
            </div>
          </div>
        </div>
        
        <!-- Floating SEO Badge -->
        <div style="position: absolute; bottom: -20px; left: -20px; background: #fff; padding: 16px 24px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); border: 1px solid #e5e7eb; display: flex; align-items: center; gap: 16px; transform: translateZ(20px);">
          <div style="width: 48px; height: 48px; background: rgba(16, 185, 129, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #10b981;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
          </div>
          <div style="text-align: left;">
            <div style="font-size: 1.25rem; font-weight: 800; color: #111;">#1</div>
            <div style="font-size: 0.85rem; color: #64748b; font-weight: 600;">Google Ranking</div>
          </div>
        </div>
      </div>
    </div>
  </section>"""
    
    # Replace the old hero
    content = re.sub(r'<!-- Hero Section -->.*?</section>', new_hero, content, flags=re.DOTALL)
    
    # Add id features for smooth scroll
    content = content.replace('<section class="dp-sections">', '<section class="dp-sections" id="features">')

    with open(file_path, 'w') as f:
        f.write(content)


def update_voimai():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/voimai/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    new_css = """
    /* Voimai Visualizer Styles */
    .voim-visualizer {
      margin: 40px auto;
      max-width: 400px;
      background: rgba(15, 22, 35, 0.6);
      border: 1px solid rgba(16, 185, 129, 0.2);
      border-radius: 24px;
      padding: 32px;
      backdrop-filter: blur(10px);
      box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.05);
      position: relative;
    }
    .voim-profile {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background: linear-gradient(135deg, #10b981, #3b82f6);
      margin: 0 auto 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 30px rgba(16, 185, 129, 0.4);
      position: relative;
    }
    .voim-profile::after {
      content: '';
      position: absolute;
      top: -10px; left: -10px; right: -10px; bottom: -10px;
      border-radius: 50%;
      border: 2px solid rgba(16, 185, 129, 0.3);
      animation: pulse-ring 2s infinite cubic-bezier(0.215, 0.61, 0.355, 1);
    }
    @keyframes pulse-ring {
      0% { transform: scale(0.8); opacity: 0.5; }
      100% { transform: scale(1.5); opacity: 0; }
    }
    .voim-status {
      font-size: 0.9rem;
      color: #10b981;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }
    .status-dot {
      width: 8px;
      height: 8px;
      background: #10b981;
      border-radius: 50%;
      animation: blink 1s infinite alternate;
    }
    @keyframes blink {
      0% { opacity: 0.3; }
      100% { opacity: 1; }
    }
    .audio-waves {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      height: 60px;
      margin-bottom: 24px;
    }
    .wave-bar {
      width: 6px;
      background: #10b981;
      border-radius: 4px;
      animation: wave 1.2s infinite ease-in-out;
    }
    .wave-bar:nth-child(1) { height: 20px; animation-delay: 0.0s; }
    .wave-bar:nth-child(2) { height: 40px; animation-delay: 0.1s; }
    .wave-bar:nth-child(3) { height: 60px; animation-delay: 0.2s; }
    .wave-bar:nth-child(4) { height: 30px; animation-delay: 0.3s; }
    .wave-bar:nth-child(5) { height: 50px; animation-delay: 0.4s; }
    .wave-bar:nth-child(6) { height: 25px; animation-delay: 0.5s; }
    .wave-bar:nth-child(7) { height: 45px; animation-delay: 0.6s; }
    
    @keyframes wave {
      0%, 100% { transform: scaleY(0.5); opacity: 0.5; }
      50% { transform: scaleY(1); opacity: 1; }
    }
    
    .voim-transcript {
      background: rgba(0,0,0,0.3);
      border-radius: 12px;
      padding: 16px;
      text-align: left;
      font-size: 0.95rem;
      color: rgba(255,255,255,0.9);
      border: 1px solid rgba(255,255,255,0.05);
    }
    .transcript-role {
      font-weight: 700;
      color: #94a3b8;
      font-size: 0.75rem;
      text-transform: uppercase;
      margin-bottom: 4px;
    }
  </style>
</head>"""

    content = content.replace("  </style>\n</head>", new_css)
    
    new_hero = """  <!-- Hero Section -->
  <header class="voim-hero">
    <div class="container">
      <div style="display:inline-block; padding: 6px 16px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 100px; color: #10b981; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">ZenoHosp AI</div>
      <h1>The Front Desk Employee That<br><span>Never Sleeps.</span></h1>
      <p>Automate appointments, answer queries in 400+ languages, and follow up with patients automatically. Voim.ai is a conversational AI agent designed specifically for healthcare.</p>
      
      <!-- Interactive Voimai Visualizer -->
      <div class="voim-visualizer">
        <div class="voim-profile">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
        </div>
        <div class="voim-status"><div class="status-dot"></div> AI Agent Speaking...</div>
        <div class="audio-waves">
          <div class="wave-bar"></div>
          <div class="wave-bar"></div>
          <div class="wave-bar"></div>
          <div class="wave-bar"></div>
          <div class="wave-bar"></div>
          <div class="wave-bar"></div>
          <div class="wave-bar"></div>
        </div>
        <div class="voim-transcript">
          <div class="transcript-role">Voim.ai</div>
          <div>"Hello! This is ZenoHosp. I see you'd like to book an appointment with Dr. Reddy. Is tomorrow at 10:00 AM suitable for you?"</div>
        </div>
      </div>
      
      <div style="margin-top: 40px;">
        <a href="/contact-us/index.html" class="btn btn-primary btn-lg" style="box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3);">Schedule AI Demo</a>
      </div>
    </div>
  </header>"""

    content = re.sub(r'<!-- Hero Section -->.*?</header>', new_hero, content, flags=re.DOTALL)

    with open(file_path, 'w') as f:
        f.write(content)


def update_homepage():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    new_css = """
  .ecosystem-section {
    padding: 100px 0;
    background: #0a0a08;
    color: #fff;
    border-top: 1px solid rgba(255,255,255,0.05);
  }
  .ecosystem-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 32px;
    margin-top: 60px;
  }
  .eco-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 40px;
    transition: all 0.3s ease;
    text-decoration: none;
    color: #fff;
    display: flex;
    flex-direction: column;
    height: 100%;
    position: relative;
    overflow: hidden;
  }
  .eco-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at top right, var(--eco-color), transparent 70%);
    opacity: 0;
    transition: opacity 0.4s ease;
    z-index: 0;
  }
  .eco-card:hover {
    transform: translateY(-8px);
    border-color: rgba(255,255,255,0.2);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
  }
  .eco-card:hover::before {
    opacity: 0.15;
  }
  .eco-content {
    position: relative;
    z-index: 1;
    flex: 1;
  }
  .eco-icon {
    width: 60px;
    height: 60px;
    background: rgba(255,255,255,0.05);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
    color: var(--eco-color);
    transition: all 0.3s ease;
  }
  .eco-card:hover .eco-icon {
    background: var(--eco-color);
    color: #fff;
    transform: scale(1.1);
  }
  .eco-card h3 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 12px;
  }
  .eco-card p {
    color: #9ca3af;
    line-height: 1.6;
    margin-bottom: 24px;
  }
  .eco-link {
    margin-top: auto;
    font-weight: 600;
    color: var(--eco-color);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .eco-link svg {
    transition: transform 0.3s ease;
  }
  .eco-card:hover .eco-link svg {
    transform: translateX(5px);
  }
</style>
"""
    content = content.replace("</style>", new_css)
    
    new_section = """
  <!-- Services Ecosystem Section -->
  <section class="ecosystem-section">
    <div class="container">
      <div style="text-align: center; max-width: 800px; margin: 0 auto;">
        <div style="display:inline-block; padding: 6px 16px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 100px; color: #10b981; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">ZenoHosp Digital Services</div>
        <h2 style="font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 800; margin-bottom: 24px; line-height: 1.1;">End-to-End Hospital<br><span style="color: #10b981;">Growth Engine</span></h2>
        <p style="font-size: 1.2rem; color: #9ca3af;">Beyond software, we provide the elite digital infrastructure your hospital needs to attract patients, build authority, and scale revenue.</p>
      </div>

      <div class="ecosystem-grid">
        <!-- Websites -->
        <a href="/services/digital-presence/index.html" class="eco-card" style="--eco-color: #10b981;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            </div>
            <h3>Hospital Websites</h3>
            <p>Premium, high-speed websites with local SEO optimization to dominate Google searches.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>

        <!-- Custom Software -->
        <a href="/services/custom-software/index.html" class="eco-card" style="--eco-color: #f97316;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>
            </div>
            <h3>Custom Software</h3>
            <p>Bespoke medical modules, patient portals, and integrations tailored to your workflows.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>

        <!-- Social Media -->
        <a href="/services/social-media/index.html" class="eco-card" style="--eco-color: #a855f7;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
            </div>
            <h3>Social Media</h3>
            <p>Viral, highly professional content and reels that position your doctors as thought leaders.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>

        <!-- Advertising -->
        <a href="/services/advertising/index.html" class="eco-card" style="--eco-color: #3b82f6;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            </div>
            <h3>Healthcare Ads</h3>
            <p>Targeted Google and Meta ad campaigns that drive high-intent patients to your OPD.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>
        
        <!-- Voim.ai -->
        <a href="/services/voimai/index.html" class="eco-card" style="--eco-color: #ec4899;">
          <div class="eco-content">
            <div class="eco-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
            </div>
            <h3>Voim.ai Agent</h3>
            <p>AI-powered voice receptionist that handles calls, schedules appointments, and follows up automatically.</p>
          </div>
          <div class="eco-link">Learn More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
        </a>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->"""

    # Insert before FAQ section
    content = content.replace("  <!-- FAQ Section -->", new_section)

    with open(file_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    update_digital_presence()
    update_voimai()
    update_homepage()
    print("Done")
