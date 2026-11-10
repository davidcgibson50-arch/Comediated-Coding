# AIM-AI Analysis E6: Profiles, Departure Order and Networks on the Five AIM-AI v2 Dimensions

*Results note, November 10, 2026. A labelled reanalysis of data release 1 (October 30, 2026) for the findings article (v3). No new coding. Under AIM-AI v2, steering and provenance of production are two independent dimensions, so the five coded dimensions are the primary reading everywhere, and E5's "counted once" variants become a historical sensitivity check.*

## Reproduction first

Scripts were rebuilt in Python from data release 1 (AIM-AI_v081_all162_intended.csv; ENA-ready EOML file; C12 sweep log). Before any new value was computed, the following reproduced exactly:

- Five dimension distributions for the 139 learner episodes; 71 mixed profiles; 41 distinct profiles; 37 of 127 steering-provenance divergences, 30 with human steering and AI-supplied material.
- Departure order on five dimensions: Loevinger H = .82, Goodenough-Edwards reproducibility = .96 (NE treated as missing). Four-dimension check (E5, interaction structure departs if either component departs): H = .91, reproducibility .98.
- Pre-sweep mixed profiles: 78 of 139.
- Instructor-episode figures in draft v2: AI positioned as assistant 19 of 23 (83%), steering human-dominant 20 (87%), no co-mediated code, interpretation not evident 8 (35%).

Model 1 (Run 4.1, 15 nodes) and Model 2 (Run 5, adding EO and ML) were fitted with rENA 0.3.1 on the five coded dimensions and are archived; under v2 they need no refit. Their reported values stand: Model 1 variance 33.9% and 12.8%, fit .99 and .98, Kruskal-Wallis p = .726 and .615; Model 2 variance 27.0% and 10.7%.

Method note: Goodenough-Edwards reproducibility counts, for each episode, departures from the ideal pattern implied by its number of departed dimensions, over coded cells. A minimum-error variant gives .98; the article reports the Goodenough-Edwards value, which is the published one.

## 1. Profiles (Table 2 and Table 3 of the article)

| Dimension | AD | AS | CM | HD | NE | Departs (% of coded) |
|---|---|---|---|---|---|---|
| Engagement | 7 | 34 | 6 | 88 | 4 | 35 |
| Steering | 1 | 13 | 3 | 112 | 10 | 13 |
| Provenance of production | 11 | 27 | 2 | 97 | 2 | 29 |
| Interpretive influence | 1 | 17 | 2 | 89 | 30 | 18 |
| Positioning of AI | 2 | 67 | 5 | 22 | 43 | 77 |

- **71 of 139 learner designs (51%) are mixed**; 41 distinct profiles occur.
- Mixtures: AS with HD 53; AD, AS and HD 8; CM with HD 3; AS, CM and HD 2; AD with AS 2; AD with HD 2; AS with CM 1.
- Uniform: HD throughout 61; AS throughout 6; CM throughout 1; none AD throughout.
- Steering and provenance diverge in 37 of the 127 designs where both are coded: human steering with AS material 20, with AD material 10; AS steering with HD material 5; other 2.

Commonest profiles (engagement, steering, provenance, interpretation, positioning):

| Profile | Episodes |
|---|---|
| HD, HD, HD, HD, NE | 28 |
| HD, HD, HD, HD, AS | 18 |
| HD, HD, HD, HD, HD | 14 |
| AS, HD, AS, HD, AS | 9 |
| HD, NE, HD, HD, NE | 9 |
| HD, HD, HD, NE, HD | 6 |
| AS, AS, AS, AS, AS | 5 |
| HD, HD, HD, NE, AS | 5 |

The eight profiles cover 94 of 139 episodes. The commonest mixed profile is the learner who steers and judges while the AI's material makes up the work and the AI structures engagement (9).

## 2. Departure order

| Order | Dimension | Departs (% of coded) |
|---|---|---|
| 1 | Positioning of AI | 77 |
| 2 | Engagement | 35 |
| 3 | Provenance of production | 29 |
| 4 | Interpretive influence | 18 |
| 5 | Steering | 13 |

- Scale: H = .82 (bootstrap over entries, 2,000 resamples: 95% interval .73 to .91); reproducibility .96.
- **The top of the order holds.** Steering departs less often than interpretation in 96% of resamples; the full order above appears in 94% of resamples.
- Within collections: Georgia Tech H = .85, Stanford .89, Toronto .77 (reproducibility .96, .98, .95).
- Before the C12 sweep: H = .77, reproducibility .94, same order. The sweep sharpened the order but did not produce it.
- Pairwise structure: every design that departs on engagement, provenance, interpretation or steering also departs on positioning where positioning is coded (Hij = 1.00), and every steering departure also departs on engagement. The weak links are between provenance and the two retained dimensions: interpretation departs without provenance in 7 designs (Hij = .54) and steering without provenance in 6 (Hij = .45).
- Reading: the retained core is the direction of the exchange and judgment together; v2's "interpretation held longest" becomes "steering held longest, then interpretation".
- **The exceptions are mostly tutoring designs.** Twelve episodes break the order. Six share the profile in which the AI steers and judges while the learner produces the work (AS or CM on every dimension except provenance, HD): BuzzTutor (GT-06), SMART Tutor (GT-08), the Socratic agent in the entrepreneurship course (GT-09, co-mediated), Socratic Mind (GT-18), the healthcare pronunciation tool (GT-13) and the grammar-checker step of TO-BelloWrite. This is the intelligent-tutoring arrangement: the AI asks, hints and evaluates; the learner answers in their own words. Two more (TO-BelloWrite-A1, TO-MacKay-A2) cede only interpretation, with AI feedback as the standard for the learner's own work, as in v2. Three cede only provenance while engagement stays human (curation of AI images: ST-02, ST-05; GT-31). The cumulative order therefore describes designs in which AI produces; tutoring designs, in which AI directs and judges learner production, are a second, inverted arrangement. Episode-level list: e6_scale_exceptions.csv.

## 3. Networks

- **Model 1 is primary.** E5's recommendation already was to keep it.
- **Shared human-led core.** In every collection the five strongest mean connections join human-dominant nodes only: Georgia Tech engagement with provenance (.247), Stanford steering with provenance (.305), Toronto engagement with provenance (.262).
- **Stanford's steering-provenance link is reinstated as a descriptive reading.** E5 withdrew it because it joined two components of one dimension; under v2 they are independent dimensions, so the link is a legitimate co-occurrence: Stanford's policies most often leave the learner both directing and producing the work. Positions show no collection difference (p = .726, .615), so it stays descriptive, Low confidence.
- **EO** sits on the human-led pole of Model 2, nearest human steering (0.47) and human interpretation (0.57). Report it with both.
- **ML's position remains unreported.** Model 2's second dimension was not stable across representations of the interaction-structure dimensions in E5 (|r| = .27), so ML stays a descriptive finding.

## 4. Trajectories and dependence (unchanged on five dimensions)

19 steps between consecutive sequential episodes; mean change in the human-direction score +0.32; 8 of the 9 sequential entries whose score changes end closer to human direction (sign test p = .039); holistic carryover .69 against .53 for random pairs (p = .012).

## 5. Instructor episodes (exploratory contrast)

On five dimensions, 19 of 23 instructor episodes are mixed (14 on four dimensions in v2), against 71 of 139 learner episodes. Instructors position the AI as an assistant in 19 (83%), steer their own exchanges in 20 (87%), and no instructor episode is co-mediated on any dimension; interpretation is not evident in 8 (35%).

## What changes in the article

1. Mixed profiles: 71 of 139 (51%), replacing 56 (40%) plus 15 "divided".
2. Departure order: H = .82, reproducibility .96, five items; the retained core is steering and interpretation, with steering held longest (robust in 96% of resamples).
3. "Divided interaction structure" disappears as a category; the 30 of 37 human-steering, AI-material designs become the central multidimensional finding.
4. Model 1 is the primary network; Table A1 (counted once) is dropped; E5 becomes a one-sentence sensitivity note.
5. Stanford's steering-provenance link returns as a descriptive reading.
6. Instructor contrast: 19 of 23 mixed.

## Files

Scripts: e6_profiles.py (profiles, Guttman and Loevinger scaling with bootstrap, pre-sweep reversion, exceptions, instructor recount); outputs e6_profiles.json and e6_scale_exceptions.csv. To add to the materials repository.
