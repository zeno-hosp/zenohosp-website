import os
import glob

old_desktop = """        <li class="has-dropdown">
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

new_desktop = """        <li class="has-dropdown">
          <a href="#" class="dropdown-trigger">Services <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></a>
          <div class="nav-dropdown">
            <div class="dropdown-content">
              <a href="/services/digital-presence/index.html" class="dropdown-item">
                <div class="dropdown-icon" style="background: rgba(59, 130, 246, 0.1); color: #3b82f6; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                </div>
                <div class="dropdown-info">
                  <strong>Hospital Websites</strong>
                  <span>Digital presence & SEO</span>
                </div>
              </a>
              <a href="/services/custom-software/index.html" class="dropdown-item">
                <div class="dropdown-icon" style="background: rgba(249, 115, 22, 0.1); color: #f97316; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>
                </div>
                <div class="dropdown-info">
                  <strong>Hospital Custom Software</strong>
                  <span>Bespoke hospital modules</span>
                </div>
              </a>
              <a href="/services/social-media/index.html" class="dropdown-item">
                <div class="dropdown-icon" style="background: rgba(168, 85, 247, 0.1); color: #a855f7; display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
                </div>
                <div class="dropdown-info">
                  <strong>Social Media Management</strong>
                  <span>Video & content by Zesignworks</span>
                </div>
              </a>
            </div>
          </div>
        </li>"""


old_mobile = """      <li>
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

new_mobile = """      <li>
        <div class="dropdown-label" id="services-toggle">
          Services
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </div>
        <div class="mobile-dropdown" id="services-dropdown">
          <a href="/services/digital-presence/index.html">Hospital Websites</a>
          <a href="/services/custom-software/index.html">Hospital Custom Software</a>
          <a href="/services/social-media/index.html">Social Media Management</a>
        </div>
      </li>"""

count = 0
for filepath in glob.glob('**/*.html', recursive=True):
    with open(filepath, 'r') as f:
        content = f.read()

    changed = False
    
    if old_desktop in content:
        content = content.replace(old_desktop, new_desktop)
        changed = True
        
    if old_mobile in content:
        content = content.replace(old_mobile, new_mobile)
        changed = True

    if changed:
        with open(filepath, 'w') as f:
            f.write(content)
        count += 1
        
print(f"Updated {count} HTML files.")
