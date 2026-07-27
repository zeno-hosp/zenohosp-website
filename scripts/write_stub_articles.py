#!/usr/bin/env python3
"""Fill the two placeholder blog posts with real articles.

Both pages shipped with "[PASTE YOUR ARTICLE CONTENT HERE]" in the body and were
noindexed in an earlier pass so they could not drag site quality. The originals
live on LinkedIn but the text was not available, so these are newly written on
the same topics.

Two consequences worth being explicit about:

1. The "originally published on LinkedIn" line is REMOVED from both. The LinkedIn
   articles exist, but this is not their text — leaving the attribution would
   assert something false.
2. The noindex is lifted and the pages go back into the sitemap, since they now
   have content.

Written in the voice of the existing posts (see blog/inventory-money-missing.html):
first-person plural, mechanism-first, Indian hospital specifics, no invented
statistics or customer claims.
"""

import pathlib
import re
import sys

ARTICLES = {
    "blog/patient-wait-times-discharge.html": {
        "lede": "Why patients wait hours after doctor says you can go home",
        "read": "5 min read",
        "body": """
      <p>A consultant finishes the morning round at 10am and tells the family the patient can go
        home. The family starts packing. At 3pm they are still sitting on the bed, waiting for
        a piece of paper.</p>

      <p>Everyone in the hospital knows this happens. What is less obvious is that it is almost
        never a staffing problem. Adding another person to the billing counter rarely fixes it,
        because the queue at the billing counter is a symptom. The real delay is that
        <strong>clinical discharge and financial discharge are two different events</strong>, and
        the second one cannot start until every department has finished reporting.</p>

      <h3>The bill cannot close until the last department reports</h3>

      <p>A discharge bill is an assembly job. It needs the ward charges, the pharmacy
        consumption, the lab and radiology, any OT consumables, the room rent calculated to the
        right hour, and the TPA or insurance position. If any one of those arrives late, the
        whole bill waits.</p>

      <p>In most hospitals at least one of them always arrives late, because the charge is
        recorded on paper at the point of care and keyed into the billing system afterwards. The
        gap between those two moments is the discharge delay. It is not one big delay; it is
        five small ones stacked end to end.</p>

      <h3>Three things that reliably hold up the bill</h3>

      <p><strong>1. Ward returns.</strong> Medicines are indented to the ward in advance. Some
        get used, some do not. Before the bill can be finalised, the unused strips have to
        physically come back to the pharmacy and be credited. If that return is processed at the
        pharmacy counter rather than at the ward, it queues behind whatever else the pharmacy is
        doing — and the patient waits for it.</p>

      <p><strong>2. Charges that post after the fact.</strong> OT consumables are the classic
        case. Items opened in theatre get noted on a sheet, and that sheet reaches billing when
        someone carries it there. A last-minute investigation ordered on the morning of discharge
        is the same problem in miniature. The bill has to be reopened, recalculated, and
        re-approved.</p>

      <p><strong>3. TPA approval started too late.</strong> If the final approval request goes to
        the insurer on the day of discharge, the patient is now waiting on a third party the
        hospital does not control. Hospitals that start the pre-authorisation trail at admission
        and keep it current through the stay do not have this problem on the last day.</p>

      <h3>What the wait actually costs</h3>

      <p>The obvious cost is the patient experience, and it is a real one — discharge is the last
        thing a family remembers about the hospital, and a four-hour wait undoes a good clinical
        outcome in their retelling of it.</p>

      <p>The less obvious cost is the bed. A bed occupied by a patient who was cleared at 10am
        and left at 3pm is a bed that could not be allocated for five hours. In a hospital
        running near capacity, that is not a comfort issue, it is a throughput issue: elective
        admissions get pushed, and the emergency department holds patients waiting for a ward
        bed. Multiply five hours across the discharges in a month and the number gets
        uncomfortable quickly.</p>

      <h3>What actually fixes it</h3>

      <p>The fix is not a faster billing counter. It is removing the reconciliation step
        entirely, by making sure there was never a second copy of the charge to reconcile.</p>

      <ul>
        <li><strong>Charges post when the event happens, not when the paper arrives.</strong> If
          the nurse records administration in the system and that record <em>is</em> the billing
          entry, there is nothing to key in later. The bill is current at every moment of the
          stay, which means at discharge it is already finished.</li>
        <li><strong>Returns are processed where they physically happen.</strong> Ward-level
          dispensing and ward-level return means the credit hits the bill at the ward, not after
          a walk to the pharmacy.</li>
        <li><strong>The insurance trail runs from admission.</strong> Pre-authorisation,
          interim approvals and the final claim tracked as one continuous thread rather than a
          scramble on the last morning.</li>
      </ul>

      <p>The test worth running on your own hospital is simple: pick a patient mid-stay and ask
        for their current bill. If the finance team can produce an accurate one in under a
        minute, discharge will be fast. If producing it requires ringing three departments, that
        is exactly what is happening at every discharge, every day.</p>
"""
    },
    "blog/revenue-left-on-table.html": {
        "lede": "Three places hospitals leave revenue on the table without realizing",
        "read": "5 min read",
        "body": """
      <p>When we talk to hospital owners about revenue leakage, the first assumption is usually
        theft. It almost never is. In our experience building hospital systems, the money leaves
        through gaps in how things get recorded — and the people involved have no idea it is
        happening, because from where they stand nothing looks wrong.</p>

      <p>Here are three places it goes, all of which are invisible in a monthly P&amp;L.</p>

      <h3>1. Consumables opened in theatre</h3>

      <p>A surgery runs long. The team opens an extra set of sutures, a second mesh, another
        pack. In theatre, that is a clinical decision made in seconds and correctly nobody stops
        to think about billing.</p>

      <p>What happens next decides whether the hospital gets paid for it. If the consumption is
        written on a sheet and that sheet travels to billing later, some of it will not make it —
        not through dishonesty, but because the sheet is incomplete, or illegible, or arrives
        after the bill is closed. The item is gone from stock either way. Only the revenue is
        missing.</p>

      <p>This is the cleanest example of the pattern: the hospital has already paid for the item
        and already delivered the value. Everything needed to bill it existed at the moment it
        was used. It was lost purely in transit between two records.</p>

      <h3>2. Stock that expires in the right order</h3>

      <p>Most pharmacies say they run FIFO — first in, first out. For medicine that is the wrong
        rule. The correct rule is FEFO: <strong>first expiry, first out</strong>. A batch
        received later can easily expire sooner, and if you dispense strictly by receipt date you
        will hold the short-dated batch until it is worthless.</p>

      <p>The difference sounds academic until you look at a write-off register. Expiry losses are
        usually treated as a cost of doing business, which is why they rarely get investigated.
        But a large share of them are not inevitable — they are the arithmetic result of picking
        stock in the wrong order, month after month.</p>

      <p>This one compounds quietly. Nobody notices a single expired box. The register only shows
        the total, and the total gets accepted as normal.</p>

      <h3>3. Insurance deductions nobody argues with</h3>

      <p>A TPA settles a claim for less than it was raised for. The remittance arrives with a
        deduction and a reason code. Somebody records the receipt and moves on to the next
        claim.</p>

      <p>Some of those deductions are legitimate. Some are not — a document that was actually
        submitted, a tariff applied at the wrong rate, a package rule misread. The only way to
        know which is which is to reconcile line by line against what was raised, and that takes
        time the billing team does not have while new claims are stacking up.</p>

      <p>So the deduction gets accepted by default. Not because anyone decided to accept it, but
        because nobody had the hours to challenge it inside the appeal window. Multiply a small
        average shortfall across a year of claims and this is frequently the largest of the
        three.</p>

      <h3>The pattern underneath all three</h3>

      <p>None of these is a people problem, and none of them is fixed by asking staff to be more
        careful. In every case the information needed to get paid existed at the moment the event
        happened. It was lost because the system required someone to move it from one place to
        another, and that transfer is where things fall through.</p>

      <p>Which is why the fix is structural rather than procedural:</p>

      <ul>
        <li><strong>Record consumption at the point of use</strong>, so the clinical record and
          the billing record are the same record and there is no transfer to lose.</li>
        <li><strong>Enforce FEFO in the picking logic</strong> rather than in the training
          manual, so the short-dated batch is the one the system hands over.</li>
        <li><strong>Reconcile remittances against raised claims automatically</strong>, so a
          shortfall surfaces as an exception to review rather than a line nobody reads.</li>
      </ul>

      <p>Better reporting does not solve any of this. A dashboard showing you last month's
        leakage is still a dashboard about money you have already lost. The goal is a system
        where the leak structurally cannot happen — where there is no second copy of the record
        to go missing in the first place.</p>
"""
    },
}


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    for rel, art in ARTICLES.items():
        path = root / rel
        html = path.read_text(encoding="utf-8")
        if "PASTE YOUR ARTICLE CONTENT HERE" not in html:
            print(f"  already written: {rel}")
            continue

        start = html.index('<section class="blog-content">')
        end = html.index("</section>", start) + len("</section>")
        html = html[:start] + f'<section class="blog-content">{art["body"]}    </section>' + html[end:]

        # Written here, not republished — the LinkedIn attribution would be false.
        html = re.sub(
            r'\s*<p style="font-style: italic[^>]*>.*?originally published.*?</p>',
            "", html, flags=re.S)

        # It has content now, so it can be indexed.
        html = re.sub(
            r'\s*<!--\s*Placeholder: body is still.*?-->\s*\n?', "\n", html, flags=re.S)
        html = re.sub(r'\s*<meta name="robots" content="noindex, follow">\s*\n?', "\n", html)

        html = html.replace("3 min read", art["read"]).replace("2 min read", art["read"])
        path.write_text(html, encoding="utf-8")
        print(f"  wrote {rel}")

    # Back into the sitemap now that they are real pages.
    sm = root / "sitemap.xml"
    x = sm.read_text(encoding="utf-8")
    for rel in ARTICLES:
        url = f"https://www.zenohosp.com/{rel[:-len('.html')]}/"
        if url in x:
            continue
        x = x.replace("</urlset>",
                      f"  <url>\n    <loc>{url}</loc>\n    <lastmod>2026-07-27</lastmod>\n"
                      f"    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n</urlset>")
    sm.write_text(x, encoding="utf-8")
    print(f"\nsitemap now {x.count('<url>')} urls")


if __name__ == "__main__":
    sys.exit(main())
