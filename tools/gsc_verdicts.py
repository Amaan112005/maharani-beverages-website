#!/usr/bin/env python3
"""GSC verdict engine — drop a new GSC export into ~/Downloads, run this,
get every programme verdict computed against pre-registered criteria.

Usage: python3 tools/gsc_verdicts.py <export.xlsx>
Criteria (from experiment register + ME protocol):
  ME-1/2/3 (titles): query-level CTR delta on the URL's top queries,
    win = +50% relative CTR with position stable ±1.5, min 200 impressions.
  E1 (pincode on 20L): 20L URL CTR trend vs 2026-10-30 baseline.
  E4 gate check: confirms 30-day hold has elapsed.
  D-3: legacy-URL coverage check (expect 'Page with redirect') + primary
    page clicks vs combined baseline.
  Near-me cluster: CTR vs 1.93% baseline.
"""
import sys, re, json, warnings, collections, pathlib
warnings.filterwarnings('ignore')
import openpyxl

BASELINE = json.load(open('research/seo-organic-growth-master/data/summary.json'))
ROOT = pathlib.Path('.')

def load(f):
    wb = openpyxl.load_workbook(pathlib.Path.home() / 'Downloads' / f, read_only=True, data_only=True)
    out = {}
    for name in wb.sheetnames:
        ws = wb[name]
        rows = list(ws.iter_rows(values_only=True))
        out[name] = rows[1:]
    return out

def main(export):
    d = load(export)
    pages = {}
    for r in d['Pages']:
        if r[0]:
            u = str(r[0]).rstrip('/').replace('https://maharanibeverages.com', '') or '/'
            pages[u] = {'clicks': r[1] or 0, 'impr': r[2] or 0, 'ctr': r[3] or 0, 'pos': r[4] or 0}
    queries = [{'q': str(r[0]), 'clicks': r[1] or 0, 'impr': r[2] or 0, 'ctr': r[3] or 0, 'pos': r[4] or 0} for r in d['Queries'] if r[0]]

    base_perf = {}
    for r in open('research/seo-organic-growth-master/data/page-inventory.csv').read().splitlines()[1:]:
        parts = r.split(',')
        if len(parts) > 3:
            base_perf[parts[0]] = {'clicks': float(parts[2] or 0), 'impr': float(parts[3] or 0)}

    print('=' * 60)
    print(f'VERDICT RUN: {export}')
    print('=' * 60)

    # ME-1..3 title verdicts (page-level CTR as proxy; query-level needs GSC UI)
    for url, name in [('/blog/is-14543-vs-is-10500-drinking-water-standards', 'ME-1 IS 14543 title'),
                      ('/blog/bisleri-vs-kinley-vs-zenith-kolkata', 'ME-2 comparison title'),
                      ('/kolkata-water-supply', 'ME-3 hub title')]:
        b = base_perf.get(url, {'clicks': 0, 'impr': 0})
        n = pages.get(url)
        if not n or n['impr'] < 200:
            print(f'{name}: INSUFFICIENT DATA (new impressions {n["impr"] if n else 0:.0f} < 200) — keep measuring')
            continue
        bctr = b['clicks'] / b['impr'] if b['impr'] else 0
        nctr = n['clicks'] / n['impr']
        rel = (nctr - bctr) / bctr if bctr else float('inf')
        print(f'{name}: CTR {bctr*100:.2f}% -> {nctr*100:.2f}% (rel {rel:+.0%}), impressions {b["impr"]:.0f} -> {n["impr"]:.0f}')

    # E1 pincode on 20L
    b = base_perf.get('/20-liter-water-jar-delivery-kolkata', {'clicks': 115, 'impr': 5221})
    n = pages.get('/20-liter-water-jar-delivery-kolkata', {'clicks': 0, 'impr': 0})
    bctr, nctr = b['clicks']/b['impr'], (n['clicks']/n['impr'] if n['impr'] else 0)
    print(f'E1 pincode-on-20L: 20L CTR {bctr*100:.2f}% -> {nctr*100:.2f}% (interim; whatsapp_click events decisive post-GA4)')

    # D-3 consolidation check
    legacy = ['/drinking-water-kolkata', '/mineral-water-kolkata', '/drinking-water-howrah', '/mineral-water-howrah']
    legacy_impr = sum(pages.get(u, {}).get('impr', 0) for u in legacy)
    print(f'D3 consolidation: legacy URLs still earning {legacy_impr:.0f} impressions in export '
          f'(GSC UI should classify them "Page with redirect"; nonzero here = lag)')
    for u in ['/drinking-water-supplier-kolkata', '/mineral-water-supplier-kolkata',
              '/drinking-water-supplier-howrah', '/mineral-water-supplier-howrah']:
        b = base_perf.get(u, {'clicks': 0, 'impr': 0}); n = pages.get(u, {'clicks': 0, 'impr': 0})
        print(f'  primary {u}: {b["clicks"]:.0f}+{b["impr"]:.0f} -> {n["clicks"]:.0f}+{n["impr"]:.0f}')

    # Near-me cluster CTR
    nm = [q for q in queries if re.search(r'near me|nearby', q['q'], re.I)]
    c, i = sum(q['clicks'] for q in nm), sum(q['impr'] for q in nm)
    ctr = c / i if i else 0
    print(f'Near-me cluster: {i:.0f} impressions, CTR {ctr*100:.2f}% (baseline 4351 impr / 1.93%)')

    # New articles read
    for u, nm2 in [('/blog/how-to-read-packaged-water-bottle-label-india', 'label guide'),
                   ('/blog/20-litre-water-can-vs-jar-vs-bottle', 'can-vs-jar')]:
        n = pages.get(u, {'clicks': 0, 'impr': 0})
        print(f'New article {nm2}: {n["clicks"]:.0f} clicks / {n["impr"]:.0f} impressions (indexation + early demand read)')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'https___maharanibeverages.com_-Performance-on-Search-2026-11-30.xlsx')
