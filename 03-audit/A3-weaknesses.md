# A3: where the pitch fails to convince

Audit session, 2026-09-01. The pitch as audited: `09-final-decision.md` (the argument),
`13-solution-spec-for-deck.md` (the deck), `12-spike-results.md` (the numbers),
`11-build-playbook.md` (the plan). Read as a judge with ten minutes would.

## Reconciliation with my Stage 2 commitment first

My committed Stage 2 answer was: none of my 5 alternatives beats 26169. After reading
the argument, that answer **stands**, and 09's reasoning strengthens it in two places I
had not counted: the winner-pattern correction (products beat models, and this PS is a
product brief) and defect (c) in the spike (the open-loop external-video architecture,
found only by running code). Two places where my Stage 2 work stands AGAINST the
package's framing and modifies it: (1) my A2 case for 26158 disproves 09's premise that
26169 is scored against the only printed rubric; NTRO prints one too, so the pitch's
edge is "we built to the rubric", never "only we have a rubric". (2) My A2 fallback
ruling changes: if the annexure had failed verification, the right fallback was 26158,
not 26228. It did not fail, so this is recorded and closed.

The runner-up contradiction (09 names 26147, the artifact table scores 26228 second at
74 vs 67) resolves against 09: with claim 20's "80% coverage" figure shown to be
invented and claim 21 half-wrong, 26147's demotion evidence was sloppy, but its
rejection stands on the two legs that survived audit (URH archived read-only 2026-03-29;
the "arrive 90 to 95 percent built" rule, which 26147 satisfies worst of the five).
26228 is the runner-up. It also gained in audit: claim 25's "69 to 81% ceiling" is
false, detection on known attacks is 0.90+ AUC while collapsing on novel attacks, and
claim 24's "shipped plumbing" overstates, since no product binds inference outputs to
model and data lineage end-to-end. 26228 rises, does not reach 26169, and becomes the
natural second filing (see A4 fix 8).

---

## The weaknesses, ordered by what each costs, worst first

### 1. The acquisition number hides the absence of a search, and a domain expert will find it

**The failing line: `13-solution-spec` slide 3, results table row "acquisition time |
0.07 s against a 2 s target", and every `12-spike-results` scenario row repeating
0.07 s.** The annexure specifies a screen of minimum 2000x2000 px, initial camera at
centre, initial target location random. At the spike's own scale that is a 12.5-degree
world seen through a 4x3-degree window: roughly 13 FOV-tiles. The spike's scene spans
+/-1.6 degrees (`fsoc_spike.py` line 41), inside the initial FOV, so acquisition never
searches; 0.07 s is detection latency, not acquisition. A blind raster of the specified
screen at the 5 deg/s slew cap cannot finish inside 2 s, ever. The jury question this
invites: "your spot spawns in the far corner of the screen; walk me through the first
two seconds." The current pitch has no answer, and this is also my answer to the
prompt's "question we cannot answer" lens. Cost if unfixed: the Technical Evaluation
Q&A (20% at the finale) and the credibility of the deck's flagship table; ISRO's BP-1
scenarios can spawn off-FOV and the score would collapse in the 30% band. The saving
grace: every competing team fails this identically, and the team that names it wins the
exchange. Fix in A4 (fix 1), the highest-leverage prep task.

### 2. The deck can be read as non-responsive to "AI-Based" by a screener who never opens the annexure

**The failing line: `13-solution-spec` slide 2, innovation bullet 3: "We report the
classical baseline as a headline result... The annexure says 'AI methods (if used)'."**
Two problems. First, the annexure's Expected Solution section opens "Participants shall
develop an AI-assisted camera tracking system", so AI-optional is one section read
against another, not settled. Second and worse: national screening and the internal jury
score the deck against the PS title and portal text. The title says "AI-Based". A deck
whose most prominent algorithmic claim is classical-beats-AI invites a non-responsive
read from any evaluator who never clicked the Dataset Link. Cost: the screening gate
itself. The fix is positioning, not engineering: AI present as a first-class component
(learned detection under impulse noise, where the spike's own data says detection is the
failure mode), with the classical baseline as the measured comparison inside it.

### 3. There is no wedge sentence, there is a wedge paragraph

**The failing section: `13-solution-spec` slide 2, "Proposed solution" (4 lines) plus
"Idea title suggestion... something in the register of 'an FSOC coarse-alignment
testbed you can measure with'".** The register is right and the sentence does not exist.
`11-build-playbook` even instructs "Slide 2 must open with the sentence a screener
remembers" and then no file supplies it. What a judge could repeat to another judge
tonight: nothing shorter than 40 words exists in the package. Cost: the deck's first
five seconds. Rewritten in A4 (fix 3).

### 4. "7 of 11" is the honest number but the wrong headline number

**The failing line: slide 3 table, first row "scenarios meeting all five published
targets | 7 of 11".** As a headline it reads as 64%, invites "why not 11", and buries
the strongest fact in the package: **0.36 px mean error, 5 of 5 targets, on video the
tracker had never seen**, which maps to the single largest scoring band (Benchmark
Performance-2, 30%). 7-of-11 belongs on the slide as the honesty exhibit next to the
worst-case panel, not as the lead. Also, "33 to 42 FPS" is machine-specific: my rerun
of the same code produced 24.3 to 60.6 FPS. All above the bar, but the deck must pin
FPS to named hardware or a judge who reruns it gets different numbers than the slide.
Cost: medium; this is ordering and captioning, fixed in A4 (fix 4).

### 5. The references slide cites categories, not references

**The failing lines: slide 6, "Published work on centroid error decomposing into bias
and jitter..." and "Published free-space optical terminal results for context..."** with
no author, venue, or link on either. The official criteria include clarity and details
in the prescribed format; slide 6 is the prescribed field for exactly this, and it is
the cheapest slide to make bulletproof. The claims are also checkable today: real
terminals at ~10 microradian RMS and sub-second acquisition are in the audit's resolved
sources (arXiv 2508.08950: mean acquisition 0.908 s, all trials under 1 s). Slide 5's
"live national capability area" is likewise assertable with ISRO LEOS's own optical
communication page and the ERNET/MeitY Kohima FSOC pilot. Cost: small but pure loss,
since every fix is a paste. Fixed in A4 (fix 5).

### 6. The feasibility story leaves the two scoring-critical tasks unowned in practice

**The failing section: `11-build-playbook` section 10, roles 1, 5 and 6 against the
team's actual composition (2 strong engineers, 4 unknowns).** Roles 2, 3, 4 (detection,
tracking, control) are where the strong engineers will gravitate and where the spike
says the problem is already solved. The marks say otherwise: role 5 (GUI plus the
standalone executable, inside Functional Verification's 20%) and role 6 (logs,
comparator, coverage, report, "the role that wins the 60 percent") are the scoring
spine, and role 1's physically defensible disturbance chain is the credibility spine,
already half-open because the validated turbulence module is still not wired into the
scenario table (GAPS item 5, confirmed unfixed in my rerun: the 7-of-11 table still uses
contrast-based atmosphere). A GUI rendering camera frames at 20+ FPS from Python plus
PyInstaller packaging is a real task with real failure modes, and no named person owns
it. The one specific task the plan is optimistic about: **the standalone GUI executable
sustaining 20 FPS with live statistics, owned by nobody**. Fixed in A4 (fix 6).

### 7. The differentiation story leans on annexure obscurity that will not hold for 3 months

**The failing line: `09-final-decision` "The requirement is only visible to a team that
opened the annexure."** True this week. The Drive link sits on the public portal, the
third-party PS aggregators already mirror the portal fields, and there are 19 days to
the national deadline and 3 months to the finale. Assume 3 to 5 serious teams nationally
build to the weights. The durable differentiation is what a deck-only team cannot
produce by 20 September: measured numbers with an honest failure case, a physics-
validated turbulence model (exponent 1.652 vs 1.667, replicated in this audit), and the
open-loop external-video architecture. The pitch survives the four-similar-pitches
morning on those; it does not survive on "we found the PDF". Cost: low today, high in
December if the plan keeps treating the annexure as secret. Fix folded into A4 fixes 3
and 4.

### 8. Package-level: the runner-up contradiction and the unused second filing

**The failing lines: `09-final-decision` "The runner-up, and why it lost" naming 26147,
against the artifact's scored table (26228 at 74, 26147 at 67); and the guidelines'
"One team can submit Ideas against maximum of 2 Problem Statement only" (page 16,
verified), which 09 never uses.** A teammate reading 09 and the artifact side by side
finds the package disagreeing with itself the night before the internal round, and the
team is leaving a free option on the table by filing one idea. Resolved above and in A4
fix 8: 26228 is the runner-up and the second filing.

---

## The three-screen walk, restated for a deck-only round

The internal round is a PPT upload, confirmed 2026-08-31, so "screens" are deck panels.
Where a judge stops believing today: slide 3, the results table, at the acquisition row
(weakness 1) — the one number that is too good. What is being hand-waved: the search
phase (weakness 1) and the atmosphere behind the 7-of-11 table (weakness 6, turbulence
validated but not wired). Both are named in the deck's own risk slide only obliquely
(risk 2 names turbulence realism; nothing names search). The fix set in A4 makes the
weakest row honest and keeps every other number as-is, because every other number
replicated on my machine today.
