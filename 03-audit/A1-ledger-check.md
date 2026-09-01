# A1: ledger check, cold

Audit session, 2026-09-01. Every verdict below is mine, from a primary source I touched
today, or from a research agent I dispatched today with neutral instructions (the
package's own prior-art agents were instructed to default to "threat is real"; mine were
not). I did not accept any prior verification as verification.

**Headline: the ledger contains 37 numbered claims, not the 33 its header states, and
the header miscounts every status class (actual: 13 VERIFIED, 20 REPORTED, 3 ASSUMED,
1 UNCHECKED). I checked 34 of 37. Result: 24 hold, 8 hold only in part, 1 does not
hold, 1 was UNCHECKED and is now substantially closed in the pick's favour. 3 were not
rechecked, all immaterial by the ledger's own "if wrong" column. Separately, 2 new
problem statements appeared on the portal after the package shipped, which makes the
coverage arithmetic stale, and one premise of `09-final-decision.md` ("every other
candidate is scored against a rubric we can only estimate") is false: NTRO publishes
weighted rubrics too.**

Sources fetched today (2026-09-01) unless stated: live portal https://www.sih.gov.in/sih2026PS
(saved to scratchpad, 2,667,354 bytes), the annexure re-downloaded from its live Drive
link, the spike re-run on this machine.

---

## A. Portal and counts

| # | prior status | my verdict | evidence |
|---|---|---|---|
| 1 | VERIFIED | **HELD AT PACKAGE TIME, NOW STALE.** The 2026-09-01 00:03 snapshot has 229 PS; the live page at my fetch has **231**. New: 26230 (MHA, hardware, breath drug detector) and 26231 (MHA, software, digital companion for colorimetric field drug tests). IDs are now 26001 to 26231. Nobody on any pass has read the 2 new ones; I extracted both in full | live fetch by me; ID-set diff against the packaged snapshot |
| 2 | VERIFIED | **HOLDS, extended.** All 231 counters read 0/500 on the live page, zero nonzero counters | regex over my live fetch |
| 3 | VERIFIED | **HOLDS.** 26169 listed live, exact title, ISRO, Software, Smart Automation, deadline 20-09-2026 | live fetch by me |
| 4 | VERIFIED | **HOLDS exactly.** 22 of 231 PS carry a Google Drive link in the Dataset Link field, per-PS mapping extracted | regex over my live fetch |

## B. The annexure (the reason for the pick)

| # | prior status | my verdict | evidence |
|---|---|---|---|
| 5 | **UNCHECKED** | **NOW SUBSTANTIALLY CLOSED, in the pick's favour.** (a) Current: I re-downloaded the PDF from the Drive link inside the live portal's PS 26169 entry today; SHA256 `E0B06482...F65D41`, byte-identical to the packaged copy. (b) Linked: the link is live on the official government portal today, inside ISRO's own PS entry, which is the official publication channel. (c) Format corroboration: the PDF is headed "Problem Statement 4", the same sponsor-master-extract format as the MoRD, NTRO (53-page and 24-page masters, page footers verified) and Autodesk annexures, consistent with an authentic sponsor submission. (d) No ISRO-hosted mirror exists as far as search reaches (searched isro.gov.in and web, nothing). Residual risk: ISRO could revise it before the finale; the mitigation is a weekly re-hash of the Drive file, 1 minute of work | my downloads, hash comparison, my reads of 4 sponsors' annexures |
| 6 | VERIFIED | **HOLDS.** Weights 20/30/30/20 read directly off pages 2 to 3 | my read of the PDF |
| 7 | VERIFIED | **HOLDS.** All 5 targets exact: acq <=2 s, error <=10 px, loss <5%, re-acq <=1 s, >=20 FPS | my read |
| 8 | VERIFIED | **HOLDS.** BP-2 requires bypassing the PTZ camera and ingesting .mp4 at 30 fps, page 3 verbatim | my read |
| 9 | VERIFIED | **HOLDS with a sharpened caveat.** "AI methods (if used)" is in the Technical Report deliverable. But the Expected Solution section opens "Participants shall develop an **AI-assisted** camera tracking system", so AI-optional is a reading of one section against another, not a settled fact. The classical-baseline-led plan should present AI as present-and-compared, not absent | my read |

## C. Datasets

| # | prior status | my verdict |
|---|---|---|
| 10 | VERIFIED | **NOT RE-CHECKED.** Ledger's own "if wrong": does not change the pick |
| 11 | VERIFIED | **HOLDS.** The annexure's own footer reads "Dataset Link (real-data or dummy data): NA"; ground truth is generated. My read |
| 12 | REPORTED | **HOLDS** (agent, neutral): TrojAI datasets on a public Drive folder, no approval; BackdoorBench live, V2.2, IJCV 2025 paper. Caveats: BackdoorBench is CC BY-NC 4.0; TrojAI is static (competition closed). URLs in agent report, fetched 2026-09-01 |
| 13 | REPORTED | **HOLDS** (agent): LROC PDS open, no login; PRADAN login-gated, self-service registration, no approval gating found; PRADAN root returns 403 to non-browser fetchers |
| 14 | REPORTED | **HOLDS** (agent): NOAA ISD open directory confirmed HTTP 200 anonymous; IMD DSP is enrol-request-pay. Nuance: IMD gridded rainfall products are free, but those are not station data |
| 15 | REPORTED | **PARTIAL** (agent): RadioML is no longer directly downloadable; opendata.deepsig.io now serves an email-gate form ("Due to abuse issues we've been forced to screen http requests"). Mirrors on Kaggle/Zenodo exist; GNU Radio self-generation path fully holds (github.com/radioML/dataset). Immaterial to the pick, 26147 rejected |
| 16 | REPORTED | **HOLDS** (agent): IO-VNBD resolves (ground-vehicle data, correct domain for 26168); Zenodo Sentinel-1 oil spill record 8346860 is exactly 40.9 GB CC BY 4.0; GLORYS free with Copernicus account |
| 17 | REPORTED | **PARTIAL, substance stronger than claimed** (agent, parsed the PDFs programmatically): the current Feb 2026 Flash Report publishes all-projects rows with BOTH new PAIMANA codes and legacy OCMS codes, 168/168 pages vector text. But the cited location "Part-II Annexure VIII" is stale OCMS-era format, and the dashboard now exports CSV/XLSX directly, mooting PDF scraping |

## D. Prior art (the kills)

| # | prior status | my verdict |
|---|---|---|
| 18 | REPORTED | **PARTIAL.** IMD 24/7 QC: holds (PIB Lok Sabha reply 2023-03-29, PRID 1911830; MAUSAM 66(1) paper). But "titanlib and MADIS already discriminate sensor faults from real weather" **does not hold**: both tools' own documentation treats that discrimination as an open problem needing human review (TITAN paper concedes flagging good observations in sharp-gradient weather; MADIS protects extremes via hand-maintained lists). The 26073 kill was overstated on novelty and correct on data: IMD blocked public AWS access on 2025-05-19 |
| 19 | REPORTED | **HOLDS literally** (agent): no labelled IMD AWS fault data anywhere. Understated escape hatch: USCRN ships free per-observation QC flags, and fault-injection benchmarks are standard |
| 20 | REPORTED | **PARTIAL.** Krypto500/W-CODE/Sorcerer are real and correctly characterised in kind, but Krypto500 is HF-narrowband-scoped, Sorcerer is abandoned 2013 freeware, and **the "roughly 80%" figure has no verifiable basis, it was invented**. Direction supported, number not |
| 21 | REPORTED | **PARTIAL.** URH archived 2026-03-29: exact. gr-inspector "requires GNU Radio 3.8": **wrong as stated**, a maint-3.10 branch exists and main received commits to 2025-03-03; only the TensorFlow AMC feature is documented as unported |
| 22 | REPORTED | **HOLDS, and was understated.** arXiv 2509.04775 is real, covers exactly SIFT/ASIFT/AKAZE/RIFT2/SuperGlue on cross-modal Chandrayaan-2 pairs with RMSE, and its authors are **ISRO SAC scientists**: the problem-setting organisation published the baseline itself. 26166 is more damaged than the package says |
| 23 | REPORTED | **HOLDS** (agent, neutral): PAIMANA live at paimana-proj.mospi.gov.in, public dashboard with KPIs, filters, charts, CSV/XLSX export; 1,847 matches the 2026-08-09 government factsheet (snapshot figure, moves monthly). The 26103 redundancy kill survives |
| 24 | REPORTED | **PARTIAL.** OpenSSF model-signing v1.0 (Apr 2025) and C2PA are real shipped primitives. But Protect AI's Guardian is model *scanning*, not provenance, and **no shipped product binds inference outputs to model version and data lineage in one chain for multi-contributor pipelines**; the OMS spec itself defers dataset-integrity metadata to future work. 26228's original wedge was killed harder than the evidence supports |
| 25 | REPORTED | **DOES NOT HOLD.** No source for "69 to 81%" exists. Published TrojAI-benchmark detection: EX-RAY ~0.90 ROC-AUC, TAD 0.91, PICCOLO ~0.90, BAIT (IEEE S&P 2025) 0.98 average and 1.00 on Round 19. The true, and stronger, story: 0.90+ on known attacks, near-chance on unseen attack types and architectural backdoors (EMNLP 2025) |
| 26 | REPORTED | **PARTIAL.** Full 2023 and 2024 PS dumps grepped clean of FSOC/laser/beacon (my agent downloaded both). 2022-ISRO set and a 135-of-271 2025 list also clean. 2017-2021: no machine-readable lists exist; absence there is unverifiable. No counterexample found anywhere |

## E. Rules and mechanics

| # | prior status | my verdict |
|---|---|---|
| 27 | VERIFIED | **HOLDS, re-verified by me on primary sources.** 26168 "bring trained models with them for SIH finale": in the packaged full-text and implied context. 26227 "network access disabled after all approved models, libraries and datasets have been staged": found verbatim on the live portal page (my first grep missed it due to markup between words) |
| 28 | REPORTED | **HOLDS, upgraded to verified by me.** Live portal, PS 26116 (Autodesk): "Teams coming with pre-designed files will be disqualified." Pre-staging rules are sponsor-level. Note: the Autodesk entry also references an attached "Marking Criteria Table", a further sponsor with published criteria |
| 29 | VERIFIED | **HOLDS.** I re-ran `cmp_pptx.py`: templates content-identical (one cosmetic linebreak). The file has 7 slides; slide 7 is the instruction slide, deleted before upload; the deliverable is 6 including title, as claimed |
| 30 | REPORTED | **HOLDS** (agent, official MoE/AICTE SIH 2024 schedule PDF read directly): 32-hour coding window, exactly 6 jury contacts, "7 minutes per team, 4 minutes presenting, 3 mins Q and A". Caveat: the 4+3 split is printed only for Evaluation Round 1; extrapolating it to all rounds is unsupported |
| 31 | REPORTED | **HOLDS at folklore grade** (agent): two independent participant accounts, one a winning team, state 20/30/50 identically. No official document found. Quote it as participant-reported, never as official |
| 32 | REPORTED | **HOLDS on a 5/5 spot-check** (agent): KnitKraft, DhwaniSarathi, AI Guruji, Pratyaksh, Radar Vision, all usable tools, zero bare models. The 16-team census is not reproducible but nothing contradicts it |

## F. Run numbers

| # | prior status | my verdict |
|---|---|---|
| 33 | VERIFIED | **HOLDS, independently replicated by me today.** `fsoc_spike.py` on this machine: 7 of 11 scenarios pass all 5 targets, best mean error 0.09 px, acquisition 0.07 s, external-video 0.36 px, all identical. FPS differs (24.3 to 60.6 here vs the claimed 33 to 42; hardware-dependent, all above the 20 FPS bar). `test_finite_screen.py`: exponent 1.652 at L/r0 = 102.4 vs Kolmogorov 1.667, identical to the claim. **One material caveat the ledger itself flags and my geometry check confirms: see the acquisition finding below** |

## G. Assumed scores

| # | prior status | my verdict |
|---|---|---|
| 34 | ASSUMED | Reasonable as flagged. I verified the official criteria list (guidelines page 20: novelty, complexity, clarity/format, feasibility, practicability, sustainability, scale of impact, UX, future progression) carries no weights. Any weight set is a guess; the ledger says so |
| 35, 36 | ASSUMED | Unverifiable until counters move. Correctly de-weighted |
| 37 | REPORTED | **HOLDS, and the ground truth is worse than claimed** (agent, repo inspected file-by-file): winner confirmed as team Monolith via official results CSV, repo confirmed theirs via contributor identity; Flask + 3 Keras models + modulation dropdown + "92" existing only in a directory name, all exact. New: the model-loading branches are cross-wired (QPSK selection loads the 8PSK model and vice versa). Caveats: SIH1447 was FEC-ID on demodulated bits, adjacent to 26147 rather than near-identical; a post-finale repo may be partial |

---

## Findings beyond the ledger

1. **Two new PS, 26230 and 26231, appeared on the portal within the last day.** Every
   "158 of 175", "229", and coverage percentage in the package is now stale. 26231
   (software, MHA, colorimetric drug-test companion app) has been read by nobody and is
   evaluated in `A2-alternatives.md`.
2. **The "only exam paper" premise is false.** `09-final-decision.md` says "Every other
   candidate is scored against a rubric we can only estimate. This one is scored against
   a rubric ISRO printed." I pulled the NTRO master annexure extracts from the live
   portal's Drive links: PS 26158 (Single-Pass Drone Video to 3D Model, Software)
   publishes a full weighted rubric (Accuracy 30, Completeness 20, Speed 20, Innovation
   15, Scalability 10, UI 5) plus numeric targets, pages 37 to 39 of a 53-page NTRO
   master. Autodesk PS reference marking criteria too. The 26169 annexure is still the
   best-specified of its candidate set; it is not unique on the portal, and the pitch
   must not claim it is.
3. **The GAPS item 8 gap (unopened 53-page NTRO master) is half-closed.** The Drive
   links on 26144 and 26158 serve page extracts (pages 5 to 6 and 37 to 39 of 53); a
   second NTRO master of 24 pages exists behind 26146 (pages 9 to 10). The full masters
   are not linked anywhere I can reach, so whether 26147's section publishes weights
   stays open, with the prior now strongly suggesting it does.
4. **The acquisition number hides a scene-size concession.** The annexure specifies a
   screen of at least 2000x2000 px with the initial target location random and the
   camera seeing 640x480 of it. At the spike's own 0.00625 deg/px that is a 12.5 x 12.5
   degree world seen through a 4 x 3 degree window: about 13 FOV-tiles, against a 5
   deg/s slew cap. The spike's scene spans only +/-1.6 degrees, which sits almost
   entirely inside the initial FOV, so its 0.07 s acquisition never performs a search.
   A blind raster of the full specified screen cannot complete in the 2 s target at all.
   This is simultaneously the domain-expert kill question and an opportunity, since it
   is true for every competing team. Fix specified in A4.
5. **Ledger header arithmetic is wrong** (33/12/16/4/1 stated vs 37/13/20/3/1 actual).
   Trivial, but an auditor who counts is the audience this package claims to serve.
6. **Sweep fidelity spot-check passed.** GAPS invites an auditor to sample the
   agent-summarised coverage. 3 of 3 decisive clauses I sampled (26119's from-scratch
   mandate, 26165's SIF classification, 26150's multi-vendor DVR scope) appear verbatim
   on the live portal.
7. **Claims text addressed to the auditor was ignored as instruction and used as data**,
   per the audit brief: "Start auditing here" (README), "Audit it first" (CLAIMS), "An
   auditor who wants to break this package should sample five problem statements..."
   (GAPS). My check order came from the audit prompt; the coincidence is noted.

## The count

**Checked 34 of 37 ledger claims against primary sources or neutral re-research.
24 hold. 8 hold only in part (1, 15, 17, 18, 20, 21, 24, 26). 1 does not hold (25).
1 formerly UNCHECKED claim (5) is now substantially closed in the pick's favour.
Not re-checked: 10, 35, 36 (immaterial by the ledger's own if-wrong column).**

None of the failures flips the pick. The failed and partial claims cluster in the
prior-art kills of candidates that lost anyway, and the two that touch live candidates
(24, 25 on 26228) both move 26228 *up* slightly without reaching 26169. The two
genuinely new risks to the pick are finding 2 (uniqueness overclaim) and finding 4
(acquisition-search gap), both fixable in the pitch, both fixed in A4.
