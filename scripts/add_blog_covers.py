import os
import glob
import re

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
blog_dir = os.path.join(directory, 'blog')

# 1. Update CSS
css_path = os.path.join(directory, 'css', 'pages', 'blog.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.blog-card-img' not in css_content:
    css_content += "\n.blog-card-img { width: 100%; height: 200px; object-fit: cover; display: block; border-bottom: 1px solid #eee; }\n"
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

# 2. Update blog/index.html
index_html_path = os.path.join(blog_dir, 'index.html')
with open(index_html_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Add background to featured article
if "background: url('/images/blog-cover-1.jpg')" not in index_content:
    index_content = index_content.replace(
        '<div class="featured-article-visual">',
        '<div class="featured-article-visual" style="background: linear-gradient(135deg, rgba(10,14,26,0.8) 0%, rgba(15,32,64,0.8) 100%), url(\'/images/blog-cover-1.jpg\') center/cover;">'
    )

# Add images to blog cards (alternate 1 and 2)
cards = re.split(r'(<a [^>]*class="blog-card"[^>]*>)', index_content)
new_index_content = cards[0]

img_idx = 2 # Start with 2 since featured uses 1
for i in range(1, len(cards), 2):
    tag = cards[i]
    body = cards[i+1]
    
    # Check if already has img
    if 'class="blog-card-img"' not in body:
        img_tag = f'\n          <img src="/images/blog-cover-{img_idx}.jpg" alt="Cover" class="blog-card-img">'
        body = img_tag + body
        
    new_index_content += tag + body
    img_idx = 1 if img_idx == 2 else 2

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(new_index_content)

# 3. Update individual blog posts
blog_files = glob.glob(os.path.join(blog_dir, '*.html'))
img_idx = 1
for file_path in blog_files:
    if os.path.basename(file_path) == 'index.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Update style if not exists
    if '.blog-article-hero-img' not in content:
        style_addition = """
      .blog-article-hero-img {
          max-width: 800px;
          width: 100%;
          height: auto;
          max-height: 400px;
          object-fit: cover;
          border-radius: 16px;
          margin: 40px auto 0 auto;
          display: block;
      }"""
        content = content.replace('</style>', style_addition + '\n    </style>')
        
    # Inject image into hero
    if 'class="blog-article-hero-img"' not in content:
        hero_img_html = f'\n      <div class="container">\n        <img src="/images/blog-cover-{img_idx}.jpg" class="blog-article-hero-img" alt="Blog Cover Image">\n      </div>\n    </section>'
        content = re.sub(r'(<section class="blog-article-hero">.*?)(</section>)', r'\1' + hero_img_html, content, flags=re.DOTALL)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    img_idx = 2 if img_idx == 1 else 1

print("Cover images applied to all blogs.")
