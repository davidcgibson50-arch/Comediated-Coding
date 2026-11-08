Co-Mediated Coding: Data, Codebook and Analysis Files

This repository holds the materials behind our article "Co-Mediated Coding: Rules, Reasoning-Model Coders and Multidimensional Profiles" (David Gibson, Curtin University, and M. Elizabeth Azukas, Georgia Tech Research Institute; manuscript in preparation). We share the codebook, the coded results, the source corpus, the epistemic network analysis (ENA) workflow and the human-readable summaries so that readers can trace any coded episode back to its source text and forward to the models.

The article describes a coding process in which human-authored rules and current-generation reasoning-model coders worked together across three phases: codebook creation, coding, and testing and analysis. The object of the coding is the Interactional Model of AI-Mediated Learning (AIM-AI), applied to instructor-authored case collections about teaching with generative AI.

Study at a glance
Item	Value
Framework	AIM-AI: four configurations (AI-dominant AD, AI-structured AS, co-mediated CM, human-dominant HD) across five dimensions (D1 engagement type, D2 steering, D3 provenance of production, D4 interpretive influence, D5 positioning of the AI)
Corpus	Three public collections of instructor-authored AI teaching cases (Georgia Tech, Stanford, Toronto); in the article these are described as Collections A, B and C
Units	89 entries (published cases) holding 162 mediation episodes; 139 learner episodes in 81 learner entries; 23 instructor-only episodes
Coding	Moderated coding under Codebook v0.7.1, blind recoding of 65 episodes by three AI-model coding sessions under v0.8, adjudication, the C12 majority-initiator sweep and the v0.8.1 patch
Frozen data	Data release 1 (October 30, 2026)
Models	Model 1 (Run 4.1, 15 dimension nodes) and Model 2 (Run 5, adding designed epistemic opportunity and mediational literacy nodes), fitted with rENA 0.3.1
Codebook in this repository	v0.8.5 (November 7, 2026)
Repository contents
1. Codebook

AIM-AI_Final_Codebook_v0_8_5.xlsx The authoritative codebook as a multi-sheet workbook. It defines the 4 x 5 configuration-by-dimension matrix with code IDs (for example HD-2, AS-5), the extension codes (designed epistemic opportunity, EO; mediational literacy, ML; trajectory use case; reporting stance and others), the decision rules, and the binding calibration rules C1 to C13 that take precedence over boundary notes. Every worked example in the calibration rules is invented and set in a discipline and with a tool absent from the coded sample, so that no example is keyed to a corpus entry.

AIM-AI_Final_Codebook_v0_8_5.md A plain-text Markdown rendering of the same codebook, convenient for reading on GitHub, diffing between versions, and supplying to a coder (human or AI) as a single file.

Version note: v0.8.5 is an editorial release. It clarifies that provenance of production (D3) is not to be read as a learning-activity type and changes no code definitions, boundaries or values. The coded data and models in this repository were produced under v0.8.4 and remain valid under v0.8.5.

2. Results

AIM-AI_Final_Results_Report.md The full results report for data release 1 (October 30, 2026). It covers the corpus and units, the coding process and agreement statistics (Krippendorff's alpha among the three v0.8 coding sessions), Model 1 and Model 2, analyses of episode-count clusters, sequence direction and within-entry dependence, the descriptive extension and reporting-stance codes, the instructor-only panel, twelve findings with confidence ratings, and limitations. The figures it cites are in the figures archive described below.

3. Figures

AIM-AI_Final_Figures-20261108T190452Z-1-001.zip The final figures referenced in the results report:

File	Content
AIM-AI_Final_Fig1_Model1_points_by_institution.png	Model 1 unit positions by collection, with means and 95% confidence intervals
AIM-AI_Final_Fig2a_Model1_mean_network_Georgia_Tech.png	Model 1 mean network, Georgia Tech
AIM-AI_Final_Fig2b_Model1_mean_network_Stanford.png	Model 1 mean network, Stanford
AIM-AI_Final_Fig2c_Model1_mean_network_Toronto.png	Model 1 mean network, Toronto
AIM-AI_Final_Fig3_Model2_points_with_EO_ML_nodes.png	Model 2 unit positions with all 17 node positions
AIM-AI_Final_Fig4_cluster_positions.png	Model 1 unit positions colored by episode-count cluster
AIM-AI_Final_Fig5_heatmap_dimension_by_cluster.png	Distribution of configurations on each dimension by cluster
4. Human-readable views of the coded episodes

AIM-AI Episode Encyclopedia.docx The coded learner episodes organized by cell of the AIM-AI matrix, built on Codebook v0.8.4 and data release 1. It opens with an overview, cell counts and narrative vignettes of the four within-episode trajectory cases, followed by one section per dimension (D1 to D5) and a section on the instructor-only episodes. Each entry gives the institution and title, a trajectory tag (single use, sequential, recurrent, within-episode) and a short paraphrase of the design. Quotation marks are used only for the source's own words.

AIM-AI Article Summaries with Heat Maps.docx One section per entry for all 89 entries, narrating every coded cell of the intended profile episode by episode, each followed by a heat map of the entry's profile (configurations by dimensions). This is the entry-level counterpart of the encyclopedia. Version note: these summaries were built on the moderated Codebook v0.7.1 coding (October 27, 2026), before the v0.8 recode, the C12 sweep and the v0.8.1 patch. Some cells therefore differ from data release 1. Where the two disagree, the results report and the encyclopedia are authoritative.

5. ENA workflow and coding history

ENA Analysis-20261108T190744Z-1-001.zip The working folder for the ENA, kept as an audit trail rather than a polished package. It contains:

01_Source_Coding, 02_ENA_Ready_Data, 03_ENA_Models_and_Outputs and 04_Analysis_Notes_and_Decisions: the original pipeline folders, including run notes for Runs 1 to 3.
05_Scripts_and_Restart: Python and R scripts for parsing coding forms, building ENA-ready files, merging and plotting, with a restart guide.
Version 7.2 files: materials from the v0.7.x coding stage.
Version 8: the v0.8 blind recode by three coding sessions (episodes_GPTv8.csv, episodes_CCODEv8.csv, claude-incognito-codesv8.xlsx and the matching entry files), agreement by field (v8_IRR_by_field.csv), the adjudication log, the C12 sweep log, the v0.8.1 patch log, resolved and ENA-ready intended-profile files for all 162 episodes, and the Run 4, Run 4.1 and Run 5 folders with their handoff notes.
A folder README describing the ENA data format.

Earlier-version files (for example aimai_ena_episodes_v07.csv and the "Superseded files" folder) are retained so that every step can be reconstructed; they are not the final data.

6. Corpus

Corpus files-20261108T191412Z-1-001.zip The source texts that were screened and coded:

Georgia Tech: the Academic AI Playbook (2026), in six PDF parts.
Stanford: AIM-AI_corpus_Stanford.txt, the extracted text of the entries drawn from the Stanford CTL AIMES library of examples.
Toronto: AIM-AI_corpus_Toronto.txt, the extracted text of the entries drawn from the University of Toronto teaching examples.
7. Coding template

04_entry_coding_template.csv The blank entry-level template used in the v0.8 blind recode for the reporting-stance codes. Each row identifies one of the 31 recoded entries (institution, entry ID, authors, short title, source category and screening decision) and leaves columns for Claim Stance (CS), AI-use Stance (US), Limitations Acknowledged (LA), Traces Collected (TC) and a memo. It shows the format a new coder receives and can be reused for replication.

Suggested reading order
The results report, for the findings and how they were reached.
The codebook (Markdown version for reading, workbook for coding).
The episode encyclopedia, to see what the coded cells look like in practice.
The ENA archive, to check or rerun any step.
Key terms
Entry: one published case in a collection.
Episode: one occasion in which a participant exchanges with an AI system toward a single objective; an entry may hold several.
Intended profile: codes taken from design statements, the basis of the models. The reported profile (enactment) was coded but is mostly not evident in these collections.
NE: not evident in the design statements.
Data release 1: the frozen coding of October 30, 2026, analyzed in the results report.
Limitations of these materials

All coding, adjudication and patch drafting were carried out by AI-model coding sessions working from shared, human-authored rules, with every ruling approved by a human researcher. The framework and initial codebook were human-produced, and human oversight shaped the process throughout. The agreement statistics reported here are consistency tests among AI-model sessions, not inter-rater reliability between independent human coders. The study is a design-layer analysis of instructor intentions and reporting stances, not of learner outcomes.

Rights and reuse

The corpus files reproduce texts published by Georgia Tech, Stanford University and the University of Toronto; copyright in those texts remains with their authors and institutions, and they are included for verification of the coding only. The codebook, coded data, scripts, figures and reports are the work of the authors. [Add license, for example CC BY 4.0 for data and documents and MIT for scripts.]

How to cite

When citing these materials, we suggest citing the article and the repository:

Gibson, D., & Azukas, M. E. (2026). Co-mediated coding: Rules, reasoning-model coders and multidimensional profiles [Manuscript in preparation]. DOI: [to be added on publication]

Gibson, D., & Azukas, M. E. (2026). Co-mediated coding: Data, codebook and analysis files (Data release 1) [Data set]. GitHub. DOI: [to be added, for example via a Zenodo release]

Contact

David Gibson, Curtin University (davidcgibson50@gmail.com)
