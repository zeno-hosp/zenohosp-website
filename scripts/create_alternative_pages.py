#!/usr/bin/env python3
"""Build "<competitor> alternatives" pages under /compare/.

Why this page type: someone searching "MocDoc alternative" is already in-market
and already unhappy. That is the highest-converting query class in B2B SaaS, and
the SERP for it is far weaker than for "best hospital software india" — the
incumbent's own site cannot rank for its own alternatives query, and the
listicle publishers cover it thinly.

ZenoHosp had five "vs" pages (Adrine, Attune, eHospital, Insta, NuvertOS), all
around 300 words, and none for MocDoc, Practo or Caresoft — the three names a
mid-size Indian hospital is most likely to be leaving.

ACCURACY RULE: every claim about a competitor here is either (a) already
researched and published on ZenoHosp's own comparison page, or (b) a positioning
statement the vendor makes publicly about itself. No pricing is asserted for any
competitor, because none of them publish it. Verify before publishing.

Reuses the layout of the cost guide so pages inherit the design system.
"""

import json
import pathlib
import re
import sys

TEMPLATE = "resources/hospital-management-software-cost-india.html"

COMPETITORS = [
    {
        "slug": "mocdoc-alternatives",
        "name": "MocDoc",
        "title": "MocDoc Alternatives for Indian Hospitals (2026)",
        "hero_sub": "If MocDoc is not the right fit for your hospital, here is an honest look at what to compare it against — and where each option actually differs.",
        "description": (
            "Comparing MocDoc alternatives for Indian hospitals in 2026 — where MocDoc "
            "fits, when hospitals outgrow it, and how ZenoHosp, Insta and Attune differ "
            "on pricing transparency, module depth and deployment."
        ),
        "fair": (
            "MocDoc is a genuinely broad cloud suite. It covers OPD and IPD workflows, "
            "GST-compliant billing, pharmacy with FIFO and expiry handling, bi-directional "
            "lab analyser interfacing, HR, and doctor and patient mobile apps. Its "
            "laboratory heritage shows — the LIS integration is one of the stronger parts "
            "of the product, which is why it is a common choice for hospitals that grew "
            "out of a diagnostics business."
        ),
        "reasons": [
            ("You cannot get a price without a sales cycle",
             "MocDoc quotes on request, as most Indian HMS vendors do. If you are trying to "
             "build a budget before you shortlist, that is a real obstacle — and it means two "
             "hospitals of similar size can end up paying quite different amounts."),
            ("Breadth-first, and you need depth in one place",
             "A suite that covers everything covers some things at surface level. Hospitals "
             "with an unusual OT workflow, a complex TPA mix, or heavy ward-level dispensing "
             "sometimes find the specific module they care most about needs vendor "
             "engagement to go deeper."),
            ("You want the pharmacy and finance ledger genuinely welded together",
             "The test worth running on any HMS: order an IPD drug and watch whether it "
             "deducts from pharmacy stock by FEFO and lands on the patient's bill without "
             "anyone re-keying it. Ask for that demo specifically."),
        ],
        "zeno_angle": (
            "ZenoHosp publishes its rates rather than quoting on request, with add-on modules "
            "itemised and no per-user fee, so you can budget before you talk to anyone — "
            "current figures are on the <a href=\"/pricing/index.html\">pricing page</a>. "
            "It is built specifically for the 35–500 bed range, "
            "which means less breadth than a suite aiming at clinics and chains "
            "simultaneously, and more depth in ward, OT and IPD billing workflows."
        ),
        "not_for": (
            "If you run a single clinic or a diagnostics centre without inpatient beds, "
            "ZenoHosp is more system than you need — MocDoc or a practice management tool "
            "will serve you better and cost less."
        ),
    },
    {
        "slug": "practo-ray-alternatives",
        "name": "Practo Ray",
        "title": "Practo Ray Alternatives for Growing Hospitals (2026)",
        "hero_sub": "Practo Ray is a good practice management tool. It is not a hospital system — here is what to move to when you add beds.",
        "description": (
            "Practo Ray alternatives for hospitals that have outgrown clinic software — "
            "what changes when you add inpatient beds, wards, OT scheduling and "
            "multi-department billing, and which Indian HMS platforms cover it."
        ),
        "fair": (
            "Practo Ray is genuinely good at the job it is built for: appointment "
            "scheduling, digital prescriptions, and patient records for individual "
            "practitioners and small multi-doctor clinics. It is fast, clean, and it comes "
            "attached to the Practo patient network, which is a real acquisition channel "
            "for a consultant building a practice."
        ),
        "reasons": [
            ("You have added inpatient beds",
             "This is the fault line. Practice management software manages an appointment "
             "and a prescription. The moment a patient is admitted, you need bed allocation, "
             "ward nursing workflows, IPD drug dispensing, daily charge accrual and a "
             "discharge summary — a different category of system entirely."),
            ("Billing has become multi-department",
             "Once a single patient journey touches OPD, lab, pharmacy, OT and a ward, every "
             "one of those has to post charges to one ledger automatically. If your staff "
             "are reconciling departments by hand at discharge, you have outgrown the tool."),
            ("You need NABH and ABDM documentation",
             "Audit trails, role-based access, automated discharge summaries and ABHA "
             "linking are hospital-grade requirements. They are not what a clinic scheduler "
             "is designed to produce."),
        ],
        "zeno_angle": (
            "ZenoHosp starts where clinic software stops: wards, OT scheduling, IPD billing "
            "and pharmacy on one ledger, with ABDM built in rather than bolted on. Pricing "
            "is published rather than quoted on request, and charged per hospital location "
            "rather than per user — so hiring more front-desk staff does not raise the bill. "
            "Current figures are on the <a href=\"/pricing/index.html\">pricing page</a>."
        ),
        "not_for": (
            "If you are a solo practitioner or a two-doctor clinic with no beds, stay on "
            "Practo Ray. ZenoHosp would be overhead you do not need, and we will tell you "
            "that on the call."
        ),
    },
    {
        "slug": "healthray-alternatives",
        "name": "Healthray",
        "title": "Healthray Alternatives for Indian Hospitals (2026)",
        "hero_sub": "Two full-suite HMS platforms aimed at similar hospitals. Here is where they actually differ.",
        "description": (
            "Healthray alternatives for Indian hospitals in 2026 — how full-suite HMS platforms "
            "compare on pricing transparency, deployment and module depth for 35-500 bed facilities."
        ),
        "fair": (
            "Healthray is a full hospital management suite covering OPD, IPD, billing, pharmacy "
            "and laboratory, positioned at medium and large hospitals. That is broadly the same "
            "ground ZenoHosp occupies, which makes this a genuine like-for-like comparison rather "
            "than a category mismatch."
        ),
        "reasons": [
            ("You cannot compare cost without a sales cycle",
             "Like most Indian HMS vendors, pricing is not published. When two suites look "
             "similar on a feature grid, cost becomes the deciding factor - and you cannot weigh "
             "it until you have sat through demos with both."),
            ("Feature lists look identical, so test the seams instead",
             "Every full-suite vendor lists OPD, IPD, pharmacy and lab. What separates them is "
             "whether those modules genuinely share one ledger. Order an IPD drug in each demo "
             "and watch whether it deducts stock and hits the bill without anyone re-keying."),
            ("Fit is about your size band, not the feature count",
             "A suite built for large hospitals carries configuration overhead a 60-bed facility "
             "will pay for and never use. A suite built for clinics runs out of room at 200 beds. "
             "Ask specifically what size hospital the product is designed around."),
        ],
        "zeno_angle": (
            "ZenoHosp publishes its rates rather than quoting on request, and is built "
            "specifically for the 35-500 bed band - which means less breadth than a platform "
            "aiming at everything from clinics to chains, and more depth in ward, OT and IPD "
            "billing workflows."
        ),
        "not_for": (
            "If you are running a large multi-state tertiary network needing heavily customised "
            "local database architecture, you want an enterprise platform sized for that, not us."
        ),
    },
    {
        "slug": "healthplix-alternatives",
        "name": "HealthPlix",
        "title": "HealthPlix Alternatives: From EMR to Full Hospital System (2026)",
        "hero_sub": "HealthPlix is built for the consulting room. Here is what to move to when you need the whole hospital.",
        "description": (
            "HealthPlix alternatives for hospitals that need more than an EMR — what changes when "
            "you add inpatient beds, wards, pharmacy and multi-department billing."
        ),
        "fair": (
            "HealthPlix is an EMR built around a specific and real problem: helping a consultant "
            "get through a high-volume OPD without drowning in prescription writing. For a doctor "
            "seeing 60 patients a day, that focus is genuinely valuable, and a broader hospital "
            "suite will not match it at that one job."
        ),
        "reasons": [
            ("An EMR is not a hospital system",
             "EMR records the clinical encounter. A hospital system also has to allocate beds, "
             "run ward nursing workflows, dispense from pharmacy stock, schedule theatre, accrue "
             "charges daily and produce a discharge summary. Those are different problems."),
            ("Billing has become multi-department",
             "Once one patient journey touches OPD, lab, pharmacy, OT and a ward, every one of "
             "those has to post to a single ledger automatically. If staff reconcile departments "
             "by hand at discharge, the tool has been outgrown."),
            ("You need institutional compliance, not individual records",
             "NABH audit trails, role-based access across departments, and ABDM health-record "
             "linking at the front desk are hospital-level requirements that a consultant-focused "
             "EMR is not designed to produce."),
        ],
        "zeno_angle": (
            "ZenoHosp starts where EMR stops: wards, OT scheduling, IPD billing and pharmacy on "
            "one ledger, with ABDM built in. Pricing is published and charged per location rather "
            "than per user, so adding consultants does not raise the bill."
        ),
        "not_for": (
            "If you are a solo consultant or a small clinic without beds, a focused EMR will "
            "serve you better and cost less. We would say so on the call."
        ),
    },
    {
        "slug": "smarthms-alternatives",
        "name": "SMARTHMS",
        "title": "SMARTHMS Alternatives for Indian Hospitals (2026)",
        "hero_sub": "If stock control is why you chose SMARTHMS, here is what to weigh when the rest of the hospital needs the same rigour.",
        "description": (
            "SMARTHMS alternatives for Indian hospitals — comparing inventory-led hospital "
            "software against full-suite platforms on clinical depth, billing integration and pricing."
        ),
        "fair": (
            "SMARTHMS positions around operational efficiency and materials management, and "
            "hospitals that pick it usually do so for a good reason: consumables and pharmacy "
            "stock were the biggest leak, and it addressed that."
        ),
        "reasons": [
            ("Stock control solved, revenue leakage not",
             "Tight inventory stops items disappearing from the store. It does not stop an item "
             "being used on a patient and never reaching the bill. That second leak lives in the "
             "gap between consumption and billing, and only closes when the two are one record."),
            ("The clinical side has to keep up",
             "Once inventory is under control, the constraint moves - usually to IPD billing, ward "
             "workflows or discharge speed. A platform led by materials management may be "
             "shallower exactly where you now need depth."),
            ("Pricing is quote-based",
             "As with most vendors in this market, you cannot compare cost without going through "
             "a sales cycle first."),
        ],
        "zeno_angle": (
            "ZenoHosp treats inventory as one module on a shared ledger rather than the centre of "
            "the product - stock deducts by FEFO at the point of use and the charge posts to the "
            "patient bill in the same action. Rates are published rather than quoted."
        ),
        "not_for": (
            "If inventory genuinely is your only problem and the rest of your stack works, "
            "replacing everything to fix one thing is rarely worth the disruption."
        ),
    },
    {
        "slug": "caresoft-alternatives",
        "name": "Caresoft",
        "title": "Caresoft HMS Alternatives: Moving Off On-Premise (2026)",
        "hero_sub": "Most hospitals looking past Caresoft are really asking a different question — whether to stay on a local server at all.",
        "description": (
            "Caresoft HMS alternatives for Indian hospitals in 2026 — what actually changes "
            "when you move from an on-premise server to cloud HMS, what it costs, and how "
            "to migrate without losing patient history."
        ),
        "fair": (
            "Caresoft is one of the longer-established Indian HMS vendors, and there is a "
            "reason hospitals stay: a locally deployed system you already know, with your "
            "data on your own server, is a known quantity. If you have the IT staff and the "
            "infrastructure, that familiarity has real value and is not worth discarding "
            "casually."
        ),
        "reasons": [
            ("The server is becoming the cost",
             "A perpetual licence looks cheaper than a subscription until you add the box, "
             "its replacement cycle, the UPS, backups, and the person who maintains all of "
             "it. Run that total across five years before you compare licence figures."),
            ("You have more than one location",
             "On-premise gets structurally harder with each branch. Consolidated reporting "
             "across sites, shared patient records and central inventory are the things that "
             "start costing you real money in workarounds."),
            ("Updates arrive on someone else's schedule",
             "ABDM requirements and GST rules keep moving. On a locally installed system, "
             "every regulatory change is a deployment project rather than something that is "
             "simply already there on Monday."),
        ],
        "zeno_angle": (
            "ZenoHosp is cloud-native, with published pricing and no server to own. If data "
            "residency policy or genuinely unreliable connectivity means you must stay "
            "local, we also offer on-premise as a one-time perpetual licence with an AMC — "
            "so the deployment model is a choice rather than a reason to rule us out."
        ),
        "not_for": (
            "If your connectivity is genuinely unreliable and your policy requires data on "
            "your own premises, do not let anyone talk you onto cloud for its own sake. Ask "
            "for the on-premise option instead."
        ),
    },
]


def build_body(c):
    reasons = "\n".join(
        f"""                <div class="comp-item-card">
                    <h3>{title}</h3>
                    <p>{text}</p>
                </div>"""
        for title, text in c["reasons"]
    )
    return f"""
    <!-- Hero Section -->
    <header class="seo-hero">
        <div class="seo-bg-glow"></div>
        <div class="container">
            <h1>{c['name']} Alternatives</h1>
            <p>{c['hero_sub']}</p>
        </div>
    </header>

    <!-- Fair summary of the incumbent -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="explainer-box">
                <p><strong>First, credit where it is due.</strong> {c['fair']}</p>
                <p>We build a competing product, so read this with that in mind. What follows
                    is where hospitals tell us the fit breaks down — not a claim that
                    {c['name']} is a bad product.</p>
            </div>
        </div>
    </section>

    <hr style="border: 0; border-top: 1px solid var(--zd-cream-dark); margin: 0;">

    <!-- Why hospitals look elsewhere -->
    <section class="section-padding bg-cream">
        <div class="container">
            <div class="section-header">
                <h2>Why hospitals look for a {c['name']} alternative</h2>
                <p>Three patterns that come up repeatedly.</p>
            </div>
            <div class="comp-list-grid">
{reasons}
            </div>
        </div>
    </section>

    <hr style="border: 0; border-top: 1px solid var(--zd-cream-dark); margin: 0;">

    <!-- Where ZenoHosp fits -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="section-header">
                <h2>Where ZenoHosp fits</h2>
            </div>
            <div class="explainer-box">
                <p>{c['zeno_angle']}</p>
                <p><strong>Where it does not fit.</strong> {c['not_for']}</p>
                <p>The full cost breakdown — including implementation, migration and AMC —
                    is on our <a href="/resources/hospital-management-software-cost-india.html">hospital
                    software cost guide</a>, and the wider market view is in our
                    <a href="/resources/best-hospital-management-software-india-2026.html">2026 HMS
                    comparison</a>.</p>
            </div>
        </div>
    </section>

    <hr style="border: 0; border-top: 1px solid var(--zd-cream-dark); margin: 0;">

    <!-- How to run the evaluation -->
    <section class="section-padding bg-cream">
        <div class="container">
            <div class="section-header">
                <h2>How to test any replacement</h2>
                <p>Four things worth insisting on before you switch anything.</p>
            </div>
            <div class="explainer-box">
                <p><strong>1. Demand the cross-module demo.</strong> Order an IPD drug in the
                    demo and watch it deduct from pharmacy stock and appear on the patient's
                    bill without anyone re-keying it. If that needs a workaround, everything
                    else is decoration.</p>
                <p><strong>2. Get the migration scope in writing.</strong> How many years of
                    patient history, in what format, who cleans it, and what it costs. This is
                    where switching projects overrun.</p>
                <p><strong>3. Ask for the year-two price.</strong> Not just the first-year
                    figure. Renewal rates that appear only after you have migrated are the
                    oldest move in enterprise software.</p>
                <p><strong>4. Ask how you would leave.</strong> What the export format is and
                    how long it takes. A vendor confident in its product answers immediately.</p>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="section-header">
                <h2>Want a straight answer on fit?</h2>
                <p>Tell us your bed count, your modules and what is breaking today. If ZenoHosp
                    is the wrong size for you, we will say so on the first call.</p>
            </div>
            <div style="text-align: center;">
                <a href="/contact-us/index.html" class="btn btn-primary btn-lg">Book a Demo</a>
                <a href="/pricing/index.html" class="btn btn-outline btn-lg">See Pricing</a>
            </div>
        </div>
    </section>
"""


def build_schema(c, url):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"What are the best {c['name']} alternatives in India?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": (
                        f"Indian hospitals evaluating alternatives to {c['name']} most often "
                        "compare ZenoHosp, Insta HMS, Attune HIS and MocDoc. The right choice "
                        "depends on bed count, whether you need inpatient and OT workflows, and "
                        "whether you require cloud or on-premise deployment. ZenoHosp publishes "
                        "its pricing rather than quoting on request, which most Indian HMS vendors do not."
                    ),
                },
            },
            {
                "@type": "Question",
                "name": f"Why do hospitals switch away from {c['name']}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": " ".join(f"{t}: {d}" for t, d in c["reasons"]),
                },
            },
            {
                "@type": "Question",
                "name": "What should I check before switching hospital software?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": (
                        "Insist on a cross-module demo where an IPD drug order deducts from "
                        "pharmacy stock and posts to the patient bill without re-keying. Get the "
                        "data migration scope in writing, including how many years of history and "
                        "who cleans the data. Ask for the year-two renewal price, not just the "
                        "first-year figure. And ask what the data export format is, so you know "
                        "how you would leave."
                    ),
                },
            },
        ],
    }, indent=2)


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    template = (root / TEMPLATE).read_text(encoding="utf-8")

    head = template[: template.index("<body>")]
    nav = template[template.index("<body>"): template.index("<!-- Hero Section -->")]
    footer = template[template.index("    <zeno-footer>"):]

    for c in COMPETITORS:
        url = f"https://www.zenohosp.com/compare/{c['slug']}/"
        h = re.sub(r"<title>.*?</title>", f"<title>{c['title']}</title>", head, flags=re.S)
        h = re.sub(r'(<meta\s+name="description"\s*\n?\s*content=")[^"]*(")',
                   lambda m: m.group(1) + c["description"] + m.group(2), h, flags=re.I)
        h = re.sub(r'(<link rel="canonical" href=")[^"]*(")',
                   lambda m: m.group(1) + url + m.group(2), h)
        for prop, val in (("og:title", c["title"]), ("og:description", c["description"]), ("og:url", url)):
            h = re.sub(rf'(property="{prop}" content=")[^"]*(")',
                       lambda m, v=val: m.group(1) + v + m.group(2), h)
        h = re.sub(r'(<meta\s+name="keywords"\s+content=")[^"]*(")',
                   lambda m: m.group(1) + f"{c['name']} alternatives, {c['name']} vs ZenoHosp, "
                   "hospital management software India, HMS comparison" + m.group(2), h, flags=re.I)

        def drop_page_specific(match):
            try:
                parsed = json.loads(match.group(1))
            except json.JSONDecodeError:
                return match.group(0)
            return "" if parsed.get("@type") in {"Article", "FAQPage", "WebPage", "ItemList", "BreadcrumbList"} else match.group(0)

        h = re.sub(r'\s*<script type="application/ld\+json">(.*?)</script>',
                   drop_page_specific, h, flags=re.S)
        h = h.replace("</head>", "").rstrip()
        h += '\n\n  <script type="application/ld+json">\n' + build_schema(c, url) + "\n</script>\n</head>\n"

        out_dir = root / "compare" / c["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(h + nav + build_body(c) + "\n" + footer, encoding="utf-8")
        print(f"  compare/{c['slug']}/  —  {c['title']}")

    print(f"\nbuilt {len(COMPETITORS)} alternative pages")


if __name__ == "__main__":
    sys.exit(main())
