#!/usr/bin/env python3
"""Add FAQ content and FAQPage schema to the existing /compare/zenohosp-vs-*/ pages.

The five vs pages carried ~300 words each and no FAQ schema. That is too thin to
hold a position on a query where the competitor's own brand is in the phrase, and
it leaves the rich-result slot on the table.

Each page gains: five buyer-stage FAQs (cost, migration, switching time, and
crucially "when is the competitor the better choice"), FAQPage schema, and links
into the cost guide, the 2026 comparison and the alternatives pages.

The "when they are better" answer is deliberate. A comparison page that admits a
competitor wins some scenarios reads as credible rather than as sales copy, and
it is the part that tends to get quoted back by AI answers.

ACCURACY RULE: competitor claims reuse what ZenoHosp has already researched and
published (the 2026 comparison page). Where the product is not well characterised
on this site — Adrine — the copy stays on ZenoHosp and migration mechanics rather
than asserting things about them.
"""

import json
import pathlib
import sys

COST_LINE = (
    "ZenoHosp publishes its rates — ₹9,000 per month for the Essential Pack, ₹8,000 "
    "billed annually, plus GST, scaling by bed tier with no per-user fee."
)

PAGES = {
    "zenohosp-vs-instahms": {
        "name": "Insta HMS",
        "cost": (
            f"Insta quotes on request rather than publishing pricing, so a direct comparison "
            f"is not possible until you have their number. {COST_LINE} If you are budgeting "
            f"before shortlisting, that difference matters more than it sounds."
        ),
        "better": (
            "Insta is the stronger fit for large multi-centre private networks that need "
            "enterprise-grade revenue cycle discipline and have the process maturity to use "
            "it. If you run several hospitals with complex insurer and corporate rate "
            "structures and a dedicated IT function, it earns its scope. ZenoHosp is built "
            "for the 35–500 bed single or small multi-site band."
        ),
    },
    "zenohosp-vs-attune": {
        "name": "Attune HIS",
        "cost": (
            f"Attune prices per engagement, sized for enterprise and multi-location "
            f"diagnostics networks. {COST_LINE}"
        ),
        "better": (
            "Attune is the stronger fit if your operation is lab-led — a diagnostics network "
            "with heavy analyser and device integration across many locations. Its LIS "
            "heritage is genuine and deep. If the laboratory is the business rather than a "
            "department, weigh that seriously."
        ),
    },
    "zenohosp-vs-ehospital": {
        "name": "eHospital (NIC)",
        "cost": (
            f"eHospital is developed by the National Informatics Centre and carries no "
            f"licence cost for government facilities — nothing commercial competes with free. "
            f"It is not offered as a commercial product for private hospitals. {COST_LINE}"
        ),
        "better": (
            "If you are a government hospital or a public health facility, eHospital is "
            "almost certainly the right answer and we would not try to talk you out of it. "
            "The trade-off is that enhancements and support follow government process rather "
            "than a commercial SLA, which matters more to private hospitals than public ones."
        ),
    },
    "zenohosp-vs-nuvertos": {
        "name": "NuvertOS",
        "cost": (
            f"NuvertOS sells modules individually so hospitals can start small, and quotes "
            f"per rollout. {COST_LINE} Worth comparing the two-year total rather than the "
            f"entry price, since phased rollouts add modules over time."
        ),
        "better": (
            "NuvertOS suits a hospital that wants to digitise one department at a time on a "
            "tight initial budget. If you genuinely cannot take a whole-hospital rollout this "
            "year, a phased approach is sensible. The thing to check is what the modules cost "
            "once they are all in, and how well they talk to each other at that point."
        ),
    },
    "zenohosp-vs-adrine": {
        "name": "Adrine",
        "cost": (
            f"{COST_LINE} Ask any vendor for the year-two renewal rate in writing, not just "
            f"the first-year figure — that is where switching costs usually hide."
        ),
        "better": (
            "Any incumbent has one large advantage: your staff already know it and your data "
            "is already in it. If the current system is working and the gaps are minor, the "
            "disruption of switching may not be worth it. Switching earns its keep when "
            "departments are not talking to each other and the reconciliation is manual."
        ),
    },
}

SHARED = [
    (
        "Can we migrate our existing patient data?",
        "Yes. Migration scope is agreed before the project starts — how many years of "
        "history, which modules, and in what format. We put that in writing because "
        "migration is the single most common cause of a delayed go-live, and a vague "
        "scope is how switching projects overrun.",
    ),
    (
        "How long does switching take?",
        "A typical mid-size hospital goes live within 90 days, covering configuration, "
        "data migration, staff training and a supported cutover. The state of the data "
        "you are migrating moves this more than anything else, so we scope it first.",
    ),
    (
        "What should we test in the demo?",
        "Order an IPD drug and watch whether it deducts from pharmacy stock by FEFO and "
        "lands on the patient's bill without anyone re-keying it. That single workflow "
        "tells you more about whether a system is genuinely integrated than any feature "
        "list will.",
    ),
]


def faqs(slug, spec):
    return [
        (f"Is ZenoHosp cheaper than {spec['name']}?", spec["cost"]),
        *SHARED,
        (f"When is {spec['name']} the better choice?", spec["better"]),
    ]


def build_section(slug, spec):
    cards = "\n".join(
        f"""        <div class="short-card">
          <h3>{q}</h3>
          <p>{a}</p>
        </div>"""
        for q, a in faqs(slug, spec)
    )
    return f"""
  <!-- Buyer FAQ (added by scripts/expand_vs_pages.py) -->
  <section class="shortcomings">
    <div class="container">
      <div style="text-align: center; margin-bottom: 60px;">
        <h2 style="font-size: 2.5rem; font-weight: 800;">ZenoHosp vs {spec['name']}: common questions</h2>
      </div>
      <div class="short-grid">
{cards}
      </div>
      <p style="text-align: center; margin-top: 48px; font-size: 1.05rem; line-height: 1.8;">
        Still shortlisting? See the <a href="/resources/best-hospital-management-software-india-2026.html">2026 comparison of hospital management software in India</a>,
        or the <a href="/resources/hospital-management-software-cost-india.html">full cost breakdown</a> covering implementation, migration and AMC.
      </p>
    </div>
  </section>

"""


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    done = 0

    for slug, spec in PAGES.items():
        path = root / "compare" / slug / "index.html"
        if not path.exists():
            print(f"  missing: {slug}")
            continue
        html = path.read_text(encoding="utf-8")
        if "expand_vs_pages.py" in html:
            print(f"  already expanded: {slug}")
            continue

        marker = '<section class="cta-banner">'
        idx = html.index(marker)
        line_start = html.rfind("\n", 0, idx) + 1
        html = html[:line_start] + build_section(slug, spec) + html[line_start:]

        schema = json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in faqs(slug, spec)
            ],
        }, indent=2, ensure_ascii=False)
        html = html.replace(
            "</head>",
            f'  <script type="application/ld+json">\n{schema}\n</script>\n</head>',
            1,
        )

        path.write_text(html, encoding="utf-8")
        print(f"  expanded compare/{slug}/")
        done += 1

    print(f"\nexpanded {done} vs pages")


if __name__ == "__main__":
    sys.exit(main())
