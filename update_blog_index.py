import os

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
index_file = os.path.join(directory, 'blog', 'index.html')

with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_cards = """
        <a href="/blog/hospital-inventory-management-2026.html" class="blog-card">
          <div class="blog-card-header">
            <span class="blog-cat-tag cat-operations">Operations</span>
            <span class="blog-read-time">9 min</span>
          </div>
          <div class="blog-card-body">
            <h3>The Ultimate Guide to Hospital Inventory Management in 2026</h3>
            <p>Learn how modern hospital inventory management software prevents stockouts, reduces expiry wastage with FEFO, and automates supply chain purchasing.</p>
            <div class="blog-card-footer">
              <span class="blog-date">June 2026</span>
              <span class="blog-arrow">→</span>
            </div>
          </div>
        </a>

        <a href="/blog/cloud-vs-legacy-hms.html" class="blog-card">
          <div class="blog-card-header">
            <span class="blog-cat-tag cat-technology">Technology</span>
            <span class="blog-read-time">7 min</span>
          </div>
          <div class="blog-card-body">
            <h3>Why Cloud-Based HMS is Replacing Legacy Systems in Indian Hospitals</h3>
            <p>Compare the hidden costs of legacy on-premise hospital management software with modern, secure, and scalable cloud-based HMS solutions.</p>
            <div class="blog-card-footer">
              <span class="blog-date">June 2026</span>
              <span class="blog-arrow">→</span>
            </div>
          </div>
        </a>

        <a href="/blog/stop-revenue-leakage-ipd.html" class="blog-card">
          <div class="blog-card-header">
            <span class="blog-cat-tag cat-finance">Finance</span>
            <span class="blog-read-time">6 min</span>
          </div>
          <div class="blog-card-body">
            <h3>Maximizing Hospital Revenue: How to Stop Billing Leakage in IPD</h3>
            <p>Discover actionable strategies to prevent unbilled procedures, optimize IPD billing software, and maximize revenue cycle management in hospitals.</p>
            <div class="blog-card-footer">
              <span class="blog-date">June 2026</span>
              <span class="blog-arrow">→</span>
            </div>
          </div>
        </a>
"""

if "hospital-inventory-management-2026.html" not in content:
    content = content.replace('<div class="blog-grid">', '<div class="blog-grid">\n' + new_cards)
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated blog/index.html")
else:
    print("Already updated.")
