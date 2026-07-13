import os
import re

def parse_css(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Very basic parsing using character by character to handle nested braces (like @media)
    blocks = []
    current_block = ""
    brace_count = 0
    in_comment = False
    
    i = 0
    while i < len(content):
        c = content[i]
        
        # Handle comments
        if c == '/' and i+1 < len(content) and content[i+1] == '*':
            in_comment = True
            current_block += c
            i += 1
            continue
        if in_comment:
            current_block += c
            if c == '/' and content[i-1] == '*':
                in_comment = False
            i += 1
            continue
            
        current_block += c
        if c == '{':
            brace_count += 1
        elif c == '}':
            brace_count -= 1
            if brace_count == 0:
                blocks.append(current_block.strip())
                current_block = ""
        i += 1
        
    return blocks

blocks = parse_css('css/styles.css')

categories = {
    'asset': [],
    'hms': [],
    'inv': [],
    'ot': [],
    'pharm': [],
    'marketing': [],
    'home': [],
    'global': []
}

for block in blocks:
    if block.startswith('@media'):
        categories['global'].append(block)
    elif '.asset-' in block or block.startswith('.asset'):
        categories['asset'].append(block)
    elif '.hms-' in block or block.startswith('.hms'):
        categories['hms'].append(block)
    elif '.inv-' in block or block.startswith('.inv'):
        categories['inv'].append(block)
    elif '.ot-' in block or block.startswith('.ot'):
        categories['ot'].append(block)
    elif '.pharm-' in block or block.startswith('.pharm'):
        categories['pharm'].append(block)
    elif '.marketing-' in block or block.startswith('.marketing'):
        categories['marketing'].append(block)
    elif '.home-' in block or block.startswith('.home'):
        categories['home'].append(block)
    else:
        categories['global'].append(block)

print("Parsed", len(blocks), "blocks")
for k, v in categories.items():
    print(f"{k}: {len(v)} blocks")

