import os

def insert_calculator():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/voimai/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    css_to_add = """
  /* ROI Calculator Styles */
  .roi-section {
    padding: 80px 0;
    background: #0a0a08;
    border-top: 1px solid rgba(255,255,255,0.05);
  }
  .roi-container {
    max-width: 900px;
    margin: 0 auto;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 48px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    display: flex;
    flex-direction: column;
    gap: 40px;
  }
  @media(min-width: 768px) {
    .roi-container {
      flex-direction: row;
      align-items: stretch;
    }
  }
  .roi-inputs {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }
  .roi-outputs {
    flex: 1;
    background: rgba(0,0,0,0.3);
    border-radius: 16px;
    padding: 32px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    border: 1px solid rgba(255,255,255,0.05);
  }
  .slider-group {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .slider-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .slider-header label {
    color: #fff;
    font-weight: 600;
    font-size: 1.1rem;
  }
  .slider-header .slider-val {
    color: #10b981;
    font-weight: 700;
    font-size: 1.2rem;
  }
  input[type=range] {
    -webkit-appearance: none;
    width: 100%;
    background: transparent;
  }
  input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
    height: 24px;
    width: 24px;
    border-radius: 50%;
    background: #10b981;
    cursor: pointer;
    margin-top: -10px;
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
  }
  input[type=range]::-webkit-slider-runnable-track {
    width: 100%;
    height: 6px;
    cursor: pointer;
    background: rgba(255,255,255,0.1);
    border-radius: 3px;
  }
  input[type=range]:focus {
    outline: none;
  }
  .output-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 16px;
    border-bottom: 1px dashed rgba(255,255,255,0.1);
  }
  .output-row:last-child {
    border-bottom: none;
    padding-bottom: 0;
    margin-top: auto;
  }
  .output-label {
    color: #9ca3af;
    font-size: 1rem;
  }
  .output-val {
    color: #fff;
    font-size: 1.2rem;
    font-weight: 600;
  }
  .output-savings .output-val {
    color: #10b981;
    font-size: 2.2rem;
    font-weight: 800;
  }
  .output-savings .output-label {
    color: #fff;
    font-weight: 600;
    font-size: 1.1rem;
  }
</style>
"""

    html_to_add = """
  <!-- ROI Calculator Section -->
  <section class="roi-section">
    <div class="container">
      <div style="text-align: center; margin-bottom: 48px;">
        <div style="display:inline-block; padding: 6px 16px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 100px; color: #10b981; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 16px;">Interactive Demo</div>
        <h2 style="font-size: clamp(2rem, 3vw, 2.5rem); font-weight: 800; color: #fff; margin-bottom: 16px;">Calculate Your Savings</h2>
        <p style="color: #9ca3af; max-width: 600px; margin: 0 auto; font-size: 1.1rem;">See exactly how much money your hospital saves every single month by switching to Voim.ai.</p>
      </div>
      
      <div class="roi-container">
        <!-- Inputs -->
        <div class="roi-inputs">
          <div class="slider-group">
            <div class="slider-header">
              <label for="receptionists">Number of Receptionists</label>
              <span class="slider-val" id="val-receptionists">3</span>
            </div>
            <input type="range" id="receptionists" min="1" max="15" value="3">
          </div>
          
          <div class="slider-group">
            <div class="slider-header">
              <label for="salary">Avg. Monthly Salary (₹)</label>
              <span class="slider-val" id="val-salary">₹20,000</span>
            </div>
            <input type="range" id="salary" min="10000" max="50000" step="1000" value="20000">
          </div>
          
          <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2); padding: 16px; border-radius: 12px; display: flex; align-items: flex-start; gap: 12px; margin-top: auto;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" style="flex-shrink: 0;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem; margin: 0;">Human receptionists take breaks, sleep, and miss calls during peak hours. Voim.ai is available 24/7/365.</p>
          </div>
        </div>
        
        <!-- Outputs -->
        <div class="roi-outputs">
          <div class="output-row">
            <span class="output-label">Current Monthly Cost</span>
            <span class="output-val" id="out-current">₹60,000</span>
          </div>
          <div class="output-row">
            <span class="output-label">Voim.ai Flat Cost</span>
            <span class="output-val" style="color: #9ca3af;">₹15,000</span>
          </div>
          <div class="output-row output-savings" style="margin-top: 24px; padding-top: 24px; border-top: 1px solid rgba(16, 185, 129, 0.3);">
            <div style="display: flex; flex-direction: column;">
              <span class="output-label">Net Monthly Savings</span>
              <span style="font-size: 0.85rem; color: #9ca3af; margin-top: 4px;">Direct impact to your bottom line</span>
            </div>
            <span class="output-val" id="out-savings">₹45,000</span>
          </div>
          
          <a href="/contact-us/index.html" class="btn btn-primary" style="margin-top: 24px; width: 100%; text-align: center; background: #fff; color: #111; font-weight: 700; border: none;">Claim Your Savings Now</a>
        </div>
      </div>
    </div>
  </section>
"""
    
    js_to_add = """
  <!-- ROI Calculator Logic -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const elRec = document.getElementById('receptionists');
      const elSal = document.getElementById('salary');
      const valRec = document.getElementById('val-receptionists');
      const valSal = document.getElementById('val-salary');
      
      const outCurrent = document.getElementById('out-current');
      const outSavings = document.getElementById('out-savings');
      
      const voimaiCost = 15000;
      
      function formatINR(number) {
        return '₹' + new Intl.NumberFormat('en-IN').format(number);
      }
      
      function calculateROI() {
        const rec = parseInt(elRec.value);
        const sal = parseInt(elSal.value);
        
        valRec.innerText = rec;
        valSal.innerText = formatINR(sal);
        
        const currentCost = rec * sal;
        outCurrent.innerText = formatINR(currentCost);
        
        const savings = Math.max(0, currentCost - voimaiCost);
        outSavings.innerText = formatINR(savings);
      }
      
      elRec.addEventListener('input', calculateROI);
      elSal.addEventListener('input', calculateROI);
    });
  </script>
</body>
"""

    if "<!-- ROI Calculator Section -->" not in content:
        # Insert CSS
        content = content.replace("</style>", css_to_add)
        
        # Insert HTML before FAQ Section
        if "<!-- FAQ Section -->" in content:
             content = content.replace("  <!-- FAQ Section -->", html_to_add + "\n  <!-- FAQ Section -->")
        else:
             print("Could not find FAQ section to insert before")
             
        # Insert JS before </body>
        content = content.replace("</body>", js_to_add)
        
        with open(file_path, 'w') as f:
            f.write(content)
        print("Done")
    else:
        print("Calculator already exists.")

if __name__ == "__main__":
    insert_calculator()
