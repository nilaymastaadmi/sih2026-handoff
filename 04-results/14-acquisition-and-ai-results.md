# 14. Full-screen acquisition and the AI scorer, measured

Run 2026-09-02 on Nilay's machine. Execution status: verified locally (both runs
executed, exit 0; outputs in `spike-output/`). These two runs close the two gaps the
audit named: the acquisition-search hand-wave (A3 weakness 1) and "AI-assisted" being
a plan rather than a number (A3 weakness 2).

## 1. Full-screen acquisition CDF (`spike/acquisition_cdf.py`)

Setup: the annexure's minimum screen, 2000x2000 px = 12.5 x 12.5 degrees at the
spike's 0.00625 deg/px. Camera starts at centre seeing 640x480 (4 x 3 deg), beacon
spawns uniformly at random and drifts on a slow straight line (0.15 deg/s). Search:
expanding-square tile sweep, 15% overlap, at the 5 deg/s slew cap (the annexure's
tight end; it allows up to 10). Lock = the spike's own tracker confirming 3
consecutive SNR-floored detections. 500 seeded runs, 25 s cap each.

| quantity | value |
|---|---|
| runs | 500 |
| acquired within the 2 s target | **30% (149 of 500)** |
| median acquisition time, acquired runs | 2.37 s |
| p90 / p95 / max | 5.10 / 5.63 / 23.53 s |
| spawns inside the initial FOV (53 runs), median | 0.067 s |
| spawns outside the initial FOV, acquired (278 runs), median | 2.92 s |
| not acquired within 25 s by this baseline sweep | 169 runs (34%) |

Reading, for the deck and the jury:

1. **The 2 s target is met by 30% of blind random spawns at 5 deg/s.** In-FOV
   acquisition is 0.07 s (matching the scenario table); typical out-of-FOV
   acquisition is 2 to 6 s. This is geometry, not implementation: one full sweep of
   13 fields of view takes about 16 s at the cap, so no blind search can beat 2 s for
   a far spawn. Every competing team faces the same wall; this run measures it.
2. **The 34% timeout tail is a property of the baseline search, not a ceiling.** The
   failures are a moving beacon crossing tiles the sweep has already left. Named
   improvements, in order: the annexure-allowed 10 deg/s slew (halves sweep time),
   a velocity-aware re-sweep pattern, and a-priori spawn information (an uncertainty
   cone) when the scenario provides it.
3. Numbers live in `spike-output/acquisition_cdf.json`; the plot for the deck is
   `spike-output/acquisition_cdf.png`.

## 2. The AI component, A/B measured (`spike/ai_scorer.py`)

A numpy logistic regression on 21x21 patches (beacon point-spread function vs impulse
noise), trained on 16,000 self-generated labelled patches (99.7% training accuracy),
used to re-rank the top-6 candidate peaks in the detector. All 11 scenarios rerun
classical vs AI-assisted under identical conditions on the same machine.

| scenario | classical | AI-assisted |
|---|---|---|
| scenario grid, all 5 targets met | 7 of 11 | **8 of 11** |
| impulse noise 10% (annexure max), mean error | 11.68 px, 4/5 targets | **3.59 px, 5/5 targets** |
| same, p95 / max error | 60.26 / 451.6 px | 4.06 / 212.2 px |
| same, re-acquisition | 0.75 s | 0.23 s |
| all clean scenarios | reference | byte-identical outputs |
| random walk, low light | 39.0 px mean, 11.3% loss | 28.3 px mean, 22.0% loss (still 3/5) |
| all-maxima worst case | claims lock at 420 px mean error | abstains: 95% loss, 41.8 px when locked |

Reading:

1. **The AI flips the annexure-maximum impulse-noise case from fail to pass** and
   lifts the grid to 8 of 11. It changes nothing where the classical path already
   works, which is the honest meaning of "AI where the data says it pays".
2. **The worst-case behaviour is designed abstention.** Under all disturbance maxima
   the beacon is genuinely invisible on most frames; the classical detector "locks"
   onto noise (420 px mean error while claiming lock), the scorer declines to lock it
   cannot justify. A coarse-alignment stage that is confidently wrong feeds garbage to
   the fine stage; one that abstains hands over cleanly.
3. **Honest caveat, do not round it away:** random-walk-lowlight improves on error and
   worsens on loss, and remains a 3-of-5 scenario. The deck reports 8 of 11 and says
   nothing stronger. Full numbers: `spike/ai_scorer_results.json`.
