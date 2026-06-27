import glob
import os
import re

files = glob.glob('apps/*/docs/*.html')

count = 0
for file in files:
    # Get the app name from the path: apps/<app_name>/docs/file.html
    parts = file.split('/')
    if len(parts) >= 2:
        app_name = parts[1]
        
        with open(file, 'r') as f:
            content = f.read()
            
        # Replace href="/apps/index.html" with href="/apps/app_name/index.html"
        new_content, num_subs = re.subn(
            r'href="/apps/index\.html"',
            f'href="/apps/{app_name}/index.html"',
            content
        )
        
        if num_subs > 0:
            with open(file, 'w') as f:
                f.write(new_content)
            count += 1
            print(f"Fixed back link in {file}")

print(f"Total files fixed: {count}")
