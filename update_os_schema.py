import os
import re

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html') or file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = re.sub(
                r'"operatingSystem":\s*"Web(?:-based)?,\s*Cloud"', 
                r'"operatingSystem": "Web-based, Cloud, On-Premise"', 
                content
            )

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print("operatingSystem schema updated site-wide.")
