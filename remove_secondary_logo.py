import os
import glob
import re

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website/apps'
html_files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The block looks like:
    # <a href="/apps/hms/index.html" class="mlogo">
    #   <img src="/images/zenohosp-b.svg" alt="ZenoHosp Logo" style="height: 24px; width: auto; vertical-align: middle;" /> <span class="mod">HMS</span>
    # </a>

    # We want to remove the <img> tag that is immediately followed by <span class="mod">.
    # More generally, we can just remove the <img> tag inside class="mlogo".
    
    # A regex to match: <a [^>]*class="mlogo"[^>]*>...</a> and replace the <img> inside it.
    
    def remove_img(match):
        inner_html = match.group(2)
        # remove the img tag inside
        inner_html = re.sub(r'\s*<img[^>]*>\s*', ' ', inner_html)
        return match.group(1) + inner_html + match.group(3)

    # Regex: match from <a ... class="mlogo" ...> to </a>
    # Note: re.sub with a function is powerful here.
    new_content = re.sub(r'(<a[^>]*class="mlogo"[^>]*>)(.*?)(</a>)', remove_img, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Removed secondary logo from {count} files.")
