import os
import glob

def check_remaining_logos():
    directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
    html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'zenohosp-b.svg' in line:
                if 'class="mlogo"' not in line:
                    print(f"{filepath}:{i+1}: {line.strip()}")

if __name__ == '__main__':
    check_remaining_logos()
