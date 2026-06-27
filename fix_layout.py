import re

with open('apps/people/index.html', 'r') as f:
    html = f.read()

# Fix the DOM order for feature-alt-left (Feature 2 and Feature 5)
# They currently have feature-visual then feature-content. We need feature-content then feature-visual.
# Let's find sections with feature-alt-left

def swap_visual_content(match):
    visual_block = match.group(1)
    content_block = match.group(2)
    return content_block + "\n      " + visual_block

# A bit risky to regex HTML, let's use a simpler approach.
# Feature 2 starts at <!-- Feature 2: Attendance & Leave -->
# It has <div class="feature-visual"> ... </div> then <div class="feature-content"> ... </div>
import bs4

soup = bs4.BeautifulSoup(html, 'html.parser')

alt_left_sections = soup.find_all('section', class_='feature-alt-left')
for section in alt_left_sections:
    container = section.find('div', class_='container')
    if container:
        visual = container.find('div', class_='feature-visual')
        content = container.find('div', class_='feature-content')
        if visual and content:
            # Check their order in the container
            children = list(container.children)
            visual_idx = children.index(visual)
            content_idx = children.index(content)
            
            if visual_idx < content_idx:
                # Extract visual and insert after content
                visual.extract()
                content.insert_after(visual)

# Now fix the visuals and text mapping
# Feature 1: "Hospital HR Management & Onboarding" -> Needs an HR visual
# Feature 2: "Smart Duty Rostering & Attendance" -> Needs the Roster visual
# Feature 2 is currently using the Attendance visual (which we might just replace with the Roster visual)

# Wait, let's just create a new HR visual for Feature 1, and move the Roster visual to Feature 2.
# Let's grab the original visuals.
feature1 = soup.find('section', id='features') # Feature 1
feat1_visual = feature1.find('div', class_='feature-visual')

hr_visual_html = """
<div class="feature-visual">
  <div style="background:#fff;border:1px solid #e5e7eb;border-radius:12px;overflow:hidden;max-width:380px;margin:0 auto;box-shadow:0 15px 35px rgba(0,0,0,0.05);">
    <div style="background:#2D8A6E;padding:20px;display:flex;align-items:center;gap:16px;">
      <div style="width:56px;height:56px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;font-size:1.5rem;">👩‍⚕️</div>
      <div>
        <div style="font-weight:700;color:#fff;font-size:1.1rem;">Dr. Ananya Sharma</div>
        <div style="font-size:.8rem;color:rgba(255,255,255,.8);">Senior Cardiologist • ID: EMP-1042</div>
      </div>
    </div>
    <div style="padding:20px;">
      <div style="font-size:.8rem;font-weight:600;color:#555;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;">Digital Vault</div>
      
      <div style="display:flex;align-items:center;justify-content:space-between;padding:12px;background:#f9fafb;border-radius:8px;margin-bottom:8px;border:1px solid #eee;">
        <div style="display:flex;align-items:center;gap:12px;">
          <div style="font-size:1.2rem;">📄</div>
          <div>
            <div style="font-weight:600;font-size:.85rem;color:#333;">Medical Council License</div>
            <div style="font-size:.7rem;color:#888;">Valid till Dec 2028</div>
          </div>
        </div>
        <span style="background:#d1fae5;color:#065f46;padding:4px 10px;border-radius:20px;font-size:.7rem;font-weight:600;">Verified</span>
      </div>

      <div style="display:flex;align-items:center;justify-content:space-between;padding:12px;background:#f9fafb;border-radius:8px;margin-bottom:8px;border:1px solid #eee;">
        <div style="display:flex;align-items:center;gap:12px;">
          <div style="font-size:1.2rem;">📜</div>
          <div>
            <div style="font-weight:600;font-size:.85rem;color:#333;">Employment Contract</div>
            <div style="font-size:.7rem;color:#888;">Signed Jan 2024</div>
          </div>
        </div>
        <span style="background:#d1fae5;color:#065f46;padding:4px 10px;border-radius:20px;font-size:.7rem;font-weight:600;">Active</span>
      </div>

      <div style="display:flex;align-items:center;justify-content:space-between;padding:12px;background:#fff5f5;border-radius:8px;border:1px solid #fee2e2;">
        <div style="display:flex;align-items:center;gap:12px;">
          <div style="font-size:1.2rem;">🎓</div>
          <div>
            <div style="font-weight:600;font-size:.85rem;color:#991b1b;">BLS Certification</div>
            <div style="font-size:.7rem;color:#dc2626;">Expires in 14 days</div>
          </div>
        </div>
        <button style="background:#dc2626;color:#fff;border:none;border-radius:6px;padding:6px 12px;font-size:.7rem;font-weight:600;cursor:pointer;">Send Alert</button>
      </div>

    </div>
  </div>
</div>
"""
new_hr_visual = bs4.BeautifulSoup(hr_visual_html, 'html.parser')

roster_visual = feat1_visual.extract()
feature1.find('div', class_='container').append(new_hr_visual)

feature2 = alt_left_sections[0] # The second feature (which is alt-left)
feat2_visual = feature2.find('div', class_='feature-visual')
# We replace feat2_visual with roster_visual
feat2_visual.replace_with(roster_visual)


with open('apps/people/index.html', 'w') as f:
    f.write(str(soup))

print("Layout and visuals fixed!")
