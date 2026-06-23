import os
import glob

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
html_files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '—' in content:
        # Replace spaces around em-dash with space-hyphen-space
        content = content.replace(' — ', ' - ')
        # Replace any remaining em-dashes with a hyphen
        content = content.replace('—', '-')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Replaced em-dash in {count} HTML files.")
