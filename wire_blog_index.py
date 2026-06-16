import re

with open('./blog/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the href="#" for the 5 articles. 
# We can search for the h3 titles and replace the preceding href="#"

replacements = [
    ("ABDM in 2026: What Every Hospital Administrator Needs to Know Before the Deadline", "/blog/abdm-compliance-2026.html"),
    ("How to Reduce OT Cancellations by 80% — A Step-by-Step Guide for Surgery Coordinators", "/blog/reduce-ot-cancellations.html"),
    ("GST Compliance for Hospitals: The Complete Guide to Getting Your Bills Right in 2026", "/blog/gst-compliance-hospitals.html"),
    ("Why Your Lab's Turnaround Time Is Killing Patient Trust — And the One Change That Fixes It", "/blog/lab-turnaround-time.html"),
    ("FIFO vs. FEFO for Hospital Pharmacy — Why Getting This Wrong Costs More Than You Think", "/blog/fifo-vs-fefo-pharmacy.html")
]

for title, url in replacements:
    # Find the block starting with <a href="#" class="blog-card"> up to the title
    # This regex looks for the nearest <a href="#"> before the title
    pattern = re.compile(r'<a href="#" class="blog-card">((?:(?!<a href).)*?<h3>' + re.escape(title) + r'</h3>)', re.DOTALL)
    content = pattern.sub(f'<a href="{url}" class="blog-card">\\1', content)

with open('./blog/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Blog index updated.")
