# 05. Independent top 12, committed before reading any prior pass

Written 2026-08-31, before opening `03-folder-critique.md` or `03-merged-longlist.tsv`. Inputs: the Phase 1 rubric (`01-event-model.md`), the Phase 2 axes (`02-competitor-model.md`), the Phase 4 assets (`04-assets.md`), `ps_clean.tsv`, `ps_clean-notes.md`, and full official descriptions for 30 candidates extracted from a fresh live-portal download made today (not from the stale on-disk scrape).

## Coverage, stated honestly

- 229 rows total. 54 Hardware rows excluded on sight per the category rule.
- Of the 175 Software rows: all 175 evaluated at the level of title, organisation, theme and the 200-character description opening. 30 of the 175 then read in full official text (mean 2,560 characters) before selection. The other 145 were judged on metadata plus opening only.
- Excluded on a single filter without reading further: 17 of the 175, the Student Innovation block (26193-26209). Single filter: they are open theme categories, not concrete problems, and will absorb the largest and most generic idea pool; there is no PS body to out-read.
- So the number the brief asks for: 175 of 175 software PS evaluated, 17 excluded on one filter, 158 given at least a comparative metadata read, 30 given a full-text read.

## Phase 4 mapping used (capability, not repo names, to PS)

| Asset capability | PS it powers |
|---|---|
| GPS L1 correlator SoC + spectrogram CNN work (DSP, RF, acquisition search) | 26147, 26055, 26168 |
| Pre-registered stats, sealed-holdout eval discipline | 26073, 26066, 26166, 26168 (26168's PS demands measured results in the proposal) |
| Merkle-chained tamper-evident decision log (alpaca) | 26228 (cryptographic inference provenance is a required capability) |
| Multi-tool agent + quantified eval harness with hallucination tier | 26117 |
| Discrete-event simulation + parameterised scheduler vs greedy baseline (icpc-huawei, sorter-validation) | 26027, 26123, 26055 |
| Document-to-database deterministic extraction (jaw2026) | 26034, and it strengthens 26117's document tasks |
| CV defect detection with rupee cost layer (pcb-drishti) | 26034, 26143 |
| Physical-line Monte Carlo modelling | 26027, 26123 |
| Analog SKY130 pair | unused: authorship unconfirmed, standing instruction to ask first, and no shortlisted PS needs it |

## The 12, committed

Order is rough preference, refined in Phase 6. Sub-scores out of 100 come in Phase 7 for the final 5.

1. **26147, NTRO, Automated analysis of .IQ and .wav files with signal parameter extraction.** Axis D at maximum: modulation ID, demodulation (FSK/QAM/PSK), de-interleaving, FEC decoding (Viterbi, RS, LDPC). A generalist LLM team cannot fake this and will submit a thin RadioML CNN. Ground truth is self-generable in GNU Radio, so axis H (a measured bit-error-rate protocol) needs no external data grant. Direct DSP asset leverage. Crowding ASSUMED low: no buzzwords, intimidating body text.
2. **26073, MoES/IMD, AI anomaly detection for Automatic Weather Stations.** The PS publishes its own evaluation weights (Innovation 25%, Detection accuracy 20%, real-time 15%...) and says scoring uses anomaly-injected data; we can pre-build exactly that benchmark and report F1 before submission. Public AWS-type data exists (IMD archives, NOAA ISD Indian stations). Explicitly invites ESP32 edge deployment: a Rs 500 live demo at the internal round. Low glamour, high winnability.
3. **26228, MoD/Indian Army DGIS, Trustworthy CV integrity assurance.** Requires a tamper-evident audit trail and cryptographic binding of input, model digest and output: the alpaca Merkle-chain capability nearly verbatim. Air-gapped, model-agnostic, public benchmarks named in the PS (NIST TrojAI, BackdoorBench). Crowding ASSUMED near zero: last rows of the list, hard, no consumer appeal.
4. **26117, MRPL, Sovereign on-premise agentic AI workbench.** The one buzzy pick, taken because our differentiators are real: a quantified eval harness with a hallucination tier, and the PS itself demands proof of zero egress, which suits our audit-log discipline. Dataset field says no proprietary data required. Overscope is the main risk; scope must be cut to 2 task types done measurably well.
5. **26055, DRDO, Smart scan strategy for Electronic Warfare.** On full read this is self-contained: the core is a simulated RF environment with truth data plus a learned scheduler scored on named figures of merit (intercept time, Pd, Pfa). The portal dataset link is malformed and gets resolved in Phase 6, but the build does not depend on it. DSP plus scheduling assets both fire. Crowding ASSUMED low.
6. **26166, ISRO, Chandrayaan-2 multi-modal image correspondence.** Public data (ISSDC map browser, LROC), evaluation metrics named in the PS (sub-pixel RMSE, inlier ratio). Wedge: show the classical SIFT baseline failing across illumination and beat it with a measured number. Most engaged sponsor in the purpose model.
7. **26168, ISRO, AI dead reckoning for GNSS-denied navigation.** The PS names its dataset (IO-VNBD, on GitHub), sets numeric drift benchmarks, and requires preliminary model results inside the idea proposal. That rule is a moat for a team that measures early, and a filter against decks with no numbers. Kalman filtering plus IMU work sits next to the GNSS correlator asset. Phone demo is theatrical: GPS off, drive, watch drift stay bounded.
8. **26143, NTRO, Oil spill detection with AIS attribution.** Datasets named in the PS itself (Zenodo Sentinel-1 oil spill set, marinecadastre AIS samples, synthetic AIS allowed). Wedge: physics drift hindcasting with OpenDrift plus probabilistic vessel scoring measured on synthetic truth, versus the modal YOLO-on-SAR-chips deck that cannot attribute anything.
9. **26066, MoES/INCOIS, OceanEmbed subsurface temperature reconstruction.** Fully specified ML problem with public data named (GLORYS, gridded ARGO via INCOIS LAS), region, depths and metrics fixed. Wedge: honest skill against climatology and persistence baselines, which most teams will not know to include. Research-integrity asset fits exactly.
10. **26027, Ministry of Railways, Automatic block planning.** FLAG: one of the 9 corrupted titles, prints as "Al-Powered"; handle in any string matching. The one big-ministry operations-research pick: integrate maintenance demand and corridor availability, optimise block schedules for asset availability. All named source systems (TMS, SMMS, TDMS, COA) are internal, so the honest plan is a synthetic-but-realistic division model built from public timetables, and that must be said out loud in the pitch. Discrete-event simulation asset direct. Railways juries are experienced and present.
11. **26034, DoCA, Legal Metrology packaged-commodity compliance checker.** Real enforcement pain, rules are public law, and the demo data is any product on any shelf: real data in hand by definition. jaw2026-style extraction plus a rule engine with clause-cited violations, pcb-drishti-style verdict layer. Font-size-in-mm from an image needs a reference object; solvable, and worth stating as the hard part.
12. **26123, Bharat Electronics, Edge-AI distributed AMR fleet coordination.** Success criteria are numeric in the PS (zero collisions, 20% task-time reduction vs stop-and-wait). Simulation explicitly acceptable. DES plus robotics assets. The pick most exposed to existing multi-agent path-finding literature, which is also its feasibility guarantee.

## Bubble list (evaluated in full, held out of the 12)

26079 (forecast bust detection: clever, public TIGGE data, lost the weather slot to 26073's published rubric), 26023 (CMPDI reporting: strong deterministic-answers wedge for parliament questions but internal archives plus an LLM-shaped ask attracts the RAG crowd), 26165 (OIL SIF NLP: practitioner-written but data is OIL-internal, proxy transfer is a stretch), 26102 (MPLADS anomalies: public dashboard named, granularity unverified), 26056 (airfare index: PS demands ToS-compliant scraping of sites whose ToS forbid it; kill on internal contradiction), 26100 (GeM compliance: core is integration with non-public government APIs, demo would be mocked), 26104 (voice cloning detection: real asset fit via spectrogram CNN and public ASVspoof data, but ASSUMED the single most crowded cyber PS on the list; it is the kind of title every LLM recommends), 26053, 26054, 26051, 26083, 26074, 26059, 26171, 26176, 26227.

## Expectation against the two prior passes (written before reading them)

I expect neither prior pass to have shortlisted at least these 6 of my 12: 26027, 26034, 26073, 26123, 26147, 26228. Reasoning: both passes are described as having concentrated on 65 PS with a defence and space lean; my six above are either buried in boring ministries, at the unfashionable tail of the ID range, or wear no fashionable keyword. I expect 26055, 26066, 26166 to appear in at least one pass, and 26117, 26143, 26168 could go either way.

This list is committed as of this file's write time. Phase 6 may cut it but additions require stating that the addition came after exposure to the prior passes.
