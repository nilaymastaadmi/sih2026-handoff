# CLAIMS: every load-bearing claim, with its status

A claim is load-bearing if the pick changes when it is false.

**Status is exactly one of:**
- **VERIFIED**: checked against a primary source in this session, by me, not by a delegated agent.
- **REPORTED**: a prior session, a research folder, or a research agent asserts it and I did not recheck it myself. Most of the competitive-landscape claims sit here. Treat them as one source deep.
- **ASSUMED**: reasoned to, not observed.
- **UNCHECKED**: it matters and nobody has looked.

Count: 33 claims. 12 VERIFIED, 16 REPORTED, 4 ASSUMED, 1 UNCHECKED.

The single UNCHECKED claim, number 5, is the weakest point in the whole package. Audit it first.

---

## A. The portal and the counts

| # | claim | where used | status | source | if wrong |
|---|---|---|---|---|---|
| 1 | The portal lists 229 problem statements, 175 Software and 54 Hardware, IDs 26001 to 26229 contiguous | everywhere; defines the search space | VERIFIED | regex over `evidence/portal-snapshots/sih2026PS-2026-08-31.html`, matches Session 1's independent re-parse in `evidence/ps_clean-notes.md` | Coverage claims in `GAPS.md` are wrong and the sweep missed rows |
| 2 | Every one of the 229 idea counters read 0/500 on 2026-08-31 at 22:37 and again on 2026-09-01 at 00:03 | all crowding scores; the decision to de-weight crowding | VERIFIED | two direct scrapes, `evidence/live-idea-counts-2026-08-31.tsv` and the two portal snapshots | Crowding becomes measurable, and every ASSUMED crowd score below could be replaced with a real number |
| 3 | PS 26169 is still listed and not withdrawn, deadline 20 September 2026 | the pick is filable | VERIFIED | scrape 2026-09-01, `evidence/portal-snapshots/sih2026PS-2026-09-01.html` | The pick does not exist and everything downstream is void |
| 4 | 22 of 229 problem statements carry a document link in the "Dataset Link" field | the discovery method that found the annexure | VERIFIED | regex over the live page, run by me | The claim that this was an under-exploited seam is overstated |

## B. The annexure, which is the reason for the pick

| # | claim | where used | status | source | if wrong |
|---|---|---|---|---|---|
| 5 | **The PS 26169 annexure is current and authoritative** | the entire basis for preferring 26169 over 26228 and 26166 | **UNCHECKED** | the PDF was downloaded from the Drive link in the portal's Dataset Link field. It carries no date, no version, and no ISRO letterhead beyond its content. I did not find an ISRO-hosted copy to cross-check | **The main reason for the pick evaporates.** Without published weights and targets, 26169 is an ordinary tracking problem and 26228's lower build risk likely wins |
| 6 | The annexure states evaluation weights of Functional Verification 20%, Benchmark Performance-1 30%, Benchmark Performance-2 30%, Technical Evaluation 20% | `09`, `11`, `13`, the artifact | VERIFIED | read pages 2 and 3 of `evidence/ps-annexures/PS26169-annexure-ISRO.pdf` directly | The "60 percent is scored from logs" strategy is misdirected |
| 7 | The annexure sets targets: acquisition <=2 s, tracking error <=10 px, target loss <5%, re-acquisition <=1 s, throughput >=20 FPS | the spike's pass or fail criteria | VERIFIED | same PDF, page 1 to 2 | The spike measured against the wrong bar and "7 of 11" is meaningless |
| 8 | Benchmark Performance-2 requires the software to bypass its own camera and ingest supplied .mp4 files | the swappable-frame-source architecture, called the decision that cannot be retrofitted | VERIFIED | same PDF, page 3, quoted verbatim in `09` | The architectural priority is wrong, though a swappable source costs little anyway |
| 9 | The annexure says "AI methods (if used)", making AI optional | the defence against "what does a neural network buy over a centroid tracker" | VERIFIED | same PDF, Deliverables section | A classical-baseline-led entry reads as non-responsive to an "AI-Based" title |

## C. Datasets and data availability for the candidates

| # | claim | where used | status | source | if wrong |
|---|---|---|---|---|---|
| 10 | PS 26055's malformed dataset link resolves to `alan-turing-institute/turing-synthetic-radar-dataset`, 70 GB, Apache 2.0, gated behind a contact-sharing agreement | `06`, the kill criterion on 26055 did not fire | VERIFIED | I fetched the Hugging Face page myself | 26055's only stated weakness is unmitigated and it should have been cut earlier, which does not change the final pick |
| 11 | PS 26169 needs no external dataset; ground truth is generated | the "zero data risk" claim | VERIFIED | the annexure names no dataset, and the spike generates its own scenes | Data risk returns and 26169's main practical advantage weakens |
| 12 | NIST TrojAI and BackdoorBench are public and downloadable without approval (for 26228) | 26228's data story | REPORTED | two research agents fetched the pages; I did not | 26228 gets worse, which does not change the pick |
| 13 | LROC NAC lunar imagery is public with no registration; Chandrayaan-2 via ISSDC PRADAN needs a free account (for 26166) | 26166's data story | REPORTED | two research agents, corroborating each other | 26166 gets worse, which does not change the pick |
| 14 | NOAA ISD gives free no-login weather station data; IMD's own portal is a paid request portal (for 26073) | 26073's data story before it was killed on other grounds | REPORTED | two research agents | Immaterial; 26073 was killed on prior art, not data |
| 15 | DeepSig RadioML is directly downloadable, and labelled IQ can be self-generated in GNU Radio (for 26147) | 26147's data story | REPORTED | one research agent | Immaterial; 26147 was rejected on build risk |
| 16 | IO-VNBD resolves on GitHub; Zenodo Sentinel-1 oil spill set is 40.9 GB CC BY 4.0; GLORYS is free with a Copernicus account | 26168, 26143, 26066 data stories | REPORTED | two research agents | Only affects candidates already cut |
| 17 | MoSPI publishes project-level rows with stable project codes in Flash Report Part-II Annexure VIII, as selectable vector text | the 26103 refutation is about redundancy, not data absence | REPORTED | one research agent fetched and read the May 2024 report; a second agent had earlier claimed the opposite | If data is in fact aggregate-only, 26103 dies twice over, which does not change the pick |

## D. Prior art, the claims that killed candidates

| # | claim | where used | status | source | if wrong |
|---|---|---|---|---|---|
| 18 | IMD already runs 24/7 operational quality control, and free titanlib and NOAA MADIS already discriminate sensor faults from real weather | killed 26073 outright | REPORTED | one adversarial agent, instructed to default to "real threat" on ambiguity. I did not re-fetch | 26073 returns to contention. It had the highest internal-round winnability score before this |
| 19 | No public labelled sensor-fault ground truth exists for IMD AWS | the decisive half of the 26073 kill | REPORTED | same agent; an absence-of-evidence finding, which is the weakest kind | Same as 18 |
| 20 | Krypto500, Wavecom W-CODE and the free Sorcerer already cover roughly 80% of PS 26147, and they are catalogue matchers rather than blind recoverers | demoted 26147 from rank 1 to rank 4 | REPORTED | one adversarial agent, with vendor URLs | 26147's novelty recovers and it becomes a strong contender given its sponsor |
| 21 | Universal Radio Hacker was archived read-only on 2026-03-29 and gr-inspector still requires GNU Radio 3.8 | 26147's build risk, which is what finally rejected it | REPORTED | one research agent | 26147's build risk drops materially |
| 22 | arXiv 2509.04775 (September 2025) already evaluated SIFT, ASIFT, AKAZE, RIFT2 and SuperGlue on cross-modality Chandrayaan-2 pairs and reported RMSE | damaged 26166 | REPORTED | one adversarial agent | 26166 recovers and becomes the strongest ISRO alternative |
| 23 | PAIMANA is MoSPI's own live production system with analytics already shipped, tracking 1,847 projects | refuted 26103 | REPORTED | one adversarial agent, with a PIB citation | 26103 recovers |
| 24 | The cryptographic-provenance half of 26228 is shipped plumbing: OpenSSF Model Signing v1.0, C2PA, Protect AI, HiddenLayer | forced 26228's wedge to move to air-gapped detection | REPORTED | one adversarial agent | 26228's original wedge stands and it strengthens against 26169 |
| 25 | Published TrojAI backdoor detection sits at a 69% to 81% ceiling | 26228's surviving wedge | REPORTED | one adversarial agent | 26228's remaining wedge is weaker or stronger than stated |
| 26 | No prior SIH edition posted an FSOC or laser-pointing problem statement | 26169 has no precedent to be measured against | REPORTED | one research agent; absence of evidence | A precedent exists and the bar may be higher than assumed |

## E. Rules, format and mechanics

| # | claim | where used | status | source | if wrong |
|---|---|---|---|---|---|
| 27 | Pre-built work may be brought to the finale. ISRO PS 26168 says "bring trained models with them for SIH finale"; MoD PS 26227 requires the demo to run "with network access disabled after all approved models, libraries and datasets have been staged" | the whole "arrive 90 to 95 percent built" strategy | VERIFIED | I grepped the official PS text myself in `evidence/ps-full-text/` | The strategy inverts and every candidate becomes a 32-hour cold build |
| 28 | Autodesk problem statements explicitly disqualify pre-designed files and ban AI-generated content, so pre-staging rules vary by sponsor | the caveat on claim 27 | REPORTED | the annexure sweep agent read the Autodesk PDFs, now in `evidence/ps-annexures/` | The variation is narrower or wider than stated |
| 29 | The official IDEA template is six slides including the title, and the file supplied on 2026-09-01 is content-identical to the one analysed earlier | the deliverable format | VERIFIED | I diffed both pptx files field by field with `scripts/session2/cmp_pptx.py` | The deck is built to the wrong format |
| 30 | The finale gives about 32 hours of coding, six jury contacts, and 4 minutes presenting plus 3 minutes of questions per evaluation | demo-legibility reasoning throughout | REPORTED | one research agent, from an official MoE/AICTE schedule PDF for SIH 2024 | Timing arguments about demo legibility weaken |
| 31 | Evaluation round weights are approximately 20, 30 and 50 percent, with the final round on end-to-end product and commercial viability | the "put money in the deck" instruction | REPORTED | one team's published account, with a second source corroborating only the 50 | The emphasis on commercial framing is misplaced |
| 32 | Across 16 identified winning teams, zero presented a bare model, notebook or benchmark | the correction that overturned the `02` thesis | REPORTED | one research agent's survey; a convenience sample, not a census | The "boring tool with a number" thesis was right after all, which would favour a different pick |

## F. Numbers I produced by running code

| # | claim | where used | status | source | if wrong |
|---|---|---|---|---|---|
| 33 | The prototype meets all five published targets in 7 of 11 scenarios, best mean error 0.09 px, acquisition 0.07 s, 33 to 42 FPS; the external-video path scores 0.36 px; the turbulence generator matches Kolmogorov theory with a fitted exponent of 1.652 against 1.667 at L/r0 = 102 | the feasibility argument and the slide 3 evidence | VERIFIED | I wrote and ran `spike/fsoc_spike.py`, `spike/tune_subharmonics.py` and `spike/test_finite_screen.py`; output in `evidence/spike-output/` | Feasibility is unproven. Note the scenario table still uses the annexure's contrast-based atmosphere, not the validated turbulence module, which is not yet wired in |

## G. Scores and weights, all reasoned

| # | claim | where used | status | source | if wrong |
|---|---|---|---|---|---|
| 34 | The idea-template rubric weights are Novelty 25, Technical 20, Feasibility 20, Clarity 15, Impact 12, References 8 | every score out of 100 in every file | ASSUMED | my own estimate. SIH publishes no weights. The guidelines list nine criteria without weighting | Every total out of 100 shifts, and the ordering between 26169 at 84, 26228 at 74 and 26166 at 73 could change |
| 35 | Crowding scores: 26169 = 3, 26228 = 1, 26166 = 4, 26147 = 2, 26103 = 2, all out of 10 | the comparison tables | ASSUMED | inferred from title glamour and theme popularity, because all counters read 0/500 | Low impact by design: crowding was de-weighted to a tiebreaker after claim 32 |
| 36 | Internal-round winnability scores out of 10 | the comparison tables | ASSUMED | my estimate, with the jury unknown | Ordering could shift, most likely between 26169 and 26228 |
| 37 | The 2023 SIH1447 winning artifact is weak: a Flask app with three Keras models where the operator selects the modulation from a dropdown, and a 92% figure existing only as a filename | the argument that past winners are a floor, and part of 26147's assessment | REPORTED | one research agent found and read the public repository | The historical bar is higher than claimed, which strengthens `10-the-2026-bar.md` rather than weakening it |
