# 11. Build playbook for PS 26169

Written 2026-08-31. Derived from ISRO's published annexure plus a red-team simulation of an IIT photonics team entering the same problem statement. Read `09-final-decision.md` for why this problem statement, and `10-the-2026-bar.md` for the standard.

## 1. The strategic core, in one sentence

**Ship a measurement instrument, not a tracker.**

The red-team's answer to "how does a strong team lose this" was unambiguous: they build something that works beautifully on their own scene generator, then cannot cleanly ingest ISRO's supplied .mp4 or emit a log in the expected shape. That is 30 percent forfeited at the moment of evaluation with no recovery path.

## 2. Why our background beats an optics lab here

Benchmark Performance-2 is 30 percent of the marks and **it is an input/output and convention problem, not an optics problem.** ISRO supplies video at 30 fps and compares our centroid log against values they have already computed. What decides that score is origin convention, zero versus one indexing, y-down versus y-up, frame-index alignment and units.

That is a golden-model comparison problem. It is exactly the GPS L1 correlator validated against an independent C++ software model: 400 seeds, roughly 132,400 instructions, zero mismatches. A team with that discipline wins this band outright while an optics team is still tuning a point spread function. The photonics advantage does not apply to the 30 percent that separates entries.

Combined with Benchmark-1, **60 percent of the marks are scored from logs.** Treat the automatic performance log as a specification-conformant file format with its own validator, not as debug output.

## 3. The targets are not hard, so do not win there

Converting ISRO's own numbers: 4 degrees across 640 pixels is 0.00625 degrees per pixel, which is **109 microradians per pixel**. The 10-pixel tracking-error target is therefore **1.09 milliradians**, roughly 100 times looser than a real optical terminal such as TBIRD at about 10 microradians RMS per axis. The 2-second acquisition target sits between a 0.908-second published lab result and a 22-second on-orbit demonstration.

Conclusion: the numeric targets are coarse-stage and every serious team will hit them. **Nobody gets separated on the targets. Teams get separated on the rubric.** Do not spend the eight weeks chasing a better tracker; spend them on conformance, coverage and honest measurement.

## 4. Architecture, decided now and not revisited

One process, explicit module boundaries, every stage behind an interface:

`scene` produces a 2000x2000 canvas with the beacon rendered as a sub-pixel Gaussian spot, not a drawn square. `sensor` crops 640x480 at the current pan and tilt, applies blur, then the noise chain. `detect`. `track`. `control`. `log`.

**The single most important architectural decision: the frame source is a swappable interface from commit one.** Benchmark-2 requires bypassing our own virtual camera and ingesting external video. If the tracker is wired to an internal frame generator, that cannot be retrofitted in a 32-hour finale. Build `SceneFrameSource` and `Mp4FrameSource` against the same interface on day one and test both continuously.

Every disturbance injector is separately seeded, individually loggable and replayable. Runs must be byte-identical on rerun, so a judge can re-run our worst case and get our number.

## 5. Algorithms, with the classical baseline as a first-class result

Detection: background estimate, adaptive threshold, connected components, then **two independent centroid estimators**, a thresholded centre-of-gravity on a small window and a 2D Gaussian least-squares fit. Report both. The disagreement between them is a free turbulence-severity signal that costs nothing to compute.

Tracking: a constant-acceleration Kalman filter on position, velocity and acceleration, with measurement noise adapted from per-frame signal-to-noise, and **innovation gating** so a salt-and-pepper false blob cannot capture the track. Detection failure under 10 percent salt-and-pepper noise is the actual failure mode of this problem, not tracker speed.

Loss handling: coast on the predicted state for a few frames before declaring loss. That is what buys the sub-1-second re-acquisition target. Acquisition should be a spiral scan seeded from last known position, never a raster from a fixed corner, because acquisition tuned to the demo start position is the second most common way teams lose.

Control: two-axis proportional-integral with velocity feed-forward from the Kalman state, an explicit rate limiter at the 5 to 10 degrees per second cap, anti-windup, and a deliberate one-frame latency model so the loop is honest about delay.

The annexure says "AI methods (**if used**)". AI is optional. **Ship the classical centroid plus Kalman path as a headline reported result**, including the regimes where it beats anything learned. That both defuses the "what does a neural network buy here" question and sends a signal no appearance-optimised entry will send.

## 6. The finding to build a slide around

From ISRO's own parameter table: maximum camera jitter is 20 pixels per frame. At 30 fps that is 600 pixels per second, which at 0.00625 degrees per pixel is **3.75 degrees per second**. The camera pan and tilt cap is 5 to 10 degrees per second. At the 5 degrees per second setting the margin is only **1.33 times**, before adding platform motion at another 20 pixels per frame and the target's own motion. The commanded rate saturates in the worst case.

Any team claiming under 5 percent target loss at worst-case disturbance without addressing rate saturation has not tested that corner. We should characterise it, plot where saturation begins, and state it. This is a question we can ask ourselves and answer with a number, and it is the kind of question that ends a rival's Q and A.

## 7. Coverage, not a demo video

Four motion types by four target sizes by five atmospheric conditions by three noise types is **240 scenario cells**. Run them, report coverage against that grid, and publish the cells that fail. This is constrained-random verification with coverage closure applied to scenario space, which is a practice this team demonstrably has and almost no student team brings.

Statistics: tracking error across frames is heavily autocorrelated, so naive per-frame standard errors are inflated. Correct for it and say why. Report the 95th percentile of acquisition time across seeds, not a lucky run. If several tracker variants are tried, remember that four attempts make one apparent winner likely by chance, and pre-register which comparison counts.

## 8. Mistakes the red-team predicts we will make

Read these as directed at us specifically.

1. Over-investing in tracker speed when detection under heavy salt-and-pepper noise is the real failure mode.
2. Building an RTL or FPGA path nobody asked for. The deliverable is a standalone executable.
3. Treating the GUI as decoration. Functional Verification is 20 percent and names the GUI explicitly.
4. Writing a report that reads as a verification plan with no optics vocabulary. That costs real points with an SAC optics engineer. The report must speak in refractive-index structure constant, Fried parameter, angle-of-arrival jitter, centroid bias versus jitter, and an explicit pixel-to-angle conversion.
5. Claiming a ranking among tracker variants that is really noise.

## 9. A claim we must not make

**Do not write "formal verification" in any SIH report, deck or pitch.** The underlying CV wording is flagged as re-opened and unsettled in the working notes, and an unsupported claim in a competition document is a needless risk. The supportable and stronger claim is constrained-random verification with coverage closure, which has hard numbers behind it: 400 seeds, roughly 132,400 instructions, zero mismatches, with coverage reported honestly at 91.7 percent line, 71.0 percent branch and 68.7 percent toggle.

## 10. Six roles, non-overlapping

Winners assign six named distinct roles including a business and presentation owner. Mapped to this build:

1. Scene and sensor model, including the physically defensible disturbance chain.
2. Detection and centroiding, both estimators.
3. Tracking filter, gating and loss or re-acquisition logic.
4. Control loop, rate limiting and latency model.
5. GUI, live parameter controls and the real-time statistics display.
6. Log schema, the golden-model comparator, the coverage harness, the report and the pitch.

Role 6 is the one that wins the 60 percent, and it is the role most teams will not staff at all.

## 11. What goes in the 2 September deck

Six slides including the title, PDF only, official template unmodified.

Slide 2 must open with the sentence a screener remembers, and it should be about being measurable, not about lasers. Slide 3 needs a real screenshot: even a first-pass beacon tracked through injected noise with a live error trace beats any architecture diagram. Slide 4 names three specific risks, and rate saturation at worst-case jitter is the one that proves we read the annexure. Slide 5 carries the money argument, which ISRO hands us: this replaces expensive cameras, pan-tilt mechanisms and optical benches with software, which is the sponsor's own stated motive. Slide 6 cites the annexure, AOtools or HCIPy, and two real papers on centroid bias and turbulence parameterisation.

The one thing to get onto slide 3 before 2 September is a screenshot of something actually running.
