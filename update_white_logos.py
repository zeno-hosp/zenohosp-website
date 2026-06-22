import os
import glob

def update_to_white_logos():
    directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
    html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)
    
    replacements = [
        # Platform strip
        ('class="ps-brand"><img src="/images/zenohosp-b.svg"',
         'class="ps-brand"><img src="/images/zenohosp-w.svg"'),
        
        # Main header
        ('class="logo"><img src="/images/zenohosp-b.svg"',
         'class="logo"><img src="/images/zenohosp-w.svg"'),
         
        # Footer
        ('<img src="/images/zenohosp-b.svg" alt="ZenoHosp Logo" style="height: 32px; width: auto; display: block;" />',
         '<img src="/images/zenohosp-w.svg" alt="ZenoHosp Logo" style="height: 32px; width: auto; display: block;" />')
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
            
    print(f"Updated {count} files.")

if __name__ == '__main__':
    update_to_white_logos()
