import os

def add_metrics_section():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/social-media/index.html"
    
    with open(file_path, "r") as f:
        content = f.read()

    metrics_css = """
    .metrics-section {
      background: #0a0a08;
      color: #fff;
      padding: 80px 0;
      border-top: 1px solid rgba(255,255,255,0.05);
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 40px;
      text-align: center;
    }
    .metric-item h3 {
      font-size: 3.5rem;
      font-weight: 800;
      background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 12px;
      line-height: 1;
    }
    .metric-item p {
      font-size: 1.1rem;
      color: rgba(255, 255, 255, 0.8);
      line-height: 1.6;
    }
    .metric-item span {
      display: block;
      font-size: 0.9rem;
      color: rgba(255,255,255,0.5);
      margin-top: 8px;
    }
    .metrics-cta {
      text-align: center;
      margin-top: 60px;
      padding-top: 40px;
      border-top: 1px solid rgba(255,255,255,0.1);
    }
    .metrics-cta h4 {
      font-size: 1.8rem;
      font-weight: 700;
      margin-bottom: 16px;
    }
    .metrics-cta p {
      color: rgba(255,255,255,0.7);
      font-size: 1.15rem;
      max-width: 700px;
      margin: 0 auto 32px;
    }
    @media (max-width: 768px) {
      .metrics-grid { grid-template-columns: 1fr; }
    }
    """
    
    # Inject CSS
    if ".metrics-section {" not in content:
        content = content.replace("</style>", metrics_css + "\n  </style>")

    metrics_html = """
  <!-- Trust & Metrics Section -->
  <section class="metrics-section">
    <div class="container">
      <div class="metrics-grid">
        <div class="metric-item">
          <h3>60+</h3>
          <p>Doctor Profiles Managed</p>
          <span>Improving OPD counts across Tamil Nadu, Kerala & Bangalore.</span>
        </div>
        <div class="metric-item">
          <h3>40+</h3>
          <p>Hospital Tie-ups</p>
          <span>Building visible, trusted brands in regional healthcare.</span>
        </div>
        <div class="metric-item">
          <h3>35%</h3>
          <p>Average Growth</p>
          <span>Increase in patient footfall via targeted digital marketing.</span>
        </div>
      </div>
      
      <div class="metrics-cta">
        <h4>Be The Next Success Story</h4>
        <p>Join 40+ hospitals who have entrusted us to improve their personal and hospital brand visibility. Increase your patient count and gain immense community trust.</p>
        <a href="/contact-us/index.html" class="btn btn-primary" style="background: #fff; color: #111; border: none; padding: 12px 32px; font-weight: 700; border-radius: 8px;">Improve Your Brand Today</a>
      </div>
    </div>
  </section>
"""

    if "<!-- Trust & Metrics Section -->" not in content:
        # Insert before Benefits Grid
        content = content.replace('  <!-- Benefits Grid -->', metrics_html + '\n  <!-- Benefits Grid -->')

    with open(file_path, "w") as f:
        f.write(content)
        
    print("Added metrics section!")

if __name__ == "__main__":
    add_metrics_section()
