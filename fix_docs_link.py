import os
import glob
import re

APPS = ['hms', 'inventory', 'ot-room', 'finance', 'pharmacy', 'lab', 'people', 'asset']

count = 0
for app in APPS:
    app_dir = os.path.join('apps', app)
    # Get all html files for this app
    all_pages = glob.glob(os.path.join(app_dir, '**', '*.html'), recursive=True)
    
    docs_link = f'<li><a href="/apps/{app}/docs/index.html">Docs</a></li>'
    
    for page in all_pages:
        # Skip docs pages since they have a different header
        if '/docs/' in page:
            continue
            
        with open(page, 'r') as f:
            content = f.read()
            
        # Add to main desktop nav and mobile nav right after Resources if Docs isn't there already
        # Regex explanation:
        # We look for <li><a ...>Resources</a></li>
        # Followed by some whitespace
        # Then we assert that the next thing is NOT Docs
        
        # We can use a simpler approach: 
        # Split by the Resources line, and check if the next line contains 'Docs'
        
        resources_pattern = re.compile(rf'(<li>\s*<a[^>]*href=["\'][^"\']*/apps/{app}/resources/index\.html["\'][^>]*>Resources</a>\s*</li>)', re.IGNORECASE)
        
        # Find all matches
        parts = resources_pattern.split(content)
        if len(parts) > 1:
            new_content = parts[0]
            modified = False
            for i in range(1, len(parts), 2):
                res_line = parts[i]
                next_part = parts[i+1]
                
                # Check if Docs is already right there (within the next 100 characters to be safe)
                if not re.search(r'<li>\s*<a[^>]*>Docs</a>', next_part[:150], re.IGNORECASE):
                    # We need to preserve the indentation of the resources line
                    indent = ""
                    indent_match = re.search(r'([ \t]+)$', parts[i-1])
                    if indent_match:
                        indent = "\n" + indent_match.group(1)
                    
                    new_content += res_line + indent + docs_link + next_part
                    modified = True
                else:
                    new_content += res_line + next_part
                    
            if modified:
                with open(page, 'w') as f:
                    f.write(new_content)
                count += 1
                print(f"Added Docs link to {page}")

print(f"Total files updated: {count}")
