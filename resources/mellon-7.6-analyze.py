#!/usr/bin/env python3
"""Reproduce 7.6 from pinned public annual exports; no network or CSV output.

Usage: python3 scripts/analyze-mellon-7-6-aapi.py --source-root ../ --output outputs/mellon-7.6 --itu-config config/mellon-7/itu-2026-provisional-7.6.json
Weekly GeoJSON top-level features are interval measurements. The similarly named
JSON collection_week array is a cumulative prefix and is deliberately not used.
"""
import argparse
from datetime import date
import gzip
import hashlib
import json
import re
from pathlib import Path
import subprocess

COHORTS = {
    'pitt-201': (2026, 'The Pitt 201–203', ['IND', 'PHL', 'AUS']),
    'pitt-213': (2026, 'The Pitt 213–215', ['IND', 'PHL', 'AUS']),
    'bear-05': (2026, 'The Bear S05', ['IND', 'PHL', 'AUS']),
    'bear-02': (2023, 'The Bear S02', ['IND', 'PHL', 'AUS']),
    'bear-03': (2024, 'The Bear S03', ['IND', 'PHL', 'AUS']),
    'bear-04': (2025, 'The Bear S04', ['IND', 'PHL', 'AUS']),
    'godzilla-minus-one': (2024, 'Godzilla Minus One', ['JPN', 'USA', 'CHN', 'KOR']),
    'godzilla-x-kong-the-new-empire': (2024, 'Godzilla x Kong', ['JPN', 'USA', 'CHN', 'KOR']),
    'godzilla-vs-kong': (2021, 'Godzilla vs. Kong', ['JPN', 'USA', 'CHN', 'KOR']),
    'monarch-legacy-of-monsters-101': (2023, 'Monarch 101', ['JPN', 'USA', 'CHN', 'KOR']),
    'monarch-legacy-of-monsters-110': (2024, 'Monarch 110', ['JPN', 'USA', 'CHN', 'KOR']),
    'monarch-legacy-of-monsters-201': (2026, 'Monarch 201', ['JPN', 'USA', 'CHN', 'KOR']),
    'monarch-legacy-of-monsters-208': (2026, 'Monarch 208', ['JPN', 'USA', 'CHN', 'KOR']),
}
GROUPS = {
    'pitt-bear-compare': ['pitt-201', 'pitt-213', 'bear-05', 'bear-02', 'bear-03', 'bear-04'],
    'godzilla': ['godzilla-minus-one', 'godzilla-x-kong-the-new-empire', 'godzilla-vs-kong',
                'monarch-legacy-of-monsters-101', 'monarch-legacy-of-monsters-110',
                'monarch-legacy-of-monsters-201', 'monarch-legacy-of-monsters-208'],
}
FIELDS = ['size', 'mobile', 'satellite', 'tor', 'tor_exit_nodes', 'vpn', 'relay', 'proxy', 'hosting', 'service']
ROLES = ['downloaders', 'uploaders']


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def empty():
    return {r: {f: 0 for f in FIELDS} for r in ROLES}


def add(target, source):
    for r in ROLES:
        for f in FIELDS:
            value = source[r][f]
            assert isinstance(value, int) and value >= 0
            if f != 'size':
                assert value <= source[r]['size']
            target[r][f] += value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--reuse', action='store_true', help='Reuse completed objects only after checking commit and every source hash.')
    parser.add_argument('--itu-config', type=Path, required=True, help='Explicit versioned ITU estimates and reference-year status.')
    parser.add_argument('--pitt-weeks', type=int, choices=[10, 15, 26], default=10)
    parser.add_argument('--godzilla-weeks', type=int, choices=[10, 15, 26], default=15)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    results = {'schema_version': 3, 'windows': {'pitt-bear-compare': list(range(1, args.pitt_weeks + 1)), 'godzilla': list(range(1, args.godzilla_weeks + 1))},
               'groups': GROUPS,
               'unit': 'Sum of interval GeoJSON swarm weights across the selected weeks; repeated peers may recur across weeks and torrents. Not unique people.',
               'denominator': 'Worldwide top-level aggregate features in the same selected weeks, including unclassified countries.',
               'objects': {}}
    for key, (year, label, countries) in COHORTS.items():
        repo = args.source_root / f'alpha60-results-{year}'
        commit = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
        group = next(g for g, keys in GROUPS.items() if key in keys)
        weeks = results['windows'][group]
        cached = args.output / f'{key}.json'
        if args.reuse and cached.exists() and [w['week'] for w in json.loads(cached.read_text())['weeks']] == list(weeks):
            record = json.loads(cached.read_text())
            assert record['source_commit'] == commit
            assert all(digest((repo / s['path']).read_bytes()) == s['sha256'] for s in record['sources'])
            results['objects'][key] = record
            print(key, 'reused after hash verification', flush=True)
            continue
        base = f'https://github.com/alpha60-devops/{repo.name}/blob/{commit}/'
        sources = []

        def read(relative):
            path = repo / relative
            # Refuse an uncommitted source: pinning HEAD must identify the bytes used.
            changed = subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain', '--', relative], text=True)
            assert not changed, (path, changed)
            raw = path.read_bytes()
            sources.append({'path': relative, 'url': base + relative, 'sha256': digest(raw)})
            return gzip.decompress(raw) if path.suffix == '.gz' else raw

        meta = json.loads(read(f'data/json/{key}-cumulative.json'))
        audit = read(f'docs/itemized/{key}-sample-cache-audit.md').decode()
        record = {'label': label, 'year': year, 'source_commit': commit, 'countries': countries,
                  'sample_duration': meta['sample_duration'], 'sample_days': meta['sample_days'],
                  'collection_id': meta['collection_id'], 'data_version': meta['data_version'],
                  'ip_geolocation_version': meta['ip_geolocation_version'],
                  'coverage_notes': [l for l in audit.splitlines() if 'missing' in l.lower() or 'hourly gap:' in l],
                  'weeks': [], 'world': empty(), 'country': {c: empty() for c in countries}}
        cities = {}
        for week in weeks:
            relative = f'data/geojson.week/{key}-week-{week:05d}.geojson.gz'
            doc = json.loads(read(relative))
            assert doc['id'] == key and doc['duration_index'] == week and doc['duration_type'] == 'week'
            assert doc['swarm_hexagon_resolution'] == 5 and doc['swarm_size_min'] == 3
            dates = doc['datestamp'].removesuffix('-partial').split('-to-')
            assert len(dates) == 2 and len(dates[1]) == 10, doc['datestamp']
            assert (date.fromisoformat(min(dates[1], record['sample_duration'][-10:])) - date.fromisoformat(dates[0])).days == 6
            row = {'week': week, 'dates': doc['datestamp'], 'features': len(doc['features']),
                   'world': empty(), 'country': {c: empty() for c in countries}}
            for feature in doc['features']:
                p = feature['properties']
                add(row['world'], p)
                country = p['country_code']
                if country in countries:
                    add(row['country'][country], p)
                    city_id = country + ':' + str(p['geoname_id'])
                    if city_id not in cities:
                        cities[city_id] = {'id': city_id, 'country': country, 'city': p['city'],
                                           'coordinates': feature['geometry']['coordinates'], **empty()}
                    add(cities[city_id], p)
            add(record['world'], row['world'])
            for c in countries:
                add(record['country'][c], row['country'][c])
            record['weeks'].append(row)
            del doc
            print(key, week, row['dates'], row['world']['downloaders']['size'], flush=True)
        record['cities'] = list(cities.values())
        record['sources'] = sources
        results['objects'][key] = record
        (args.output / f'{key}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    results['coverage_sensitivity'] = {}
    for group, keys in GROUPS.items():
        affected = set()
        for key in keys:
            record = results['objects'][key]
            for week in record['weeks']:
                begin, end = week['dates'].removesuffix('-partial').split('-to-')
                if week['dates'].endswith('-partial'):
                    affected.add(week['week'])
                for note in record['coverage_notes']:
                    dates = re.findall(r'\d{4}-\d{2}-\d{2}', note)
                    if dates and min(dates) <= end and max(dates) >= begin:
                        affected.add(week['week'])
        retained = [w for w in results['windows'][group] if w not in affected]
        sensitivity = {'excluded_weeks_in_all_objects': sorted(affected), 'retained_weeks': retained, 'objects': {}}
        for key in keys:
            record = results['objects'][key]
            value = {'world': empty(), 'country': {c: empty() for c in record['countries']}}
            for week in record['weeks']:
                if week['week'] in retained:
                    add(value['world'], week['world'])
                    for c in record['countries']:
                        add(value['country'][c], week['country'][c])
            sensitivity['objects'][key] = value
        results['coverage_sensitivity'][group] = sensitivity
    policy = json.loads(args.itu_config.read_text())
    assert policy['reference_year'] == 2026 and policy['reference_users_billions'] > 0
    results['itu_policy'] = policy
    results['itu_policy_sha256'] = digest(args.itu_config.read_bytes())

    def scale(value, factor):
        return {k: scale(v, factor) if isinstance(v, dict) else v * factor for k, v in value.items()}

    for key, record in results['objects'].items():
        source_year = int(record['sample_duration'][:4])
        assert source_year == record['year']
        source_users = policy['years'][str(source_year)]['users_billions']
        factor = policy['reference_users_billions'] / source_users
        record['itu_2026'] = {'source_year': source_year, 'source_users_billions': source_users,
                              'reference_users_billions': policy['reference_users_billions'],
                              'factor': factor, 'status': policy['reference_status'],
                              'world': scale(record['world'], factor),
                              'country': scale(record['country'], factor),
                              'weeks': [{'week': w['week'], 'world': scale(w['world'], factor),
                                         'country': scale(w['country'], factor)} for w in record['weeks']]}
        if source_year == 2024:
            revised_factor = policy['reference_users_billions'] / policy['revision_sensitivity']['2024_users_billions']
            record['itu_2026']['revised_2024_scenario'] = {'factor': revised_factor, 'world': scale(record['world'], revised_factor), 'country': scale(record['country'], revised_factor)}
    (args.output / 'analysis.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
