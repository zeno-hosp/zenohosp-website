import os
import glob
import re

def standardize_footers():
    directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
    index_path = os.path.join(directory, 'index.html')
    
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    # Extract the global footer
    match = re.search(r'(?s)(<footer\b[^>]*>.*?</footer>)', index_content)
    if not match:
        print("Could not find footer in index.html")
        return
        
    global_footer = match.group(1)
    
    html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)
    count = 0
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace existing footer with global_footer
        # Be careful not to replace if it's already identical
        new_content, num_subs = re.subn(r'(?s)<footer\b[^>]*>.*?</footer>', global_footer, content)
        
        if num_subs > 0 and new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated footer in {filepath}")
            
    print(f"Standardized footers in {count} files.")

if __name__ == '__main__':
    standardize_footers()
