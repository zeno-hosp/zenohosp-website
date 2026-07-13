import os
import glob
import re

def update_remaining_logos():
    # Find all html files
    html_files = glob.glob('/Users/iniyananbu/Documents/Zeno Hosp Website/**/*.html', recursive=True)
    count = 0
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern 1: ps-brand
        # <a href="/index.html" class="ps-brand"><span class="logo-icon">Z</span>ZenoHosp</a>
        content = re.sub(
            r'<a href="[^"]*" class="ps-brand">\s*<span class="logo-icon">Z</span>ZenoHosp\s*</a>',
            r'<a href="/index.html" class="ps-brand"><img src="/images/zenohosp-b.svg" alt="ZenoHosp Logo" style="height: 20px; width: auto; vertical-align: middle;" /></a>',
            content
        )

        # Pattern 2: mlogo or any other place with <span class="logo-icon">Z</span>ZenoHosp
        # We need to replace just the logo part, keeping <span class="mod">...</span> intact
        content = re.sub(
            r'<span class="logo-icon">Z</span>ZenoHosp',
            r'<img src="/images/zenohosp-b.svg" alt="ZenoHosp Logo" style="height: 24px; width: auto; vertical-align: middle;" />',
            content
        )

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1

    print(f"Updated logos in {count} files.")

if __name__ == '__main__':
    update_remaining_logos()
