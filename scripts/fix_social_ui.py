import os

def fix_social_media_ui():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/social-media/index.html"
    
    with open(file_path, "r") as f:
        content = f.read()

    # The required CSS block
    full_css = """
  <style>
    .dp-hero {
      background: #0a0a08;
      padding: 120px 0 80px;
      text-align: center;
      position: relative;
      overflow: hidden;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .dp-hero h1 {
      font-size: clamp(3rem, 5vw, 4.5rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: -.03em;
      margin-bottom: 24px;
      line-height: 1.1;
    }
    .dp-hero p {
      font-size: 1.25rem;
      color: rgba(255, 255, 255, 0.6);
      max-width: 700px;
      margin: 0 auto 40px;
      line-height: 1.6;
    }
    .dp-sections {
      padding: 100px 0;
      background: #fafafa;
    }
    .dp-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 40px;
      margin-bottom: 60px;
    }
    .feature-card {
      background: #fff;
      padding: 40px;
      border-radius: 16px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.02);
      border: 1px solid #e5e7eb;
    }
    .feature-card h3 {
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 16px;
      color: #111;
    }
    .feature-card p {
      color: #4b5563;
      line-height: 1.6;
      font-size: 1.05rem;
    }
    .feature-icon {
      width: 50px;
      height: 50px;
      background: rgba(168, 85, 247, 0.1);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 24px;
      color: #a855f7;
    }
    .process-section {
      padding: 80px 0;
      background: #fff;
      border-top: 1px solid #f3f4f6;
    }
    .process-flow {
      max-width: 800px;
      margin: 48px auto 0;
    }
    .process-step {
      display: flex;
      gap: 32px;
      margin-bottom: 40px;
      position: relative;
    }
    .process-step:not(:last-child)::before {
      content: '';
      position: absolute;
      left: 20px;
      top: 40px;
      bottom: -20px;
      width: 2px;
      background: #e5e7eb;
    }
    .step-number {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: #a855f7;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      flex-shrink: 0;
      z-index: 1;
    }
    .step-text h3 {
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 8px;
      color: #111;
    }
    .step-text p {
      color: #4b5563;
      line-height: 1.6;
    }
    @media (max-width: 768px) {
      .dp-grid { grid-template-columns: 1fr; }
      .process-step { flex-direction: column; gap: 16px; }
      .process-step:not(:last-child)::before { display: none; }
    }
    .cta-banner {
      background: #a855f7;
      padding: 80px 0;
      text-align: center;
      color: #fff;
    }
    .cta-banner h2 {
      font-size: 3rem;
      font-weight: 800;
      margin-bottom: 24px;
      letter-spacing: -0.03em;
    }
    .cta-banner p {
      font-size: 1.2rem;
      margin-bottom: 32px;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
      color: rgba(255,255,255,0.9);
    }
    
    /* Social Media Specific Additions */
    .social-mockup {
      background: #fff;
      border-radius: 20px;
      padding: 16px;
      width: 320px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.2);
      border: 1px solid rgba(255,255,255,0.1);
      transform: rotate(2deg);
      position: relative;
    }
    .social-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }
    .social-avatar {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: linear-gradient(45deg, #f09433, #dc2743, #bc1888);
      padding: 2px;
    }
    .social-avatar img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: #fff;
      object-fit: cover;
    }
    .social-name {
      font-weight: 700;
      color: #111;
      font-size: 0.95rem;
    }
    .social-loc {
      font-size: 0.75rem;
      color: #666;
    }
    .social-image {
      width: 100%;
      height: 320px;
      border-radius: 12px;
      background: #f3f4f6;
      margin-bottom: 16px;
      position: relative;
      overflow: hidden;
    }
    .social-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .play-btn {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 50px;
      height: 50px;
      background: rgba(255,255,255,0.9);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .social-actions {
      display: flex;
      gap: 16px;
      margin-bottom: 12px;
      color: #111;
    }
    .social-caption {
      font-size: 0.9rem;
      color: #111;
      line-height: 1.4;
    }
    .social-caption span {
      color: #00376b;
    }
    .regional-fonts {
      font-size: 1.25rem;
      font-weight: 600;
      color: #a855f7;
      margin-top: 12px;
      letter-spacing: 0.05em;
    }
    .doctor-pull-section {
      padding: 100px 0;
      background: #fff;
    }
    .doctor-pull-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }
    .doctor-pull-content h2 {
      font-size: 2.5rem;
      font-weight: 800;
      color: #111;
      margin-bottom: 24px;
      line-height: 1.2;
    }
    .doctor-pull-content p {
      font-size: 1.15rem;
      color: #4b5563;
      line-height: 1.7;
      margin-bottom: 20px;
    }
    .stat-box {
      background: #fafafa;
      border-left: 4px solid #a855f7;
      padding: 24px;
      border-radius: 0 12px 12px 0;
      margin-top: 32px;
    }
    .stat-box h4 {
      font-size: 1.2rem;
      color: #111;
      margin-bottom: 8px;
    }
    .roi-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 60px;
      border-top: 1px solid #e5e7eb;
      padding-top: 60px;
    }
    .roi-card { text-align: center; }
    .roi-card h3 { font-size: 3rem; color: #a855f7; font-weight: 800; margin-bottom: 8px; }
    .roi-card p { font-size: 1.1rem; color: #4b5563; font-weight: 600; }
    
    @media (max-width: 900px) {
      .doctor-pull-grid { grid-template-columns: 1fr; }
      .roi-grid { grid-template-columns: 1fr; }
    }
  </style>
"""

    if "<style>" in content:
        # Just to be safe, if there's an existing style block we replace it entirely.
        start = content.find("<style>")
        end = content.find("</style>") + len("</style>")
        if end > start:
            content = content[:start] + full_css + content[end:]
    else:
        # Insert before </head>
        content = content.replace("</head>", full_css + "\n</head>")

    with open(file_path, "w") as f:
        f.write(content)
        
    print("Fixed social media UI!")

if __name__ == "__main__":
    fix_social_media_ui()
