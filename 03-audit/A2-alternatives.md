# A2: the road not taken. Five alternatives, built blind.

Written 2026-09-01 by the audit session, BEFORE reading `00-RECOMMENDATION.md` or
`09-final-decision.md`. At this point I know only the pick's identity (26169), the
runner-up (26228), and what CLAIMS/GAPS state about them. I have not read the argument.

Method: my own scan of all 175 software titles in `ps_clean.tsv`, full official text
pulled from `evidence/ps-full-text/` for every candidate below, scored against the
official idea-selection criteria (guidelines page 20: novelty, complexity, clarity and
format, feasibility, practicability, sustainability, scale of impact, user experience,
future work progression) plus the team's asset inventory (`inputs/04-assets.md`).

Never-read constraint: the prompt requires at least 2 picks from PS that GAPS.md admits
were never read. GAPS admits two never-read sets: the Student Innovation software block
(26193 to 26209, seen but never evaluated) and all 54 hardware (out of scope here, the
prompt asks for software). I take 26198 from the SI block, and I add 26231, which is
stronger than "admitted never read": it was added to the live portal after the package
shipped (the 2026-09-01 00:03 snapshot has 229 PS; the live page at my fetch, same day,
has 231, adding 26230 and 26231). Nobody on any prior pass has ever seen it. I state
this interpretation openly rather than pretending 26231 is in GAPS.

---

## 1. PS 26119, MRPL: Indigenous GPU-Accelerated Optimization Solver

Official text (sweep-chunk-4): "It shall not be built upon any existing open source
solver library but shall be built from scratch from mathematical foundation."

The case. This clause is the strongest anti-consensus property in the entire 229. Every
LLM-prepared competitor pitch dies by decree: you cannot wrap HiGHS, OR-Tools, or CBC.
A team that shows up with a from-scratch revised-simplex core, a working branch-and-bound
on top, and honest Netlib benchmark numbers is competing against approximately nobody,
because almost no student team can build a numerically stable simplex in 3 months. This
team has an unusual shot: two strong engineers, `icpc-huawei` (a discrete-event
simulator and parameterised scheduler in C++, benchmarked against a baseline), and a
verification culture (golden-reference scoreboards, mutant testing) that maps directly
onto "prove your solver correct against known optima". The internal-round number exists:
"solves N of M Netlib LP instances to within 1e-6 of the published optimum" is
producible in two weeks for a restricted subset. Sovereignty is the loudest theme in
this year's PS set and the judges' patriotic instinct works for you. The demo is a bake-
off table against GLPK, which is legible in 10 minutes. Novelty 10/10, feasibility of a
credible *subset* 6/10, and the PS text itself blesses a "solver core, not a modelling
environment" scope cut.

## 2. PS 26158, NTRO: Single-Pass Drone Video to Accurate 3D Model Generation System

The case. This is the only other PS I found with a published, weighted evaluation
rubric: the NTRO master annexure (pages 37 to 39 of 53, fetched by me from the portal's
Drive link on 2026-09-01) specifies Reconstruction Accuracy 30%, Model Completeness 20%,
Processing Speed 20%, Innovation 15%, Scalability 10%, UI 5%, with numeric targets
(under 15 minutes for a 10-minute video, spatial accuracy 1 m or better, OBJ/PLY/LAS
outputs, web viewer). Whatever made a published rubric decisive for 26169 applies here
too, and nobody else knows: the rubric sits in an image-only PDF whose text layer
extracts to 3 bytes, so every scraper-based team sees "Dataset Link" and nothing else.
The sponsor is NTRO, which the package's own research rates as the most engaged sponsor
in SIH history (6 implementations from 2023, mid-finale redirects in 2025). The demo is
the best in the whole candidate set: fly-through of a 3D model in a browser is the kind
of thing judges photograph. The open-source substrate (COLMAP, OpenMVS, gaussian
splatting) is mature, and the single-pass constraint is a real research edge where the
team can measure and publish honest failure cases. Data risk near zero: any drone video
develops it. Weaknesses: no team asset touches SfM, and the compute is heavy.

## 3. PS 26035, DoCA: Test report generation for Non-Automatic Weighing Instruments per OIML R-76

The case. The highest-floor entry available. OIML R-76 is a published international
recommendation with exact formulas: maximum permissible errors by accuracy class,
verification scale intervals, rounding tests, eccentricity and repeatability protocols.
Correctness is therefore provable, not claimed, and this team's entire verification DNA
(constrained-random stimulus, golden-reference scoreboard, 1.27 million assertion checks
in `axi-cdc-uvm`) transfers exactly: generate 10,000 randomised virtual instruments and
observation sets, run them through the compliance engine and through an independently
coded oracle, report "10,000 randomised instruments, 0 mismatches". That is a number no
other team in the room will have, because no other team thinks in scoreboards. The
sponsor pain is real and stated: reports "largely prepared manually using spreadsheets",
legally mandated under the Legal Metrology Act 2009. The build is small enough that the
internal-round demo is the finished product, which converts the finale from a build risk
into a polish exercise. Weaknesses the pitch must survive: low glamour, low novelty
score against an "AI-powered" field, and a ceiling on scale-of-impact points. But it is
the entry most likely to actually work flawlessly on stage, and judges remember the one
demo that did not crash.

## 4. PS 26231, MHA: Digital Companion for Field Drug Testing

The case. Added to the portal on or about 2026-09-01: it is absent from the 229-PS
snapshot taken at 00:03 that morning and present, with 26230, in my live fetch the same
day. Zero teams have scraped it, zero LLM shortlists contain it, and the idea counter
reads 0/500 like everything else, so the crowding advantage is real rather than assumed
for at least the first week. The ask is tightly bounded and demoable in exactly three
screens: photograph a colorimetric test kit with a reference colour card in frame,
classify positive/negative/inconclusive under lighting correction, and generate a
tamper-evident record (timestamp, GPS, operator ID, cryptographic hash of the image).
The team has shipped both halves before: `pcb-drishti-pro` is deployed CV classification
with a decision layer, and `alpaca-hackathon` carries a hash-chained, Merkle-sealed
audit log that a judge can verify live. The chain-of-custody angle gives the pitch a
number ("every record verifiable in under a second; tampering detected on any single
bit flip") and a story no generic CV team tells. Risks: colour calibration across kit
brands and phone cameras is the hard 20%, the sponsor engagement is unknown because the
PS is 1 day old, and MHA's evaluation culture is opaque. Impact case writes itself:
NDPS field testing today produces no verifiable record at all, the PS says so.

## 5. PS 26198, Student Innovation (software): MedTech / HealthTech bucket

The case. The strongest asset-first entry available in the never-evaluated SI block. The
team owns a real, characterised, imbalanced biomedical dataset on disk (3,163
phonocardiogram spectrograms, 724 MB, class split 75.6/19.5/4.9) and an honest,
completed model study (`heart-murmur-index`: 11+ architectures, seeds, ablations, best
test macro-F1 0.6019, negative results registered). Pitch: a primary-health-centre
auscultation triage aid that flags "murmur present / absent / unknown" with an explicit
abstention class, calibrated so the number on screen is a screening sensitivity, not an
accuracy fantasy. The internal-round demo runs today with zero build: upload a heart
sound, see the spectrogram, the three-way call and the confidence. The differentiation
is honesty: every competing medical-AI SI pitch claims 95%+; this one shows a
pre-registered study whose headline includes what failed, which is exactly the
credibility a physician juror probes for. Weaknesses are structural, and I will not
soften them: SI is the most crowded category in SIH by construction (every team without
a sponsor PS lands there), the 0.60 macro-F1 is honest but unglamorous, and the path
from triage aid to deployment runs through clinical validation no hackathon covers.

---

## The committed question

**Does any of these 5 beat PS 26169 for this team at the BITS Goa internal round?**

**Answer: No. Committed before reading the pick's argument.**

Reasoning, briefly. The two serious challengers are 26158 and 26119. 26158 matches
26169's published-rubric advantage and beats its demo ceiling, but the team starts from
zero on SfM, the compute cost is real, and the 1 m accuracy plus 15-minute processing
targets are a finale gamble, where 26169's targets are already 7-of-11 met by a working
prototype (I reran it today: same numbers). 26119 beats 26169 on novelty and
anti-consensus, and it is the pick I would make for a team of six compiler engineers
with nothing to lose; for this team, at this round, with the internal deadline in days,
a from-scratch numerical solver cannot produce a defensible number by the internal round
without betting the month on it. 26035, 26231 and 26198 are all viable, none dominant:
26035 caps its ceiling, 26231 carries 1-day-old-sponsor risk, 26198 fights the SI crowd.

What would change this answer: if the 26169 annexure were shown stale or withdrawn
(claim 5), 26158 becomes the pick, not 26228, because it is the only candidate that
preserves the published-rubric edge. Recorded here so Stage 3 can test it.
