import os

def apply_green_theme():
    file_path = "/Users/iniyananbu/Documents/ZenoHosp Website/services/custom-software/index.html"
    with open(file_path, 'r') as f:
        content = f.read()

    # Replace orange colors with green
    content = content.replace('#f97316', '#10b981')
    content = content.replace('rgba(249, 115, 22, 0.1)', 'rgba(16, 185, 129, 0.1)')
    
    # Let's also check if there are any inline SVGs that use orange in the CTA section. 
    # Or if there are orange classes.

    with open(file_path, 'w') as f:
        f.write(content)
    print("Green theme applied!")

if __name__ == "__main__":
    apply_green_theme()
