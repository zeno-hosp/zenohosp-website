import os
import glob
import re

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
html_files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Check if demo-modal script is already included
    if '<script src="/js/components/demo-modal.js"></script>' not in content:
        # Check if demo-modal tag exists
        if '<demo-modal></demo-modal>' not in content:
            # We want to insert both right before the footer script, app script, or </body>
            injection_html = "\n    <demo-modal></demo-modal>\n    <script src=\"/js/components/demo-modal.js\"></script>\n"
            
            # Find a good place to inject (before footer.js or app.js or </body>)
            if '<script src="/js/app.js"' in content:
                content = content.replace('<script src="/js/app.js"', injection_html + '    <script src="/js/app.js"')
                modified = True
            elif '</body>' in content:
                content = content.replace('</body>', injection_html + '</body>')
                modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Injected demo-modal into {count} files.")
