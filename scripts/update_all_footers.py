import os
import glob

OLD_FOOTER = """        <div class="footer-links">
          <h4>Solutions</h4>
          <ul>
            <li><a href="/apps/hms/index.html">Hospital Management</a></li>
            <li><a href="/apps/ot-room/index.html">Operation Theatre</a></li>
            <li><a href="/apps/pharmacy/index.html">Pharmacy</a></li>
            <li><a href="/apps/inventory/index.html">Inventory</a></li>
            <li><a href="/apps/asset/index.html">Asset Management</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Company</h4>
          <ul>
            <li><a href="/about-us/index.html">About Us</a></li>
            <li><a href="/careers/index.html">Careers</a></li>
            <li><a href="/blog/index.html">Blog</a></li>
            <li><a href="/contact-us/index.html">Contact Us</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Support</h4>
          <ul>
            <li><a href="/help/index.html">Help Center</a></li>
            <li><a href="/help/index.html">Documentation</a></li>
            <li><a href="#">API Reference</a></li>
            <li><a href="/status/index.html">Status</a></li>
          </ul>
        </div>"""

NEW_FOOTER = """        <div class="footer-links">
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
            <li><a href="/careers/index.html">Careers</a></li>
            <li><a href="/blog/index.html">Blog</a></li>
            <li><a href="/contact-us/index.html">Contact Us</a></li>
          </ul>
          <h4 style="margin-top: 24px;">Compare</h4>
          <ul>
            <li><a href="/compare/zenohosp-vs-adrine/index.html">vs Adrine</a></li>
            <li><a href="/compare/zenohosp-vs-nuvertos/index.html">vs NuvertOS</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Support</h4>
          <ul>
            <li><a href="/help/index.html">Help Center</a></li>
            <li><a href="/help/index.html">Documentation</a></li>
            <li><a href="#">API Reference</a></li>
            <li><a href="/status/index.html">Status</a></li>
          </ul>
        </div>"""

def update_footers(directory):
    count = 0
    # Use glob to find all html files recursively
    for filepath in glob.glob(os.path.join(directory, '**/*.html'), recursive=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if OLD_FOOTER in content:
                content = content.replace(OLD_FOOTER, NEW_FOOTER)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Updated footer in: {filepath}")
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            
    print(f"\\nSuccessfully updated {count} files.")

if __name__ == '__main__':
    update_footers('/Users/iniyananbu/Documents/Zeno Hosp Website')
