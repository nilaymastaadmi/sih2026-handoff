# GAPS: what was not done

This is the file to read before trusting anything else. It is deliberately unflattering.

## 1. Reading coverage, exact numbers

| set | count | treatment |
|---|---|---|
| Problem statements on the portal | 229 | |
| Hardware | 54 | **Excluded on a single category filter. Not read at all.** |
| Software | 175 | |
| Software, Student Innovation block (26193 to 26209) | 17 | **Excluded on a single filter without analysis.** Their descriptions are short enough that `ps_clean.tsv` holds the complete text, so they were seen but never evaluated |
| Software, non-template | 158 | Full official portal description read for **158 of 158** |

So: **158 of 175 software problem statements were read in full. 17 were excluded on one filter. All 54 hardware were excluded on category without being read.**

**But who read them matters, and this is the biggest honesty caveat in the package.** Of those 158 full descriptions, I personally read about 34: the 30 in `evidence/ps-full-text/longlist-30-full-descriptions.md`, plus 26119, 26078, 26035 and 26169 which I pulled individually. The other 124 were read by six parallel agents, and I saw only their structured summaries. **The coverage claim is real, but for 124 problem statements it rests on agent summarisation that I did not spot-check.** An auditor who wants to break this package should sample five problem statements from the sweep chunks, read them, and compare against what the corresponding agent reported.

The hardware exclusion was inherited from Session 1 as a rule and never revisited. The official guidelines say there is no bar on the software and hardware mix a college nominates. If the team is willing to enter hardware, 54 problem statements have never been looked at by anyone in this exercise.

## 2. Checks skipped, partial, or impossible

1. **The 12-point deliverable format was not reapplied to the final five.** `prompt-2` Phase 7 specified twelve numbered fields per finalist. `00-RECOMMENDATION.md` follows that format for the *earlier* five. After the coverage sweep changed the five, `09-final-decision.md` was written as prose and never re-cast into the twelve fields. Effort estimates, person-week role splits, and per-PS confidence statements are therefore missing for the current five.
2. **Live idea counts never became usable.** They were fetched three times and were 0/500 every time. The prompt's intent, to replace guessed crowding with measured crowding, was not achievable in the window. Every crowding number in the package is ASSUMED.
3. **Dataset checks covered the finalists, not all twelve.** `prompt-2` Phase 6 asked for data availability on all eleven non-26055 candidates. Coverage was good for the five that survived and thin for the seven cut.
4. **Reddit was unreachable** for the evaluator-behaviour research. The crawler was blocked and three archive mirrors failed. All internal-round politics and judge-diligence folklore is therefore unevidenced in both directions.
5. **The turbulence module is validated but not integrated.** `spike/turbulence.py` matches Kolmogorov theory, but `spike/fsoc_spike.py` still renders atmosphere as contrast and brightness reduction. **The 7-of-11 scenario table was produced with the placeholder model, not the validated one.** Anyone quoting both in the same breath is overstating.
6. **The 240-cell coverage matrix was never run.** It is named as the method in `11-build-playbook.md` and remains unexecuted.
7. **Whether BITS Goa binds the problem statement at internal nomination is unknown.** National rules select the PS at national submission on 20 September, so there may be 18 days of optionality after the internal round. This was flagged repeatedly and never answered, because only the SPOC can answer it.
8. **The NTRO 53-page master annexure was not opened.** Two annexures recovered during the sweep are page extracts from one 53-page NTRO document. It very likely contains a section for PS 26147, possibly with published weights of the kind that decided 26169. Since 26147 was a serious contender, not opening this is a real omission.
9. **No global SIH rule on pre-built work was located.** Claim 27 rests on two sponsors' own problem statement text, not on a rule in the guidelines. Autodesk forbids what ISRO instructs, so the rule is sponsor-level, and no guidelines-level statement was found either way.
10. **The SKY130 analog repositories were never authorship-verified.** A standing instruction says to ask before treating them as solo work. They went unused, so this never blocked anything, but the question is still open.
11. **Artifact watch dropped twice.** Cosmetic only; the published page is unaffected.

## 3. Points where two readings were available and one was chosen

1. **Crowding: primary axis, or nearly irrelevant?** Early work ranked heavily on low crowding. Winner evidence then showed that finale slots are fixed per problem statement regardless of filings, and that the teams most emphasising uncrowded picks lost. I de-weighted crowding to a tiebreaker. **The other reading:** crowding still governs the screening gate, which you must pass before the finale weights matter, and the winner sample is small and self-selected.
2. **PS 26119, the from-scratch solver.** Folder A scored it DEAD at 50. I proved that verdict was a truncation artifact: the decisive "Expected Solution" clause begins at character 3,150 of a 4,118-character description, and the file both prior passes used truncates at 1,500. I then declined to promote it, on finale-build risk. **The other reading:** its "shall not be built upon any existing open source solver library" clause disqualifies the modal pitch by decree, which is the strongest anti-consensus property found anywhere in the 229, and I left it on the table.
3. **PS 26103.** A first-principles agent argued it was the best match for the team's rarest assets. An adversarial agent refuted it on redundancy with PAIMANA. I sided with the adversarial agent. **The other reading:** redundancy with an incumbent portal does not preclude a better analytical layer, and the first-principles case for asset fit was never rebutted on its merits.
4. **26147 versus 26169.** 26147 has the better sponsor by every measurable proxy: 6 implementations from SIH 2023, evaluators who redirected teams mid-finale in 2025, and a near-identical problem already won in 2023. I rejected it on build risk. **The other reading:** sponsor engagement determines whether a winner is declared at all, and build risk is something a capable team retires.
5. **"AI methods (if used)".** I read this as making AI optional, which defuses the strongest attack on 26169. **The other reading:** the title says "AI-Based", and an evaluator may treat a classical-baseline-led entry as non-responsive regardless of that parenthesis.
6. **Who the runner-up is.** `09-final-decision.md` calls 26147 the runner-up on sponsor grounds. The scored table puts 26228 second at 74 and 26147 fourth at 67. **Both statements are in the package and they disagree.** Not resolved here, per the instruction not to re-litigate.

## 4. The weakest link, named

**Claim 5 in `CLAIMS.md`: that the PS 26169 annexure is current and authoritative. It is the only UNCHECKED claim, and the pick rests on it.**

The chain is: the annexure publishes ISRO's marking weights and numeric targets, therefore 26169 is scored against a rubric we can build to, therefore it beats candidates scored against rubrics we can only estimate. Remove the annexure and 26169 becomes an ordinary tracking problem with no published rubric, no external benchmark videos, and no numeric targets, at which point 26228's lower build risk and 26166's better demo both become competitive again.

The annexure came from a Google Drive link in a portal field labelled "Dataset Link". It carries no date, no version number, and no independent ISRO-hosted mirror was found. It is internally consistent and reads as an official document, which is why it was trusted, but **trusting it is a judgement, not a verification.**

Second weakest: **fourteen of the sixteen REPORTED claims come from a single agent each, with no independent corroboration.** Five candidates were killed or demoted on those claims. The prior-art kills in particular (26073, 26147, 26166, 26103) each rest on one adversarial agent that was explicitly instructed to default to "this is a real threat" when evidence was ambiguous. That instruction was deliberate and useful, but it biases toward killing, and I did not re-run any of those searches without the bias.

## 5. Problem statements dropped with less confidence than the writeups suggest

- **26066, INCOIS subsurface ocean temperature.** The annexure sweep called its specification the strongest of the nine it examined: seven public datasets with DOIs, all returning HTTP 200, an exact grid and fifteen fixed depth levels. It stayed cut on demo shape and domain niche. That is a judgement about presentation, not about substance.
- **26119, the indigenous solver.** See section 3. Cut on finale risk after being shown to have been killed unfairly.
- **26035, OIML weighing instrument test reports.** The highest-floor option found: correctness is provable rather than claimed, and the constrained-random verification asset maps onto it exactly. Dropped on ceiling and impact, which is the softest reason used anywhere in this package.
- **26046, Ayush clinical trials.** Dismissed as "mostly enterprise CRUD" *before* the winner study established that six of thirteen documented winners built exactly that shape. It was never re-examined after that correction, which is an inconsistency in my own process.
- **26078, NCMRWF extreme weather tracking.** Held back because two named datasets were ASSUMED internal. That assumption was never tested.

## 6. Structural weaknesses in how this was produced

1. **Adversarial testing was applied unevenly and late.** The first prior-art test covered only my top three, which killed one and gutted another. The other candidates were tested a round later. Testing favourites first is backwards, and the ordering shaped which candidates survived long enough to be examined properly.
2. **Agent scores were anchored.** Six sweep agents were each told the bar was 75, and each returned nominees at 79 to 85. That clustering is an artifact of the prompt, and I discounted it, but a better design would not have stated the bar.
3. **The `02-competitor-model.md` thesis was falsified by my own later research** and the file is retained unrevised, with only a pointer in `08` and the README. A reader taking `02` at face value gets advice the package later contradicts.
4. **No independent replication of the spike.** The prototype was written and run by the same process that specified it. Its 7-of-11 result has not been checked by anything other than itself.
