---
layout: default
title: "Asian-global and U.S. context: three geographic pilot cases"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "American Born Chinese, Shogun and No More Bets: geography and network attributes"
---

{::nomarkdown}
<img src="../resources/a60-logo-block-gray.simple.svg?sanitize=true" height="50" width="100" alt="Alpha60">
<div style="height: 50px;"></div>
<link rel="stylesheet" href="../resources/izzi-table-wcag-22.css">
<link rel="stylesheet" href="../resources/mellon-7.6-analysis.css">
<script defer src="../resources/mellon-7.6-analysis.js"></script>
{:/}

[AAPI-Led results](../index.html)

# Asian-global and U.S. context: three geographic pilot cases

## Summary

American Born Chinese has a higher USA downloader share than Shogun (17.85%
versus 7.03%), but most of that gap disappears when hosting is excluded
(4.93% versus 4.32%). No More Bets supplies a non-USA-production case: its
USA share is 4.94% and Asia-27 share 24.83%, with 88.82% of its uploader
weight located in Asia-27. The third object has a longer sampling window and
a newer geolocation pipeline. These selected cases describe observed network
geography; they do not establish that production or citizenship predicts audience location.

## Definition and current scope

The proxy is **USA production AND at least two counted U.S. citizens** among
qualifying contributors in `asian-led-global`. Under the reviewed Round 3
rules, American Born Chinese has three counted citizens (YES), Shogun one
(NO), and No More Bets zero plus non-USA production (NO). The current
confirmed cohort is 82 YES / 230 NO, with 26 unresolved candidates separate.
This page is a three-object pilot, not the proposed full-cohort study.

Both original objects also qualify for the broader metadata `aapi-led` slice
and appear in this site's editorial roster. No More Bets qualifies for that
broader metadata slice but is absent from the 47-object editorial roster.
The metadata composition, production/citizenship proxy and editorial roster
are distinct definitions. This analysis does not change the site's roster.

The original pair each spans 105 days / 15 weeks: American Born Chinese
2023-05-24–2023-09-05 (194 BTIHs), Shogun 2024-02-28–2024-06-11 (297).
Both original exports use data version `2025-09-22` and IP-geolocation
version `3:1756800417`. The No More Bets section gives its longer window.

### Geographic boundary

Asia-27 is the project's explicitly approved set, not a general continental
classification: `AFG BGD BRN BTN CHN HKG IDN IND IRN JPN KHM KOR LAO LKA
MAC MDV MMR MNG MYS NPL PAK PHL PRK SGP THA TLS VNM`.
It includes Iran and excludes Taiwan. The exact list controls all totals.

### Sources and calculation

The analysis sums every numeric member of the JSON-encoded
`Feature.properties.downloaders` and `Feature.properties.uploaders` objects
for the worldwide total and two non-overlapping regional subsets:
`country_code == USA` and the 27-code Asia set. Both regional subsets are
contained in the worldwide total. A regional percentage uses the worldwide
sum of the same role and field as its denominator. The attribute fields are
overlapping flags and must not be added together.

- [`american-born-chinese-01-cumulative.geojson`](https://raw.githubusercontent.com/alpha60-devops/alpha60-results-aapi-led/4039b679088456c4b3068f99d9e9314fb9894167/data/american-born-chinese-01-cumulative.geojson), SHA-256 `03716bb1fcd74edaad89dc51d1b9d51f8dcdf96ce38519c7a042d85d0d495ac1`
- [`shogun-2024-101-cumulative.geojson`](https://raw.githubusercontent.com/alpha60-devops/alpha60-results-aapi-led/4039b679088456c4b3068f99d9e9314fb9894167/data/shogun-2024-101-cumulative.geojson), SHA-256 `c4226bf5037d49632cf983ae70ccc92a5c9550ea3ff9df41b6f10a526a16b148`
- Asia boundary SHA-256: `b74adb818a1b41dedf9012b51ff7a8e687f62d139bdeee252948e59c28039b9c`

The source labels these records `downloaders` and `uploaders`, but the counts
should be interpreted as geolocated swarm observations, not verified people.
VPN, relay, proxy, hosting, and service locations may describe network egress
or infrastructure rather than a user's residence.

### Q1: Does the `aapi_yes` object have more downloaders in the USA?

It depends on whether “more” means an absolute count or a geographic share.

- **Absolute count: no.** `american-born-chinese-01` has 342,468 USA
  downloader observations, while `shogun-2024-101` has 1,762,992, or 5.15
  times as many. The latter is a much larger swarm overall.
- **Share of each object's worldwide GeoJSON count: yes.** USA observations
  are 17.85% of `american-born-chinese-01` downloaders versus 7.03% for
  `shogun-2024-101`, a difference of 10.82 percentage points.

The share difference is strongly affected by hosting infrastructure.
`hosting` accounts for 276,796 of the USA downloader observations for
`american-born-chinese-01` and 821,855 for `shogun-2024-101`. In a
hosting-excluded sensitivity calculation (`size - hosting`), the USA shares
are 4.93% and 4.32%, respectively: the direction remains the same, but the gap
shrinks from 10.82 to 0.61 percentage points.

### Q2: Does the `aapi_no` object have more downloaders in Asia-27?

Using the unadjusted `size` field, **yes in both absolute and proportional
terms**:

- `shogun-2024-101`: 4,553,989 Asia-27 downloader observations, 18.17% of its
  worldwide GeoJSON count;
- `american-born-chinese-01`: 331,359 observations, 17.27%;
- difference: 13.74 times as many observations and a 0.90 percentage-point
  larger share for `shogun-2024-101`.

This result is not robust to the same hosting sensitivity check. After
subtracting `hosting` from `size`, the Asia-27 share is 19.78% for
`shogun-2024-101` and 22.58% for `american-born-chinese-01`, reversing the
proportional result. The raw `aapi_no` count remains much larger because its
worldwide swarm is much larger.

### Q3: Differences across all downloader fields

Each regional cell is `count (share of the worldwide count for that field)`.
Very small fields such as `tor`, `tor_exit_nodes`, and `proxy` have unstable
percentages and should be read with their counts.

| Downloader field | ABC world | ABC USA | ABC Asia-27 | Shogun world | Shogun USA | Shogun Asia-27 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `size` | 1,918,534 | 342,468 (17.85%) | 331,359 (17.27%) | 25,064,300 | 1,762,992 (7.03%) | 4,553,989 (18.17%) |
| `mobile` | 162,980 | 6,222 (3.82%) | 24,256 (14.88%) | 2,498,436 | 55,358 (2.22%) | 287,361 (11.50%) |
| `satellite` | 995 | 121 (12.16%) | 132 (13.27%) | 25,571 | 3,815 (14.92%) | 1,950 (7.63%) |
| `tor` | 1,075 | 100 (9.30%) | 0 (0.00%) | 1,675 | 117 (6.99%) | 2 (0.12%) |
| `tor_exit_nodes` | 1,580 | 198 (12.53%) | 0 (0.00%) | 2,720 | 236 (8.68%) | 1 (0.04%) |
| `vpn` | 158,151 | 46,873 (29.64%) | 10,711 (6.77%) | 1,782,472 | 464,221 (26.04%) | 125,354 (7.03%) |
| `relay` | 2,227 | 1,688 (75.80%) | 19 (0.85%) | 9,728 | 3,446 (35.42%) | 323 (3.32%) |
| `proxy` | 253 | 151 (59.68%) | 15 (5.93%) | 1,941 | 526 (27.10%) | 135 (6.96%) |
| `hosting` | 585,341 | 276,796 (47.29%) | 30,389 (5.19%) | 3,280,421 | 821,855 (25.05%) | 244,809 (7.46%) |
| `service` | 133,268 | 45,574 (34.20%) | 7,597 (5.70%) | 1,393,452 | 431,915 (31.00%) | 72,512 (5.20%) |

The USA share is higher for `american-born-chinese-01` in nine of ten
downloader fields; `satellite` is the exception. The largest gaps are in
`relay`, `proxy`, and `hosting`, which reinforces that the headline USA
concentration is substantially an infrastructure-location signal. The
Asia-27 share is higher for `shogun-2024-101` in seven of ten fields, but not
for `mobile`, `satellite`, or `service`.

### Q3: Differences across all uploader fields

| Uploader field | ABC world | ABC USA | ABC Asia-27 | Shogun world | Shogun USA | Shogun Asia-27 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `size` | 341,595 | 111,180 (32.55%) | 59,280 (17.35%) | 3,996,540 | 433,037 (10.84%) | 595,516 (14.90%) |
| `mobile` | 24,742 | 1,032 (4.17%) | 5,553 (22.44%) | 689,728 | 17,332 (2.51%) | 100,059 (14.51%) |
| `satellite` | 185 | 28 (15.14%) | 14 (7.57%) | 11,236 | 1,270 (11.30%) | 877 (7.81%) |
| `tor` | 43 | 6 (13.95%) | 0 (0.00%) | 250 | 7 (2.80%) | 1 (0.40%) |
| `tor_exit_nodes` | 53 | 6 (11.32%) | 0 (0.00%) | 461 | 12 (2.60%) | 0 (0.00%) |
| `vpn` | 32,358 | 10,326 (31.91%) | 2,276 (7.03%) | 558,098 | 168,311 (30.16%) | 28,534 (5.11%) |
| `relay` | 564 | 402 (71.28%) | 1 (0.18%) | 3,344 | 880 (26.32%) | 39 (1.17%) |
| `proxy` | 43 | 34 (79.07%) | 1 (2.33%) | 442 | 97 (21.95%) | 41 (9.28%) |
| `hosting` | 201,294 | 102,178 (50.76%) | 6,522 (3.24%) | 913,621 | 321,096 (35.15%) | 48,304 (5.29%) |
| `service` | 29,445 | 10,140 (34.44%) | 1,801 (6.12%) | 515,532 | 160,447 (31.12%) | 24,452 (4.74%) |

The USA share is higher for `american-born-chinese-01` in every uploader
field. Its uploader distribution is especially concentrated in USA
infrastructure: 50.76% of worldwide `hosting`, 71.28% of `relay`, and 79.07%
of `proxy` observations are geolocated to the USA. Asia-27 does not show one
consistent uploader pattern: `american-born-chinese-01` has the higher
`size`, `mobile`, `vpn`, and `service` shares; `shogun-2024-101` has the higher
`satellite`, `tor`, `relay`, `proxy`, and `hosting` shares; `tor_exit_nodes`
is zero in Asia-27 for both.

### Country-level shape

The leading countries show that the regional result is not simply a USA-versus-
Asia split:

| Role and object | Five largest country totals (% of world) | Top-five share |
| --- | --- | ---: |
| Downloaders, `american-born-chinese-01` | USA 17.85%; RUS 17.24%; CHN 6.22%; KOR 4.44%; NLD 3.39% | 49.14% |
| Downloaders, `shogun-2024-101` | RUS 20.18%; KOR 7.53%; USA 7.03%; CHN 4.65%; BRA 4.62% | 44.02% |
| Uploaders, `american-born-chinese-01` | USA 32.55%; IRL 11.46%; CHN 8.49%; DEU 7.77%; CAN 3.74% | 64.00% |
| Uploaders, `shogun-2024-101` | USA 10.84%; ESP 4.45%; RUS 4.40%; GBR 4.34%; BRA 3.86% | 27.88% |

`american-born-chinese-01` is markedly more concentrated, especially for
uploaders. `shogun-2024-101` is much larger and more geographically diffuse;
Russia, Korea, and the USA lead its downloader distribution. The USA and
Ireland prominence in the smaller object's uploader and infrastructure fields
is another reason not to interpret IP geolocation directly as audience
residence.

## Preliminary conclusion

This pair provides directional but mixed evidence:

- The `aapi_yes` object has a much higher **USA share**, but not a higher raw
  USA count. Most of the apparent share gap disappears when hosting
  observations are excluded.
- The `aapi_no` object has a slightly higher unadjusted **Asia-27 downloader
  share** and a much higher raw count. The share result reverses after
  excluding hosting.
- Network-type composition, especially hosting, relay, proxy, and service
  traffic, materially changes the geographic interpretation. The observed
  pattern cannot yet support a claim that M1 classification predicts audience
  location.

## Suggested next methods

1. **Run the current Round 3 82-versus-230 comparison at fixed checkpoints.**
   Pin the canonical v3 report and its artifact digest in the development analysis; derive
   the YES/NO cohorts from confirmed `asian-led-global` objects using USA
   production and at least two counted citizens. Use weeks 1, 5, 10, and 15.
   Audit data availability and comparable observation windows first, retain
   only objects observed at each checkpoint, and report the actual eligible
   count on each side. Keep the 26 unresolved candidates separate. Compare
   per-object regional shares rather than pooled raw counts. The original
   66/101 and Round 2 84/228 splits remain historical baselines. Include the
   prior 84/228 assignment as a citizenship-conflict sensitivity analysis.
2. **Separate residential-looking and infrastructure traffic.** Report the
   full result alongside at least `size - hosting`; then test stricter filters
   for hosting, service, VPN, relay, proxy, and Tor without double-subtracting
   overlapping flags.
3. **Match objects before comparison.** Match or stratify by release year,
   media type and scope, provider, weeks observed, BTIH count, and worldwide
   swarm size. Same-franchise or same-series episodes are especially useful
   controls when they occur on opposite sides of the M1 predicate.
4. **Treat the media object as the statistical unit.** Compare medians and
   distributions of USA and Asia-27 shares across objects; use an object-level
   permutation test or bootstrap interval rather than treating millions of
   repeated IP observations as independent people.
5. **Model the country composition directly.** A hierarchical binomial or
   multinomial model with object and country effects can estimate the
   `aapi_yes` association with USA and Asia-27 shares while controlling for
   year, scale, provider, media type, and network attributes.
6. **Audit denominator and deduplication semantics.** Reconcile cumulative
   GeoJSON `size` with the weekly unique-downloader/uploader totals, quantify
   the geographic threshold's omitted mass per object, and decide whether the
   research question concerns observations, distinct IP addresses, or another
   deduplicated unit.
7. **Keep the Asia definition pinned.** Use `asia-27` consistently and report
   China, Japan, Korea, and the remaining 24 codes (use South Korea for the highlighted Korea comparison) separately so a regional
   difference cannot be driven invisibly by one country.

The next defensible stage is therefore a fixed-week, per-object cohort analysis
with infrastructure sensitivity checks—not a pooled comparison of cumulative
raw totals.


## Third pilot object: No More Bets — 2026-09-23

### Selection and comparison scope

`no-more-bets` (ASIAN-105) supplies the requested **non-USA production with
reviewed non-U.S. qualifying contributors**. Canonical country-of-origin evidence
lists China and sets USA production to false. All six qualifying people—Ao Shen
(director/writer), Lay, Gina Gin, Yong Mei, Zhou Ye, and Eric Wang—have reviewed
CHN citizenship lists without USA. Their status is `not_us_under_list_rule`;
the qualifying-person U.S. count is zero, with six resolved non-U.S. and zero
unknown/conflicting statuses. This is a claim about the reviewed qualifying
people: the credit crosswalk still has three unresolved rows and one linked
person without slice evidence. It does not certify the entire cast and crew.

The object is confirmed in both `asian-led-global` and `aapi-led` and fails the
USA-production/two-citizen proxy on both conditions. It is absent from the
47-object published AAPI-Led editorial roster. The original two objects remain
in that roster; the third object broadens the production context of this pilot.

| Object | USA production | Current Asian-global citizen count | Proxy | Available cumulative window | Sample bins / BTIH inventory |
| --- | --- | ---: | --- | --- | --- |
| `american-born-chinese-01` | true | 3 | YES | 2023-05-24 to 2023-09-05; 105 days | 15 weeks / 194 BTIHs |
| `shogun-2024-101` | true | 1 | NO | 2024-02-28 to 2024-06-11; 105 days | 15 weeks / 297 BTIHs |
| `no-more-bets` | false | 0 | NO | 2023-09-19 to 2024-05-15; 240 days | 35 weekly bins / 20 registered, 18 unique BTIHs |

**These are descriptive comparisons of the available cumulative exports.**
No More Bets is a film with a longer observation window and a different export
and geolocation generation from the original pair. Shares normalize each
export's size, but do not remove differences in observation time, torrent
inventory, release conditions, media scope, or geolocation/classification.
A common first-15-week export under the same pipeline is needed for a matched
comparison. The source audit records no missing days but 25 missing hours in
two gaps; calendar coverage does not imply continuous hourly sampling.

### Inputs and denominator

Use the published aggregate GeoJSON, summing the same ten numeric downloader
and uploader fields as the original pilot. There are 11,604 actual features,
with H3 resolution 5 and a declared minimum swarm size of 3. The GeoJSON format
marker is `20260701`; this is not its sample date. The companion cumulative
JSON reports data version `2026-08-05` and IP-geolocation version
`6:1777968300`, versus `2025-09-22` / `3:1756800417` for the original pair.
The aggregate GeoJSON does not itself embed an IP-geolocation version.

The worldwide denominators below are **1,386,404 downloader and 60,242 uploader
observations in the aggregate GeoJSON**. They are not the companion JSON's
1,395,902 / 60,353 unique-BTIH totals or its 1,426,566 / 63,800 all-BTIH totals.
Do not mix those products, interpret their discrepancy as a known missing-data
rate, or add the by-BTIH GeoJSON to the aggregate. The by-BTIH feature sums also
differ, consistent with separate spatial filtering/aggregation; their exact
cause has not been reconciled in this bounded pilot. Unclassified country
features remain in worldwide totals. Attribute flags overlap and cannot be
summed to estimate a combined infrastructure population.

### Geographic comparison

| Object | USA downloaders: count (world share) | Asia-27 downloaders: count (world share) | USA uploader share | Asia-27 uploader share |
| --- | ---: | ---: | ---: | ---: |
| American Born Chinese | 342,468 (17.85%) | 331,359 (17.27%) | 32.55% | 17.35% |
| Shogun | 1,762,992 (7.03%) | 4,553,989 (18.17%) | 10.84% | 14.90% |
| No More Bets | 68,487 (4.94%) | 344,187 (24.83%) | 2.74% | 88.82% |

For this additional pair, American Born Chinese has more USA downloader
observations than No More Bets in both absolute count and share. No More Bets
has slightly more Asia-27 downloader observations than American Born Chinese
(344,187 versus 331,359) and a higher share (24.83% versus 17.27%). Its Asia-27
count remains much smaller than Shogun's. These counts span unequal windows.

The uploader distribution is more distinct: 53,505 of 60,242 No More Bets
uploader observations (88.82%) are in Asia-27. China contributes 48,269
(80.13% of the worldwide total). This is a distribution of observed uploader
locations, not a measure of the audience's citizenship or residence.

### All downloader and uploader fields

Each regional percentage uses the worldwide total of the same role and field.
Small fields are displayed with counts: for example, the 100% USA share of
uploader `tor_exit_nodes` represents just one observation.

#### Downloaders — No More Bets

| Field | World | USA | Asia-27 |
| --- | ---: | ---: | ---: |
| `size` | 1,386,404 | 68,487 (4.94%) | 344,187 (24.83%) |
| `mobile` | 58,502 | 1,143 (1.95%) | 15,684 (26.81%) |
| `satellite` | 210 | 41 (19.52%) | 8 (3.81%) |
| `tor` | 106 | 7 (6.60%) | 4 (3.77%) |
| `tor_exit_nodes` | 67 | 7 (10.45%) | 2 (2.99%) |
| `vpn` | 41,651 | 5,432 (13.04%) | 5,353 (12.85%) |
| `relay` | 808 | 232 (28.71%) | 392 (48.51%) |
| `proxy` | 651 | 48 (7.37%) | 95 (14.59%) |
| `hosting` | 122,455 | 19,948 (16.29%) | 14,054 (11.48%) |
| `service` | 23,626 | 5,187 (21.95%) | 2,509 (10.62%) |

#### Uploaders — No More Bets

| Field | World | USA | Asia-27 |
| --- | ---: | ---: | ---: |
| `size` | 60,242 | 1,649 (2.74%) | 53,505 (88.82%) |
| `mobile` | 2,537 | 16 (0.63%) | 2,039 (80.37%) |
| `satellite` | 25 | 2 (8.00%) | 1 (4.00%) |
| `tor` | 2 | 0 (0.00%) | 0 (0.00%) |
| `tor_exit_nodes` | 1 | 1 (100.00%) | 0 (0.00%) |
| `vpn` | 1,635 | 261 (15.96%) | 667 (40.80%) |
| `relay` | 180 | 29 (16.11%) | 126 (70.00%) |
| `proxy` | 38 | 2 (5.26%) | 9 (23.68%) |
| `hosting` | 3,881 | 1,311 (33.78%) | 1,094 (28.19%) |
| `service` | 1,222 | 270 (22.09%) | 302 (24.71%) |

### Hosting-excluded sensitivity and country pattern

Subtracting `hosting` from `size` in both numerator and denominator gives:

| Object | USA downloader share | Asia-27 downloader share |
| --- | ---: | ---: |
| American Born Chinese | 4.93% | 22.58% |
| Shogun | 4.32% | 19.78% |
| No More Bets | 3.84% | 26.12% |

No More Bets retains the lowest USA and highest Asia-27 downloader shares of
the three under this sensitivity check. Its uploader USA share falls to 0.60%
and Asia-27 share rises to 92.99%. This check excludes one flag only; the result
does not establish that the remaining observations are residential traffic.

Its top five downloader countries are Russia (21.78%), China (12.82%),
South Korea (7.99%), Brazil (5.12%), and USA (4.94%). Thus the largest single
country is outside the approved Asia-27 boundary, even though Asia-27's combined
share exceeds that of the other two objects. The top uploader countries are
China (80.13%), USA (2.74%), Malaysia (2.25%), Hong Kong (1.79%), and Taiwan
(1.33%). Role-specific distributions should remain separate.

### Interpretation and next comparison

The third object adds a non-USA-production case with resolved non-U.S.
qualifying-person evidence. Its available export shows lower USA shares and
higher Asia-27 shares than the original pair, including after the hosting
sensitivity adjustment. This strengthens the descriptive range of the pilot;
three selected objects with unequal windows and export generations still do
not establish a production/citizenship effect on audience geography.

For the proposed cohort study, split the NO group into at least non-USA
production and USA production below the two-citizen threshold. Retain unknown
production and unresolved/conflicting citizenship as separate coverage flags.
Then compare those groups at common checkpoints using the same export pipeline,
per-object shares, and the infrastructure sensitivity checks already proposed.

### Sources and reproduction

- [Aggregate GeoJSON, pinned 2023-results commit](https://github.com/alpha60-devops/alpha60-results-2023/blob/188eac9b11645cc48caa174c7785c554bf972402/data/geojson.cumulative/no-more-bets-cumulative-aggregate.geojson.gz).
  Compressed SHA-256: `d3022de84e6c422f78f0911938861f274a37532dcfd1a7768c090e28efc48ea7`;
  decompressed SHA-256: `e32686792fa3abde317182e43ee561887c293de298f44e108bb49f9f6bf0ea51`.
- [Companion cumulative JSON](https://github.com/alpha60-devops/alpha60-results-2023/blob/188eac9b11645cc48caa174c7785c554bf972402/data/json/no-more-bets-cumulative.json),
  [weekly inventory](https://github.com/alpha60-devops/alpha60-results-2023/blob/188eac9b11645cc48caa174c7785c554bf972402/data/json/no-more-bets-week.json), and
  [sample-cache audit](https://github.com/alpha60-devops/alpha60-results-2023/blob/188eac9b11645cc48caa174c7785c554bf972402/docs/itemized/no-more-bets-sample-cache-audit.md).
- [Canonical Round 3 report](https://github.com/alpha60-devops/alpha60-swarm-metadata/blob/e87eeb0c/reports/candidates/h15-v3.generated.json): ASIAN-105; artifact digest remains
  `2889dae91538c550e048db3c45977dc8f9182bb13c420a479069fe32bbff6c3c`.
- [Calculation ledger](../data/mellon-7.5-no-more-bets-calculations.json)
  records the source hashes, aggregate header, every regional field sum, and
  country totals. Reproduction uses the same field-sum and hosting-subtraction
  formulas defined above and the unchanged pinned Asia-27 country set.

## Citizenship revision and analysis history

The September 23 citizenship-list extension reduced American Born Chinese's
Asian-global count from four to three after a conflict involving Chin Han;
its YES assignment is unchanged. Shogun remains at one and NO. Only the two
Masters of the Air objects moved across the full-cohort threshold, changing
84/228 to 82/230. The pilot geography did not change. The full-cohort
geographic effect of those reassignments has not been measured.

The linked development analysis retains the dated Round 1–3 history and
the proposed cohort method. Canonical metadata references require repository
access; the geographic exports and calculation ledger are public.

- [Development analysis and dated revisions (repository access required)](https://github.com/bdekoz/alpha60/blob/64732d07a/docs/development/20260922_swarm_analysis_mellon_7.3_asian_v_aapi_where.md).
- [Pinned Asia-27 boundary (repository access required)](https://github.com/bdekoz/alpha60/blob/64732d07a/config/mellon-7/geographic-slices-v1.json); the full 27-code definition is reproduced above.
