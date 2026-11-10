# AIM-AI Codebook v0.8.5 (text rendering for coders)

This file renders the coder-facing sheets of `AIM-AI_Final_Codebook_v0_8_5.xlsx`. Where they apply, the Calibration Rules take precedence over the boundary notes in the Codebook section. All examples are invented.

## 1. Purpose, evidence tiers, and coding procedure

*v0.8.5 (November 7, 2026): editorial. The crosswalk notes of the four provenance codes (AD-3, AS-3, CM-3, HD-3) no longer pair each code with a learning-activity type (Acquisition, Practice, Inquiry with discussion and collaboration, Inquiry with production); they now trace provenance to the production side of interaction structure and participant roles. No definition, boundary, rule or code value changes. Experiment E4 (condition B3) removed these notes with the LT field and found no change in dimension coding, so data release 1 stands as coded.*

*v0.8.4 (October 30, 2026): adds Calibration Rule C13, which makes a holistic "Mixed" a last resort after three ordered tests (majority initiator, required over permitted, median of the coded dimensions) and confirms that Mixed is never a dimension value. No other definition, boundary, or code value changes (see v0.8.4 Changes).*

*v0.8.3 (October 29, 2026): restores the computed sequence-direction index from v0.7.2 (HS, SS, SD; Extension Codes rows 29 to 31; Decision Rule R30; threshold in Lists!X2). The index is computed after coding from the intended profile, so no coder judgment, definition, or code value changes. The Coding Form does not carry the computed columns; the index is added to the ENA file by script.*

*v0.8 (October 29, 2026): every corpus-derived example and every episode reference has been removed. Examples in the Codebook, Extension Codes, and Calibration Rules sheets are invented, and rule text names no corpus entry. Screening records and version histories (v0.5 to v0.7) have moved to the adjudication log. No definition, boundary, or code value is changed (see v0.8 Changes).*

AIM-AI Codebook: Operationalizing the Interactional Model of AI-Mediated Learning

Version 0.7 (draft for author review), October 24, 2026. Changes from v0.6: the codebook now separates designed conditions from enacted mediation. Each episode carries an intended profile (design statements) and a reported profile (enactment evidence tiered by proximity to the learner: T1 traces, T2 participant account, T3 instructor or developer observation; weights 2.0, 1.5, 1.0). D2 is re-specified as steering, D3 as provenance of production (Laurillard activity type becomes a context field), and reported D5 as learner orientation, with the design's positioning recorded in the intended profile. New: uptake codes, turn-level move coding for traces, entry-level reporting-stance codes, and rules R22 to R29; R3, R4, R5, R12, R13, R15, R16, and R17 revised. Full record on the v0.7 Changes sheet. Earlier versions: v0.6 added R21 (static AI artifacts), Critical evaluation of AI (HD), ML-RA, and the revised R12; v0.5 realigned to the 14 September 2026 manuscript; v0.4 added adjacency-weighted coherence; v0.3 excluded non-interactional commentaries; v0.2 separated learner and instructor matrices.

**Purpose**

We developed this codebook to characterize AI-mediated learning with the Interactional Model of AI-Mediated Learning (AIM-AI). From v0.7 the codebook treats a configuration as a property of the observed learner-AI exchange and its traces in the learner's work. Designs and instructor accounts establish and describe conditions; they are coded, but as the intended profile and as reported evidence of lower proximity, so that design intent is not confounded with the mediation of learning. Applied to faculty-authored collections (the Georgia Tech playbook, the Stanford AIMES library, and the University of Toronto CTSI examples), the codebook supports an exploratory design-layer study of instructor intentions and public reporting stances (R29).

**Code ID convention**

Configuration prefix plus dimension number: AD (AI-dominant), AS (AI-structured), CM (co-mediated), HD (human-dominant); dimensions 1 engagement type, 2 interaction structure (steering), 3 provenance of production, 4 interpretive influence, 5 social positioning of AI. Profile prefixes: I- (intended), R- (reported). NE marks a dimension not evident. Extension families: EO, EB, ML, UP (uptake), LM and AM (learner and AI moves), ET (evidence tier), ES, CS, US, LA, TC (stance codes).

**Evidence tiers (R22)**

T1 trace: a raw record of the exchange or of the work's development (transcript, log, version history, screen or process recording, reproduced prompt). T2 participant account: the coded participant's own report (reflection, interview, survey response, quoted voice; an instructor's account of their own AI use). T3 observation: an instructor's or developer's report of how participants engaged. T4 design intent: what the design asks for; it populates the intended profile only. Weights for modeling reported evidence: T1 2.0, T2 1.5, T3 1.0.

**Coding procedure (summary)**

0. Screen the entry (R7, R14, R21) and code its reporting stance (R26). 1. Read the full entry once without coding. 2. Identify learning activities and mediation episodes, coding an episode only where the participant exchanges with the AI system (R1, R21). 3. Record participant, context, frame, Laurillard type, and stated purpose (R2, R3, R18). 4. Code the intended profile from design statements (R23). 5. Code the reported profile from enactment evidence, assigning a tier to each dimension (R22, R23, R27). 6. Code epistemic opportunity, mediational literacy, and uptake in intended and reported versions (R16, R17, R25). 7. Where T1 traces exist, code turns on the Move Coding Form and use its indicators to inform the reported profile (R24). 8. Review indices and flags, assign holistic configurations by judgment for each profile (R12, R28), and memo divergences. 9. Review the Entry Profile (R13).

**Interpretive stance**

Codes are descriptive and non-hierarchical: the continuum orders configurations by the distribution of cognitive responsibility, not by educational value, and an author's valence is not evidence of a configuration (R9). Misalignment across dimensions, and divergence between intended and reported profiles, are analytically informative rather than coding error.

## 2. Framework

Table 1. The AIM-AI Framework with Codebook IDs (v0.7)

Engagement and interpretive influence descriptors follow Table 4 of the 14 September 2026 manuscript; steering, provenance, and positioning are re-specified in v0.7 (author decision, October 24, 2026). Configurations are reference points on the interactional mediation continuum, not discrete categories.

| Interactional Mediation (reference configuration) | 1. Engagement Type | 2. Interaction Structure (steering) | 3. Provenance of Production | 4. Interpretive Influence | 5. Social Positioning of AI |
|---|---|---|---|---|---|
| AI-Dominant (AD) | AD-1: Passive | AD-2: AI steers; learner follows | AD-3: AI-produced; learner receives | AD-4: Limited interpretation within AI-generated framing | AD-5: Authority (deference) |
| AI-Structured (AS) | AS-1: Active | AS-2: AI scaffolds; learner chooses within it | AS-3: AI-produced; learner selects, adapts, completes | AS-4: Human interpretation within AI-structured framing | AS-5: Assistant (delegation) |
| Co-Mediated (Hybrid) (CM) | CM-1: Interactive | CM-2: Steering shared; both redirect | CM-3: Co-produced through exchange | CM-4: Reciprocal interpretation and meaning making | CM-5: Collaborator (contestation and negotiation) |
| Human-Dominant (HD) | HD-1: Constructive | HD-2: Learner steers; AI responds | HD-3: Learner-produced; AI consulted | HD-4: Human-directed interpretation and meaning making | HD-5: Advisor (selective consultation) |

Note. The unit of analysis is the mediation episode, a coherent sequence of human-AI interactions organized around one learning or task objective; an episode requires that the participant exchanges with the AI system (R21). Each episode is coded twice: an intended profile from design statements, and a reported profile from enactment evidence tiered by proximity to the learner (R22, R23). In the intended profile D5 records the positioning the design communicates; in the reported profile it records learner orientation (R27). Steering (who directs the exchange) and provenance (whose contributions make up the work) are coded independently: an on-demand explainer, for example, is learner-steered (HD-2) with AI-produced content (AD-3). Laurillard's activity types are recorded as context. The arrow from AI-dominant to human-dominant indicates increasing human responsibility for framing, direction, and interpretation; it does not indicate educational value.


## 3. Calibration Rules (binding; take precedence over Codebook boundary notes)

Adopted by David Gibson on October 26, 2026; worked examples replaced for v0.8 on October 29, 2026. These rules sharpen v0.7 boundaries without changing any definition; where they apply they take precedence over the boundary notes in the Codebook sheet. Every worked example is invented: each keeps the boundary it teaches but is set in a discipline, and with a tool, that do not appear in the coded sample. No example is drawn from, paraphrased from, or keyed to a corpus entry.

### C1. Steering: HD-2 vs CM-2 (multi-turn designs in which the AI challenges, proposes, or plays a role)

Code CM-2 when the design (a) configures or instructs the AI to raise challenges, questions, or proposals on its own turns, not only on the learner's request, and (b) requires the learner to take these up, so that AI turns can change the pathway. An AI playing an interlocutor in a conversation (for example, a conversation partner or a role-played colleague or client who initiates contributions) satisfies (a). Code HD-2 when the learner chooses each prompt, including prompts that ask the AI to challenge them: a challenge the learner invokes does not make steering CM (R10). Many turns alone are insufficient (CM-2 boundary).

*Worked examples:* (Hypothetical throughout.) Philosophy of science seminar: an assistant configured to open each of its turns with an objection to the student's argument, which the student must answer before moving on: CM-2. Hydrology design studio: the assistant proposes a drainage layout on each turn, and students must find where it fails under the storm record and repair it before the next proposal: CM-2. Hospitality management: teams send menu proposals to an assistant configured as a restaurant owner and interpret its replies, deciding what to send each time: HD-2.

### C2. Steering: HD-2 vs AS-2 vs AD-2 (who supplies the structure of the exchange at run time)

Code AS-2 when the AI system, by its design or configuration, supplies the sequence, options, or staged hints and the learner chooses within them (hint ladders, tutoring loops, practice generators, option menus, custom GPTs that gate what the AI provides). Code AD-2 when the system selects the next step without learner choice. Code HD-2 when the learner initiates and scopes each request; an on-demand explainer is HD-2 with AD-3 provenance. When a learner prompt yields an AI first draft that the learner then revises, D2 stays HD-2 and the draft's influence is recorded on D3 (AS-3) and D4 (AS-4), keeping D2 and D3 independent (R5).

*Worked examples:* (Hypothetical throughout.) Music theory: an ear-training tutor that diagnoses interval errors and unlocks graded hints the learner requests in turn: AS-2. Mineralogy: a quiz generator producing identification items at a difficulty the learner selects: AS-2. Astronomy: an on-demand chatbot answering whatever the learner asks about the week's observations: HD-2 (AD-3). Social work: a detailed learner prompt for an AI first draft of a case note, then revision by the learner: HD-2.

### C3. Instructor-designed protocols, critique steps, and verification steps

An instructor's protocol (a required sequence, a supplied starter prompt, turn limits, mandated critique or verification) is part of the design, not AI steering. Code D2 from who drives the exchange within the protocol: learner-executed steps are HD-2 unless the AI system enacts the structure (C2: AS-2 or AD-2). Mandated verification or critique is evidence for D4 (C4) and for EO, not for D2.

*Worked examples:* (Hypothetical throughout.) Forestry: teams run an instructor-supplied prompt to estimate stand volume, then check the output against published yield tables: HD-2. Archaeology: students prompt summaries of site reports and must check each summary against the excavation records: HD-2, HD-4. Theatre studies: the instructor's tiers of permitted help are built into a configured assistant that releases only what each tier allows: AS-2.

### C4. Interpretive influence: HD-4 vs AS-4 vs CM-4 (and NE)

Code HD-4 when the design requires the learner to judge AI output against criteria the AI did not supply (sources, disciplinary standards, the learner's own prior work, a rubric), or states a duty to verify AI output or a sanction for unverified output. Code AS-4 when the AI supplies the frame, the alternatives, or the criteria and the learner evaluates within them, including revising an AI first draft with no external standard named. Code CM-4 only when the design provides for reciprocal revision: the AI challenges the learner's interpretation and either party's interpretation can change through the exchange. A bare statement that the work or interpretation must be the student's own, with no verification, critique, or comparison step, is NE.

*Worked examples:* (Hypothetical throughout.) Agronomy: check each value in an AI-compiled table of soil properties against the cited survey reports: HD-4. Meteorology: correct an AI explanation of a frontal system against the assigned readings: HD-4. Grant writing: revise an AI first draft of a project summary within its structure when no external standard or verification is named: AS-4. Musicology: an assistant configured to rebut the student's reading of a symphony, with a required revision of the reading in light of the rebuttals: CM-4. Anthropology: a syllabus clause reserving interpretation of field data to the student, with no verification or comparison step: NE.

### C5. Near-boundary procedure (extends R10; revised 2026-10-26)

Choose the nearer reference point; do not default to HD. A near-boundary call is a call between configurations (AD, AS, CM, HD) on a configuration-valued field (I-D1 to I-D5, R-D1 to R-D5, holistic, start and end). For such a call: (a) the memo names the R10 question that decided it (alternatives available; AI challenge and reshaping; reciprocal reshaping versus selective challenge) and quotes or cites the deciding design statement; (b) set Confidence to Low; (c) set the R10 flag. Within-configuration questions (evidence tier; a configuration versus NE under C8) and calls on non-configuration fields (EO, ML, uptake, dialogue type, epistemic object, stated purpose, learner variability, trajectory use case, stance) are not near-boundary calls: rate their confidence by ordinary judgment. Revision of October 26, 2026 (David Gibson): only cross-configuration disagreements are routed to adjudication; all other disagreements are resolved by majority or by the mechanical rules recorded in the decision log.

### C6. Positioning (intended D5): HD-5 vs AS-5 vs CM-5 vs NE

Code intended D5 from the role the design assigns the AI (R27), read from what the AI is asked to do, not from a single label. AS-5: the design relies on the AI to carry parts of the work (drafting, summarizing, generating, getting unstuck). HD-5: consultation is optional and the learner is expected to weigh AI input against their own judgment and may set it aside. CM-5: the design calls for contestation or negotiation with the AI as a partner. NE: the AI is an object the learner tests, audits, trains, or analyzes, and the design communicates no participant role. A label alone ('partner', 'collaborator', 'assistant') is a cue (R11 by analogy): code CM-5 from a partner label only when the described role includes contestation or negotiation; otherwise code the described role.

*Worked examples:* (Hypothetical throughout.) Library science: students audit a catalogue recommender for what it fails to surface: NE. Oceanography: students compare several assistants on accuracy criteria they define for tide forecasts: NE. Geography: a policy listing permitted uses, with every AI-supplied claim confirmed against an independent source: HD-5. Veterinary anatomy: an assistant described as 'a study partner' that explains and checks answers after students attempt them: AS-5 or HD-5 by the described role. Logistics: an author calls a demand-forecasting tool 'a partner' while describing forecasts that staff review and approve: AS-5.

### C7. Provenance: AS-3 vs HD-3 (R15 is retired; the AS-3 and HD-3 boundaries and R5 apply)

Code HD-3 when the assessed product is the learner's own text, analysis, or design and AI output is (a) consulted or brainstormed with, the final work being in the learner's own words, (b) used for a bounded sub-task inside learner-produced work, (c) the object of the learner's analysis, or (d) rejected or replaced. Code AS-3 when AI-produced material appears in the product in substantial part, revised or not. AI-generated intermediate material that the learner traces, redraws, or transforms: AS-3 if it sets the form of the product, HD-3 if the final product is learner-made from it; such cases are near-boundary calls (C5).

*Worked examples:* (Hypothetical throughout.) Philosophy: AI may be used to brainstorm, but essays are written in the student's own words: HD-3. Botany: students re-prompt an image generator to reproduce their own leaf illustration, and the assessed work is their analysis of the differences: HD-3. Agronomy: AI formats the learner's field-plot measurements into a table inside a report the learner wrote: HD-3. Tourism marketing: AI-generated brochure images and slogans make up most of the submitted campaign: AS-3.

### C8. Evidence threshold for an intended code versus NE (all dimensions; chiefly D4 and D5)

Code an intended dimension only where a design statement (an instruction, a rubric criterion, a policy clause, or a stated framing of the AI) bears on it. Do not infer D4 from D2 or D3, or D5 from the tool type (R5). Reflective episodes with no new exchange (R21 reflective provision) take NE on D2 and D5. An episode left with fewer than three coded dimensions is flagged (R12), not filled by inference.

*Worked examples:* (Hypothetical throughout.) Field sketches are uploaded to condition image generation and no evaluation step is described: D4 NE. A policy line requiring students to check AI-produced text for errors before submitting: D4 HD-4. A reflection on the learner's own earlier exchange, with no new exchange: D2 and D5 NE.

### C9. Engagement (D1): CM-1 vs AS-1 vs HD-1

Code D1 from the overt behavior the design asks for (ICAP; R11). CM-1 (interactive): turn-by-turn building in which the learner responds to the substance of AI turns and the AI to the learner's. AS-1 (active): prompt-and-revise or select-and-apply loops; repeated prompting toward a fixed target is a request loop. HD-1 (constructive): the learner generates beyond the AI's material.

*Worked examples:* (Hypothetical throughout.) Spoken negotiation practice in which the assistant plays a supplier and answers the learner's offers: CM-1. Repeated prompting toward a target map rendering: AS-1.

### P1. Learner status (decision c)

Students count as learners whatever the activity setting, including students working in a research team. Staff research or teaching teams are not learners (R2): code them and flag them as non-learner episodes.

### P2. Audit recodes (decision b)

The four audit recodes are not applied to Coder A. They are decided by the blind recoding and run-off under C2 and C7.

### C10. Trajectory use case (definitions; added 2026-10-26)

Single use: one occasion of the arrangement. Sequential: designed stages with different objectives in a fixed order (the episode is one stage of such a sequence). Within-episode: the configuration is designed or reported to shift inside the one episode (Start differs from End). Recurrent: the same arrangement is repeated across occasions, sessions, or weeks. Where more than one applies, code Within-episode if Start differs from End, otherwise Recurrent over Sequential over Single use.

### C11. Instructor and staff episodes (convention; added 2026-10-26)

Code the intended profile of an instructor or staff episode from the instructor's own description of the practice they set up for themselves (what they ask the AI to do, how they review its output). Leave an intended dimension NE only when the source describes no practice bearing on it. The instructor's account of their own use is reported evidence at T2 (R22).

### C12. Majority initiator: AS vs HD vs CM where AI-produced material figures in the work (extends C5; added 2026-10-29, revised 2026-10-29)

Apply to every AS versus HD call on D1, D2, D3, the holistic configuration, and Start and End where AI-produced material (a draft, answer, set of options, artifact, code, or analysis) figures in the work. Ask who is the majority initiator of the movement between the two parties. AS: the AI's production draws the human toward it; the human selects, accepts, submits, or adjusts the material within the AI's form and substance. HD: the human draws the AI's production toward the human's own aims; the human specifies what the AI is to produce, edits, corrects, rewrites, or rebuilds it, or judges and changes it against a standard the AI did not supply (sources, literature, disciplinary criteria, the human's own prior work, ideas, or specification). Repeated human re-prompting toward the human's own target remains HD while the AI only executes. CM: both parties adapt themselves and to each other across repeated rounds, each re-editing and re-setting the context in response to the other, so that the AI's contributions change the human's direction as well as the human's changing the AI's; code CM only where the design provides for this mutual adaptation. This rule takes precedence over the prompt-and-revise cue in C9, the draft-revision clause in C2, and the 'revised or not' clause in C7. D4 remains under C4 (a verification step that only checks AI output is evidence for D4, not D3) and D5 remains under C6. An episode resolved under this rule is coded as one configuration (Start equals End) unless the design describes a shift in who initiates.

Worked examples: (Hypothetical throughout.) Viticulture: students ask an assistant for five candidate pruning schedules and submit the one they prefer, unchanged: AS. Numismatics: an assistant drafts catalogue descriptions of coins; students tidy the wording and file them: AS. Maritime law: an assistant drafts a summary of a salvage dispute; students correct it against the governing statute and submit their corrected version: HD. Glassblowing: students specify a vessel form, have an assistant draft a kiln schedule, and adjust it repeatedly against their own firing logs: HD. Choreography: an assistant proposes a phrase; students rework it, the assistant revises its next proposal in light of their changes, and the students revise their score in light of the assistant's proposals, across several stated rounds: CM.

### C13. Holistic "Mixed" (last resort; added 2026-10-30)

Code the holistic configuration as Mixed only when none of the following tests yields a predominant configuration, applied in order: (1) the majority initiator (C12); (2) what the design requires predominates over what it only permits; (3) the median of the coded dimensions (AD = 1, AS = 2, CM = 3, HD = 4). Mixed is never a dimension value; D1 to D5 take AD, AS, CM, HD or NE only.

Worked examples: (Hypothetical throughout.) Marine biology: students may use an assistant to draft sections of a reef survey report, but every species identification must be checked against the field guide, and a single misidentification fails the report. The verification is required and the drafting only permitted, so the holistic configuration is HD. Typography: a learner asks a font-pairing assistant for suggestions and adopts the one it returns. Checking the pairing against a style manual is available but not required, and the learner accepts the AI's production (C12), so the holistic configuration is AS.

## 4. Codebook (20 intersections)

### AD-1: AI-Dominant, Engagement Type (Passive)

- **Operational Definition:** The human attends to and receives AI output (reads, watches, listens) without overtly manipulating it, selecting among alternatives, or generating from it.
- **Inclusion Indicators:** Participants review AI-generated summaries, explanations, audio or video overviews, or model answers; outputs are used as delivered; editing is minimal or cosmetic. Traces: learner move types across the episode (receiving, selecting, generating, co-building) observed directly (R24).
- **Boundary / Exclusion Rule:** If the human selects, compares, highlights, or applies the output, code AS-1 (Active). Passive is descriptive, not pejorative (e.g., intentional exposure to model reasoning). If the participant only receives an AI output produced in someone else's exchange (e.g., an instructor-made AI summary) without interacting with the system, the engagement is outside the model (R21).
- **Example A (hypothetical):** "Before each seminar, students asked the course chatbot to summarize the week's readings and read the summary it returned."
- **Example B (hypothetical):** "Usage logs showed most students requested AI summaries the night before the quiz and rarely returned to the primary readings." (Consumption pattern implies reception without manipulation.)
- **Cue Words (prompts, not proof):** read, reviewed, watched, listened, was given, received, consumed
- **Theoretical Anchor:** Chi & Wylie (2014)
- **Crosswalk to v0.6:** Retained from v0.6; trace indicators added

### AD-2: AI-Dominant, Interaction Structure (steering) (AI steers; learner follows)

- **Operational Definition:** The AI determines the pathway of the exchange (what comes next, which item or step, when it ends); the learner's turns respond to or execute AI-set direction.
- **Inclusion Indicators:** Adaptive sequencing; AI-initiated next steps followed without redirection; sessions ending when the system declares completion. Traces: AI directive moves (AM-RD) answered by compliance or requests to continue.
- **Boundary / Exclusion Rule:** If the AI offers options or scaffolds among which the learner decides when and which, code AS-2. Code who directs, not who produces content (D3).
- **Example A (hypothetical):** "The tutor chose each next problem and students worked through them in the order it set."
- **Example B (hypothetical):** "Logs showed sessions ended when the system declared mastery rather than when students stopped."
- **Cue Words (prompts, not proof):** the system decided, assigned, next step, followed, sequence
- **Theoretical Anchor:** Wertsch (1991); Hutchins (1995); Borchers et al. (2026)
- **Crosswalk to v0.6:** Steering part of v0.6 AD-2; its production part moves to AD-3

### AD-3: AI-Dominant, Provenance of Production (AI-produced; learner receives)

- **Operational Definition:** The substantive content of the learner's work or understanding at the end of the episode is AI-produced and taken up as delivered.
- **Inclusion Indicators:** Explanations, summaries, drafts, code, or images used as returned; uptake UP-AD. Traces: AI text or code appearing unchanged in the product or version history.
- **Boundary / Exclusion Rule:** If the learner selects among, adapts, or completes AI material, code AS-3.
- **Example A (hypothetical):** "Version history shows the submitted paragraph identical to the AI's response."
- **Example B (hypothetical):** "Students said they used what the tutor explained to answer the quiz items."
- **Cue Words (prompts, not proof):** used as is, copied, pasted, the AI wrote, explained it to me
- **Theoretical Anchor:** Hutchins (1995); Grinschgl & Neubauer (2022); Gerlich (2025)
- **Crosswalk to v0.6:** Production side of v0.6 AD-2 (interaction structure and participant roles). Occupies the D3 position that learning activity held in v0.6; activity type is now the Laurillard context field and does not define this code.

### AD-4: AI-Dominant, Interpretive Influence (Limited interpretation within AI-generated framing)

- **Operational Definition:** The AI performs most interpretive functions: it frames the problem, identifies what information is relevant, proposes the explanation, and in effect determines meaning; the participant takes these up with little evaluation, questioning, or reframing. AI-introduced assumptions shape the interpretive field with limited opportunity to become visible.
- **Inclusion Indicators:** Acceptance without verification; AI errors or hallucinations pass through; responses converge on AI framings; the author notes participants did not question outputs. Traces: whether AI-introduced framings recur in later learner turns and in the product, and whether learner challenge or verification moves occur (R24, R25).
- **Boundary / Exclusion Rule:** If the human evaluates or chooses among AI-supplied framings, code AS-4. If AI framings are contested and revised, code CM-4. Record the epistemic opportunity separately (EO codes, R16); do not infer EO-IN from AD-4.
- **Example A (hypothetical):** "Many submissions reproduced the AI's framing of the ethical dilemma almost verbatim, including its assumption that cost was the primary consideration."
- **Example B (hypothetical):** "We noticed that responses across all three sections converged on the same three examples." (Convergence implies an inherited framing.)
- **Cue Words (prompts, not proof):** took at face value, accepted, did not question, reproduced, converged, hallucinated sources went unnoticed
- **Theoretical Anchor:** Wertsch (1991); Borchers et al. (2026); Litts et al. (2021); Caliskan et al. (2017); Ofosu-Asare (2025); Jose et al. (2025)
- **Crosswalk to v0.6:** Retained from v0.6; trace indicators added

### AD-5: AI-Dominant, Social Positioning of AI (Authority (deference))

- **Operational Definition:** In the reported profile, the learner treats AI output as correct or expert: accepts it without verification and defers to it over other sources. In the intended profile, the design presents the AI as an authoritative source.
- **Inclusion Indicators:** Acceptance without checking; deference language. Traces: uptake UP-AD of claims without verification moves (LM-VE). Accounts: 'it's always right'.
- **Boundary / Exclusion Rule:** Reported D5 is coded only from learner behavior, learner accounts, or observation of learners; an instructor's description of the tool is design framing (intended D5) (R27).
- **Example A (hypothetical):** "When the AI's value conflicted with the lab manual, students altered their data."
- **Example B (hypothetical):** "Students described the tutor as more reliable than their TAs."
- **Cue Words (prompts, not proof):** trusted, always right, relied on, deferred
- **Theoretical Anchor:** Reeves & Nass (1996); Jose et al. (2025)
- **Crosswalk to v0.6:** Retained label; reported definition restricted to learner orientation

### AS-1: AI-Structured, Engagement Type (Active)

- **Operational Definition:** The human manipulates AI output (selects, compares, highlights, applies, practices) without generating substantially new ideas beyond what the AI supplied.
- **Inclusion Indicators:** Choosing among AI alternatives; working AI-generated problems; annotating AI output; applying AI recommendations. Traces: learner move types across the episode (receiving, selecting, generating, co-building) observed directly (R24).
- **Boundary / Exclusion Rule:** If the human generates new explanations or products beyond the AI's material, consider HD-1 (Constructive); if sustained mutual building, CM-1 (Interactive).
- **Example A (hypothetical):** "Students chose the AI-proposed solution they judged most efficient and used it to complete the next problem set."
- **Example B (hypothetical):** "The headings in most outlines matched one of the three structures the AI had offered." (Artifacts reveal selection among AI options.)
- **Cue Words (prompts, not proof):** chose, selected, compared, applied, practiced, worked through
- **Theoretical Anchor:** Chi & Wylie (2014)
- **Crosswalk to v0.6:** Retained from v0.6; trace indicators added

### AS-2: AI-Structured, Interaction Structure (steering) (AI scaffolds; learner chooses within it)

- **Operational Definition:** The AI supplies the structure of the exchange (options, staged hints, a workflow) and the learner decides when to proceed and which option to take, without reshaping the structure.
- **Inclusion Indicators:** Staged hints requested at the learner's discretion; AI-proposed workflows followed with learner choices. Traces: option and scaffold moves (AM-OP, AM-SC) answered by selection (LM-SE).
- **Boundary / Exclusion Rule:** If the learner reshapes the structure or both parties redirect, code CM-2; if the learner initiates and scopes each exchange and the AI only responds, code HD-2.
- **Example A (hypothetical):** "Students asked for the next hint when they were ready and chose which of the tutor's suggested approaches to try."
- **Example B (hypothetical):** "Most sessions followed the chatbot's closing offer of a practice problem."
- **Cue Words (prompts, not proof):** hints, step-by-step, guided, workflow, chose among, suggested
- **Theoretical Anchor:** Wertsch (1991); Hutchins (1995); Borchers et al. (2026)
- **Crosswalk to v0.6:** Steering part of v0.6 AS-2; its production part moves to AS-3

### AS-3: AI-Structured, Provenance of Production (AI-produced; learner selects, adapts, completes)

- **Operational Definition:** The work is built from AI-produced material or scaffolds that the learner chooses among, revises, personalizes, or completes.
- **Inclusion Indicators:** Uptake UP-AP; AI drafts revised; solutions built from AI hints; AI images placed within a learner-curated work. Traces: AI content traceable in the product with learner edits.
- **Boundary / Exclusion Rule:** If contributions from both build on each other and cannot be attributed to one party, code CM-3; if the AI performs a delegated sub-task inside learner-produced work, code HD-3.
- **Example A (hypothetical):** "Students kept the AI-written lab procedure and inserted their own instrument settings before submitting."
- **Example B (hypothetical):** "The headings in most outlines matched one of the AI's three structures."
- **Cue Words (prompts, not proof):** starting point, revised the AI draft, personalized, built on its suggestion
- **Theoretical Anchor:** Hutchins (1995); Grinschgl & Neubauer (2022)
- **Crosswalk to v0.6:** Production side of v0.6 AS-2 (interaction structure and participant roles). Occupies the D3 position that learning activity held in v0.6; activity type is now the Laurillard context field and does not define this code.

### AS-4: AI-Structured, Interpretive Influence (Human interpretation within AI-structured framing)

- **Operational Definition:** The human evaluates alternatives and determines meaning among them, but the AI has framed the problem, identified the relevant information, and supplied the alternatives and evaluative criteria. Interpretive responsibility is greater than in AD-4 yet exercised within an AI-structured field.
- **Inclusion Indicators:** Justifying a choice among AI options; evaluating AI suggestions against AI-supplied criteria; interpretation bounded by the AI's menu. Traces: whether AI-introduced framings recur in later learner turns and in the product, and whether learner challenge or verification moves occur (R24, R25).
- **Boundary / Exclusion Rule:** If the human questions the menu itself or introduces alternatives outside it, consider CM-4 or HD-4.
- **Example A (hypothetical):** "Students had to justify why they adopted one of the AI's three proposed sampling designs over the others."
- **Example B (hypothetical):** "Even the strongest projects stayed within the three approaches the AI had suggested; no team proposed a fourth." (Interpretation bounded by AI framing.)
- **Cue Words (prompts, not proof):** justify your choice, evaluate the options, pick the best, weigh the suggestions
- **Theoretical Anchor:** Wertsch (1991); Borchers et al. (2026); Litts et al. (2021); Caliskan et al. (2017); Ofosu-Asare (2025); Jose et al. (2025)
- **Crosswalk to v0.6:** Retained from v0.6; trace indicators added

### AS-5: AI-Structured, Social Positioning of AI (Assistant (delegation))

- **Operational Definition:** The learner relies on the AI to carry parts of the work or to structure progress, delegating without deferring on judgment.
- **Inclusion Indicators:** Delegation requests; reliance to get unstuck; accounts describing the AI as a helper or tool.
- **Boundary / Exclusion Rule:** Distinguish from HD-5: an assistant is relied upon to proceed; an advisor is consulted optionally.
- **Example A (hypothetical):** "Students said they used it to break the assignment into steps whenever they were stuck."
- **Example B (hypothetical):** "Most reflections said the tool produced the first version of each section and they filled in the rest."
- **Cue Words (prompts, not proof):** helper, assistant, tool, got me unstuck
- **Theoretical Anchor:** Reeves & Nass (1996); Jose et al. (2025)
- **Crosswalk to v0.6:** Retained label; reported definition restricted to learner orientation

### CM-1: Co-Mediated (Hybrid), Engagement Type (Interactive)

- **Operational Definition:** Sustained multi-turn dialogue in which human and AI contributions build substantively on one another (ICAP interactive: co-generative exchange).
- **Inclusion Indicators:** Multiple rounds; later turns reference earlier ones; both parties add ideas, objections, or evidence. Traces: learner move types across the episode (receiving, selecting, generating, co-building) observed directly (R24).
- **Boundary / Exclusion Rule:** Many turns alone are insufficient: repetitive request and response loops are AD or AS. Look for mutual building.
- **Example A (hypothetical):** "Students completed at least five rounds of dialogue in which they defended a position, responded to the AI's objections, and revised their claims."
- **Example B (hypothetical):** "Submitted transcripts averaged 25 turns, and later student turns frequently referred back to objections the AI had raised earlier."
- **Cue Words (prompts, not proof):** dialogue, back-and-forth, rounds, debate, conversation, iterate
- **Theoretical Anchor:** Chi & Wylie (2014)
- **Crosswalk to v0.6:** Retained from v0.6; trace indicators added

### CM-2: Co-Mediated (Hybrid), Interaction Structure (steering) (Steering shared; both redirect)

- **Operational Definition:** Both learner and AI initiate topic shifts, raise questions, or redirect, and neither controls the pathway; direction is negotiated across turns.
- **Inclusion Indicators:** Agents prompted to challenge with room for learner redirection; topic shifts initiated by both parties. Traces: learner redirect or challenge moves (LM-RD, LM-CH) and AI redirect or challenge moves (AM-RD, AM-CH), each taken up.
- **Boundary / Exclusion Rule:** Many turns alone are insufficient. If the learner sets every direction and the AI's challenges do not change the pathway, code HD-2 (R10).
- **Example A (hypothetical):** "Planning a soil survey, the assistant pushed toward fewer sampling sites; the student pulled the plan back to slope coverage, and the assistant then raised a new objection about site access."
- **Example B (hypothetical):** "Transcripts showed topic shifts initiated by both the students and the agent."
- **Cue Words (prompts, not proof):** Socratic, devil's advocate, steer, redirect, pushed back, negotiated
- **Theoretical Anchor:** Vygotsky (1978); Dumas et al. (2010); Engeström (1999)
- **Crosswalk to v0.6:** Steering part of v0.6 CM-2

### CM-3: Co-Mediated (Hybrid), Provenance of Production (Co-produced through exchange)

- **Operational Definition:** The work emerges from the exchange, with substantive contributions from both learner and AI that build on each other.
- **Inclusion Indicators:** Arguments, plans, or designs revised in step with AI contributions. Traces: alternating learner generation (LM-GE) and AI production (AM-PR) moves with mutual uptake.
- **Boundary / Exclusion Rule:** Repeated requests for AI output that the learner then edits are AS-3.
- **Example A (hypothetical):** "The sampling plan grew turn by turn as the student and the assistant added and dropped candidate sites."
- **Example B (hypothetical):** "Revision histories show claims tightening in step with the AI's counterarguments."
- **Cue Words (prompts, not proof):** co-wrote, built together, back and forth, evolved through
- **Theoretical Anchor:** Hutchins (1995); Engeström (1999); Laurillard (2001)
- **Crosswalk to v0.6:** Production side of v0.6 CM-2 (interaction structure and participant roles). Occupies the D3 position that learning activity held in v0.6; activity type is now the Laurillard context field and does not define this code.

### CM-4: Co-Mediated (Hybrid), Interpretive Influence (Reciprocal interpretation and meaning making)

- **Operational Definition:** Interpretive functions are shared and contested: framing, relevance, explanation, and evaluative criteria become explicit and are negotiated, the human challenges the AI and the AI challenges the human, and interpretations are revised through exchange. Assumptions can become objects of reciprocal questioning.
- **Inclusion Indicators:** Contesting AI claims with evidence; AI counterarguments prompting revision; documented evolution of interpretation. Traces: whether AI-introduced framings recur in later learner turns and in the product, and whether learner challenge or verification moves occur (R24, R25).
- **Boundary / Exclusion Rule:** If the human evaluates AI output against their own fixed criteria without reciprocal revision, code HD-4.
- **Example A (hypothetical):** "When the AI characterized the policy as settled, a student challenged it with contrary evidence, and the AI's revised response led her to narrow her own claim."
- **Example B (hypothetical):** "Revision histories showed claims tightening across drafts in step with the AI's counterarguments." (Reciprocal influence inferred from artifacts.)
- **Cue Words (prompts, not proof):** challenged, pushed back, counterargument, revised, negotiated, reconsidered
- **Theoretical Anchor:** Wertsch (1991); Borchers et al. (2026); Litts et al. (2021); Caliskan et al. (2017); Ofosu-Asare (2025); Jose et al. (2025)
- **Crosswalk to v0.6:** Retained from v0.6; trace indicators added

### CM-5: Co-Mediated (Hybrid), Social Positioning of AI (Collaborator (contestation and negotiation))

- **Operational Definition:** The learner treats the AI as a peer whose contributions warrant engagement and disagreement.
- **Inclusion Indicators:** Contestation and negotiation in traces; accounts describing the AI as a partner; disagreement treated as productive.
- **Boundary / Exclusion Rule:** Positioning is distinct from structure (R5): an exchange can be co-mediated while the learner defers to the AI.
- **Example A (hypothetical):** "Students argued with the agent and kept the objections they found persuasive."
- **Example B (hypothetical):** "One student wrote that she now treated the assistant as a sparring partner whose objections she had to answer."
- **Cue Words (prompts, not proof):** partner, collaborator, sparring partner, pushed back
- **Theoretical Anchor:** Reeves & Nass (1996); Jose et al. (2025)
- **Crosswalk to v0.6:** Retained label; reported definition restricted to learner orientation

### HD-1: Human-Dominant, Engagement Type (Constructive)

- **Operational Definition:** The human generates ideas, explanations, or products beyond the information given (ICAP constructive); AI contributions are peripheral to generation.
- **Inclusion Indicators:** Original writing, design, analysis, or explanation by the human; AI consulted for bounded checks. Traces: learner move types across the episode (receiving, selecting, generating, co-building) observed directly (R24).
- **Boundary / Exclusion Rule:** If generation happens through sustained co-generative dialogue with the AI, code CM-1.
- **Example A (hypothetical):** "Students wrote their own explanations of each design decision and consulted the AI only to check terminology."
- **Example B (hypothetical):** "Final projects contained original data collection and analyses not found in any AI output we tested."
- **Cue Words (prompts, not proof):** created, designed, wrote their own, generated, built, explained in their own words
- **Theoretical Anchor:** Chi & Wylie (2014)
- **Crosswalk to v0.6:** Retained from v0.6; trace indicators added

### HD-2: Human-Dominant, Interaction Structure (steering) (Learner steers; AI responds)

- **Operational Definition:** The learner initiates, scopes, redirects, and closes the exchange; AI turns respond to learner requests and do not set the pathway.
- **Inclusion Indicators:** Learner-initiated questions or requests drive each turn; on-demand asking; bounded uses at learner-chosen points. Traces dominated by learner request, question, redirect, and close moves (LM-RQ, LM-QU, LM-RD, LM-CL).
- **Boundary / Exclusion Rule:** Learner steering does not imply learner production: an on-demand explainer is HD-2 with AD-3 provenance. If the AI's structure shapes the work, consider AS-2.
- **Example A (hypothetical):** "Students asked the chatbot whatever they were stuck on and stopped when they had what they needed."
- **Example B (hypothetical):** "Logs show short, learner-initiated sessions scattered across the term."
- **Cue Words (prompts, not proof):** asked, at their discretion, when needed, permitted only for, on demand
- **Theoretical Anchor:** Wertsch (1991); Hutchins (1995); Borchers et al. (2026)
- **Crosswalk to v0.6:** Steering part of v0.6 HD-2

### HD-3: Human-Dominant, Provenance of Production (Learner-produced; AI consulted)

- **Operational Definition:** The substantive content is the learner's; AI contributions are consulted, checked, or perform delegated sub-tasks, or the work is the learner's analysis of AI output.
- **Inclusion Indicators:** Original analysis; AI used for verification, proofreading, or bounded sub-tasks such as formatting tables of the learner's own measurements; AI uptake limited to minor edits or rejected.
- **Boundary / Exclusion Rule:** If AI-produced material forms a substantial part of the product, code AS-3 even when the learner directs the exchange.
- **Example A (hypothetical):** "Students wrote their own geology field report and used the model only to convert their outcrop measurements into a formatted table."
- **Example B (hypothetical):** "Final reports contained analyses not found in any AI output we tested."
- **Cue Words (prompts, not proof):** wrote their own, only to check, proofread, delegated, our analysis
- **Theoretical Anchor:** Hutchins (1995); Grinschgl & Neubauer (2022)
- **Crosswalk to v0.6:** Production side of v0.6 HD-2 (interaction structure and participant roles). Occupies the D3 position that learning activity held in v0.6; activity type is now the Laurillard context field and does not define this code.

### HD-4: Human-Dominant, Interpretive Influence (Human-directed interpretation and meaning making)

- **Operational Definition:** The human frames the problem, identifies relevant information, sets the evaluative criteria, and determines meaning; AI outputs are verified against human standards, and AI may be used selectively to test, challenge, or extend independently developed reasoning.
- **Inclusion Indicators:** Verification requirements; critique of AI output against disciplinary criteria; human-owned argumentation; AI invoked as a test of reasoning the human has already developed. Traces: whether AI-introduced framings recur in later learner turns and in the product, and whether learner challenge or verification moves occur (R24, R25).
- **Boundary / Exclusion Rule:** If interpretations shift reciprocally through exchange, code CM-4. Selective AI challenge invoked by the human does not by itself make an episode CM (R10).
- **Example A (hypothetical):** "Students were required to verify every AI-suggested source against the original and discard any they could not confirm."
- **Example B (hypothetical):** "The rubric allocated most points to students' justification of claims rather than to the claims themselves." (Design intent locating interpretive authority with the human.)
- **Cue Words (prompts, not proof):** verify, fact-check, critique, evaluate against, their own criteria, stress-test
- **Theoretical Anchor:** Wertsch (1991); Borchers et al. (2026); Litts et al. (2021); Caliskan et al. (2017); Ofosu-Asare (2025); Jose et al. (2025)
- **Crosswalk to v0.6:** Retained from v0.6; trace indicators added

### HD-5: Human-Dominant, Social Positioning of AI (Advisor (selective consultation))

- **Operational Definition:** The learner consults AI optionally and weighs its input against their own judgment, often setting it aside.
- **Inclusion Indicators:** Selective consultation; frequent rejection or non-uptake (UP-RJ, UP-IG); accounts of a 'second opinion'.
- **Boundary / Exclusion Rule:** Distinguish from AS-5 (Assistant), where the learner relies on the AI to proceed.
- **Example A (hypothetical):** "A doctoral student called the AI a second opinion she could take or leave."
- **Example B (hypothetical):** "Several students reported not using the AI at all for major sections."
- **Cue Words (prompts, not proof):** second opinion, consult, sounding board, optional
- **Theoretical Anchor:** Reeves & Nass (1996); Jose et al. (2025)
- **Crosswalk to v0.6:** Retained label; reported definition restricted to learner orientation

## 5. Extension codes

### EO-IN: Hidden epistemology: Epistemic Opportunity (Inherited)

- **Operational Definition:** AI-introduced assumptions about relevance, evidence, explanation, authority, or legitimate reasoning shape the participant's interpretation without being recognized as choices.
- **Inclusion Indicators:** Convergence on AI framings; culturally situated associations or omissions pass through unremarked; the author notes participants treated the AI's account as complete.
- **Boundary / Exclusion Rule:** If participants notice the assumption, code EO-RE. Do not infer EO-IN from AD-4 or AD-5 alone (R5, R16). Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "Most students' explanations of the market crash foregrounded the same two causes the AI had emphasized, and none mentioned that other accounts existed."
- **Indirect Evidence Example (hypothetical):** "Across sections, case analyses described the 'typical patient' in the same demographic terms the chatbot had used."
- **Cue Words (prompts, not proof):** took for granted, the standard account, same framing, unquestioned
- **Source Section (14 Sept manuscript):** Interpretive Influence and Hidden Epistemology; Scenario A
- **Theoretical Anchor:** Litts et al. (2021); Caliskan et al. (2017); Jose et al. (2025)

### EO-RE: Hidden epistemology: Epistemic Opportunity (Recognized)

- **Operational Definition:** Participants identify that an AI contribution embeds a perspective, selection, emphasis, or assumption.
- **Inclusion Indicators:** Annotating what the AI included and omitted; naming a default perspective or bias; noting what the AI treated as relevant.
- **Boundary / Exclusion Rule:** If participants go on to assess the assumption against evidence or criteria, code EO-EV. Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "Students annotated the AI's summary to mark which perspectives it had foregrounded and which it had left out."
- **Indirect Evidence Example (hypothetical):** "In reflections, most students named at least one thing the chatbot 'assumed we already agreed with.'"
- **Cue Words (prompts, not proof):** noticed, pointed out, identified the bias, what's missing, default perspective
- **Source Section (14 Sept manuscript):** Interpretive Influence and Hidden Epistemology
- **Theoretical Anchor:** Litts et al. (2021); Ofosu-Asare (2025)

### EO-EV: Hidden epistemology: Epistemic Opportunity (Evaluated)

- **Operational Definition:** Participants assess an AI-introduced assumption against evidence, disciplinary criteria, or other sources.
- **Inclusion Indicators:** Comparing AI accounts with primary sources; judging whether AI evidence fits a claim; rubric criteria for evaluating AI framing.
- **Boundary / Exclusion Rule:** If the assumption is contested within the human-AI exchange, code EO-CH. Evaluation may occur outside the exchange. Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "Teams compared the AI's account of the policy's history with two archival sources and rated where its causal emphasis held up."
- **Indirect Evidence Example (hypothetical):** "The rubric awarded points for judging whether the AI's evidence was appropriate to the claim it supported."
- **Cue Words (prompts, not proof):** verified, compared against, assessed, weighed, checked the source
- **Source Section (14 Sept manuscript):** Interpretive Influence and Hidden Epistemology; Scenario B
- **Theoretical Anchor:** Wertsch (1991); Jose et al. (2025)

### EO-CH: Hidden epistemology: Epistemic Opportunity (Challenged)

- **Operational Definition:** Participants contest an AI-introduced assumption within the exchange by pushing back, requesting counterevidence, or asking the AI to justify or consider alternatives.
- **Inclusion Indicators:** Requests such as 'justify that criterion' or 'what would a critic say'; documented AI revisions following challenge.
- **Boundary / Exclusion Rule:** If the participant replaces the AI's framing with their own interpretive direction, code EO-RD. Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "When the assistant treated cost as the decisive criterion, students asked it to justify that criterion and then to argue from an equity standpoint."
- **Indirect Evidence Example (hypothetical):** "Transcripts contained frequent requests such as 'what are you assuming here?'"
- **Cue Words (prompts, not proof):** pushed back, asked it to justify, challenged, counterargument, contested
- **Source Section (14 Sept manuscript):** Interpretive Influence and Hidden Epistemology; Scenario C
- **Theoretical Anchor:** Borchers et al. (2026); Jose et al. (2025)

### EO-RD: Hidden epistemology: Epistemic Opportunity (Redirected)

- **Operational Definition:** Participants reframe the interpretive direction after an AI-introduced assumption becomes visible, establishing their own frame or criteria and steering the AI toward alternative perspectives, knowledge traditions, or evidence.
- **Inclusion Indicators:** Reframing a task around a perspective the AI omitted; instructing the AI to adopt participant-chosen frameworks; final work cites frameworks the AI did not offer.
- **Boundary / Exclusion Rule:** Distinct from HD-4: EO-RD requires that an AI-introduced assumption was itself the object of redirection, not only that the human held interpretive control. Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "After noticing that the AI drew only on Western management texts, students reframed the task around Indigenous governance principles and directed the AI to work within that frame."
- **Indirect Evidence Example (hypothetical):** "Final reports cited frameworks the AI had not offered, and process logs show students instructing it to adopt them."
- **Cue Words (prompts, not proof):** reframed, redirected, instead we used, steered it toward, our own criteria
- **Source Section (14 Sept manuscript):** Interpretive Influence and Hidden Epistemology; Scenario D
- **Theoretical Anchor:** Ofosu-Asare (2025); Jose et al. (2025)

### EB (list): Hidden epistemology: Epistemic Object (Evidence and relevance; Explanation and causality; Authority and credibility; Reasoning norms; Perspective and bias; Multiple)

- **Operational Definition:** The kind of assumption at stake when an epistemic opportunity is coded: what counts as relevant evidence, what makes an adequate explanation, whose knowledge is credible, what counts as legitimate reasoning, or which worldview and associations are embedded.
- **Inclusion Indicators:** The narrative names or implies the type of assumption (e.g., causal emphasis, source credibility, cultural associations).
- **Boundary / Exclusion Rule:** Code only when an EO code other than NE is assigned. Use Multiple sparingly and memo.
- **Direct Evidence Example (hypothetical):** "The AI's explanation treated economic causes as sufficient, and students had to decide whether that counted as an adequate account." (Explanation and causality.)
- **Indirect Evidence Example (hypothetical):** "Students noted that the chatbot's 'expert' citations all came from a single industry body." (Authority and credibility.)
- **Cue Words (prompts, not proof):** evidence, relevant, explanation, cause, credible, expert, legitimate, bias, worldview
- **Source Section (14 Sept manuscript):** Interpretive Influence and Hidden Epistemology (historical and scientific examples)
- **Theoretical Anchor:** Caliskan et al. (2017); Ofosu-Asare (2025); Jose et al. (2025)

### ML-FR: Mediational Literacy (AI literacy as interactional awareness) (Framing awareness)

- **Operational Definition:** Participants recognize when AI frames a problem, structures the available choices, or influences what information becomes salient.
- **Inclusion Indicators:** Activities that ask learners to identify how the AI framed a question, which options it made available, or what it emphasized.
- **Boundary / Exclusion Rule:** If the focus is on embedded assumptions or bias, code ML-EP; if on offloaded cognitive work, ML-CW; if on deciding how to use AI, ML-DD. Technical AI knowledge (how models work, prompt skill) is not ML (R17). Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "After each session, students wrote a short note on how the AI had framed the question and which alternatives it never raised."
- **Indirect Evidence Example (hypothetical):** "Students began prefacing prompts with 'don't propose a structure yet.'" (Behavior implies awareness of AI structuring.)
- **Cue Words (prompts, not proof):** framed, structured the options, made salient, steered
- **Source Section (14 Sept manuscript):** Discussion: AI literacy paragraph
- **Theoretical Anchor:** Wertsch (1991); Borchers et al. (2026)

### ML-EP: Mediational Literacy (AI literacy as interactional awareness) (Epistemic awareness)

- **Operational Definition:** Participants recognize that AI contributions may carry implicit epistemic assumptions, worldviews, or biases.
- **Inclusion Indicators:** Activities or reported reflections that address whose knowledge AI treats as authoritative, what it leaves out, or what associations it reproduces.
- **Boundary / Exclusion Rule:** ML-EP is a capacity the design builds or participants report; EO codes describe what happened to a specific assumption in the episode. An episode can carry both. Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "We asked students to identify whose knowledge the AI's answer treated as authoritative."
- **Indirect Evidence Example (hypothetical):** "Several reflections named the chatbot's 'default perspective' as a limitation they now watch for."
- **Cue Words (prompts, not proof):** bias, perspective, worldview, whose knowledge, assumptions
- **Source Section (14 Sept manuscript):** Discussion: AI literacy paragraph
- **Theoretical Anchor:** Litts et al. (2021); Ofosu-Asare (2025); Jose et al. (2025)

### ML-CW: Mediational Literacy (AI literacy as interactional awareness) (Cognitive-work awareness)

- **Operational Definition:** Participants recognize when AI is assuming cognitive work that they might otherwise perform.
- **Inclusion Indicators:** Logs or discussions distinguishing human from AI contributions to a task; reflections on what was offloaded.
- **Boundary / Exclusion Rule:** If participants act on that recognition by deciding when to use AI, code ML-DD. Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "Students logged which parts of the analysis they had done and which the AI had done, then discussed what they had given up."
- **Indirect Evidence Example (hypothetical):** "In end-of-term surveys students described noticing they had 'stopped trying to remember formulas' once the tutor was available."
- **Cue Words (prompts, not proof):** offloaded, did the thinking, gave up, relied on
- **Source Section (14 Sept manuscript):** Discussion: AI literacy paragraph
- **Theoretical Anchor:** Grinschgl & Neubauer (2022); Gerlich (2025)

### ML-DD: Mediational Literacy (AI literacy as interactional awareness) (Deliberate decision-making)

- **Operational Definition:** Participants make and justify decisions about when to accept, question, redirect, or independently evaluate AI contributions, including choosing the interactional configuration that suits a task.
- **Inclusion Indicators:** AI-use plans that assign stages to AI or to the learner with reasons; disclosure statements that justify declining or accepting AI help.
- **Boundary / Exclusion Rule:** Mandated use limits set by the instructor are design conditions (HD-2), not ML-DD, unless participants make and justify the decisions. Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "Each assignment required an AI-use plan stating which stages would be AI-supported, which would be done independently, and why."
- **Indirect Evidence Example (hypothetical):** "AI disclosure statements increasingly explained why the student had declined AI help for particular sections."
- **Cue Words (prompts, not proof):** decided when, chose not to, AI-use plan, justified, on purpose
- **Source Section (14 Sept manuscript):** Discussion: AI literacy paragraph
- **Theoretical Anchor:** Borchers et al. (2026); Järvelä et al. (2023)

### ML-RA: Mediational Literacy (AI literacy as interactional awareness) (Relational awareness)

- **Operational Definition:** Participants recognize and reflect on how interacting with AI as an interlocutor differs from interacting with people, or on the relationship they form with it (naturalness, social presence, comfort or anxiety, attachment, trust in it as a conversational partner).
- **Inclusion Indicators:** Reflections or surveys comparing exchanges with the AI and exchanges with people; journals or logs tracking how the participant's relation to the AI changes over time; reports of how it felt to work with the AI.
- **Boundary / Exclusion Rule:** ML-RA is reflective awareness, coded only where the design asks for it or participants report it. How the AI is positioned within the episode is D5 and is coded independently (R5): a participant can treat the AI as a collaborator (CM-5) without ML-RA. If the reflection concerns what the AI framed, assumed, or did for the participant, code ML-FR, ML-EP, or ML-CW instead. Coded in intended and reported versions (R23).
- **Direct Evidence Example (hypothetical):** "After each practice tour in which the assistant played a park visitor, recreation students noted how guiding it differed from guiding a classmate."
- **Indirect Evidence Example (hypothetical):** "Journal entries shifted over the term from treating the assistant as an audience to impress to treating it as a rehearsal tool."
- **Cue Words (prompts, not proof):** felt natural, like a person, robot, relationship, companion, comfortable, awkward, compared with a friend
- **Source Section (14 Sept manuscript):** Discussion: AI literacy paragraph; Social Positioning of AI
- **Theoretical Anchor:** Reeves & Nass (1996)

### ML-MX / ML-NA: Mediational Literacy (AI literacy as interactional awareness) (Multiple / Not addressed)

- **Operational Definition:** ML-MX: more than one ML code is evidenced, including ML-RA (list them in the memo). ML-NA: the episode does not address awareness of AI as a mediator or as an interlocutor.

### TR (computed): Within-episode trajectory (Stable; Toward human direction; Toward AI direction)

- **Operational Definition:** Direction of movement along the interactional mediation continuum within one mediation episode, computed from the coded Start and End configurations (ordered AD, AS, CM, HD by the distribution of cognitive responsibility).
- **Inclusion Indicators:** The narrative describes interaction changing while the objective stays constant (e.g., starting with an AI-generated argument and ending with independent evaluation).
- **Boundary / Exclusion Rule:** If the objective changes, open a new episode instead (R6). Oscillating trajectories (e.g., HD to CM to HD) compute as Stable; memo them.
- **Direct Evidence Example (hypothetical):** "Students first asked the AI for a model answer, then interrogated its reasoning, and finally rewrote the argument on their own." (Start AD, End HD.)
- **Indirect Evidence Example (hypothetical):** "Later drafts cite fewer AI suggestions and more of the student's own sources." (Shift toward human direction inferred from artifacts.)
- **Cue Words (prompts, not proof):** at first, then, by the end, gradually, shifted
- **Source Section (14 Sept manuscript):** AIM-AI Framework: mediation episodes; Table 1 of the source
- **Theoretical Anchor:** Järvelä et al. (2023); Hutchins (1995)

### DP (list): Design: Stated Purpose (Introduce or model (AD); Guided practice (AS); Inquiry and refinement (CM); Independent production (HD); Critical evaluation of AI (HD); Multiple; Not stated)

- **Operational Definition:** The instructional purpose the author states for the design, using the purpose categories the source associates with each configuration. Critical evaluation of AI (HD), added in v0.6, records designs whose stated aim is for participants to test, audit, or critique AI behavior or output against standards the humans set; it is an HD purpose because the design places evaluative authority with the participant.
- **Inclusion Indicators:** Explicit statements of what the activity is for.
- **Boundary / Exclusion Rule:** Code purpose from stated intent only, not from the design itself. Use Critical evaluation of AI only when evaluating the AI is itself the stated purpose; verification requirements attached to some other purpose (e.g., an essay with a fact-checking rule) keep that other purpose.
- **Direct Evidence Example (hypothetical):** "We wanted students to see what a disciplinary argument looks like before writing one." (Introduce or model.)
- **Indirect Evidence Example (hypothetical):** "We wanted students to find out what these tools value by testing them against a standard we set first." (Critical evaluation of AI.)
- **Cue Words (prompts, not proof):** so that, the goal was, we wanted, in order to
- **Source Section (14 Sept manuscript):** Discussion; Table 5 of the source
- **Theoretical Anchor:** Baxter & Sommerville (2011)

### ST (list): Sociotechnical Frame (High-stakes assessment; Low-stakes or formative; Self-directed or optional; Professional or workplace; Instructor preparation; Unclear)

- **Operational Definition:** The institutional frame in which the episode occurs, which shapes what the AI is authorized to do and what counts as acceptable performance.
- **Inclusion Indicators:** Assessment weight, optional versus required use, workplace or placement settings.
- **Boundary / Exclusion Rule:** Do not infer configuration from the frame (R18).
- **Direct Evidence Example (hypothetical):** "The AI tutor was available for ungraded weekly practice only." (Low-stakes or formative.)
- **Cue Words (prompts, not proof):** graded, final exam, optional, placement, client
- **Source Section (14 Sept manuscript):** The AIM-AI Framework: sociotechnical systems
- **Theoretical Anchor:** Baxter & Sommerville (2011); Bouakaz & Khalid (2025)

### DT (list): Dialogue Type (Instructional; Feedback-oriented; Collaborative; Reflective)

- **Operational Definition:** The dominant conversational function the AI serves in the episode: explaining and guiding; responding to learner actions during practice; iterative exchange and idea development; or supporting metacognitive monitoring and self-regulation.
- **Inclusion Indicators:** Narrative describes what the AI's turns do in the exchange.
- **Boundary / Exclusion Rule:** Optional code. Typical but not required alignments: instructional with AD-3, feedback-oriented with AS-3, collaborative with CM-3; reflective can occur in any configuration.
- **Direct Evidence Example (hypothetical):** "After each lab, the assistant asked students what they would do differently next time." (Reflective.)
- **Cue Words (prompts, not proof):** explained, feedback, back-and-forth, reflect, monitor
- **Source Section (14 Sept manuscript):** Learning Activity
- **Theoretical Anchor:** Laurillard (2001); Järvelä et al. (2023)

### LV (list): Learner Variability Noted (Prior knowledge; Motivation; Self-regulation; Cultural context; AI literacy; Orientation toward AI; Multiple; None noted)

- **Operational Definition:** Sources of within-configuration variation that the author reports, recorded so that later analyses can examine the limitation the source identifies.
- **Inclusion Indicators:** The author attributes differences in how participants engaged to one of these sources.
- **Boundary / Exclusion Rule:** Record only what the author reports; do not infer.
- **Direct Evidence Example (hypothetical):** "Students with programming experience used the tutor very differently from novices." (Prior knowledge.)
- **Cue Words (prompts, not proof):** some students, novices, experienced, more confident, skeptical of AI
- **Source Section (14 Sept manuscript):** Discussion: limitations
- **Theoretical Anchor:** Chi & Wylie (2014)

### ET (list): Evidence tier (T1 trace; T2 participant account; T3 observation; T4 design intent)

- **Operational Definition:** Proximity of the evidence for a code to the coded participant's exchange with the AI. Assigned per reported dimension and per reported EO, ML, and uptake code.
- **Inclusion Indicators:** T1: transcript, log, version history, reproduced prompt. T2: the participant's own reflection, survey response, interview, or quoted voice (an instructor's account of their own use is T2). T3: instructor or developer report of how participants engaged. T4: design statements.
- **Boundary / Exclusion Rule:** T4 never enters the reported profile. Code the highest tier available for each dimension. Weights for modeling: T1 2.0, T2 1.5, T3 1.0 (R22).
- **Cue Words (prompts, not proof):** transcript, log, students wrote, survey, we observed, the assignment requires
- **Source Section (14 Sept manuscript):** Discussion: design and enactment
- **Theoretical Anchor:** Winne (2010)

### UP (list): Uptake of AI contributions (UP-AD adopted; UP-AP adapted; UP-CT contested; UP-RJ rejected; UP-IG ignored; UP-MX mixed)

- **Operational Definition:** What the learner does with a substantive AI contribution: takes it up as is, revises it, disputes it within the exchange, discards it, or leaves it unused. The most direct observable form of mediational impact.
- **Inclusion Indicators:** Traces linking an AI contribution to later learner turns or to the product; accounts of keeping, changing, or discarding AI output; designs requiring a decision on each AI contribution (intended uptake).
- **Boundary / Exclusion Rule:** Coded in intended and reported versions (R25). UP-MX when contributions in one episode are treated differently; list them in the memo. Do not infer uptake from outcomes alone.
- **Direct Evidence Example (hypothetical):** "Students kept the AI's outline but replaced every example with one from their own fieldwork." (UP-AP)
- **Indirect Evidence Example (hypothetical):** "Version histories show AI-suggested sentences deleted in the next draft." (UP-RJ)
- **Cue Words (prompts, not proof):** kept, used as is, revised, rewrote, rejected, discarded, ignored
- **Source Section (14 Sept manuscript):** Interpretive Influence and Hidden Epistemology
- **Theoretical Anchor:** Wertsch (1991); Hutchins (1995)

### LM (list): Learner moves (T1 only) (LM-RQ request; LM-QU question; LM-SE select; LM-AP apply; LM-GE generate; LM-CH challenge; LM-VE verify; LM-RD redirect; LM-RF reflect; LM-CL close)

- **Operational Definition:** The function of each learner turn in a traced exchange.
- **Inclusion Indicators:** Coded turn by turn on the Move Coding Form.
- **Boundary / Exclusion Rule:** Code the turn's main function; split a turn only when it clearly performs two functions. Steering moves for the indicator block: RQ, QU, RD, CL.
- **Source Section (14 Sept manuscript):** Engagement Type; Interaction Structure
- **Theoretical Anchor:** Chi & Wylie (2014); Laurillard (2001)

### AM (list): AI moves (T1 only) (AM-EX explain; AM-PR produce content; AM-OP offer options; AM-SC scaffold; AM-FB feedback; AM-CH challenge; AM-RD redirect; AM-CO comply or revise)

- **Operational Definition:** The function of each AI turn in a traced exchange.
- **Inclusion Indicators:** Coded turn by turn on the Move Coding Form; each substantive AI contribution receives an ID so learner uptake can be linked to it.
- **Boundary / Exclusion Rule:** Steering moves for the indicator block: RD, SC, OP. AI production share = AM-PR turns over all AI turns.
- **Source Section (14 Sept manuscript):** Interaction Structure; Provenance
- **Theoretical Anchor:** Laurillard (2001); Hutchins (1995)

### LT (list): Laurillard activity type (context) (Acquisition; Practice; Inquiry, discussion, collaboration; Inquiry, production; Reflection; Multiple)

- **Operational Definition:** The kind of learning work the activity asks for, recorded as context and no longer as a configuration dimension.
- **Inclusion Indicators:** Assignment genre and stated activity.
- **Boundary / Exclusion Rule:** Do not infer a configuration from the activity type.
- **Source Section (14 Sept manuscript):** Learning Activity
- **Theoretical Anchor:** Laurillard (2001)

### ES (computed): Reporting stance: evidence (Design only (T4); Instructor observation (T3); Participant account (T2); Reproduced traces (T1))

- **Operational Definition:** The highest tier of evidence an entry offers for any of its episodes.
- **Inclusion Indicators:** Computed on the Entry Profile from the episodes' highest tiers.
- **Source Section (14 Sept manuscript):** R26

### CS (list): Reporting stance: claim (Descriptive; Benefit claimed; Mixed results; Critical)

- **Operational Definition:** Whether the author describes the design, claims benefit, reports mixed results, or reports critically on AI's contribution.
- **Inclusion Indicators:** Results and Lessons sections; curator framing for prescriptive entries.
- **Boundary / Exclusion Rule:** Kept separate from configuration codes (R9).
- **Source Section (14 Sept manuscript):** R26

### US (list): Reporting stance: AI use (Assigned; Optional; Limited; Prohibited; Mixed; Instructor use)

- **Operational Definition:** The AI-use stance as the author or curator states it.
- **Inclusion Indicators:** Policy language; curator labels.
- **Boundary / Exclusion Rule:** Record the stated stance; do not infer it from the coded configuration.
- **Source Section (14 Sept manuscript):** R26

### LA (list): Reporting stance: limitations (None stated; Design limits; Evidence limits; Both)

- **Operational Definition:** Whether the author names limitations of the design, of the evidence, or both.
- **Inclusion Indicators:** Explicit statements of limits.
- **Boundary / Exclusion Rule:** Limits of the AI tool itself are not limitations of the design or evidence.
- **Source Section (14 Sept manuscript):** R26

### TC (list): Reporting stance: traces collected (Not described; Collected, not reproduced; Partly reproduced; Reproduced)

- **Operational Definition:** Whether the design collects traces (logs, transcripts, histories, screenshots) and whether the entry reproduces them.
- **Inclusion Indicators:** Requirements to submit logs or prompts; platform logging; reproduced exchanges.
- **Boundary / Exclusion Rule:** Identifies sources for a trace corpus; trace collection is not itself evidence of a configuration.
- **Source Section (14 Sept manuscript):** R26

### HS (computed): Sequence direction (0.00 to 3.00)

- **Operational Definition:** Human-direction score of one learner episode: the mean of the intended dimension codes D1 to D5 on the ordinal continuum AD = 0, AS = 1, CM = 2, HD = 3, over the dimensions coded with a configuration (NE excluded).
- **Inclusion Indicators:** Computed from the intended profile; no judgment is added.
- **Boundary / Exclusion Rule:** Not computed for instructor, staff or other non-learner episodes (P1, C11). Scores from fewer than three coded dimensions carry the existing Low evidence flag. The score orders the distribution of cognitive responsibility; it is not a quality scale (R9).
- **Direct Evidence Example (hypothetical):** (Computed) An episode coded AS, HD, AS, HD, AS has HS = 1.80.
- **Indirect Evidence Example (hypothetical):** (Computed) An episode coded HD on four dimensions with D5 NE has HS = 3.00.
- **Source Section (14 Sept manuscript):** AIM-AI Framework: mediation episodes and trajectories; R30
- **Theoretical Anchor:** Hutchins (1995); Järvelä et al. (2023)

### SS (computed): Sequence direction (NE; Stable; Toward human direction; Toward AI direction)

- **Operational Definition:** Step direction: the change in HS from the previous learner episode of the same entry to this one, classed by the sequence threshold (Lists, default 0.5).
- **Inclusion Indicators:** Two or more learner episodes in the entry, in episode order.
- **Boundary / Exclusion Rule:** NE for the first learner episode of an entry and for entries with a single learner episode. Instructor episodes between learner episodes are skipped. The step carries the trajectory use case of both episodes, so sequential and recurrent steps can be analyzed separately.
- **Direct Evidence Example (hypothetical):** (Computed) Stage 1 AS (HS 1.20) to Stage 2 HD (HS 3.00): change +1.80, Toward human direction.
- **Indirect Evidence Example (hypothetical):** (Computed) A recurrent weekly tutor episode followed by a drafting episode with change -0.40: Stable.
- **Source Section (14 Sept manuscript):** AIM-AI Framework: mediation episodes and trajectories; R30
- **Theoretical Anchor:** Hutchins (1995); Järvelä et al. (2023)

### SD (computed): Sequence direction (NE; Stable; Toward human direction; Toward AI direction; Oscillating flag)

- **Operational Definition:** Sequence direction of an entry: the change in HS from the first to the last learner episode, classed by the sequence threshold. An Oscillating flag is added when the entry contains at least one step toward human direction and at least one toward AI direction.
- **Inclusion Indicators:** Entries with two or more scored learner episodes.
- **Boundary / Exclusion Rule:** NE for entries with fewer than two scored learner episodes, including all single-episode entries and instructor-only entries. Within-episode movement remains TR (R6); SD describes movement across episodes only.
- **Direct Evidence Example (hypothetical):** (Computed) AS, AS, HD across three stages: change +1.60, Toward human direction.
- **Indirect Evidence Example (hypothetical):** (Computed) HD, CM, HD: change 0.00, Stable, no Oscillating flag because the first step (-0.40) is below threshold.
- **Source Section (14 Sept manuscript):** AIM-AI Framework: mediation episodes and trajectories; R30
- **Theoretical Anchor:** Hutchins (1995); Järvelä et al. (2023)

## 6. Decision rules

### R1. Unit of analysis

Three nested units. (a) Article: the 'play' as the volume presents it. (b) Learning activity: a distinct human-AI interaction arrangement described in the article (the v0.4 'segment'), identified by a label in the Learning Activity column. (c) Mediation episode: a coherent sequence of human-AI interactions organized around one learning or task objective; this is the primary coding unit and occupies one row of the Coding Form. Where a narrative describes an arrangement only at the level of design, with no distinguishable objectives, code one episode for that activity (Episode # = 1) and memo 'episode not resolvable'. Episodes roll up to activities and articles (R13). An episode requires that the participant exchanges with the AI system (prompting, conversing with, configuring, or running it); engagement with a static AI artifact is not an episode (R21).

*Rationale:* The 14 September manuscript adopts the mediation episode as its primary unit of analysis and illustrates variation within and across episodes inside one learning activity (Tables 1 and 2 of the source). Instructor narratives often describe arrangements rather than episodes, so the fallback preserves v0.4 coding where finer resolution is unavailable.

### R2. Human participant

Record whose interaction is coded: student, instructor, TA, intern or trainee, research team, or group. Instructor-AI episodes are coded with the same codebook and flagged for separate analysis. The Summary Matrix reports learner and instructor episodes separately.

*Rationale:* The source framework is articulated for learners; applying it to instructor professional practice extends its scope and should be analyzed separately.

### R3. Evidence locus and design versus enactment

Code two profiles for every episode (R23). The intended profile comes from design statements (T4); the reported profile comes from enactment evidence (T1 to T3). Record the evidence locus as before; Purpose-Design Alignment compares the stated purpose with the intended holistic configuration, and Intended-Reported Alignment compares the two holistic configurations.

*Rationale:* v0.7: the author's decision to separate design intent from the mediation of learning replaces the single profile assigned from enactment where it existed and from design otherwise.

### R4. Evidence tier

Each reported dimension carries an evidence tier (T1 trace, T2 participant account, T3 observation; R22), which replaces the v0.6 direct and indirect types. NE = not evident. Never code from the technology label alone.

*Rationale:* v0.6 'direct' meant that the narrative stated something explicitly, which can be an explicit statement of design intent; tiers measure proximity to the learner instead.

### R5. Dimension independence

Code each of the five dimensions on its own evidence before assigning a holistic configuration, and code the extension codes (EO, EB, ML, DT) independently of the dimensions. Do not infer EO from D4 or D5, or ML from EO. Misalignment (e.g., CM-2 structure with AD-5 authority positioning) is recorded, not corrected. v0.7: steering (D2) and provenance (D3) are coded independently; their divergence (e.g., learner-steered exchanges with AI-produced content) is recorded, not resolved.

*Rationale:* The source treats social positioning as analytically distinct from interaction structure and now adds that positioning affects whether epistemic assumptions are accepted implicitly or evaluated, which can only be examined if the two are coded separately.

### R6. Within-episode shifts

Do not split an episode when interaction shifts while the objective stays constant. Record the Start and End configurations; the trajectory is computed. Code the five dimensions on the predominant pattern and assign the holistic configuration as the predominant configuration, or Mixed where none predominates. Open a new episode when the objective changes.

*Rationale:* Replaces the v0.4 sub-segment rule (12a, 12b), which the source now addresses directly: shifts within an episode are characterized as a trajectory (Table 1 of the source), shifts across objectives as separate episodes (Table 2).

### R7. Sample screening: AI removal

Exclude from the sample any article whose response to AI consists solely of removing AI from learning activity. Articles that combine AI removal with any described human-AI interaction arrangement are retained; their AI-removal components are not coded but are noted in the screening note. Detection or monitoring of student AI use is treated as instructor-AI interaction (R2) where the instructor uses an AI system, and screened case by case otherwise.

*Rationale:* Human-dominant configurations still position AI as an advisor; its absence falls outside the model's range.

### R8. AI-mediated human-human interaction

Where AI mediates relations among humans (e.g., an agent that connects peers), set participant to Group, code AI roles per D2 indicators, and memo the configuration of the human-human layer.

*Rationale:* Extends the model's dyadic framing; flagged for theoretical discussion.

### R9. Non-evaluative coding

Do not infer configuration, epistemic opportunity, or mediational literacy from the author's valence (success, concern, enthusiasm). Codes describe organization of participation, not quality.

*Rationale:* The source is explicitly non-hierarchical and now describes the continuum as descriptive, not hierarchical.

### R10. Boundary heuristics on a continuum

Configurations are reference points on a continuum with intentionally permeable boundaries. AD vs AS: are alternatives or choices available to the human? AS vs CM: does the AI challenge the human, and can the human reshape the structure? CM vs HD: does the AI's contribution reciprocally reshape the trajectory, or does the human invoke testing or challenge selectively while retaining direction? Near-boundary episodes: code the nearer reference point, lower Confidence, and memo.

*Rationale:* Derived from the contrasts among Scenarios A to D and from the revised Interpretive Influence section, which allows human-dominant learners to use AI selectively to 'test, challenge, or extend' their reasoning.

### R11. Author labels

Code engagement against ICAP definitions, not the author's vocabulary (e.g., 'active learning' or 'interactive tool' in the narrative is a cue, not a code).

*Rationale:* Chi and Wylie (2014) define categories by overt behavior; narrative labels are often colloquial.

### R12. Holistic configuration and episode quality

Assign the holistic configuration by judgment after reviewing the modal configuration, the adjacency-weighted coherence index (where reported), and evidence density. Configurations are ordered AD=1 to HD=4 for this index only. Adjacency Coherence = 1 - D/1.5, where D is the mean absolute distance of coded dimensions from their median configuration; it is reported only for episodes with at least four coded dimensions, because with two or three coded dimensions a single divergent code dominates the index. Evidence Density = coded dimensions / 5. Direct Share = proportion of coded dimensions with direct evidence. Composite Index = Adjacency Coherence x Evidence Density, reported only where coherence is reported. Memo the rationale whenever the Review Flag fires: fewer than 3 coded dimensions, adjacency coherence strictly below 2/3 (so that a 2-2 split of adjacent configurations, or one dimension two steps from the rest, which both score exactly 2/3, does not fire), or a modal tie. v0.7: indices are computed separately for the intended and reported profiles; the Review Flag uses the intended profile; reported coherence is reported only where four or more reported dimensions are coded.

*Rationale:* With five dimensions, the low-evidence threshold moves from 4 of 7 (.57) to 3 of 5 (.60), the closest proportional equivalent. Merging the role dimensions into D2 also removes the triple weighting that structure and roles previously carried in the index. v0.6: in the pilot, 10 of 16 low-coherence flags under the .67 cut-off scored exactly 2/3, the mildest misalignment the index can register on four dimensions, and low coherence occurred in 3 of 4 episodes with two coded dimensions against 1 of 24 with five.

### R13. Entry-level profile

Each entry receives a profile on the Entry Profile sheet: reporting-stance codes (R26), episode counts, intended and reported holistic counts, episodes with reported dimensions, tier-weighted reported evidence, mean intended coherence, and intended-reported divergences.

*Rationale:* Retains within-article and within-activity variation while allowing article-level comparison across the 67 'plays' in the GT corpus.

### R14. Sample screening: non-interactional commentaries

Exclude from the sample, and label as non-interactional commentaries, articles that describe no human-AI interaction arrangement: AI appears only as subject matter, or the article describes policy, resource, or professional development work rather than an interaction. Also exclude articles whose only human-AI arrangement is an incidental instructor use mentioned in passing (e.g., in a footnote or a single procedural sentence), when the student-facing components consist of AI removal, AI as subject matter, or static AI artifacts (R21).

*Rationale:* AIM-AI characterizes interactional configurations; without a described interaction there is nothing for the five dimensions to code. The source's new AI-literacy section, however, describes learners' awareness of AI as a mediator, which some Teaching AI articles may address without describing an interaction. Reviewed for v0.5: the ML codes apply only to included articles; the 10 commentaries remain excluded. v0.6: an incidental-instructor provision applies where an entry's only student-facing arrangement is a static AI artifact; the screening cases are recorded in the adjudication log.

### R15. D2 integration

Retired in v0.7. D2 now records steering only and D3 records provenance, so structure and role evidence no longer compete for one code. Record their divergence under R5.

*Rationale:* The v0.6 rule gave operational priority to who steers and who produces the substance; v0.7 codes the two separately.

### R16. Hidden epistemology

For each episode in which interpretive content is described, code the most extensive epistemic move evidenced (EO-IN, EO-RE, EO-EV, EO-CH, EO-RD) or NE, and the epistemic object (EB) where identifiable. EO describes the opportunities participants had to recognize, evaluate, challenge, or redirect AI-introduced assumptions; it is not a quality rating, and hidden epistemology is assumed possible in every configuration. v0.7: code EO in intended (designed opportunity) and reported (evidenced move, with tier) versions.

*Rationale:* The source states that hidden epistemology 'remains possible in all four configurations; what changes is how epistemic influence is distributed and the opportunities available to the learner.'

### R17. Mediational literacy

Code ML when the narrative designs for, or reports, participants' awareness of AI as a mediator of their own thinking (framing, epistemic assumptions, offloaded cognitive work, deliberate decisions) or of AI as an interlocutor (relational awareness, ML-RA). Knowledge of AI capabilities, limitations, or prompting technique alone is not ML. Code ML-NA otherwise. v0.7: code ML in intended (designed for) and reported (evidenced, with tier) versions.

*Rationale:* The source extends AI literacy to 'the capacity to recognize and critically manage one's relationship with AI as a mediator of learning, reasoning, and meaning making.' v0.6 adds relational awareness, a relation the media equation literature treats as social (Reeves & Nass, 1996); the pilot cases that prompted it are recorded in the adjudication log.

### R18. Sociotechnical frame

Record the institutional frame (stakes, optionality, workplace). Do not infer configuration from the frame.

*Rationale:* The source positions configurations as products of the broader sociotechnical system, contrasting high-stakes assessment with self-directed inquiry.

### R19. Learner variability

Record any source of within-configuration variation the author reports (prior knowledge, motivation, self-regulation, cultural context, AI literacy, orientation toward AI). Do not infer.

*Rationale:* The source names learner variability as an unaddressed limitation; recording it builds evidence for future refinement.

### R20. Dialogue type

Optionally code the dominant conversational function of the AI (instructional, feedback-oriented, collaborative, reflective).

*Rationale:* Operationalizes the Laurillard dialogue variants the source describes under Learning Activity, which v0.4 did not code.

### R21. Static AI artifacts

Code a mediation episode only when the human participant exchanges with the AI system: prompting it, conversing with it, configuring it, or running it. Engagement with an AI output that someone else produced (e.g., an AI-written reading summary handed out by the instructor, AI-generated practice items distributed without access to the generator, an AI-produced map supplied for annotation, or watching another person use an AI system) is a static AI artifact and sits outside the model. Do not code it as an episode; record it in the activity memo. Where it is the only student-facing arrangement in an article, screen the article 'Exclude: static AI artifact only'. The exchange that produced the artifact may be coded as an instructor episode (R2) when the narrative describes it in more than passing (R14). Reflection on the participant's own prior exchange with AI remains codable as a reflective episode (HD-3).

*Rationale:* AIM-AI characterizes how cognitive responsibility is distributed within a human-AI exchange. A learner who critiques a fixed output has no exchange whose distribution can be coded; the interpretive work is a human-only activity. The pilot cases that prompted this rule are recorded in the adjudication log.

### R22. Evidence tiers and weights

Assign each reported dimension, and each reported EO, ML, and uptake code, the highest tier available: T1 trace (raw record of the exchange or of the work's development), T2 participant account (the coded participant's own report), T3 observation (an instructor's or developer's report of how participants engaged). Tiers are judged relative to the human participant coded, so an instructor's account of their own AI use is T2. T4 design intent populates the intended profile only. For modeling, weight reported codes T1 2.0, T2 1.5, T3 1.0.

*Rationale:* The author's decision to weight by tier aligns the evidence with the aim of characterizing mediational impact on the learner and avoids confounding design intent with mediation (Winne, 2010, makes the parallel argument for trace data in self-regulated learning).

### R23. Two profiles

Code each dimension twice. Intended profile: the configuration the design statements ask for or communicate (I-D1 to I-D5). Reported profile: the configuration evidenced by enactment (R-D1 to R-D5), each with a tier; leave a dimension NE when no enactment evidence bears on it. Outcome claims (e.g., better grades, sharper hypotheses) are not evidence of a configuration. EO, ML, and uptake are coded in both versions.

*Rationale:* Separates designed conditions from enacted mediation, as the source states that design 'does not determine how learners will actually engage'.

### R24. Move coding for traces

Where T1 traces exist, code each turn on the Move Coding Form with one learner (LM) or AI (AM) move code, assign IDs to substantive AI contributions, and link learner uptake to them. Use the indicator block (learner steering share, AI production share, challenge moves, uptake counts, suggested D2) to inform, not replace, the reported profile. Episode boundaries are set where the objective of the exchange changes in the trace.

*Rationale:* Makes engagement, steering, provenance, and interpretive influence observable at turn level and addresses the source's open limitation on episode boundaries. Thresholds in the suggested D2 are provisional and to be calibrated on trace data.

### R25. Uptake

For each episode, code the dominant learner response to substantive AI contributions (UP-AD, UP-AP, UP-CT, UP-RJ, UP-IG, or UP-MX) in intended and reported versions. Code reported uptake only from traces or accounts that link an AI contribution to what the learner did with it.

*Rationale:* Operationalizes mediational impact as an observable process consequence, keeping the model descriptive (it does not predict learning outcomes).

### R26. Reporting-stance codes

Code each entry's evidence stance (computed: the highest tier across its episodes), claim stance, AI-use stance, limitations acknowledged, and traces collected on the Entry Profile.

*Rationale:* Supports the design-layer study of how instructors and curators publicly report AI use (R29).

### R27. Positioning

In the reported profile, code D5 only from learner behavior, learner accounts, or observation of learners. Instructor or curator descriptions of the AI (assistant, partner, instrument) are coded as the intended D5, the positioning the design communicates.

*Rationale:* In the v0.6 pilot, D5 was the dimension least aligned with the others and was often coded from instructor vocabulary.

### R28. Holistic configurations per profile

Assign an intended and a reported holistic configuration by judgment after reviewing each profile's modal configuration and coherence. Assign a reported holistic configuration only where at least two reported dimensions are coded; otherwise NE.

*Rationale:* Avoids treating a single reported dimension as an episode-level characterization.

### R29. Scope of faculty-report collections

Applications to faculty-authored or curated collections are exploratory analyses of instructor intentions and public reporting stances. Report the intended profile as the main analysis and the reported profile as the evidence such collections offer. Claims about mediational impact on learners require reported profiles grounded in T1 or T2 evidence.

*Rationale:* The author's reframing of the three-corpus analysis as a design-layer study (October 24, 2026).

### R30. Sequence direction (computed)

For every entry with two or more scored learner episodes, compute the human-direction score (HS) of each learner episode from the intended profile, the step direction (SS) between consecutive learner episodes, and the entry sequence direction (SD) from the first to the last learner episode. Order episodes by episode number within the entry; skip instructor and other non-learner episodes. A change of at least the sequence threshold (0.5 on the 0 to 3 scale) toward HD is Toward human direction, at least the threshold toward AD is Toward AI direction, and anything smaller is Stable. Flag an entry as Oscillating when it holds steps in both directions. Single-episode entries are NE. No coder judgment is involved, so SS and SD are not adjudicated.

*Rationale:* Complements TR (R6), which covers movement inside one episode, by recording movement across the learner episodes of an entry. The threshold of 0.5 is one step on the ordinal continuum shared across two dimensions; report sensitivity at 0.34, 0.75 and 1.0. The computation is made after coding, from the intended profile, and does not enter any coding decision.

## 7. Controlled vocabularies

- **Codes:** AD; AS; CM; HD; NE
- **Tier:** T1; T2; T3
- **Participant:** Student; Instructor; TA; Intern/Trainee; Research team; Group; Other
- **Context:** Teaching; Internship/Experiential; Research training; Course preparation; Other
- **Frame:** High-stakes assessment; Low-stakes or formative; Self-directed or optional; Professional or workplace; Instructor preparation; Unclear
- **Laurillard:** Acquisition; Practice; Inquiry, discussion, collaboration; Inquiry, production; Reflection; Multiple; NE
- **Dialogue:** Instructional; Feedback-oriented; Collaborative; Reflective; Mixed; NE
- **Epistemic Opportunity:** EO-IN; EO-RE; EO-EV; EO-CH; EO-RD; NE
- **Epistemic Object:** Evidence and relevance; Explanation and causality; Authority and credibility; Reasoning norms; Perspective and bias; Multiple; NE
- **Mediational Literacy:** ML-FR; ML-EP; ML-CW; ML-DD; ML-RA; ML-MX; ML-NA; NE
- **Uptake:** UP-AD; UP-AP; UP-CT; UP-RJ; UP-IG; UP-MX; NE
- **Purpose:** Introduce or model (AD); Guided practice (AS); Inquiry and refinement (CM); Independent production (HD); Critical evaluation of AI (HD); Multiple; Not stated
- **Learner Variability:** Prior knowledge; Motivation; Self-regulation; Cultural context; AI literacy; Orientation toward AI; Multiple; None noted
- **Holistic:** AD; AS; CM; HD; Mixed; NE
- **Confidence:** High; Medium; Low
- **Trajectory Basis:** Intended; Reported
- **Screening:** Include; Exclude: AI removed; Exclude: non-interactional commentary; Exclude: static AI artifact only; Exclude: other
- **Claim Stance:** Descriptive; Benefit claimed; Mixed results; Critical
- **AI-use Stance:** Assigned; Optional; Limited; Prohibited; Mixed; Instructor use
- **Limitations:** None stated; Design limits; Evidence limits; Both
- **Sequence threshold (R30):** 0.5 (sensitivity 0.34, 0.75, 1.0)
- **Traces Collected:** Not described; Collected, not reproduced; Partly reproduced; Reproduced
- **Speaker:** Learner; AI
- **Move:** LM-RQ; LM-QU; LM-SE; LM-AP; LM-GE; LM-CH; LM-VE; LM-RD; LM-RF; LM-CL; AM-EX; AM-PR; AM-OP; AM-SC; AM-FB; AM-CH; AM-RD; AM-CO
