import re

html_path = '/Users/iniyananbu/Documents/ZenoHosp Website/careers/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the block
block_pattern = r'\s*<!-- Senior Doctor - Zema AI -->.*?</div>\s*</div>\s*</div>'
match = re.search(block_pattern, content, re.DOTALL)
if match:
    block_text = match.group(0)
    
    # Remove from old position
    content = content.replace(block_text, '')
    
    # Modify title and comment
    block_text = block_text.replace('Senior Doctor - Zema AI', 'Senior MD Surgeon')
    block_text = block_text.replace('Senior Doctor', 'Senior MD Surgeon') # Just in case
    
    # Insert at new position (after <div class="openings-grid">)
    insert_marker = '<div class="openings-grid">\n'
    content = content.replace(insert_marker, insert_marker + block_text + '\n')

    # Also update the heading that says "6 openings across engineering and design"
    # To "7 openings across engineering, medical, and design"
    content = content.replace('<h2>6 openings across engineering and design</h2>', '<h2>7 openings across engineering, medical, and design</h2>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated careers successfully.")
