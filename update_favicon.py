import os
import glob
import re

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
html_files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace the old fav.ico link with the new favicon.svg link
    # Using regex to catch any variations in spacing or quote types
    new_content = re.sub(
        r'<link\s+rel=[\'"]icon[\'"]\s+type=[\'"]image/x-icon[\'"]\s+href=[\'"]/images/fav\.ico[\'"]\s*>',
        '<link rel="icon" type="image/svg+xml" href="/images/favicon.svg">',
        content
    )
    
    # Also catch cases without type or different order
    if 'fav.ico' in new_content:
        new_content = new_content.replace('href="/images/fav.ico"', 'href="/images/favicon.svg" type="image/svg+xml"')

    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated favicon link to favicon.svg in {count} HTML files.")
