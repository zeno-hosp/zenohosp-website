#!/usr/bin/env python3
"""
update_missing_seo.py — Comprehensive SEO repair and gap filling across all pages.

1. Fixes broken contact link (/pricing/contact-us.html#contact-form -> /contact-us/#contact-form)
2. Fixes missing alt attribute on noscript pixel in index.html
3. Fixes 404 image reference (og-security.png -> hero-doctors.png) in security/index.html
4. Standardizes title branding in resources/hospital-management-software-cost-india.html
5. Fixes module pricing canonicals to self-canonicalize (matching sitemap and other modules)
6. Updates boilerplate og:description & twitter:description with page-specific meta descriptions
7. Completes Open Graph tags (og:type, og:site_name, og:url, og:title, og:description, og:image)
8. Completes Twitter Card tags (twitter:card, twitter:url, twitter:title, twitter:description, twitter:image)
9. Injects Organization & SoftwareApplication JSON-LD schema into pages missing entity markup
"""

import os
import glob
import re
import html
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://www.zenohosp.com"
DEFAULT_OG_IMAGE = f"{SITE_URL}/images/hero-doctors.png"
BRAND = "ZenoHosp"

DRY_RUN = "--dry-run" in sys.argv or "--apply" not in sys.argv

def get_canonical_url(rel_path):
    if rel_path == "index.html":
        return f"{SITE_URL}/"
    if rel_path.endswith("/index.html"):
        return f"{SITE_URL}/{rel_path[:-len('index.html')]}"
    if rel_path.endswith(".html"):
        return f"{SITE_URL}/{rel_path[:-len('.html')]}/"
    return f"{SITE_URL}/{rel_path}/"

def clean_text(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    return " ".join(html.unescape(text).split()).strip()

ORGANIZATION_SCHEMA = """  <script type=\"application/ld+json\">
{
  \"@context\": \"https://schema.org\",
  \"@type\": \"Organization\",
  \"name\": \"ZenoHosp\",
  \"alternateName\": [
    \"ZenoHosp\",
    \"Zenohosp\",
    \"Zeno Hosp\",
    \"ZenoHosp HMS\",
    \"zenohosp.com\"
  ],
  \"url\": \"https://www.zenohosp.com/\",
  \"logo\": \"https://www.zenohosp.com/images/zenohosp-b.svg\",
  \"description\": \"ZenoHosp is a technology corporation and software developer of cloud-based Hospital Management Software (HMS), EMR, clinic POS, and electronic health record systems. ZenoHosp is a software enterprise and is not a drug, medication, or pharmaceutical product.\",
  \"areaServed\": {
    \"@type\": \"Country\",
    \"name\": \"India\"
  },
  \"contactPoint\": {
    \"@type\": \"ContactPoint\",
    \"telephone\": \"+91-8056159395\",
    \"contactType\": \"customer service\",
    \"areaServed\": \"IN\",
    \"availableLanguage\": [
      \"English\",
      \"Hindi\",
      \"Tamil\"
    ]
  },
  \"sameAs\": [
    \"https://www.linkedin.com/company/zenohosp\",
    \"https://www.instagram.com/zenohosp/\",
    \"https://x.com/zenohosp\"
  ]
}
</script>
  <script type=\"application/ld+json\">
{
  \"@context\": \"https://schema.org\",
  \"@type\": \"SoftwareApplication\",
  \"name\": \"ZenoHosp Hospital Management Software\",
  \"description\": \"ZenoHosp is the leading Hospital Management Software (HMS) suite in India, unifying EMR, OPD, IPD, OT scheduling, pharmacy, and laboratory workflows on a single cloud platform.\",
  \"applicationCategory\": \"HealthcareBusinessApplication\",
  \"operatingSystem\": \"Web-based, Cloud, On-Premise\",
  \"offers\": {
    \"@type\": \"Offer\",
    \"price\": \"0\",
    \"priceCurrency\": \"INR\",
    \"description\": \"Free demo available for hospitals in India\"
  }
}
</script>"""

def process_file(file_path):
    rel_path = os.path.relpath(file_path, BASE_DIR).replace(os.sep, '/')
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    orig = content
    changes = []
    
    # 1. Broken link fix: /pricing/contact-us.html#contact-form -> /contact-us/#contact-form
    if '/pricing/contact-us.html#contact-form' in content:
        content = content.replace('/pricing/contact-us.html#contact-form', '/contact-us/#contact-form')
        changes.append("Fixed broken contact-us link")
        
    # 2. Missing alt in index.html noscript Facebook pixel
    if rel_path == 'index.html' and 'style="display:none"\n    src="https://www.facebook.com/tr?id=' in content:
        content = re.sub(
            r'(<img height="1" width="1" style="display:none"\s*\n?\s*src="https://www.facebook.com/tr\?[^"]*")\s*/?>',
            r'\1 alt="" />',
            content
        )
        changes.append("Added alt attribute to noscript pixel image")
        
    # 3. 404 image reference in security/index.html
    if 'images/og-security.png' in content:
        content = content.replace('https://www.zenohosp.com/images/og-security.png', DEFAULT_OG_IMAGE)
        content = content.replace('/images/og-security.png', DEFAULT_OG_IMAGE)
        changes.append("Fixed 404 og-security.png to hero-doctors.png")
        
    # 4. Standardize cost guide title
    if rel_path == 'resources/hospital-management-software-cost-india.html':
        old_title = "<title>Hospital Management Software Cost in India (2026 Price Guide)</title>"
        new_title = "<title>Hospital Management Software Cost in India (2026 Price Guide) | ZenoHosp</title>"
        if old_title in content:
            content = content.replace(old_title, new_title)
            changes.append("Added | ZenoHosp brand to title")
            
    # 5. Fix module pricing canonicals
    if rel_path in [
        'apps/asset/pricing/index.html',
        'apps/finance/pricing/index.html',
        'apps/hms/pricing/index.html',
        'apps/inventory/pricing/index.html',
        'apps/people/pricing/index.html'
    ]:
        correct_canon = get_canonical_url(rel_path)
        content = re.sub(
            r'<link\s+rel="canonical"\s+href="https://www.zenohosp\.com/pricing/"\s*/?>',
            f'<link rel="canonical" href="{correct_canon}">',
            content
        )
        changes.append(f"Fixed canonical to self-referencing {correct_canon}")
        
    # Extract page metadata
    title_m = re.search(r'<title>(.*?)</title>', content, re.I | re.S)
    page_title = clean_text(title_m.group(1)) if title_m else "Hospital Management Software & Healthcare Solutions | ZenoHosp"
    
    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content="([^"]*)"', content, re.I)
    if not desc_m:
        desc_m = re.search(r'<meta\s+content="([^"]*)"\s+name=["\']description["\']', content, re.I)
    page_desc = desc_m.group(1).strip() if desc_m else ""
    
    canonical_url = get_canonical_url(rel_path)
    # Check if page already has canonical
    canon_m = re.search(r'<link\s+[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', content, re.I)
    if canon_m:
        canonical_url = canon_m.group(1).strip()
        
    # Check og:image
    og_img_m = re.search(r'<meta\s+(?:property|name)=["\']og:image["\']\s+content="([^"]*)"', content, re.I)
    if not og_img_m:
        og_img_m = re.search(r'<meta\s+content="([^"]*)"\s+(?:property|name)=["\']og:image["\']', content, re.I)
    page_og_img = og_img_m.group(1).strip() if og_img_m else DEFAULT_OG_IMAGE
    
    # 6. Replace boilerplate og:description and twitter:description
    boilerplate_str = "ZenoHosp is an advanced Hospital Management System (HMS). Discover Hospital Management Software & Healthcare Solutions for your healthcare facility."
    if boilerplate_str in content and page_desc:
        content = content.replace(boilerplate_str, html.escape(page_desc, quote=True))
        changes.append("Replaced boilerplate og:description with page description")
        
    # 7. Check & inject/update OpenGraph and Twitter tags
    head_end = content.find('</head>')
    if head_end != -1:
        head_part = content[:head_end]
        
        # Check OpenGraph elements
        has_og_type = 'property="og:type"' in head_part or 'name="og:type"' in head_part
        has_og_site = 'property="og:site_name"' in head_part or 'name="og:site_name"' in head_part
        has_og_url = 'property="og:url"' in head_part or 'name="og:url"' in head_part
        has_og_title = 'property="og:title"' in head_part or 'name="og:title"' in head_part
        has_og_desc = 'property="og:description"' in head_part or 'name="og:description"' in head_part
        has_og_img = 'property="og:image"' in head_part or 'name="og:image"' in head_part
        
        # Check Twitter elements
        has_tw_card = 'name="twitter:card"' in head_part or 'property="twitter:card"' in head_part
        has_tw_url = 'name="twitter:url"' in head_part or 'property="twitter:url"' in head_part
        has_tw_title = 'name="twitter:title"' in head_part or 'property="twitter:title"' in head_part
        has_tw_desc = 'name="twitter:description"' in head_part or 'property="twitter:description"' in head_part
        has_tw_img = 'name="twitter:image"' in head_part or 'property="twitter:image"' in head_part
        
        # If thank-you page or other page has no OG/Twitter tags at all
        og_type = "article" if ("/blog/" in rel_path or "/webinars/" in rel_path) else "website"
        
        missing_tags = []
        if not has_og_type:
            missing_tags.append(f'  <meta property="og:type" content="{og_type}">')
        if not has_og_site:
            missing_tags.append('  <meta property="og:site_name" content="ZenoHosp">')
        if not has_og_url:
            missing_tags.append(f'  <meta property="og:url" content="{canonical_url}">')
        if not has_og_title:
            missing_tags.append(f'  <meta property="og:title" content="{html.escape(page_title, quote=True)}">')
        if not has_og_desc and page_desc:
            missing_tags.append(f'  <meta property="og:description" content="{html.escape(page_desc, quote=True)}">')
        if not has_og_img:
            missing_tags.append(f'  <meta property="og:image" content="{page_og_img}">')
            
        if not has_tw_card:
            missing_tags.append('  <meta property="twitter:card" content="summary_large_image">')
        if not has_tw_url:
            missing_tags.append(f'  <meta property="twitter:url" content="{canonical_url}">')
        if not has_tw_title:
            missing_tags.append(f'  <meta property="twitter:title" content="{html.escape(page_title, quote=True)}">')
        if not has_tw_desc and page_desc:
            missing_tags.append(f'  <meta property="twitter:description" content="{html.escape(page_desc, quote=True)}">')
        if not has_tw_img:
            missing_tags.append(f'  <meta property="twitter:image" content="{page_og_img}">')
            
        if missing_tags:
            block = "\n" + "\n".join(missing_tags) + "\n"
            # Insert before </head> or after existing OG tags
            last_og = re.search(r'<meta\s+(?:property|name)=["\'](?:og|twitter):[^>]*>\n?', content)
            if last_og:
                # Find the last meta property tag in head
                all_metas = list(re.finditer(r'<meta\s+(?:property|name)=["\'](?:og|twitter):[^>]*>\n?', content[:head_end]))
                pos = all_metas[-1].end()
                content = content[:pos] + "\n".join(missing_tags) + "\n" + content[pos:]
            else:
                # Insert right before </head>
                content = content[:head_end] + block + content[head_end:]
            changes.append(f"Added {len(missing_tags)} missing OG/Twitter tags")
            
    # 8. Schema injection for pages missing Organization schema
    if rel_path in [
        'for-doctors/index.html',
        'for-founders/index.html',
        'services/custom-software/index.html',
        'services/digital-presence/index.html'
    ] and '"@type": "Organization"' not in content:
        head_end = content.find('</head>')
        if head_end != -1:
            content = content[:head_end] + "\n" + ORGANIZATION_SCHEMA + "\n" + content[head_end:]
            changes.append("Injected Organization & SoftwareApplication JSON-LD schema")
            
    if content != orig:
        if not DRY_RUN:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        return rel_path, changes
    return rel_path, None

def main():
    pages = [p for p in sorted(glob.glob(os.path.join(BASE_DIR, '**', '*.html'), recursive=True))
             if not any(skip in p for skip in ['/components/', '/.git/', '/node_modules/', 'google8d5ba0a9486bf4c0'])]
    
    mode = "DRY RUN (no files modified)" if DRY_RUN else "APPLYING CHANGES"
    print(f"=== update_missing_seo.py ({mode}) ===")
    print(f"Scanning {len(pages)} pages...\n")
    
    modified_count = 0
    for p in pages:
        rel_path, changes = process_file(p)
        if changes:
            modified_count += 1
            print(f"• {rel_path}:")
            for c in changes:
                print(f"    - {c}")
                
    print(f"\nTotal pages updated: {modified_count} / {len(pages)}")
    if DRY_RUN:
        print("\nTo apply these updates, run with --apply")

if __name__ == '__main__':
    main()
