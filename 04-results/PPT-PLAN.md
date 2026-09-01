# PPT plan: from this folder to the uploaded deck

Written 2026-09-02. Deadline: the deck uploads the evening of 2026-09-02 (today).
Inputs: `01-research/SIH2026-IDEA-Format.pptx` (the official template),
`03-audit/A4-improved-pitch.md` (the field-by-field content, final), and
`13-solution-spec-for-deck.md` (layout guidance, superseded by A4 where they differ).

## Non-negotiable template rules (from the template's own instruction slide)

Six slides maximum including the title. The provided template only, headings unchanged.
Points and diagrams, not paragraphs. Export to PDF; no PPT accepted. **Delete the
7th (instruction) slide before export.**

## Build sequence, owners, times

| # | task | owner | time | done when |
|---|---|---|---|---|
| 1 | Acquisition run: expanding-square search, 2000x2000 screen, 500 random spawns, CDF plot + fraction within 2 s | Nilay | 0.5 to 1 person-day, started last night | `spike/` emits the CDF and one number for the slide 3 table |
| 2 | Fill slides 1 to 6 from A4's IDEA template draft, verbatim where possible | deck owner (T6) | 2 h | all 18 template fields populated, no placeholders |
| 3 | Slide 3 assets: pipeline flow (scene to sensor to detect to track to control to log, frame source drawn as a switch), the 4-frame evidence panel (`spike-output/evidence_panels.png`), the results table ordered per A4 fix 4 (external video first, worst case last, FPS as a 2-machine range) | T6 + Nilay | 1 h | slide 3 carries at least one measured number and one real screenshot |
| 4 | Slide 4 risks: the three from A4 (acquisition search, rate saturation, turbulence realism), each with its number | T6 | 30 min | no generic risk text anywhere |
| 5 | Slide 6 references: paste A4 fix 5's resolved list, nothing uncited | T6 | 15 min | every line has a link or an identifier |
| 6 | Wedge check: slide 2 opens with the wedge sentence ("ISRO published five numeric performance targets for this problem; our testbed already meets all five on video it had never seen, at 0.36 pixels mean error"), and "AI-assisted" appears in the first line of the proposed solution | Nilay | 10 min | a reader of slide 2's first two lines can repeat the pitch |
| 7 | Second-reader pass against the checklist below | any teammate who did not build the deck | 20 min | every box ticked |
| 8 | Export PDF, upload, confirm receipt | Nilay | 15 min | uploaded the evening of 2026-09-02, not at the deadline minute |

## Second-reader checklist (pre-mortem items 2 and 4 live here)

- [ ] 6 slides exactly, instruction slide deleted, headings untouched
- [ ] PDF export, not PPT
- [ ] PS ID 26169, exact official title, theme Smart Automation, category Software, team ID and name as registered
- [ ] "AI-Based"/"AI-assisted" present in slide 2's opening; nothing reads as classical-instead-of-AI
- [ ] Every number on the deck traces to `12-spike-results.md` or the acquisition run; no number the team cannot reproduce on stage
- [ ] The worst-case failure appears (it is the credibility exhibit, do not sanitise it)
- [ ] FPS quoted as a range across named hardware, not one machine's lucky number
- [ ] No placeholder text, no "[measure]", no lorem
- [ ] References all resolve; no bare "published work on X"
- [ ] File name and upload portal per the SPOC's instruction

## If the acquisition run is not done by deck freeze

Ship the honest fallback row: "acquisition (in-FOV) 0.07 s; full-screen random-spawn
acquisition reported as a CDF, first finale milestone". Do not put an unmeasured
full-screen number on the slide. A number we cannot produce is worse than no number.

## After the internal round (parking, not for today)

- SPOC questions: does nomination bind the PS; can a second idea (26228) be filed
  nationally.
- Wire the validated turbulence module into the scenario table and re-emit the 11-row
  table (A4 fix 6, owner E2, was due 2026-09-05).
- GUI + PyInstaller smoke test by 2026-09-07 (A4 fix 6).
- Re-check idea counters before the 20 September national filing.
