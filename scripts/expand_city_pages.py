#!/usr/bin/env python3
"""Add local FAQ content and FAQPage schema to the /hms-software/<city>/ pages.

Local queries are the winnable ones. "hospital management software chennai" is
contested by a handful of local vendors rather than by national listicle
publishers, and ZenoHosp is headquartered there with 40+ hospitals live in the
city. But the city pages carry only ~170 words, which is not enough to hold a
position against anyone who writes a real page.

This adds, per city: a short orientation paragraph, six locally-framed FAQs
answering what buyers actually ask (cost, language, implementation time, local
team, data residency, state compliance), matching FAQPage schema, and links into
the cost guide and comparison page.

CLAIMS RULE: the Chennai-specific proof points already on the site (40+
hospitals, Tier-IV data centres in the city, 90-day go-live) are reused only for
Chennai. Nothing equivalent is invented for the other four cities — where a fact
is not known, the copy stays general rather than inventing a number.
"""

import json
import pathlib
import re
import sys

CITIES = {
    "chennai": {
        "city": "Chennai",
        "state": "Tamil Nadu",
        "language": "Tamil",
        "intro": (
            "ZenoHosp is built in Chennai. Our implementation team, our support desk and "
            "our engineering are all in the city, which means a site visit is a drive "
            "across town rather than a flight and a ticket queue. We are live in 40+ "
            "hospitals and nursing homes across Chennai, from single-speciality nursing "
            "homes in Egmore to 300-bed multispeciality chains on OMR."
        ),
        "local_proof": (
            "Yes. ZenoHosp is headquartered in Chennai and our implementation team works "
            "on-site across the city. We commit to a 90-day go-live, and if we miss it we "
            "extend the engagement at no charge."
        ),
        "residency": (
            "For Chennai hospitals, patient data is hosted on Tier-IV infrastructure "
            "within the city, so DPDP Act data residency is something you can actually "
            "point to during an audit rather than take on trust."
        ),
    },
    "coimbatore": {
        "city": "Coimbatore",
        "state": "Tamil Nadu",
        "language": "Tamil",
        "intro": (
            "Coimbatore's hospital sector runs on a mix of long-established multispeciality "
            "institutions and fast-growing single-speciality centres. ZenoHosp is built in "
            "Tamil Nadu, supports Tamil natively, and our implementation team travels to "
            "Coimbatore for on-site rollout rather than running the whole project over "
            "video calls."
        ),
        "local_proof": (
            "Our team is based in Tamil Nadu and handles Coimbatore rollouts on-site. "
            "Implementation, training and go-live support all happen at your hospital."
        ),
        "residency": (
            "Patient data for Indian hospitals is hosted in Indian data centres, in line "
            "with DPDP Act residency expectations."
        ),
    },
    "bengaluru": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "language": "Kannada",
        "intro": (
            "Bengaluru hospitals tend to face a particular combination: patients who expect "
            "digital-first service, serious NABH documentation requirements, and a heavy "
            "mix of corporate and insurance billing. ZenoHosp handles the TPA and corporate "
            "rate-card side natively, which is usually where the reconciliation time goes."
        ),
        "local_proof": (
            "We run Bengaluru implementations with on-site support during rollout and "
            "training, followed by remote support from our team."
        ),
        "residency": (
            "Patient data for Indian hospitals is hosted in Indian data centres, in line "
            "with DPDP Act residency expectations."
        ),
    },
    "hyderabad": {
        "city": "Hyderabad",
        "state": "Telangana",
        "language": "Telugu",
        "intro": (
            "Hyderabad's hospital market spans large corporate chains and a deep base of "
            "independent multispeciality hospitals in the 50–250 bed range — which is "
            "exactly the band ZenoHosp is built for. The platform covers OPD, IPD, wards, "
            "OT, pharmacy and lab on one ledger."
        ),
        "local_proof": (
            "We run Hyderabad implementations with on-site support during rollout and "
            "training, followed by remote support from our team."
        ),
        "residency": (
            "Patient data for Indian hospitals is hosted in Indian data centres, in line "
            "with DPDP Act residency expectations."
        ),
    },
    "mumbai": {
        "city": "Mumbai",
        "state": "Maharashtra",
        "language": "Marathi and Hindi",
        "intro": (
            "Space is the constraint that shapes Mumbai hospitals. Bed turnover matters "
            "more here than almost anywhere, which makes discharge speed a genuine revenue "
            "lever — every hour a discharged patient waits at the billing desk is an hour "
            "the bed cannot be refilled."
        ),
        "local_proof": (
            "We run Mumbai implementations with on-site support during rollout and "
            "training, followed by remote support from our team."
        ),
        "residency": (
            "Patient data for Indian hospitals is hosted in Indian data centres, in line "
            "with DPDP Act residency expectations."
        ),
    },
}

COST_ANSWER_SCHEMA = (
    "ZenoHosp publishes its pricing, which most Indian HMS vendors do not. The Essential "
    "Pack covering HMS, Inventory, Asset, Finance and People starts at Rs 9,000 per month "
    "billed monthly, or Rs 8,000 per month billed annually, plus GST. Clinical add-ons are "
    "priced separately - OT Room from Rs 1,000, Pharmacy from Rs 2,000 and Lab from Rs "
    "2,500 per month. Rates scale by bed tier, and there is no per-user fee."
)


# JSON-LD is served as UTF-8, so the rupee glyph is safe in both the visible
# copy and the schema. Kept as one string so the two cannot drift apart.
COST_ANSWER = COST_ANSWER_SCHEMA.replace("Rs ", "\u20b9").replace("separately - OT", "separately \u2014 OT")


def faqs(c):
    return [
        (f"How much does hospital management software cost in {c['city']}?", COST_ANSWER),
        (f"Does ZenoHosp support {c['language']}?",
         f"Yes. Patient communication, appointment reminders and prescription receipts are "
         f"available in {c['language']} as standard - not as a paid add-on or plugin."),
        (f"Do you have a team in {c['city']}?", c["local_proof"]),
        ("How long does implementation take?",
         "A typical mid-size hospital goes live within 90 days, covering configuration, "
         "data migration from your existing system, staff training and a supported "
         "cutover. The variable that moves this most is the state of the data you are "
         "migrating, so we scope that first."),
        ("Where is our patient data stored?", c["residency"]),
        (f"Does it handle {c['state']} GST and ABDM compliance?",
         f"Yes. GST calculation with HSN/SAC categorisation for pharmacy items is built "
         f"into the billing engine, along with TPA and insurance reconciliation. ABHA ID "
         f"creation and health-record linking under ABDM are included rather than billed "
         f"as a separate integration."),
    ]


def build_section(c):
    cards = "\n".join(
        f"""          <div class="comp-item-card">
            <h3>{q}</h3>
            <p>{a}</p>
          </div>"""
        for q, a in faqs(c)
    )
    return f"""
  <!-- Local orientation + FAQ (added by scripts/expand_city_pages.py) -->
  <section class="city-detail-section">
    <div class="container">
      <div class="city-intro">
        <p>{c['intro']}</p>
        <p>If you are still shortlisting, our <a href="/resources/best-hospital-management-software-india-2026.html">2026 comparison of hospital management software in India</a> covers the main platforms side by side, and the <a href="/resources/hospital-management-software-cost-india.html">cost guide</a> breaks down what implementation, migration and AMC actually add to the subscription.</p>
      </div>

      <h2 class="city-faq-heading">{c['city']} hospital software questions</h2>
      <div class="city-faq-grid">
{cards}
      </div>
    </div>
  </section>

"""


CSS = """

/* City page detail + FAQ blocks (scripts/expand_city_pages.py) */

.city-detail-section {
  padding: 80px 0;
  background: #f5f5f2;
}

.city-intro {
  max-width: 820px;
  margin: 0 auto 56px;
  font-size: 1.125rem;
  line-height: 1.8;
  color: #4a4a45;
}

.city-intro p + p {
  margin-top: 1.25rem;
}

.city-faq-heading {
  text-align: center;
  font-size: clamp(1.75rem, 3vw, 2.25rem);
  font-weight: 700;
  color: #11110d;
  margin-bottom: 40px;
}

.city-faq-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
  max-width: 1000px;
  margin: 0 auto;
}

.city-faq-grid .comp-item-card {
  background: #fff;
  border: 1px solid #eaeae6;
  border-radius: 16px;
  padding: 28px;
}

.city-faq-grid .comp-item-card h3 {
  font-size: 1.05rem;
  font-weight: 600;
  color: #11110d;
  margin: 0 0 12px;
  line-height: 1.4;
}

.city-faq-grid .comp-item-card p {
  font-size: 0.95rem;
  color: #4a4a45;
  line-height: 1.7;
  margin: 0;
}
"""


def main():
    root = pathlib.Path(__file__).resolve().parent.parent

    css_path = root / "css" / "main.css"
    css = css_path.read_text(encoding="utf-8")
    if ".city-detail-section" not in css:
        css_path.write_text(css + CSS, encoding="utf-8")
        print("appended city page styles to css/main.css")

    for slug, c in CITIES.items():
        path = root / "hms-software" / slug / "index.html"
        if not path.exists():
            print(f"  missing: {slug}")
            continue
        html = path.read_text(encoding="utf-8")
        if "city-detail-section" in html:
            print(f"  already expanded: {slug}")
            continue

        # Sits above the closing call to action.
        marker = '<section class="cta-banner">'
        idx = html.index(marker)
        # Keep any indentation that precedes the CTA section.
        line_start = html.rfind("\n", 0, idx) + 1
        html = html[:line_start] + build_section(c) + html[line_start:]

        schema = json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in faqs(c)
            ],
        }, indent=2)
        html = html.replace(
            "</head>",
            f'  <script type="application/ld+json">\n{schema}\n</script>\n</head>',
            1,
        )

        path.write_text(html, encoding="utf-8")
        print(f"  expanded hms-software/{slug}/")

    print(f"\nexpanded {len(CITIES)} city pages")


if __name__ == "__main__":
    sys.exit(main())
