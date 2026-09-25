"""Six resolution detail plates drawn exclusively with Izzi and Cartofreako.

Uses the same lake-subtracted, seam-split vector land as the native city maps.
City weights retain the approved weekly by-BTIH grain and weeks 1–26.
"""
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess

from shapely.geometry import Point, box, mapping, shape

COUNTRIES = {'PHL': 'Philippines', 'AUS': 'Australia', 'IND': 'India',
             'JPN': 'Japan', 'CHN': 'China', 'KOR': 'South Korea'}
GROUPS = [('ge1080', '≥1080p (1080 + 2160)'), ('lt1080', '<1080p (720 + SD)')]
AREA = .012  # Actual circle area in square points per downloader weight.
AUS_EXTENT = (112, -44, 154, -9)  # Mainland, Tasmania and adjacent islands.


def render_country_plates(site, native, izzi, plates, table, figure):
    root = Path(__file__).parent
    renderer = root / 'mellon-7-6-resolution-maps.cc'
    executable = native.directory / 'resolution-maps'
    subprocess.run(['g++', '-std=c++20', '-O2', '-I'+str(izzi/'src'),
                    '-I'+str(native.directory), str(renderer), '-o', str(executable)], check=True)
    assert list(plates['country']) == list(COUNTRIES)
    text = '''
## Pitt 201–203: combined resolution country close-ups

These six plates cover **Philippines (PHL), Australia (AUS), India (IND),
Japan (JPN), China (CHN), and South Korea (KOR)**, with **≥1080p (1080 and
2160)** and **<1080p (720 and SD)** together on each country map. They cover
**weeks 1–26, January 9–July 9, 2026**. Pink filled circles show ≥1080p;
orange rings show <1080p. Circle **area** represents downloader weight on
one scale across all six plates. The two groups share city centers.
Hover or focus a circle for its count and mobile rate.

The source is the weekly **by-BTIH geographic product**, joined to all 392
canonical, unique-BTIH torrent records by member ID and exact name: 236 torrents
at ≥1080p and 156 below 1080p; none have unclassified resolution. Weights repeat
across torrents and weeks. This product has a different aggregation grain from
the top-level weekly geographic product used in the comparison tables above;
its totals are not interchangeable with those tables or unique-person counts.
Missing sampling hours remain unadjusted, including the reported July 3 gap.

**Izzi and Cartofreako** draw the vector plates using the audit's registered
Cahill–Keyes projection. Each country outline and its mapped city
coordinates fit the available panel width or height while preserving projected
proportions. Geographic scale differs by country. Lake water is removed from
the land polygons; interior holes and projection seams are preserved.
Australia retains the mainland/Tasmania close-up; offshore islands across a
projection cut would shrink the mainland. All sampled Australian cities fit
this extent. The other five countries use their complete outlines.
'''
    rows = []
    for code, country in COUNTRIES.items():
        for group, label in GROUPS:
            values = plates['country'][code][group]['downloaders']
            rate = f"{100*values['mobile']/values['size']:.2f}%" if values['size'] else '—'
            rows.append([country, label, f"{values['size']:,}", rate])
    text += table(['Country', 'Resolution group', 'Downloader weight', 'Mobile rate'], rows)
    boundaries = json.loads(native.boundaries.read_text())
    boundaries['countries'] = [c for c in boundaries['countries'] if c['iso3'] in COUNTRIES]
    australia = next(c for c in boundaries['countries'] if c['iso3'] == 'AUS')
    cropped = shape(australia['geometry']).intersection(box(*AUS_EXTENT))
    assert cropped.geom_type == 'MultiPolygon' and cropped.is_valid
    australia['geometry'] = mapping(cropped)
    australia['extent_lon_lat'] = AUS_EXTENT
    australia['lakes_removed'] = [lake for lake in australia['lakes_removed']
                                  if box(*AUS_EXTENT).covers(Point(lake['water_reference']))]
    boundary_path = site / 'data/mellon-7.6-resolution-map-boundaries.json'
    boundary_path.write_text(json.dumps(boundaries, ensure_ascii=False, separators=(',', ':')) + '\n')
    provenance = {
        'renderer': 'Izzi circle_element / svg_element; Cartofreako native Cahill–Keyes',
        'renderer_sha256': hashlib.sha256(renderer.read_bytes()).hexdigest(),
        'projection': {k: v for k, v in native.provenance.items() if k != 'renderer_sha256'},
        'boundary_file': boundary_path.name,
        'boundary_sha256': hashlib.sha256(boundary_path.read_bytes()).hexdigest(),
        'area_points_squared_per_weight': AREA,
        'circle_radius_formula': 'sqrt(downloader_weight * 0.012 / pi)',
        'canvas_points': [720, 770],
        'fit': 'Country land and located cities; Australia mainland/Tasmania crop; uniform scale; room for largest circle.',
        'countries': {},
    }
    for code, country in COUNTRIES.items():
        local = [city for city in plates['cities'] if city['country'] == code]
        plotted = [city for city in local if int(city['id'].split(':')[1]) > 0
                   and all(math.isfinite(v) for v in city['coordinates'])
                   and -180 <= city['coordinates'][0] <= 180 and -90 <= city['coordinates'][1] <= 90]
        if code == 'AUS':
            assert all(AUS_EXTENT[0] <= city['coordinates'][0] <= AUS_EXTENT[2]
                       and AUS_EXTENT[1] <= city['coordinates'][1] <= AUS_EXTENT[3] for city in plotted)
        plotted.sort(key=lambda city: (-sum(city[g]['downloaders']['size'] for g, _ in GROUPS), city['id']))
        cities = []
        for city in plotted:
            marks = []
            for group, label in GROUPS:
                values = city[group]['downloaders']
                count, mobile = values['size'], values['mobile']
                rate = f'{100*mobile/count:.2f}%' if count else '—'
                marks.append({'weight': count, 'tooltip': f"{city['city']}, {country} · {label} · {count:,} downloader weight · Mobile {mobile:,} ({rate}) · Weeks 1–26, 2026-01-09 to 2026-07-09 · by-BTIH product"})
            cities.append({k: city[k] for k in ['id', 'city', 'coordinates']} | {'marks': marks})
        name = 'mellon-7.6-pitt-201-' + code.lower()
        description = f'Combined ≥1080p and <1080p downloader weights. Weeks 1–26. {len(plotted)} identified city locations. One circle-area scale across all six countries.'
        payload = {'code': code, 'title': f'{country}: Pitt 201–203 resolution swarms',
                   'subtitle': description, 'area_points_squared_per_weight': AREA,
                   'canvas_points': provenance['canvas_points'], 'cities': cities}
        native.render(name, payload, executable=executable, boundaries=boundary_path)
        omitted = {g: plates['country'][code][g]['downloaders']['size'] - sum(c[g]['downloaders']['size'] for c in plotted) for g, _ in GROUPS}
        outline = next(c for c in boundaries['countries'] if c['iso3'] == code)
        provenance['countries'][code] = {'city_rows': len(local), 'plotted_city_rows': len(plotted),
                                        'unlocated_downloader_weight': omitted,
                                        'lake_features_removed': len(outline['lakes_removed']),
                                        'extent_lon_lat': AUS_EXTENT if code == 'AUS' else None}
        text += '\n### ' + country + '\n'
        text += figure(site, name, description + (' Australia extent: mainland and Tasmania.' if code == 'AUS' else '') + " Country outlines use Natural Earth’s de facto boundaries; map orientation follows the registered audit projection.")
        text += f"Unlocated downloader weight: ≥1080p **{omitted['ge1080']:,}**; <1080p **{omitted['lt1080']:,}**. These weights remain in the country totals above.\n"
        text += '\n<details markdown="1"><summary>' + country + ': top ten mapped cities and mobile rates</summary>\n'
        text += table(['City', '≥1080p weight', '≥1080p mobile rate', '<1080p weight', '<1080p mobile rate'], [[c['city']] + [value for g, _ in GROUPS for value in [f"{c[g]['downloaders']['size']:,}", f"{100*c[g]['downloaders']['mobile']/c[g]['downloaders']['size']:.2f}%" if c[g]['downloaders']['size'] else '—']] for c in plotted[:10]])
        text += '\n</details>\n'
    (site / 'data/mellon-7.6-country-plates-provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
    for path in [renderer, Path(__file__), root/'mellon_7_6_native_maps.py',
                 root/'mellon-7-6-city-maps.cc', root/'prepare-country-cartography.py']:
        shutil.copyfile(path, site / 'resources' / path.name)
    text += f"\nProjection: [Cartofreako native Cahill–Keyes]({native.provenance['url']}), with its one-degree longitude registration; developed from the Cahill–Keyes work of Gene Keyes and Mary Jo Graça. [Izzi renderer](../resources/mellon-7-6-resolution-maps.cc). Basemap: Natural Earth v5.1.2 1:10m countries and lakes, public domain. [Country and lake geometry with upstream hashes](../data/mellon-7.6-resolution-map-boundaries.json) and [projection, extent, circle-area and omitted-weight provenance](../data/mellon-7.6-country-plates-provenance.json). Member resolutions, all cities, weekly group totals and pinned source hashes are in the calculation ledger.\n"
    return text
