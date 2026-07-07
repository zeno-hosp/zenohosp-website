import os

def add_pain_points():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/voimai/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    css_to_add = """
    /* Pain Points Section */
    .pain-points {
      padding: 100px 0;
      background: #ffffff;
    }
    .pain-header {
      text-align: center;
      max-width: 800px;
      margin: 0 auto 60px;
    }
    .pain-header h2 {
      font-size: 2.5rem;
      font-weight: 800;
      color: #111827;
      margin-bottom: 16px;
    }
    .pain-header p {
      font-size: 1.15rem;
      color: #64748b;
      line-height: 1.6;
    }
    .pain-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 32px;
    }
    .pain-card {
      background: #f8fafc;
      border: 1px solid rgba(0,0,0,0.05);
      border-radius: 16px;
      padding: 40px;
      text-align: left;
    }
    .pain-icon {
      width: 48px;
      height: 48px;
      background: rgba(239, 68, 68, 0.1);
      color: #ef4444;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 24px;
    }
    .pain-card h3 {
      font-size: 1.3rem;
      font-weight: 700;
      color: #111827;
      margin-bottom: 12px;
    }
    .pain-card p {
      color: #64748b;
      line-height: 1.6;
      font-size: 1rem;
    }
    @media (max-width: 768px) {
      .pain-grid { grid-template-columns: 1fr; }
    }
"""

    html_to_add = """
  <!-- Pain Points Section -->
  <section class="pain-points">
    <div class="container">
      <div class="pain-header">
        <div style="display:inline-block; padding: 6px 16px; background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 100px; color: #ef4444; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 16px;">The Problem</div>
        <h2>The High Cost of Traditional Reception</h2>
        <p>Hospitals lose thousands of dollars daily due to overwhelmed front desks and inefficient call handling. Here is what happens without Voim.ai.</p>
      </div>
      
      <div class="pain-grid">
        <div class="pain-card">
          <div class="pain-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path><line x1="22" y1="2" x2="2" y2="22"></line></svg>
          </div>
          <h3>Missed Appointments</h3>
          <p>Peak hour call volumes inevitably lead to long hold times. Frustrated patients hang up and book appointments with competing clinics.</p>
        </div>
        <div class="pain-card">
          <div class="pain-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="20" y1="8" x2="20" y2="14"></line><line x1="23" y1="11" x2="17" y2="11"></line></svg>
          </div>
          <h3>Staff Burnout</h3>
          <p>Your highly-paid receptionists spend 80% of their day answering the exact same repetitive queries about hospital timings, locations, and insurance.</p>
        </div>
        <div class="pain-card">
          <div class="pain-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><line x1="9" y1="12" x2="15" y2="12"></line></svg>
          </div>
          <h3>Ignored Follow-ups</h3>
          <p>Crucial post-discharge checkup calls are rarely made due to lack of human bandwidth, massively increasing patient readmission risks.</p>
        </div>
      </div>
    </div>
  </section>
"""

    if "<!-- Pain Points Section -->" not in content:
        # Insert CSS
        content = content.replace("</style>", css_to_add + "\n  </style>")
        
        # Insert HTML before Features Grid
        target = "<!-- Features Grid Section -->"
        if target in content:
             content = content.replace(target, html_to_add + "\n  " + target)
        else:
             print("Could not find target to insert before")
             return
             
        with open(file_path, 'w') as f:
            f.write(content)
        print("Done")
    else:
        print("Section already exists.")

if __name__ == "__main__":
    add_pain_points()
