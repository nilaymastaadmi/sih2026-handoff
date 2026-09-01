# 07. Coverage sweep of the 128 unread problem statements, and an adversarial prior-art test

Written 2026-08-31, after the internal deadline moved to 2 Sept. This file supersedes parts of `00-RECOMMENDATION.md`. Two of the five picks in that file are damaged, one fatally.

## 1. What was swept

Of 175 software PS: 30 read in full previously by me, 19 by Folder A, 0 by Folder B (it worked from the listing table, which carries no descriptions). Excluding the 17 Student Innovation rows, **128 software PS had never been read past their opening 200 characters by anyone.**

All 128 full official texts were extracted from a live portal download taken 2026-08-31, 0 missing, and read completely by 6 independent readers. Total swept text 424 KB, mean description 2,560 characters.

**Coverage now: 158 of 158 non-Student-Innovation software PS read in full. The unread gap is closed.**

Live idea counters re-checked at 22:37 on 2026-08-31: still 0/500 on all 229. Crowding remains ASSUMED everywhere.

## 2. The most important finding: two of my own picks failed an adversarial prior-art test

I ran a dedicated skeptic against my own top three, instructed to prove a shipped product already does the job and to default to "real threat" when ambiguous. That bias must be discounted, but two results survive discounting.

### 26073 (IMD weather-station anomaly detection) is DEAD. Removed.

The incumbent is not a competitor's product, it is **the evaluating agency's own 24/7 operational system**. IMD documents QC covering completeness, climatological consistency, time consistency, internal consistency, spatial and range checks, monitored round the clock at the Pune Central Receiving Servers and every State Meteorological Centre. Two free open-source stacks already do the exact "sensor fault versus genuine weather" discrimination the PS asks for: MET Norway TITAN/titanlib (https://github.com/metno/TITAN, built explicitly for real-time operational QC of large AWS networks with spatial buddy checks) and NOAA MADIS 3-level QC (https://madis.ncep.noaa.gov/madis_qc.shtml). All fetched 2026-08-31.

Kill shot: **no public labelled sensor-fault ground truth for IMD AWS exists.** Without labels there is no measured claim, and an unmeasured claim presented to the sponsoring agency about its own operational system is the worst available position. I previously rated this 76 and called it the highest internal-round winnability on the board. That was wrong, and it was wrong because I scored the PS text without testing the incumbent.

### 26147 (NTRO signal parameter extraction) is badly damaged. Demoted from rank 1.

Roughly 80% of the ask ships today as commercial product. Krypto500/Krypto1000 by COMINT Consulting advertises classification across more than 3,000 signalling systems down to equipment and submode. Wavecom W-CODE covers 300+ modes including MIL-STD-188-110 and STANAG 4285/4529/4539/5066 with **auto-detect that identifies mode and parameters automatically**. Rohde and Schwarz CA100 does "analysis, classification, demodulation and decoding". Sorcerer is free and decodes STANAG 4285 and MIL-STD-188-110A/B. All fetched 2026-08-31.

My stated wedge was "everyone else classifies the modulation, we recover the bitstream." That wedge is partly false: W-CODE already auto-detects parameters and decodes. **The correction:** every one of those tools is a *library-match* classifier that identifies a signal from its own catalogue. Genuinely blind reconstruction, estimating unknown interleaver depth and type and unknown convolutional generator polynomials with no protocol library, remains academic, and no packaged open-source implementation of blind interleaver-plus-FEC recovery was found. That narrow gap is real but is PhD-grade and is the part least likely to demo in a 36-hour finale. ASSUMED: an NTRO panel has evaluated or owns W-CODE or Krypto500.

26147 survives only if pitched explicitly as the blind, no-library case with the COTS landscape acknowledged on the slide, or on an indigenisation motive (both named tools are foreign and export-controlled), which is ASSUMED and unverified.

### 26228 (MoD CV integrity assurance) SURVIVED, with its wedge corrected.

The skeptic could not refute it end to end. But it refuted half of it, and that half was my stated wedge.

The cryptographic-binding half is solved plumbing, not research: OpenSSF Model Signing v1.0 (April 2025, Sigstore bundles, PKI-agnostic including bare keys), C2PA 1.4/2.0 AI/ML guidance defining signed manifests binding inputs and producing model to output, plus shipped scanners (Protect AI Guardian, acquired by Palo Alto July 2025, 4.47M model versions scanned; HiddenLayer Model Scanner shipped inside Azure AI Foundry and Databricks). Fetched 2026-08-31. **Do not pitch provenance as novel.**

What survives, and is now the wedge: the *detection* half sits against a published research ceiling, not a solved product. NIST/IARPA TrojAI round 9 results: PICCOLO 96% clean / 81% backdoored, DBS 83% / 69%, Meta Classifier 100% / 69%; round 2 had most performers below 0.80 AUC-ROC. And Sigstore keyless signing requires OIDC plus the public Rekor transparency log, **neither of which exists air-gapped**, while the PS mandates offline operation. An offline trust profile plus the full multi-contributor data-to-model-to-preprocessing-to-output chain is currently four separate products stitched together, not one shipped thing.

## 3. Genuine new finds from the 128

Eleven PS were nominated at 79 to 85. That clustering just above the stated bar of 75 is anchoring by six independent agents, not eleven upgrades, and I discounted accordingly. Four survive my own review. Three of the four were touched by neither prior pass.

### 26169, ISRO, "Development of an AI-Based Virtual Camera Tracking System for Coarse Alignment of Mobile Free Space Optical Communication (FSOC) Terminals". NEW, untouched by both passes.

The strongest structural profile found. The body mandates injecting "disturbances due to atmospheric turbulence, platform vibrations, camera motion, noise" into a virtual camera feed and logging six named metrics: simulation duration, FPS, acquisition time, average and maximum tracking error, lock retention rate, processing time. **Data risk is zero by construction**: the team generates the scenario, so ground truth is exact and no portal, MoU or login stands between us and a measured number. That is the single cleanest evidence story of any candidate, better than 26147's self-generation because there is no COTS incumbent. Acquisition over a field of view is a correlation search, which is a direct match to the GPS correlator asset. Hardest thing: Kolmogorov or von Karman phase-screen generation at a stated refractive-index structure constant driving a pan-tilt loop with real slew-rate and latency limits without the loop going unstable. Crowding 3/10 ASSUMED: "coarse alignment" and "lock retention rate" are not searchable keywords, and the deliverables demand a standalone executable plus a 10 to 15 page technical report, which suppresses low-effort entries.

### 26103, MoSPI, "Use case on web-based integrated project-monitoring platform". NEW, untouched by both passes.

The title reads as a CRUD portal; the body is a research brief. It asks for an "Assessment of whether Artificial Intelligence (AI) and Machine Learning (ML) techniques provide significant gains over conventional statistical methods". That is an explicit invitation to report an honest negative or modest result, which is a documented strength of this team rather than a risk. It hands over its own baseline arithmetic: 1,981 ongoing projects, original cost Rs 37.13 lakh crore against revised Rs 42.78 lakh crore.

Data verified public 2026-08-31: the PAIMANA portal at https://paimana-proj.mospi.gov.in/ loads, and monthly Flash Reports are published as public PDFs, for example https://ipm.mospi.gov.in/Content/PDF/FlashReport_March_2026.pdf. Latest published figures track 1,775 projects worth Rs 37.11 lakh crore as of July 2026; the August 2026 Flash Report is due 25 Sept 2026. Caveat: the reports are PDFs, not a clean dataset, and the report-selection interface on the portal shows a Login link. Extraction is required, which is itself a direct match to the verified PDF-and-spreadsheet-to-relational-store capability.

Two assets compose here: PDF corpus extraction builds the dataset, and pre-registered statistics with correction for autocorrelated overlapping samples produces the honest number. The trap most teams fall into is named and specific: the same project recurs across dozens of monthly snapshots, so a random train/test split trains and tests on the same project and yields a fake R-squared near 0.96. Correct handling needs grouped time-forward validation, plus survival analysis for right-censored ongoing projects. Crowding 2/10 ASSUMED: no fashionable keyword, and the difficulty is invisible to anyone who did not read to paragraph 6.

### 26035, DoCA, "Development of a Software Program/Application for Generation of Test Reports for Non-Automatic Weighing Instruments (NAWI) as per OIML Recommendation R-76". NEW, untouched by both passes.

The highest-floor, lowest-ceiling option. Pass/fail is a decision table over a published standard, not a prediction, so correctness is provable rather than claimed. Named baseline in the body: test reports "are largely prepared manually using spreadsheets or document templates, making the process time-consuming, prone to calculation errors and lacking uniformity". Statute is public (Legal Metrology Act 2009 and the Rules 2011, at the URL the portal itself supplies). The wedge available to this team and almost nobody else: prove the pass/fail function correct across the entire OIML R-76 input domain using constrained-random generation with coverage closure, the hardware-verification method applied to a legal compliance function. Honest weakness, not hidden: impact is narrow (designated laboratories and state Legal Metrology officers, not a citizen population), and the build looks small at first glance. Crowding 3/10 ASSUMED: no AI keyword anywhere, and the theme bucket is Miscellaneous.

### 26119, MRPL, "Indigenous GPU-Accelerated Optimization Solver". Previously killed unfairly.

Folder A rated this DEAD at 50 with the reason "20-30 years of PhD-level work; the one honest number is a guaranteed loss or a crash." **That verdict is a truncation artifact, and this is verifiable.** The full description is 4,118 characters. The decisive "Expected Solution" clause begins at character 3,150. The local file both prior passes worked from truncates every description at 1,500 characters, so the clause could not have been read. What it says is materially weaker than the Description's rhetoric about "thousands to millions of variables": it asks only that the solver "successfully solve standard benchmark problems from recognised optimization libraries such as MIPLIB, Netlib or Mittelmann benchmark sets, with solution quality and computational performance compared against at least one established commercial or open-source solver", and states that "a polished graphical user interface is not required".

Two clauses kill the modal pitch by decree: "It shall not be built upon any existing open source solver library but shall be built from scratch from mathematical foundation", and the explicit exemption from a GUI. Benchmarks named are all free downloads (MIPLIB, Netlib LP, Mittelmann, QPLIB). My own assessment: still the highest finale risk of any candidate, because the honest deliverable is a working from-scratch simplex that is measurably slower than HiGHS, and selling that to a sponsor who wants a CPLEX replacement is hard. Recorded as fairly-scored rather than promoted.

## 4. Rejected despite high nominated scores

- **26038** MathWorks diabetic retinopathy, nominated 81: crowding 8/10 by the nominator's own assessment. Self-disqualifying under our own heuristic.
- **26046** Ayush clinical trials CTMS, nominated 82: the Define-XML and SDTM conformance angle is genuinely machine-checkable and the PS sanctions synthetic data, but the bulk of the build is enterprise CRUD.
- **26078** NCMRWF extreme weather tracking, nominated 82: the PS hands you its own baseline failure mode ("standard deep learning models like standard CNNs or U-Nets suffer from spectral smoothing"), which is a gift. Held back only because NEPS-G and NCUM grids are ASSUMED NCMRWF-internal and the body pre-writes its own solution in first person, which caps novelty headroom. Best of the near-misses; promote if 26103's PDF extraction proves harder than expected.
- **26164** NTRO post-quantum crypto discovery, 26145, 26153, 26155: all in Blockchain and Cybersecurity, the most subscribed theme, with nominated crowding of 6 to 9 out of 10.
- **26170** ISRO burn-in screening: the nominator called its Part Average Testing framing novel; Folder A correctly identified it as AEC-Q001, roughly 20 years old. Folder A is right, novelty is low.

## 5. Revised five

| Rank | PS | Why it moved |
|---|---|---|
| 1 | **26228** MoD, CV integrity assurance | Only pick that survived adversarial prior-art review. Wedge corrected: pitch air-gapped detection and the full data-to-output chain against the published 69 to 81% TrojAI ceiling, NOT cryptographic provenance, which is shipped plumbing. |
| 2 | **26169** ISRO, FSOC virtual camera tracking | NEW. Zero data risk by construction, six metrics named in the body, correlation-search asset fit, no COTS incumbent found. |
| 3 | **26166** ISRO, Chandrayaan-2 image correspondence | Unchanged. Public ungated LROC fallback, named sub-pixel metric, most engagement-documented sponsor. |
| 4 | **26103** MoSPI, project monitoring | NEW. Two verified assets compose (PDF extraction plus honest statistics), public data confirmed, invites the honest negative result this team is known for. Lowest finale-build risk. |
| 5 | **26147** NTRO, signal parameter extraction | Demoted from 1. Survives only as the explicitly blind, no-library case with Krypto500 and W-CODE acknowledged on the slide. |

Dropped: **26073, killed by prior art.** **26055** falls out of the five but remains viable (self-contained simulation, dataset verified) as the sixth. **26035** is the high-floor fallback if a top pick fails. **26119** is fairly scored at last but carries the highest finale risk.

## 6. Consequence for the memory record

`MEMORY.md` still records `decision-2026-08-31-sih-2026-entry` as 26055 primary, 26166 second, 26066 fallback. After this sweep only 26166 remains in the five, 26066 was cut in Phase 6, and 26055 is sixth. That memory entry is now stale and should be rewritten rather than left to anchor a future session.
