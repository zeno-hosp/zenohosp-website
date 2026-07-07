import re
import sys

def redesign_voimai():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/voimai/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Inject Playfair Display
    if "Playfair+Display" not in content:
        font_link = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">'
        content = content.replace("</head>", f"  {font_link}\n</head>")
    
    # 2. Rewrite CSS Block
    # We will use regex to find the <style>...</style> block that contains body { background-color: #050a12;
    style_pattern = re.compile(r'<style>.*?body\s*\{.*?background-color:\s*#050a12;.*?</style>', re.DOTALL)
    
    new_style = """<style>
    body {
      background-color: #ffffff;
      color: #111827;
    }

    .voim-hero {
      padding: 160px 0 120px;
      text-align: center;
      position: relative;
      /* Mesh Gradient replicating the reference image */
      background-color: #011A5E;
      background-image: 
        radial-gradient(at 10% 0%, #00D4FF 0px, transparent 50%),
        radial-gradient(at 80% 0%, #0F4C81 0px, transparent 50%),
        radial-gradient(at 90% 90%, #6DD5FA 0px, transparent 50%),
        radial-gradient(at 0% 100%, #003B94 0px, transparent 50%);
      background-size: cover;
      color: #ffffff;
      border-radius: 0 0 40px 40px;
      margin: 10px;
      overflow: hidden;
      box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    .hero-pretitle {
      font-size: 0.85rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      font-weight: 600;
      color: rgba(255,255,255,0.8);
      margin-bottom: 24px;
      display: block;
    }

    .voim-hero h1 {
      font-family: 'Playfair Display', serif;
      font-size: clamp(3rem, 6vw, 5.5rem);
      font-weight: 500;
      color: #fff;
      letter-spacing: -0.02em;
      margin-bottom: 40px;
      line-height: 1.05;
      max-width: 900px;
      margin-left: auto;
      margin-right: auto;
    }

    .hero-cta {
      display: inline-flex;
      align-items: center;
      gap: 16px;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 100px;
      padding: 8px 8px 8px 32px;
      color: #fff;
      text-decoration: none;
      font-weight: 500;
      font-size: 1.1rem;
      transition: all 0.3s ease;
    }
    .hero-cta:hover {
      background: rgba(255, 255, 255, 0.2);
      transform: translateY(-2px);
    }
    
    .cta-orb {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: linear-gradient(135deg, #00D4FF, #a855f7, #ffffff);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
    }

    /* Rest of the page adapting to light mode */
    .voim-features {
      padding: 100px 0;
      background: #ffffff;
    }
    
    .voim-features h2 {
      color: #111827 !important;
    }

    .voim-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 32px;
    }
    .v-card {
      background: #ffffff;
      border: 1px solid rgba(0,0,0,0.05);
      border-radius: 16px;
      padding: 40px;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
      box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .v-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 100%; height: 4px;
      background: linear-gradient(90deg, #0ea5e9, #2563eb);
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .v-card:hover {
      box-shadow: 0 20px 40px rgba(0,0,0,0.08);
      transform: translateY(-4px);
    }
    .v-card:hover::before { opacity: 1; }
    .v-icon {
      width: 56px;
      height: 56px;
      background: rgba(37, 99, 235, 0.1);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 24px;
      color: #2563eb;
    }
    .v-card h3 {
      font-size: 1.4rem;
      font-weight: 700;
      color: #111827;
      margin-bottom: 16px;
    }
    .v-card p {
      color: #64748b;
      line-height: 1.6;
      font-size: 1.05rem;
    }
    .voim-stats {
      background: #f8fafc;
      border-top: 1px solid rgba(0,0,0,0.05);
      border-bottom: 1px solid rgba(0,0,0,0.05);
      padding: 60px 0;
    }
    .stats-container {
      display: flex;
      justify-content: space-around;
      text-align: center;
      flex-wrap: wrap;
      gap: 32px;
    }
    .stat-item h4 {
      font-size: 3rem;
      font-weight: 800;
      color: #111827;
      margin-bottom: 8px;
    }
    .stat-item p {
      font-size: 1.1rem;
      color: #2563eb;
      font-weight: 600;
    }
    .cta-banner {
      background: linear-gradient(135deg, #0ea5e9, #2563eb, #1e3a8a);
      padding: 80px 0;
      text-align: center;
      color: #fff;
    }
    .cta-banner h2 { font-size: 3rem; font-weight: 800; margin-bottom: 24px; }
    @media (max-width: 768px) {
      .voim-grid { grid-template-columns: 1fr; }
    }
  
    /* SEO Sections CSS */
    .seo-section { padding: 80px 0; background: #ffffff; border-top: 1px solid rgba(0,0,0,0.05); }
    .seo-section.alt-bg { background: #f8fafc; }
    .seo-header { text-align: center; margin-bottom: 48px; max-width: 800px; margin-left: auto; margin-right: auto; }
    .seo-header h2 { font-size: 2.5rem; font-weight: 800; color: #111827; margin-bottom: 16px; }
    .seo-header p { font-size: 1.15rem; color: #64748b; line-height: 1.6; }
    
    .usecase-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 40px; }
    .usecase-card { background: #ffffff; border: 1px solid rgba(0,0,0,0.05); padding: 40px; border-radius: 16px; position: relative; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
    .usecase-card::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #0ea5e9, #2563eb); }
    .usecase-card h3 { font-size: 1.5rem; font-weight: 700; color: #111827; margin-bottom: 24px; display: flex; align-items: center; gap: 12px; }
    .usecase-card ul { list-style: none; padding: 0; }
    .usecase-card li { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 16px; color: #64748b; line-height: 1.6; }
    .usecase-card li svg { color: #2563eb; flex-shrink: 0; margin-top: 4px; }
    
    .bottleneck-box { background: linear-gradient(145deg, #f8fafc, #ffffff); border: 1px solid rgba(37, 99, 235, 0.2); border-radius: 16px; padding: 48px; text-align: center; margin-top: 40px; }
    .bottleneck-box h3 { font-size: 2rem; color: #111827; margin-bottom: 16px; }
    .bottleneck-box p { font-size: 1.1rem; color: #64748b; max-width: 700px; margin: 0 auto; line-height: 1.6; }

    /* Fix ROI Calculator to Light mode */
    .roi-section {
        background: #f8fafc !important;
        border-top: 1px solid rgba(0,0,0,0.05) !important;
    }
    .roi-container {
        background: #ffffff !important;
        border: 1px solid rgba(0,0,0,0.08) !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.05) !important;
    }
    .roi-outputs {
        background: #f8fafc !important;
        border: 1px solid rgba(0,0,0,0.05) !important;
    }
    .slider-header label {
        color: #111827 !important;
    }
    .slider-header .slider-val {
        color: #2563eb !important;
    }
    input[type=range]::-webkit-slider-thumb {
        background: #2563eb !important;
        box-shadow: 0 0 10px rgba(37, 99, 235, 0.5) !important;
    }
    input[type=range]::-webkit-slider-runnable-track {
        background: rgba(0,0,0,0.1) !important;
    }
    .output-label {
        color: #64748b !important;
    }
    .output-val {
        color: #111827 !important;
    }
    .output-savings .output-val {
        color: #2563eb !important;
    }
    .output-savings {
        border-top: 1px dashed rgba(0,0,0,0.1) !important;
    }
    .output-savings .output-label {
        color: #111827 !important;
    }
  </style>"""
    
    if style_pattern.search(content):
        content = style_pattern.sub(new_style, content)
    else:
        print("Could not find style block to replace")
        return

    # 3. Replace Hero Section HTML
    hero_pattern = re.compile(r'<section class="voim-hero">.*?</section>', re.DOTALL)
    
    new_hero = """<section class="voim-hero">
    <div class="container">
      <span class="hero-pretitle">#1 AI VOICE AGENT PLATFORM FOR AUTOMATING CALLS</span>
      <h1>Meet your AI call center<br>from the future.</h1>
      
      <div style="margin-top: 60px;">
        <a href="/contact-us/index.html" class="hero-cta">
          Try Our Live Demo
          <div class="cta-orb"></div>
        </a>
      </div>
      
      <div style="margin-top: 80px; display: flex; flex-direction: column; align-items: flex-start; text-align: left; max-width: 300px; margin-left: 20px;">
        <div style="display: flex; gap: 4px; margin-bottom: 8px;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="#fff" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="#fff" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="#fff" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="#fff" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="#fff" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          <span style="margin-left: 8px; font-weight: 600; font-size: 0.9rem;">4.8</span>
        </div>
        <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7); line-height: 1.5; margin:0;">Build, deploy, and manage next-generation AI voice agents that sound human, execute tasks, and scale effortlessly.</p>
      </div>
    </div>
  </section>"""
    
    if hero_pattern.search(content):
        content = hero_pattern.sub(new_hero, content)
    else:
        print("Could not find hero block to replace")
        return
        
    with open(file_path, 'w') as f:
        f.write(content)
    
    print("Success")

if __name__ == "__main__":
    redesign_voimai()
