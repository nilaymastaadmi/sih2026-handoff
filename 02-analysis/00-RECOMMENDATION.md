# SIH 2026: the 5 problem statements to take to the BITS Goa internal round

Standalone brief. Written 2026-08-31. Readable with no other file open. Every SIH fact carries a source; anything unverified says ASSUMED.

## The one-paragraph version

Smart India Hackathon 2026 published 229 problem statements (175 Software, 54 Hardware) at https://sih.gov.in/sih2026PS. A team of 6 picks one to pitch at the college internal round; if selected it builds a working prototype at an offline finale in December 2026. Idea submission closes 20 Sept 2026; each team may file against at most 2 problem statements. The winning move is not to pick a fashionable problem, because most competing teams draft their pitch with the same LLM and converge on the same platform-plus-chatbot answer. The winning move is to pick a problem whose body text names a concrete dataset or workflow that a generalist team cannot fake, and where we already hold working code, then put a measured number on screen. On that logic the recommended pick is **PS 26147 (NTRO, automated .IQ/.wav signal parameter extraction)**, with four ranked alternatives below. The previously locked pick, 26055, survives but drops to rank 5.

## How these were scored

Sub-scores use the rubric derived from the official 6-slide idea template and the stated evaluation criteria (guidelines PDF, https://sih.gov.in/letters/2026/SIH%202026%20Guidelines.pdf, fetched 2026-08-31): Novelty 25, Technical approach 20, Feasibility and risk 20, Clarity and format 15, Impact and scale 12, References 8. No official weights exist; these are estimated, with reasoning in `01-event-model.md`. Two standalone numbers accompany each: crowding risk out of 10 and internal-round winnability out of 10.

**Crowding is unmeasured for every PS.** I downloaded the live portal on 2026-08-31 and every one of the 229 problem statements reads 0/500 submitted ideas. The public counter works and is the only real crowding evidence that will ever exist, but no idea has been filed yet. Every crowding number below is therefore ASSUMED, with reasoning shown, and must be re-checked once submissions open.

Recommendation order optimises the internal round first (the brief's instruction), so internal-round winnability is weighted above the national-screening rubric total. Where the two disagree it is flagged.

**Confirmed 2026-08-31 by the team:** the BITS Goa internal round is a PPT/proposal upload only, with no live pitch and no live demo, and the jury is not yet known. This tightens rather than changes the ranking. The entire internal gate is the 6-slide PDF, so "the number on screen" becomes "a real result screenshot inside the deck", which favours the depth picks whose technical-approach slide a generalist team cannot write. It does not favour a live demo, so 26073's rank-2 case now rests on its published rubric and its finale-safety, not on its ESP32 demo (that demo only pays off at the finale). Because the format makes each deck cheap to produce, the two-ideas-per-team hedge (submit 26147 and 26073) is now clearly worth doing.

---

## 1. PS 26147 — Automated model for analysis of .IQ and .wav files along with signal parameter extraction  (RECOMMENDED)

1. **PS ID / title / org:** 26147. Official title exactly as above. Organisation National Technical Research Organisation (NTRO). Category Software. Theme Space Technology (the portal's label; the content is RF signals intelligence). Source https://sih.gov.in/sih2026PS, PS modal `ViewProblemStatement26147`, fetched 2026-08-31.
2. **The real pain.** NTRO signals analysts receive off-air recordings across HF/VHF/UHF as raw .IQ and .wav files and, in the PS's own words, carry out the analysis manually to identify modulation type, sampling rate, FEC and interleaving before the signal can be processed. The failure is throughput and inconsistency: a human does per-file what should be automated, and thin metadata means fine parameters are often unrecoverable. The only source for this pain is the PS body itself; no CAG report, tender or RTI on NTRO SIGINT workflows is public, which is expected for an intelligence agency and is itself the finding.
3. **Rating 80/100.** Novelty 22.0 (blind de-interleaving and FEC recovery, not a modulation classifier), Technical 18.4, Feasibility 12.4 (the full FEC chain is hard), Clarity 12.3, Impact 8.4, References 6.8. Crowding risk 2/10 ASSUMED (intimidating DSP body text, no fashionable keyword, so few teams file). Internal-round winnability 8/10.
4. **The modal pitch.** A RadioML CNN that classifies 11 modulation types at ~95% on the public dataset, wrapped in a Streamlit uploader, calling the solved part of the problem the whole problem. It will not demodulate, de-interleave or decode anything.
5. **Our wedge.** "Everyone else classifies the modulation; we recover the bitstream, because we have built the acquisition and DSP chain in hardware before."
6. **Demo spine.** Screen 1: drop a .wav, show modulation identified and a constellation plot. Screen 2: demodulate and de-interleave to a recovered bit sequence. Screen 3: a table of extracted parameters (sampling rate, FEC type, interleaver depth) against ground truth. The number on screen: bit-error-rate against self-generated truth, e.g. 0 errors on a clean FSK capture.
7. **Evidence plan.** DeepSig RadioML 2016/2018 (https://www.deepsig.ai/datasets/, CC BY-NC-SA, direct download) plus self-generated labelled IQ from GNU Radio (generator public at https://github.com/radioML/dataset), fetched 2026-08-31. Self-generation is the point: we own the ground truth, so the BER number is ungameable. Fallback if RadioML errata bite: generate the entire training and test set in GNU Radio, which the dataset authors themselves recommend.
8. **Build leverage.** The GPS L1 C/A correlator SoC (a 1,023-hypothesis acquisition search validated against a C++ signal model) and the phonocardiogram spectrogram CNN work supply the acquisition, DSP and signal-classification spine. Estimated saving 4 to 6 days versus starting the DSP layer cold.
9. **Flaws and difficulties.** Technical risk: high, the blind FEC and de-interleaving chain (Viterbi, RS, LDPC over unknown parameters) is the genuinely hard part and may only partially ship for the finale. Data risk: near zero, self-generable. Jury risk: low, an NTRO evaluator will respect a working demodulator and punish a bare classifier. Team risk: this needs the 2 strong engineers on the DSP core; the 4 unknowns cannot carry it. **Hardest single thing:** blind FEC parameter estimation with no side information.
10. **Effort.** Idea round 2 person-weeks (1 strong engineer builds the modulation-ID plus demod demo, 1 writes the deck). Finale 12 person-weeks over 3 weeks: 2 strong engineers on the blind chain, 2 on the GUI and pipeline, 2 on test-signal generation and validation.
11. **Kill criterion.** If, in a 2-day spike, we cannot demonstrate any blind demodulation on self-generated IQ beyond modulation ID, drop it: the wedge evaporates and it becomes the modal classifier.
12. **Confidence.** Verified: the PS text, the datasets, the self-generation path, the asset fit. Assumed: crowding (all counters 0/500 today), and that we can push the FEC chain far enough by December.

## 2. PS 26073 — AI/ML-Based Intelligent Anomaly Detection for Automatic Weather Stations (AWS)

1. **PS ID / title / org:** 26073. Official title exactly as above. Organisation Ministry of Earth Sciences (MoES), India Meteorological Department. Category Software. Theme Disaster Management. Fetched 2026-08-31.
2. **The real pain.** AWS sensors drift, freeze, spike and drop out, and bad readings corrupt forecasts and warnings. The PS states that threshold-based quality control is insufficient for hidden or multivariate anomalies. IMD operates a large AWS/ARG network across India (several hundred stations, exact current count ASSUMED); the source for the specific QC gap is the PS body.
3. **Rating 76/100.** Novelty 15.0, Technical 14.4, Feasibility 18.0 (very buildable), Clarity 13.2, Impact 8.6, References 6.4. Crowding risk 4/10 ASSUMED (weather is popular, but this sub-problem is dull). Internal-round winnability 9/10, the highest of the five.
4. **The modal pitch.** An LSTM autoencoder over temperature, pressure and humidity with a reconstruction-error threshold and a dashboard, no edge deployment, no injected-anomaly benchmark.
5. **Our wedge.** "The problem statement tells you exactly how it is scored, so we built that benchmark, injected the anomalies ourselves, and ship the F1 number on a Rs 500 board."
6. **Demo spine.** Screen 1: live sensor stream on an ESP32 with a physically induced fault. Screen 2: the anomaly flagged in real time with an explanation (which sensor, why). Screen 3: F1 and false-alarm rate on the injected-anomaly test set. The number: F1 on anomaly-injected data, the exact metric the PS names.
7. **Evidence plan.** NOAA Integrated Surface Database for Indian stations (https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database, free, no login, also on AWS Open Data), plus self-injected synthetic anomalies. Fallback: Max Planck weather set on Kaggle and the NAB benchmark. IMD's own DSP portal (https://dsp.imdpune.gov.in) is a paid request portal, so we do not depend on it. Fetched 2026-08-31.
8. **Build leverage.** The controlled multi-architecture study discipline from the heart-murmur CNN project (single-variable ablations, seed replication, negative results kept) transfers directly. Saving ASSUMED 2 to 3 days on evaluation rigour, not on code.
9. **Flaws and difficulties.** Technical risk: low. Data risk: low (ISD confirmed public). Jury risk: an IMD evaluator may say WMO-standard QC already exists; the answer is the explainability and edge-deployment the PS explicitly asks for. Team risk: low, the 4 unknowns can own data plumbing and the dashboard. **Hardest single thing:** distinguishing a genuine extreme-weather event from a sensor anomaly without spatial neighbours.
10. **Effort.** Idea round 1.5 person-weeks. Finale 8 person-weeks over 3 weeks: 1 strong engineer on the model, 1 on the ESP32 edge path, the rest on data, injection and UI.
11. **Kill criterion.** If a spatial-consistency requirement creeps in that needs live neighbouring-station feeds we cannot get, the single-station framing collapses; drop or rescope.
12. **Confidence.** Verified: PS text, its published rubric, the data path. Assumed: crowding, and that a single-station model satisfies the jury.

Note: by national-screening rubric total, 26228 (below) scores 78 to this PS's 76. 26073 is placed second because it carries the lowest finale-build risk of the five and because the PS publishes its own scoring rubric, which is a deck-stage advantage that survives the confirmed PPT-only internal format. On a deck-only gate 26228 is close behind; the two are near-tied, and if the finale build were guaranteed to happen I would weight 26228's higher rubric total and near-zero crowding to swap them.

## 3. PS 26228 — Trustworthy Computer Vision Integrity Assurance for Data, Models and Inference Outputs in Multi-Contributor Pipelines

1. **PS ID / title / org:** 26228. Official title exactly as above. Organisation Ministry of Defence, Indian Army (DGIS). Category Software. Theme Blockchain & Cybersecurity. Fetched 2026-08-31.
2. **The real pain.** Defence CV pipelines mix training data from many contributors, vendor-supplied models and downstream inference. Any stage can be poisoned, backdoored, substituted or replayed. The PS wants one evidence-based assurance layer that does not assume any source is trusted. The external anchor is real: the US NIST TrojAI program exists precisely because trojaned models are a recognised threat, https://pages.nist.gov/trojai/docs/data.html, fetched 2026-08-31.
3. **Rating 78/100.** Novelty 20.5, Technical 17.0, Feasibility 14.0, Clarity 10.8 (hard to pitch fast), Impact 8.2, References 7.0. Crowding risk 1/10 ASSUMED (last rows of the list, hard, no consumer appeal, likely the least-filed PS of the five). Internal-round winnability 7/10.
4. **The modal pitch.** A backdoor detector run on one CIFAR model, or a data-cleaning script, addressing one of the three lifecycle stages and ignoring the cryptographic inference-provenance requirement entirely.
5. **Our wedge.** "We already built a tamper-evident, hash-chained decision log with a sealed Merkle root; binding an inference to its exact input and model digest is a capability we can demo on day one, not design from scratch."
6. **Demo spine.** Screen 1: a poisoned sample and a substituted model both flagged with a human-readable reason and confidence. Screen 2: an inference record, then a replayed/altered copy detected as tampered via its hash chain. Screen 3: the assurance report with a coverage statement of what it does and does not catch. The number: detection rate on self-introduced poisoning/backdoor/tamper cases at a stated false-positive rate.
7. **Evidence plan.** NIST TrojAI (public), BackdoorBench (https://github.com/SCLBD/BackdoorBench, public), COCO/YOLO formats (public), fetched 2026-08-31. Fallback: team-generated poisoning and backdoor cases, which the PS explicitly permits.
8. **Build leverage.** The alpaca hackathon agent's hash-chained artifact log with a Merkle root sealed to a timestamp (verified locally: 19 artifacts, root matches seal) maps almost verbatim onto capability 2.2.3, inference provenance and output integrity. Saving ASSUMED 5 to 7 days, the largest asset leverage of the five, on the one sub-capability most teams will skip.
9. **Flaws and difficulties.** Technical risk: the five required capabilities are broad and must be narrowed to survive; model-integrity assessment under black-box access is genuinely hard. Data risk: low. Jury risk: a DGIS evaluator is technical and present; strong on merits. Team risk: needs a strong engineer on the crypto-provenance spine. **Hardest single thing:** black-box backdoor detection without retraining the supplied model.
10. **Effort.** Idea round 2 person-weeks. Finale 12 person-weeks over 3 weeks, scope narrowed to data integrity plus inference provenance plus one model-integrity method done well rather than all five thinly.
11. **Kill criterion.** If scope cannot be cut to a demoable core in the first design pass, it sprawls into an unwinnable everything-tool; drop it.
12. **Confidence.** Verified: PS text, the public benchmarks, the near-exact asset fit. Assumed: crowding (near-zero but unmeasured), and that a narrowed scope still reads as complete to the jury.

## 4. PS 26166 — Multi-modal, Sun angle and scale invariant image correspondence using Chandrayaan-2 optical images (OHRC, TMC and IIRS)

1. **PS ID / title / org:** 26166. Official title exactly as above. Organisation ISRO, Department of Space. Category Software. Theme Space Technology. Fetched 2026-08-31.
2. **The real pain.** Registering lunar images across different sensors, sun angles and altitudes is hard; classical feature matchers (SIFT, ORB) break under illumination and scale change, so alignment is manual or fails, which blocks change detection and mapping. The external anchor is the sponsor's track record: ISRO's Space Applications Centre has documented taking 4 SIH solutions in-house (purpose model, `01-event-model.md`), so this is a sponsor that actually engages.
3. **Rating 77/100.** Novelty 19.5, Technical 16.0, Feasibility 14.8, Clarity 11.7, Impact 8.9, References 6.6. Crowding risk 4/10 ASSUMED (ISRO space PS attract space enthusiasts). Internal-round winnability 7/10.
4. **The modal pitch.** A pretrained SuperGlue or LoFTR demo on two similar lunar crops with a pretty match visualisation and no error metric and no failure case.
5. **Our wedge.** "We show the classical baseline failing across a 40-degree sun-angle change, then beat it with a measured sub-pixel registration error."
6. **Demo spine.** Screen 1: SIFT/ORB failing on a cross-illumination lunar pair. Screen 2: our matcher aligning the same pair. Screen 3: registration error and inlier ratio against the baseline. The number: sub-pixel RMSE, the exact metric the PS names.
7. **Evidence plan.** LRO NAC imagery (https://www.lroc.asu.edu, public, no registration) as the ungated primary, plus Chandrayaan-2 OHRC/TMC-2/IIRS via ISSDC PRADAN (https://pradan.issdc.gov.in/ch2/, free signup, activation latency ASSUMED ~1 day), fetched 2026-08-31. Fallback: run entirely on LRO NAC if ISSDC activation is slow.
8. **Build leverage.** None direct. The spectrogram-CNN and correlator work is adjacent image-and-signal experience but no code transfers. Build leverage: None.
9. **Flaws and difficulties.** Technical risk: medium, cross-modal invariant matching is a live research area. Data risk: low, LRO is ungated. Jury risk: low, ISRO is engaged and technical. Team risk: needs a strong engineer on the matching model. **Hardest single thing:** sub-pixel accuracy across sensor and illumination change with a uniform match distribution.
10. **Effort.** Idea round 2 person-weeks. Finale 12 person-weeks over 3 weeks.
11. **Kill criterion.** If ISSDC access does not activate and LRO-only turns out to miss the multi-sensor point the PS asks for, the pitch narrows below what the sponsor wants; reassess.
12. **Confidence.** Verified: PS text, named metrics, LRO public access, sponsor engagement. Assumed: crowding, ISSDC activation latency, zero code reuse.

## 5. PS 26055 — Smart Scan strategy for Electronic Warfare

1. **PS ID / title / org:** 26055. Official title exactly as above (one of the few exact-title matches). Organisation DRDO, Department of Defence Production / IDEX. Category Software. Theme Robotics and Drones. Fetched 2026-08-31.
2. **The real pain.** An EW receiver must sweep a wide spectrum with an instantaneous bandwidth far narrower than the whole band. Open-loop strategies sweep fast but waste time on non-threatening emitters and miss new or agile threats. The PS wants a learned scheduler that minimises intercept time and maximises interception rate. Source: the PS body; no public DRDO tender or report on this is available, which is expected and is the finding.
3. **Rating 75/100.** Novelty 20.0, Technical 16.4, Feasibility 14.0, Clarity 10.2 (EW framing is abstract for a general jury), Impact 8.6, References 6.2. Crowding risk 2/10 ASSUMED (forbidding EW framing filters entrants). Internal-round winnability 7/10.
4. **The modal pitch.** A generic reinforcement-learning agent on a toy bandit with a reward curve and no radar-domain grounding and no honest figures of merit.
5. **Our wedge.** "We validate the scan scheduler against an external emitter-truth dataset, not just our own simulator, so the interception-rate gain is not something we tuned into existence."
6. **Demo spine.** Screen 1: open-loop sweep missing threat emitters in a simulated RF environment. Screen 2: the learned scheduler catching them. Screen 3: average intercept time and interception ratio, our scheduler versus open-loop. The number: interception rate uplift over the open-loop baseline.
7. **Evidence plan.** The Turing Synthetic Radar Dataset (`alan-turing-institute/turing-synthetic-radar-dataset`, 70 GB, Apache 2.0, contact-gated login, verified to exist 2026-08-31) as external emitter truth. The core simulated RF environment and scheduler are self-contained and need no external data. Fallback: build the emitter environment fully in-house, which the PS itself describes.
8. **Build leverage.** The GPS correlator SoC (acquisition search, RF signal modelling) and the discrete-event scheduling work (a parameterised policy benchmarked against a greedy baseline) both transfer. Saving ASSUMED 3 to 5 days.
9. **Flaws and difficulties.** Technical risk: medium. Data risk: low (sim self-contained; dataset confirmed). Jury risk: low, a DRDO evaluator respects the figures of merit. Team risk: needs a strong engineer on the RL scheduler. **Hardest single thing:** proving the interception gain is real and not an artifact of a simulator the team also wrote, which is exactly what the external dataset is for.
10. **Effort.** Idea round 2 person-weeks. Finale 12 person-weeks over 3 weeks.
11. **Kill criterion.** If the external Turing dataset cannot be integrated to validate the scheduler and the only evidence stays self-simulated, the wedge weakens to the modal RL demo; reassess.
12. **Confidence.** Verified: PS text, the dataset's existence, licence and gate, the asset fit. Assumed: crowding, and that the external-validation story lands with the jury.

---

## Recommended pick and why it beats number 2 (under 150 words)

Take **26147 (NTRO signal parameter extraction)**. It is the purest expression of the only heuristic that beats a field of LLM-drafted decks: pick the problem whose body demands domain depth a generalist cannot fake, then show a measured number the team owns. Its training data is self-generable in GNU Radio, so the bit-error-rate on screen is ungameable, and our GPS correlator and DSP assets mean we start the hard part with a running spine. It scores highest on the rubric (80) and lowest on crowding (2/10 ASSUMED). Number 2, 26073, wins the internal round more easily thanks to its published scoring rubric and a Rs 500 live demo, and it is the safer bet, but its ceiling is lower and an IMD jury can call it solved. Because a team may file two ideas, pitch 26147 and pair it with 26073 as the second national idea: highest ceiling plus a safe floor.

## Verdict on the locked 26055 / 26166 / 26066 decision

**It partially survives.** 26055 and 26166 both remain in the final 5, so the ideas are validated on the merits. But the ranking breaks: 26055 drops from primary to rank 5, 26166 from second to rank 4, and 26066 (the fallback) is cut entirely, displaced by three problem statements neither prior pass evaluated (26147 was scored but demoted, 26228 and 26073 outrank the fallback). The specific thing that breaks is the primary choice and the crowding-based ranking under it: Folder A scored 26147 highest at 82, then demoted it to rank 5 using a crowding axis that is uniformly 0/500 across all 229 PS today and therefore unmeasured. Remove the unmeasured adjustment and 26147 returns to the top. **Evidence that would change it back:** once idea submission opens, live counters showing 26147 crowded near the 500 cap while 26055 stays quiet would restore 26055 to primary; or our own failure, in a 2-day spike, to demonstrate any blind demodulation on self-generated IQ would drop 26147 below 26073 and 26055.

---

## Filled-in IDEA template draft for the top pick (26147), ready to adapt

Fields follow the official template (`00-idea-template-verbatim.md`). This is a starting draft, not a final deck; numbers marked [measure] must be produced from a real spike before submission.

**Slide 1 (title):**
- Problem Statement ID: 26147
- Problem Statement Title: Automated model for analysis of .IQ and .wav files along with signal parameter extraction
- Theme: Space Technology
- PS Category: Software
- Team ID: [to fill]
- Team Name: [to fill]

**Slide 2, IDEA:**
- Proposed solution: a GUI tool that ingests a .IQ or .wav capture and returns not just the modulation class but a recovered bitstream, by chaining automated parameter estimation, demodulation, de-interleaving and forward-error-correction decoding.
- Detailed explanation: the tool estimates sampling rate and modulation, plots the constellation and time-frequency waterfall, demodulates (FSK/QAM/PSK), de-interleaves (block, convolutional, diagonal, pseudo-random) and decodes FEC (Viterbi, Reed-Solomon, LDPC), then correlates the bitstream to separate header from payload.
- How it addresses the problem: it replaces NTRO's manual per-file parameter identification with an automated pipeline that recovers the fine parameters thin metadata currently hides.
- Innovation and uniqueness: most solutions stop at modulation classification, the solved part. Ours recovers the bitstream end to end and reports bit-error-rate against ground truth, because we generate our own labelled signals and therefore know the truth.

**Slide 3, TECHNICAL APPROACH:**
- Technologies: Python, GNU Radio, NumPy/SciPy signal processing, PyTorch for the modulation and interleaver classifiers, a Qt or Streamlit GUI. Optional C++ for the FEC inner loops.
- Methodology: (1) generate labelled IQ in GNU Radio spanning modulations, SNRs and channel effects; (2) train modulation and parameter estimators; (3) implement the demod, de-interleave and FEC-decode chain; (4) evaluate BER against ground truth on a held-out generated set and on RadioML captures. Flowchart plus a working prototype screenshot of a recovered bitstream.

**Slide 4, FEASIBILITY AND VIABILITY:**
- Feasibility: modulation ID and demodulation are tractable now; the acquisition and DSP spine reuses existing team code from a GPS correlator SoC.
- Challenges and risks: blind FEC and interleaver parameter estimation with no side information is the hard part and may only partially generalise.
- Strategies: start from a bounded parameter set the tool searches over, self-generate the exact cases to be decoded, and report per-stage accuracy so partial success is still a measured result.

**Slide 5, IMPACT AND BENEFITS:**
- Impact on target audience: NTRO analysts move from manual per-file analysis to automated triage, with recovered bitstreams instead of parameter guesses.
- Benefits: throughput (economic, staff time), consistency (fewer human errors), and a reusable, auditable signal-analysis pipeline.

**Slide 6, RESEARCH AND REFERENCES:**
- DeepSig RadioML datasets, https://www.deepsig.ai/datasets/
- GNU Radio and the RadioML generator, https://github.com/radioML/dataset
- Standard references on Viterbi, Reed-Solomon and LDPC decoding and on blind modulation classification [add 2 to 3 specific citations before submission].

---

Execution status: changed locally (all Phase 1 to 7 files written under `round2/`). Verification status: the live idea counts, the 26055 dataset, and every finalist's data path were checked against the live web on 2026-08-31 and are recorded in `06-verification.md`. Not yet: committed, pushed.
