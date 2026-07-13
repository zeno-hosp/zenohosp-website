class ZenoFooter extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
<footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/index.html" class="logo">
            <img src="/images/zenohosp-w.svg" alt="ZenoHosp Logo" style="height: 32px; width: auto; display: block;" />
          </a>
          <p>Hospital software built in Chennai, used by 75+ facilities across India.</p>
          <div class="social-links">
            <a href="https://www.linkedin.com/company/zenohosp" target="_blank" rel="noopener" aria-label="LinkedIn" class="social-li"><svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
            <a href="https://x.com/zenohosp" target="_blank" rel="noopener" aria-label="Twitter" class="social-tw"><svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
            <a href="https://www.instagram.com/zenohosp/" target="_blank" rel="noopener" aria-label="Instagram" class="social-ig"><svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
            <a href="mailto:hi@zenohosp.com" aria-label="Email" class="social-em"><svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></a>
          </div>
        </div>

        <div class="footer-links">
          <h4>Solutions</h4>
          <ul>
            <li><a href="/apps/hms/index.html">Hospital Management</a></li>
            <li><a href="/apps/ot-room/index.html">Operation Theatre</a></li>
            <li><a href="/apps/pharmacy/index.html">Pharmacy</a></li>
            <li><a href="/apps/inventory/index.html">Inventory</a></li>
            <li><a href="/apps/asset/index.html">Asset Management</a></li>
            <li><a href="/solutions/abdm-compliance/index.html">ABDM Compliance</a></li>
          </ul>
        </div>

        <div class="footer-links">
          <h4>Company</h4>
          <ul>
            <li><a href="/about-us/index.html">About Us</a></li>
            <li><a href="/services/index.html">Services</a></li>
            <li><a href="/careers/index.html">Careers</a></li>
            <li><a href="/blog/index.html">Blog</a></li>
            <li><a href="/contact-us/index.html">Contact Us</a></li>
          </ul>
          <h4 style="margin-top: 24px;">For You</h4>
          <ul>
            <li><a href="/for-doctors/index.html">For Doctors</a></li>
            <li><a href="/for-founders/index.html">For Founders</a></li>
            <li><a href="/india/index.html">Built for India</a></li>
          </ul>
        </div>

        <div class="footer-links">
          <h4>Compare</h4>
          <ul>
            <li><a href="/resources/best-hospital-management-software-india-2026.html">Best HMS in India 2026</a></li>
            <li><a href="/compare/zenohosp-vs-adrine/index.html">vs Adrine</a></li>
            <li><a href="/compare/zenohosp-vs-nuvertos/index.html">vs NuvertOS</a></li>
            <li><a href="/compare/zenohosp-vs-ehospital/index.html">vs eHospital</a></li>
            <li><a href="/compare/zenohosp-vs-instahms/index.html">vs Insta HMS</a></li>
            <li><a href="/compare/zenohosp-vs-attune/index.html">vs Attune</a></li>
          </ul>
          <h4 style="margin-top: 24px;">Case Studies</h4>
          <ul>
            <li><a href="/customers/dss-multispeciality/index.html">DSS Multispeciality</a></li>
            <li><a href="/customers/lakshmi-hospital/index.html">Lakshmi Hospital</a></li>
            <li><a href="/customers/kedar-ent-hospital/index.html">Kedar ENT</a></li>
            <li><a href="/customers/city-general-hospital/index.html">City General</a></li>
          </ul>
        </div>

        <div class="footer-links">
          <h4>Support</h4>
          <ul>
            <li><a href="/help/index.html">Help Center</a></li>
            <li><a href="/help/index.html">Documentation</a></li>
            <li><a href="/status/index.html">Status</a></li>
          </ul>
          <h4 style="margin-top: 24px;">HMS by City</h4>
          <ul>
            <li><a href="/hms-software/mumbai/index.html">Mumbai</a></li>
            <li><a href="/hms-software/bengaluru/index.html">Bengaluru</a></li>
            <li><a href="/hms-software/hyderabad/index.html">Hyderabad</a></li>
            <li><a href="/hms-software/chennai/index.html">Chennai</a></li>
            <li><a href="/hms-software/coimbatore/index.html">Coimbatore</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Zeno Hosp. All rights reserved.</p>
        <div class="footer-legal">
          <a href="/privacy-policy/index.html">Privacy Policy</a>
          <a href="/terms-of-service/index.html">Terms of Service</a>
          <a href="/cookie-policy/index.html">Cookies</a>
        </div>
      </div>
    </div>
  </footer>
    `;
  }
}
customElements.define('zeno-footer', ZenoFooter);
