import os
import glob
import re
import shutil

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
apps_dir = os.path.join(directory, 'apps')

essential_apps = ['hms', 'inventory', 'asset', 'finance', 'people']
addon_apps = ['pharmacy', 'lab', 'ot-room']

# Read global pricing
with open(os.path.join(directory, 'pricing', 'index.html'), 'r', encoding='utf-8') as f:
    global_pricing_content = f.read()

# Helper to format app name for title
def get_app_title(app):
    mapping = {
        'hms': 'HMS',
        'inventory': 'Inventory',
        'asset': 'Asset Management',
        'finance': 'Finance',
        'people': 'People Management',
        'pharmacy': 'Pharmacy',
        'lab': 'Lab',
        'ot-room': 'OT Room'
    }
    return mapping.get(app, app.title())

# 1. Essential Apps
for app in essential_apps:
    app_index = os.path.join(apps_dir, app, 'index.html')
    if not os.path.exists(app_index):
        continue
        
    with open(app_index, 'r', encoding='utf-8') as f:
        app_content = f.read()
        
    # Extract nav components from app
    # 1. platform-strip
    strip_match = re.search(r'(<div class="platform-strip">.*?</div>\s*<header)', app_content, re.DOTALL)
    if not strip_match:
        # Some apps might not have platform strip formatted exactly this way, let's just grab from platform-strip to </header>
        nav_match = re.search(r'(<div class="platform-strip">.*?</header>)', app_content, re.DOTALL)
    else:
        nav_match = re.search(r'(<div class="platform-strip">.*?</header>)', app_content, re.DOTALL)
        
    mobile_match = re.search(r'(<div class="mobile-nav-overlay".*?</ul>\s*</div>)', app_content, re.DOTALL)
    
    if nav_match and mobile_match:
        app_nav = nav_match.group(1)
        app_mobile = mobile_match.group(1)
        
        # We need to replace href="/pricing/index.html" with href="/apps/app_name/pricing/index.html" in the extracted navs
        app_nav = app_nav.replace('href="/pricing/index.html"', f'href="/apps/{app}/pricing/index.html"')
        app_mobile = app_mobile.replace('href="/pricing/index.html"', f'href="/apps/{app}/pricing/index.html"')
        
        # Remove global nav from global pricing
        # Global nav: <nav class="marketing-navbar"...</nav>
        # Global mobile: <div class="mobile-nav-overlay"...</div> <div class="mobile-nav-menu"...</div>
        
        # Use regex to strip them
        new_content = re.sub(r'<nav class="navbar marketing-navbar".*?</nav>', app_nav, global_pricing_content, flags=re.DOTALL)
        new_content = re.sub(r'<div class="mobile-nav-overlay".*?</ul>\s*</div>', app_mobile, new_content, flags=re.DOTALL)
        
        # Change Title
        new_content = re.sub(r'<title>.*?</title>', f'<title>{get_app_title(app)} Pricing | ZenoHosp Cost</title>', new_content)
        
        # Create output dir
        out_dir = os.path.join(apps_dir, app, 'pricing')
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, 'index.html')
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Created pricing page for {app}")
        
    else:
        print(f"Could not extract nav for {app}")
