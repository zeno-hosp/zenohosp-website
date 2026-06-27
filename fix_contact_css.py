import os
import re

css_path = '/Users/iniyananbu/Documents/ZenoHosp Website/css/pages/contact.css'

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix any weird diff artifacts that might have been accidentally inserted
content = content.replace('+.contact-hero', '')

# Replace the gradient with the black background
content = re.sub(
    r'\.contact-hero\s*\{[^}]*background:\s*linear-gradient[^}]*\}',
    '.contact-hero{padding:140px 0 80px;background:#11110d;position:relative;overflow:hidden;color:#fff}.contact-hero::before{content:\'\';position:absolute;inset:0;background:radial-gradient(ellipse 60% 50% at 50% 0%,rgba(209,244,112,0.1) 0%,transparent 70%);pointer-events:none}',
    content
)

# Replace contact-hero-split if it doesn't have z-index: 1 yet
if 'z-index:1' not in content:
    content = content.replace(
        '.contact-hero-split{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}',
        '.contact-hero-split{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;position:relative;z-index:1}'
    )

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated contact.css successfully.")
