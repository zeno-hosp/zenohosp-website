import os
import re

def update_voimai_nav():
    base_dir = "/Users/iniyananbu/Documents/ZenoHosp Website"
    
    # Desktop Regex: Search for the Advertising block to insert Voim.ai after it
    desktop_pattern = re.compile(
        r'(<a\s+href="/services/advertising/index\.html"\s+class="dropdown-item">.*?</a>)',
        re.DOTALL
    )
    
    desktop_insert = """
              <a href="/services/voimai/index.html" class="dropdown-item">
                <div class="dropdown-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px;">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20">
                    <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path>
                    <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
                    <line x1="12" y1="19" x2="12" y2="23"></line>
                    <line x1="8" y1="23" x2="16" y2="23"></line>
                  </svg>
                </div>
                <div class="dropdown-info">
                  <strong>Voim.ai Agent</strong>
                  <span>AI Voice Caller & Scheduler</span>
                </div>
              </a>"""
              
    # Mobile Regex
    mobile_pattern = re.compile(
        r'(<a\s+href="/services/advertising/index\.html"[^>]*>Advertising</a>)'
    )
    mobile_insert = '\n          <a href="/services/voimai/index.html">Voim.ai</a>'
    
    updated_count = 0
    skipped_count = 0

    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root:
            continue
            
        for file in files:
            if not file.endswith(".html"):
                continue
                
            filepath = os.path.join(root, file)
            
            # Skip the newly created Voim.ai page itself since it was created with the link
            if 'services/voimai/index.html' in filepath:
                continue

            try:
                with open(filepath, 'r') as f:
                    content = f.read()
            except Exception as e:
                continue
            
            if '<strong>Voim.ai Agent</strong>' in content:
                skipped_count += 1
                continue
            
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
                
    print(f"Updated {updated_count} files with Voim.ai nav, skipped {skipped_count} files.")

if __name__ == "__main__":
    update_voimai_nav()
