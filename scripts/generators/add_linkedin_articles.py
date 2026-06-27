import os
import re

base_dir = '/Users/iniyananbu/Documents/ZenoHosp Website/blog'
template_path = os.path.join(base_dir, 'post-template.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

articles = [
    {
        'filename': 'inventory-money-missing.html',
        'title': 'Where hospital money and inventory actually go missing',
        'category': 'Finance & Operations',
        'cat_class': 'cat-finance',
        'date': 'June 2026',
        'read_time': '2 min read',
        'desc': 'Zenohosp Helps Founders avoid Fund leakage and Inventory Leakage',
        'img': '/images/blog-cover-1.jpg'
    },
    {
        'filename': 'revenue-left-on-table.html',
        'title': 'Three places hospitals leave revenue on the table without realizing',
        'category': 'Finance',
        'cat_class': 'cat-finance',
        'date': 'June 2026',
        'read_time': '3 min read',
        'desc': 'Discover the hidden areas where hospitals commonly lose revenue and how to capture it.',
        'img': '/images/blog-cover-2.jpg'
    },
    {
        'filename': 'patient-wait-times-discharge.html',
        'title': 'Why patients wait hours after doctor says you can go home',
        'category': 'Operations',
        'cat_class': 'cat-operations',
        'date': 'June 2026',
        'read_time': '3 min read',
        'desc': 'Learn why discharge delays happen and how modern HMS can reduce patient wait times.',
        'img': '/images/blog-cover-1.jpg'
    }
]

new_cards_html = ""

for article in articles:
    content = template
    # Update title tags
    content = re.sub(r'<title>.*?</title>', f'<title>{article["title"]} | ZenoHosp Blog</title>', content)
    content = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{article["title"]}">', content)
    
    # Update H1
    content = re.sub(r'<h1>.*?</h1>', f'<h1>{article["title"]}</h1>', content)
    
    # Update description
    content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{article["desc"]}">', content)
    content = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{article["desc"]}">', content)
    
    # Update meta
    meta_html = f"""<div class="blog-article-meta">
          <span>{article["category"]}</span> • <span>{article["date"]}</span> • <span>{article["read_time"]}</span>
        </div>"""
    content = re.sub(r'<div class="blog-article-meta">.*?</div>', meta_html, content, flags=re.DOTALL)
    
    # Replace content body with placeholder
    placeholder = f"""<section class="blog-content">
      <h2>{article['title']}</h2>
      <p style="padding: 40px; background-color: #fef3c7; border-left: 4px solid #f59e0b; border-radius: 4px; font-weight: bold;">
        [PASTE YOUR ARTICLE CONTENT HERE]
      </p>
    </section>"""
    content = re.sub(r'<section class="blog-content">.*?</section>', placeholder, content, flags=re.DOTALL)
    
    # Write file
    with open(os.path.join(base_dir, article['filename']), 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Generate card HTML for index
    new_cards_html += f"""
        <a href="/blog/{article['filename']}" class="blog-card">
          <img src="{article['img']}" alt="Cover" class="blog-card-img">
          <div class="blog-card-header">
            <span class="blog-cat-tag {article['cat_class']}">{article['category'].split(' ')[0]}</span>
            <span class="blog-read-time">{article['read_time'].split(' ')[0]} min</span>
          </div>
          <div class="blog-card-body">
            <h3>{article['title']}</h3>
            <p>{article['desc']}</p>
            <div class="blog-card-footer">
              <span class="blog-date">{article['date']}</span>
              <span class="blog-arrow">→</span>
            </div>
          </div>
        </a>
"""

# Update index.html
index_path = os.path.join(base_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Insert cards after <div class="blog-grid">
index_content = index_content.replace('<div class="blog-grid">', '<div class="blog-grid">\n' + new_cards_html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Created 3 articles and updated index.html successfully.")
