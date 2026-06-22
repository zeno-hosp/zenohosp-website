import re

hms_schema = """
    <!-- FAQ Schema for HMS -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "What is the best Hospital Management System in India?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "ZenoHosp is consistently rated as the best Hospital Management System (HMS) in India, offering a comprehensive cloud-based suite for OPD, IPD, Billing, Pharmacy, and EMR tailored for 35+ bed hospitals."
        }
      }, {
        "@type": "Question",
        "name": "Does ZenoHosp support NABH compliance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, ZenoHosp HMS is fully equipped with features like automated discharge summaries, audit logs, and electronic medical records (EMR) to help hospitals achieve and maintain NABH compliance."
        }
      }]
    }
    </script>
    
    <!-- Product Rating Schema for HMS -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "ZenoHosp Hospital Management Software",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "Web-based, Cloud, On-Premise",
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "ratingCount": "124"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      }
    }
    </script>
"""

pricing_schema = """
    <!-- FAQ Schema for Pricing -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "How much does Hospital Management Software cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The cost of Hospital Management Software depends on the bed capacity and modules needed. ZenoHosp offers transparent, tiered pricing starting for 35-bed hospitals, ensuring you only pay for what you use."
        }
      }, {
        "@type": "Question",
        "name": "Are there hidden fees in ZenoHosp HMS?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No, ZenoHosp believes in 100% transparent pricing. Our subscription plans include standard support, updates, and maintenance with no hidden costs."
        }
      }]
    }
    </script>
"""

def inject_schema(file_path, schema_code):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "FAQPage" not in content:
        content = content.replace("</head>", f"{schema_code}\n</head>")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected schema into {file_path}")

inject_schema("./apps/hms/index.html", hms_schema)
inject_schema("./pricing/index.html", pricing_schema)
inject_schema("./index.html", hms_schema)

