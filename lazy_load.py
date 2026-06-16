import os
import re

def add_lazy_loading(directory):
    img_tag_pattern = re.compile(r'<img\s+([^>]*?)>', re.IGNORECASE)

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
                    
                    # Don't lazy load if it already has loading attr
                    if 'loading=' in inner_attrs.lower():
                        return img_str
                        
                    # Don't lazy load hero images or logos
                    if 'hero' in inner_attrs.lower() or 'logo' in inner_attrs.lower() or 'favicon' in inner_attrs.lower():
                        return img_str
                        
                    return f'<img {inner_attrs} loading="lazy">'

                new_content = img_tag_pattern.sub(replace_img, content)
                
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Added lazy loading in: {path}")

add_lazy_loading(".")
print("Done lazy loading optimization.")
