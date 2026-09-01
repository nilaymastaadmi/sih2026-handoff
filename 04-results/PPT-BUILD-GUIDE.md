# PPT build guide: the 26169 IDEA deck, step by step

Written 2026-09-02 for the teammate building the deck. Everything you need is in this
repository. This is manual work with no room for invention: **every sentence you need
is written below, every number is measured, and section 8 tells you where each number
comes from.** If you find yourself writing a new claim or a new number, stop; that is
not your job tonight. Formatting judgement (fitting text, nudging boxes) is yours.

## 0. Inputs

| file | role |
|---|---|
| `01-research/SIH2026-IDEA-Format.pptx` | the official template. Start from a COPY of this file |
| `04-results/spike-output/evidence_panels.png` | goes on slide 3 |
| `04-results/spike-output/acquisition_cdf.png` | goes on slide 4 |
| this guide | all text and the table, copy-paste |

Save your working copy as `SIH2026-26169-BeaconBench.pptx`. Final deliverable is a
**PDF export of exactly 6 slides**.

## 1. Golden rules (from the template's own instruction slide, and our audit)

1. Maximum 6 slides INCLUDING the title slide. The template's 7th slide is the
   instruction slide: **delete it before export** (step 7).
2. Do not change the slide headings or the printed field labels ("Proposed
   Solution...", "Detailed explanation...", etc.). Content goes UNDER each label.
3. Points and images, never paragraphs.
4. Export to PDF. PPT uploads are not accepted.
5. Do not alter any number from this guide, and do not round 8-of-11 upward, ever.
   The honest failure rows are deliberate; they are our credibility exhibit.
6. The small "Your Team Name" oval on slides 2 to 6: put the registered team name in
   it (or delete the oval on every slide consistently; pick one, apply to all five).
7. Footers and slide numbers: leave untouched.

## 2. Slide 1 (title)

Fill the existing text box lines exactly:

```
Problem Statement ID – 26169
Problem Statement Title- Development of an AI-Based Virtual Camera Tracking System
for Coarse Alignment of Mobile Free Space Optical Communication (FSOC) Terminals
Theme- Smart Automation
PS Category- Software
Team ID- <registered Team ID>
Team Name (Registered on portal)- <registered name>
```

The two `<...>` items are the ONLY things in this deck that come from you, from the
portal registration. Everything else is in this guide.

## 3. Slide 2 (IDEA TITLE)

At the top of the content area, one line, larger and bold:

```
BeaconBench: an FSOC coarse-alignment testbed you can measure with
```

Under **Proposed Solution (Describe your Idea/Solution/Prototype)** put these 2 bullets:

```
• ISRO published five numeric performance targets for this problem; our testbed
  already meets all five on video it had never seen, at 0.36 px mean error.
• A software instrument replacing the cameras, pan-tilt mounts and optical benches
  needed to develop laser-terminal pointing: configurable virtual sky, beacon flown
  through the annexure's full disturbance set, AI-assisted detect-and-track loop,
  automatic self-grading on every run.
```

Under **Detailed explanation of the proposed solution**, 5 bullets:

```
• Scene + sensor: sub-pixel Gaussian beacon on a 2000x2000 px screen; 640x480 sensor
  cropped at the commanded pan/tilt; annexure disturbances (noise, jitter, platform
  motion, atmosphere).
• Acquisition: expanding-square search at the slew cap, reported as a time CDF over
  500 random spawns, not a single lucky number.
• Detection: adaptive median-MAD threshold + a learned spot scorer for impulse-noise
  frames; two independent centroiders whose disagreement is a confidence signal.
• Tracking: ego-motion-compensated constant-acceleration Kalman filter with
  innovation gating and coasting. Control: rate-limited pan-tilt with anti-windup.
• Logging: every run emits the annexure's performance report automatically.
```

Under **How it addresses the problem**, 1 bullet:

```
• The sponsor's stated motive is an inexpensive, accessible platform for algorithm
  development; this is that platform, scoring itself with the exact metrics the
  annexure names.
```

Under **Innovation and uniqueness of the solution**, 3 bullets:

```
• Swappable frame source: external .mp4 is a first-class input, already measured at
  0.36 px on unseen frames (Benchmark Performance-2 is 30% of the marks).
• AI where the data says it pays: a learned spot scorer takes the annexure's 10%
  salt-and-pepper maximum from failing to passing all 5 targets (mean error
  11.7 → 3.6 px, p95 60.3 → 4.1 px), leaves clean scenarios untouched, and abstains
  rather than lock on noise at the all-maxima extreme. Grid: 7 → 8 of 11.
• A published failure boundary, derived from ISRO's own disturbance maxima.
```

Fitting: labels bold ~13 pt, bullets ~11 to 12 pt. If it overflows, shrink bullets to
10.5 pt before cutting any bullet; if you must cut, cut the logging bullet first.

## 4. Slide 3 (TECHNICAL APPROACH)

Left half, under **Technologies to be used**:

```
• Python, numpy, PIL: the entire dependency list for every number on this slide.
  AOtools/HCIPy phase screens for the physics mode. Desktop GUI packaged as a
  standalone executable. No GPU, no cloud, no internet.
```

Under **Methodology and process for implementation**:

```
• scene → sensor → [ virtual camera | external .mp4 ] → detect → track → control → log
• The switch is the architecture: Benchmark Performance-2 supplies .mp4 files, and an
  open-loop external path cannot be retrofitted into a monolithic simulator.
```

If you have 20 spare minutes, redraw the first bullet as a proper left-to-right chevron
flow diagram with the frame-source switch drawn as a two-way branch; the arrow-text
line is the acceptable fallback.

Right half, top: insert `evidence_panels.png`, width ~6.3 in. Caption under it, small:

```
Four measured regimes, tracked centroid overlaid: clear 0.14 px, fog+Poisson 0.41 px,
salt & pepper 10% 0.36 px, compound worst case failing honestly at 424 px.
```

Bottom, full width: insert a 3-column table with EXACTLY these 10 rows (~10 pt):

| Result (measured, replicated on a 2nd machine) | value | target |
|---|---|---|
| External video path (BP-2 rehearsal) | 0.36 px mean, 5/5 targets | err ≤ 10 px |
| Best mean tracking error | 0.09 px (≈10 µrad) | ≤ 10 px |
| Acquisition, beacon in FOV | 0.07 s | ≤ 2 s |
| Full-screen acquisition, 500 random spawns | 30% within 2 s; median 2.37 s, p95 5.63 s | ≤ 2 s |
| Re-acquisition after forced dropout | 0.80 s | ≤ 1 s |
| Impulse noise 10% (annexure max): classical → +AI scorer | 11.7 → 3.6 px mean; 4/5 → 5/5 targets | ≤ 10 px |
| Scenario grid, all 5 targets met | classical 7/11, AI-assisted 8/11 | |
| Throughput (two machines) | 24–61 FPS | ≥ 20 FPS |
| All-maxima compound case | fails: beacon not visible above noise; boundary published | |

Make the last row's value cell dark red. Everything else default ink.

## 5. Slide 4 (FEASIBILITY AND VIABILITY)

Left ~60%, under **Analysis of the feasibility of the idea**:

```
• An end-to-end loop exists and was independently rerun during audit with identical
  numbers. Remaining work is physical fidelity, coverage (240-cell scenario grid),
  the GUI executable and the report; not discovery.
```

Under **Potential challenges and risks**, 3 bullets:

```
• Full-screen acquisition: a blind sweep of the 2000x2000 screen cannot finish in 2 s
  at the 5 deg/s slew cap (~13 fields of view, one sweep ≈ 16 s). Acquisition is a
  search-strategy problem, and we measured it: 30% of 500 random spawns acquire
  within 2 s; a moving beacon evades the baseline sweep in 34% of runs.
• Rate saturation: 20 px/frame of jitter at 30 fps is 3.75 deg/s against a 5 deg/s
  cap; our compound worst case fails here, measured.
• Turbulence realism: contrast reduction is compliant but not physics.
```

Under **Strategies for overcoming these challenges**, 3 bullets:

```
• Search: the annexure-allowed 10 deg/s slew halves sweep time; a velocity-aware
  re-sweep targets the 34% evasion tail; a-priori spawn information (uncertainty
  cone) when the scenario provides it. The CDF is republished after each change.
• Saturation: publish the boundary instead of hiding it; add feed-forward from
  estimated target velocity.
• Turbulence: Kolmogorov phase screens already built and validated (structure-
  function exponent 1.652 vs 5/3 at L/r0 = 102); being wired into the scenario table.
```

Right ~40%: insert `acquisition_cdf.png`, width ~4.9 in. Caption under it:

```
Full-screen acquisition CDF, 500 random spawns: every competing team faces this
geometry; we are the ones who measured it.
```

## 6. Slide 5 (IMPACT AND BENEFITS)

Under **Potential impact on the target audience**, 2 bullets:

```
• ISRO engineers and students develop and regression-test pointing, acquisition and
  tracking algorithms in minutes on a laptop instead of queueing for an optical bench.
• The annexure itself states the hardware this replaces: expensive cameras, pan-tilt
  mechanisms, optical components and equipment.
```

Under **Benefits of the solution (social, economic, environmental, etc.)**, 3 bullets:

```
• Economic: one testbed replaces per-student hardware; hundreds of scenarios
  regression-tested in minutes rather than a lab queue.
• Strategic: FSOC is a live national capability area. ISRO LEOS lists optical
  communication among its next-generation technologies; MeitY/ERNET already runs an
  FSOC connectivity pilot at Kohima.
• Educational: an accessible instrument for exactly the algorithm development and
  learning the problem statement describes.
```

## 7. Slide 6 (RESEARCH AND REFERENCES), then finish

Under **Details / Links of the reference and research work**, 9 bullets (~12 pt):

```
• PS 26169 specification annexure (parameters, evaluation weightage), via the
  official portal Dataset Link: drive.google.com/file/d/1AWRWChSMKU8FI38XxfFyQJfCRp3gqkF6
• SIH 2026 portal and guidelines: sih.gov.in/sih2026PS
• arXiv 2508.08950: mobile FSO terminal acquisition, mean 0.908 s, all trials < 1 s
• arXiv 2309.10999: pointing-and-acquisition algorithms with simulation for
  aircraft FSO links
• arXiv 2304.02804: lidar-assisted coarse acquisition of mobile FSO terminals
• SPIE 9354: MIT NODE, pointing-acquisition-tracking for a CubeSat optical module
• AOtools (LGPL-3.0) and HCIPy (MIT): Kolmogorov / von Karman phase screens,
  Fresnel propagation
• ISRO LEOS, optical communication under next-generation technologies:
  isro.gov.in/LEOS.html
• MeitY/ERNET FSOC pilot, Kohima: ernet.in/projects/fsoc.html
```

Then: **delete slide 7** (the instructions slide). Confirm the deck is 6 slides.
File → Export → PDF. Open the PDF and page through all 6 before handing it over.

## 8. Where every number comes from (verify, don't trust)

| number on the deck | source in this repo |
|---|---|
| 0.36 px external video, 5/5 | `04-results/12-spike-results.md` table, external video row |
| 0.09 px best mean error | same file, straight-line-haze row |
| 0.07 s in-FOV acquisition; 0.80 s re-acq | same file |
| 30% within 2 s; median 2.37 s; p95 5.63 s; 34% evasion | `04-results/spike-output/acquisition_cdf.json` (`fraction_within_2s` 0.298, `median_s` 2.367, `p95_s` 5.633, `timeouts_over_25s` 169/500) |
| 11.7 → 3.6 px; p95 60.3 → 4.1; 4/5 → 5/5; grid 7 → 8 of 11 | `04-results/spike/ai_scorer_results.json` and `04-results/14-acquisition-and-ai-results.md` |
| 24–61 FPS two machines | `12-spike-results.md` (33–42) plus the audit rerun (24.3–60.6), `03-audit/A1-ledger-check.md` claim 33 |
| exponent 1.652 vs 5/3 at L/r0 = 102 | `12-spike-results.md` section 6, replicated in A1 |
| 20/30/30/20 weights, 5 targets, .mp4 bypass | `01-research/PS26169-annexure-ISRO.pdf` pages 1 to 3 |
| panel captions 0.14 / 0.41 / 0.36 / 424 px | `13-solution-spec-for-deck.md` slide 3 section |

To regenerate any of them: `cd 04-results/spike` then `python fsoc_spike.py`,
`python ai_scorer.py`, `python acquisition_cdf.py` (slow), `python test_finite_screen.py`.

## 9. Final checklist (second reader runs this, not the builder)

- [ ] Exactly 6 slides; instruction slide gone
- [ ] PDF export, not PPT; all 6 pages render, images sharp
- [ ] Slide 1: PS ID 26169, exact official title, Smart Automation, Software, real
      Team ID and Team Name (no `<...>` left anywhere)
- [ ] Slide 2 opens with the BeaconBench line and the 0.36 px sentence
- [ ] "AI" appears with a measured number (the 11.7 → 3.6 px bullet), and nothing
      reads as classical-instead-of-AI
- [ ] Both failure rows present (all-maxima case, 34% evasion tail); nobody softened them
- [ ] The grid says 8 of 11 and NOT more
- [ ] Every number matches section 8's source files
- [ ] Field labels and slide headings unmodified
- [ ] Uploaded well before the deadline, receipt confirmed
