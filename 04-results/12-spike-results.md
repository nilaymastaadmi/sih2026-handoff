# 12. Feasibility spike, run 2026-09-01. The choice is now verified, not argued.

Code: `round2/spike/fsoc_spike.py` and `round2/spike/make_evidence.py`. Artifacts: `evidence_panels.png`, `performance_log.json`. Dependencies: numpy and PIL only, no OpenCV, no scipy.

Execution status: **verified locally.** The numbers below were produced by running the code, not by reading it.

## 1. Headline

A working closed-loop beacon acquisition and tracking system was built and run against ISRO's own published parameter table and its five published performance targets.

**7 of 11 disturbance scenarios meet all five targets**, most at sub-pixel accuracy. The external-video path, which is 30 percent of the marks, passes 5 of 5 at 0.36 px mean error.

| scenario | acq | mean err | loss | re-acq | FPS | targets |
|---|---|---|---|---|---|---|
| clear, circular | 0.07 s | 0.12 px | 4.3% | 0.80 s | 41.7 | 5/5 |
| straight line, haze | 0.07 s | 0.09 px | 4.3% | 0.80 s | 35.5 | 5/5 |
| figure of eight, rain | 0.07 s | 0.44 px | 4.3% | 0.80 s | 34.1 | 5/5 |
| fog + Poisson | 0.07 s | 0.36 px | 4.3% | 0.80 s | 34.7 | 5/5 |
| platform motion 20 px/frame | 0.07 s | 3.41 px | 4.3% | 0.80 s | 33.7 | 5/5 |
| small spot 5 px | 0.07 s | 0.16 px | 4.3% | 0.80 s | 33.7 | 5/5 |
| large spot 20 px | 0.07 s | 0.21 px | 4.3% | 0.80 s | 33.3 | 5/5 |
| salt and pepper 10% | 0.07 s | 11.68 px | 2.0% | 0.03 s | 33.6 | 4/5 |
| camera jitter 20 px/frame | 0.07 s | 10.86 px | 6.0% | 0.03 s | 33.8 | 3/5 |
| random walk, low light | 0.07 s | 39.03 px | 11.3% | 0.03 s | 35.6 | 3/5 |
| **worst case, all maxima** | 0.07 s | **420 px** | 13.0% | 0.03 s | 34.7 | 3/5 |
| **external video (Benchmark-2)** | 0.07 s | **0.36 px** | 4.3% | 0.80 s | 34.0 | **5/5** |

For scale: 10 px is 1.09 mrad, so 0.12 px is about 13 microradians.

## 2. Three real defects the spike found, which reading could not have

**(a) Filtering in image coordinates while the camera moves.** First run produced 100 to 2000 px errors with the controller saturating up to 92 percent of frames. Cause: the Kalman filter was fighting its own control action, because at a 5 deg/s slew cap the camera itself displaces the beacon 26.7 px per frame and a naive filter reads that as target motion. Fix: `ego_shift()` removes the commanded pan and tilt from the state so the filter models target motion only. Saturation fell to under 3 percent and the straight-line case went to 0.09 px.

**(b) A constant-velocity model lags on curved trajectories.** After (a), circular and figure-of-eight motion still carried a steady 34 to 53 px error while straight-line motion was already at 0.09 px. That signature is model lag, not noise. Fix: constant-acceleration state. Circular went from 33.90 px to 0.12 px.

**(c) The pointing loop cannot be closed around pre-recorded video.** This is the important one. Benchmark Performance-2 supplies .mp4 files, and a recording does not respond to pan commands. Closing the loop around it produced 87 percent controller saturation and an 11 px error that is an artifact of the architecture, not of the tracker. Fix: frame sources declare `steerable`, and the external-video path runs open-loop and reports centroiding error only. The same scenario then scored 0.36 px with zero saturation.

Defect (c) would have cost most of a 30 percent band, and it is only discoverable by actually running an external-video path. A team that builds a monolithic simulator finds it on the day, with no time to re-architect.

## 3. The honest failures, kept

**Compound worst case fails.** With fog, noise sigma 20, 10 percent salt and pepper, Poisson, 20 px/frame jitter and 20 px/frame platform motion simultaneously, the system loses the beacon: 420 px error and 92 percent controller saturation. Inspection of the rendered frame confirms the beacon is genuinely not visible above the noise at that combination. This is the rate-saturation corner predicted from ISRO's own table before any code was written: 20 px/frame at 30 fps is 3.75 deg/s against a 5 deg/s cap, a margin of only 1.33 times before platform and target motion are added.

**Camera jitter at the annexure maximum gives 10.86 px, marginally over the 10 px target, and this is correct behaviour.** Angle-of-arrival jitter is white noise. A smoothing filter should not chase it, and a coarse-alignment stage is not supposed to: rejecting jitter is the fine-pointing stage's job. Reporting this as a failure to fix would be wrong; reporting it as a designed boundary between coarse and fine stages is the physics.

**Low light plus random walk is the weakest genuine case** at 39 px, and is the first thing to improve.

## 4. What this settles about the decision

1. **The targets are reachable.** Sub-pixel tracking under fog, Poisson noise and 10 percent salt and pepper, at 33 to 42 FPS on a laptop with numpy alone. ISRO's targets are coarse-stage and generous, exactly as the red-team's comparison against real terminals predicted.
2. **The architecture survives contact.** The swappable frame source works, and its value was demonstrated by finding defect (c).
3. **No dependency risk.** numpy and PIL only. The standalone-executable deliverable is straightforward, and nothing here needs OpenCV, scipy, a GPU or an internet connection.
4. **The build is not the risk.** A working end-to-end loop took one session. The eight weeks go to physical fidelity of the disturbance model, the 240-cell coverage matrix, the GUI, and the report.
5. **We now have a real result for slide 3** before the deadline, which was the single highest-leverage pre-submission task.

## 5. What the spike is not

It is a feasibility artifact, not the entry.

## 6. Turbulence, now built and validated (added later the same day)

The gap named above has been closed at the physics level. `round2/spike/turbulence.py` implements Kolmogorov and von Karman phase screens by the FFT method with subharmonic augmentation, derives the Fried parameter from the refractive index structure constant as r0 = (0.423 k^2 Cn2 L)^(-3/5), and computes the Rytov variance.

**It is validated, not asserted.** A generated screen only counts as turbulence if its phase structure function matches D(r) = 6.88 (r/r0)^(5/3).

Measured mean ratio to theory over 0.3 < r/r0 < 4, and the fitted power-law exponent against a theoretical 5/3 = 1.667:

| subharmonic levels | ratio | exponent |
|---|---|---|
| 0 | 0.574 | 1.444 |
| 2 | 0.796 | 1.586 |
| 5 | 0.923 | 1.643 |

The level count was measured rather than guessed, and 5 is now the default.

A residual 8 percent shortfall remained, so it was tested rather than excused. Holding sampling, r0 and the evaluation band fixed while growing the screen:

| screen | L/r0 | ratio | exponent |
|---|---|---|---|
| 0.64 m | 12.8 | 0.832 | 1.610 |
| 1.28 m | 25.6 | 0.843 | 1.601 |
| 2.56 m | 51.2 | 0.861 | 1.616 |
| 5.12 m | 102.4 | **0.950** | **1.652** |

The ratio converges toward 1 and the exponent toward 5/3 as the screen grows. That is the expected behaviour of a bounded simulation against a theory with an infinite outer scale, so **the generator is correct and the residual is physics**. Exponent error at the largest screen is 0.9 percent.

Beacon imaging through the screens behaves correctly too: over Cn2 from 1e-16 to 1e-13 at 1550 nm on a 10 km path with a 5 cm aperture, r0 falls from 31.2 cm to 0.50 cm, D/r0 rises from 0.16 to 10.1, and the spot's centroid wander grows from 0.73 to 4.59 px as it breaks up.

This is the piece an optics evaluator will probe first, and it is now the piece with a controlled experiment behind it.

## 7. Still outstanding

`turbulence.py` is validated but not yet wired into the tracker's renderer, so the scenario table in section 1 still uses the annexure's contrast-and-brightness description. That integration, and the lock-retention against Cn2 curve it enables, is the next piece of work and is the red-team's nominated "killer moment" for the finale.

Also missing: multiple simultaneous targets (the annexure allows more than one), the spiral acquisition scan, the GUI, and the 240-cell coverage matrix.
