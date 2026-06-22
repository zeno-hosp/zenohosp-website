import os
import glob

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
apps_dir = os.path.join(directory, 'apps')

essential_apps = ['hms', 'inventory', 'asset', 'finance', 'people']

for app in essential_apps:
    app_path = os.path.join(apps_dir, app)
    if not os.path.exists(app_path):
        continue
        
    html_files = glob.glob(os.path.join(app_path, '**/*.html'), recursive=True)
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('href="/pricing/index.html"', f'href="/apps/{app}/pricing/index.html"')
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated links in {file_path}")
