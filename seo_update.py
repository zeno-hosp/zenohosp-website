import re

seo_data = {
    "./index.html": {
        "title": "Best Hospital Management Software (HMS) in India | ZenoHosp",
        "description": "ZenoHosp is India's leading Hospital Management Software (HMS). Streamline your clinic or hospital with our unified EMR, OPD, IPD, and billing platform.",
        "keywords": "Best Hospital Management Software, Best HMS Software India, Top Hospital Software, Clinic Management System, ZenoHosp, EMR, Healthcare Automation"
    },
    "./apps/hms/index.html": {
        "title": "Best Hospital Management System (HMS) & EMR | ZenoHosp",
        "description": "Looking for the best hospital software? ZenoHosp is a top-rated Hospital Management System (HMS) that unifies your OPD, IPD, and Billing on a single enterprise platform.",
        "keywords": "Best Hospital Software, Best Hospital Management Software, Hospital Management System (HMS), Electronic Medical Records (EMR), Top Hospital Software, Hospital Billing System"
    },
    "./apps/pharmacy/index.html": {
        "title": "Best Hospital Pharmacy Management Software | ZenoHosp",
        "description": "Optimize your hospital pharmacy with ZenoHosp's advanced pharmacy management software. Handle inventory, expiry alerts, dispensing, and GST billing effortlessly.",
        "keywords": "Hospital Pharmacy Software, Pharmacy Management System, Best Pharmacy Billing Software, Medical Store Software, Drug Inventory System, ZenoHosp Pharmacy"
    },
    "./apps/ot-room/index.html": {
        "title": "Top Operation Theatre (OT) Management Software | ZenoHosp",
        "description": "Streamline surgical schedules with ZenoHosp's OT Management Software. Manage surgeons, operation theatres, consumables, and checklists on one platform.",
        "keywords": "OT Management Software, Operation Theatre Scheduling Software, Surgery Management System, Hospital OT Software, ZenoHosp OT Module"
    },
    "./apps/inventory/index.html": {
        "title": "Best Hospital Inventory Management Software | ZenoHosp",
        "description": "Prevent stockouts and reduce wastage with ZenoHosp's hospital inventory software. Track medical stock, automate POs, and manage multiple stores seamlessly.",
        "keywords": "Hospital Inventory Management Software, Medical Inventory System, Hospital Stock Management, Healthcare Inventory Software, ZenoHosp Inventory"
    },
    "./apps/lab/index.html": {
        "title": "Best Laboratory Information System (LIS) Software | ZenoHosp",
        "description": "Automate your pathology lab with ZenoHosp LIS. Connect analyzers, track samples, and deliver fast, accurate test reports with our integrated laboratory software.",
        "keywords": "Laboratory Information System, Best LIS Software, Pathology Lab Software, Diagnostic Lab Management System, ZenoHosp Lab Module"
    },
    "./pricing/index.html": {
        "title": "Hospital Management Software Pricing | ZenoHosp Cost",
        "description": "Affordable and transparent pricing for the best hospital management software. Calculate your ZenoHosp HMS cost based on hospital bed capacity.",
        "keywords": "Hospital Management Software Pricing, HMS Cost in India, ZenoHosp Pricing, EMR Software Cost, Clinic Software Price"
    }
}

for file_path, tags in seo_data.items():
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace Title
        content = re.sub(r'<title>.*?</title>', f'<title>{tags["title"]}</title>', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Replace Description
        if '<meta name="description"' in content:
            content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*/?>', f'<meta name="description" content="{tags["description"]}">', content, flags=re.IGNORECASE | re.DOTALL)
        else:
            # Insert before </head>
            content = content.replace('</head>', f'    <meta name="description" content="{tags["description"]}">\n</head>')
            
        # Replace Keywords
        if '<meta name="keywords"' in content:
            content = re.sub(r'<meta\s+name=["\']keywords["\']\s+content=["\'].*?["\']\s*/?>', f'<meta name="keywords" content="{tags["keywords"]}">', content, flags=re.IGNORECASE | re.DOTALL)
        else:
            # Insert before </head>
            content = content.replace('</head>', f'    <meta name="keywords" content="{tags["keywords"]}">\n</head>')

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated SEO for {file_path}")
    except Exception as e:
        print(f"Failed {file_path}: {e}")

