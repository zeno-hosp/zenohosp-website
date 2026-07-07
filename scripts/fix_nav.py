import os

def fix_service_navbars():
    base_dir = "/Users/iniyananbu/Documents/ZenoHosp Website"
    
    # 1. Read index.html to extract the correct desktop + mobile navbars
    with open(os.path.join(base_dir, "index.html"), "r") as f:
        index_content = f.read()
    
    # Extract from <nav class="navbar marketing-navbar" id="main-nav"> up to the end of <div class="mobile-nav-menu marketing-mobile-nav" id="mobile-menu">
    # We can use split or regex.
    start_str = '<nav class="navbar marketing-navbar" id="main-nav">'
    end_str = '  </div>\n  <!-- Hero Section -->'
    
    if start_str not in index_content or end_str not in index_content:
        print("Could not find navbar in index.html")
        return
        
    correct_nav_content = start_str + index_content.split(start_str)[1].split(end_str)[0] + '  </div>'
    
    # 2. Files to update
    files_to_update = [
        "services/digital-presence/index.html",
        "services/custom-software/index.html",
        "services/social-media/index.html"
    ]
    
    for file_path in files_to_update:
        full_path = os.path.join(base_dir, file_path)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, "r") as f:
            content = f.read()
            
        # The service pages currently have <nav class="navbar marketing-navbar" id="main-nav"> ... </nav>
        # And NO mobile nav. They end the nav section before <!-- Hero Section -->
        
        target_end_str = '  <!-- Hero Section -->'
        
        if start_str not in content or target_end_str not in content:
            print(f"Could not find navbar block in {file_path}")
            continue
            
        # Replace the entire block
        new_content = content.split(start_str)[0] + correct_nav_content + "\n" + target_end_str + content.split(target_end_str)[1]
        
        with open(full_path, "w") as f:
            f.write(new_content)
        
        print(f"Updated {file_path}")

if __name__ == "__main__":
    fix_service_navbars()
