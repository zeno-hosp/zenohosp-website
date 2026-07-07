import os
import re

def update_html_files_regex():
    base_dir = "/Users/iniyananbu/Documents/ZenoHosp Website"
    
    # Desktop Regex
    # Match the entire Social Media Management dropdown-item block
    desktop_pattern = re.compile(
        r'(<a\s+href="/services/social-media/index\.html"\s+class="dropdown-item">.*?</a>)',
        re.DOTALL
    )
    
    desktop_insert = """
              <a href="/services/advertising/index.html" class="dropdown-item">
                <div class="dropdown-icon" style="background: rgba(59, 130, 246, 0.1); color: #3b82f6; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px;">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20">
                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                  </svg>
                </div>
                <div class="dropdown-info">
                  <strong>Advertising</strong>
                  <span>Google, FB & YouTube Ads</span>
                </div>
              </a>"""
              
    # Mobile Regex
    mobile_pattern = re.compile(
        r'(<a\s+href="/services/social-media/index\.html"[^>]*>Social Media Management</a>)'
    )
    mobile_insert = '\n          <a href="/services/advertising/index.html">Advertising</a>'
    
    updated_count = 0
    skipped_count = 0

    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root:
            continue
            
        for file in files:
            if not file.endswith(".html"):
                continue
                
            filepath = os.path.join(root, file)
            
            # Skip the new page itself
            if 'services/advertising/index.html' in filepath:
                continue

            try:
                with open(filepath, 'r') as f:
                    content = f.read()
            except Exception as e:
                continue
            
            if '<strong>Advertising</strong>' in content:
                skipped_count += 1
                continue

            # Need to match both to ensure we replace correctly
            # Wait, in the mobile menu, it's NOT a class="dropdown-item".
            # The desktop has class="dropdown-item".
            
            # We must be careful because the desktop regex matches `<a href="/services/social-media/index.html" class="dropdown-item">`
            # But the mobile one matches `<a href="/services/social-media/index.html">Social Media Management</a>`
            
            if desktop_pattern.search(content) and mobile_pattern.search(content):
                # Replace desktop
                new_content = desktop_pattern.sub(r'\1' + desktop_insert, content)
                # Replace mobile
                new_content = mobile_pattern.sub(r'\1' + mobile_insert, new_content)
                
                with open(filepath, 'w') as f:
                    f.write(new_content)
                updated_count += 1
            else:
                skipped_count += 1
                
    print(f"Regex Updated {updated_count} files, skipped {skipped_count} files.")

if __name__ == "__main__":
    update_html_files_regex()
