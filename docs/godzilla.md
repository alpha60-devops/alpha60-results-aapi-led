---
layout: default
title: "Godzilla: Japan, USA, China and South Korea"
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

# Godzilla: Japan, USA, China and South Korea

## Summary and conclusions

- Minus One does **not** consistently have the highest Japanese downloader
  share: it has **1.37%**, compared with **1.13%** for The New Empire and
  **2.33%** for Vs. Kong. Japanese production alone does not explain these
  three observed distributions.
- Vs. Kong has a much higher USA downloader share: **20.09%**, versus
  **7.88%** for Minus One and **6.85%** for The New Empire. Excluding hosting
  leaves **17.92% / 4.89% / 4.27%**, respectively. Hosting changes the size
  of the gap but does not remove it. The 2021-versus-2024 comparison also
  spans different release conditions and collection histories.
- South Korea has the largest share among the four requested countries for
  the two 2024 objects: **8.03%** for Minus One and **7.10%** for The New
  Empire. Their Korean mobile rates are low (**1.85% / 2.41%**), compared
  with Japan (**25.88% / 26.20%**). Minus One’s narrow Korea-over-USA
  ordering reverses when flagged or gap-affected weeks are excluded. Country
  concentration and mobile network composition are different signals.

All three objects are films, but matching elapsed sampling weeks does not match
release timing, torrent inventories or network availability. These observations
support a descriptive franchise comparison, not a causal estimate of Japanese
versus U.S. production or a claim about viewers' nationality.

## Objects and observation windows

The requested contrast is the Japanese Toho film *Godzilla Minus One* versus the two U.S. MonsterVerse productions. These cases cannot isolate a production-country effect from release year, title, torrent inventory or distribution. “Korea” means South Korea (KOR); North Korea is not pooled into that result.

| Object / key | Full available sample | Analyzed weeks 2–11 | Worldwide downloader weight | Worldwide uploader weight |
| --- | --- | --- | --- | --- |
| Godzilla Minus One / `godzilla-minus-one` | 2024-05-02-to-2024-10-30 | 2024-05-09 to 2024-07-17-partial | 23,187,309 | 2,573,466 |
| Godzilla x Kong / `godzilla-x-kong-the-new-empire` | 2024-05-14-to-2024-11-11 | 2024-05-21 to 2024-07-29 | 33,002,925 | 5,303,249 |
| Godzilla vs. Kong / `godzilla-vs-kong` | 2021-03-31-to-2021-09-28 | 2021-04-07 to 2021-06-15 | 38,143,957 | 8,742,540 |


The Minus One audit reports 18 missing hours spanning July 10–11, within
the selected window. The New Empire audit reports no gaps.
The Vs. Kong audit identifies missing day July 21, outside the selected window;
that older audit does not establish complete hourly coverage.

### Coverage sensitivity

As a conservative check, exclude every elapsed-week index that has a `-partial` export flag or overlaps an audit-reported gap in **any** compared object, from **all** objects. Partial flags can reflect member-level coverage and are not an estimate of missing hours. Retained week indices: **3, 6, 7, 8, 9**. The table compares downloader world shares; it does not impute missing observations.

| Country | Object | Weeks 2–11 share | Retained-weeks share |
| --- | --- | --- | --- |
| Japan | Godzilla Minus One | 1.37% | 1.32% |
| Japan | Godzilla x Kong | 1.13% | 1.09% |
| Japan | Godzilla vs. Kong | 2.33% | 2.60% |
| USA | Godzilla Minus One | 7.88% | 7.73% |
| USA | Godzilla x Kong | 6.85% | 6.83% |
| USA | Godzilla vs. Kong | 20.09% | 21.92% |
| China | Godzilla Minus One | 4.65% | 4.31% |
| China | Godzilla x Kong | 3.98% | 3.79% |
| China | Godzilla vs. Kong | 5.41% | 5.54% |
| South Korea | Godzilla Minus One | 8.03% | 7.60% |
| South Korea | Godzilla x Kong | 7.10% | 6.81% |
| South Korea | Godzilla vs. Kong | 2.31% | 2.22% |

The ordering of the films is unchanged for Japan, USA and China. For South Korea, the narrow Minus One versus The New Empire gap remains positive, but the within-film comparison changes: Minus One’s USA share now exceeds its Korean share. Treat their near-tie as coverage-sensitive.

## Country distribution and network composition

Counts below are summed weekly swarm weights. Geographic shares use the worldwide role total; flag rates use the country role total.
### Downloaders

| Country | Object | Weight | World share | Mobile rate | Hosting rate | VPN rate | World share excluding hosting |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Japan | Godzilla Minus One | 318,039 | 1.37% | 25.88% | 13.84% | 8.50% | 1.40% |
| Japan | Godzilla x Kong | 371,834 | 1.13% | 26.20% | 12.90% | 7.46% | 1.14% |
| Japan | Godzilla vs. Kong | 888,529 | 2.33% | 12.53% | 7.81% | 1.09% | 2.40% |
| USA | Godzilla Minus One | 1,826,097 | 7.88% | 3.45% | 47.76% | 23.11% | 4.89% |
| USA | Godzilla x Kong | 2,261,447 | 6.85% | 6.36% | 46.09% | 20.02% | 4.27% |
| USA | Godzilla vs. Kong | 7,661,693 | 20.09% | 2.92% | 20.17% | 3.09% | 17.92% |
| China | Godzilla Minus One | 1,078,043 | 4.65% | 2.51% | 5.14% | 1.30% | 5.24% |
| China | Godzilla x Kong | 1,313,641 | 3.98% | 2.20% | 5.15% | 1.32% | 4.37% |
| China | Godzilla vs. Kong | 2,062,415 | 5.41% | 2.44% | 6.00% | 0.56% | 5.68% |
| South Korea | Godzilla Minus One | 1,861,431 | 8.03% | 1.85% | 2.94% | 1.25% | 9.25% |
| South Korea | Godzilla x Kong | 2,344,254 | 7.10% | 2.41% | 2.90% | 1.26% | 7.98% |
| South Korea | Godzilla vs. Kong | 879,219 | 2.31% | 6.23% | 4.66% | 0.54% | 2.46% |

### Uploaders

| Country | Object | Weight | World share | Mobile rate | Hosting rate | VPN rate | World share excluding hosting |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Japan | Godzilla Minus One | 14,670 | 0.57% | 25.18% | 36.50% | 26.62% | 0.45% |
| Japan | Godzilla x Kong | 13,629 | 0.26% | 27.60% | 32.61% | 18.71% | 0.20% |
| Japan | Godzilla vs. Kong | 33,277 | 0.38% | 19.89% | 16.28% | 7.03% | 0.34% |
| USA | Godzilla Minus One | 299,536 | 11.64% | 4.99% | 66.71% | 36.08% | 4.82% |
| USA | Godzilla x Kong | 412,300 | 7.77% | 8.70% | 61.62% | 26.07% | 3.41% |
| USA | Godzilla vs. Kong | 546,049 | 6.25% | 6.58% | 34.15% | 11.20% | 4.44% |
| China | Godzilla Minus One | 72,578 | 2.82% | 6.61% | 5.83% | 0.69% | 3.30% |
| China | Godzilla x Kong | 91,576 | 1.73% | 5.43% | 4.83% | 0.85% | 1.88% |
| China | Godzilla vs. Kong | 173,223 | 1.98% | 2.64% | 2.06% | 0.78% | 2.09% |
| South Korea | Godzilla Minus One | 15,806 | 0.61% | 5.88% | 5.31% | 2.73% | 0.72% |
| South Korea | Godzilla x Kong | 37,422 | 0.71% | 9.86% | 2.88% | 1.27% | 0.78% |
| South Korea | Godzilla vs. Kong | 205,037 | 2.35% | 5.84% | 1.50% | 0.65% | 2.49% |


## Hot and cold locations

Orange upward triangles favor the first named object; blue downward triangles favor the second. These are selected differences in **city share of the worldwide swarm**, rather than differences in raw title size. Hover or focus a triangle for its values; the following table provides the same evidence.

{::nomarkdown}
<figure class="analysis-figure">
{% include mellon-7.6-godzilla-map-1.svg %}
<figcaption>Selected shared city locations; weeks 2–11. Full counts and periods are in the calculation ledger. Land: Natural Earth via Cartofreako. <a href="../resources/mellon-7.6-godzilla-map-1.svg">Download SVG</a>.</figcaption>
<div class="map-tooltip" role="status" aria-live="polite" hidden></div>
</figure>
{:/}


| Country / city | Godzilla Minus One weight | Godzilla x Kong weight | First world share | Second world share | Difference (pp) |
| --- | --- | --- | --- | --- | --- |
| Japan / Tokyo | 90,261 | 105,401 | 0.389% | 0.319% | +0.070 |
| Japan / Kawasaki | 13,962 | 3,222 | 0.060% | 0.010% | +0.050 |
| Japan / Yokohama | 13,109 | 28,734 | 0.057% | 0.087% | -0.031 |
| Japan / Amagasaki | 409 | 1,284 | 0.002% | 0.004% | -0.002 |
| USA / Los Angeles | 98,895 | 113,932 | 0.427% | 0.345% | +0.081 |
| USA / New York City | 115,501 | 140,643 | 0.498% | 0.426% | +0.072 |
| USA / Newark | 17,585 | 31,634 | 0.076% | 0.096% | -0.020 |
| USA / Santa Clara | 7,204 | 15,670 | 0.031% | 0.047% | -0.016 |
| China / Shanghai | 185,246 | 230,019 | 0.799% | 0.697% | +0.102 |
| China / Xi’an | 48,498 | 44,056 | 0.209% | 0.133% | +0.076 |
| China / Xiuying | 288 | 2,510 | 0.001% | 0.008% | -0.006 |
| China / Nanshan | 21 | 136 | 0.000% | 0.000% | -0.000 |
| South Korea / Seoul | 724,870 | 921,235 | 3.126% | 2.791% | +0.335 |
| South Korea / Incheon | 167,097 | 208,892 | 0.721% | 0.633% | +0.088 |
| South Korea / Bucheon-si | 18,772 | 27,035 | 0.081% | 0.082% | -0.001 |
| South Korea / Dongmyeon | 44 | 79 | 0.000% | 0.000% | -0.000 |

Among the selected shared locations, Seoul has the largest positive difference (+0.335 pp) and Yokohama the smallest difference (-0.031 pp). These comparisons normalize by each object's worldwide swarm weight; they do not imply the same ordering of absolute counts.

{::nomarkdown}
<figure class="analysis-figure">
{% include mellon-7.6-godzilla-map-2.svg %}
<figcaption>Selected shared city locations; weeks 2–11. Full counts and periods are in the calculation ledger. Land: Natural Earth via Cartofreako. <a href="../resources/mellon-7.6-godzilla-map-2.svg">Download SVG</a>.</figcaption>
<div class="map-tooltip" role="status" aria-live="polite" hidden></div>
</figure>
{:/}


| Country / city | Godzilla Minus One weight | Godzilla vs. Kong weight | First world share | Second world share | Difference (pp) |
| --- | --- | --- | --- | --- | --- |
| Japan / Ōi | 10,178 | 2,858 | 0.044% | 0.007% | +0.036 |
| Japan / Kawasaki | 13,962 | 12,823 | 0.060% | 0.034% | +0.027 |
| Japan / Tokyo | 90,261 | 220,498 | 0.389% | 0.578% | -0.189 |
| Japan / Yokohama | 13,109 | 32,623 | 0.057% | 0.086% | -0.029 |
| USA / Miami | 51,096 | 52,584 | 0.220% | 0.138% | +0.083 |
| USA / Los Angeles | 98,895 | 139,229 | 0.427% | 0.365% | +0.061 |
| USA / Columbus | 27,598 | 588,551 | 0.119% | 1.543% | -1.424 |
| USA / Seattle | 45,673 | 388,725 | 0.197% | 1.019% | -0.822 |
| China / Qingdao | 113,974 | 69,146 | 0.492% | 0.181% | +0.310 |
| China / Nanjing | 139,679 | 115,957 | 0.602% | 0.304% | +0.298 |
| China / Shenzhen | 74,517 | 233,030 | 0.321% | 0.611% | -0.290 |
| China / Beijing | 70,627 | 225,065 | 0.305% | 0.590% | -0.285 |
| South Korea / Seoul | 724,870 | 452,261 | 3.126% | 1.186% | +1.940 |
| South Korea / Incheon | 167,097 | 74,559 | 0.721% | 0.195% | +0.525 |
| South Korea / Damyang | 65 | 487 | 0.000% | 0.001% | -0.001 |

Among the selected shared locations, Seoul has the largest positive difference (+1.940 pp) and Columbus the smallest difference (-1.424 pp). These comparisons normalize by each object's worldwide swarm weight; they do not imply the same ordering of absolute counts.

## Weekly behavior

Each line shows that week’s country share of worldwide downloader weight. All panels use the same vertical scale. Comparing shares separates geographic composition from changes in total observed swarm size.

{::nomarkdown}
<figure class="analysis-figure">
{% include mellon-7.6-godzilla-weekly.svg %}
<figcaption>Seven-day interval shares, elapsed weeks 2–11; calendar dates differ by object. Missing sampling hours remain unadjusted. <a href="../resources/mellon-7.6-godzilla-weekly.svg">Download SVG</a>.</figcaption>
<div class="map-tooltip" role="status" aria-live="polite" hidden></div>
</figure>
{:/}

Vs. Kong shows a pronounced USA change between weeks 4 and 5 (April 21–27 versus April 28–May 4, 2021): downloader weight rises from **224,155 to 1,210,927**, and world share from **7.54% to 24.41%**. Excluding hosting still leaves a rise from **5.81% to 22.33%**. The weekly aggregate does not establish whether this reflects torrent-inventory changes, collection behavior or demand; it should not be attributed to a release event or mobile adoption without further evidence.

- **Godzilla Minus One:** Japan peaks in week 6 (40,138); week 11 versus week 2 weight changes +5.6%, and mobile rate changes +0.99 pp; USA peaks in week 6 (222,765); week 11 versus week 2 weight changes -9.1%, and mobile rate changes -2.43 pp; China peaks in week 5 (133,547); week 11 versus week 2 weight changes -7.1%, and mobile rate changes -0.80 pp; South Korea peaks in week 6 (235,819); week 11 versus week 2 weight changes +40.9%, and mobile rate changes -0.46 pp.
- **Godzilla x Kong:** Japan peaks in week 11 (49,776); week 11 versus week 2 weight changes +11.1%, and mobile rate changes +0.90 pp; USA peaks in week 2 (289,250); week 11 versus week 2 weight changes -18.1%, and mobile rate changes -3.84 pp; China peaks in week 11 (184,307); week 11 versus week 2 weight changes +14.0%, and mobile rate changes -0.40 pp; South Korea peaks in week 11 (354,421); week 11 versus week 2 weight changes +31.7%, and mobile rate changes -1.37 pp.
- **Godzilla vs. Kong:** Japan peaks in week 7 (156,468); week 11 versus week 2 weight changes +198.8%, and mobile rate changes -2.97 pp; USA peaks in week 7 (1,270,827); week 11 versus week 2 weight changes +99.5%, and mobile rate changes -5.87 pp; China peaks in week 5 (324,717); week 11 versus week 2 weight changes -8.9%, and mobile rate changes -0.13 pp; South Korea peaks in week 2 (133,340); week 11 versus week 2 weight changes -48.4%, and mobile rate changes -4.14 pp.

These are descriptive peaks within the selected ten bins, not release-day peaks or evidence of a weekday effect. No daily or hourly behavioral claim is inferred from weekly data.

<details markdown="1"><summary>Weekly counts, mobile rates and calendar dates</summary>


| Object | Week / dates | World downloaders | Country | Country downloaders | World share | Mobile rate |
| --- | --- | --- | --- | --- | --- | --- |
| Godzilla Minus One | 2 / 2024-05-09-to-2024-05-15-partial | 2,282,575 | Japan | 25,913 | 1.14% | 25.30% |
| Godzilla Minus One | 2 / 2024-05-09-to-2024-05-15-partial | 2,282,575 | USA | 178,159 | 7.81% | 4.78% |
| Godzilla Minus One | 2 / 2024-05-09-to-2024-05-15-partial | 2,282,575 | China | 102,795 | 4.50% | 3.56% |
| Godzilla Minus One | 2 / 2024-05-09-to-2024-05-15-partial | 2,282,575 | South Korea | 124,807 | 5.47% | 2.19% |
| Godzilla Minus One | 3 / 2024-05-16-to-2024-05-22 | 2,319,683 | Japan | 31,830 | 1.37% | 25.60% |
| Godzilla Minus One | 3 / 2024-05-16-to-2024-05-22 | 2,319,683 | USA | 191,459 | 8.25% | 3.59% |
| Godzilla Minus One | 3 / 2024-05-16-to-2024-05-22 | 2,319,683 | China | 104,723 | 4.51% | 3.27% |
| Godzilla Minus One | 3 / 2024-05-16-to-2024-05-22 | 2,319,683 | South Korea | 171,401 | 7.39% | 1.89% |
| Godzilla Minus One | 4 / 2024-05-23-to-2024-05-29-partial | 2,324,450 | Japan | 37,623 | 1.62% | 26.24% |
| Godzilla Minus One | 4 / 2024-05-23-to-2024-05-29-partial | 2,324,450 | USA | 188,869 | 8.13% | 3.38% |
| Godzilla Minus One | 4 / 2024-05-23-to-2024-05-29-partial | 2,324,450 | China | 128,729 | 5.54% | 2.64% |
| Godzilla Minus One | 4 / 2024-05-23-to-2024-05-29-partial | 2,324,450 | South Korea | 223,969 | 9.64% | 1.85% |
| Godzilla Minus One | 5 / 2024-05-30-to-2024-06-05-partial | 2,615,417 | Japan | 38,045 | 1.45% | 26.00% |
| Godzilla Minus One | 5 / 2024-05-30-to-2024-06-05-partial | 2,615,417 | USA | 218,514 | 8.35% | 4.93% |
| Godzilla Minus One | 5 / 2024-05-30-to-2024-06-05-partial | 2,615,417 | China | 133,547 | 5.11% | 1.84% |
| Godzilla Minus One | 5 / 2024-05-30-to-2024-06-05-partial | 2,615,417 | South Korea | 231,057 | 8.83% | 1.84% |
| Godzilla Minus One | 6 / 2024-06-06-to-2024-06-12 | 2,689,284 | Japan | 40,138 | 1.49% | 26.13% |
| Godzilla Minus One | 6 / 2024-06-06-to-2024-06-12 | 2,689,284 | USA | 222,765 | 8.28% | 3.58% |
| Godzilla Minus One | 6 / 2024-06-06-to-2024-06-12 | 2,689,284 | China | 132,737 | 4.94% | 1.90% |
| Godzilla Minus One | 6 / 2024-06-06-to-2024-06-12 | 2,689,284 | South Korea | 235,819 | 8.77% | 1.85% |
| Godzilla Minus One | 7 / 2024-06-13-to-2024-06-19 | 2,424,787 | Japan | 30,029 | 1.24% | 26.09% |
| Godzilla Minus One | 7 / 2024-06-13-to-2024-06-19 | 2,424,787 | USA | 184,625 | 7.61% | 3.19% |
| Godzilla Minus One | 7 / 2024-06-13-to-2024-06-19 | 2,424,787 | China | 95,957 | 3.96% | 2.67% |
| Godzilla Minus One | 7 / 2024-06-13-to-2024-06-19 | 2,424,787 | South Korea | 172,040 | 7.10% | 1.86% |
| Godzilla Minus One | 8 / 2024-06-20-to-2024-06-26 | 2,183,356 | Japan | 22,310 | 1.02% | 24.80% |
| Godzilla Minus One | 8 / 2024-06-20-to-2024-06-26 | 2,183,356 | USA | 143,692 | 6.58% | 3.23% |
| Godzilla Minus One | 8 / 2024-06-20-to-2024-06-26 | 2,183,356 | China | 70,978 | 3.25% | 2.83% |
| Godzilla Minus One | 8 / 2024-06-20-to-2024-06-26 | 2,183,356 | South Korea | 122,589 | 5.61% | 1.78% |
| Godzilla Minus One | 9 / 2024-06-27-to-2024-07-03 | 2,176,024 | Japan | 31,609 | 1.45% | 25.96% |
| Godzilla Minus One | 9 / 2024-06-27-to-2024-07-03 | 2,176,024 | USA | 168,618 | 7.75% | 2.41% |
| Godzilla Minus One | 9 / 2024-06-27-to-2024-07-03 | 2,176,024 | China | 103,841 | 4.77% | 2.00% |
| Godzilla Minus One | 9 / 2024-06-27-to-2024-07-03 | 2,176,024 | South Korea | 194,893 | 8.96% | 1.81% |
| Godzilla Minus One | 10 / 2024-07-04-to-2024-07-10 | 2,020,393 | Japan | 33,169 | 1.64% | 25.92% |
| Godzilla Minus One | 10 / 2024-07-04-to-2024-07-10 | 2,020,393 | USA | 167,498 | 8.29% | 2.40% |
| Godzilla Minus One | 10 / 2024-07-04-to-2024-07-10 | 2,020,393 | China | 109,229 | 5.41% | 2.10% |
| Godzilla Minus One | 10 / 2024-07-04-to-2024-07-10 | 2,020,393 | South Korea | 209,021 | 10.35% | 1.80% |
| Godzilla Minus One | 11 / 2024-07-11-to-2024-07-17-partial | 2,151,340 | Japan | 27,373 | 1.27% | 26.29% |
| Godzilla Minus One | 11 / 2024-07-11-to-2024-07-17-partial | 2,151,340 | USA | 161,898 | 7.53% | 2.35% |
| Godzilla Minus One | 11 / 2024-07-11-to-2024-07-17-partial | 2,151,340 | China | 95,507 | 4.44% | 2.76% |
| Godzilla Minus One | 11 / 2024-07-11-to-2024-07-17-partial | 2,151,340 | South Korea | 175,835 | 8.17% | 1.73% |
| Godzilla x Kong | 2 / 2024-05-21-to-2024-05-27 | 4,289,660 | Japan | 44,805 | 1.04% | 26.15% |
| Godzilla x Kong | 2 / 2024-05-21-to-2024-05-27 | 4,289,660 | USA | 289,250 | 6.74% | 8.14% |
| Godzilla x Kong | 2 / 2024-05-21-to-2024-05-27 | 4,289,660 | China | 161,656 | 3.77% | 2.56% |
| Godzilla x Kong | 2 / 2024-05-21-to-2024-05-27 | 4,289,660 | South Korea | 269,091 | 6.27% | 3.19% |
| Godzilla x Kong | 3 / 2024-05-28-to-2024-06-03 | 3,948,582 | Japan | 45,340 | 1.15% | 26.47% |
| Godzilla x Kong | 3 / 2024-05-28-to-2024-06-03 | 3,948,582 | USA | 263,859 | 6.68% | 7.22% |
| Godzilla x Kong | 3 / 2024-05-28-to-2024-06-03 | 3,948,582 | China | 163,001 | 4.13% | 1.67% |
| Godzilla x Kong | 3 / 2024-05-28-to-2024-06-03 | 3,948,582 | South Korea | 282,287 | 7.15% | 2.48% |
| Godzilla x Kong | 4 / 2024-06-04-to-2024-06-10 | 3,665,641 | Japan | 45,291 | 1.24% | 26.22% |
| Godzilla x Kong | 4 / 2024-06-04-to-2024-06-10 | 3,665,641 | USA | 260,624 | 7.11% | 7.17% |
| Godzilla x Kong | 4 / 2024-06-04-to-2024-06-10 | 3,665,641 | China | 161,179 | 4.40% | 1.69% |
| Godzilla x Kong | 4 / 2024-06-04-to-2024-06-10 | 3,665,641 | South Korea | 277,481 | 7.57% | 2.33% |
| Godzilla x Kong | 5 / 2024-06-11-to-2024-06-17 | 3,383,188 | Japan | 30,944 | 0.91% | 26.36% |
| Godzilla x Kong | 5 / 2024-06-11-to-2024-06-17 | 3,383,188 | USA | 224,486 | 6.64% | 6.43% |
| Godzilla x Kong | 5 / 2024-06-11-to-2024-06-17 | 3,383,188 | China | 105,528 | 3.12% | 2.42% |
| Godzilla x Kong | 5 / 2024-06-11-to-2024-06-17 | 3,383,188 | South Korea | 179,676 | 5.31% | 3.05% |
| Godzilla x Kong | 6 / 2024-06-18-to-2024-06-24 | 3,134,906 | Japan | 28,356 | 0.90% | 25.92% |
| Godzilla x Kong | 6 / 2024-06-18-to-2024-06-24 | 3,134,906 | USA | 199,067 | 6.35% | 6.65% |
| Godzilla x Kong | 6 / 2024-06-18-to-2024-06-24 | 3,134,906 | China | 93,427 | 2.98% | 2.42% |
| Godzilla x Kong | 6 / 2024-06-18-to-2024-06-24 | 3,134,906 | South Korea | 167,711 | 5.35% | 2.79% |
| Godzilla x Kong | 7 / 2024-06-25-to-2024-07-01 | 2,996,099 | Japan | 28,343 | 0.95% | 25.30% |
| Godzilla x Kong | 7 / 2024-06-25-to-2024-07-01 | 2,996,099 | USA | 194,029 | 6.48% | 6.49% |
| Godzilla x Kong | 7 / 2024-06-25-to-2024-07-01 | 2,996,099 | China | 96,180 | 3.21% | 2.32% |
| Godzilla x Kong | 7 / 2024-06-25-to-2024-07-01 | 2,996,099 | South Korea | 169,698 | 5.66% | 2.45% |
| Godzilla x Kong | 8 / 2024-07-02-to-2024-07-08 | 2,987,428 | Japan | 38,025 | 1.27% | 25.60% |
| Godzilla x Kong | 8 / 2024-07-02-to-2024-07-08 | 2,987,428 | USA | 227,314 | 7.61% | 5.56% |
| Godzilla x Kong | 8 / 2024-07-02-to-2024-07-08 | 2,987,428 | China | 133,549 | 4.47% | 2.04% |
| Godzilla x Kong | 8 / 2024-07-02-to-2024-07-08 | 2,987,428 | South Korea | 242,775 | 8.13% | 2.23% |
| Godzilla x Kong | 9 / 2024-07-09-to-2024-07-15 | 3,055,307 | Japan | 36,475 | 1.19% | 26.13% |
| Godzilla x Kong | 9 / 2024-07-09-to-2024-07-15 | 3,055,307 | USA | 216,101 | 7.07% | 5.65% |
| Godzilla x Kong | 9 / 2024-07-09-to-2024-07-15 | 3,055,307 | China | 125,317 | 4.10% | 2.51% |
| Godzilla x Kong | 9 / 2024-07-09-to-2024-07-15 | 3,055,307 | South Korea | 235,922 | 7.72% | 2.10% |
| Godzilla x Kong | 10 / 2024-07-16-to-2024-07-22-partial | 2,166,099 | Japan | 24,479 | 1.13% | 26.14% |
| Godzilla x Kong | 10 / 2024-07-16-to-2024-07-22-partial | 2,166,099 | USA | 149,861 | 6.92% | 4.80% |
| Godzilla x Kong | 10 / 2024-07-16-to-2024-07-22-partial | 2,166,099 | China | 89,497 | 4.13% | 2.75% |
| Godzilla x Kong | 10 / 2024-07-16-to-2024-07-22-partial | 2,166,099 | South Korea | 165,192 | 7.63% | 2.05% |
| Godzilla x Kong | 11 / 2024-07-23-to-2024-07-29 | 3,376,015 | Japan | 49,776 | 1.47% | 27.05% |
| Godzilla x Kong | 11 / 2024-07-23-to-2024-07-29 | 3,376,015 | USA | 236,856 | 7.02% | 4.31% |
| Godzilla x Kong | 11 / 2024-07-23-to-2024-07-29 | 3,376,015 | China | 184,307 | 5.46% | 2.16% |
| Godzilla x Kong | 11 / 2024-07-23-to-2024-07-29 | 3,376,015 | South Korea | 354,421 | 10.50% | 1.82% |
| Godzilla vs. Kong | 2 / 2021-04-07-to-2021-04-13 | 4,595,486 | Japan | 31,640 | 0.69% | 15.36% |
| Godzilla vs. Kong | 2 / 2021-04-07-to-2021-04-13 | 4,595,486 | USA | 385,660 | 8.39% | 8.01% |
| Godzilla vs. Kong | 2 / 2021-04-07-to-2021-04-13 | 4,595,486 | China | 204,451 | 4.45% | 2.43% |
| Godzilla vs. Kong | 2 / 2021-04-07-to-2021-04-13 | 4,595,486 | South Korea | 133,340 | 2.90% | 8.35% |
| Godzilla vs. Kong | 3 / 2021-04-14-to-2021-04-20 | 3,321,353 | Japan | 8,886 | 0.27% | 24.39% |
| Godzilla vs. Kong | 3 / 2021-04-14-to-2021-04-20 | 3,321,353 | USA | 180,970 | 5.45% | 13.27% |
| Godzilla vs. Kong | 3 / 2021-04-14-to-2021-04-20 | 3,321,353 | China | 111,155 | 3.35% | 2.75% |
| Godzilla vs. Kong | 3 / 2021-04-14-to-2021-04-20 | 3,321,353 | South Korea | 61,135 | 1.84% | 10.67% |
| Godzilla vs. Kong | 4 / 2021-04-21-to-2021-04-27 | 2,972,988 | Japan | 13,444 | 0.45% | 18.69% |
| Godzilla vs. Kong | 4 / 2021-04-21-to-2021-04-27 | 2,972,988 | USA | 224,155 | 7.54% | 9.46% |
| Godzilla vs. Kong | 4 / 2021-04-21-to-2021-04-27 | 2,972,988 | China | 83,705 | 2.82% | 2.55% |
| Godzilla vs. Kong | 4 / 2021-04-21-to-2021-04-27 | 2,972,988 | South Korea | 54,288 | 1.83% | 10.43% |
| Godzilla vs. Kong | 5 / 2021-04-28-to-2021-05-04 | 4,960,450 | Japan | 148,241 | 2.99% | 11.92% |
| Godzilla vs. Kong | 5 / 2021-04-28-to-2021-05-04 | 4,960,450 | USA | 1,210,927 | 24.41% | 2.29% |
| Godzilla vs. Kong | 5 / 2021-04-28-to-2021-05-04 | 4,960,450 | China | 324,717 | 6.55% | 2.40% |
| Godzilla vs. Kong | 5 / 2021-04-28-to-2021-05-04 | 4,960,450 | South Korea | 120,456 | 2.43% | 5.72% |
| Godzilla vs. Kong | 6 / 2021-05-05-to-2021-05-11 | 4,517,424 | Japan | 142,706 | 3.16% | 11.99% |
| Godzilla vs. Kong | 6 / 2021-05-05-to-2021-05-11 | 4,517,424 | USA | 1,167,825 | 25.85% | 2.01% |
| Godzilla vs. Kong | 6 / 2021-05-05-to-2021-05-11 | 4,517,424 | China | 279,464 | 6.19% | 2.45% |
| Godzilla vs. Kong | 6 / 2021-05-05-to-2021-05-11 | 4,517,424 | South Korea | 107,170 | 2.37% | 5.19% |
| Godzilla vs. Kong | 7 / 2021-05-12-to-2021-05-18 | 4,672,259 | Japan | 156,468 | 3.35% | 11.99% |
| Godzilla vs. Kong | 7 / 2021-05-12-to-2021-05-18 | 4,672,259 | USA | 1,270,827 | 27.20% | 1.94% |
| Godzilla vs. Kong | 7 / 2021-05-12-to-2021-05-18 | 4,672,259 | China | 295,237 | 6.32% | 2.41% |
| Godzilla vs. Kong | 7 / 2021-05-12-to-2021-05-18 | 4,672,259 | South Korea | 110,042 | 2.36% | 4.69% |
| Godzilla vs. Kong | 8 / 2021-05-19-to-2021-05-25 | 3,640,619 | Japan | 104,079 | 2.86% | 12.40% |
| Godzilla vs. Kong | 8 / 2021-05-19-to-2021-05-25 | 3,640,619 | USA | 867,659 | 23.83% | 2.20% |
| Godzilla vs. Kong | 8 / 2021-05-19-to-2021-05-25 | 3,640,619 | China | 207,620 | 5.70% | 2.54% |
| Godzilla vs. Kong | 8 / 2021-05-19-to-2021-05-25 | 3,640,619 | South Korea | 80,085 | 2.20% | 4.95% |
| Godzilla vs. Kong | 9 / 2021-05-26-to-2021-06-01 | 3,254,132 | Japan | 92,209 | 2.83% | 12.58% |
| Godzilla vs. Kong | 9 / 2021-05-26-to-2021-06-01 | 3,254,132 | USA | 766,433 | 23.55% | 2.44% |
| Godzilla vs. Kong | 9 / 2021-05-26-to-2021-06-01 | 3,254,132 | China | 182,502 | 5.61% | 2.42% |
| Godzilla vs. Kong | 9 / 2021-05-26-to-2021-06-01 | 3,254,132 | South Korea | 72,732 | 2.24% | 4.98% |
| Godzilla vs. Kong | 10 / 2021-06-02-to-2021-06-08 | 3,206,836 | Japan | 96,318 | 3.00% | 12.49% |
| Godzilla vs. Kong | 10 / 2021-06-02-to-2021-06-08 | 3,206,836 | USA | 817,874 | 25.50% | 2.14% |
| Godzilla vs. Kong | 10 / 2021-06-02-to-2021-06-08 | 3,206,836 | China | 187,371 | 5.84% | 2.39% |
| Godzilla vs. Kong | 10 / 2021-06-02-to-2021-06-08 | 3,206,836 | South Korea | 71,108 | 2.22% | 4.68% |
| Godzilla vs. Kong | 11 / 2021-06-09-to-2021-06-15 | 3,002,410 | Japan | 94,538 | 3.15% | 12.39% |
| Godzilla vs. Kong | 11 / 2021-06-09-to-2021-06-15 | 3,002,410 | USA | 769,363 | 25.62% | 2.14% |
| Godzilla vs. Kong | 11 / 2021-06-09-to-2021-06-15 | 3,002,410 | China | 186,193 | 6.20% | 2.30% |
| Godzilla vs. Kong | 11 / 2021-06-09-to-2021-06-15 | 3,002,410 | South Korea | 68,863 | 2.29% | 4.21% |


</details>

## Projection choices

1. **Equal Earth, centered at 180°E, cropped to 95°E–305°E and 8°S–76°N, puts East Asia and the USA on either side of the Pacific.** The city-difference maps use that geographic
   preclip and central-meridian variant with the spherical Equal Earth equations
   through PROJ. It is an area-preserving display, not a density normalization.
   Cartofreako documents Equal Earth as an **exploration-only comparison method**,
   outside its six production atlas families. This centered variant is not
   EPSG:8857 and is not presented as a new registered CRS.
2. **Cahill–Keyes**, for a complementary full-world view consistent with Alpha60's
   existing geography. Its 70–160°E northern and southern octants place most of
   South/East Asia and Australia together. A Pacific/USA comparison crosses
   octants; retain visible cuts and split paths correctly. Use the same data,
   colors and denominators when comparing layouts. This is a recommendation; the maps above use Equal Earth.

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
- **Difference maps:** geolocated city aggregates keyed by country and GeoNames ID, using
  source representative coordinates. Only shared identified cities with at least
  100 combined downloader weight qualify. Show at most two positive and two
  negative differences per country, ranked by percentage-point difference.
  An absent or suppressed location is not zero. Triangles indicate sign;
  color intensity encodes magnitude on a symmetric scale shared by all difference maps on this page.
  “Hot” and “cold” describe larger and smaller observed shares, without a test of
  statistical significance. They do not describe population-adjusted demand.
- **Export:** all selected files declare H3 resolution 5 and minimum swarm size 3.
  Geographic filtering and aggregation mean these denominators differ from
  companion JSON unique-BTIH totals. Do not interpret the discrepancy as a known
  missing-data percentage. Weekly JSON `collection_week` values are cumulative
  prefixes; the geographic interval series used here is a different product.


## References and reproduction

- [Calculation ledger: every interval, country, network field, city and source SHA-256](../data/mellon-7.6-analysis.json). All ten flags for both roles are retained.
- [Godzilla Minus One: godzilla-minus-one-cumulative.json](https://github.com/alpha60-devops/alpha60-results-2024/blob/92a3c99741588412cbc26644d1e3879b1d97740f/data/json/godzilla-minus-one-cumulative.json).
- [Godzilla Minus One: godzilla-minus-one-sample-cache-audit.md](https://github.com/alpha60-devops/alpha60-results-2024/blob/92a3c99741588412cbc26644d1e3879b1d97740f/docs/itemized/godzilla-minus-one-sample-cache-audit.md).
- [Godzilla Minus One: first analyzed weekly GeoJSON](https://github.com/alpha60-devops/alpha60-results-2024/blob/92a3c99741588412cbc26644d1e3879b1d97740f/data/geojson.week/godzilla-minus-one-week-00002.geojson.gz); matched and extended interval filenames and hashes are in the ledger. Companion export version `2026-08-05`; IP-geolocation version `6:1777968300`.
- [Godzilla x Kong: godzilla-x-kong-the-new-empire-cumulative.json](https://github.com/alpha60-devops/alpha60-results-2024/blob/92a3c99741588412cbc26644d1e3879b1d97740f/data/json/godzilla-x-kong-the-new-empire-cumulative.json).
- [Godzilla x Kong: godzilla-x-kong-the-new-empire-sample-cache-audit.md](https://github.com/alpha60-devops/alpha60-results-2024/blob/92a3c99741588412cbc26644d1e3879b1d97740f/docs/itemized/godzilla-x-kong-the-new-empire-sample-cache-audit.md).
- [Godzilla x Kong: first analyzed weekly GeoJSON](https://github.com/alpha60-devops/alpha60-results-2024/blob/92a3c99741588412cbc26644d1e3879b1d97740f/data/geojson.week/godzilla-x-kong-the-new-empire-week-00002.geojson.gz); matched and extended interval filenames and hashes are in the ledger. Companion export version `2026-08-05`; IP-geolocation version `6:1777968300`.
- [Godzilla vs. Kong: godzilla-vs-kong-cumulative.json](https://github.com/alpha60-devops/alpha60-results-2021/blob/95af5fee975b04b25bad7f03aa5e1d571a939437/data/json/godzilla-vs-kong-cumulative.json).
- [Godzilla vs. Kong: godzilla-vs-kong-sample-cache-audit.md](https://github.com/alpha60-devops/alpha60-results-2021/blob/95af5fee975b04b25bad7f03aa5e1d571a939437/docs/itemized/godzilla-vs-kong-sample-cache-audit.md).
- [Godzilla vs. Kong: first analyzed weekly GeoJSON](https://github.com/alpha60-devops/alpha60-results-2021/blob/95af5fee975b04b25bad7f03aa5e1d571a939437/data/geojson.week/godzilla-vs-kong-week-00002.geojson.gz); matched and extended interval filenames and hashes are in the ledger. Companion export version `2026-08-05`; IP-geolocation version `6:1777968300`.
- [Basemap source](https://github.com/bdekoz/cartofreako/blob/ec201801a0386fc681c7637e26a838117ecf23de/src.wasm/cartofreako-cahill-keyes-land-110m.geojson); SHA-256 `7e3775f54f715d69ea7ddf91c4e270d195473250543a7a3e60f45002fe34dffa`. Natural Earth data are public domain.
- [Download the analysis script](../resources/mellon-7.6-analyze.py) and [ITU configuration](../data/mellon-7.6-itu-2026.json). Run with `--source-root /path/to/checkouts --output /path/to/output --itu-config /path/to/mellon-7.6-itu-2026.json`, with the annual repositories checked out at the ledger commits. It emits JSON only. Then run the [extension script](../resources/mellon-7.6-extend.py) in the same directory as the analysis script with `--source-root /path/to/checkouts --ledger /path/to/output/analysis.json` to add extended intervals and by-BTIH resolution weights. [Figure and validation scripts (repository access required)](https://github.com/bdekoz/alpha60/tree/main/scripts): `render-mellon-7-6-aapi.py` and `check-mellon-7-6-aapi.py`.
- [Toho's official Minus One announcement](https://godzilla.com/blogs/news/new-godzilla-minus-one-trailer-movie-tickets): identifies the film and director Takashi Yamazaki.
- [Legendary: Godzilla vs. Kong](https://www.legendary.com/film/godzilla-vs-kong/) and [Godzilla x Kong: The New Empire](https://www.legendary.com/film/godzilla-x-kong-the-new-empire/): official film records and Warner Bros. distribution credits.
- [Legendary and Warner Bros. franchise announcement](https://www.legendary.com/legendary-and-warner-bros-pictures-announce-cinematic-franchise-uniting-godzilla-king-kong-and-other-iconic-giant-monsters/): describes Legendary's Godzilla/Kong films and collaboration with Toho. The requested production contrast does not imply that the U.S. films have no Toho involvement.
