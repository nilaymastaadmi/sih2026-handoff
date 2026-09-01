# A0: VERDICT

Audit session, 2026-09-01. Standalone: readable with no other file open.

## The call

**Keep the pick. PS 26169 (ISRO, AI-Based Virtual Camera Tracking for FSOC Coarse
Alignment). No switch.**

The audit tried to break it four ways: re-verifying every ledger claim against primary
sources, re-running the prototype cold on this machine, building the strongest case for
five alternatives before reading the pick's argument (committed in writing in
`A2-alternatives.md`), and re-running the prior-art kills through neutral agents after
the originals were run through deliberately hostile ones. The pick survived all four.
The runner-up is 26228 (Ministry of Defence, CV integrity), resolving the package's
internal contradiction with `09-final-decision.md`, and it should be filed as the
team's second idea, since the guidelines allow two.

## The count

**37 claims in the ledger (its own header miscounts them as 33). Checked 34 of 37
against primary sources or neutral re-research. 24 hold. 8 hold only in part. 1 does
not hold. None of the failures flips the pick; they cluster in the prior-art kills of
candidates that lost anyway.** The one outright failure: "TrojAI backdoor detection
sits at a 69 to 81% ceiling" (published detectors reach 0.90+ AUC on known attacks and
collapse on novel ones, which is a different and better argument for 26228 as the
hedge). The formerly UNCHECKED claim 5, the annexure's authority, is now substantially
closed in the pick's favour: I re-downloaded it from the live portal's own Dataset Link
today and it is byte-identical (SHA256 match) to the packaged copy, still linked from
ISRO's official PS entry.

Material new facts the package did not have: the portal added 2 problem statements
(26230, 26231) in the last day, so every coverage figure is stale by 2; and NTRO also
publishes weighted rubrics (verified from its master annexure, pages 37 to 39 of 53),
so the pitch may say "we built to ISRO's published rubric", never "no other PS has
one". The prototype replicated exactly: 7 of 11 scenarios meet all 5 published targets,
0.36 px on external video, turbulence exponent 1.652 vs theory's 1.667.

## The three changes that most improve our odds, ranked

1. **Run the full-screen acquisition test tonight** (0.5 to 1 person-day). The spike's
   0.07 s acquisition is measured on a scene that fits inside the initial field of
   view; the annexure's screen is 13 fields of view wide with random spawn, and a blind
   raster cannot meet the 2 s target at all. An expanding-square search plus an
   acquisition-time CDF over 500 random spawns turns the pitch's most attackable number
   into the one exhibit no other team will have.
2. **Reframe the deck: one wedge sentence, AI first-class.** Open slide 2 with "ISRO
   published five numeric performance targets for this problem; our testbed already
   meets all five on video it had never seen, at 0.36 pixels mean error." Present the
   learned detector on the measured failure mode (impulse noise) alongside the
   classical baseline, never classical-instead-of-AI: screeners score the deck against
   a title that says "AI-Based".
3. **Hold 26228 as the national-stage hedge.** Corrected 2026-09-02 per Nilay: the
   internal round allows one PS per team, so this is not an internal action. The
   guidelines' two-ideas allowance (page 16) applies to the national portal submission
   by a nominated team. If nominated, confirm with the SPOC that a second idea can be
   filed by 20 September, then file 26228; the audit strengthened its wedge (no shipped
   product binds inference outputs to model and data lineage end-to-end; detection of
   novel attacks is near-chance) and its deck is a half-day lift from the existing
   twelve-field writeup.

## Still UNCHECKED after this audit, and who checks it

1. **Whether BITS Goa binds the team to the internally-filed PS or allows a change
   before the 20 September national submission.** Only the SPOC can answer. Owner:
   Nilay, this week. This is the single open fact that could change strategy (it
   governs how safe the two-filing hedge is).
2. **The internal jury's composition and taste.** Unknowable until announced; mitigated
   by change 2 and change 3, not resolvable by research.
3. **Whether ISRO revises the annexure before the finale.** Unpredictable; mitigation
   is mechanical: re-hash the Drive file weekly (1 minute; any session can do it, the
   command and the reference hash are in `A1-ledger-check.md`).
4. **Whether "AI-assisted" in the annexure's Expected Solution means a learned
   component is mandatory in ISRO's scoring.** No public source can settle it; fix 2's
   positioning makes the question moot by shipping one either way.
5. **Immaterial residue:** the 26055 dataset gate (candidate rejected), FSOC precedent
   in SIH 2017-2021 (no lists exist; 2023 and 2024 verified clean), and whether 26147's
   section of the NTRO master publishes weights (candidate rejected; the master's other
   sections do).
