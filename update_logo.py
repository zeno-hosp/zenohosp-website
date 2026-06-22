import os
import glob
import re

def update_assets(directory):
    count = 0
    
    # 1. Favicon replacement
    favicon_pattern = re.compile(r'<link\s+rel="icon"\s+type="image/svg\+xml"\s+href="/images/favicon\.svg">')
    new_favicon = '<link rel="icon" type="image/x-icon" href="/images/fav.ico">'
    
    # 2. JSON-LD logo replacement
    json_logo_pattern = re.compile(r'"logo":\s*"https://zenohosp\.com/images/favicon\.svg"')
    new_json_logo = '"logo": "https://zenohosp.com/images/zenohosp-b.svg"'
    
    # 3. HTML Logo replacement
    # We want to match:
    # <a href="/index.html" class="logo">
    #   <span class="logo-icon">Z</span>
    #   <span class="logo-text">Zeno<span class="logo-accent">Hosp</span></span>
    # </a>
    logo_pattern = re.compile(
        r'(<a href="/index\.html" class="logo">)\s*<span class="logo-icon">Z</span>\s*<span class="logo-text">Zeno<span class="logo-accent">Hosp</span></span>\s*(</a>)',
        re.MULTILINE
    )
    
    for filepath in glob.glob(os.path.join(directory, '**/*.html'), recursive=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            content = favicon_pattern.sub(new_favicon, content)
            content = json_logo_pattern.sub(new_json_logo, content)
            
            # The replacement will insert the img tag
            content = logo_pattern.sub(
                r'\1\n  <img src="/images/zenohosp-b.svg" alt="ZenoHosp Logo" style="height: 32px; width: auto; display: block;" />\n\2', 
                content
            )
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Updated: {filepath}")
                
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            
    print(f"\\nSuccessfully updated {count} files.")

if __name__ == '__main__':
    update_assets('/Users/iniyananbu/Documents/Zeno Hosp Website')
