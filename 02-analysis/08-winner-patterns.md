# 08. What actually wins SIH, from winner anatomies. And where my thesis was wrong.

Written 2026-08-31. Built from 16 identified winning or finalist teams across SIH 2022 to 2025, plus the official MoE/AICTE finale schedule. Every claim below traces to a named team or a primary document. This file corrects `02-competitor-model.md`.

## 1. The finding that breaks my thesis

**Zero winners presented a bare model, notebook, or benchmark.**

Of 13 winning teams whose artifact is documented: 6 built full-stack platforms with an ML component inside, 4 built physical devices, 1 built a simulation toolchain. Where machine learning existed at all, it was wrapped in an app, a device, or an API. Not one team won by showing a measured number against a baseline as the deliverable.

My Phase 2 model said: the modal team pitches a platform, so we should pitch the boring tool that beats a named baseline. The first half is right. **The second half is wrong.** The winners also pitch platforms. They win on execution, on responding to the jury, and on commercial framing, not on refusing to build a product.

The corrected rule: **the measured number wins the screening PDF; the working product wins the room.** We need both, and I had been treating the number as sufficient.

## 2. The scoring weights, from the one team that published them

Team DORA the Explorer, SIH 2023, PS SIH1370, Government of Jharkhand:

- Evaluation 1: 20 percent, presentation and feasibility
- Evaluation 2: 30 percent, technical work and execution
- Evaluation 3: 50 percent, **end-to-end product and commercial viability**

Half the marks sit on the last round, and that round is explicitly about the product and its commercial case, not the algorithm. Independently corroborated at 50 percent by a second 2023 finalist. The 20/30 split is single-source.

## 3. The finale is a fixed clock

From the official SIH 2024 Software Edition schedule (msruas.ac.in): coding starts 09:30 Day 1 and stops 17:30 Day 2, so the real build window is **32 hours, not 36**. Six jury contacts totalling roughly 40 minutes. Each evaluation slot is **4 minutes presenting plus 3 minutes of questions**, minimum 3 judges per panel. Mentoring slots are 5 to 10 minutes and carry **zero marks**.

## 4. The five behaviours to copy, ranked by evidence strength

1. **Treat every mentoring round as requirements gathering, and ship the requested change before the next evaluation.** Four independent teams across 2022, 2024 and 2025 describe the same mechanic. A 2022 winner puts it bluntly: the judges' suggested modifications matter more than the problem statement text. One team was told to prioritise its interface, did not, and lost.
2. **Arrive with 90 to 95 percent built.** A 2024 winner: you can only improve the prototype by 5 to 10 percent on site, and stop changing anything two hours before final evaluation. Three other timelines corroborate an August-to-November build.
3. **Put money in the deck.** Development cost, deployment cost, funding required, break-even horizon, exit plan. Three independent teams cite this as the differentiator, and it is half the final round's weight. One team's market analysis "received positive attention" from judges.
4. **Assign six named non-overlapping roles, including one business and presentation owner.** Three teams. The published Solar Masters split: leader, hardware, model designer, IoT, app developer, researcher.
5. **Do not filter problem statements by submission count. Filter by whether you already have a prototype in that domain.** See below.

## 5. Crowding: my heuristic was wrong, and the correction is well evidenced

The popular advice, widely shared on LinkedIn, is that fewer submissions means better odds. An actual 2024 winner contradicts it directly, saying low-submission problem statements did not help and their experience was the opposite. The structural argument agrees: submissions are capped at 500 per problem statement and 5 to 7 colleges are selected per problem statement regardless of how many filed, which flattens crowding at the shortlist gate. Solar Masters faced 106 submissions for 6 slots, 5.7 percent.

Note also who says what. The two teams in this corpus that most emphasised picking an unusual or uncrowded problem statement both **lost** at the finale. One of them had used uniqueness to clear the internal round, which is consistent: crowding is a screening-stage lever and does close to nothing for winning.

**Consequence for us:** crowding drops from a primary ranking axis to a tiebreaker. Since the goal is to win rather than to qualify, the axes that matter are asset reuse, product shape, and iteration speed under jury feedback.

## 6. Scope expands at the finale, it does not shrink

Three independent teams report judges adding requirements mid-event: air-quality monitoring plus dynamic GIS plus model-app integration for one team, two rounds of accuracy rework for another, and a third whose stated strategy was to complete every task the judges gave. No winner in the sample reports deliberately cutting scope.

This inverts my "narrow the scope" advice. The correct posture is: arrive with a complete product and enough headroom that four less-experienced teammates can add a judge-requested feature inside one round.

## 7. Sponsor-toolchain mastery is a documented win condition

Both MathWorks problem statements in this corpus were won by teams that used MathWorks tools end to end. Solar Masters took two weeks of self-paced MathWorks training before the finale. If a sponsor names its own tools or formats, using them fluently is itself a scoring axis.

## 8. Risks this corpus surfaced

- **Judge domain mismatch is real.** One detailed critical account describes a finale panel with no grasp of the domain, no scores shared, and no leaderboard. Niche defence and space problem statements carry this risk: depth only helps if the panel can perceive it.
- **Attendance risk.** One team qualified for the finale and could not attend because of end-of-semester exams. December sits inside placement season.
- **Problem statements can be withdrawn.** One team's chosen problem statement was cancelled by the ministry one day before a submission deadline.
- **The internal funnel is generous but real.** DJ Sanghvi nominated 50 teams internally, sent 14 to the finale, and won 6.

## 9. What this changes about our pick

Re-scored on the corrected model, where the deliverable must be a product with a visible surface, the team must arrive nearly finished, and half the final marks are product plus commercial viability:

- **26228 (MoD, model integrity) falls.** Its output is a verdict and a signed receipt, which is text on a screen. Three independent sources say the most common jury feedback is about the demo surface, and this candidate has the weakest one. Its cryptographic half was already refuted as novel. It is now out of contention for the single pick.
- **26169 (ISRO, beacon tracking) holds.** It is the one candidate that is legible on a projector without narration, its four required metrics give the four less-experienced teammates four independent owned modules, and it has no external data dependency, so arriving 90 to 95 percent built is realistic. It is a simulation toolchain, and exactly one winner in this corpus won with a simulation toolchain, so the shape is proven but not common.
- **26147 (NTRO, signal analysis) gains on framing and loses on build.** Its commercial story is the strongest of the five: Krypto500 and W-CODE are foreign, export-controlled and expensive, so an indigenous extensible alternative is a genuine sovereignty and cost argument, which is exactly what a 50-percent-weighted final round rewards. Against that, its primary open-source tool was archived in March 2026, the blind-recovery core exists only as papers, and the toolchain fights a Windows machine. Behaviour 2, arrive nearly finished, is the one it is least able to satisfy.
- **26166 (ISRO, lunar) is unchanged**: excellent demo surface, but its headline contribution was pre-empted by a September 2025 paper on ISRO's own instruments.

The remaining open question at the time of writing is what the SIH1447 winning team actually built, since NTRO posed nearly this problem in 2023 and a student team won it. That result decides whether 26147's build risk is as fatal as it looks.
