import os

def fix_social_media_page():
    base_dir = "/Users/iniyananbu/Documents/ZenoHosp Website"
    social_file = os.path.join(base_dir, "services/social-media/index.html")
    index_file = os.path.join(base_dir, "index.html")
    
    # Read index.html for standard head and nav
    with open(index_file, "r") as f:
        index_content = f.read()
        
    start_str = '<!DOCTYPE html>'
    end_str = '  <!-- Hero Section -->'
    
    head_and_nav = index_content.split(end_str)[0]
    
    # We need to change the title, meta description in head_and_nav
    # It currently has index.html's meta.
    # Let's replace the title and meta manually.
    title_start = '<title>'
    title_end = '</title>'
    head_and_nav = head_and_nav.replace(
        head_and_nav[head_and_nav.find(title_start):head_and_nav.find(title_end)+len(title_end)],
        '<title>Hospital Social Media & Video Management | ZenoHosp Services</title>'
    )
    
    meta_desc_start = '<meta name="description" content="'
    meta_desc_end = '">'
    # Using regex or just split
    parts = head_and_nav.split('<meta name="description" content="')
    if len(parts) > 1:
        rest = parts[1].split('">', 1)
        head_and_nav = parts[0] + '<meta name="description" content="ZenoHosp handles hospital social media content, including professional video shoots and editing through our exclusive tie-up with Zesignworks.">' + rest[1]
        
    # Inject CSS before </style>
    new_css = """
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
"""
    head_and_nav = head_and_nav.replace('</style>', new_css + '\n  </style>')
    
    # Now read the broken social_file to extract the new body
    # From <!-- Hero Section --> down to the end.
    with open(social_file, "r") as f:
        broken_content = f.read()
        
    body_content = '  <!-- Hero Section -->' + broken_content.split('  <!-- Hero Section -->')[1]
    
    final_content = head_and_nav + body_content
    with open(social_file, "w") as f:
        f.write(final_content)
        
    print("Fixed social media page!")

if __name__ == "__main__":
    fix_social_media_page()
