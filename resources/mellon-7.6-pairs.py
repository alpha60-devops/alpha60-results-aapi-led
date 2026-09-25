#!/usr/bin/env python3
"""Compare reviewed AAPI / non-USA Asian-global pairs in an exact week prefix.

Raw interval geography is reduced independently of the identity/citizenship
metadata. The latter selects and describes the objects; it does not classify
swarm participants. All ten fields and both roles remain inspectable in JSON.
"""
import argparse
from datetime import date
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

ANALYZER = Path(__file__).with_name('analyze-mellon-7-6-aapi.py')
if not ANALYZER.exists():
    ANALYZER = Path(__file__).with_name('mellon-7.6-analyze.py')
SPEC = importlib.util.spec_from_file_location('analysis', ANALYZER)
analysis = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(analysis)

PAIRS = [
    {'id': 'original', 'aapi': 'american-born-chinese-01', 'global': 'no-more-bets'},
    {'id': 'action-films', 'aapi': 'shang-chi-and-the-legend-of-the-ten-rings', 'global': 'vanguard'},
    {'id': 'beef-lazarus', 'aapi': 'beef-02', 'global': 'lazarus-101'},
]
OBJECTS = {
    'american-born-chinese-01': (2023, 'American Born Chinese'),
    'no-more-bets': (2023, 'No More Bets'),
    'shang-chi-and-the-legend-of-the-ten-rings': (2021, 'Shang-Chi'),
    'vanguard': (2020, 'Vanguard'),
    'beef-02': (2026, 'Beef S02'),
    'lazarus-101': (2025, 'Lazarus 101'),
}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root', type=Path, required=True)
    p.add_argument('--metadata-root', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--weeks', type=int, choices=[10, 15, 26], default=15)
    args = p.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    metadata_path = args.metadata_root / 'reports/candidates/h15-v3.generated.json'
    raw = metadata_path.read_bytes()
    report = json.loads(raw)
    metadata_commit = subprocess.check_output(
        ['git', '-C', str(args.metadata_root), 'rev-parse', 'HEAD'], text=True).strip()
    assert not subprocess.check_output(
        ['git', '-C', str(args.metadata_root), 'status', '--porcelain', '--',
         str(metadata_path.relative_to(args.metadata_root))], text=True)
    groups = {s['slice_key']: {c['collection_key']: c for c in s['candidates']}
              for s in report['slices']}
    asia = {c['code'] for c in report['country_sets']['asia-28']}
    assert len(asia) == 28 and 'TWN' in asia and 'USA' not in asia
    result = {
        'schema_version': 1, 'weeks': list(range(1, args.weeks + 1)),
        'pairs': PAIRS, 'objects': {}, 'asia_country_codes': sorted(asia),
        'metadata_source': {
            'commit': metadata_commit, 'sha256': hashlib.sha256(raw).hexdigest(),
            'artifact_digest': report['artifact_digest'], 'definition_id': report['definition_id'],
            'url': 'https://github.com/alpha60-devops/alpha60-swarm-metadata/blob/'
                   + metadata_commit + '/reports/candidates/h15-v3.generated.json',
        },
        'method': {
            'unit': 'Summed top-level weekly aggregate GeoJSON swarm weights; repeated peers may recur. Not unique people or completed downloads.',
            'geography': 'USA and Asia-28 (including TWN); worldwide denominators retain other and unclassified countries.',
            'shares': 'Each role and field divides by its corresponding worldwide role/field total. Mobile, hosting and VPN rates divide by country/region size.',
            'selection': 'AAPI side: confirmed aapi-led, USA production, >=2 confirmed USA citizens. Global side: confirmed asian-led-global, non-USA production, <=1 confirmed USA citizens. These identity slices overlap.',
            'adjustment': 'Geographic shares and raw weights; no Internet-user multiplier is applied to this paired geography analysis.',
        },
    }
    for pair in PAIRS:
        for side, skey in [('aapi', 'aapi-led'), ('global', 'asian-led-global')]:
            key = pair[side]
            candidate = groups[skey][key]
            assert candidate['disposition'] == 'confirmed'
            citizens = candidate['usa_citizen_actors_creators']['count']
            assert candidate['usa_production']['value'] is (side == 'aapi')
            assert citizens >= 2 if side == 'aapi' else citizens <= 1
            year, label = OBJECTS[key]
            repo = args.source_root / f'alpha60-results-{year}'
            commit = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
            sources = []

            def read(relative):
                assert not subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain', '--', relative], text=True)
                payload = (repo / relative).read_bytes()
                sources.append({'path': relative, 'sha256': hashlib.sha256(payload).hexdigest(),
                                'url': f'https://github.com/alpha60-devops/{repo.name}/blob/{commit}/{relative}'})
                return gzip.decompress(payload) if relative.endswith('.gz') else payload

            meta = json.loads(read(f'data/json/{key}-cumulative.json'))
            audit = read(f'docs/itemized/{key}-sample-cache-audit.md').decode()
            record = {
                'label': label, 'year': year, 'source_commit': commit,
                'sample_duration': meta['sample_duration'], 'collection_id': meta['collection_id'],
                'data_version': meta['data_version'], 'ip_geolocation_version': meta['ip_geolocation_version'],
                'eligibility': {k: candidate[k] for k in [
                    'candidate_id', 'disposition', 'reviewed_counts', 'usa_production',
                    'usa_citizen_actors_creators', 'scope_alignment', 'coverage']},
                'selected_slice': skey, 'weeks': [], 'world': analysis.empty(),
                'regions': {c: analysis.empty() for c in ['USA', 'Asia-28']},
                'countries': {},
                'coverage_notes': [line for line in audit.splitlines()
                                   if 'missing' in line.lower() or 'hourly gap:' in line],
            }
            for week in result['weeks']:
                doc = json.loads(read(f'data/geojson.week/{key}-week-{week:05d}.geojson.gz'))
                assert doc['id'] == key and doc['duration_index'] == week and doc['duration_type'] == 'week'
                assert doc['swarm_hexagon_resolution'] == 5 and doc['swarm_size_min'] == 3
                start, end = doc['datestamp'].removesuffix('-partial').split('-to-')
                cutoff = min(end, record['sample_duration'][-10:])
                assert (date.fromisoformat(cutoff) - date.fromisoformat(start)).days == 6
                row = {'week': week, 'dates': doc['datestamp'], 'features': len(doc['features']),
                       'world': analysis.empty(), 'regions': {c: analysis.empty() for c in ['USA', 'Asia-28']}}
                for feature in doc['features']:
                    values = feature['properties']; code = values['country_code']
                    analysis.add(row['world'], values)
                    analysis.add(record['countries'].setdefault(code, analysis.empty()), values)
                    if code == 'USA': analysis.add(row['regions']['USA'], values)
                    if code in asia: analysis.add(row['regions']['Asia-28'], values)
                analysis.add(record['world'], row['world'])
                for region in row['regions']: analysis.add(record['regions'][region], row['regions'][region])
                record['weeks'].append(row)
                print(key, week, row['dates'], row['world']['downloaders']['size'], flush=True)
                del doc
            record['sources'] = sources
            result['objects'][key] = record
            (args.output / f'{key}.json').write_text(json.dumps(record, indent=2, ensure_ascii=False)+'\n')
        excluded = set()
        for key in [pair['aapi'], pair['global']]:
            record = result['objects'][key]
            for week in record['weeks']:
                start, end = week['dates'].removesuffix('-partial').split('-to-')
                if week['dates'].endswith('-partial'): excluded.add(week['week'])
                for note in record['coverage_notes']:
                    dates = re.findall(r'\d{4}-\d{2}-\d{2}', note)
                    if dates and min(dates) <= end and max(dates) >= start: excluded.add(week['week'])
        pair['coverage_sensitivity'] = {'excluded_weeks': sorted(excluded),
                                        'retained_weeks': sorted(set(result['weeks'])-excluded), 'objects': {}}
        for key in [pair['aapi'], pair['global']]:
            record = result['objects'][key]
            totals = {'world': analysis.empty(), 'regions': {c: analysis.empty() for c in ['USA', 'Asia-28']}}
            for week in record['weeks']:
                if week['week'] in excluded: continue
                analysis.add(totals['world'], week['world'])
                for region in week['regions']: analysis.add(totals['regions'][region], week['regions'][region])
            pair['coverage_sensitivity']['objects'][key] = totals
    (args.output / 'pairs.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')


if __name__ == '__main__':
    main()
