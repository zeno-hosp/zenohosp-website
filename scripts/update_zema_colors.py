import re

def update_colors_in_file(filepath, start_marker, end_marker):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the section to update
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx)

    if start_idx == -1 or end_idx == -1:
        print(f"Could not find section in {filepath}")
        return

    # Extract section
    section = content[start_idx:end_idx]

    # Replace Hex
    section = section.replace('#d1f470', '#E86712')
    
    # Replace rgba with spaces
    section = section.replace('209, 244, 112', '232, 103, 18')
    # Replace rgba without spaces
    section = section.replace('209,244,112', '232,103,18')

    # Reconstruct content
    new_content = content[:start_idx] + section + content[end_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated colors in {filepath}")

# Update solutions/index.html (styles and html)
update_colors_in_file(
    '/Users/iniyananbu/Documents/Zeno Hosp Website/solutions/index.html',
    '.zema-section {',
    '<!-- ══ CALL TO ACTION ════════════════════════════════════════ -->'
)

# Update pricing/index.html
update_colors_in_file(
    '/Users/iniyananbu/Documents/Zeno Hosp Website/pricing/index.html',
    '<!-- ══ ZEMA AI ADD-ON ════════════════════════════════════════ -->',
    '<!-- ══ FAQS ════════════════════════════════════════ -->'
)
