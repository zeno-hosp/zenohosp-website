class DemoModal extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <div class="demo-modal-overlay" style="display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.6); backdrop-filter: blur(4px); z-index: 9999; justify-content: center; align-items: center; overflow-y: auto; padding: 20px;">
        <div class="demo-modal-content" style="background: white; border-radius: 20px; padding: 40px; max-width: 600px; width: 100%; position: relative; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);">
          
          <button class="demo-modal-close" aria-label="Close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; cursor: pointer; color: #666; padding: 8px;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>

          <div class="contact-form-card" style="box-shadow: none; padding: 0; background: transparent; border: none;">
            <h3 style="margin-top: 0;">Request a Live Demo</h3>
            <p>Tell us about your hospital and we'll personalise the demo for you.</p>

            <form action="https://formspree.io/f/xwvjzvnd" method="POST" style="margin-top: 24px;">
              <div class="form-grid">
                <div class="form-group">
                  <label for="modal-firstName">First Name *</label>
                  <input type="text" id="modal-firstName" name="firstName" required placeholder="Rajesh">
                </div>
                <div class="form-group">
                  <label for="modal-lastName">Last Name *</label>
                  <input type="text" id="modal-lastName" name="lastName" required placeholder="Kumar">
                </div>
                <div class="form-group">
                  <label for="modal-email">Work Email *</label>
                  <input type="email" id="modal-email" name="email" required placeholder="rajesh@hospital.com">
                </div>
                <div class="form-group">
                  <label for="modal-phone">Phone / WhatsApp *</label>
                  <input type="tel" id="modal-phone" name="phone" required placeholder="+91 98765 43210">
                </div>
                <div class="form-group full-width">
                  <label for="modal-hospital">Hospital / Clinic Name *</label>
                  <input type="text" id="modal-hospital" name="hospital" required placeholder="Lakshmi Hospital">
                </div>
                <div class="form-group">
                  <label for="modal-size">Facility Size</label>
                  <select id="modal-size" name="size">
                    <option value="">Select bed count / scale</option>
                    <option value="clinic">Clinic / Polyclinic (no beds)</option>
                    <option value="1-50">1–50 beds</option>
                    <option value="51-100">51–100 beds</option>
                    <option value="101-250">101–250 beds</option>
                    <option value="251-500">251–500 beds</option>
                    <option value="75+">75+ beds</option>
                  </select>
                </div>
                <div class="form-group full-width">
                  <label for="modal-interest">Modules I'm most interested in</label>
                  <select id="modal-interest" name="interest">
                    <option value="all">Complete Suite — all modules</option>
                    <option value="hms">HMS — Patient management & EMR</option>
                    <option value="ot">OT Room — Operation theatre scheduling</option>
                    <option value="pharmacy">Pharmacy — Dispensing & billing</option>
                    <option value="inventory">Inventory — Stock & supply chain</option>
                    <option value="finance">Finance — Billing, GST & insurance</option>
                    <option value="lab">Lab — LIS & analyser integration</option>
                    <option value="people">People — HR, roster & payroll</option>
                    <option value="asset">Asset — Equipment lifecycle</option>
                  </select>
                </div>
              </div>

              <div class="form-submit" style="margin-top: 32px;">
                <button type="submit" class="btn btn-primary" style="width: 100%;">Schedule My Demo →</button>
              </div>
              <div class="form-trust" style="justify-content: center; margin-top: 16px;">
                <span>No commitment required</span>
                <span>No spam, ever</span>
              </div>
            </form>
          </div>
        </div>
      </div>
    `;

    // Event listeners
    const overlay = this.querySelector('.demo-modal-overlay');
    const closeBtn = this.querySelector('.demo-modal-close');
    const modalContent = this.querySelector('.demo-modal-content');

    closeBtn.addEventListener('click', () => this.close());
    
    // Close on overlay click
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        this.close();
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.close();
      }
    });
  }

  open() {
    const overlay = this.querySelector('.demo-modal-overlay');
    if (overlay) {
      overlay.style.display = 'flex';
      // Prevent body scrolling
      document.body.style.overflow = 'hidden';
    }
  }

  close() {
    const overlay = this.querySelector('.demo-modal-overlay');
    if (overlay) {
      overlay.style.display = 'none';
      // Restore body scrolling
      document.body.style.overflow = '';
    }
  }
}

customElements.define('demo-modal', DemoModal);
