#!/usr/bin/env python3
"""
fill_pillar_comparison.py — replace the 64 [VERIFY: ...] placeholders that
shipped on the pillar page's competitor comparison with researched copy.

Sources (checked 2026-07-13): practo.com/providers/hospitals/insta (+features),
mocdoc.com + Techjockey/Capterra listings, attunelive.com, vanuston.com
(Medeil), NIC eHospital public materials. "Careview" could not be verified as a
real Indian HMS product, so that column/card is replaced with eHospital (NIC),
which the site already compares against (compare/zenohosp-vs-ehospital).

Competitor copy is deliberately neutral and based on each vendor's own public
positioning; limitations are framed as fit considerations, not defects.
A "compiled from public vendor materials" disclaimer is added under the table.
"""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(BASE, "resources", "best-hospital-management-software-india-2026.html")
h = open(F, encoding="utf-8").read()

# ---- rename the unverifiable competitor ----
h = h.replace("<h3>Careview</h3>", "<h3>eHospital (NIC)</h3>")
h = h.replace("<th>Careview</th>", "<th>eHospital (NIC)</th>")

# ---- replacements keyed on the [VERIFY: ...] text ----
R = {
    # --- Insta HMS card ---
    "Insta HMS target customer profile in Indian market":
        "Multi-department and multi-centre private hospitals — with a strong installed base in South India — that want enterprise-grade revenue cycle discipline.",
    "Insta HMS core strengths and key module advantages":
        "OPD/IPD, operation theatre, lab and radiology (with PACS integrations), pharmacy and inventory on one cloud platform; handles complex TPA, insurer and corporate rate structures; known for fast implementations.",
    "Insta HMS limitations regarding price model, setup duration, or user curve":
        "Quote-based pricing (not published); the platform's depth is best utilised by larger, process-mature facilities.",
    # --- MocDoc card ---
    "MocDoc hospital tier primary target profile":
        "Mid-size hospitals that want a broad cloud ERP covering clinical and back-office operations in one subscription.",
    "MocDoc hospital tier key capabilities, e.g. laboratory information system":
        "OPD/IPD workflows, GST-compliant billing, pharmacy with FIFO and expiry alerts, bi-directional lab analyser interfacing, HR, and doctor/patient mobile apps; reports 1,500+ institutions.",
    "MocDoc hospital tier constraints regarding pricing tiers or deep clinical modules":
        "Breadth-first suite — deeper clinical customisation typically needs vendor engagement; pricing on request.",
    # --- eHospital card (was Careview) ---
    "Careview hospital software primary target":
        "Government hospitals and public health facilities — eHospital is developed by the National Informatics Centre (NIC), Government of India.",
    "Careview primary strengths in regional Indian hospitals":
        "No licence cost for government facilities, national-scale deployments, ABDM-aligned patient registration, and OPD/IPD, billing, lab and pharmacy modules on NIC cloud infrastructure.",
    "Careview primary limitations or tech stack feedback":
        "Not offered as a commercial product for private hospitals; enhancements and support follow government processes rather than a commercial SLA.",
    # --- Attune card ---
    "Attune HIS best target segment in Indian healthcare":
        "Enterprise hospitals (roughly 50-500 beds) and diagnostics networks — especially lab-heavy, multi-location operations.",
    "Attune HIS major strengths in clinical workflows and diagnostics":
        "Strong LIS heritage with large-scale analyser and device integration, plus OPD/IPD, pharmacy, billing and TPA modules; proven multi-centre rollouts.",
    "Attune HIS limitations regarding deployment complexity or software costs":
        "Enterprise-grade scope: custom pricing and implementation cycles sized for larger organisations.",
    # --- Medeil card ---
    "Medeil best target profile, e.g. retail pharmacy chains vs full multi-specialty hospitals":
        "Standalone and chain pharmacies, and hospital pharmacy counters that need a dedicated dispensing and inventory system.",
    "Medeil key advantages, e.g. pharmacy inventory management":
        "Pharmacy-specialist POS with a ~1-lakh drug database, expiry and reorder management, and affordable entry pricing; used across retail, hospital and veterinary pharmacies.",
    "Medeil constraints when used as a full IPD/EMR hospital management suite":
        "Pharmacy-first product — it is not a full IPD/EMR hospital suite, so wards, OT and clinical workflows need separate systems.",

    # --- ZenoHosp cells ---
    "ZenoHosp OT scheduling module live release status":
        "Built. OT Room module: scheduling, pre-op checklists, utilisation analytics.",
    "ZenoHosp pharmacy integration contract finalized and API sync active":
        "Built. Prescriptions land in the dispensing queue; sales post to Finance.",
    "ZenoHosp multi-department billing pharmacy integration dependency":
        "Built. OPD, IPD, pharmacy and lab charges consolidate on one bill.",
    "ZenoHosp payroll module launch status":
        "Built. People module: rosters, attendance and payroll.",

    # --- table cells: IPD ---
    "Insta HMS IPD support": "Yes — IPD EMR with bed management.",
    "MocDoc IPD support": "Yes — independent OPD/IPD workflows.",
    "Careview IPD support": "Yes — in government deployments.",
    "Attune HIS IPD support": "Yes.",
    "Medeil IPD support": "No — pharmacy-first product.",
    # --- OT ---
    "Insta HMS OT support": "Yes — OT module.",
    "MocDoc OT support": "Varies by plan — confirm scope on demo.",
    "Careview OT support": "Varies by deployment.",
    "Attune HIS OT support": "Yes.",
    "Medeil OT support": "No.",
    # --- pharmacy ---
    "Insta HMS pharmacy integration": "Yes — prescription-linked dispensing.",
    "MocDoc pharmacy integration": "Yes — FIFO, expiry alerts, integrated billing.",
    "Careview pharmacy integration": "Yes.",
    "Attune HIS pharmacy integration": "Yes.",
    "Medeil pharmacy integration": "Yes — core specialisation.",
    # --- lab ---
    "Insta HMS lab integration": "Yes — lab & radiology with PACS.",
    "MocDoc lab integration": "Yes — bi-directional analyser interfacing.",
    "Careview lab integration": "Yes.",
    "Attune HIS lab integration": "Yes — flagship LIS strength.",
    "Medeil lab integration": "No.",
    # --- GST ---
    "Insta HMS GST support": "Yes.",
    "MocDoc GST support": "Yes — GST invoices and filing reports.",
    "Careview GST support": "Government billing formats.",
    "Attune HIS GST support": "Yes.",
    "Medeil GST support": "Yes — pharmacy billing.",
    # --- multi-dept billing ---
    "Insta HMS multi-dept billing": "Yes.",
    "MocDoc multi-dept billing": "Yes.",
    "Careview multi-dept billing": "Yes.",
    "Attune HIS multi-dept billing": "Yes.",
    "Medeil multi-dept billing": "No — pharmacy counter only.",
    # --- zip discharge ---
    "Insta HMS instant discharge support": "Standard discharge billing workflow.",
    "MocDoc instant discharge support": "Standard discharge billing workflow.",
    "Careview instant discharge support": "Standard discharge billing workflow.",
    "Attune HIS instant discharge support": "Standard discharge billing workflow.",
    "Medeil instant discharge support": "Not applicable.",
    # --- payroll ---
    "Insta HMS payroll support": "Resource management; payroll varies by plan.",
    "MocDoc payroll support": "Yes — HR module.",
    "Careview payroll support": "No — separate government systems.",
    "Attune HIS payroll support": "Varies by plan.",
    "Medeil payroll support": "No.",
    # --- deployment ---
    "Insta HMS deployment options": "Cloud.",
    "MocDoc deployment options": "Cloud.",
    "Careview deployment options": "NIC cloud (government).",
    "Attune HIS deployment options": "Cloud (enterprise).",
    "Medeil deployment options": "Cloud and on-premise POS.",
}

missing = []
for key, val in R.items():
    pat = '<span class="verify-text">[VERIFY: %s]</span>' % key
    if pat in h:
        h = h.replace(pat, val)
    else:
        missing.append(key)

# ---- disclaimer under the comparison table ----
DISC = ('\n            <p style="font-size:0.85rem;opacity:0.75;margin-top:12px;">'
        'Competitor information is compiled from each vendor\'s public website and '
        'marketplace listings as of July 2026 and may change; please verify specifics '
        'with the vendor before purchase.</p>')
if "compiled from each vendor" not in h:
    # after the close of the feature comparison table's wrapper
    i = h.find("Feature and Capability Comparison")
    j = h.find("</div>", h.find("</table>", i)) + len("</div>")
    h = h[:j] + DISC + h[j:]

open(F, "w", encoding="utf-8").write(h)
left = len(re.findall(r"\[VERIFY", h))
print(f"replaced {len(R) - len(missing)} placeholders; unmatched keys: {missing or 'none'}")
print(f"[VERIFY markers remaining in file: {left}")
