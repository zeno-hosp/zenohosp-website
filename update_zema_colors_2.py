import os

def replace_in_block(filepath, start_str, end_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find(start_str)
    if start_idx == -1:
        print(f"Start string not found in {filepath}")
        return

    # To encompass the style tag as well for solutions, let's just find the exact block bounds
    end_idx = content.find(end_str, start_idx)
    if end_idx == -1:
        print(f"End string not found in {filepath}")
        return

    end_idx += len(end_str) # Include the end string

    block = content[start_idx:end_idx]

    # Replacements
    block = block.replace('#d1f470', '#E86712')
    block = block.replace('rgba(209, 244, 112,', 'rgba(232, 103, 18,')
    block = block.replace('rgba(209,244,112,', 'rgba(232,103,18,')

    new_content = content[:start_idx] + block + content[end_idx:]

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated colors in {filepath}")

# Update solutions/index.html
replace_in_block(
    '/Users/iniyananbu/Documents/Zeno Hosp Website/solutions/index.html',
    '.zema-section {',
    '</section>'
)

# Update pricing/index.html
replace_in_block(
    '/Users/iniyananbu/Documents/Zeno Hosp Website/pricing/index.html',
    '<section id="zema-pricing"',
    '</section>'
)
