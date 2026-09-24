---
layout: default
title: "The Pitt and The Bear: India, Philippines, Australia"
author: "Benjamin De Kosnik <bkoz@gnu.org>"
description: "Geographic and mobile-network comparison at matched sampling weeks"
---

{::nomarkdown}
<img src="../resources/a60-logo-block-gray.simple.svg?sanitize=true" height="50" width="100" alt="Alpha60">
<div style="height: 50px;"></div>
<link rel="stylesheet" href="../resources/izzi-table-wcag-22.css">
<link rel="stylesheet" href="../resources/mellon-7.6-analysis.css">
<script defer src="../resources/mellon-7.6-analysis.js"></script>
{:/}

[AAPI-Led results](../index.html)

# The Pitt and The Bear: India, Philippines, Australia

## Summary and conclusions

- Both Pitt episode groups have higher downloader shares than Bear S05 in all
  three countries over weeks 2–11. The largest gap is India's share for Pitt
  201–203: **0.62% versus 0.36%**, a 0.26 percentage-point difference.
  Pitt 213–215 is much closer to Bear in India: **0.38% versus 0.36%**.
- Australia's share is **1.39% / 1.54% / 1.26%** for Pitt 201–203,
  Pitt 213–215 and Bear. Hosting accounts for roughly 31–34% of each object's
  Australian downloader weight; excluding hosting reduces those world shares
  to **1.15% / 1.24% / 1.07%**, preserving their order.
- Mobile network rates are higher in India and the Philippines than Australia
  for all three objects. In the Philippines, the rates are **23.69% / 23.16% /
  19.98%**, respectively; in Australia they are **3.75% / 3.13% / 2.96%**.
  This is a network-classification comparison, not a measure of phone viewing.

The two Pitt groups differ enough that pooling them would hide useful variation.
The episode-versus-season scope and sampling gaps limit claims about the series
as a whole. Country shares, raw counts, uploader geography and network flags
are therefore reported separately below.

## Objects and observation windows

The available 2026 comparison uses two three-episode Pitt groups separately against Bear season 5. Episode groups and a whole-season torrent inventory have different scopes. These are object-specific comparisons, not a ranking of the two entire series. Earlier Bear seasons and the Bear special (`bear-00`) are outside this selection.

| Object / key | Full available sample | Analyzed weeks 2–11 | Worldwide downloader weight | Worldwide uploader weight |
| --- | --- | --- | --- | --- |
| The Pitt 201–203 / `pitt-201` | 2026-01-09-to-2026-07-09 | 2026-01-16 to 2026-03-26 | 32,283,556 | 1,811,934 |
| The Pitt 213–215 / `pitt-213` | 2026-04-03-to-2026-09-11 | 2026-04-10 to 2026-06-18 | 31,871,675 | 2,680,124 |
| The Bear S05 / `bear-05` | 2026-06-26-to-2026-09-11 | 2026-07-03 to 2026-09-10 | 36,932,145 | 2,057,365 |


Within the selected windows, the audits report one missing hour for Pitt
201–203 (February 8–9), seven missing hours for Pitt 213–215 (April 25–26
and June 2–3), and 29 missing hours including August 15 for Bear S05.
The pooled comparison is not adjusted for those missing observations.
All other gaps listed in the ledger fall outside these selected windows.

### Coverage sensitivity

As a conservative check, exclude every elapsed-week index that has a `-partial` export flag or overlaps an audit-reported gap in **any** compared object, from **all** objects. Partial flags can reflect member-level coverage and are not an estimate of missing hours. Retained week indices: **2, 3, 6, 7, 10, 11**. The table compares downloader world shares; it does not impute missing observations.

| Country | Object | Weeks 2–11 share | Retained-weeks share |
| --- | --- | --- | --- |
| India | The Pitt 201–203 | 0.62% | 0.64% |
| India | The Pitt 213–215 | 0.38% | 0.39% |
| India | The Bear S05 | 0.36% | 0.38% |
| Philippines | The Pitt 201–203 | 0.20% | 0.20% |
| Philippines | The Pitt 213–215 | 0.21% | 0.23% |
| Philippines | The Bear S05 | 0.16% | 0.17% |
| Australia | The Pitt 201–203 | 1.39% | 1.43% |
| Australia | The Pitt 213–215 | 1.54% | 1.61% |
| Australia | The Bear S05 | 1.26% | 1.33% |

The Pitt groups retain higher shares than Bear in all three countries, although the India difference for Pitt 213–215 remains small.

## Country distribution and network composition

Counts below are summed weekly swarm weights. Geographic shares use the worldwide role total; flag rates use the country role total.
### Downloaders

| Country | Object | Weight | World share | Mobile rate | Hosting rate | VPN rate | World share excluding hosting |
| --- | --- | --- | --- | --- | --- | --- | --- |
| India | The Pitt 201–203 | 200,770 | 0.62% | 18.54% | 3.26% | 0.68% | 0.72% |
| India | The Pitt 213–215 | 119,598 | 0.38% | 21.02% | 6.08% | 1.06% | 0.43% |
| India | The Bear S05 | 132,895 | 0.36% | 18.08% | 5.20% | 1.11% | 0.42% |
| Philippines | The Pitt 201–203 | 63,610 | 0.20% | 23.69% | 2.88% | 1.65% | 0.23% |
| Philippines | The Pitt 213–215 | 68,026 | 0.21% | 23.16% | 1.66% | 1.26% | 0.26% |
| Philippines | The Bear S05 | 60,239 | 0.16% | 19.98% | 1.18% | 1.01% | 0.20% |
| Australia | The Pitt 201–203 | 449,463 | 1.39% | 3.75% | 31.20% | 29.44% | 1.15% |
| Australia | The Pitt 213–215 | 489,779 | 1.54% | 3.13% | 33.87% | 31.39% | 1.24% |
| Australia | The Bear S05 | 464,145 | 1.26% | 2.96% | 31.34% | 27.59% | 1.07% |

### Uploaders

| Country | Object | Weight | World share | Mobile rate | Hosting rate | VPN rate | World share excluding hosting |
| --- | --- | --- | --- | --- | --- | --- | --- |
| India | The Pitt 201–203 | 19,364 | 1.07% | 22.87% | 4.14% | 0.41% | 1.61% |
| India | The Pitt 213–215 | 21,516 | 0.80% | 24.72% | 2.62% | 0.48% | 1.27% |
| India | The Bear S05 | 14,468 | 0.70% | 15.08% | 5.49% | 0.37% | 1.14% |
| Philippines | The Pitt 201–203 | 17,859 | 0.99% | 25.62% | 1.65% | 1.06% | 1.52% |
| Philippines | The Pitt 213–215 | 20,460 | 0.76% | 26.51% | 1.45% | 1.22% | 1.22% |
| Philippines | The Bear S05 | 9,345 | 0.45% | 18.38% | 1.09% | 1.03% | 0.77% |
| Australia | The Pitt 201–203 | 111,750 | 6.17% | 4.41% | 34.30% | 35.10% | 6.37% |
| Australia | The Pitt 213–215 | 150,698 | 5.62% | 3.48% | 36.22% | 36.45% | 5.80% |
| Australia | The Bear S05 | 94,621 | 4.60% | 2.71% | 36.37% | 36.73% | 5.01% |


## Hot and cold locations

Orange upward triangles favor the first named object; blue downward triangles favor the second. These are selected differences in **city share of the worldwide swarm**, rather than differences in raw title size. Hover or focus a triangle for its values; the following table provides the same evidence.

{::nomarkdown}
<figure class="analysis-figure">
{% include mellon-7.6-pitt-bear-compare-map-1.svg %}
<figcaption>Selected shared city locations; weeks 2–11. Full counts and periods are in the calculation ledger. Land: Natural Earth via Cartofreako. <a href="../resources/mellon-7.6-pitt-bear-compare-map-1.svg">Download SVG</a>.</figcaption>
<div class="map-tooltip" role="status" aria-live="polite" hidden></div>
</figure>
{:/}


| Country / city | The Pitt 201–203 weight | The Bear S05 weight | First world share | Second world share | Difference (pp) |
| --- | --- | --- | --- | --- | --- |
| India / Chennai | 14,761 | 8,476 | 0.046% | 0.023% | +0.023 |
| India / Agartala | 5,389 | 469 | 0.017% | 0.001% | +0.015 |
| India / Mumbai | 10,931 | 15,384 | 0.034% | 0.042% | -0.008 |
| India / Bāshettihalli | 873 | 1,454 | 0.003% | 0.004% | -0.001 |
| Philippines / Manila | 14,020 | 5,517 | 0.043% | 0.015% | +0.028 |
| Philippines / Cebu City | 5,266 | 4,268 | 0.016% | 0.012% | +0.005 |
| Philippines / Quezon City | 16,329 | 27,940 | 0.051% | 0.076% | -0.025 |
| Philippines / Binangonan | 143 | 703 | 0.000% | 0.002% | -0.001 |
| Australia / Sydney | 149,537 | 156,562 | 0.463% | 0.424% | +0.039 |
| Australia / Melbourne | 130,423 | 136,731 | 0.404% | 0.370% | +0.034 |
| Australia / Leeton | 37 | 379 | 0.000% | 0.001% | -0.001 |
| Australia / St Albans | 488 | 781 | 0.002% | 0.002% | -0.001 |

Among the selected shared locations, Sydney has the largest positive difference (+0.039 pp) and Quezon City the smallest difference (-0.025 pp). These comparisons normalize by each object's worldwide swarm weight; they do not imply the same ordering of absolute counts.

{::nomarkdown}
<figure class="analysis-figure">
{% include mellon-7.6-pitt-bear-compare-map-2.svg %}
<figcaption>Selected shared city locations; weeks 2–11. Full counts and periods are in the calculation ledger. Land: Natural Earth via Cartofreako. <a href="../resources/mellon-7.6-pitt-bear-compare-map-2.svg">Download SVG</a>.</figcaption>
<div class="map-tooltip" role="status" aria-live="polite" hidden></div>
</figure>
{:/}


| Country / city | The Pitt 213–215 weight | The Bear S05 weight | First world share | Second world share | Difference (pp) |
| --- | --- | --- | --- | --- | --- |
| India / Delhi | 13,931 | 11,774 | 0.044% | 0.032% | +0.012 |
| India / Chennai | 9,538 | 8,476 | 0.030% | 0.023% | +0.007 |
| India / Mumbai | 10,934 | 15,384 | 0.034% | 0.042% | -0.007 |
| India / Bengaluru | 11,660 | 15,607 | 0.037% | 0.042% | -0.006 |
| Philippines / Manila | 8,745 | 5,517 | 0.027% | 0.015% | +0.012 |
| Philippines / Imus | 1,921 | 543 | 0.006% | 0.001% | +0.005 |
| Philippines / Paranaque City | 341 | 1,209 | 0.001% | 0.003% | -0.002 |
| Philippines / Majayjay | 279 | 549 | 0.001% | 0.001% | -0.001 |
| Australia / Sydney | 159,441 | 156,562 | 0.500% | 0.424% | +0.076 |
| Australia / Melbourne | 141,823 | 136,731 | 0.445% | 0.370% | +0.075 |
| Australia / Leeton | 76 | 379 | 0.000% | 0.001% | -0.001 |
| Australia / Burwood | 6 | 232 | 0.000% | 0.001% | -0.001 |

Among the selected shared locations, Sydney has the largest positive difference (+0.076 pp) and Mumbai the smallest difference (-0.007 pp). These comparisons normalize by each object's worldwide swarm weight; they do not imply the same ordering of absolute counts.

## Weekly behavior

Each line shows that week’s country share of worldwide downloader weight. All panels use the same vertical scale. Comparing shares separates geographic composition from changes in total observed swarm size.

{::nomarkdown}
<figure class="analysis-figure">
{% include mellon-7.6-pitt-bear-compare-weekly.svg %}
<figcaption>Seven-day interval shares, elapsed weeks 2–11; calendar dates differ by object. Missing sampling hours remain unadjusted. <a href="../resources/mellon-7.6-pitt-bear-compare-weekly.svg">Download SVG</a>.</figcaption>
<div class="map-tooltip" role="status" aria-live="polite" hidden></div>
</figure>
{:/}

- **The Pitt 201–203:** India peaks in week 3 (25,987); week 11 versus week 2 weight changes +1.7%, and mobile rate changes -1.16 pp; Philippines peaks in week 11 (7,359); week 11 versus week 2 weight changes +20.9%, and mobile rate changes +3.50 pp; Australia peaks in week 3 (62,430); week 11 versus week 2 weight changes -18.8%, and mobile rate changes -1.13 pp.
- **The Pitt 213–215:** India peaks in week 3 (20,345); week 11 versus week 2 weight changes -15.9%, and mobile rate changes -3.26 pp; Philippines peaks in week 3 (13,090); week 11 versus week 2 weight changes -41.7%, and mobile rate changes -3.20 pp; Australia peaks in week 3 (85,333); week 11 versus week 2 weight changes -38.7%, and mobile rate changes -0.83 pp.
- **The Bear S05:** India peaks in week 2 (20,134); week 11 versus week 2 weight changes -32.6%, and mobile rate changes -4.69 pp; Philippines peaks in week 2 (8,516); week 11 versus week 2 weight changes -34.9%, and mobile rate changes +2.18 pp; Australia peaks in week 2 (78,258); week 11 versus week 2 weight changes -55.5%, and mobile rate changes +0.71 pp.

These are descriptive peaks within the selected ten bins, not release-day peaks or evidence of a weekday effect. No daily or hourly behavioral claim is inferred from weekly data.

<details markdown="1"><summary>Weekly counts, mobile rates and calendar dates</summary>


| Object | Week / dates | World downloaders | Country | Country downloaders | World share | Mobile rate |
| --- | --- | --- | --- | --- | --- | --- |
| The Pitt 201–203 | 2 / 2026-01-16-to-2026-01-22 | 2,412,424 | India | 19,124 | 0.79% | 20.19% |
| The Pitt 201–203 | 2 / 2026-01-16-to-2026-01-22 | 2,412,424 | Philippines | 6,087 | 0.25% | 22.67% |
| The Pitt 201–203 | 2 / 2026-01-16-to-2026-01-22 | 2,412,424 | Australia | 48,466 | 2.01% | 4.45% |
| The Pitt 201–203 | 3 / 2026-01-23-to-2026-01-29 | 3,433,688 | India | 25,987 | 0.76% | 19.36% |
| The Pitt 201–203 | 3 / 2026-01-23-to-2026-01-29 | 3,433,688 | Philippines | 7,264 | 0.21% | 22.40% |
| The Pitt 201–203 | 3 / 2026-01-23-to-2026-01-29 | 3,433,688 | Australia | 62,430 | 1.82% | 3.93% |
| The Pitt 201–203 | 4 / 2026-01-30-to-2026-02-05 | 3,431,648 | India | 21,828 | 0.64% | 19.68% |
| The Pitt 201–203 | 4 / 2026-01-30-to-2026-02-05 | 3,431,648 | Philippines | 6,301 | 0.18% | 23.36% |
| The Pitt 201–203 | 4 / 2026-01-30-to-2026-02-05 | 3,431,648 | Australia | 52,391 | 1.53% | 3.48% |
| The Pitt 201–203 | 5 / 2026-02-06-to-2026-02-12 | 3,449,955 | India | 20,562 | 0.60% | 18.07% |
| The Pitt 201–203 | 5 / 2026-02-06-to-2026-02-12 | 3,449,955 | Philippines | 5,320 | 0.15% | 21.33% |
| The Pitt 201–203 | 5 / 2026-02-06-to-2026-02-12 | 3,449,955 | Australia | 44,825 | 1.30% | 4.37% |
| The Pitt 201–203 | 6 / 2026-02-13-to-2026-02-19 | 3,695,468 | India | 21,767 | 0.59% | 17.76% |
| The Pitt 201–203 | 6 / 2026-02-13-to-2026-02-19 | 3,695,468 | Philippines | 5,684 | 0.15% | 23.33% |
| The Pitt 201–203 | 6 / 2026-02-13-to-2026-02-19 | 3,695,468 | Australia | 44,542 | 1.21% | 3.93% |
| The Pitt 201–203 | 7 / 2026-02-20-to-2026-02-26 | 3,412,460 | India | 17,217 | 0.50% | 16.81% |
| The Pitt 201–203 | 7 / 2026-02-20-to-2026-02-26 | 3,412,460 | Philippines | 5,884 | 0.17% | 21.96% |
| The Pitt 201–203 | 7 / 2026-02-20-to-2026-02-26 | 3,412,460 | Australia | 41,422 | 1.21% | 3.60% |
| The Pitt 201–203 | 8 / 2026-02-27-to-2026-03-05 | 3,075,151 | India | 15,845 | 0.52% | 18.40% |
| The Pitt 201–203 | 8 / 2026-02-27-to-2026-03-05 | 3,075,151 | Philippines | 5,837 | 0.19% | 23.47% |
| The Pitt 201–203 | 8 / 2026-02-27-to-2026-03-05 | 3,075,151 | Australia | 36,522 | 1.19% | 3.52% |
| The Pitt 201–203 | 9 / 2026-03-06-to-2026-03-12 | 3,059,240 | India | 19,532 | 0.64% | 17.36% |
| The Pitt 201–203 | 9 / 2026-03-06-to-2026-03-12 | 3,059,240 | Philippines | 6,804 | 0.22% | 24.18% |
| The Pitt 201–203 | 9 / 2026-03-06-to-2026-03-12 | 3,059,240 | Australia | 39,755 | 1.30% | 3.02% |
| The Pitt 201–203 | 10 / 2026-03-13-to-2026-03-19 | 3,087,203 | India | 19,456 | 0.63% | 18.22% |
| The Pitt 201–203 | 10 / 2026-03-13-to-2026-03-19 | 3,087,203 | Philippines | 7,070 | 0.23% | 26.85% |
| The Pitt 201–203 | 10 / 2026-03-13-to-2026-03-19 | 3,087,203 | Australia | 39,741 | 1.29% | 3.58% |
| The Pitt 201–203 | 11 / 2026-03-20-to-2026-03-26 | 3,226,319 | India | 19,452 | 0.60% | 19.03% |
| The Pitt 201–203 | 11 / 2026-03-20-to-2026-03-26 | 3,226,319 | Philippines | 7,359 | 0.23% | 26.17% |
| The Pitt 201–203 | 11 / 2026-03-20-to-2026-03-26 | 3,226,319 | Australia | 39,369 | 1.22% | 3.32% |
| The Pitt 213–215 | 2 / 2026-04-10-to-2026-04-16 | 2,203,483 | India | 12,262 | 0.56% | 21.47% |
| The Pitt 213–215 | 2 / 2026-04-10-to-2026-04-16 | 2,203,483 | Philippines | 8,607 | 0.39% | 24.00% |
| The Pitt 213–215 | 2 / 2026-04-10-to-2026-04-16 | 2,203,483 | Australia | 59,875 | 2.72% | 4.01% |
| The Pitt 213–215 | 3 / 2026-04-17-to-2026-04-23 | 3,448,677 | India | 20,345 | 0.59% | 26.11% |
| The Pitt 213–215 | 3 / 2026-04-17-to-2026-04-23 | 3,448,677 | Philippines | 13,090 | 0.38% | 22.29% |
| The Pitt 213–215 | 3 / 2026-04-17-to-2026-04-23 | 3,448,677 | Australia | 85,333 | 2.47% | 3.48% |
| The Pitt 213–215 | 4 / 2026-04-24-to-2026-04-30 | 3,095,165 | India | 13,200 | 0.43% | 23.62% |
| The Pitt 213–215 | 4 / 2026-04-24-to-2026-04-30 | 3,095,165 | Philippines | 7,723 | 0.25% | 24.82% |
| The Pitt 213–215 | 4 / 2026-04-24-to-2026-04-30 | 3,095,165 | Australia | 57,977 | 1.87% | 2.95% |
| The Pitt 213–215 | 5 / 2026-05-01-to-2026-05-07 | 3,141,187 | India | 11,809 | 0.38% | 21.50% |
| The Pitt 213–215 | 5 / 2026-05-01-to-2026-05-07 | 3,141,187 | Philippines | 6,714 | 0.21% | 26.06% |
| The Pitt 213–215 | 5 / 2026-05-01-to-2026-05-07 | 3,141,187 | Australia | 50,633 | 1.61% | 2.82% |
| The Pitt 213–215 | 6 / 2026-05-08-to-2026-05-14 | 3,107,995 | India | 11,010 | 0.35% | 19.63% |
| The Pitt 213–215 | 6 / 2026-05-08-to-2026-05-14 | 3,107,995 | Philippines | 5,990 | 0.19% | 22.60% |
| The Pitt 213–215 | 6 / 2026-05-08-to-2026-05-14 | 3,107,995 | Australia | 45,415 | 1.46% | 2.87% |
| The Pitt 213–215 | 7 / 2026-05-15-to-2026-05-21 | 3,562,348 | India | 11,928 | 0.33% | 20.82% |
| The Pitt 213–215 | 7 / 2026-05-15-to-2026-05-21 | 3,562,348 | Philippines | 6,012 | 0.17% | 22.31% |
| The Pitt 213–215 | 7 / 2026-05-15-to-2026-05-21 | 3,562,348 | Australia | 44,887 | 1.26% | 2.94% |
| The Pitt 213–215 | 8 / 2026-05-22-to-2026-05-28 | 3,449,035 | India | 10,771 | 0.31% | 17.96% |
| The Pitt 213–215 | 8 / 2026-05-22-to-2026-05-28 | 3,449,035 | Philippines | 5,688 | 0.16% | 22.56% |
| The Pitt 213–215 | 8 / 2026-05-22-to-2026-05-28 | 3,449,035 | Australia | 41,026 | 1.19% | 2.77% |
| The Pitt 213–215 | 9 / 2026-05-29-to-2026-06-04 | 3,375,947 | India | 9,980 | 0.30% | 15.55% |
| The Pitt 213–215 | 9 / 2026-05-29-to-2026-06-04 | 3,375,947 | Philippines | 5,155 | 0.15% | 22.93% |
| The Pitt 213–215 | 9 / 2026-05-29-to-2026-06-04 | 3,375,947 | Australia | 37,982 | 1.13% | 2.88% |
| The Pitt 213–215 | 10 / 2026-06-05-to-2026-06-11 | 2,901,241 | India | 7,977 | 0.27% | 19.07% |
| The Pitt 213–215 | 10 / 2026-06-05-to-2026-06-11 | 2,901,241 | Philippines | 4,028 | 0.14% | 22.27% |
| The Pitt 213–215 | 10 / 2026-06-05-to-2026-06-11 | 2,901,241 | Australia | 29,969 | 1.03% | 2.73% |
| The Pitt 213–215 | 11 / 2026-06-12-to-2026-06-18 | 3,586,597 | India | 10,316 | 0.29% | 18.21% |
| The Pitt 213–215 | 11 / 2026-06-12-to-2026-06-18 | 3,586,597 | Philippines | 5,019 | 0.14% | 20.80% |
| The Pitt 213–215 | 11 / 2026-06-12-to-2026-06-18 | 3,586,597 | Australia | 36,682 | 1.02% | 3.18% |
| The Bear S05 | 2 / 2026-07-03-to-2026-07-09 | 4,251,047 | India | 20,134 | 0.47% | 18.42% |
| The Bear S05 | 2 / 2026-07-03-to-2026-07-09 | 4,251,047 | Philippines | 8,516 | 0.20% | 20.30% |
| The Bear S05 | 2 / 2026-07-03-to-2026-07-09 | 4,251,047 | Australia | 78,258 | 1.84% | 2.89% |
| The Bear S05 | 3 / 2026-07-10-to-2026-07-16 | 4,183,977 | India | 15,964 | 0.38% | 18.89% |
| The Bear S05 | 3 / 2026-07-10-to-2026-07-16 | 4,183,977 | Philippines | 7,339 | 0.18% | 19.68% |
| The Bear S05 | 3 / 2026-07-10-to-2026-07-16 | 4,183,977 | Australia | 61,592 | 1.47% | 2.96% |
| The Bear S05 | 4 / 2026-07-17-to-2026-07-23 | 4,162,697 | India | 14,086 | 0.34% | 18.95% |
| The Bear S05 | 4 / 2026-07-17-to-2026-07-23 | 4,162,697 | Philippines | 6,477 | 0.16% | 21.75% |
| The Bear S05 | 4 / 2026-07-17-to-2026-07-23 | 4,162,697 | Australia | 53,721 | 1.29% | 2.99% |
| The Bear S05 | 5 / 2026-07-24-to-2026-07-30 | 4,100,179 | India | 13,150 | 0.32% | 17.98% |
| The Bear S05 | 5 / 2026-07-24-to-2026-07-30 | 4,100,179 | Philippines | 6,143 | 0.15% | 18.75% |
| The Bear S05 | 5 / 2026-07-24-to-2026-07-30 | 4,100,179 | Australia | 50,230 | 1.23% | 2.79% |
| The Bear S05 | 6 / 2026-07-31-to-2026-08-06 | 3,842,928 | India | 12,967 | 0.34% | 19.86% |
| The Bear S05 | 6 / 2026-07-31-to-2026-08-06 | 3,842,928 | Philippines | 5,939 | 0.15% | 18.39% |
| The Bear S05 | 6 / 2026-07-31-to-2026-08-06 | 3,842,928 | Australia | 45,634 | 1.19% | 2.90% |
| The Bear S05 | 7 / 2026-08-07-to-2026-08-13 | 3,719,071 | India | 12,511 | 0.34% | 18.17% |
| The Bear S05 | 7 / 2026-08-07-to-2026-08-13 | 3,719,071 | Philippines | 5,703 | 0.15% | 19.17% |
| The Bear S05 | 7 / 2026-08-07-to-2026-08-13 | 3,719,071 | Australia | 44,104 | 1.19% | 2.74% |
| The Bear S05 | 8 / 2026-08-14-to-2026-08-20-partial | 2,923,008 | India | 9,310 | 0.32% | 17.83% |
| The Bear S05 | 8 / 2026-08-14-to-2026-08-20-partial | 2,923,008 | Philippines | 4,504 | 0.15% | 17.50% |
| The Bear S05 | 8 / 2026-08-14-to-2026-08-20-partial | 2,923,008 | Australia | 30,460 | 1.04% | 2.92% |
| The Bear S05 | 9 / 2026-08-21-to-2026-08-27 | 3,422,039 | India | 10,931 | 0.32% | 18.79% |
| The Bear S05 | 9 / 2026-08-21-to-2026-08-27 | 3,422,039 | Philippines | 4,987 | 0.15% | 18.79% |
| The Bear S05 | 9 / 2026-08-21-to-2026-08-27 | 3,422,039 | Australia | 32,936 | 0.96% | 2.96% |
| The Bear S05 | 10 / 2026-08-28-to-2026-09-03 | 3,263,467 | India | 10,276 | 0.31% | 17.99% |
| The Bear S05 | 10 / 2026-08-28-to-2026-09-03 | 3,263,467 | Philippines | 5,090 | 0.16% | 22.53% |
| The Bear S05 | 10 / 2026-08-28-to-2026-09-03 | 3,263,467 | Australia | 32,367 | 0.99% | 3.00% |
| The Bear S05 | 11 / 2026-09-04-to-2026-09-10 | 3,063,732 | India | 13,566 | 0.44% | 13.73% |
| The Bear S05 | 11 / 2026-09-04-to-2026-09-10 | 3,063,732 | Philippines | 5,541 | 0.18% | 22.49% |
| The Bear S05 | 11 / 2026-09-04-to-2026-09-10 | 3,063,732 | Australia | 34,843 | 1.14% | 3.60% |


</details>

## Projection choices

1. **Equal Earth, centered at 120°E, cropped to 65–156°E and 46°S–39°N, keeps India, the Philippines and Australia together.** This page uses that geographic
   preclip and central-meridian variant with the spherical Equal Earth equations
   through PROJ. It is an area-preserving display, not a density normalization.
   Cartofreako documents Equal Earth as an **exploration-only comparison method**,
   outside its six production atlas families. This centered variant is not
   EPSG:8857 and is not presented as a new registered CRS.
2. **Cahill–Keyes**, for a complementary full-world view consistent with Alpha60's
   existing geography. Its 70–160°E northern and southern octants place most of
   South/East Asia and Australia together. A Pacific/USA comparison crosses
   octants; retain visible cuts and split paths correctly. Use the same data,
   colors and denominators when comparing layouts. This is a recommendation;
   the maps above use Equal Earth.

References: [Cartofreako Equal Earth context](https://bdekoz.github.io/cartofreako/docs/pages/projections/equal-earth/context.html),
[equations and implementation boundary](https://bdekoz.github.io/cartofreako/docs/pages/projections/equal-earth/implementation.html),
[Cahill–Keyes geometry and octants](https://bdekoz.github.io/cartofreako/docs/pages/projections/cahill-keyes/context.html).

## Methods and limits

- **Units:** sum `downloaders.size` or `uploaders.size` in the top-level
  `features` array of each weekly aggregate GeoJSON. Summing ten intervals
  produces repeated swarm weights across weeks and torrents, not unique people,
  unique addresses over the full window, or completed views. The nested
  `collection_week_by_btiha` is not added again.
- **Window:** weeks 2–11 inclusive, ten seven-day bins. Opening bins are excluded
  because they can be shorter; later incomplete trailing bins are also excluded.
  Some retained seven-day bins carry a `-partial` source flag; the coverage
  sensitivity excludes their elapsed-week indices from all compared objects.
  The compared calendar dates differ. Sample-cache gaps are disclosed above;
  matching elapsed weeks does not match release conditions or hourly coverage.
- **Shares:** country or city downloader weight divided by worldwide downloader
  weight over the same intervals, including unclassified-country features.
  Pooled shares use sums of counts, not the unweighted mean of weekly percentages.
  Uploader shares have a separate uploader denominator.
- **Flags:** mobile, hosting and VPN rates divide the country's flagged weight by
  that country's size for the same role. Flags overlap. A mobile flag describes
  IP network classification, not a device, connection technology, citizenship,
  residence or verified audience. Wi-Fi versus cellular usage is not resolved.
- **Hosting sensitivity:** subtract hosting from size in both country and global
  denominators. This removes one flag; it does not identify residential traffic.
- **Maps:** geolocated city aggregates keyed by country and GeoNames ID, using
  source representative coordinates. Only shared identified cities with at least
  100 combined downloader weight qualify. Show at most two positive and two
  negative differences per country, ranked by percentage-point difference.
  An absent or suppressed location is not zero. Triangles indicate sign;
  color intensity encodes magnitude on a symmetric scale shared by the two maps.
  “Hot” and “cold” describe larger and smaller observed shares, without a test of
  statistical significance. They do not describe population-adjusted demand.
- **Export:** all selected files declare H3 resolution 5 and minimum swarm size 3.
  Geographic filtering and aggregation mean these denominators differ from
  companion JSON unique-BTIH totals. Do not interpret the discrepancy as a known
  missing-data percentage. Weekly JSON `collection_week` values are cumulative
  prefixes; the geographic interval series used here is a different product.


## References and reproduction

- [Calculation ledger: every interval, country, network field, city and source SHA-256](../data/mellon-7.6-analysis.json). All ten flags for both roles are retained.
- [The Pitt 201–203: pitt-201-cumulative.json](https://github.com/alpha60-devops/alpha60-results-2026/blob/55986b899dad42e378dffedb0e13d2888358833f/data/json/pitt-201-cumulative.json).
- [The Pitt 201–203: pitt-201-sample-cache-audit.md](https://github.com/alpha60-devops/alpha60-results-2026/blob/55986b899dad42e378dffedb0e13d2888358833f/docs/itemized/pitt-201-sample-cache-audit.md).
- [The Pitt 201–203: weekly GeoJSON directory](https://github.com/alpha60-devops/alpha60-results-2026/tree/55986b899dad42e378dffedb0e13d2888358833f/data/geojson.week); exact ten filenames and hashes are in the ledger. Companion export version `2026-08-05`; IP-geolocation version `6:1777968300`.
- [The Pitt 213–215: pitt-213-cumulative.json](https://github.com/alpha60-devops/alpha60-results-2026/blob/55986b899dad42e378dffedb0e13d2888358833f/data/json/pitt-213-cumulative.json).
- [The Pitt 213–215: pitt-213-sample-cache-audit.md](https://github.com/alpha60-devops/alpha60-results-2026/blob/55986b899dad42e378dffedb0e13d2888358833f/docs/itemized/pitt-213-sample-cache-audit.md).
- [The Pitt 213–215: weekly GeoJSON directory](https://github.com/alpha60-devops/alpha60-results-2026/tree/55986b899dad42e378dffedb0e13d2888358833f/data/geojson.week); exact ten filenames and hashes are in the ledger. Companion export version `2026-08-05`; IP-geolocation version `6:1777968300`.
- [The Bear S05: bear-05-cumulative.json](https://github.com/alpha60-devops/alpha60-results-2026/blob/55986b899dad42e378dffedb0e13d2888358833f/data/json/bear-05-cumulative.json).
- [The Bear S05: bear-05-sample-cache-audit.md](https://github.com/alpha60-devops/alpha60-results-2026/blob/55986b899dad42e378dffedb0e13d2888358833f/docs/itemized/bear-05-sample-cache-audit.md).
- [The Bear S05: weekly GeoJSON directory](https://github.com/alpha60-devops/alpha60-results-2026/tree/55986b899dad42e378dffedb0e13d2888358833f/data/geojson.week); exact ten filenames and hashes are in the ledger. Companion export version `2026-08-05`; IP-geolocation version `6:1777968300`.
- [Basemap source](https://github.com/bdekoz/cartofreako/blob/ec201801a0386fc681c7637e26a838117ecf23de/src.wasm/cartofreako-cahill-keyes-land-110m.geojson); SHA-256 `7e3775f54f715d69ea7ddf91c4e270d195473250543a7a3e60f45002fe34dffa`. Natural Earth data are public domain.
- [Download the analysis script](../resources/mellon-7.6-analyze.py). Run with `--source-root /path/to/checkouts --output /path/to/output`, with the annual repositories checked out at the ledger commits. It emits JSON only. [Figure and validation scripts (repository access required)](https://github.com/bdekoz/alpha60/tree/main/scripts): `render-mellon-7-6-aapi.py` and `check-mellon-7-6-aapi.py`.
