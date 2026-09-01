# A4: the improved pitch

Audit session, 2026-09-01. One fix per A3 weakness, then the rebuilt pitch assets.
Owners: "E1" = Nilay, "E2" = second strong engineer, "T3-T6" = the four other
teammates, named by the team tonight. Dates assume the internal deck freezes the
evening of 2026-09-02.

---

## The eight fixes

**Fix 1 (for A3-1, the acquisition search).** Action, not text: add a full-screen
acquisition mode to the spike. Scene 2000x2000 px (+/-6.25 deg), camera starts centred,
beacon spawns uniformly at random, expanding-square search at the slew cap until first
detection, then hand over to the tracker. Run 500 spawns, output the acquisition-time
CDF and the fraction acquired within 2 s. Owner: E1. Date: run tonight, 2026-09-01,
results into the deck 2026-09-02 morning. Cost: 0.5 to 1 person-day. Until the run
exists, the deck's acquisition row reads: "acquisition (in-FOV) 0.07 s; full-screen
random-spawn acquisition reported as a CDF, measured, not assumed." **This is also the
single prep task that most increases our odds** (see below).

**Fix 2 (for A3-2, AI positioning).** Replacement text. Slide 2 innovation bullet 3
becomes: "AI where the data says it pays: detection under impulse noise is our measured
failure mode (worst frame 451 px at 10% salt-and-pepper), so a learned detector scores
candidate spots and a classical centroid-plus-Kalman spine tracks them; the deck
reports both, per scenario, as the annexure's technical report requires." Nothing in
the deck may read as "classical instead of AI"; everything reads "AI where measured,
classical where measured, numbers for both."

**Fix 3 (for A3-3, the wedge).** The wedge sentence, verbatim, opening slide 2:
**"ISRO published five numeric performance targets for this problem; our testbed
already meets all five on video it had never seen, at 0.36 pixels mean error."**
The judge-to-judge form this compresses to is "they already pass ISRO's own published
benchmarks", which is one clause and survives retelling.

**Fix 4 (for A3-4, the number).** Replacement ordering for the slide 3 table: row 1
external video 0.36 px 5-of-5 (the 30% band), row 2 best tracking 0.09 px (~10 urad),
row 3 acquisition per fix 1, row 4 the honesty row: "all-maxima compound case: fails at
420 px, 92% controller saturation, boundary published." The 7-of-11 grid moves to the
caption of the evidence panel. FPS gets pinned: "24 to 61 FPS across two machines
(i5 laptop, desktop), floor 24 FPS against the 20 FPS target" — replicated numbers
only, no single-machine range presented as universal. Owner: whoever builds the deck
(T6 drafts, E1 signs off). Date: 2026-09-02.

**Fix 5 (for A3-5, references).** Replacement slide 6 list, every line resolved during
this audit on 2026-09-01 (fetcher in brackets; "me" = this audit session directly):

- PS 26169 annexure, via the portal Dataset Link (drive.google.com/file/d/1AWRWChSMKU8FI38XxfFyQJfCRp3gqkF6) [me, hash-verified against 2 fetch dates]
- Guidelines and portal, sih.gov.in/sih2026PS [me, live]
- Kani et al., "Seamless acquisition strategies for mobile FSO terminals", arXiv 2508.08950: real terminal, mean acquisition 0.908 s, all trials under 1 s [audit agent]
- arXiv 2309.10999 (pointing-and-acquisition algorithms with simulation, gateway-aircraft FSO) and arXiv 2304.02804 (lidar-assisted coarse acquisition, acquisition-time optimisation) [audit agent]
- MIT NODE PAT line: SPIE 9354, "Development of a pointing, acquisition, and tracking system for a CubeSat optical communication module" [audit agent]
- AOtools (LGPL-3.0) and HCIPy (MIT) for Kolmogorov/von Karman phase screens and Fresnel propagation [named in package; licence status as recorded there]
- ISRO LEOS, optical communication under next-generation technologies, isro.gov.in/LEOS.html; ERNET/MeitY FSOC pilot, Kohima, ernet.in/projects/fsoc.html [audit agent] — these two also back slide 5's "live national capability" line

**Fix 6 (for A3-6, unowned tasks).** Assignments, tonight: role 5 (GUI, standalone
executable, 20+ FPS live display) gets a named owner from T3-T6 with E2 as backstop,
and a packaging smoke test (PyInstaller one-window build showing a moving beacon) due
2026-09-07, five days in, not December. Role 1's physics half: E2 wires the validated
`turbulence.py` into the scenario table and reruns the 11 scenarios, due 2026-09-05;
until then no document pairs the 7-of-11 table with the Kolmogorov validation in one
breath (GAPS 5 stays flagged). Role 6 (logs, comparator, coverage, report) is E1's
after the fix-1 run.

**Fix 7 (for A3-7, obscurity leaning).** Replacement framing line for every internal
document and the pitch: "Assume every serious team has read the annexure by the finale.
Our edge is what a reader cannot copy by 20 September: measured results, a published
failure boundary, a physics-validated turbulence model, and an architecture that
already ingests external video." Delete "only visible to a team that opened the
annexure" as a load-bearing argument anywhere it appears.

**Fix 8 (for A3-8, runner-up and hedge).** Decision text: the runner-up is **26228**
(scored 74, second in the artifact table; its audit position improved: no shipped
product binds inference outputs to model and data lineage end-to-end, and published
backdoor detection is 0.90+ AUC on known attacks while near-chance on novel ones, which
is a better wedge than the one the package retired). **Scope correction from Nilay,
2026-09-02: the BITS internal round allows one PS per team**, so the hedge is not an
internal-round action. The guidelines' two-ideas line (page 16) governs the national
portal submission by a nominated team. Revised action: pitch 26169 alone internally;
if nominated, ask the SPOC whether a second idea can be filed on the portal by 20
September, and only then does T6 draft the 26228 deck from `00-RECOMMENDATION.md`
section 3's twelve fields with the two corrected claims above. This folds into A0 open
item 1 (the SPOC question now carries both the binding question and the second-idea
question). The 09/artifact runner-up contradiction is still closed by this paragraph.

---

## The revised three-panel demo spine (deck panels; the internal round is deck-only)

1. **Panel 1, the instrument.** GUI frame: virtual sky, tracked beacon, live metric
   strip. The number on the panel: **0.09 px mean tracking error, about 10
   microradians, through haze**.
2. **Panel 2, the external-video path.** Foreign .mp4 in, same tracker, no code change,
   open loop by design. The number: **0.36 px, 5 of 5 published targets, on frames the
   tracker had never seen**.
3. **Panel 3, the boundary.** The compound worst case failing honestly, with the
   saturation math from ISRO's own table. The numbers: **7 of 11 scenarios pass all
   five targets; the all-maxima case fails at 420 px and we publish the boundary**.

## The revised evidence plan

Only sources resolved during this audit, each with its resolution status: the annexure
(me, byte-identical across 2026-08-31 and 2026-09-01 fetches, linked live from the
official portal); the live portal itself (me, full page saved); the spike numbers (me,
independently rerun on this machine today, all replicated except machine-dependent FPS);
the turbulence validation (me, rerun, exponent 1.652 replicated exactly); the FSOC
literature and ISRO/ERNET capability pages (audit agents, URLs in fix 5). Dropped from
the evidence plan: nothing, but every "published work on X" placeholder is now a
specific citation or it does not ship.

## The one prep task that most increases our odds

**Fix 1, the full-screen acquisition run. Cost: 0.5 to 1 person-day (E1, tonight).**
It converts the pitch's most attackable number into its most distinctive one. No other
team will show an acquisition-time CDF over random spawns, because no other team will
have noticed the screen-versus-FOV geometry in time; it is simultaneously the answer to
the domain expert's best question and the strongest possible proof that the team read
the annexure more carefully than anyone in the room.

---

## Filled IDEA template draft (field names from `00-idea-template-verbatim.md`)

**Slide 1, SMART INDIA HACKATHON 2026**
- Problem Statement ID: 26169
- Problem Statement Title: Development of an AI-Based Virtual Camera Tracking System for Coarse Alignment of Mobile Free Space Optical Communication (FSOC) Terminals
- Theme: Smart Automation
- PS Category: Software
- Team ID / Team Name (Registered on portal): as registered

**Slide 2, IDEA TITLE** — working title: **BeaconBench, an FSOC coarse-alignment
testbed you can measure with.**
- Proposed Solution (Describe your Idea/Solution/Prototype): ISRO published five
  numeric performance targets for this problem; our testbed already meets all five on
  video it had never seen, at 0.36 pixels mean error. It is a software instrument that
  replaces the cameras, pan-tilt mounts and optical benches needed to develop
  laser-terminal pointing: it renders a configurable virtual sky, flies a beacon
  through the annexure's full disturbance set, closes an AI-assisted detection and
  tracking loop around it, and grades every run automatically.
- Detailed explanation of the proposed solution: (1) scene and sensor: sub-pixel
  Gaussian beacon on a 2000x2000 screen, 640x480 sensor cropped at the commanded pan
  and tilt, disturbances per the annexure's table; (2) acquisition: expanding-square
  search at the slew cap, reported as a time CDF over random spawns; (3) detection:
  adaptive thresholding plus a learned spot scorer for impulse-noise frames, two
  independent centroiders whose disagreement is a confidence signal; (4) tracking: ego-
  motion-compensated constant-acceleration Kalman filter with innovation gating; (5)
  control: rate-limited pan-tilt with anti-windup; (6) logging: every run emits the
  annexure's performance report.
- How it addresses the problem: the sponsor's stated motive is an inexpensive,
  accessible platform for algorithm development; this is that platform, and it scores
  itself with the exact metrics the annexure names.
- Innovation and uniqueness of the solution: (a) the frame source is swappable, so
  externally supplied .mp4 is a first-class input, already measured at 0.36 px on
  unseen frames; (b) AI where the data says it pays: a learned detector on the measured
  failure mode (impulse noise), reported against the classical baseline per scenario;
  (c) a published failure boundary: we state where the loop saturates and why, from
  ISRO's own disturbance maxima.

**Slide 3, TECHNICAL APPROACH**
- Technologies to be used: Python, numpy, PIL (the entire dependency list for every
  number on this slide); AOtools/HCIPy phase screens for the physics mode; desktop GUI
  packaged as a standalone executable; no GPU, no cloud, no internet.
- Methodology and process for implementation (Flow Charts/Images/working prototype):
  pipeline flow `scene -> sensor -> detect -> track -> control -> log` with the frame
  source drawn as a switch (virtual camera | external video). Evidence panel image:
  four measured frames, clear 0.14 px, fog+Poisson 0.41 px, salt-and-pepper 0.36 px,
  compound worst case failing at 424 px, captioned as measured on 2026-09-01. Results
  table per fix 4, acquisition row per fix 1.

**Slide 4, FEASIBILITY AND VIABILITY**
- Analysis of the feasibility of the idea: an end-to-end loop exists and was
  independently rerun during audit; remaining work is physical fidelity, coverage
  (240-cell scenario grid), the GUI executable, and the report, not discovery.
- Potential challenges and risks: (1) full-screen acquisition against a 5 deg/s slew
  cap: a blind raster of the specified screen cannot finish in 2 s, so acquisition is a
  search-strategy problem, and we treat it as one; (2) rate saturation at the
  disturbance maxima: 20 px/frame at 30 fps is 3.75 deg/s against a 5 deg/s cap, our
  compound worst case fails here, measured; (3) turbulence realism: contrast reduction
  is compliant but not physics, and must be replaced by validated phase screens.
- Strategies for overcoming these challenges: (1) expanding-square search reported as
  a CDF, not a single number; (2) publish the saturation boundary and add velocity
  feed-forward; (3) our Kolmogorov generator is already validated against theory
  (structure-function exponent 1.652 vs 5/3 at L/r0 = 102) and is being wired into the
  scenario table.

**Slide 5, IMPACT AND BENEFITS**
- Potential impact on the target audience: ISRO engineers and students develop and
  regression-test PAT algorithms in minutes on a laptop instead of queueing for an
  optical bench; the sponsor's own annexure states the hardware this replaces.
- Benefits of the solution (social, economic, environmental, etc.): economic: one
  testbed replaces per-student cameras, pan-tilt mechanisms and optics, ISRO's stated
  motive; strategic: FSOC is a live national capability (ISRO LEOS lists optical
  communication among next-generation technologies; MeitY/ERNET already runs an FSOC
  connectivity pilot at Kohima); educational: an accessible instrument for exactly the
  algorithm development the PS describes.

**Slide 6, RESEARCH AND REFERENCES**
- Details / Links of the reference and research work: the fix 5 list, verbatim.

---

## The three questions the jury is most likely to ask

**Q1. "The beacon spawns anywhere on a 2000x2000 screen and you see 640x480. How do
you acquire in 2 seconds?"**
A blind raster cannot: 13 fields of view against a 5 deg/s cap needs about 5 seconds.
So we run an expanding-square search and report the acquisition CDF over 500 random
spawns instead of quoting one lucky number; within-FOV acquisition is 0.07 s, and the
CDF states exactly what fraction meets 2 s. (55 words)

**Q2. "What does AI buy you over a centroid tracker and a Kalman filter?"**
On clean frames, nothing, and we say so with numbers. Our measured failure mode is
detection under impulse noise: worst frame 451 px at 10% salt-and-pepper. A learned
spot scorer recovers those frames. The deck reports classical and AI-assisted results
side by side per scenario, which the annexure's technical report explicitly asks for.
(58 words)

**Q3. "Contrast reduction is not atmosphere. What is your turbulence model?"**
Agreed. Contrast mode exists because the annexure specifies it. The physics mode is
Kolmogorov phase screens with subharmonic augmentation, validated against the
theoretical structure function: fitted exponent 1.652 against 5/3 at L/r0 = 102, with
the residual explained by finite screen size, measured across four grid sizes. (51
words)

---

## Pre-mortem: it is 2026-09-03 and we did not advance

Ordered by probability, each with the prevention that was available this week.

1. **A generalist internal jury screened for buzzwords and picked platform decks; ours
   read as a niche instrument.** Prevention: the wedge sentence opens slide 2, the
   money argument (replaces hardware, sponsor's own words) opens slide 5, and "AI-
   assisted" appears in the first line, all shipped in the 2026-09-02 deck.
2. **The deck was scored against the PS title and read as under-delivering "AI-Based".**
   Prevention: fix 2's wording, AI as a first-class measured component, no
   classical-instead-of-AI framing anywhere.
3. **A technical juror hit the acquisition row and the answer was not in the deck.**
   Prevention: fix 1 run tonight and the CDF row in the table; Q1 rehearsed.
4. **Process fumble under the 2 September crunch: instruction slide not deleted, PPT
   uploaded instead of PDF, a seventh slide, a placeholder left in.** Prevention: the
   template rules checklist in `13`, executed by a second reader, upload the evening
   before, not at the deadline. (JPMC resume deadline 09:00 IST 2026-09-02 collides;
   the deck freezes the night of 2026-09-01 for this reason.)
5. **The internal jury quota went to themes with local sponsors or the pick collided
   with a stronger BITS team on the same PS.** Prevention: limited; the mitigation is
   the second filing (26228, fix 8) so one jury preference does not zero the team, and
   the 0/500 counters re-checked before filing to confirm 26169 is not locally crowded.
