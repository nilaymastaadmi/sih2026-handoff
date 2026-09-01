# ps_clean.tsv, build notes and cross-check report

Built 2026-08-31 by `round2/build_ps_clean.py` (parse), `round2/compare_ps.py` (cross-check) and `round2/make_ps_clean.py` (emit).
Output: `round2/ps_clean.tsv`, 229 data rows plus 1 header row.

## 1. What the two sources actually are

This matters, because they are not independent.

- `sih2026PS.html`, 2,626,093 bytes, 30,944 lines. A raw scrape of the SIH 2026 problem statement page. It contains two separate renderings of the same data: the listing table `<table id="dataTablePS">`, and one detail modal `<div id="ViewProblemStatementNNNNN">` per problem statement.
- `ps_all.tsv`, 336,011 bytes, 230 lines (1 header, 229 data). This file is **not** an independent source. It was produced from `sih2026PS.html` by `C:\Users\toshn\sih-2026\parse_ps.py`, which reads the modals and writes the TSV, truncating `Description` at 1500 characters.

So a literal "cross-check the two against each other" can only detect a parser bug in `parse_ps.py`, not a scrape error. To get a real second opinion, this build parses `sih2026PS.html` again from scratch with lxml, without reusing `parse_ps.py`, and compares three views:

| view | what it is | how obtained |
|---|---|---|
| LIST | the listing table rows (S.No., Organization, Title, Category, PS Number, Idea count, Theme, Deadline) | parsed fresh here |
| MODAL | the per-PS detail modals (ID, Title, Description, Organization, Department, Category, Theme, Youtube Link, Dataset Link, Contact info) | parsed fresh here |
| TSV | `ps_all.tsv` as it sits on disk | read as given |

`ps_clean.tsv` is emitted from MODAL, because MODAL is the only view carrying the untruncated description.

## 2. Row counts

| source | rows |
|---|---|
| `sih2026PS.html` LIST table body | 229 |
| `sih2026PS.html` modal divs | 229 (229 unique ids, 0 duplicate ids) |
| `ps_all.tsv` | 230 lines = 1 header + 229 data rows |
| `round2/ps_clean.tsv` | 230 lines = 1 header + 229 data rows |

The brief called `ps_all.tsv` a 230-row file. That is the line count including the header. The problem statement count is 229.

Set equality holds across all three views: the LIST id set, the MODAL id set and the TSV id set are the same 229 ids.

ID range 26001 to 26229. All 229 ids begin `26`. The block is contiguous: 0 numeric gaps in 26001 to 26229, 0 duplicate ids in any view.

## 3. Category split

| category | count | share of 229 |
|---|---|---|
| Software | 175 | 76.4% |
| Hardware | 54 | 23.6% |
| neither, blank or unclear | 0 | 0% |

Identical counts in all three views. No row carries a category value other than the exact strings `Software` and `Hardware`.

Category by theme, from `ps_clean.tsv`:

| theme | Software | Hardware | total |
|---|---|---|---|
| Smart Automation | 44 | 11 | 55 |
| Blockchain & Cybersecurity | 29 | 2 | 31 |
| Disaster Management | 23 | 2 | 25 |
| Agriculture, FoodTech & Rural Development | 13 | 9 | 22 |
| MedTech / BioTech / HealthTech | 13 | 5 | 18 |
| Miscellaneous | 12 | 3 | 15 |
| Robotics and Drones | 4 | 8 | 12 |
| Smart Education | 8 | 3 | 11 |
| Space Technology | 8 | 1 | 9 |
| Clean & Green Technology | 5 | 2 | 7 |
| Transportation & Logistics | 6 | 1 | 7 |
| Smart Vehicles | 4 | 2 | 6 |
| Heritage & Culture | 2 | 1 | 3 |
| Fitness & Sports | 1 | 1 | 2 |
| Renewable / Sustainable Energy | 1 | 1 | 2 |
| Travel & Tourism | 1 | 1 | 2 |
| Toys & Games | 1 | 1 | 2 |
| **total** | **175** | **54** | **229** |

## 4. Every row where the sources disagree

### 4a. ID

0 substantive disagreements. All 229 ids match across LIST, MODAL and TSV.

229 of 229 rows carry a **formatting** difference in one field the views render differently: the LIST table's `PS Number` column prints `SIH26001` while the modal's `Problem Statement ID` field and the modal div id both read `26001`. This is a constant `SIH` prefix applied to every row, not a per-row conflict. It is recorded once rather than 229 times because the rule is uniform: for every id N in 26001 to 26229, LIST `PS Number` equals `SIH` followed by N, LIST `data-target` equals N, MODAL `Problem Statement ID` equals N, TSV `Problem Statement ID` equals N. Verified programmatically on all 229 rows with 0 exceptions.

`ps_clean.tsv` carries the unprefixed form, `26001`, matching the modal.

### 4b. Title

0 disagreements. All 229 titles are identical across LIST, MODAL and TSV after whitespace normalisation.

### 4c. Organisation

0 disagreements. All 229 `Organization` values are identical across LIST, MODAL and TSV after whitespace normalisation.

### 4d. Fields not required by the brief, checked anyway

- Category: 0 disagreements across 229 rows.
- Theme: 0 disagreements across 229 rows.
- Description: LIST does not carry it. 158 of 229 TSV descriptions are exactly 1500 characters, the truncation limit hard-coded in `parse_ps.py`. All 229 TSV descriptions match the first 1500 characters of the corresponding MODAL description exactly. So `ps_all.tsv` is lossy but not wrong: it loses tail text on 158 rows and alters nothing. MODAL description lengths run 78 to 12,027 characters, mean 2,560.

## 5. Rows dropped

**0 rows dropped.** All 229 problem statements are present in `ps_clean.tsv`.

The drop criteria applied, and the count failing each:

| criterion | rows failing |
|---|---|
| missing or non-numeric `Problem Statement ID` | 0 |
| empty `Problem Statement Title` | 0 |
| empty `Organization` | 0 |
| empty `Department` | 0 |
| empty `Category` | 0 |
| empty `Theme` | 0 |
| empty `Description` | 0 |
| id present in one view but absent in another | 0 |
| duplicate id within a view | 0 |
| embedded tab or newline that would corrupt the TSV | 0 |
| leading, trailing or doubled whitespace after normalisation | 0 |

## 6. PS IDs that look carried over from SIH 2024 or SIH 2025

**By ID numbering: 0 of 229.** Every id sits in the 26001 to 26229 block, which is the SIH 2026 numbering series. SIH 2024 ids ran in a 1xxx series and SIH 2025 ids in a 25xxx series; no id in this file falls in either range. The block is contiguous with no gaps, which is what a freshly minted single-year series looks like.

**By title or description: not verifiable on this machine. ASSUMED.** There is no SIH 2024 or SIH 2025 problem statement dataset anywhere under `C:\Users\toshn\`, so a title-level or description-level comparison against prior years cannot be run. Any claim that a given 2026 problem statement restates a 2024 or 2025 one would be unverified guesswork and is not made here. Getting a real answer needs the prior-year PS lists pulled from sih.gov.in/sih2024 and sih.gov.in/sih2025.

**Prior-year artifacts that ARE present in the scrape, and what they are.** These are page-template leftovers, not carried-over problem statements.

| artifact | where | what it is |
|---|---|---|
| `<tr id="ps-2024">` | thead of `<table id="dataTablePS">` | leftover row id from the SIH 2024 page template |
| `href="/letters/SIH2025-Guidelines-College-SPOC-updated.pdf"` | mobile nav menu | the mobile nav on the 2026 PS page still links the **2025** SPOC guidelines |
| `href="/letters/SIH2025-IDEA-Presentation-Format.pptx"` | mobile nav menu | the mobile nav still links the **2025** idea presentation template |
| `https://x.com/SIH2025` | footer social links | 2025 handle |
| `(c) 2025-26 Smart India Hackathon` | footer | copyright line |
| `/sih2024`, `/sih2025` dropdown entries | top nav | archive links to previous editions |

The two stale `SIH2025-*` document links matter for a practical reason. The local copies in `C:\Users\toshn\sih-2026\` are named `SIH2026-Guidelines.pdf` and `SIH2026-IDEA-Format.pptx`, so they did not come from those mobile-nav links. Their provenance is not established by this scrape. The pptx package metadata gives `dcterms:modified = 2026-06-02T09:29:39Z` and `cp:lastModifiedBy = AICTE`, which is consistent with a 2026 file.

## 7. Column mapping, stated explicitly

The requested schema asks for `organisation` and `ministry`. The source has no field named `ministry`. Its two body fields are `Organization` and `Department`. The mapping used is a straight copy with no reinterpretation:

| output column | source field | copied verbatim |
|---|---|---|
| `ps_id` | modal `Problem Statement ID` | yes |
| `title` | modal `Problem Statement Title` | yes |
| `organisation` | modal `Organization` | yes |
| `ministry` | modal `Department` | yes |
| `category` | modal `Category` | yes |
| `theme` | modal `Theme` | yes |
| `description_short` | modal `Description`, truncated | prefix only, see section 8 |

**Read the `ministry` column with this caveat.** In this dataset `Organization` is the top-level posting body and `Department` is the sub-unit under it. On 174 of 229 rows the two differ, and on those rows the `ministry` column holds a sub-unit, not a ministry: `SAIL`, `NMDC`, `Coal India Limited`, `India Meteorological Department`, `AICTE, MIC-Student Innovation`, and so on. On the remaining 55 of 229 rows `Organization` and `Department` are identical strings and both columns carry the same value.

The `organisation` column is also not uniformly a ministry. Only 104 of 229 rows have an `Organization` string beginning with the word `Ministry`. The other 125 are agencies (NTRO 23, ISRO 11, DRDO 7, AICTE 34 plus 3 under its long name, MoSPI 4), state governments (Government Of Maharashtra 9, Governmcnt of Jharkhand 5) and private companies (Autodesk 5, Bharat Electronics Limited 5, Egreen Quanta 5, Qualcomm Inc 5, Oil India Limited 4, MRPL 3, MathWorks 2).

32 distinct `Organization` values, 43 distinct `Department` values.

## 8. How description_short was produced

Rule, applied identically to all 229 rows and to nothing else:

1. Take the modal `Description` with its HTML tags stripped and whitespace collapsed to single spaces.
2. If it is 200 characters or fewer, keep it whole.
3. Otherwise take the first 200 characters and cut back to the last space, so no word is split.
4. Add nothing. No ellipsis, no marker, no rewording, no reordering, no selection of a better sentence.

Result: every `description_short` value is a literal prefix of the official description. Longest value 200 characters. 37 of 229 rows have a description of 200 characters or fewer, so on those 37 rows `description_short` is the complete official description; on the other 192 it is a prefix.

Because the official descriptions almost all open with the literal word `Background:` followed by scene-setting, a 200-character prefix frequently ends inside the background paragraph and does not reach the `Expected Solution:` section. Anyone judging a problem statement on `description_short` alone is reading its opening sentence. The full text is in `sih2026PS.html` and, truncated at 1500 characters, in `ps_all.tsv`.

## 9. Data quality observations in the source

Factual, verified by count. No judgement about any problem statement's merit is made or implied.

**17 pairs of exactly duplicated titles and descriptions.** IDs 26193 to 26209 and 26210 to 26226, all `AICTE` / `AICTE, MIC-Student Innovation`. Each pair shares an identical title and an identical description and a shared theme, differing only in `Category`: the 26193 to 26209 run is Software, the 26210 to 26226 run is Hardware. Verified on all 17 pairs. This is the Student Innovation category offered once per theme in each category, not a scrape defect. It means the 34 Student Innovation rows describe 17 distinct briefs.

**Typographic errors in the source, reproduced verbatim in `ps_clean.tsv`:**

| error | correct form | rows | ids |
|---|---|---|---|
| `Al-` with a lowercase L where `AI-` is meant, in titles | `AI-` | 9 | 26002, 26004, 26027, 26039, 26042, 26107, 26109, 26111, 26188 |
| `Governmcnt of Jharkhand` | `Government of Jharkhand` | 5 | 26039 to 26043 |
| `National Centre for Polar andOcean Research (NCPOR)`, missing space | `Polar and Ocean` | 7 | 26059 to 26065 |
| `lndian` with a lowercase L in a title | `Indian` | 1 | 26109 |
| `Indian Cyber Crime Coordination Centre (I4C),CIS Division`, missing space after comma | | 3 | 26182 to 26184 |
| `Yantra India Limited, Ambajhari,Nagpur`, missing space after comma | | 1 | 26098 |

61 titles use `AI` correctly, so the lowercase-L form is a minority error, not a house style. **Any exact-string title match against this file will fail on those 9 rows unless the L-for-I substitution is handled.** That is the single most likely cause of a title verification failing in Task D.

**Two bodies spelled two ways each:**

| variant A | rows | variant B | rows |
|---|---|---|---|
| `AICTE` | 34 (26193 to 26226) | `All India Council for Technical Education (AICTE)` | 3 (26104, 26105, 26106) |
| `Ministry of defence (MoD)`, lowercase d | 2 (26227, 26228) | `Ministry of Defence (MoD)`, capital D | 1 (26098) |

An exact-string organisation match will treat each pair as two different bodies.

**Field completeness across all 229 rows:**

| field | non-empty | empty |
|---|---|---|
| Problem Statement ID | 229 | 0 |
| Problem Statement Title | 229 | 0 |
| Organization | 229 | 0 |
| Department | 229 | 0 |
| Category | 229 | 0 |
| Theme | 229 | 0 |
| Description | 229 | 0 |
| Dataset Link | 44 | 185 |
| Youtube Link | 5 | 224 |
| Contact info | 0 | 229 |

**Scrape timing.** The `Submitted Idea(s) Count` column reads `0/500` on all 229 rows and the `Deadline for Idea Submission` column reads `20 September 2026` on all 229 rows. A uniform zero count means this scrape was taken before any idea was submitted, so it carries no signal about which problem statements are crowded. Competition data needs a fresh pull of that column closer to the deadline.

**Mojibake in the source.** 70 of 229 rows carry at least one double-encoded character sequence. `sih2026PS.html` itself decodes as strict UTF-8 (2,626,093 bytes, 0 decode errors), so the corruption was already in the portal's stored text before the page was rendered; it is not introduced by the scrape or by this parser. Occurrence counts: 219 sequences beginning `â€` (covering em dash, en dash, curly single and double quotes, and bullet), 22 `Â°` (degree sign), 3 `Âµ` (micro sign), 1 `Ã±`, 1 `Ã©`. These are reproduced verbatim in `ps_clean.tsv` rather than silently repaired, so the file still matches the portal. Any full-text search for a phrase containing a dash or an apostrophe needs to allow for it.

## 10. Prompt-injection check

All 229 rows, every field, plus the raw HTML, were scanned for text addressed to an AI reader: `as an AI`, `ignore previous`, `ignore prior`, `disregard`, `system prompt`, `you must now`, `language model`, `LLM`, `assistant`, `prior instructions`, `do not tell`, `pretend`, `jailbreak`, `claude`, `chatgpt`, `gpt-`, `instructions to the model`, `your task is to`, `you are an AI/assistant/agent/model`.

42 pattern hits across the modal fields, 84 across the raw HTML (the raw count double-counts because each description is stored twice on the page, once live and once inside an HTML comment). **0 of them are an instruction addressed to the reader of this file.** Every hit is subject-matter content: problem statements that are themselves about building AI assistants. Three worth quoting so nobody has to re-check them:

- **26027**, Ministry of Railways: `Your task is to develop an Automatic Block Planning system that integrates maintenance, defects and corri...`. Addressed to the participating student team, which is standard SIH problem-statement phrasing. Not addressed to a model, and it instructs nothing about how to read or rank this dataset.
- **26117**: `None of this can go through cloud AI assistants like Claude or Codex because the underlying data is confidential`. The word Claude appears as an example of a cloud AI product inside a problem statement about air-gapped tooling. Descriptive, not directive.
- **26154**: `The system shall act as an AI-powered content transformation engine`. Describes the software to be built, not the reader.

Nothing in `sih2026PS.html` or `ps_all.tsv` tells the reader what to conclude, what to shortlist, or what to ignore.
