# 01. Event model: SIH 2026

Written 2026-08-31. Sources: `00-guidelines-verbatim.md` and `00-idea-template-verbatim.md` (both extracted 2026-08-31 from official files), plus 3 web research passes run 2026-08-31. Every web claim carries its URL and that fetch date. Anything not verified says ASSUMED.

## 1. The mechanics that matter

- Submission is a 6-slide PDF in a fixed template, uploaded by the team leader on the portal, plus idea title and description fields. Guidelines PDF slide 11, and https://www.sih.gov.in/letters/2026/SIH2026-IDEA-Presentation-Format.pptx (fetched 2026-08-31).
- Last date for team nomination and idea submission by the college SPOC: 20 Sept 2026. Confirmed in 2 live sources: guidelines PDF slide 10 and the deadline column of https://sih.gov.in/sih2026PS (fetched 2026-08-31). BITS Goa's internal round must finish far enough before 20 Sept for the SPOC to nominate and teams to upload.
- One team may submit ideas against a maximum of 2 problem statements. Guidelines slide 10 and https://sih.gov.in/faqs (fetched 2026-08-31). This is an underused hedge: the team gets a second shot for one extra deck.
- 500-idea cap per PS, then the PS freezes. Counts are public, per PS, on https://sih.gov.in/sih2026PS. Verified live 2026-08-31 by direct fetch: 229 PS (175 Software, 54 Hardware), and every one of the 229 rows reads 0/500 today. Crowding is currently unmeasurable from the portal; counters will move as SPOCs nominate, mostly in the 2 weeks before 20 Sept.
- 4 to 5 teams per PS reach the grand finale, and the PS organisation is not obligated to declare any winner. Guidelines slide 12. Finale: offline at nodal centres, December 2026 proposed, guidelines slide 13. Duration NOT published for 2026; past software finales ran 36 hours (PIB release title, https://www.pib.gov.in/PressReleasePage.aspx?PRID=2202893, page 403, ASSUMED for 2026).
- Prize Rs 1,50,000 per PS, paid only if the organisation likes the winning idea. Guidelines slide 18 and FAQ (fetched 2026-08-31).
- Nomination cap: 50 teams per institute (45 + 5 waitlist) in the guidelines PDF and FAQ; the sih.gov.in homepage says "best 30 teams + 5 waitlisted" (fetched 2026-08-31). 3 sources say 45+5, 1 says 30+5. Either way BITS Goa's internal round is a real filter, not a formality.
- Team: 6 members, same college, at least 1 female, up to 2 optional mentors at finale stage. Guidelines slides 7, 14.

## 2. The scoring rubric, restated with weights

The idea template's fields are the whole scoring surface. The official criteria list (guidelines slide 20, order as printed): novelty of the idea, complexity, clarity and details in prescribed format, feasibility, practicability, sustainability, scale of impact, user experience, potential for future work progression. No official weights exist anywhere; the weights below are my estimates, reasoning shown.

| Weight | Axis | Template home | Why this weight |
|---|---|---|---|
| 25 | Novelty and uniqueness | Slide 2 | First listed criterion, and the only axis that separates decks in a fast screen. With up to 500 near-identical AI-drafted decks per PS, sameness is fatal. |
| 20 | Technical approach credibility (complexity) | Slide 3 | The field label explicitly invites "working prototype" at idea stage. A named-component architecture plus prototype evidence beats icon soup. |
| 20 | Feasibility and honest risk | Slide 4 | The PS organisation picks 4-5 teams it believes will produce a prototype by December. Specific risks with tested mitigations signal competence. |
| 15 | Clarity and prescribed format | Whole deck | 6 slides max, points not paragraphs, PDF only (template slide 7). Screeners triage hundreds of decks; wall-of-text dies. An uncited prep blog claims 2-3 minutes per deck at national screening, ASSUMED. |
| 12 | Impact, scale, UX | Slide 5 | Every deck claims big impact, so variance is low at screening. It matters much more at the finale (see failure modes). |
| 8 | References and research | Slide 6 | Low ceiling, but a live dataset link plus 2 real citations is a cheap credibility signal most teams skip. |

Corroboration for roughly this shape: the one documented internal-round rubric found (Luthfaa Polytechnic, SIH 2025) scores 5 axes at 10 marks each: Innovation, Feasibility, Impact/Business Value, Technical Execution, Presentation (https://lpi.ac.in/pdf/REPORT%20on%20Internal%20Hackathon%202025%20LPI.pdf, fetched 2026-08-31). An SEO prep blog's uncited split (Innovation 25, Problem understanding 20, Feasibility 20, Impact 20, Presentation 15) also lands near mine, ASSUMED.

## 3. Why the event exists: the purpose model

- Sponsoring a PS costs the organisation real money: Rs 1,95,000 per software PS, Rs 3,00,000 per hardware PS per https://www.sih.gov.in/submit_problem_statement, while https://www.sih.gov.in/faqs says Rs 2.50L software / Rs 3.55L hardware plus Rs 25,000 registration (waived for government). The 2 official pages disagree on amounts (both fetched 2026-08-31), but both prove a PS is a paid, deliberate act by a named sponsor, not free-floating filler. Someone inside that organisation asked for this.
- The government's side of the trade: lifetime free access to the winning solution's IP, a 6-month to 1-year post-finale development window with a ministry-appointed technical agency, quarterly status reports to MIC/AICTE, and a recommended (not guaranteed) stipend of Rs 10,000-15,000 per month for up to 6 students. https://www.sih.gov.in/projectImplementation (fetched 2026-08-31). Functionally a procurement and R&D shortcut with no tender.
- Deployment reality: the government claims 24 projects implemented for 2022 and 30 for 2023, plus named acceptances (ISRO 4, Ayush 8, DST 4, DRDO 1) (PIB curtain-raiser mirrored at https://nagalandtribune.in/smart-india-hackathon-2024/, fetched 2026-08-31). Independently verified production deployments found: 0. Contradicting evidence exists: Careers360 documented 2019 hardware winners first contacted 8 months after winning and 2018 software winners waiting nearly 2 years (https://news.careers360.com/new-ideas-old-problems-what-happens-smart-india-hackathon-winners, fetched 2026-08-31). Implication for us: pitch deployment-readiness because judges score it, not because deployment is likely.
- What BITS Goa gets: SIH participation feeds the MoE Innovation Cell IIC star rating (1 of 5 scored components, https://www.edhitch.com/iic-star-rating-innovation-signal-iqacs-miss.html, fetched 2026-08-31) and press coverage (BITS has issued win releases before, https://www.bits-pilani.ac.in/bits-pilani-students-win-a-competition-in-smart-india-hackathon/, fetched 2026-08-31). Internal judges therefore optimise for teams that will not embarrass the institute at nationals and might produce a bragging right. ASSUMED but consistent with the incentive structure.
- Ministry engagement variance is real and evidenced: ISRO/SAC publishes named per-PS expert contacts and a dedicated inbox and took 4 solutions in-house; Ayush accepted 8; DST funded 4; DRDO accepted 1. Slow or absent: the 2 Careers360 cases above. Per-ministry finale attendance records: NOT FOUND (fetched 2026-08-31). A PS from an evidenced-engaged sponsor is worth a scoring bonus; an anonymous-sponsor PS carries jury-absence risk.

## 4. Internal round versus finale: the delta

Internal round (what we optimise first):
- Format: PPT plus live pitch, nothing built. 3 first-hand accounts confirm no prototype requirement (https://www.geeksforgeeks.org/contest-experiences/smart-indian-hackathon-sih-internal-hackathon-experience/, https://www.geeksforgeeks.org/smart-india-hackathon-sih-experience-year-2023/, https://sarahkhan.hashnode.dev/smart-india-hackathon-internal-hackathon-to-finals, all fetched 2026-08-31).
- Judges are faculty, likely 3-5 of them, scoring dozens of teams in one day (documented case: 9 teams, jury of 3, 5 rubrics x 10 marks, Luthfaa report above). At BITS Goa scale expect 30-100+ teams. ASSUMED range.
- One documented edge: being "the only team with a unique problem statement" helped a team clear internals (Sarah Khan account above). PS choice is itself a differentiator internally.
- What wins: a clear pitch, a PS the judges believe can win nationally, a team that looks able to build it, and novelty they can repeat to colleagues. Impact rhetoric matters more here than at national screening because the pitch is oral.

Finale (what we must not dead-end at):
- 3 mentoring rounds plus 3 scored evaluation rounds; one account weights them 20/30/50 with a working prototype required by round 3 (Sarah Khan above). 4 independent sources, including 1 jury-side, describe iterating on judge feedback between rounds as the actual scored game (https://www.linkedin.com/pulse/smart-india-hackathon-my-experience-mentor-evaluator-swet-chandan and others, fetched 2026-08-31).
- The most-cited first-hand loss reason is a weak business, cost or scalability answer: 3 first-hand accounts plus 1 guide. Technical wow with no unit economics loses at the end.
- Teams that arrive without a near-finished prototype cannot recover: "you can only improve your current prototype by 5 to 10%" (2024 winners, https://how-we-won-sih-24-and-survived-it.hashnode.dev/everything-about-winning-sih-2024, fetched 2026-08-31).

The delta in one line: internally you sell the idea and the team; at the finale you defend a working artifact's numbers under 3 rounds of adversarial iteration. A PS that pitches well internally but cannot yield a demoable artifact by December (data locked away, hardware-in-disguise, integration-only) is a dead end and must be filtered now.

## 5. Evaluator failure modes, ranked by independent source count

1. Weak cost, scalability or business answer: 3 first-hand + 1 guide. Prepare unit economics per PS.
2. No working or unstable prototype at the finale: 2 first-hand + 2 guides.
3. Weak grasp of the actual problem, solving the title not the body: 2 guides + 1 first-hand echo ("judges cared about the solution, not the technology").
4. Overscope, too many features: 2 guides, 0 first-hand. Plausible, weaker evidence.
5. Screening skim risk: 1 team claims their submitted video was never viewed; 1 blog claims 2-3 minutes per deck. Both single-source, ASSUMED. Design the deck so slide 2 alone can win the skim.
6. Crowding mechanics: SIH 2025 averaged 266 ideas per PS (72,165 ideas, 271 PS, https://www.newsonair.gov.in/8th-edition-of-smart-india-hackathon-2025-begins-mic, fetched 2026-08-31); in 2024 some PS hit the 500 cap while others drew 30-40 (https://dev.to/macroandmicro/behind-the-scenes-key-takeaways-from-our-smart-india-hackathon-2024-experience-5glc, fetched 2026-08-31). With 4-5 finale slots fixed per PS, a 30-40-idea PS implies roughly 12-17% finale odds versus roughly 1% at the cap. 1 first-hand counterexample of winning from a crowded PS exists. Crowding is a real lever, not the whole game.

Known reporting gap: Reddit was unreachable to the research agent (blocked crawler, 3 mirrors down), so internal-round politics and judge-diligence folklore are unverified in both directions, 0 sources.
