import os
import glob

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
html_files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace "Zeno Hosp" with "ZenoHosp" in the content
    # But we should be careful not to replace it if it's part of a file path, though in HTML it's mostly text/meta
    if 'Zeno Hosp' in content:
        content = content.replace('Zeno Hosp', 'ZenoHosp')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Replaced 'Zeno Hosp' with 'ZenoHosp' in {count} HTML files.")
