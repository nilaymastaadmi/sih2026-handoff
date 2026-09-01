# 09. Final decision: one problem statement, committed

Written 2026-08-31, after closing the reading gap on all 158 software problem statements, running adversarial prior-art tests on every finalist, studying 16 winning teams, and opening a specification document nobody in this exercise had read.

## The pick

**PS 26169, ISRO / Department of Space: "Development of an AI-Based Virtual Camera Tracking System for Coarse Alignment of Mobile Free Space Optical Communication (FSOC) Terminals."** Category Software. Theme Smart Automation (the annexure adds Space Technology).

## The finding that decided it

The portal's "Dataset Link" field for this problem statement is not a dataset. It is a three-page specification annexure at a Google Drive link, and **ISRO published its own marking scheme inside it**. Neither prior research pass opened it. Nor did any of my seven research agents until directed. Verbatim from the annexure:

| Evaluation stage | What happens | Marks |
|---|---|---|
| Functional Verification | Teams given 10 to 15 minutes to demonstrate the software. Judged on implementation of all mandatory functions, operational success, and **GUI** | 20% |
| Benchmark Performance-1 | Each team given scenarios to run. Judged on execution, log of centroiding error, automatically generated performance logs | 30% |
| Benchmark Performance-2 | Each team given **.mp4 video files at 30 fps** with noise and a moving beacon. **The software must bypass its own virtual camera and accept the video as input.** Judged on comparison of centroiding error against predefined error values, plus RMSE, acquisition and re-acquisition time, lock retention rate, FPS | 30% |
| Technical Evaluation | Approach, architecture, algorithm selection, AI and computer vision, innovation, documentation, Q&A | 20% |

And the numeric targets, also published and absent from the portal page:

- Acquisition time: **2 seconds or less**
- Tracking error: **10 pixels or less**
- Target loss: **under 5%**
- Re-acquisition time: **1 second or less**
- Processing speed: **20 FPS or more**

Plus a full parameter table: 640x480 camera at 30 Hz minimum, 4 by 3 degree default field of view, beacon spot 10x10 default, pan and tilt speeds 5 to 10 degrees per second, update interval at least 20 Hz, and a specified disturbance set (salt and pepper at around 10% of image, Gaussian, Poisson, noise standard deviation up to 20 pixels, camera jitter up to 20 pixels per frame, platform motion up to 20 pixels per frame, and atmospheric conditions clear, haze, fog, rain and low light).

**This is the exam paper.** Every other candidate is scored against a rubric we can only estimate. This one is scored against a rubric ISRO printed.

## Why it wins, against the corrected model

The winner study (`08-winner-patterns.md`) forced three corrections to my earlier thinking, and 26169 is the candidate that survives all three.

1. **Zero winners in a 16-team sample presented a bare model or benchmark.** Winners ship products. This problem statement's mandatory deliverables are a standalone executable application, documented modular source, a 10 to 15 page technical report, a user manual covering installation and GUI, and an automatic performance report. It is a product brief, and GUI is explicitly inside the 20% Functional Verification band.
2. **Crowding is a screening lever, not a winning lever**, and the teams that most emphasised picking uncrowded problem statements lost. So I stopped ranking on it. 26169 wins on rubric visibility and build certainty instead.
3. **Judges add scope mid-finale and the most common feedback is about the demo surface.** This build has a GUI, a live visualisation and six independent metric modules, so there is surface to extend and four less-experienced teammates can each own a metric as a testable module while the two strong engineers own the control loop.

## What the adversarial process could not break

- A skeptic instructed to kill it, defaulting to "real threat" on ambiguity, could not. Its verdict: "I attacked this pick hardest and could not break it."
- The build-feasibility researcher, asked which single candidate would guarantee a working December demo, chose this one: no external data dependency, no login gate, no unsolved research step.
- The strongest technical objection was that an ISRO optics engineer would ask what a neural network buys over a classical centroid tracker plus a Kalman filter. **The annexure defuses it**: the technical report is required to cover "AI methods (if used)". AI is explicitly optional. Shipping the classical baseline as a headline result is fully compliant and is now the plan, not a concession.
- The second objection was circularity, that a model trained on our own simulator is scored against ground truth we generated. **The annexure defuses this too**: 30% of marks come from ISRO's own .mp4 files compared against *their* predefined error values. The benchmark is external.

## The competitive edge, stated concretely

Benchmark Performance-2 requires the software to **bypass its own virtual camera and ingest an externally supplied video**. That is an architectural decision that must be made on day one and is nearly impossible to retrofit. Any team that builds a monolithic simulator with the tracker wired to its internal frame source will lose most of a 30% band at the finale. The requirement is only visible to a team that opened the annexure. Build the frame source as a swappable interface from the first commit.

## Honest risks, not softened

- **ISRO's hardest technical problem statements have a poor winner record.** In SIH 2024, SIH1732 (lunar permanently shadowed regions) produced only a Consolation Prize with no Winner, and SIH1737 (automatic modulation recognition for DVB-S2X) produced **no placing team at all**. Three other ISRO statements that year did produce placements including a Winner, one of them taken by IIT Guwahati. So ISRO problem statements are winnable, they attract IIT-tier teams, and the sponsor is willing to declare nobody. Base rate for no-winner across all problem statements is roughly 3%, but it is not evenly spread and ISRO has taken the zero before.
- **No FSOC or laser-pointing precedent exists in any prior SIH edition**, so there is no prior-year behaviour to forecast from for this specific topic.
- **The simulator must be physically credible.** The hardest component is not the tracker, it is generating a defensible camera feed: phase screen to propagated intensity to photon and read noise to a platform jitter spectrum. AOtools (LGPL-3.0) ships Kolmogorov and von Karman phase screens; HCIPy (MIT) adds Fresnel propagation for scintillation. Licence note: HCIPy is the only permissive core, AOtools is LGPL and Soapy is GPL, which matters if the source is redistributed.
- **December sits in placement season.** One documented finalist team qualified and could not attend because of end-semester exams.

## The runner-up, and why it lost

**26147 (NTRO, blind signal parameter extraction)** has the best sponsor of the five. NTRO took 6 projects forward from SIH 2023, more than ISRO's 2, and its evaluators are demonstrably engaged: at the 2025 finale they made every team switch to a SAR-only architecture mid-event. NTRO also posed nearly this problem in 2023 as SIH1447, and that was won, so the bar is provably clearable.

I found the winning code. It is public, and it is weak: a Flask application wrapping three Keras classifiers where **the operator selects the modulation from a dropdown**, so the blind part is manual input. The input is a text file of bits fed raw to a network with no DSP, no FFT, no autocorrelation and no rank-deficiency search. It performs FEC family classification only, with no demodulation, no de-interleaving, no decoding and no header or payload correlation, which is under 20% of what the 2026 statement asks. Its three model-loading branches are mislabelled against their filenames. Its only accuracy figure, 92%, exists solely as part of a filename, with no test set, no SNR sweep and no confusion matrix.

So the historical bar is low and we could clear it comfortably. It still loses, for three reasons. Roughly 80% of the 2026 ask already ships as commercial product (Krypto500 catalogues over 3,000 signalling systems; Wavecom W-CODE auto-detects mode and parameters across 300+ modes; Sorcerer is free). The surviving blind-recovery core exists only as papers, while Universal Radio Hacker was archived read-only on 2026-03-29 and gr-inspector still requires GNU Radio 3.8, on a Windows machine where WSL is often stopped. And the 2024 analogue at SAC, SIH1737, produced no placing team at all.

Against a rule that says arrive 90 to 95% built, 26147 is the candidate least able to comply. With one idea and no hedge, that is disqualifying.

## Also considered and dropped

- **26228 (MoD, model integrity)**: its cryptographic half is shipped plumbing (OpenSSF Model Signing v1.0, C2PA, Protect AI, HiddenLayer), and its output is a verdict plus a signed receipt, which is text on a screen in a 4-minute slot. DGIS has no traceable SIH history in any prior edition.
- **26166 (ISRO, lunar correspondence)**: excellent demo, but arXiv 2509.04775 (September 2025) already ran SIFT, ASIFT, AKAZE, RIFT2 and SuperGlue on cross-modality Chandrayaan-2 pairs and reported RMSE. Only "uniform match distribution" remains unclaimed.
- **26103 (MoSPI)**: PAIMANA is the client's own live production system with analytics already shipped, tracking 1,847 projects; public columns are outcomes, so "anticipated cost" leaks the answer; MoSPI has no SIH track record.
- **26073 (IMD)**: killed outright. The incumbent is the evaluating agency's own 24/7 operational quality control, plus free titanlib and NOAA MADIS, and no public labelled fault data exists.

## First actions

1. Confirm with the SPOC whether nomination binds the team to the problem statement filed internally, or whether it can change before the 20 September national submission. National rules choose the PS at national submission, so this may be local policy only.
2. Build the frame source as a swappable interface from commit one, so external .mp4 ingestion is native rather than retrofitted.
3. Implement the classical centroid plus Kalman baseline first and keep it as a reported headline result.
4. Instrument all six metrics from the start: simulation duration, FPS, acquisition time, average and maximum tracking error, lock retention rate, processing time. They are 60% of the marks and four of them are natural module owners for the four less-experienced teammates.
5. Put money in the deck. Half the final round in the one published SIH rubric is product plus commercial viability, and the argument here is real: this replaces expensive cameras, pan-tilt mechanisms and optical benches with software, which is ISRO's own stated motive.
