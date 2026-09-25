---
layout: default
title: "AAPI-Led"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Analysis of AAPI-Led peer-to-peer distribution"
---


{::nomarkdown}
<img src="resources/a60-logo-block-gray.simple.svg?sanitize=true" height="50" width="100">

<div style="height: 50px;">
</div>
{:/}


## About

These are results from sampling peer swarms associated with *media objects*
being *shared* on the internet. Here, *media objects* are instances of media
that represent a specific film, television series or episode, or recorded
event as a file or archive. *Sharing* means the BitTorrent peer-to-peer file
sharing protocol. This is part of the long-term [Alpha60](https://alpha60.co/)
project.

## AAPI-Led

Definition: Texts produced by US production companies (co-productions are acceptable as long as one major partner is a US company) that feature AAPI characters, actors, creators, and/or storylines. A text does not need all four (AAPI characters, actors, creators, and/or storylines) to qualify.

Edge cases to consider: Bojack Horseman - major AAPI character but no other meaningful AAPI involvement; it is VERY difficult, instinctively, to call Bojack Horsemen an AAPI-led text. And so while a text doesn’t need to meet all four AAPI criteria, it likely has to meet more than one… 

This excludes: texts that are not produced by US production companies (regardless of AAPI involvement otherwise); texts that exclusively feature non-US Asian characters, actors, creators, and/or storylines (e.g. a Chinese-British actor would not be counted). 


Sample dates: 2018 to 2026

<div style="height: 50px;"></div>
{% include aapi-media-objects-list.html %}
<div style="height: 50px;"></div>


## Results, Commentary
- [AAPI-Led](docs/aapi.html)
- [AAPI and Asian-global: matched geographic comparisons](docs/asia-asian-where.html)
- [The Pitt versus The Bear: India, Philippines and Australia](docs/pitt-bear-compare.html)
- [Godzilla and Monarch: Japan, USA, China and South Korea](docs/godzilla.html)
- [Fail: meta-compare aapi-led vs. white-led](https://github.com/bdekoz/alpha60/blob/main/docs/development/20260916_swarm_analysis_mellon_7.1_hex_space_cardinality_results.md)

<div style="height: 50px;"></div>


## Data

### Forms

The files below are this group's published measurements. The itemized links
above open annual sample-cache audits, which may describe newer exports or
different observation windows. Check the sample dates when comparing sources.

Replace `<collection-key>` with a key from the group list above. Each form
links to an example from this group's `data/` directory.

- [Cumulative measurements (JSON)](data/3-body-problem-01-cumulative.json)
  - `<collection-key>-cumulative.json` — Collection totals and cumulative summaries.
- [Cumulative BTIH and media-object measurements (JSON)](data/3-body-problem-01-cumulative-btiha-media-objects.json)
  - `<collection-key>-cumulative-btiha-media-objects.json` — Torrent/media inventory and per-BTIH cumulative measurements.
- [Cumulative network classifications (JSON)](data/3-body-problem-01-cumulative-ip-swarm.json)
  - `<collection-key>-cumulative-ip-swarm.json` — IP-swarm and network summaries.
- [Weekly measurements (JSON)](data/3-body-problem-01-week.json)
  - `<collection-key>-week.json` — Weekly collection, BTIH, and country measurements.
- [Geographic observations (GeoJSON)](data/3-body-problem-01-cumulative.geojson)
  - `<collection-key>-cumulative.geojson` — Cumulative downloader and uploader geography.
- [Canonical media-object metadata (repository access required)](https://github.com/alpha60-devops/alpha60-swarm-metadata/tree/main/metadata)
  - `<collection-key>.json` — Descriptive source metadata.
- [JSON field documentation](docs/data-json.2026.html)

### [Source](https://github.com/alpha60-devops/alpha60-results-aapi-led/tree/main/data)


{::nomarkdown}
<svg width="100" height=100>
    <circle cx="20" cy="50" r="10" fill="black"/>
</svg>
{:/}
