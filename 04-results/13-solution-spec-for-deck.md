# 13. The solution, specified. Hand this to whoever builds the deck.

For PS 26169. Mapped to the official six-slide template, field by field. Every number here was produced by running `round2/spike/fsoc_spike.py` on 2026-09-01, or quoted from ISRO's own annexure. Nothing here is aspirational.

**Template rules that are not negotiable:** six slides maximum including the title, the provided template only, do not change the idea-detail pointers, points and diagrams rather than paragraphs, export to PDF, no PPT accepted.

---

## Slide 1, title page

- Problem Statement ID: **26169**
- Problem Statement Title: **Development of an AI-Based Virtual Camera Tracking System for Coarse Alignment of Mobile Free Space Optical Communication (FSOC) Terminals**
- Theme: **Smart Automation**
- PS Category: **Software**
- Team ID / Team Name: as registered

## Slide 2, IDEA TITLE

**Idea title suggestion:** a name that says instrument, not demo. Something in the register of "an FSOC coarse-alignment testbed you can measure with."

**Proposed solution.** A software testbed that replaces the expensive cameras, pan-tilt mechanisms and optical benches normally needed to develop laser-terminal pointing algorithms. It generates a configurable virtual sky, flies a beacon through it, injects the disturbances a real terminal actually suffers, and closes a pointing loop around a detected and tracked beacon, reporting its own accuracy automatically.

**Detailed explanation, four points.**
1. Scene and sensor: a beacon rendered as a sub-pixel Gaussian spot, cropped to a 640x480 sensor at the commanded pan and tilt, with atmospheric contrast loss, camera jitter, platform motion and the noise families the annexure names.
2. Detection: median and MAD adaptive thresholding, impulse suppression, and two independent centroid estimators, so their disagreement becomes a free confidence signal.
3. Tracking: a constant-acceleration Kalman filter in a camera-compensated frame, with innovation gating so a noise spike cannot capture the track, and coasting on prediction so a brief dropout does not become a loss.
4. Control: rate-limited pan and tilt with the annexure's own slew cap, gimbal travel limits, and anti-windup.

**How it addresses the problem.** The problem statement's stated motive is an inexpensive, accessible platform for algorithm development and learning. The deliverable is therefore an instrument: every run emits the performance report the annexure asks for, so an ISRO engineer can evaluate a new tracking idea without touching hardware.

**Innovation and uniqueness, the three that are actually ours.**
- The frame source is swappable, so externally supplied video is a first-class input rather than a retrofit. **We already ran this path: 0.36 px mean error on frames the tracker had never seen.**
- The filter is ego-motion compensated, so it does not fight its own control loop. Measured effect: controller saturation fell from 92 percent to under 3 percent, and error fell from 113.95 px to 0.12 px.
- We report the classical baseline as a headline result, not a strawman. The annexure says "AI methods (if used)", so the honest comparison is compliant and is the stronger claim.

## Slide 3, TECHNICAL APPROACH

**Technologies.** Python. numpy and PIL for the core, which is the entire dependency list for the results below. AOtools or HCIPy for physically parameterised turbulence in the full build. A desktop GUI for the required standalone executable. No GPU, no cloud, no internet.

**Methodology.** Show the pipeline as a flow: `scene -> sensor -> detect -> track -> control -> log`, with the frame source drawn as a switch between the virtual camera and an external video file, because that switch is what earns Benchmark Performance-2.

**Put the evidence panel on this slide.** `round2/spike/evidence_panels.png`, four frames with the tracked centroid overlaid: clear at 0.14 px, fog with Poisson noise at 0.41 px, ten percent salt and pepper at 0.36 px, and the compound worst case failing honestly at 424 px. Caption it as measured, and name the four regimes.

**The results table, measured on 2026-09-01:**

| | result |
|---|---|
| scenarios meeting all five published targets | 7 of 11 |
| best mean tracking error | 0.09 px, about 10 microradians |
| acquisition time | 0.07 s against a 2 s target |
| re-acquisition after forced dropout | 0.80 s against a 1 s target |
| throughput | 33 to 42 FPS against a 20 FPS target |
| external-video path | 0.36 px, 5 of 5 targets |

## Slide 4, FEASIBILITY AND VIABILITY

**Feasibility.** A working end-to-end loop already exists and hits the targets. The remaining eight weeks go to physical fidelity, coverage and the interface, not to discovering whether it can be done.

**Challenges and risks, the three real ones. Name them specifically, because generic risks read as filler.**
1. **Rate saturation at the disturbance maxima.** ISRO's own table allows 20 px/frame of jitter, which at 30 fps is 3.75 deg/s against a 5 deg/s slew cap, a margin of 1.33 times before platform and target motion. Our worst case fails here, measured, at 92 percent saturation. Anyone claiming under 5 percent loss at full disturbance has not tested this corner.
2. **Turbulence realism.** Contrast reduction is what the annexure describes, but it is not defensible physics. This must move to Kolmogorov or von Karman phase screens parameterised by the refractive index structure constant.
3. **Detection under impulse noise**, not tracker speed, is the true failure mode. Our maximum error under ten percent salt and pepper is 451 px on isolated frames even though the mean is 11.68 px.

**Strategies.** For (1), characterise and publish the saturation boundary rather than hiding it, and add feed-forward from the estimated target velocity. For (2), rebuild on AOtools or HCIPy and validate the screen's structure function. For (3), multi-candidate association instead of a single peak.

## Slide 5, IMPACT AND BENEFITS

**Target audience.** ISRO engineers and students developing pointing, acquisition and tracking algorithms without access to an optical bench.

**Benefits, using the sponsor's own argument.** The annexure states that developing these algorithms on real hardware requires expensive cameras, pan-tilt mechanisms and optical components, and that a software testbed is the inexpensive alternative. The economic case is therefore ISRO's own: one testbed replaces per-student hardware, and algorithms can be regression-tested across hundreds of scenarios in minutes rather than in a lab queue.

**Scale.** Free-space optical communication is a live national capability area, and the coarse-alignment stage generalises across satellite, UAV and ground-terminal links.

## Slide 6, RESEARCH AND REFERENCES

- The official PS 26169 annexure, which carries the parameter table and the evaluation weightage.
- AOtools and HCIPy for Kolmogorov and von Karman phase screens and Fresnel propagation.
- Published work on centroid error decomposing into bias and jitter, and on the existence of an optimal exposure time.
- Published free-space optical terminal results for context: real terminals achieve about 10 microradians RMS pointing, against this problem statement's 10 px which is 1.09 mrad, confirming this is explicitly the coarse stage.

---

## Three things the deck must not do

1. **Do not claim formal verification anywhere.** The underlying CV wording is unsettled. The supportable and stronger claim is constrained-random verification with coverage closure.
2. **Do not hide the worst-case failure.** It is the single most credible thing on the slide, and half the final round's marks are product and viability judged by people who have seen a hundred flawless claims.
3. **Do not fill slide 3 with an architecture diagram alone.** Every team will have one. Almost none will have a measured number on data they did not choose.
