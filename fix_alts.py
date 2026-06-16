import os
import re

def fix_alt_tags(directory):
    img_tag_pattern = re.compile(r'<img\s+([^>]*?)>', re.IGNORECASE)
    alt_attr_pattern = re.compile(r'alt\s*=\s*[\'"](.*?)[\'"]', re.IGNORECASE)

    for root, _, files in os.walk(directory):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                def replace_img(match):
                    img_str = match.group(0)
                    inner_attrs = match.group(1)
                    if not alt_attr_pattern.search(inner_attrs):
                        return f'<img {inner_attrs} alt="ZenoHosp Healthcare Software">'
                    return img_str

                new_content = img_tag_pattern.sub(replace_img, content)
                
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Fixed missing alt tags in: {path}")

fix_alt_tags(".")
print("Done fixing alt tags.")
