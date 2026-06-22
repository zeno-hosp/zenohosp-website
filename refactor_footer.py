import os
import glob
import re

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'

# 1. Extract standard footer from pricing/index.html
pricing_file = os.path.join(directory, 'pricing', 'index.html')
with open(pricing_file, 'r', encoding='utf-8') as f:
    pricing_content = f.read()

footer_match = re.search(r'(<footer class="footer">.*?</footer>)', pricing_content, re.DOTALL)
if not footer_match:
    print("Could not find standard footer in pricing/index.html")
    exit(1)

standard_footer = footer_match.group(1)

# Escape backticks if any exist in the footer (standard practice for JS template literals)
standard_footer = standard_footer.replace('`', '\\`')

# 2. Create the JS Web Component
js_dir = os.path.join(directory, 'js', 'components')
os.makedirs(js_dir, exist_ok=True)
footer_js_path = os.path.join(js_dir, 'footer.js')

js_content = f"""class ZenoFooter extends HTMLElement {{
  connectedCallback() {{
    this.innerHTML = `
{standard_footer}
    `;
  }}
}}
customElements.define('zeno-footer', ZenoFooter);
"""

with open(footer_js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Created /js/components/footer.js")

# 3. Replace footer in all HTML files
html_files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)
count = 0

for file_path in html_files:
    # Skip any files inside node_modules or something if they exist (not likely here, but safe)
    if 'node_modules' in file_path:
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # Replace footer block with component
    content = re.sub(r'<footer class="footer">.*?</footer>', '<zeno-footer></zeno-footer>', content, flags=re.DOTALL)
    
    # Inject script if not already there
    script_tag = '<script src="/js/components/footer.js"></script>\n    <script src="/js/app.js"'
    if 'src="/js/components/footer.js"' not in content:
        content = content.replace('<script src="/js/app.js"', script_tag)
        
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Refactored footer in {count} HTML files.")
