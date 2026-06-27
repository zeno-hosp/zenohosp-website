import os
import glob

# Get all html files in apps/finance
files = glob.glob('apps/finance/**/*.html', recursive=True)

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # 1. Add css/finance.css if not present
    if 'href="/css/finance.css"' not in content and 'href="../../css/finance.css"' not in content:
        # Find the closing </head> or main.css link
        if '<link rel="stylesheet" href="/css/main.css">' in content:
            content = content.replace(
                '<link rel="stylesheet" href="/css/main.css">',
                '<link rel="stylesheet" href="/css/main.css">\n  <link rel="stylesheet" href="/css/finance.css">'
            )
        elif '<link rel="stylesheet" href="../../css/main.css">' in content:
             content = content.replace(
                '<link rel="stylesheet" href="../../css/main.css">',
                '<link rel="stylesheet" href="../../css/main.css">\n  <link rel="stylesheet" href="/css/finance.css">'
            )
        else:
            content = content.replace('</head>', '  <link rel="stylesheet" href="/css/finance.css">\n</head>')

    # 2. Add finance-app class to body
    if '<body class="finance-app">' not in content and 'class="finance-app"' not in content:
        if '<body>' in content:
            content = content.replace('<body>', '<body class="finance-app">')
        elif '<body class="' in content:
            content = content.replace('<body class="', '<body class="finance-app ')

    with open(file, 'w') as f:
        f.write(content)

print(f"Updated {len(files)} files.")
