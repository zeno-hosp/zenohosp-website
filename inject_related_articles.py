import os
import re

related_html = """
      <div style="margin-top: 60px; padding-top: 40px; border-top: 1px solid var(--color-border);">
        <h3 style="margin-bottom: 20px;">Related Articles</h3>
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 10px;">→ <a href="/blog/top-10-hospital-management-software-india.html" style="color: var(--color-hms); text-decoration: none; font-weight: 500;">Top 10 Hospital Management Software in India (2026)</a></li>
          <li style="margin-bottom: 10px;">→ <a href="/blog/abdm-compliance-2026.html" style="color: var(--color-hms); text-decoration: none; font-weight: 500;">ABDM Compliance Guide for Hospitals</a></li>
          <li style="margin-bottom: 10px;">→ <a href="/blog/fragmented-hospital-software-costs.html" style="color: var(--color-hms); text-decoration: none; font-weight: 500;">The Hidden Cost of Fragmented Hospital Software</a></li>
        </ul>
      </div>
"""

blog_dir = "./blog"
for file in os.listdir(blog_dir):
    if file.endswith(".html") and file != "index.html" and file != "post-template.html":
        filepath = os.path.join(blog_dir, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Avoid double-injecting
        if "Related Articles" in content:
            continue
            
        # Inject right before <div class="blog-cta">
        content = content.replace('<div class="blog-cta">', related_html + '\n      <div class="blog-cta">')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Related Articles internal linking injected.")
