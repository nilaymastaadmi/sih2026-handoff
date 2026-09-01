# 06. Verification and elimination

Written 2026-08-31 after reading `03-folder-critique.md` and `03-merged-longlist.tsv`. The 12 from `05-independent-12.md` were committed before this file was opened. All fetches dated 2026-08-31.

## Part A. Where my 12 agree and disagree with the two folders

My 12: 26147, 26073, 26228, 26117, 26055, 26166, 26168, 26143, 26066, 26027, 26034, 26123.

- **Absent from both folders' combined 65-PS coverage: 26228, 26034, 26123.** Clean coverage wins, exactly the gap the brief flags.
- **Touched only glancingly by Folder A, never reaching a scored shortlist: 26168** (one-line completeness-critic mention, "longlisted-not-designed") and **26027** (phase-3 longlist, then killed DEAD by a skeptic without ever being scored in a tier). So **5 of my 12 were not meaningfully shortlisted by either pass**: 26228, 26034, 26123, 26168, 26027. Floor of 5 met, stated honestly rather than inflated.
- **Overlap with Folder A:** 26055 (its PRIMARY), 26166 (its SECOND), 26066 (its FALLBACK and only SURVIVES), 26147 (its top-5 rank 5, and its highest raw score at 82), 26073 (its Tier 1), 26117 (its Tier 2, killed DEAD), 26143 (its Tier 2 near-miss at 72).
- **Overlap with Folder B:** effectively none. Folder B worked from titles only and its territory (deepfake, document forensics, quantum, MathWorks) barely intersects mine. This is expected and is itself evidence: Folder B never read a description, so it could not surface the description-driven picks (26147, 26228, 26073, 26034) that my process rewards.

### What the critique changed in my thinking

1. **Folder A's own raw scores rank 26147 first**: 26147=82, 26066=80, 26055=79, 26166=~78, 26073=70. Folder A then inverted 26147 to rank 5 in its top five using a CROWDING axis. I have now shown (Part B) that crowding is uniformly 0/500 across all 229 PS and therefore unmeasured. Stripping the unmeasured crowding adjustment re-elevates 26147 to the top. This is the spine of my disagreement with the lock.
2. **26055's kill risk is resolved in its favour** (Part B): the Turing dataset exists, so the stated mitigation for its only weakness holds. 26055 survives.
3. **26027 loses me**: on full re-read I agree with Folder A's DEAD verdict. Cut.
4. **26117 loses me** for reasons broader than Folder A's (which rested on a void premise): overscope, no single ungameable number, buzzy enough to draw the crowd. Cut.
5. **The 26104 collision** (Folder A 63 "mobbed" vs Folder B 75% rank 1): I never had 26104 in my 12; I bubbled it as ASSUMED the most crowd-exposed cyber PS. The critique confirms the crowding concern is real and unmeasured on both sides. I do not add it. It is the textbook case of a PS every LLM recommends.

## Part B. The three required checks

### Check 1. Live idea counts (the only real crowding evidence)

I downloaded the live listing https://sih.gov.in/sih2026PS fresh on 2026-08-31 (2,642,733 bytes, saved to scratchpad) and regex-extracted the `Submitted Idea(s) Count` cell for every row.

**Result: all 229 PS read 0/500. 0 of 229 nonzero.** Split confirmed at 175 Software, 54 Hardware, matching session 1. The submitted-count column is public and served in plain static HTML (no JavaScript), exactly as the guidelines promise, but no idea has been submitted against any PS yet. Idea submission opens ahead of the 20 Sept 2026 deadline; SPOCs nominate in the final 2 weeks, so counters will move then.

**Consequence, applied throughout:** every crowding score in this document and in Phase 7 carries the word ASSUMED with its reasoning shown. There is no measured crowding for any PS. The extraction pipeline is saved and can be re-run in one command closer to the deadline; that re-run is the single highest-value action before submission.

### Check 2. The 26055 dataset

The portal's malformed link `huggingface.co/datasets/alan-turing institute/turing-synthetic radar dataset` (two spaces) corrects to `alan-turing-institute/turing-synthetic-radar-dataset`.

**It exists.** Hugging Face page resolves (fetched 2026-08-31). The Turing Synthetic Radar Dataset (TSRD): approximately 4 billion pulses across 6,000 pulse trains, up to 90 emitters per train, built specifically for radar pulse deinterleaving in electronic-warfare and signal-intelligence research. **Size 70 GB. Licence Apache 2.0. Access is gated**: a contact-information agreement plus a free Hugging Face login is required before download. A duplicate mirror exists at `alan-turing-institute/Turing_Synthetic_Radar_Dataset`.

**Verdict: the kill criterion does not fire.** The dataset that Folder A named as the mitigation for 26055's only stated weakness (the "self-tuned emitter sim" critique) is real, openly licensed, and downloadable behind a soft contact gate. It actually strengthens 26055, because it supplies external emitter truth to validate the scan scheduler against an environment the team did not generate. Two practical caveats: 70 GB is a heavy download, and the sim-plus-scheduler core of 26055 can be built without it, so the dataset is a validation asset, not a dependency.

### Check 3. Data availability for the other finalists

Verified by two independent research passes on 2026-08-31. Summary for every PS that survives to the final 5, plus the ones cut on other grounds.

| PS | Named data | Resolves? | Gate | Verdict |
|---|---|---|---|---|
| 26147 | DeepSig RadioML 2016/2018 + self-generate in GNU Radio | yes | RadioML direct download, CC BY-NC-SA; generator public at github.com/radioML/dataset | **Strongest data story: self-generable, no gate, we control ground truth** |
| 26073 | NOAA ISD; IMD DSP portal; Kaggle | yes | ISD public no-login (also AWS Open Data mirror); IMD DSP is a paid/request portal | Public path confirmed via ISD + Kaggle; IMD's own AWS feed is gated |
| 26228 | NIST TrojAI; BackdoorBench; COCO/YOLO | yes | TrojAI marked PUBLIC (data.nist.gov/od/id/mds2-3163); BackdoorBench public GitHub; COCO/YOLO public | No data risk |
| 26166 | Chandrayaan-2 via ISSDC PRADAN; LROC NAC | yes | LROC NAC public, no registration; Chandrayaan-2 needs a free ISSDC signup, activation latency ASSUMED ~1 day | Ungated fallback (LROC) plus free-signup primary; safe |
| 26055 | Turing TSRD | yes | 70 GB, Apache 2.0, contact-gate | See Check 2; sim self-contained anyway |
| 26168 (cut) | IO-VNBD | yes | public GitHub, no licence stated; comma2k19 (MIT) as fallback | data fine |
| 26143 (cut) | Zenodo Sentinel-1 oil spill 40.9 GB CC BY 4.0; marinecadastre AIS | yes | both open, no login; AIS is US-waters only | data fine but AIS is not Indian-Ocean |
| 26066 (cut) | GLORYS; INCOIS gridded ARGO | yes | GLORYS free w/ Copernicus account; INCOIS ERDDAP public | data fine, heavy engineering |
| 26034 (cut) | Legal Metrology (Packaged Commodities) Rules 2011 | yes | public on India Code, no login; demo data is any product on any shelf | statute-as-data fully available |

**No PS in my final 5 fails the data-availability kill test.** The one PS whose data story is weakest, 26073, still has a confirmed no-approval source (NOAA ISD), so it survives; the note is recorded in its Phase 7 data-risk line.

## Part C. Elimination round: 12 to 5

For each of the 12 I argue the case that it loses, then record the decision. Tests applied: data does not exist publicly; hardware or field problem in software clothing; a shipped product already does it; will be the crowded PS; cannot be demoed in the minutes we get; the honest deliverable is policy/integration/procurement, not software; a domain gate we cannot cross; a weak or absent jury.

**KEPT (5):**

- **26147 NTRO signal analysis.** Losing case: the blind FEC/de-interleaving chain that defines the PS is genuinely hard and may not fully ship for the finale (Folder A skeptic, WEAKENED). Rebuttal: for the idea round no build is required, and the hard part is exactly what no generalist LLM team can even write a credible slide for; the easy part (modulation ID) being solved means the modal deck loses on the actual ask. Data self-generable, crowd ASSUMED low, deepest asset fit. KEPT.
- **26073 MoES/IMD AWS anomaly.** Losing case: IMD already runs WMO-standard QC, so a jury may call it solved (Folder A skeptic). Rebuttal: the PS explicitly wants ML-based, explainable, edge-deployable detection and publishes its own scoring rubric, which we can build to exactly; the ESP32 live demo is the cheapest reliable physical demo on the board. KEPT.
- **26228 MoD CV integrity.** Losing case: the 5-capability scope is broad and could sprawl. Rebuttal: the cryptographic inference-provenance capability maps almost verbatim to a Merkle-chained decision log we have already built and verified; public benchmarks named in the PS; near-zero crowd (last rows of the list, hard, no consumer appeal). Coverage win. KEPT.
- **26166 ISRO lunar correspondence.** Losing case: October-December bandwidth and team-fit (Folder A). Rebuttal: public data with a named metric (sub-pixel RMSE, inlier ratio), the most documented-engaged sponsor in the purpose model, and a clean wedge (beat the SIFT/ORB baseline that collapses across illumination). KEPT.
- **26055 DRDO EW.** Losing case: the interception-rate gain could be an artifact of a self-tuned sim (Folder A). Rebuttal: the Turing dataset (Check 2) supplies external emitter truth to close exactly that gap; self-contained build, DSP asset fit, crowd ASSUMED low. KEPT, but demoted from Folder A's primary to my rank 5.

**CUT (7), one line each:**

1. **26027 Railways block planning** killed by internal-only source systems (TMS/SMMS/TDMS/COA), an optimisation that is a solver library call, and a self-defined baseline that is unfalsifiable: three independent failures.
2. **26117 MRPL sovereign agentic workbench** killed by overscope and buzz: a do-everything agent with no single ungameable headline number, attractive to exactly the LLM crowd we want to avoid.
3. **26123 BEL AMR fleet coordination** killed by prior art: mature multi-agent path-finding literature already provides the answer, and it reads as a robotics-class project rather than a differentiated entry.
4. **26066 MoES OceanEmbed** killed on opportunity cost: strong and data-real, but a heavy data-engineering lift in a niche domain, and 26166 fills the "public data plus named metric plus engaged sponsor" slot with a cleaner demo.
5. **26143 NTRO oil spill + AIS** killed on ambition and overlap: two-modality fusion plus drift hindcasting is a lot for the window, the AIS data is US-waters only, and it competes with 26055/26166 for the geospatial-DSP slot.
6. **26168 ISRO dead reckoning** killed on overlap and gate: its proposal-stage measurement requirement is excellent and its demo visceral, but the sub-10% drift benchmark is a hard technical bar and it duplicates 26166's ISRO slot. Retained as the natural SECOND national idea beside 26166, not in the top 5.
7. **26034 DoCA Legal Metrology** killed on ceiling: real-data-in-hand and very demoable, but the lowest ceiling of the set and adjacent to the generic compliance-checker genre. Best kept as a safe fallback if a top pick is dropped.

## Part D. Verdict on the locked decision

The lock (26055 primary / 26166 second / 26066 fallback, recorded in `MEMORY.md` as `decision-2026-08-31-sih-2026-entry`) **partially survives**.

- **Survives:** 26055 and 26166 both remain in my final 5, so both ideas are validated on the merits.
- **Breaks:** the ranking. 26055 drops from primary to my rank 5; 26166 drops from second to my rank 4; 26066 is cut entirely. My rank 1 is 26147, the PS Folder A scored highest (82) and then demoted to rank 5 on a crowding axis I have shown is uniformly unmeasured today.
- **Evidence that would change it back:** live idea counts (once submissions open) showing 26147 crowded near the 500 cap while 26055 stays quiet would restore 26055 to the top; or our own inability, in a 2-day spike, to demonstrate any blind demodulation on self-generated IQ would drop 26147 below 26073 and 26055.
