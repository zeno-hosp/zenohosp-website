import os
import glob

def revert_main_header_logo():
    directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
    html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)
    
    replacements = [
        # Main header - revert to black logo because background is white
        ('class="logo"><img src="/images/zenohosp-w.svg"',
         'class="logo"><img src="/images/zenohosp-b.svg"')
    ]
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for old_str, new_str in replacements:
            new_content = new_content.replace(old_str, new_str)
            
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            
    print(f"Reverted {count} files.")

if __name__ == '__main__':
    revert_main_header_logo()
