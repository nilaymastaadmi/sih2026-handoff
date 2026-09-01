# PS 26169 spike, verified 2026-09-01

numpy and PIL only. No OpenCV, no scipy, no GPU, no network.

| file | what it does |
|---|---|
| `fsoc_spike.py` | closed-loop beacon acquisition and tracking against ISRO's published parameter table and its five performance targets |
| `make_evidence.py` | writes `evidence_panels.png` and `performance_log.json` |
| `turbulence.py` | Kolmogorov and von Karman phase screens, plus the structure-function validation |
| `tune_subharmonics.py` | measures how many subharmonic levels the generator needs |
| `test_finite_screen.py` | controlled test proving the residual deficit is the finite screen, not a bug |

## Results

**Tracking, 7 of 11 disturbance scenarios meet all five published targets.** Best mean error 0.09 px (about 10 microradians), acquisition 0.07 s against a 2 s target, re-acquisition 0.80 s against 1 s, 33 to 42 FPS against 20. The external-video path, which is 30 percent of the finale marks, scores 0.36 px and passes 5 of 5.

**Turbulence, validated rather than asserted.** The phase structure function is compared against Kolmogorov theory, D(r) = 6.88 (r/r0)^(5/3):

| subharmonic levels | mean ratio to theory | fitted exponent |
|---|---|---|
| 0 | 0.574 | 1.444 |
| 2 | 0.796 | 1.586 |
| 5 | 0.923 | 1.643 |

and with 5 levels, as the screen grows at fixed sampling and fixed evaluation band:

| screen | L/r0 | mean ratio | fitted exponent |
|---|---|---|---|
| 0.64 m | 12.8 | 0.832 | 1.610 |
| 1.28 m | 25.6 | 0.843 | 1.601 |
| 2.56 m | 51.2 | 0.861 | 1.616 |
| **5.12 m** | **102.4** | **0.950** | **1.652** |

Theory is 1.667, so the exponent is within 0.9 percent. The ratio converging toward 1 as the screen grows demonstrates that the residual shortfall is the finite outer scale of a bounded simulation, which Kolmogorov theory does not have, rather than an error in the generator.

## Three defects the spike found

1. **Filtering in image coordinates while the camera slews.** The filter fought its own control action: at a 5 deg/s cap the camera displaces the beacon 26.7 px per frame. Ego-motion compensation dropped controller saturation from 92 percent to under 3 percent and error from 113.95 px to 0.12 px.
2. **Constant-velocity lag on curved paths.** Straight-line motion was already at 0.09 px while circular sat at 33.90 px, which is a model signature, not noise. A constant-acceleration state took circular to 0.12 px.
3. **A pointing loop cannot be closed around pre-recorded video.** Benchmark Performance-2 supplies .mp4 files that do not respond to pan commands. Closing the loop gave 87 percent saturation and a meaningless error; running that path open-loop gives 0.36 px and zero saturation. This is worth most of a 30 percent band and is only findable by building the external path.

## Known limitations

The tracker's scene renderer still uses the annexure's contrast-and-brightness description of atmosphere. `turbulence.py` is validated but not yet wired into `fsoc_spike.py`; that integration, plus the resulting lock-retention against Cn2 curve, is the next piece of work. Also outstanding: multiple simultaneous targets, the spiral acquisition scan, the GUI, and the 240-cell coverage matrix.
