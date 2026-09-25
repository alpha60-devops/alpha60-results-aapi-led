"""Publish verified a60-carto-geo country plates from the original sample cache.

Drawing, labels, projection and member colors all come from the native audit
renderer. This module only verifies/copies assets and assembles the Markdown.
"""
import html
import json
from pathlib import Path
import shutil

from country_cartography import digest

COUNTRIES = {'PHL': 'Philippines', 'AUS': 'Australia', 'IND': 'India',
             'JPN': 'Japan', 'CHN': 'China', 'KOR': 'South Korea'}


def render_country_plates(site, manifest_path, table):
    manifest_path = Path(manifest_path)
    manifest = json.loads(manifest_path.read_text())
    assert manifest['collection'] == 'pitt-201'
    assert manifest['source']['input_mode'] == 'sample-cache-cumulative'
    assert manifest['validation']['status'] == 'passed'
    assert manifest['validation']['members_checked'] == 392
    assert [r['country'] for r in manifest['countries']] == list(COUNTRIES)
    target = site / 'docs/figures'
    target.mkdir(parents=True, exist_ok=True)
    for name, sha in manifest['assets'].items():
        source = manifest_path.parent / name
        assert digest(source) == sha, name
        if source.resolve() != (target/name).resolve():
            shutil.copyfile(source, target/name)
    if manifest_path.resolve() != (target/manifest_path.name).resolve():
        shutil.copyfile(manifest_path, target/manifest_path.name)
    boundary = Path(__file__).resolve().parents[1] / 'resources/cartography/country-boundaries-v1.json'
    assert digest(boundary) == manifest['source']['boundary_sha256']
    shutil.copyfile(boundary, site/'data/mellon-7.6-cache-map-boundaries.json')
    records = manifest['countries']
    assert len({r['radius_base'] for r in records}) == 1
    text = '''
## Pitt 201–203: cumulative sample-cache country close-ups

**Philippines (PHL), Australia (AUS), India (IND), Japan (JPN), China (CHN),
and South Korea (KOR)** use the original **cumulative sample cache,
January 9–July 9, 2026**. Each map combines **all sampled resolutions**:
2160, 1080, 720 and SD. The existing audit renderer assigns colors to each
of the **392 coalesced unique-BTIH members**: yellow/orange for 2160,
pink/purple for 1080, blue for 720 and green for SD, with member shades
within those families. The member-to-color assignments are recorded in the
[source accounting](figures/pitt-201-country-source-accounting.json).

These are raw cumulative-cache downloader weights, after BTIH coalescing and
IP geolocation. No GeoJSON reconstruction, publication threshold, product
rescaling, ITU scaling or missing-hour imputation is applied. Cumulative
weights and the weekly geographic totals above have different aggregation
grains and should not be substituted for one another. Neither counts viewers.

**Izzi and Cartofreako** draw every map through the existing
`a60-carto-geo --cumulative-maps … --country ISO3` mechanism. Country outlines
and city positions use registered Cahill–Keyes coordinates and fit the page
uniformly. Australia keeps the mainland and Tasmania together, with offshore
islands in insets. Vector lake holes and projection seams are retained. Circle area
represents downloader weight, with the same coefficient and 5% opacity across
all six countries. Location names retain the audit's centered, weight-sized
Apercu style at their mapped locations.

**Click any map to open its high-resolution image in a new tab.**
'''
    rows = []
    for record in records:
        combined = next(v for v in record['variants'] if v['group'] == 'combined')
        assert not any(record['excluded_unsupported_resolution'][r] for r in ('downloaders','uploaders'))
        assert len(combined['members']) == 392
        rows.append([COUNTRIES[record['country']], f"{combined['downloaders']:,}",
                     f"{combined['uploaders']:,}"])
    text += table(['Country', 'Cumulative-cache downloaders', 'Cumulative-cache uploaders'], rows)
    for record in records:
        country = COUNTRIES[record['country']]
        combined = next(v for v in record['variants'] if v['group'] == 'combined')
        assert combined['status'] == 'rendered'
        stem = Path(combined['file']).stem
        text += f'''\n### {country}\n
{{::nomarkdown}}
<figure class="analysis-figure country-cache-figure" data-country="{record['country']}">
<a href="figures/{stem}-4k.webp" target="_blank" rel="noopener">
<img src="figures/{stem}.webp" alt="{country}: Pitt 201–203 cumulative downloaders, all resolutions; opens high-resolution image in a new tab" loading="lazy" style="max-width:100%;height:auto">
</a>
<figcaption>{country}, January 9–July 9, 2026. All sampled resolutions; color per coalesced BTIH member.
<a href="figures/{stem}-4k.webp" target="_blank" rel="noopener">High-resolution image (3840-pixel long edge; new tab)</a> ·
<a href="figures/{stem}.svg">Vector SVG</a> ·
<a href="figures/{record['receipt_file']}">Accounting and layout receipt</a>.</figcaption>
</figure>
{{:/}}

<details markdown="1"><summary>{country}: top cumulative-cache locations</summary>
'''
        text += table(['Location', 'Downloader weight'],
                      [[html.escape(c['city'] or '(unnamed location)').replace('|','&#124;'), f"{c['downloaders']:,}"]
                       for c in combined['cities'][:10]])
        text += f"\nCountry-coded locations outside the vector boundary are retained: **{len(record['outside_boundary_coordinates'])} coordinate pairs**. Exact ISO3 codes determine membership.\n\n</details>\n"
    archive = manifest['source']['cache_archive']
    text += f'''
Source archive: `pitt-201.cache/cache.20260709.tar.xz`, SHA-256
`{archive['sha256']}`. The render manifest records all 416 cumulative input
files, torrent inventory hashes, geolocation database hash, native C++ source
and executable hashes, and pinned Izzi/Cartofreako revisions.

[Verified render manifest](figures/{manifest_path.name}) ·
[Country geometry and upstream hashes](../data/mellon-7.6-cache-map-boundaries.json) ·
[Native audit renderer](https://github.com/bdekoz/alpha60/blob/main/src/a60-carto-geo.cc) ·
[Reproduction instructions](https://github.com/bdekoz/alpha60/blob/main/docs/pages/swarm-cartography.md).
'''
    shutil.copyfile(Path(__file__), site/'resources'/Path(__file__).name)
    return text
