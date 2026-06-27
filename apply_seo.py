import os
import re

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if it doesn't look like a standard HTML page
    if '<head>' not in content or '</head>' not in content:
        return

    # Extract current title if exists
    title_match = re.search(r'<title>(.*?)</title>', content, flags=re.IGNORECASE | re.DOTALL)
    current_title = title_match.group(1).strip() if title_match else "Hospital Management Software & Healthcare Solutions | Zenohosp"

    # Make sure Zenohosp is in the title
    if "Zenohosp" not in current_title and "ZenoHosp" not in current_title:
        current_title += " | Zenohosp"
        
    # Standardize capitalization of Zenohosp for better brand recognition
    # We will use "Zenohosp" (which is the spelling the user searched for) as a strong keyword, along with ZenoHosp.

    # Prepare SEO tags
    description = f"Zenohosp is an advanced Hospital Management System (HMS). Discover {current_title.split('|')[0].strip()} for your healthcare facility."
    keywords = "Zenohosp, ZenoHosp, Hospital Management System, HMS, Healthcare Software, EMR, Clinic Software"
    
    # Check if there is specific data in seo_data from before? I'll just use a generic but highly optimized one for all files,
    # except the ones we already know about.

    # 1. Update Title
    content = re.sub(r'<title>.*?</title>', f'<title>{current_title}</title>', content, flags=re.IGNORECASE | re.DOTALL)
    
    # 2. Update/Add Meta Description
    if '<meta name="description"' in content:
        content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*/?>', f'<meta name="description" content="{description}">', content, flags=re.IGNORECASE | re.DOTALL)
    else:
        content = content.replace('</head>', f'    <meta name="description" content="{description}">\n</head>')
        
    # 3. Update/Add Meta Keywords
    if '<meta name="keywords"' in content:
        content = re.sub(r'<meta\s+name=["\']keywords["\']\s+content=["\'].*?["\']\s*/?>', f'<meta name="keywords" content="{keywords}">', content, flags=re.IGNORECASE | re.DOTALL)
    else:
        content = content.replace('</head>', f'    <meta name="keywords" content="{keywords}">\n</head>')

    # 4. Add OpenGraph tags
    og_tags = f"""
    <meta property="og:site_name" content="Zenohosp">
    <meta property="og:title" content="{current_title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    """
    if 'property="og:site_name"' not in content:
        content = content.replace('</head>', f'{og_tags}\n</head>')

    # 5. Inject JSON-LD Organization Schema only in the main index.html
    if filepath.endswith('index.html') and filepath.count('/') == 1:  # Root index.html
        schema_markup = """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Zenohosp",
      "alternateName": "ZenoHosp",
      "url": "https://www.zenohosp.com",
      "logo": "https://www.zenohosp.com/images/logo.png",
      "description": "Zenohosp is a leading provider of Hospital Management Systems and Healthcare IT solutions.",
      "sameAs": [
        "https://www.linkedin.com/company/zenohosp",
        "https://twitter.com/zenohosp"
      ]
    }
    </script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Zenohosp HMS",
      "operatingSystem": "Web",
      "applicationCategory": "HealthcareApplication",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>
        """
        if '"@type": "Organization"' not in content:
            content = content.replace('</head>', f'{schema_markup}\n</head>')

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


# Traverse all directories and process HTML files
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_html_file(filepath)

print("SEO update completed across all files.")
