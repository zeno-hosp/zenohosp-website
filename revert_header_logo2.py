import os
import glob
import re

def revert_main_header_logo():
    directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
    html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)
    
    count = 0
    # Use a regex that matches:
    # <a href="/index.html" class="logo">
    #   <img src="/images/zenohosp-w.svg" ...
    pattern = re.compile(r'(<a href="/index\.html" class="logo">\s*)<img src="/images/zenohosp-w\.svg"', re.IGNORECASE)
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, num_subs = pattern.subn(r'\1<img src="/images/zenohosp-b.svg"', content)
        
        if num_subs > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            
    print(f"Reverted {count} files using regex.")

if __name__ == '__main__':
    revert_main_header_logo()
