import os
import glob
import re

directory = '/Users/iniyananbu/Documents/Zeno Hosp Website'
apps_dir = os.path.join(directory, 'apps')

addon_apps = {
    'pharmacy': {
        'name': 'Pharmacy',
        'desc': 'Dispensing and stock management',
        'tiers': {
            'tier1': {'monthly': 2000, 'yearly': 1800},
            'tier2': {'monthly': 3500, 'yearly': 3150},
            'tier3': {'monthly': 5500, 'yearly': 4950},
            'tier4': {'monthly': 9000, 'yearly': 8100}
        }
    },
    'lab': {
        'name': 'Lab',
        'desc': 'Diagnostics and reporting',
        'tiers': {
            'tier1': {'monthly': 2500, 'yearly': 2250},
            'tier2': {'monthly': 4000, 'yearly': 3600},
            'tier3': {'monthly': 7000, 'yearly': 6300},
            'tier4': {'monthly': 11000, 'yearly': 9900}
        }
    },
    'ot-room': {
        'name': 'OT Room',
        'desc': 'Surgical scheduling and live dashboards',
        'tiers': {
            'tier1': {'monthly': 1000, 'yearly': 900},
            'tier2': {'monthly': 1700, 'yearly': 1530},
            'tier3': {'monthly': 2800, 'yearly': 2520},
            'tier4': {'monthly': 4500, 'yearly': 4050}
        }
    }
}

html_template = """<!DOCTYPE html>
<html lang="en" data-billing="monthly">

<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-27WDP0T7BZ"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-27WDP0T7BZ');
  </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Pricing for {app_name} Module.">
    <link rel="icon" type="image/x-icon" href="/images/fav.ico">
    <title>{app_name} Pricing | ZenoHosp Cost</title>

    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" as="style">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/main.css">
    <meta name="theme-color" content="#111827">

    <style>
    .standalone-calc {{
        background: var(--zd-white, #ffffff);
        border-radius: var(--zd-radius-xl, 24px);
        padding: 40px;
        border: 1px solid rgba(0,0,0,0.05);
        box-shadow: var(--zd-shadow-md, 0 4px 16px rgba(0,0,0,0.08));
        max-width: 600px;
        margin: 0 auto;
    }}
    .billing-toggle {{
        display: flex; justify-content: center; margin-bottom: 30px;
    }}
    .price-display {{
        font-size: 3.5rem; font-weight: 800; color: var(--zd-obsidian); margin: 20px 0;
    }}
    [data-billing="yearly"] .monthly-price {{ display: none; }}
    [data-billing="yearly"] .yearly-price {{ display: inline; }}
    [data-billing="monthly"] .monthly-price {{ display: inline; }}
    [data-billing="monthly"] .yearly-price {{ display: none; }}
    </style>
</head>

<body>

    {nav_content}

    <section class="pricing-hero reveal" style="padding-top: 60px; padding-bottom: 40px;">
        <div class="container" style="text-align: center;">
            <span class="hero-pill">{app_name} Pricing</span>
            <h1 style="margin-bottom: 16px;">{app_name} Module Pricing</h1>
            <p>{app_desc}</p>
        </div>
    </section>

    <section class="pricing-main reveal" style="padding-bottom: 80px;">
        <div class="container">
            <div class="standalone-calc">
                
                <div class="billing-toggle" role="group">
                    <button type="button" class="billing-btn active" data-billing="monthly">Monthly</button>
                    <button type="button" class="billing-btn" data-billing="yearly">Yearly (Billed Annually)</button>
                </div>

                <div style="margin-bottom: 24px;">
                    <label for="bed-count" style="display:block; font-size: 0.85rem; font-weight: 700; color: var(--zd-text-dark); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">Hospital Capacity</label>
                    <select id="bed-count" style="width: 100%; padding: 14px 16px; border: 1px solid rgba(0,0,0,0.1); border-radius: 8px; font-family: inherit; font-size: 1.05rem; background: #f9f9f9; cursor: pointer; outline: none; transition: border-color 0.2s;">
                        <option value="tier1" data-monthly="{t1m}" data-yearly="{t1y}">35 - 80 beds</option>
                        <option value="tier2" data-monthly="{t2m}" data-yearly="{t2y}">81 - 150 beds</option>
                        <option value="tier3" data-monthly="{t3m}" data-yearly="{t3y}">151 - 250 beds</option>
                        <option value="tier4" data-monthly="{t4m}" data-yearly="{t4y}">251+ beds</option>
                    </select>
                </div>

                <div style="text-align: center; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
                    <p style="color: var(--zd-text-muted); font-size: 0.95rem; margin: 0;">Total Price</p>
                    <div class="price-display">
                        <span class="monthly-price" id="display-monthly">₹{t1m_fmt}</span>
                        <span class="yearly-price" id="display-yearly">₹{t1y_fmt}</span>
                        <span style="font-size: 1.2rem; color: var(--zd-text-muted); font-weight: 500;">/mo</span>
                    </div>
                    <p id="billing-note" style="color: var(--zd-text-muted); font-size: 0.9rem; margin-bottom: 24px;">Billed monthly (+ GST)</p>
                    <a href="/contact-us/index.html" class="btn btn-primary" style="width: 100%; padding: 16px; font-size: 1.1rem;">Request Demo & Quote</a>
                </div>

            </div>
        </div>
    </section>

{footer_content}

<script>
document.addEventListener('DOMContentLoaded', () => {{
    const billingBtns = document.querySelectorAll('.billing-btn');
    const bedSelect = document.getElementById('bed-count');
    const displayMonthly = document.getElementById('display-monthly');
    const displayYearly = document.getElementById('display-yearly');
    const billingNote = document.getElementById('billing-note');
    
    // Toggle Billing
    billingBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
            billingBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const mode = btn.getAttribute('data-billing');
            document.documentElement.setAttribute('data-billing', mode);
            updatePrice();
        }});
    }});

    // Change bed count
    bedSelect.addEventListener('change', updatePrice);

    function formatCurrency(num) {{
        return new Intl.NumberFormat('en-IN').format(num);
    }}

    function updatePrice() {{
        const selectedOption = bedSelect.options[bedSelect.selectedIndex];
        const monthly = parseInt(selectedOption.getAttribute('data-monthly'), 10);
        const yearly = parseInt(selectedOption.getAttribute('data-yearly'), 10);

        displayMonthly.textContent = '₹' + formatCurrency(monthly);
        displayYearly.textContent = '₹' + formatCurrency(yearly);
        
        const mode = document.documentElement.getAttribute('data-billing');
        if(mode === 'yearly') {{
            billingNote.textContent = 'Billed annually (₹' + formatCurrency(yearly * 12) + '/year + GST)';
        }} else {{
            billingNote.textContent = 'Billed monthly (+ GST)';
        }}
    }}
}});
</script>
</body>
</html>
"""

# Extract footer from global pricing
with open(os.path.join(directory, 'pricing', 'index.html'), 'r', encoding='utf-8') as f:
    global_content = f.read()

footer_match = re.search(r'(<!-- Footer -->.*?)<script>', global_content, re.DOTALL)
footer_content = footer_match.group(1) if footer_match else ""

for app, config in addon_apps.items():
    app_index = os.path.join(apps_dir, app, 'index.html')
    if not os.path.exists(app_index):
        print(f"Skipping {app}, index not found.")
        continue
        
    with open(app_index, 'r', encoding='utf-8') as f:
        app_content = f.read()
        
    # Extract nav components from app
    nav_match = re.search(r'(<div class="platform-strip">.*?</header>)', app_content, re.DOTALL)
    mobile_match = re.search(r'(<div class="mobile-nav-overlay".*?</ul>\s*</div>)', app_content, re.DOTALL)
    
    if nav_match and mobile_match:
        app_nav = nav_match.group(1)
        app_mobile = mobile_match.group(1)
        
        # Replace href="/pricing/index.html" with href="/apps/app_name/pricing/index.html"
        app_nav = app_nav.replace('href="/pricing/index.html"', f'href="/apps/{app}/pricing/index.html"')
        app_mobile = app_mobile.replace('href="/pricing/index.html"', f'href="/apps/{app}/pricing/index.html"')
        
        full_nav = app_nav + "\n" + app_mobile
        
        t1m = config['tiers']['tier1']['monthly']
        t1y = config['tiers']['tier1']['yearly']
        
        page_html = html_template.format(
            app_name=config['name'],
            app_desc=config['desc'],
            nav_content=full_nav,
            footer_content=footer_content,
            t1m=t1m, t1y=t1y, t1m_fmt=f"{t1m:,}", t1y_fmt=f"{t1y:,}",
            t2m=config['tiers']['tier2']['monthly'], t2y=config['tiers']['tier2']['yearly'],
            t3m=config['tiers']['tier3']['monthly'], t3y=config['tiers']['tier3']['yearly'],
            t4m=config['tiers']['tier4']['monthly'], t4y=config['tiers']['tier4']['yearly']
        )
        
        out_dir = os.path.join(apps_dir, app, 'pricing')
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, 'index.html')
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
            
        print(f"Created standalone pricing page for {app}")
        
        # Now update all links in this app's folder
        html_files = glob.glob(os.path.join(apps_dir, app, '**/*.html'), recursive=True)
        for file_path in html_files:
            with open(file_path, 'r', encoding='utf-8') as f_html:
                html_c = f_html.read()
            
            new_html_c = html_c.replace('href="/pricing/index.html"', f'href="/apps/{app}/pricing/index.html"')
            
            if new_html_c != html_c:
                with open(file_path, 'w', encoding='utf-8') as f_html:
                    f_html.write(new_html_c)
                print(f"Updated links in {file_path}")
    else:
        print(f"Could not extract nav for {app}")
