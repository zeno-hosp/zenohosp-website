import os
from datetime import datetime

base_url = "https://zenohosp.com"
sitemap_path = "./sitemap.xml"

# List of paths to exclude from sitemap
exclude_paths = [
    "node_modules",
    "components",
    "google8d5ba0a9486bf4c0.html"
]

def should_exclude(path):
    for ex in exclude_paths:
        if ex in path:
            return True
    return False

urls = []

for root, _, files in os.walk("."):
    if should_exclude(root):
        continue
        
    for file in files:
        if file.endswith(".html") and not should_exclude(file):
            filepath = os.path.join(root, file)
            
            # Clean path to form URL
            url_path = filepath.replace("./", "/").replace("\\", "/")
            
            # Use directory paths instead of exact .html paths for root index files
            if url_path.endswith("index.html"):
                url_path = url_path.replace("index.html", "")
            
            full_url = f"{base_url}{url_path}"
            
            # Assign Priority
            priority = "0.6"
            changefreq = "monthly"
            
            if url_path == "/":
                priority = "1.0"
                changefreq = "weekly"
            elif "/apps/" in url_path and url_path.endswith("/"):
                priority = "0.9"
                changefreq = "weekly"
            elif "/pricing/" in url_path:
                priority = "0.9"
                changefreq = "weekly"
            elif "/features/" in url_path:
                priority = "0.8"
            elif "/docs/" in url_path:
                priority = "0.7"

            urls.append(f"""  <url>
    <loc>{full_url}</loc>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

print(f"Generated sitemap with {len(urls)} URLs")
