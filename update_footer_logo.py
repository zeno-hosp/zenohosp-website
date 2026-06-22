import os
import glob
import re

def update_footer_logo():
    directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
    html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)
    
    count = 0
    # Use a regex that matches:
    # <div class="footer-brand">
    #   <a href="/index.html" class="logo">
    #     <img src="/images/zenohosp-b.svg"
    
    pattern = re.compile(r'(class="footer-brand"\s*>\s*<a[^>]*class="logo"[^>]*>\s*<img[^>]*src="/images/zenohosp-)b(\.svg")', re.IGNORECASE | re.DOTALL)
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, num_subs = pattern.subn(r'\g<1>w\g<2>', content)
        
        if num_subs > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            
    print(f"Updated footer logos in {count} files.")

if __name__ == '__main__':
    update_footer_logo()
