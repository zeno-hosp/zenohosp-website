import os

def update_html_files():
    base_dir = "/Users/iniyananbu/Documents/ZenoHosp Website"
    
    desktop_search = '<span>Video & content by Zesignworks</span>\n                </div>\n              </a>'
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
              
    mobile_search = '<a href="/services/social-media/index.html">Social Media Management</a>'
    mobile_insert = '<a href="/services/advertising/index.html">Advertising</a>'
    
    updated_count = 0
    skipped_count = 0

    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root:
            continue
            
        for file in files:
            if not file.endswith(".html"):
                continue
                
            filepath = os.path.join(root, file)
            
            # Skip if this is the new page itself which we already added the nav manually
            if 'services/advertising/index.html' in filepath:
                continue

            try:
                with open(filepath, 'r') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {filepath}: {e}")
                continue

            if desktop_search in content and mobile_search in content:
                if '<strong>Advertising</strong>' not in content:
                    new_content = content.replace(desktop_search, desktop_search + desktop_insert)
                    new_content = new_content.replace(mobile_search, mobile_search + '\n          ' + mobile_insert)
                    
                    with open(filepath, 'w') as f:
                        f.write(new_content)
                    updated_count += 1
                else:
                    skipped_count += 1
            else:
                skipped_count += 1
                
    print(f"Updated {updated_count} files, skipped {skipped_count} files.")

if __name__ == "__main__":
    update_html_files()
