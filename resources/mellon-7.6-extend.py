#!/usr/bin/env python3
"""Add available weeks 1–26 and Pitt 201 resolution-country measurements.

Consumes the matched-window ledger produced by analyze-mellon-7-6-aapi.py.
The country plates use nested by-BTIH features exclusively, joined to the
canonical unique-BTIH inventory by BOTH member ID and exact name.
"""
import argparse
from datetime import date
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

ANALYZER = Path(__file__).with_name('analyze-mellon-7-6-aapi.py')
if not ANALYZER.exists():
    ANALYZER = Path(__file__).with_name('mellon-7.6-analyze.py')
SPEC = importlib.util.spec_from_file_location('analysis', ANALYZER)
analysis = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(analysis)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ledger', type=Path, required=True)
    p.add_argument('--source-root', type=Path, required=True)
    args = p.parse_args()
    data = json.loads(args.ledger.read_text())
    plates = {'collection_key': 'pitt-201', 'weeks': list(range(1, 27)),
              'groups': {'ge1080': '>=1080p: 1080 and 2160', 'lt1080': '<1080p: 720 and sd', 'unknown': 'Unclassified resolution'},
              'unit': 'Sum of published by-BTIH geographic feature weights over weeks 1–26, not unique people or the top-level aggregate product.',
              'country': {c: {g: analysis.empty() for g in ['ge1080', 'lt1080', 'unknown']} for c in ['PHL', 'IND', 'AUS']},
              'cities': {}, 'members': [], 'weekly_country': [], 'sources': []}
    for key, record in data['objects'].items():
        if record['countries'] != ['IND', 'PHL', 'AUS']:
            continue
        repo = args.source_root / f"alpha60-results-{record['year']}"
        assert subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip() == record['source_commit']

        def read(relative):
            assert not subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain', '--', relative], text=True)
            raw = (repo / relative).read_bytes()
            source = {'path': relative, 'url': f"https://github.com/alpha60-devops/{repo.name}/blob/{record['source_commit']}/{relative}", 'sha256': hashlib.sha256(raw).hexdigest()}
            if not any(s['path'] == relative for s in record['sources']):
                record['sources'].append(source)
            if key == 'pitt-201':
                plates['sources'].append(source)
            return json.loads(gzip.decompress(raw) if relative.endswith('.gz') else raw)

        if key == 'pitt-201':
            metadata = read('data/json/pitt-201-cumulative-btiha-media-objects.json')
            members = {(m['id'], m['name']): m for m in metadata['collection_cumulative_by_btiha']}
            assert len(members) == len(metadata['collection_cumulative_by_btiha'])
            assert len({m['btih'] for m in members.values()}) == len(members)
            for m in members.values():
                resolution = m['resolution']
                group = 'ge1080' if resolution in ['1080', '2160'] else 'lt1080' if resolution in ['720', 'sd'] else 'unknown'
                plates['members'].append({'id': m['id'], 'name': m['name'], 'btih': m['btih'], 'resolution': resolution, 'group': group})
            groups = {(m['id'], m['name']): m['group'] for m in plates['members']}
        extended = []
        excluded = []
        for week in range(1, 27):
            relative = f'data/geojson.week/{key}-week-{week:05d}.geojson.gz'
            if not (repo / relative).exists():
                excluded.append({'week': week, 'reason': 'not available'})
                continue
            existing = next((w for w in record['weeks'] if w['week'] == week), None)
            doc = None
            if existing is not None and key != 'pitt-201':
                row = existing
            else:
                doc = read(relative)
                assert doc['id'] == key and doc['duration_index'] == week
                row = {'week': week, 'dates': doc['datestamp'], 'features': len(doc['features']), 'world': analysis.empty(), 'country': {c: analysis.empty() for c in record['countries']}}
                for f in doc['features']:
                    prop = f['properties']
                    analysis.add(row['world'], prop)
                    if prop['country_code'] in row['country']:
                        analysis.add(row['country'][prop['country_code']], prop)
                if existing:
                    assert row == existing
            first, last = row['dates'].removesuffix('-partial').split('-to-')
            # GeoJSON headers can name a full nominal week beyond the actual
            # sample cutoff. The cumulative metadata supplies that cutoff.
            last = min(last, record['sample_duration'][-10:])
            span = (date.fromisoformat(last) - date.fromisoformat(first)).days + 1
            if span < 7:
                excluded.append({'week': week, 'reason': 'short trailing interval', 'dates': row['dates'], 'calendar_days': span})
                continue
            extended.append(row)
            if key == 'pitt-201':
                seen = set()
                weekly = {'week': week, 'dates': row['dates'], 'country': {c: {g: analysis.empty() for g in plates['groups']} for c in plates['country']}}
                for member in doc['collection_week_by_btiha']:
                    identity = (member['tid'], member['id'])
                    assert identity in members and identity not in seen
                    seen.add(identity)
                    group = groups[identity]
                    for f in member['features']:
                        prop = f['properties']
                        country = prop['country_code']
                        if country not in plates['country']:
                            continue
                        analysis.add(plates['country'][country][group], prop)
                        analysis.add(weekly['country'][country][group], prop)
                        city_key = f"{country}:{prop['geoname_id']}"
                        if city_key not in plates['cities']:
                            plates['cities'][city_key] = {'id': city_key, 'city': prop['city'], 'country': country, 'coordinates': f['geometry']['coordinates'], **{g: analysis.empty() for g in plates['groups']}}
                        analysis.add(plates['cities'][city_key][group], prop)
                assert seen == set(members)
                plates['weekly_country'].append(weekly)
            print(key, 'extended week', week, flush=True)
        record['extended_weeks'] = extended
        record['extended_exclusions'] = excluded
    assert [w['week'] for w in plates['weekly_country']] == list(range(1, 27))
    plates['cities'] = list(plates['cities'].values())
    data['pitt_201_resolution_plates'] = plates
    args.ledger.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
