import os
import glob
import re

desktop_dropdown_html = """        <li class="has-dropdown">
          <a href="#" class="dropdown-trigger">Services <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></a>
          <div class="nav-dropdown">
            <div class="dropdown-content">
              <a href="/services/digital-presence/index.html" class="dropdown-item">
                <div class="dropdown-icon" style="background: rgba(59, 130, 246, 0.1); color: #3b82f6; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                </div>
                <div class="dropdown-info">
                  <strong>Create Website</strong>
                  <span>Digital presence & SEO</span>
                </div>
              </a>
              <a href="/services/custom-software/index.html" class="dropdown-item">
                <div class="dropdown-icon" style="background: rgba(249, 115, 22, 0.1); color: #f97316; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>
                </div>
                <div class="dropdown-info">
                  <strong>Custom Software</strong>
                  <span>Bespoke hospital modules</span>
                </div>
              </a>
            </div>
          </div>
        </li>"""

mobile_dropdown_html = """      <li>
        <div class="dropdown-label" id="services-toggle">
          Services
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </div>
        <div class="mobile-dropdown" id="services-dropdown">
          <a href="/services/digital-presence/index.html">Create Website</a>
          <a href="/services/custom-software/index.html">Custom Software</a>
        </div>
      </li>"""

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Skip if dropdown already exists
    if 'id="services-toggle"' in content or '<strong>Create Website</strong>' in content:
        return False

    # Remove any standalone Services link if we previously added it manually
    content = re.sub(r'[\t ]*<li><a href="/services/index\.html">Services</a></li>\n?', '', content)

    # Find the target link: <li><a href="/solutions/index.html">Solutions</a></li>
    # It might have varying whitespace before it.
    pattern = re.compile(r'([ \t]*)<li><a href="/solutions/index\.html">Solutions</a></li>')
    matches = list(pattern.finditer(content))
    
    if len(matches) >= 2:
        # Assuming first match is desktop and second is mobile
        # We process from back to front to avoid messing up string indices
        m2 = matches[1]
        m1 = matches[0]
        
        # Replace mobile
        indent2 = m2.group(1)
        replacement2 = mobile_dropdown_html + '\n' + indent2 + '<li><a href="/solutions/index.html">Solutions</a></li>'
        content = content[:m2.start()] + replacement2 + content[m2.end():]
        
        # Replace desktop
        indent1 = m1.group(1)
        replacement1 = desktop_dropdown_html + '\n' + indent1 + '<li><a href="/solutions/index.html">Solutions</a></li>'
        content = content[:m1.start()] + replacement1 + content[m1.end():]
        
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    elif len(matches) == 1:
        # If only one match, it's likely desktop (maybe a broken page)
        m1 = matches[0]
        indent1 = m1.group(1)
        replacement1 = desktop_dropdown_html + '\n' + indent1 + '<li><a href="/solutions/index.html">Solutions</a></li>'
        content = content[:m1.start()] + replacement1 + content[m1.end():]
        with open(filepath, 'w') as f:
            f.write(content)
        return True

    return False

if __name__ == '__main__':
    html_files = glob.glob('**/*.html', recursive=True)
    count = 0
    for file in html_files:
        if process_file(file):
            count += 1
    print(f"Updated {count} HTML files.")
