# **AIM-AI Final Results Report: Designed Mediation in Three Collections of Instructor-Authored AI Cases**

Prepared for David Gibson and Liz. October 30, 2026\. Codebook v0.8.4; data release 1 (October 30, 2026); models Run 4.1 (Model 1\) and Run 5 (Model 2), accepted October 30, 2026\. Status of the set: see AIM-AI\_Final\_README.md.

## **Headline Numbers**

|  | Model 1 (Run 4.1) | Model 2 (Run 5\) |
| :---- | :---- | :---- |
| Nodes | 15 dimension codes | 17 (adds EO designed and ML designed) |
| Variance explained, SV1 and SV2 | 33.9%, 12.8% | 27.0%, 10.7% |
| Goodness of fit, SV1 and SV2 | .99, .98 | .99, .97 |
| Window 2 stability, SV1 and SV2 (\|r\|) | .995, .942 | .994, .866 |
| Institutions, Kruskal-Wallis p (SV1, SV2) | .726, .615 | .644, .064 (Model 2B: .597, .008) |
| Coding pass, Mann-Whitney p (SV1, SV2) | .398, .438 | .388, .506 |

Learner-episode CM counts in data release 1: engagement 6, steering 3, provenance 2, interpretation 2, positioning 5; holistic CM 3, all at Georgia Tech. Units: 81 learner entries holding 139 learner episodes.

## **1\. Purpose and Scope**

We set out to describe how instructors design the mediation of learning by generative AI, using the Interactional Model of AI-Mediated Learning (AIM-AI) set out by \[AUTHORS\] (2026). The model starts from the premise, developed by Wertsch (1991), that human thinking and action are mediated by tools and signs, and it treats generative AI as a mediator of this kind. It places each mediation episode on a continuum of four reference configurations, AI-dominant (AD), AI-structured (AS), co-mediated (CM) and human-dominant (HD), across five dimensions: engagement type, steering, provenance of production, interpretive influence and the positioning of the AI. The engagement dimension follows the ICAP framework of Chi and Wylie (2014), which distinguishes passive, active, constructive and interactive engagement. The configurations order the distribution of cognitive responsibility between learner and AI; they are not a scale of quality, and an AI-dominant design can be the right design for its purpose.  
The corpus consists of faculty-authored or curated case collections. Under decision rule R29 we therefore treat the study as a design-layer analysis of instructor intentions and public reporting stances. Our main analysis uses the intended profile, coded from design statements. We also report what the collections say about enactment, but claims about the effect of AI mediation on learners would require traces of the learner-AI exchange or learner accounts, which these collections rarely provide.  
The report proceeds from the corpus and coding process (sections 2 and 3\) to the two network models (sections 4 and 5), the analyses of clusters, sequence and dependence (section 6), the descriptive extension and stance codes (section 7\) and the instructor-only panel (section 8). Section 9 gathers the findings with confidence ratings, and section 10 sets out the limitations.

## **2\. Corpus, Sample and Units**

We distinguish entries from episodes. An entry is one published case; an episode is one occasion in which a participant exchanges with an AI system toward a single objective (R1). An entry can contain several activities and episodes. Episodes are either learner episodes, in which students, student groups or student research teams work with AI, or instructor-only episodes, in which instructors, staff or research teams use AI for their own work (C11).

| Collection | Entries | Episodes | Learner episodes | Learner entries (ENA units) |
| :---- | :---- | :---- | :---- | :---- |
| Georgia Tech | 51 | 105 | 85 | 45 |
| Stanford | 18 | 24 | 24 | 18 |
| Toronto | 20 | 33 | 30 | 18 |
| Total | 89 | 162 | 139 | 81 |

*Table 1\.* Entries, episodes and units by collection. Eight entries contain only instructor-only episodes and are not ENA units.  
The ENA unit is the entry, and the conversation is the activity, so connections accumulate between consecutive episodes of the same activity. Among the 81 learner units, 41 entries have one learner episode, 27 have two and 13 have three or more. The collections differ in kind. The Georgia Tech playbook entries are detailed teaching accounts with many multi-episode designs; the Stanford entries are mostly course AI policies, with a few assignments; the Toronto entries are teaching examples, often staged as sequential assignments.

| Collection | Single use | Sequential | Recurrent | Within-episode |
| :---- | :---- | :---- | :---- | :---- |
| Georgia Tech | 31 | 16 | 36 | 2 |
| Stanford | 4 | 5 | 13 | 2 |
| Toronto | 6 | 20 | 4 | 0 |
| Total | 41 | 41 | 53 | 4 |

*Table 2\.* Trajectory use case of learner episodes by collection (C10).

## **3\. Coding Process**

The codebook moved through twelve versions between September 30 and October 30, 2026, listed in the Codebook versions sheet of the Decision Log. The decisive changes were the split into intended and reported profiles in v0.7, the binding calibration rules C1 to C11 in v0.7.1, the majority-initiator rule C12 in v0.8.1 and v0.8.2, and the rule on holistic Mixed, C13, in v0.8.4. C12 asks who is the majority initiator of the movement between learner and AI: AS when the AI's production draws the learner toward it, HD when the learner draws the AI's production toward the learner's own aims, and CM only where the design provides for mutual adaptation across rounds. C13 makes a holistic Mixed a last resort and confirms that Mixed is never a dimension value.  
All 162 episodes were first coded and moderated under v0.7.1 (Run 3). Under v0.8, three AI-model coding sessions (GPTv8, CCODEv8 and a Claude session without project context) recoded 65 episodes in 31 entries blind to the earlier codes. Cross-configuration disagreements were adjudicated (182 logged rulings), and a sweep applied C12 to every AS versus HD call across all 162 episodes (100 changes). Stage A of Run 5 resolved the designed epistemic-opportunity (EO) and mediational-literacy (ML) codes for the 65 recoded episodes: of 130 cells, 95 were unanimous, 29 kept the majority, 2 overturned it and 4 resolved three-way splits. Patch v0.8.1 and its addendum re-tested every CM code against mutual adaptation, resolved conflicts between trajectory use cases and Start and End configurations, and removed holistic Mixed; together they changed 14 episodes. A separate correction set GT-41-A1 D5 to AS in line with the Run 3.1 ruling. The patch produced data release 1 (October 30, 2026), the coding analyzed in this report. Every ruling is listed in the Decision Log.  
We measured agreement among the three v0.8 sessions with Krippendorff's alpha, following Hayes and Krippendorff (2007). On the 65 recoded episodes, alpha was .68 for intended D1, .84 for D2, .78 for D3, .71 for D4, .84 for D5, .70 for the holistic configuration, .70 for EO intended and .66 for ML intended (Appendix, Table 9). These are consistency statistics among AI-model coding sessions working from shared rules, not inter-rater reliability between independent human coders. The 97 episodes that were not recoded keep their moderated v0.7.1 codes as revised by the C12 sweep and the patch. Their EO and ML codes are accepted as v0.8 codes because v0.8 changed no EO or ML definition, boundary or value (amendment decision 1, October 30, 2026).  
Entry-level reporting-stance codes for claims, AI use, limitations and traces come from the three-coder v0.8 majority for the 31 recoded entries and from the v0.7.1 moderated entry-stance sheet for the other 58\. The three v0.8 coders reached a majority on every recoded stance field, so no moderated value had to be kept. Stance codes are descriptive and were not adjudicated under v0.8.

## **4\. Model 1: The 15-Node Dimensional Model (Run 4.1)**

We modeled the intended profile with epistemic network analysis (ENA). Shaffer et al. (2016) describe the method, and Bowman et al. (2021) set out its mathematical foundations. We used rENA 0.3.1 with a moving window of one episode, singular value decomposition, and the 15 codes present in at least three learner episodes. Prov.CM and Interp.CM fell below the threshold after the patch, and Steer.CM sits exactly at it. Table 3 shows the distributions behind the model.

| Dimension | AD | AS | CM | HD | NE |
| :---- | :---- | :---- | :---- | :---- | :---- |
| D1 Engagement type | 7 | 34 | 6 | 88 | 4 |
| D2 Steering | 1 | 13 | 3 | 112 | 10 |
| D3 Provenance of production | 11 | 27 | 2 | 97 | 2 |
| D4 Interpretive influence | 1 | 17 | 2 | 89 | 30 |
| D5 Positioning of the AI | 2 | 67 | 5 | 22 | 43 |
| Holistic configuration | 6 | 34 | 3 | 96 | 0 |

*Table 3\.* Intended codes of the 139 learner episodes.  
Human-dominant codes predominate on the first four dimensions. Positioning is the exception. The dimension records the social role a design gives the AI, a role that matters because, as Reeves and Nass (1996) showed, people respond to computers as social actors. Designs most often cast the AI as an assistant (AS-5), and nearly a third leave its position unstated.  
The model explains 33.9% of variance on the first dimension (SV1) and 12.8% on the second (SV2), with goodness of fit of .99 and .98. A window of two episodes reproduces the unit positions (\|r\| \= .995 and .942), and removing the one episode with a non-generative tool (Model 1B) changes nothing of substance. Table 4 gives the node positions that define the axes. SV1 runs from human-led work (Eng.HD at \-1.17, Interp.HD at \-0.83, Steer.HD at \-0.32) to AI-assisted production (Prov.AS at 2.11, Eng.AS at 1.31, Eng.AD at 1.06, Pos.AS at 0.87). On SV2, the positive pole gathers designs in which the AI supplies material or structure that the learner selectively consults (Prov.AD at 1.78, Steer.AS at 1.52, Interp.AS at 1.11, with Pos.HD at 1.67 and Prov.HD at 1.00). The negative pole is human steering in assistant-positioned designs (Pos.AS at \-1.76, Steer.HD at \-0.67).

| Node | SV1 | SV2 | Node | SV1 | SV2 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Eng.AD | 1.06 | 0.91 | Prov.AD | \-0.03 | 1.78 |
| Eng.AS | 1.31 | 0.26 | Prov.AS | 2.11 | 0.81 |
| Eng.CM | \-0.14 | 0.79 | Prov.HD | 0.29 | 1.00 |
| Eng.HD | \-1.17 | \-0.19 | Interp.AS | 0.06 | 1.11 |
| Steer.AS | 0.40 | 1.52 | Interp.HD | \-0.83 | \-0.30 |
| Steer.CM | 0.84 | \-0.39 | Pos.AS | 0.87 | \-1.76 |
| Steer.HD | \-0.32 | \-0.67 | Pos.CM | 0.56 | 0.14 |
|  |  |  | Pos.HD | 0.01 | 1.67 |

*Table 4\.* Model 1 node positions.  
The three collections show no detectable difference in network position: a Kruskal-Wallis test gives p \= .726 on SV1 and .615 on SV2 (Figure 1). Power to detect a difference is low, with 18 units each at Stanford and Toronto. Their mean networks share one core, a triad of human engagement, provenance and interpretation, and Stanford's network is weighted toward human steering with provenance and assistant positioning (Figure 2). The strongest mean connections are Eng.HD with Prov.HD (.247) at Georgia Tech, Steer.HD with Prov.HD (.305) at Stanford and Eng.HD with Prov.HD (.262) at Toronto. Positions agree closely with Run 4 before the patch (unit r \= .993 on SV1 and .958 on SV2). The units that moved most are those whose CM codes the patch changed: episodes moving from CM to HD shift toward the human-led pole, and those moving from CM to AS shift toward AI-assisted production.  
The original coding pass (pilot or full) does not separate units in the space (Mann-Whitney p \= .398 and .438). At code level, pilot entries carry Interp.HD less often than full-pass entries (.54 against .72, Fisher p \= .034), a difference we report as a coding-process caveat.  
*Figure 1\.* Model 1 unit positions by collection, with collection means and 95% confidence intervals. File: AIM-AI\_Final\_Fig1\_Model1\_points\_by\_institution.png.  
*Figure 2\.* Model 1 mean networks for Georgia Tech (2a), Stanford (2b) and Toronto (2c); line width shows mean connection weight. Files: AIM-AI\_Final\_Fig2a to Fig2c.

## **5\. Model 2: Dimensions Plus Designed Epistemic Opportunity and Mediational Literacy**

EO intended (alpha .70) and ML intended (alpha .66, borderline) met the usability rule and enter Model 2 as presence nodes. EO is present in 66 and ML in 56 of the 139 learner episodes. With the 15 Model 1 codes the model has 17 nodes. It explains 27.0% and 10.7% of variance, with goodness of fit of .99 and .97; two nodes that co-occur with many codes spread the variance. SV1 reproduces Model 1 almost exactly (unit r \= .991). SV2 keeps the Model 1 reading with its sign reversed, but it is reproduced less closely (\|r\| \= .861) and is less stable to the window (\|r\| \= .866, and .781 without the non-generative episode), so we limit claims that rest on SV2.  
Designed epistemic opportunity joins the human-led pole of SV1. Its nearest nodes are Steer.HD (distance 0.47) and Interp.HD (0.57), and its strongest links are to human interpretation and steering, most of all at Toronto (Table 5). Designed mediational literacy sits beside human steering (0.34 from Steer.HD), on the SV2 pole of human steering in assistant-positioned designs (Figure 3).

| Connection | All units | Georgia Tech | Stanford | Toronto |
| :---- | :---- | :---- | :---- | :---- |
| Interp.HD and EO | .136 | .134 | .098 | .181 |
| Steer.HD and EO | .135 | .136 | .112 | .155 |
| Prov.HD and EO | .111 | .112 | .058 | .162 |
| Steer.HD and ML | .106 | .074 | .194 | .100 |
| Prov.HD and ML | .104 | .066 | .172 | .128 |
| EO and ML | .066 | .065 | .048 | .085 |
| Pos.AS and ML | .056 | .044 | .083 | .061 |

*Table 5\.* Selected EO- and ML-linked mean connection weights in Model 2\.  
ML is more common at Stanford (62% of learner episodes) than at Georgia Tech (32%), with Fisher p \= .019. Because episodes within an entry are not independent, we also fitted generalized estimating equations with entries as clusters, the approach of Liang and Zeger (1986); the difference holds (omnibus p \= .029; Stanford against Georgia Tech odds ratio 3.62, p \= .011). On SV2 Stanford sits toward the ML pole (p \= .064 in Model 2A, .008 in Model 2B). Because that separation appears only on the less stable axis, we report it as a code-level difference rather than a difference in network structure.  
The Stanford ML codes rest mainly on awareness of what AI contributes rather than on deliberate decision-making. Of the 15 Stanford learner episodes with ML present, 5 are coded cognitive-work awareness (ML-CW), 3 epistemic awareness (ML-EP), 2 relational awareness (ML-RA), 2 multiple (ML-MX), 1 framing awareness (ML-FR) and 2 deliberate decision-making (ML-DD). The two ML-DD episodes are class-wide agreements on acceptable use, not designs in which each student makes and justifies decisions. Several of the cognitive-work codes rest on course policies that ask students to state what the AI did and did not contribute, and two ask little beyond describing the tools used and how AI output was combined with the student's writing, which R17 would not count as ML on its own. We therefore read Stanford's higher ML rate as a policy emphasis on accounting for AI's contribution, with that caveat. EO does not differ by collection or by cluster.  
Because four of the Stanford ML codes are borderline, we checked the sensitivity of the Stanford difference. We recomputed the Stanford against Georgia Tech comparison on the learner episodes of those two collections, with Fisher's exact test and the same entry-clustered GEE, after excluding (a) ST-24-A1 and ST-26-A1, whose ML-CW codes rest mainly on disclosure (R17), and (b) those two plus ST-07-A1 and ST-09-A1, whose ML-DD codes rest on class-wide agreements rather than individual justified decisions (Table 5a).

| Sample | Stanford ML | Georgia Tech ML | Fisher p | GEE odds ratio (95% CI) | GEE p |
| :---- | :---- | :---- | :---- | :---- | :---- |
| All learner episodes | 15 of 24 (62%) | 27 of 85 (32%) | .009 | 3.63 (1.34, 9.82) | .011 |
| (a) Without ST-24-A1 and ST-26-A1 | 13 of 22 (59%) | 27 of 85 (32%) | .026 | 3.18 (1.17, 8.64) | .023 |
| (b) Also without ST-07-A1 and ST-09-A1 | 11 of 20 (55%) | 27 of 85 (32%) | .070 | 2.65 (0.95, 7.41) | .063 |

*Table 5a.* Sensitivity of the Stanford against Georgia Tech ML difference to four borderline Stanford ML codes. Two-collection comparison, so the first row differs slightly from the three-collection tests above.  
The difference survives exclusion (a) but not exclusion (b): with all four borderline codes removed, the odds ratio falls to 2.65 and its confidence interval includes 1\. The check is one-sided, since Georgia Tech's ML codes were not audited in the same way; a comparable audit there could move the difference in either direction.  
*Figure 3\.* Model 2 unit positions by collection with all 17 node positions; EO designed and ML designed in green. File: AIM-AI\_Final\_Fig3\_Model2\_points\_with\_EO\_ML\_nodes.png.

## **6\. Clusters, Sequence Direction and Dependence**

We grouped learner entries by episode count (one, two, three or more: 41, 27 and 13 entries) and re-tested the five October 28 findings on data release 1 (Figures 4 and 5; Appendix, Table 7). Entries with three or more episodes are longer (median 1,485 words against 785 for single-episode entries), so we control for length and topic count where the comparison allows.

> * Episode count does not move entries in the ENA space once institution, length and topics are controlled (SV1 b \= \-0.13, p \= .42; SV2 b \= \-0.03, p \= .68).  
> * Entries with three or more episodes tighten the human-constructive triad of engagement, provenance and interpretation (+0.34, p \= .025; p \= .056 and .053 with controls), while steering connections do not differ (p \= .98).  
> * Unstated positioning (D5 NE) is more common in the three-or-more cluster (45% against 24%; GEE odds ratio 2.85 with controls, p \= .040). The earlier claim that co-mediation concentrates there is no longer supported: holistic CM in that cluster now rests on two episodes in one entry.  
> * Sequential designs move responsibility toward the learner: 8 of 9 sequential entries with a change move toward HD (sign test p \= .039; order permutation p \= .009). Across all 40 multi-episode entries the evidence is weak (p \= .18).  
> * Consecutive episodes are alike. The holistic configuration carries over between consecutive episodes more than between random pairs (.69 against .53, p \= .012), and the intraclass correlation of the human-direction score within entries is .32 (design effect 1.46, effective n 67).

**Within-episode trajectories.** Only four learner episodes are designed to shift configuration within one episode: three move toward human direction and one toward AI direction. With n \= 4 we treat them as descriptive only and present them as vignettes in the episode encyclopedia rather than modeling them. Trajectory evidence in this corpus lies mainly in sequential and recurrent designs, where movement is visible across episodes rather than within them. Sequential pairs of episodes (19 steps) move on average \+0.32 on the human-direction score, with 9 steps toward HD and 3 toward AD.  
*Figure 4\.* Model 1 unit positions colored by episode-count cluster. File: AIM-AI\_Final\_Fig4\_cluster\_positions.png.  
*Figure 5\.* Distribution of configurations on each dimension by cluster, learner episodes. File: AIM-AI\_Final\_Fig5\_heatmap\_dimension\_by\_cluster.png.

## **7\. Extension Codes**

Codes other than EO and ML intended did not meet the usability rule (alpha at least .667, resolved under v0.8, at least three learner episodes) and are reported descriptively. Agreement was insufficient for dialogue type (.31), uptake (.40), learner variability (.48), sociotechnical frame (.49), stated purpose (.53) and epistemic object (.55). The Laurillard activity type, a context field drawn from the conversational framework of Laurillard (2001), reached .70 but describes the setting rather than the mediation and is not modeled. The reported (enacted) dimensions were coded with moderate consistency (.61 to .79), but 69% to 78% of learner episodes are NE on each, and Stanford's entries carry no reported codes at all. These codes fell out of modeling for insufficient evidence in this corpus, not because they fail to apply: instructor narratives rarely show what learners did with AI contributions. Reported uptake, for example, is NE in 87% of learner episodes.  
Designed epistemic opportunity is almost always evaluation of AI output (EO-EV, 56 of the 66 EO-present learner episodes). The other codes are rare: recognition that an AI contribution embeds an assumption (EO-RE) in 4 episodes, challenge (EO-CH) in 3, redirection of an AI frame (EO-RD) in 2, and a design in which an AI assumption passes through unrecognized (EO-IN) in 1\. Recognition and redirection require the narrative to show what the AI assumed and what learners then did with it, which a design description seldom does.  
Designed mediational literacy is present in 56 learner episodes: cognitive-work awareness (ML-CW) in 17, deliberate decision-making (ML-DD) in 15, epistemic awareness (ML-EP) in 10, multiple codes (ML-MX) in 7, relational awareness (ML-RA) in 4 and framing awareness (ML-FR) in 3\.  
Reporting stances show a corpus that claims more than it documents (Table 6). Of 89 entries, 58 claim benefits, 20 are descriptive (all 18 Stanford entries, which are policies and assignments without outcome claims), 9 report mixed results and 2 are critical. Forty-seven entries state no limitation. Traces of the exchange are collected but not reproduced in 43 entries and partly reproduced in 8; no entry reproduces a full trace.

| Stance | Georgia Tech (51) | Stanford (18) | Toronto (20) |
| :---- | :---- | :---- | :---- |
| Claim: benefit claimed / mixed / critical / descriptive | 44 / 6 / 1 / 0 | 0 / 0 / 0 / 18 | 14 / 3 / 1 / 2 |
| AI use: assigned / mixed / optional / limited / instructor use / prohibited | 21 / 13 / 9 / 1 / 6 / 1 | 8 / 0 / 0 / 10 / 0 / 0 | 11 / 4 / 4 / 0 / 1 / 0 |
| Limitations: none / design / evidence / both | 12 / 18 / 11 / 10 | 18 / 0 / 0 / 0 | 17 / 2 / 1 / 0 |
| Traces: not described / collected, not reproduced / partly reproduced | 21 / 23 / 7 | 11 / 7 / 0 | 6 / 13 / 1 |
| Evidence stance: T2 / T3 / design only (no T1) | 28 / 14 / 9 | 0 / 0 / 18 | 9 / 3 / 8 |

*Table 6\.* Reporting-stance codes by collection (entries). Descriptive; not adjudicated under v0.8.

## **8\. Instructor-Only Panel**

The 23 instructor-only episodes (20 at Georgia Tech, 3 at Toronto) are coded on the same matrix but excluded from the models. Their holistic configurations are HD 13, AS 8 and AD 2\. Instructors position the AI as an assistant far more often than learner designs do (Pos.AS 83% against 48%), steer their own exchanges (Steer.HD 87%), and none of their episodes is co-mediated on any dimension. In most of them the instructor specifies the task, reviews AI drafts and keeps the decision, which is the pattern C12 codes as human-dominant. Their interpretive influence is unstated more often than in learner designs (NE 35% against 22%), because accounts of instructor use seldom say how outputs were judged.

## **9\. Findings**

| Number | Finding | Evidence | Confidence |
| :---- | :---- | :---- | :---- |
| 1 | Designs in these collections are predominantly human-dominant. | Holistic HD in 96 of 139 learner episodes; HD is the modal code on D1 to D4. | High |
| 2 | Designed co-mediation is rare. | Three holistic CM learner episodes, all at Georgia Tech, each with an AI configured to initiate, challenge or role-play. Partly a consequence of the mutual-adaptation criterion. | High (as a description under C12) |
| 3 | The three collections show no detectable difference in network position. | Kruskal-Wallis p \= .726 and .615 (Model 1); power is low, with 18 units each at Stanford and Toronto. | Moderate |
| 4 | Designed epistemic opportunity belongs to the human-led pattern. | EO on the human-led SV1 pole, nearest Steer.HD and Interp.HD; SV1 stable. | Moderate |
| 5 | Designed mediational literacy accompanies human steering in assistant-positioned designs and is more common at Stanford. | Node placement on SV2, the less stable axis; GEE p \= .029; ML alpha borderline; Stanford codes rest mainly on awareness of AI's contribution; depends on four borderline ML codes (GEE p \= .063 without them). | Very low |
| 6 | Sequential designs move responsibility toward the learner. | 8 of 9 sequential entries toward HD; permutation p \= .009; weak across all multi-episode entries. | Moderate |
| 7 | Episode count does not move entries in the network space. | Controlled SV1 b \= \-0.13, p \= .42. | Moderate |
| 8 | Entries with three or more episodes tighten the human-constructive triad. | p \= .025, borderline with controls for institution, length and topics. | Low |
| 9 | Unstated positioning concentrates in entries with three or more episodes. | GEE p \= .040 with controls; permutation p \= .06. | Low |
| 10 | Consecutive episodes of an entry share their configuration. | Carryover p \= .012; ICC .32. | Moderate |
| 11 | Instructors position AI as an assistant for their own work. | Pos.AS 83% against 48% for learner episodes. | High |
| 12 | The collections document enactment thinly. | No T1 trace; 69% to 78% NE on reported dimensions; 47 entries state no limitation. | High |

*Table 8\.* Findings with confidence ratings on the scale High, Moderate, Low, Very low.

## **10\. Limitations**

> 1. **Consistency, not reliability.** All coding, adjudication and patch drafting were done by AI-model sessions under shared rules, with rulings approved by David Gibson. Our agreement statistics are consistency tests, not inter-rater reliability between independent human coders.  
> 2. **Design-layer scope.** We model what designs intend. The findings describe instructor intentions and reporting stances, not what learners did or learned.  
> 3. **No T1 traces.** No entry reproduces a trace of the learner-AI exchange, so the reported profile rests on participant accounts and instructor observations.  
> 4. **The mutual-adaptation criterion.** C12 codes CM only where the design provides for mutual adaptation across rounds. Designs in which learners converse freely with an AI, without configuring it to initiate or contest, are coded HD or AS. The scarcity of CM partly reflects this criterion.  
> 5. **Small CM base and borderline codes.** Three holistic CM episodes and Steer.CM at the threshold make CM-specific readings fragile; ML intended has borderline consistency (.66). Several ML codes sit close to R17's exclusion of disclosure alone, and the Stanford ML difference depends on four of them (section 5).  
> 6. **Low power between collections.** With 18 units each at Stanford and Toronto, the absence of a detectable difference in network position is weak evidence of similarity.  
> 7. **SV2 stability in Model 2\.** SV2 positions, including Stanford's separation, are less robust than SV1.  
> 8. **Within-episode trajectories.** Four cases are too few to model; they are reported descriptively.  
> 9. **Mixed provenance of codes.** Of 162 episodes, 65 carry v0.8 blind-recoded codes and 97 carry moderated v0.7.1 codes revised by the C12 sweep and the patch. Stance codes were not adjudicated under v0.8.

## **11\. References**

\[AUTHORS, e.g., Surname, A. A., & Surname, B. B.\] (2026). *An interactional model of AI-mediated learning (AIM-AI)* \[Manuscript submitted for publication\].  
Bowman, D., Swiecki, Z., Cai, Z., Wang, Y., Eagan, B., Linderoth, J., & Shaffer, D. W. (2021). The mathematical foundations of epistemic network analysis. In A. R. Ruis & S. B. Lee (Eds.), *Advances in quantitative ethnography* (pp. 91–105). Springer. https\://doi.org/10.1007/978-3-030-67788-6\_7  
Chi, M. T. H., & Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. *Educational Psychologist, 49*(4), 219–243. https\://doi.org/10.1080/00461520.2014.965823  
Hayes, A. F., & Krippendorff, K. (2007). Answering the call for a standard reliability measure for coding data. *Communication Methods and Measures, 1*(1), 77–89. https\://doi.org/10.1080/19312450709336664  
Laurillard, D. (2001). *Rethinking university teaching: A conversational framework for the effective use of learning technologies* (2nd ed.). Routledge.  
Liang, K.-Y., & Zeger, S. L. (1986). Longitudinal data analysis using generalized linear models. *Biometrika, 73*(1), 13–22. https\://doi.org/10.1093/biomet/73.1.13  
Reeves, B., & Nass, C. (1996). *The media equation: How people treat computers, television, and new media like real people and places*. CSLI Publications.  
Shaffer, D. W., Collier, W., & Ruis, A. R. (2016). A tutorial on epistemic network analysis: Analyzing the structure of connections in cognitive, social, and interaction data. *Journal of Learning Analytics, 3*(3), 9–45. https\://doi.org/10.18608/jla.2016.33.3  
Wertsch, J. V. (1991). *Voices of the mind: A sociocultural approach to mediated action*. Harvard University Press.

## **Appendix: Detailed Statistics**

*Table 7\.* Cluster tests for the October 28 findings (Run 4.1; learner entries; clusters of 1, 2 and 3 or more episodes \= 41, 27 and 13 entries).

| Test | Statistic | p |
| :---- | :---- | :---- |
| 3 or more vs 1 on SV1, controlling institution, words, topics (OLS) | b \= \-0.13 | .42 |
| 3 or more vs 1 on SV2, same controls | b \= \-0.03 | .68 |
| HD triad weight, 3 or more vs 1 (raw; with institution; with institution and depth) | 0.34; 0.30; 0.34 | .025; .056; .053 |
| Steering connections, 3 or more vs 1 | 0.00 | .98 |
| Positioning NE, 3 or more vs others (GEE with controls; entry permutation) | 45% vs 24%; OR 2.85 | .040; .06 |
| Holistic CM, 3 or more vs others (Fisher; GEE) | 2 episodes in one entry | .24; .28 |
| Prov.AS, 3 or more vs others (GEE with controls; permutation) | 9% vs 24%; OR 0.22 | .016; .07 to .09 |
| Pos.HD, 3 or more vs others | 9% vs 19% | .11 to .21 |
| Sequential entries toward HD (sign test; order permutation) | 8 of 9 | .039; .009 |
| All multi-episode entries toward HD | 40 entries | .18 |
| Holistic carryover, consecutive vs random pairs | .69 vs .53 | .012 |
| ICC of the human-direction score within entries | .32 (design effect 1.46; effective n 67\) |  |
| Pilot vs full pass: Steer.HD; Interp.HD; holistic CM (Fisher) | .74 vs .86; .54 vs .72; .03 vs .01 | .086; .034; .582 |

*Table 9\.* Agreement of the three v0.8 coding sessions on the 65 recoded episodes (consistency, not inter-rater reliability).

| Field | All three agree | Krippendorff's alpha |
| :---- | :---- | :---- |
| Intended D1 to D5 | .71, .89, .80, .77, .86 | .68, .84, .78, .71, .84 |
| Holistic intended | .72 | .70 |
| Start and End configuration | .72, .69 | .69, .66 |
| Trajectory use case | .71 | .66 |
| EO intended; ML intended | .77; .69 | .70; .66 |
| Reported D1 to D5 | .66, .77, .71, .86, .85 | .61, .65, .65, .79, .74 |

*Table 10\.* Model 2 code-level tests (learner episodes; Fisher with episodes treated as independent; GEE exchangeable, clustered by entry).

| Node | Grouping | Rates | Fisher p | GEE p |
| :---- | :---- | :---- | :---- | :---- |
| EO | Institution | GT .46, ST .38, TO .60 | .236 | .417 |
| EO | Cluster (1, 2, 3 or more) | .56, .48, .39 | .289 | .412 |
| EO | 3 or more vs single-episode entries | .39 vs .56 | .131 | .188 (OR 0.49) |
| ML | Institution | GT .32, ST .62, TO .47 | .019 | .029 |
| ML | Cluster (1, 2, 3 or more) | .46, .39, .36 | .642 | .613 |
| ML | 3 or more vs single-episode entries | .36 vs .46 | .385 | .352 (OR 0.65) |

Full outputs (points, line weights, node positions, model objects, cluster and sequence files) are in the Run 5 folder bundle; every ruling is in AIM-AI\_Final\_Decision\_Log.xlsx.