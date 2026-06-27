import os
import glob
import re

APPS = ['hms', 'inventory', 'ot-room', 'finance', 'pharmacy', 'lab', 'people', 'asset']

for app in APPS:
    app_dir = os.path.join('apps', app)
    # Find a feature page for this app to extract the dropdown block
    feature_pages = glob.glob(os.path.join(app_dir, 'features', '*', 'index.html'))
    if not feature_pages:
        print(f"No feature pages found for {app}")
        continue
        
    reference_page = feature_pages[0]
    with open(reference_page, 'r') as f:
        content = f.read()
        
    # Extract the <li class="has-dropdown"> block that contains the word "Features"
    match = re.search(r'<li class="has-dropdown"><a[^>]*>Features.*?</li>', content, re.DOTALL)
    if not match:
        print(f"Could not find Features dropdown in {reference_page}")
        continue
        
    dropdown_html = match.group(0)
    print(f"Extracted dropdown for {app}")
    
    # Now find all index.html files in this app directory
    all_pages = glob.glob(os.path.join(app_dir, '**', 'index.html'), recursive=True)
    for page in all_pages:
        with open(page, 'r') as f:
            page_content = f.read()
            
        # We want to replace <li><a href="javascript:void(0)">Features</a></li>
        # or any similar <li><a href="...">Features</a></li>
        # but NOT <li class="has-dropdown">...</li>
        
        # Regex to find the bad Features link
        # It must NOT have class="has-dropdown"
        bad_link_pattern = r'<li><a[^>]*>Features</a></li>'
        
        if re.search(bad_link_pattern, page_content):
            new_content = re.sub(bad_link_pattern, dropdown_html, page_content)
            with open(page, 'w') as f:
                f.write(new_content)
            print(f"  Fixed {page}")

print("Done")
