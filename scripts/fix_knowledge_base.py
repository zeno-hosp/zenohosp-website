import os
import glob
import re

files = glob.glob('apps/**/*.html', recursive=True)

count = 0
for file in files:
    with open(file, 'r') as f:
        content = f.read()
        
    # We want to remove lines like:
    # <li><a href="/apps/ot-room/docs/index.html">Knowledge Base</a></li>
    # and any surrounding spaces, up to the newline.
    pattern = r'\n?[ \t]*<li>\s*<a[^>]*href=["\'][^"\']*/docs/index\.html["\'][^>]*>Knowledge Base</a>\s*</li>'
    
    new_content, num_subs = re.subn(pattern, '', content, flags=re.IGNORECASE)
    
    if num_subs > 0:
        with open(file, 'w') as f:
            f.write(new_content)
        count += 1
        print(f"Removed Knowledge Base from {file}")

print(f"Total files updated: {count}")
