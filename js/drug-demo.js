(function () {
  'use strict';

  var DRUGS = [
    { id: 1, brand: 'Dolo-650', generic: 'Paracetamol 650mg', mfg: 'Micro Labs', price: 30, unit: 'strip/15', schedule: 'OTC', category: 'analgesic', stock: 842, batch: 'ML-24A-7821', expiry: 'Mar 2027' },
    { id: 2, brand: 'Crocin Advance', generic: 'Paracetamol 500mg', mfg: 'GSK', price: 25, unit: 'strip/15', schedule: 'OTC', category: 'analgesic', stock: 534, batch: 'GS-24B-0093', expiry: 'Jul 2027' },
    { id: 3, brand: 'Combiflam', generic: 'Ibuprofen 400mg + Paracetamol 325mg', mfg: 'Sanofi', price: 42, unit: 'strip/20', schedule: 'OTC', category: 'analgesic', stock: 315, batch: 'SN-24C-4510', expiry: 'Nov 2026' },
    { id: 4, brand: 'Augmentin 625 Duo', generic: 'Amoxicillin 500mg + Clavulanate 125mg', mfg: 'GSK', price: 185, unit: 'strip/10', schedule: 'H', category: 'antibiotic', stock: 128, batch: 'GS-24A-1187', expiry: 'Feb 2027' },
    { id: 5, brand: 'Azithral 500', generic: 'Azithromycin 500mg', mfg: 'Alembic', price: 95, unit: 'strip/5', schedule: 'H', category: 'antibiotic', stock: 210, batch: 'AL-24B-6633', expiry: 'Sep 2027' },
    { id: 6, brand: 'Ciplox 500', generic: 'Ciprofloxacin 500mg', mfg: 'Cipla', price: 68, unit: 'strip/10', schedule: 'H', category: 'antibiotic', stock: 185, batch: 'CP-24A-9021', expiry: 'Dec 2026' },
    { id: 7, brand: 'Pan-D', generic: 'Pantoprazole 40mg + Domperidone 30mg', mfg: 'Alkem', price: 120, unit: 'strip/15', schedule: 'H', category: 'gastro', stock: 423, batch: 'AK-24C-2245', expiry: 'Jun 2027' },
    { id: 8, brand: 'Pantocid 40', generic: 'Pantoprazole 40mg', mfg: 'Sun Pharma', price: 95, unit: 'strip/15', schedule: 'H', category: 'gastro', stock: 367, batch: 'SP-24B-8814', expiry: 'May 2027' },
    { id: 9, brand: 'Razo 20', generic: 'Rabeprazole 20mg', mfg: "Dr. Reddy's", price: 85, unit: 'strip/15', schedule: 'H', category: 'gastro', stock: 290, batch: 'DR-24A-3307', expiry: 'Apr 2027' },
    { id: 10, brand: 'Glycomet 500', generic: 'Metformin 500mg', mfg: 'USV', price: 28, unit: 'strip/20', schedule: 'H', category: 'diabetes', stock: 670, batch: 'UV-24C-5512', expiry: 'Aug 2027' },
    { id: 11, brand: 'Glycomet GP 2', generic: 'Metformin 500mg + Glimepiride 2mg', mfg: 'USV', price: 115, unit: 'strip/15', schedule: 'H', category: 'diabetes', stock: 198, batch: 'UV-24A-6678', expiry: 'Jan 2027' },
    { id: 12, brand: 'Amlopress 5', generic: 'Amlodipine 5mg', mfg: 'Cipla', price: 35, unit: 'strip/15', schedule: 'H', category: 'cardiac', stock: 445, batch: 'CP-24B-1190', expiry: 'Oct 2027' },
    { id: 13, brand: 'Atorva 10', generic: 'Atorvastatin 10mg', mfg: 'Zydus', price: 82, unit: 'strip/15', schedule: 'H', category: 'cardiac', stock: 310, batch: 'ZY-24A-4432', expiry: 'Mar 2027' },
    { id: 14, brand: 'Betaloc 50', generic: 'Metoprolol 50mg', mfg: 'AstraZeneca', price: 45, unit: 'strip/14', schedule: 'H', category: 'cardiac', stock: 178, batch: 'AZ-24C-7790', expiry: 'Jul 2027' },
    { id: 15, brand: 'Losacar 50', generic: 'Losartan 50mg', mfg: 'Cadila', price: 55, unit: 'strip/15', schedule: 'H', category: 'cardiac', stock: 225, batch: 'CD-24B-3301', expiry: 'Nov 2027' },
    { id: 16, brand: 'Olmy 20', generic: 'Olmesartan 20mg', mfg: 'Micro Labs', price: 110, unit: 'strip/15', schedule: 'H', category: 'cardiac', stock: 142, batch: 'ML-24A-9945', expiry: 'May 2027' },
    { id: 17, brand: 'Cetzine', generic: 'Cetirizine 10mg', mfg: 'Alkem', price: 35, unit: 'strip/10', schedule: 'OTC', category: 'allergy', stock: 560, batch: 'AK-24C-1123', expiry: 'Feb 2028' },
    { id: 18, brand: 'Montair 10', generic: 'Montelukast 10mg', mfg: 'Cipla', price: 155, unit: 'strip/15', schedule: 'H', category: 'respiratory', stock: 87, batch: 'CP-24A-5567', expiry: 'Sep 2027' },
    { id: 19, brand: 'Shelcal 500', generic: 'Calcium 500mg + Vitamin D3', mfg: 'Torrent', price: 145, unit: 'bottle/30', schedule: 'OTC', category: 'supplement', stock: 390, batch: 'TR-24B-2234', expiry: 'Dec 2027' },
    { id: 20, brand: 'Zincovit', generic: 'Multivitamin + Multimineral', mfg: 'Apex', price: 110, unit: 'bottle/15', schedule: 'OTC', category: 'supplement', stock: 445, batch: 'AX-24C-8890', expiry: 'Jan 2028' },
    { id: 21, brand: 'Monocef 500', generic: 'Ceftriaxone 500mg', mfg: 'Aristo', price: 68, unit: 'vial', schedule: 'H1', category: 'antibiotic', stock: 45, batch: 'AR-24A-0012', expiry: 'Aug 2026' },
    { id: 22, brand: 'Insulin Actrapid', generic: 'Soluble Insulin 40IU/ml', mfg: 'Novo Nordisk', price: 189, unit: 'vial/10ml', schedule: 'H', category: 'diabetes', stock: 32, batch: 'NN-24B-5501', expiry: 'Jun 2026' },
    { id: 23, brand: 'Calpol 500', generic: 'Paracetamol 500mg', mfg: 'GSK', price: 22, unit: 'strip/15', schedule: 'OTC', category: 'analgesic', stock: 480, batch: 'GS-24C-0187', expiry: 'Aug 2027' },
    { id: 24, brand: 'Moxikind-CV 625', generic: 'Amoxicillin 500mg + Clavulanate 125mg', mfg: 'Mankind', price: 145, unit: 'strip/10', schedule: 'H', category: 'antibiotic', stock: 156, batch: 'MK-24A-7744', expiry: 'Apr 2027' },
    { id: 25, brand: 'Ecosprin 75', generic: 'Aspirin 75mg', mfg: 'USV', price: 18, unit: 'strip/14', schedule: 'OTC', category: 'cardiac', stock: 720, batch: 'UV-24B-1100', expiry: 'Nov 2027' },
    { id: 26, brand: 'Telma 40', generic: 'Telmisartan 40mg', mfg: 'Glenmark', price: 95, unit: 'strip/15', schedule: 'H', category: 'cardiac', stock: 205, batch: 'GM-24C-6632', expiry: 'Mar 2027' }
  ];

  var INTERACTIONS = [
    { drugs: [1, 3], level: 'warning', text: 'Both contain <strong>Paracetamol</strong>. Combined use risks hepatotoxicity. Maximum 4g/day total.' },
    { drugs: [2, 3], level: 'warning', text: 'Both contain <strong>Paracetamol</strong>. Combined use risks hepatotoxicity. Maximum 4g/day total.' },
    { drugs: [23, 3], level: 'warning', text: 'Both contain <strong>Paracetamol</strong>. Combined use risks hepatotoxicity. Maximum 4g/day total.' },
    { drugs: [23, 1], level: 'warning', text: '<strong>Dolo-650</strong> and <strong>Calpol</strong> are both Paracetamol. Duplicate prescription — use one.' },
    { drugs: [1, 2], level: 'warning', text: '<strong>Crocin</strong> and <strong>Dolo</strong> are both Paracetamol. Duplicate prescription — use one.' },
    { drugs: [4, 5], level: 'caution', text: 'Combining <strong>Amoxicillin</strong> + <strong>Azithromycin</strong> may increase GI side effects. Verify prescriber intent.' },
    { drugs: [4, 6], level: 'caution', text: 'Combining two <strong>antibiotics</strong> — check if prescriber intended sequential or concurrent therapy.' },
    { drugs: [10, 6], level: 'caution', text: '<strong>Ciprofloxacin</strong> may cause unpredictable blood sugar changes in patients on <strong>Metformin</strong>. Monitor glucose.' },
    { drugs: [12, 14], level: 'caution', text: '<strong>Amlodipine + Metoprolol</strong> — additive blood pressure lowering. Monitor for hypotension and bradycardia.' },
    { drugs: [3, 25], level: 'warning', text: '<strong>Ibuprofen + Aspirin</strong> — NSAIDs can reduce antiplatelet effect of Aspirin and increase GI bleeding risk.' },
    { drugs: [15, 16], level: 'caution', text: 'Two <strong>ARBs</strong> (Losartan + Olmesartan) — duplicate therapy. Usually one is sufficient.' },
    { drugs: [7, 8], level: 'caution', text: 'Both are <strong>PPIs</strong> (Pantoprazole). Duplicate prescription — use one.' }
  ];

  var ALTERNATIVES = {
    1: [{ brand: 'Crocin Advance', mfg: 'GSK', price: 25 }, { brand: 'Calpol 500', mfg: 'GSK', price: 22 }, { brand: 'Pacimol 650', mfg: 'Ipca', price: 18 }],
    2: [{ brand: 'Dolo-650', mfg: 'Micro Labs', price: 30 }, { brand: 'Calpol 500', mfg: 'GSK', price: 22 }, { brand: 'Pacimol 650', mfg: 'Ipca', price: 18 }],
    23: [{ brand: 'Dolo-650', mfg: 'Micro Labs', price: 30 }, { brand: 'Crocin Advance', mfg: 'GSK', price: 25 }, { brand: 'Pacimol 650', mfg: 'Ipca', price: 18 }],
    3: [{ brand: 'Brufen 400', mfg: 'Abbott', price: 38 }, { brand: 'Ibugesic Plus', mfg: 'Cipla', price: 35 }],
    4: [{ brand: 'Moxikind-CV 625', mfg: 'Mankind', price: 145 }, { brand: 'Clavam 625', mfg: 'Alkem', price: 155 }],
    24: [{ brand: 'Augmentin 625', mfg: 'GSK', price: 185 }, { brand: 'Clavam 625', mfg: 'Alkem', price: 155 }],
    5: [{ brand: 'Zithromax 500', mfg: 'Pfizer', price: 120 }, { brand: 'Azee 500', mfg: 'Cipla', price: 78 }],
    6: [{ brand: 'Cifran 500', mfg: 'Sun Pharma', price: 72 }, { brand: 'Zoxan 500', mfg: 'FDC', price: 58 }],
    7: [{ brand: 'Pantocid-D', mfg: 'Sun Pharma', price: 110 }, { brand: 'P2 40', mfg: 'Macleods', price: 85 }],
    8: [{ brand: 'Pan-D', mfg: 'Alkem', price: 120 }, { brand: 'Pantop 40', mfg: 'Aristo', price: 72 }],
    9: [{ brand: 'Rablet 20', mfg: 'Cadila', price: 78 }, { brand: 'Happi 20', mfg: 'Panacea', price: 65 }],
    10: [{ brand: 'Obimet 500', mfg: 'Abbott', price: 32 }, { brand: 'Metsmall 500', mfg: 'Eris', price: 24 }],
    12: [{ brand: 'Amlokind 5', mfg: 'Mankind', price: 28 }, { brand: 'Amlong 5', mfg: 'Micro Labs', price: 32 }],
    13: [{ brand: 'Lipitor 10', mfg: 'Pfizer', price: 120 }, { brand: 'Atorlip 10', mfg: 'Cipla', price: 68 }],
    18: [{ brand: 'Singulair 10', mfg: 'MSD', price: 195 }, { brand: 'Montek 10', mfg: 'Sun Pharma', price: 135 }],
    25: [{ brand: 'Aspirin 75', mfg: 'Bayer', price: 28 }, { brand: 'Ecosprin AV 75', mfg: 'USV', price: 42 }]
  };

  function getScheduleClass(s) {
    if (s === 'H1') return 'h1';
    if (s === 'H') return 'h';
    return 'otc';
  }

  function search(query) {
    var q = query.toLowerCase().trim();
    if (!q) return [];
    return DRUGS.filter(function (d) {
      return d.brand.toLowerCase().indexOf(q) !== -1 ||
             d.generic.toLowerCase().indexOf(q) !== -1 ||
             d.mfg.toLowerCase().indexOf(q) !== -1;
    });
  }

  function renderResults(results) {
    var el = document.getElementById('drugResults');
    if (!results.length) {
      el.innerHTML = '<div class="drug-result-empty">No medicines found. Try another name.</div>';
      return;
    }
    el.innerHTML = results.map(function (d) {
      return '<div class="drug-result-item" data-id="' + d.id + '">' +
        '<div class="drug-result-schedule ' + getScheduleClass(d.schedule) + '">' + d.schedule + '</div>' +
        '<div class="drug-result-info">' +
          '<div class="drug-result-name">' + d.brand + '</div>' +
          '<div class="drug-result-generic">' + d.generic + ' &middot; ' + d.mfg + '</div>' +
        '</div>' +
        '<div class="drug-result-price">₹' + d.price + '</div>' +
      '</div>';
    }).join('');
  }

  function getInteractions(drugId) {
    return INTERACTIONS.filter(function (i) {
      return i.drugs.indexOf(drugId) !== -1;
    });
  }

  function renderDetail(drug) {
    var el = document.getElementById('drugDetail');
    var interactions = getInteractions(drug.id);
    var alts = ALTERNATIVES[drug.id] || [];
    var stockClass = drug.stock > 100 ? 'in-stock' : 'low-stock';
    var stockLabel = drug.stock > 100 ? 'In Stock' : 'Low Stock';

    var interactionsHtml = '';
    if (interactions.length) {
      interactionsHtml = '<div>' +
        '<div class="drug-detail-section-title">Drug Interactions</div>' +
        interactions.map(function (ix) {
          var otherDrugId = ix.drugs[0] === drug.id ? ix.drugs[1] : ix.drugs[0];
          var otherDrug = DRUGS.find(function (d) { return d.id === otherDrugId; });
          var iconColor = ix.level === 'warning' ? '#ef4444' : '#f59e0b';
          var icon = ix.level === 'warning'
            ? '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="' + iconColor + '" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
            : '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="' + iconColor + '" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>';
          return '<div class="drug-interaction-card ' + ix.level + '">' +
            icon +
            '<div class="drug-interaction-text">' + ix.text + '</div>' +
          '</div>';
        }).join('') +
      '</div>';
    } else {
      interactionsHtml = '<div>' +
        '<div class="drug-detail-section-title">Drug Interactions</div>' +
        '<div class="drug-interaction-card safe">' +
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>' +
          '<div class="drug-interaction-text">No known interactions with commonly prescribed drugs in our database.</div>' +
        '</div>' +
      '</div>';
    }

    var altsHtml = '';
    if (alts.length) {
      altsHtml = '<div>' +
        '<div class="drug-detail-section-title">Alternatives &amp; Generics</div>' +
        '<div class="drug-alt-list">' +
        alts.map(function (a) {
          var diff = drug.price - a.price;
          var savingsText = diff > 0 ? 'Save ₹' + diff : '';
          return '<div class="drug-alt-item">' +
            '<div class="drug-alt-info">' +
              '<span class="drug-alt-name">' + a.brand + '</span>' +
              '<span class="drug-alt-mfg">' + a.mfg + '</span>' +
            '</div>' +
            '<div>' +
              '<div class="drug-alt-price">₹' + a.price + '</div>' +
              (savingsText ? '<div class="drug-alt-savings">' + savingsText + '</div>' : '') +
            '</div>' +
          '</div>';
        }).join('') +
        '</div>' +
      '</div>';
    }

    el.innerHTML =
      '<div class="drug-detail-head">' +
        '<div class="drug-detail-brand">' + drug.brand + '</div>' +
        '<div class="drug-detail-generic-name">' + drug.generic + '</div>' +
        '<div class="drug-detail-meta">' +
          '<div class="drug-detail-meta-item"><strong>' + drug.mfg + '</strong></div>' +
          '<div class="drug-detail-meta-item">Schedule: <strong>' + drug.schedule + '</strong></div>' +
          '<div class="drug-detail-meta-item">₹' + drug.price + ' / ' + drug.unit + '</div>' +
        '</div>' +
      '</div>' +
      '<div class="drug-detail-body">' +
        '<div>' +
          '<div class="drug-detail-section-title">Stock &amp; Batch</div>' +
          '<div class="drug-stock-row">' +
            '<div class="drug-stock-item"><div class="label">Status</div><div class="value ' + stockClass + '">' + stockLabel + ' (' + drug.stock + ')</div></div>' +
            '<div class="drug-stock-item"><div class="label">Batch</div><div class="value">' + drug.batch + '</div></div>' +
            '<div class="drug-stock-item"><div class="label">Expiry</div><div class="value expiry">' + drug.expiry + '</div></div>' +
          '</div>' +
        '</div>' +
        interactionsHtml +
        altsHtml +
      '</div>';
  }

  function init() {
    var input = document.getElementById('drugSearchInput');
    var resultsEl = document.getElementById('drugResults');
    var hintEl = document.getElementById('drugHint');
    if (!input) return;

    input.addEventListener('input', function () {
      var q = input.value;
      if (q.length === 0) {
        resultsEl.innerHTML = '';
        hintEl.style.display = '';
        return;
      }
      hintEl.style.display = 'none';
      var results = search(q);
      renderResults(results);
    });

    resultsEl.addEventListener('click', function (e) {
      var item = e.target.closest('.drug-result-item');
      if (!item) return;
      var id = parseInt(item.getAttribute('data-id'), 10);
      var drug = DRUGS.find(function (d) { return d.id === id; });
      if (!drug) return;

      resultsEl.querySelectorAll('.drug-result-item').forEach(function (el) {
        el.classList.remove('active');
      });
      item.classList.add('active');
      renderDetail(drug);
    });

    hintEl.addEventListener('click', function (e) {
      var tag = e.target.closest('.drug-hint-tag');
      if (!tag) return;
      var q = tag.getAttribute('data-q');
      input.value = q;
      input.dispatchEvent(new Event('input'));
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
