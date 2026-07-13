#!/usr/bin/env python3
"""
create_abdm_checklist.py — build the linkable asset page
resources/abdm-compliance-checklist-2026.html

Reuses the chrome (head boilerplate, nav, static footer, scripts) of the
"Best HMS in India 2026" pillar so the page matches the site exactly, then
swaps in checklist content + fresh metadata and JSON-LD (Article, Breadcrumb,
FAQPage; the sitewide Organization block is kept verbatim).

Facts verified 2026-07-13 against abdm.gov.in / dhis.abdm.gov.in coverage:
M1 = ABHA creation & verification; M2 = HIP record linking (FHIR R4, consent);
M3 = HIU consent-based exchange; DHIS = Rs.20/eligible transaction above a
100/month baseline, capped at Rs.4 crore, most recently extended to March 2026.

Idempotent: overwrites the output file wholesale.
"""
import re, os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "resources", "best-hospital-management-software-india-2026.html")
OUT = os.path.join(BASE, "resources", "abdm-compliance-checklist-2026.html")

URL = "https://www.zenohosp.com/resources/abdm-compliance-checklist-2026/"
TITLE = "ABDM Compliance Checklist for Indian Hospitals (2026) | ZenoHosp"
DESC = 'Step-by-step ABDM checklist for Indian hospitals: HFR & HPR registration, Milestones M1-M2-M3, ABHA at the front desk, FHIR records, DHIS incentives.'
H1 = "ABDM Compliance Checklist for Indian Hospitals (2026)"
HERO_P = ("Every registration, milestone, and incentive in one actionable checklist - for hospital "
          "founders and administrators taking their facility onto the Ayushman Bharat Digital Mission.")

pillar = open(SRC, encoding="utf-8").read()

# ---------- chrome extraction ----------
i = pillar.find("</header>")                     # close of the seo-hero header
chrome_top = pillar[: i + len("</header>")]
j = pillar.rfind("    <!-- Footer -->")
chrome_bottom = pillar[j:]

# ---------- head surgery on chrome_top ----------
chrome_top = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", chrome_top, 1, re.S)
chrome_top = re.sub(r'(<meta name="description" content=")[^"]*(")',
                    lambda m: m.group(1) + DESC + m.group(2), chrome_top, 1)
chrome_top = re.sub(r'(<link rel="canonical" href=")[^"]*(")',
                    lambda m: m.group(1) + URL + m.group(2), chrome_top, 1)
for prop, val in (("og:url", URL), ("og:title", TITLE), ("og:description", DESC)):
    chrome_top = re.sub(r'(<meta property="%s" content=")[^"]*(")' % re.escape(prop),
                        lambda m: m.group(1) + val + m.group(2), chrome_top)

# keep only the Organization JSON-LD; replace the rest with page-specific schema
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', chrome_top, re.S)
keep = [b for b in blocks if '"Organization"' in b and '"WebPage"' not in b][:1]
chrome_top = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", chrome_top, flags=re.S)

FAQS = [
    ("Is ABDM registration mandatory for private hospitals in India?",
     "ABDM adoption is voluntary for most private facilities, but it is becoming mandatory for "
     "AB-PMJAY empanelled hospitals in 2026, and several states are linking digital health readiness "
     "to empanelment and renewals. With DHIS incentives on the table, early adopters are effectively "
     "being paid to comply while laggards face empanelment risk."),
    ("What are ABDM Milestones M1, M2 and M3?",
     "M1 is creating and verifying ABHA numbers at patient registration. M2 makes your hospital a "
     "Health Information Provider (HIP): every visit, lab report and prescription becomes a care "
     "context linked to the patient's ABHA, shareable with consent in FHIR R4 format. M3 makes you a "
     "Health Information User (HIU), able to fetch a patient's records from other facilities with "
     "their consent."),
    ("How long does full ABDM compliance take?",
     "With software that is already ABDM-certified, hospitals typically go live in weeks - the work "
     "reduces to HFR/HPR registration and front-desk training. Building certification yourself "
     "through the NHA sandbox typically takes 3-6 months with existing digital infrastructure, and "
     "6-12 months from scratch."),
    ("How much can a hospital earn under the Digital Health Incentive Scheme (DHIS)?",
     "DHIS pays Rs.20 per eligible ABHA-linked digital health record above a baseline of 100 "
     "transactions per month, up to Rs.4 crore per facility. Caps apply per patient (1/day, 5/month "
     "per ABHA). The scheme has been extended multiple times, most recently to March 2026 - confirm "
     "the live window at dhis.abdm.gov.in before budgeting."),
    ("What is Scan & Share and why does it matter?",
     "Scan & Share lets patients scan a QR code at your registration desk and share their ABHA "
     "profile instantly - cutting OPD registration from minutes to seconds. It is the fastest, most "
     "visible ABDM win for patients and generates eligible DHIS transactions from day one."),
    ("Do we need to replace our existing hospital software to comply?",
     "Not necessarily. If your HMS vendor is ABDM-certified (M1/M2/M3), you inherit compliance - "
     "ZenoHosp customers, for example, get ABHA creation, care-context linking and Scan & Share "
     "built in. If your current vendor has no ABDM roadmap, factor the 3-6 month sandbox timeline "
     "into your decision."),
]

faq_schema = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
article_schema = {
    "@context": "https://schema.org", "@type": "Article",
    "headline": H1, "description": DESC,
    "datePublished": "2026-07-13", "dateModified": "2026-07-13",
    "author": {"@type": "Organization", "name": "ZenoHosp"},
    "publisher": {"@type": "Organization", "name": "ZenoHosp",
                  "logo": {"@type": "ImageObject", "url": "https://www.zenohosp.com/images/zenohosp.svg"}},
    "mainEntityOfPage": URL,
}
breadcrumb_schema = {
    "@context": "https://schema.org", "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.zenohosp.com/"},
        {"@type": "ListItem", "position": 2, "name": "Resources", "item": "https://www.zenohosp.com/resources/"},
        {"@type": "ListItem", "position": 3, "name": "ABDM Compliance Checklist 2026", "item": URL},
    ],
}
ld = "\n".join(
    '  <script type="application/ld+json">%s</script>' % s
    for s in ([keep[0].strip()] if keep else [])
    + [json.dumps(x, ensure_ascii=False) for x in (article_schema, breadcrumb_schema, faq_schema)]
)
chrome_top = chrome_top.replace("</head>", ld + "\n</head>", 1)

# ---------- hero ----------
chrome_top = re.sub(r"<h1>.*?</h1>", f"<h1>{H1}</h1>", chrome_top, 1, re.S)
chrome_top = re.sub(r"(<h1>.*?</h1>\s*<p>).*?(</p>)", lambda m: m.group(1) + HERO_P + m.group(2),
                    chrome_top, 1, re.S)

# ---------- checklist item helper ----------
def items(*texts):
    return "\n".join(
        f'                    <li style="padding:6px 0 6px 34px;position:relative;">'
        f'<span style="position:absolute;left:0;">✅</span> {t}</li>' for t in texts)

faq_html = "\n".join(
    f"""                <div style="margin-bottom:28px;">
                    <h3>{q}</h3>
                    <p>{a}</p>
                </div>""" for q, a in FAQS)

CONTENT = f"""

    <!-- At-a-glance -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="explainer-box">
                <p>The Ayushman Bharat Digital Mission (ABDM) is India's national digital health backbone: every patient gets an ABHA health account, every facility joins the Health Facility Registry, and health records move between hospitals with patient consent. In 2026 the stakes changed - ABDM compliance is becoming mandatory for AB-PMJAY empanelled hospitals, and the Digital Health Incentive Scheme (DHIS) pays facilities for every eligible digital record. This checklist covers every registration, milestone and incentive, in the order you should tackle them.</p>
            </div>
        </div>
    </section>

    <!-- Phase 0-1 -->
    <section class="section-padding bg-cream">
        <div class="container">
            <h2>Phase 1 - Registrations (Week 1-2)</h2>
            <p>Everything starts with two registries run by the National Health Authority. Both are free.</p>
            <ul style="list-style:none;padding:0;margin-top:16px;">
{items(
    "<strong>Register your facility in the HFR</strong> (Health Facility Registry) at facility.abdm.gov.in - you will need facility ownership documents and the in-charge's details.",
    "<strong>Register your doctors in the HPR</strong> (Healthcare Professionals Registry) - each clinician gets a Healthcare Professional ID linked to their council registration.",
    "<strong>Appoint an ABDM owner</strong> - one administrator accountable for milestones, front-desk training and incentive claims.",
    "<strong>Audit your software</strong> - ask your HMS vendor for their ABDM certification status (M1/M2/M3). If they are certified, Phases 2-4 shrink from months to weeks.")}
            </ul>
        </div>
    </section>

    <!-- Milestones table -->
    <section class="section-padding bg-white">
        <div class="container">
            <h2>Phase 2-4 - The Three ABDM Milestones</h2>
            <p>NHA certifies software against three milestones. If your vendor is pre-certified you inherit them; if not, this is the sandbox-to-production path.</p>
            <div class="table-responsive">
                <table class="comp-table">
                    <thead>
                        <tr><th>Milestone</th><th>What it means for your hospital</th><th>Typical effort</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>M1 - ABHA</strong></td><td>Create and verify a patient's ABHA number at registration; support Scan &amp; Share QR check-in at the front desk.</td><td>2-4 weeks</td></tr>
                        <tr><td><strong>M2 - HIP</strong></td><td>Become a Health Information Provider: every OPD visit, IPD admission, lab report and prescription is linked to the patient's ABHA as a care context and shared - with consent - in FHIR R4 format.</td><td>4-12 weeks (the demanding one)</td></tr>
                        <tr><td><strong>M3 - HIU</strong></td><td>Become a Health Information User: fetch a patient's history from other ABDM facilities with their consent - complete records at admission, fewer repeat tests.</td><td>2-4 weeks on top of M2</td></tr>
                    </tbody>
                </table>
            </div>
            <ul style="list-style:none;padding:0;margin-top:24px;">
{items(
    "<strong>M1 live:</strong> front desk creates/verifies ABHA on every new registration; Scan &amp; Share QR displayed at reception.",
    "<strong>M2 live:</strong> discharge summaries, lab reports and prescriptions auto-link to ABHA as care contexts; consent requests handled in-app.",
    "<strong>M3 live:</strong> treating doctors can request outside records with patient consent from day one of admission.",
    "<strong>Staff trained:</strong> registration desk can complete an ABHA flow in under a minute and explain consent to patients in the local language.")}
            </ul>
        </div>
    </section>

    <!-- DHIS -->
    <section class="section-padding bg-cream">
        <div class="container">
            <h2>Phase 5 - Claim Your DHIS Incentives</h2>
            <p>The Digital Health Incentive Scheme pays you to digitise. Facilities earn <strong>Rs.20 per eligible ABHA-linked record</strong> above a baseline of 100 transactions a month - up to <strong>Rs.4 crore per facility</strong>. Caps: 1 transaction/day and 5/month per patient ABHA. The scheme has been extended several times, most recently to March 2026 - <a href="https://dhis.abdm.gov.in/" target="_blank" rel="noopener">confirm the current window at dhis.abdm.gov.in</a> before you budget around it.</p>
            <ul style="list-style:none;padding:0;margin-top:16px;">
{items(
    "<strong>Register for DHIS</strong> through the ABDM portal once M1 is live.",
    "<strong>Link every eligible record</strong> - prescriptions, lab reports, consultation notes, discharge summaries - to the patient's verified ABHA.",
    "<strong>Track your monthly count</strong> against the 100-transaction baseline; a 100-bed hospital typically clears it within days.",
    "<strong>Reconcile payouts monthly</strong> - the old Rs.2,500 minimum-disbursal threshold no longer applies.")}
            </ul>
        </div>
    </section>

    <!-- How ZenoHosp helps -->
    <section class="section-padding bg-white">
        <div class="container">
            <h2>The Shortcut: ABDM-Ready Software</h2>
            <p>Hospitals running <a href="/apps/hms/index.html">ZenoHosp HMS</a> skip the sandbox entirely: ABHA creation and verification at registration, Scan &amp; Share check-in, care-context linking from <a href="/apps/lab/index.html">Lab</a> and <a href="/apps/pharmacy/index.html">Pharmacy</a>, and consent-managed record exchange are built in. Your team's checklist reduces to HFR/HPR registration and a morning of front-desk training. See <a href="/solutions/abdm-compliance/index.html">how ZenoHosp integrates with ABDM</a>, or <a href="/contact-us/index.html">book a 20-minute compliance walkthrough</a>.</p>
        </div>
    </section>

    <!-- FAQ -->
    <section class="section-padding bg-cream">
        <div class="container">
            <h2>Frequently Asked Questions</h2>
{faq_html}
        </div>
    </section>

    <!-- Related -->
    <section class="section-padding bg-white">
        <div class="container">
            <h2>Keep Reading</h2>
            <ul style="list-style:none;padding:0;line-height:2;">
                <li><a href="/blog/abdm-compliance-2026.html">ABDM in 2026: What Every Hospital Administrator Needs to Know</a></li>
                <li><a href="/solutions/abdm-compliance/index.html">ZenoHosp's ABDM &amp; ABHA Integration</a></li>
                <li><a href="/resources/best-hospital-management-software-india-2026.html">Best Hospital Management Software in India 2026</a></li>
                <li><a href="/blog/gst-compliance-hospitals.html">GST Compliance for Indian Hospitals</a></li>
            </ul>
        </div>
    </section>

"""

open(OUT, "w", encoding="utf-8").write(chrome_top + CONTENT + chrome_bottom)
print("wrote", os.path.relpath(OUT, BASE))
words = len(re.sub(r"<[^>]+>", " ", CONTENT).split())
print("content words:", words)
