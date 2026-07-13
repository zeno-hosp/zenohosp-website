import glob
import re
import os

files = glob.glob('apps/**/features/**/index.html', recursive=True)
count = 0
for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Remove the div with class="fp-hero-badge"
    # We'll use a regex that handles both single-line and multi-line if any remain
    new_content = re.sub(r'[ \t]*<div class="fp-hero-badge">.*?</svg>[^<]*</div>\n?', '', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {file}")

print(f"Total files updated: {count}")
