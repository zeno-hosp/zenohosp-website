#!/usr/bin/env python3
"""Build resources/hospital-management-software-cost-india.html.

Strategic rationale, so the next person understands why this page exists:

Every serious HMS vendor in India quotes on request. ZenoHosp's own comparison
page records this — Insta is "quote-based pricing (not published)", MocDoc is
"pricing on request", Attune is "custom pricing". That leaves the highest-intent
question a hospital owner asks — "what will this actually cost me?" — with no
good answer anywhere on the Indian web.

ZenoHosp publishes real numbers. That is a genuine, defensible content
advantage, and it is the one query where being the vendor is an asset rather
than a bias problem. Concrete figures are also what AI assistants cite, because
they are the only thing in the corpus that answers the question.

Deliberately does NOT invent competitor prices. Everything stated about other
vendors is that they quote privately, which is verifiable. Cost components and
worked examples use ZenoHosp's published rates from /pricing/.

Reuses the layout of resources/best-hospital-management-software-india-2026.html
so the page inherits the existing design system, nav and footer.
"""

import json
import pathlib
import re
import sys

TEMPLATE = "resources/best-hospital-management-software-india-2026.html"
OUTPUT = "resources/hospital-management-software-cost-india.html"

URL = "https://www.zenohosp.com/resources/hospital-management-software-cost-india/"
TITLE = "Hospital Management Software Cost in India (2026 Price Guide)"
DESCRIPTION = (
    "What hospital management software actually costs in India in 2026 — real "
    "subscription figures, the implementation and AMC costs vendors leave out of "
    "quotes, and worked totals for 50, 100 and 200-bed hospitals."
)

SCHEMA = """
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hospital Management Software Cost in India (2026 Price Guide)",
  "description": "%s",
  "inLanguage": "en-IN",
  "author": {"@type": "Organization", "name": "ZenoHosp", "url": "https://www.zenohosp.com/"},
  "publisher": {
    "@type": "Organization",
    "name": "ZenoHosp",
    "logo": {"@type": "ImageObject", "url": "https://www.zenohosp.com/images/zenohosp-b.svg"}
  },
  "mainEntityOfPage": {"@type": "WebPage", "@id": "%s"}
}
</script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does hospital management software cost in India?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a mid-size Indian hospital, hospital management software typically runs as a monthly subscription per location rather than a per-user licence. ZenoHosp publishes its rates: the Essential Pack covering HMS, Inventory, Asset, Finance and People starts at Rs 9,000 per month billed monthly, or Rs 8,000 per month billed annually (Rs 96,000 per year), plus GST. Clinical add-ons are priced separately - OT Room from Rs 1,000 per month, Pharmacy from Rs 2,000 per month and Lab from Rs 2,500 per month. Pricing scales with bed capacity across 35-80, 81-150, 151-250 and 251+ bed tiers. Most other Indian HMS vendors do not publish pricing and quote on request."
      }
    },
    {
      "@type": "Question",
      "name": "Why do most hospital software vendors in India not publish pricing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Quote-on-request pricing lets a vendor set the figure after learning your bed count, budget and how urgently you need to switch. It is not necessarily predatory, but it does mean two hospitals of the same size can pay very different amounts for the same system, and it makes shortlisting slow because you cannot compare until you have sat through several sales calls."
      }
    },
    {
      "@type": "Question",
      "name": "What costs are missing from a typical HMS quote?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The subscription is usually the smaller number. Ask specifically about one-time implementation and configuration, data migration from your existing system, staff training and retraining, on-premise server hardware if applicable, annual maintenance contract for on-premise deployments, charges for custom reports or modifications, integration fees for lab analysers and PACS, and what support costs beyond the included tier."
      }
    },
    {
      "@type": "Question",
      "name": "Is cloud or on-premise hospital software cheaper?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cloud is cheaper to start and usually cheaper over three to five years once server hardware, replacement cycles, power, backup and IT staff time are counted. On-premise can make sense where data residency policy requires it or where internet connectivity is genuinely unreliable. ZenoHosp offers on-premise as a one-time perpetual licence with an annual maintenance contract."
      }
    },
    {
      "@type": "Question",
      "name": "Should hospital software be priced per user or per bed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Per-user pricing punishes you for adding staff and encourages password sharing, which is a genuine patient-data risk. Per-location pricing that scales with bed capacity is more predictable, because your bed count changes rarely and your headcount changes constantly. ZenoHosp prices per hospital location by bed tier with no per-user fee."
      }
    }
  ]
}
</script>
""" % (DESCRIPTION, URL)


BODY = """
    <!-- Hero Section -->
    <header class="seo-hero">
        <div class="seo-bg-glow"></div>
        <div class="container">
            <h1>Hospital Management Software Cost in India</h1>
            <p>Real numbers for 2026 — what the subscription costs, what the quote leaves out, and what a 50, 100 or 200-bed hospital actually ends up paying.</p>
        </div>
    </header>

    <!-- Direct answer up front -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="explainer-box">
                <p><strong>The short answer:</strong> for a mid-size Indian hospital, expect a monthly subscription per location rather than a per-user licence. ZenoHosp's Essential Pack — HMS, Inventory, Asset, Finance and People — starts at <strong>₹9,000 per month</strong> billed monthly, or <strong>₹8,000 per month billed annually</strong> (₹96,000 a year), plus GST. Clinical add-ons are priced separately: OT Room from ₹1,000, Pharmacy from ₹2,000 and Lab from ₹2,500 per month. Pricing scales with bed capacity.</p>
                <p>We publish those figures because almost nobody else in this market does. Insta quotes on request. MocDoc quotes on request. Attune prices per engagement. That is normal for Indian HMS vendors, and it is why this page exists — you cannot budget for a system nobody will price until you are three sales calls deep.</p>
            </div>
        </div>
    </section>

    <hr style="border: 0; border-top: 1px solid var(--zd-cream-dark); margin: 0;">

    <!-- ZenoHosp published pricing -->
    <section class="section-padding bg-cream">
        <div class="container">
            <div class="section-header">
                <h2>What ZenoHosp costs</h2>
                <p>Published rates, per hospital location, exclusive of GST.</p>
            </div>
            <div class="table-responsive">
                <table class="comp-table">
                    <thead>
                        <tr>
                            <th>What you get</th>
                            <th>Billed monthly</th>
                            <th>Billed annually</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Essential Pack</strong><br>HMS + Inventory + Asset + Finance + People</td>
                            <td>₹9,000 / month</td>
                            <td>₹8,000 / month<br>(₹96,000 / year)</td>
                        </tr>
                        <tr>
                            <td>OT Room add-on<br>Surgical scheduling and live boards</td>
                            <td>+₹1,000 / month</td>
                            <td>+₹900 / month</td>
                        </tr>
                        <tr>
                            <td>Pharmacy add-on<br>Dispensing and stock management</td>
                            <td>+₹2,000 / month</td>
                            <td>+₹1,800 / month</td>
                        </tr>
                        <tr>
                            <td>Lab add-on<br>Diagnostics and reporting</td>
                            <td>+₹2,500 / month</td>
                            <td>+₹2,250 / month</td>
                        </tr>
                        <tr>
                            <td>On-premise deployment</td>
                            <td colspan="2">One-time perpetual licence plus annual maintenance contract — quoted per hospital</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="explainer-box" style="margin-top: 32px;">
                <p>Rates scale across four bed tiers — 35–80, 81–150, 151–250 and 251+ beds. There is no per-user fee, so adding front-desk staff, nurses or consultants does not change the bill. <a href="/pricing/index.html">See the full pricing page and module calculator →</a></p>
            </div>
        </div>
    </section>

    <hr style="border: 0; border-top: 1px solid var(--zd-cream-dark); margin: 0;">

    <!-- Hidden costs -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="section-header">
                <h2>The costs that are not in the quote</h2>
                <p>The subscription is usually the smaller number. These are the line items to ask about before you sign.</p>
            </div>
            <div class="comp-list-grid">
                <div class="comp-item-card">
                    <h3>Implementation and configuration</h3>
                    <ul class="comp-details-list">
                        <li><strong>Ask:</strong> is this one-time fee fixed, or billed by the day?</li>
                        <li><strong>Why it matters:</strong> configuring departments, tariffs, TPA rate cards and user roles for a 100-bed hospital is real work. A vendor who says it is free has usually priced it into the subscription or is planning to rush it.</li>
                    </ul>
                </div>
                <div class="comp-item-card">
                    <h3>Data migration</h3>
                    <ul class="comp-details-list">
                        <li><strong>Ask:</strong> how many years of patient history, and in what format?</li>
                        <li><strong>Why it matters:</strong> this is the single most common source of a budget overrun and a delayed go-live. Get the scope in writing — how many records, which modules, and who cleans the data.</li>
                    </ul>
                </div>
                <div class="comp-item-card">
                    <h3>Training — and retraining</h3>
                    <ul class="comp-details-list">
                        <li><strong>Ask:</strong> how many sessions, on-site or remote, and what happens when staff turn over?</li>
                        <li><strong>Why it matters:</strong> hospital front-desk and nursing attrition is high. Training priced as a one-off event ages badly.</li>
                    </ul>
                </div>
                <div class="comp-item-card">
                    <h3>Server hardware and AMC</h3>
                    <ul class="comp-details-list">
                        <li><strong>Ask:</strong> only relevant for on-premise — what server spec, whose UPS, whose backup, and what the annual maintenance contract covers.</li>
                        <li><strong>Why it matters:</strong> a perpetual licence looks cheaper until you add the box, the replacement cycle, power and the IT person who babysits it.</li>
                    </ul>
                </div>
                <div class="comp-item-card">
                    <h3>Integrations</h3>
                    <ul class="comp-details-list">
                        <li><strong>Ask:</strong> what does it cost to connect our lab analysers, PACS, or payment terminal?</li>
                        <li><strong>Why it matters:</strong> bi-directional analyser interfacing is frequently a separate line item, and it is the difference between a lab module that saves time and one that adds typing.</li>
                    </ul>
                </div>
                <div class="comp-item-card">
                    <h3>Customisation and reports</h3>
                    <ul class="comp-details-list">
                        <li><strong>Ask:</strong> is a custom MIS or NABH report billable, and at what rate?</li>
                        <li><strong>Why it matters:</strong> every hospital needs a report the product does not ship with. Find out the rate before you need it, not after.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <hr style="border: 0; border-top: 1px solid var(--zd-cream-dark); margin: 0;">

    <!-- Worked examples -->
    <section class="section-padding bg-cream">
        <div class="container">
            <div class="section-header">
                <h2>What it works out to</h2>
                <p>Three worked examples using ZenoHosp's published annual rates, excluding GST and one-time implementation.</p>
            </div>
            <div class="table-responsive">
                <table class="comp-table">
                    <thead>
                        <tr>
                            <th>Hospital</th>
                            <th>Typical module mix</th>
                            <th>Indicative monthly</th>
                            <th>Per bed, per month</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>50-bed</strong><br>Single-location multispeciality</td>
                            <td>Essential Pack + Pharmacy</td>
                            <td>from ₹9,800</td>
                            <td>roughly ₹196</td>
                        </tr>
                        <tr>
                            <td><strong>100-bed</strong><br>With in-house lab and OT</td>
                            <td>Essential Pack + Pharmacy + Lab + OT Room</td>
                            <td>from ₹12,950</td>
                            <td>roughly ₹130</td>
                        </tr>
                        <tr>
                            <td><strong>200-bed</strong><br>Multi-department, higher tier</td>
                            <td>Full suite, 151–250 bed tier</td>
                            <td>quoted on bed tier</td>
                            <td>falls further with scale</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="explainer-box" style="margin-top: 32px;">
                <p>The per-bed figure is the number worth holding on to. Software that costs a couple of hundred rupees per bed per month sits against a single unbilled procedure or one expired drug batch — which is usually where the money actually goes. If you want that comparison for your own numbers, the <a href="/resources/roi-calculator/index.html">ROI calculator</a> runs it.</p>
            </div>
        </div>
    </section>

    <hr style="border: 0; border-top: 1px solid var(--zd-cream-dark); margin: 0;">

    <!-- Evaluating a quote -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="section-header">
                <h2>Reading an HMS quote</h2>
                <p>Five things worth checking before the number at the bottom.</p>
            </div>
            <div class="explainer-box">
                <p><strong>1. Per-user or per-location?</strong> Per-user pricing punishes you for hiring and quietly encourages password sharing, which is a real patient-data risk in a ward. Per-location pricing tied to bed capacity is more predictable, because bed count changes rarely and headcount changes constantly.</p>
                <p><strong>2. What happens in year two?</strong> Ask for the renewal rate in writing. A low first-year figure with an unstated renewal is the oldest move in enterprise software.</p>
                <p><strong>3. Is support included, or a tier?</strong> Establish response times for a billing outage at 9pm, not just business-hours email.</p>
                <p><strong>4. Who owns the data, and how do you get it out?</strong> Ask for the export format before you sign. A vendor confident in the product will answer this immediately.</p>
                <p><strong>5. Does the price change when you add a department?</strong> If you open a dialysis unit or a second OT next year, find out now what that does to the bill.</p>
            </div>
        </div>
    </section>

    <hr style="border: 0; border-top: 1px solid var(--zd-cream-dark); margin: 0;">

    <!-- FAQ -->
    <section class="section-padding bg-cream">
        <div class="container">
            <div class="section-header">
                <h2>Frequently asked questions</h2>
            </div>
            <div class="comp-list-grid">
                <div class="comp-item-card">
                    <h3>Why do most Indian HMS vendors hide pricing?</h3>
                    <p>Quote-on-request lets a vendor set the number after learning your bed count, your budget and how urgently you need to switch. It is not necessarily predatory — enterprise deals genuinely vary — but it does mean two similar hospitals can pay very different amounts for the same system, and it makes shortlisting slow.</p>
                </div>
                <div class="comp-item-card">
                    <h3>Is cloud or on-premise cheaper?</h3>
                    <p>Cloud is cheaper to start and usually cheaper across three to five years once you count server hardware, the replacement cycle, power, backup and IT staff time. On-premise earns its keep where data residency policy demands it or connectivity is genuinely unreliable. ZenoHosp offers on-premise as a perpetual licence plus AMC.</p>
                </div>
                <div class="comp-item-card">
                    <h3>Does ABDM compliance cost extra?</h3>
                    <p>It should not be a separate SKU. ABHA creation and health-record linking are part of operating a hospital in India now, not a premium feature. Ask whether ABDM support is included or billed as an integration.</p>
                </div>
                <div class="comp-item-card">
                    <h3>How long until it pays for itself?</h3>
                    <p>The honest answer depends on where your leakage is. Hospitals that recover unbilled IPD procedures and pharmacy expiry typically see the subscription covered well inside a year — but ask any vendor promising a specific payback to show you the arithmetic on your own numbers.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="section-header">
                <h2>Want the number for your hospital?</h2>
                <p>Share your bed count, OT rooms and the modules you need. We will send a final quote within one business day — and if ZenoHosp is the wrong fit for your size, we will say so.</p>
            </div>
            <div style="text-align: center;">
                <a href="/contact-us/index.html" class="btn btn-primary btn-lg">Get a Quote</a>
                <a href="/pricing/index.html" class="btn btn-outline btn-lg">See Full Pricing</a>
            </div>
        </div>
    </section>
"""


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    template = (root / TEMPLATE).read_text(encoding="utf-8")

    head_end = template.index("<body>")
    head = template[:head_end]

    # Nav markup runs from <body> to the hero comment; footer from <zeno-footer>.
    nav_start = template.index("<body>")
    hero_start = template.index("<!-- Hero Section -->")
    nav = template[nav_start:hero_start]
    footer = template[template.index("    <zeno-footer>"):]

    head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head, flags=re.S)
    head = re.sub(
        r'(<meta\s+name="description"\s*\n?\s*content=")[^"]*(")',
        lambda m: m.group(1) + DESCRIPTION + m.group(2), head, flags=re.I)
    head = re.sub(
        r'(<link rel="canonical" href=")[^"]*(")',
        lambda m: m.group(1) + URL + m.group(2), head)
    for prop, val in (("og:title", TITLE), ("og:description", DESCRIPTION), ("og:url", URL)):
        head = re.sub(rf'(property="{prop}" content=")[^"]*(")',
                      lambda m, v=val: m.group(1) + v + m.group(2), head)
    head = re.sub(
        r'(<meta\s+name="keywords"\s+content=")[^"]*(")',
        lambda m: m.group(1) + "hospital management software cost india, HMS price, "
                  "hospital software pricing, HMS cost per bed, ZenoHosp pricing" + m.group(2),
        head, flags=re.I)

    # Drop the template's page-specific structured data but keep the shared brand
    # blocks. Each script element is matched on its own — a single regex spanning
    # blocks silently swallows the Organization schema sitting between them.
    def drop_page_specific(match):
        try:
            parsed = json.loads(match.group(1))
        except json.JSONDecodeError:
            return match.group(0)
        if parsed.get("@type") in {"WebPage", "ItemList", "FAQPage", "Article"}:
            return ""
        return match.group(0)

    head = re.sub(
        r'\s*<script type="application/ld\+json">(.*?)</script>',
        drop_page_specific,
        head,
        flags=re.S,
    )

    head = head.replace("</head>", "")
    head = head.rstrip() + "\n" + SCHEMA + "</head>\n"

    out = head + nav + BODY + "\n" + footer
    (root / OUTPUT).write_text(out, encoding="utf-8")
    print(f"wrote {OUTPUT} ({len(out.split())} tokens of markup)")


if __name__ == "__main__":
    sys.exit(main())
