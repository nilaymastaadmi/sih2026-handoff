# SIH 2026 problem statement selection, packaged for audit

**Final pick: PS 26169, Indian Space Research Organisation (ISRO), Department of Space. Official title: "Development of an AI-Based Virtual Camera Tracking System for Coarse Alignment of Mobile Free Space Optical Communication (FSOC) Terminals". Category Software, theme Smart Automation.**

**Runner-up by rubric score: PS 26228, Ministry of Defence, Indian Army (DGIS). Official title: "Trustworthy Computer Vision Integrity Assurance for Data, Models and Inference Outputs in Multi-Contributor Pipelines". Category Software, theme Blockchain & Cybersecurity.**

Note before you go further: `09-final-decision.md` names PS 26147 (NTRO) as "the runner-up" on sponsor-engagement grounds, while the scored table in `artifact/sih-final5.html` places 26228 second at 74 and 26147 fourth at 67. That inconsistency is real and is recorded in `GAPS.md`. It was not resolved here because this package was assembled under an instruction not to re-litigate the pick.

The problem PS 26169 addresses, quoted verbatim from the official portal description for PS 26169:

> "Free Space Optical Communication (FSOC) offers unprecedented advantages for next-generation mobile networks, including gigabit-to-terabit data rates, license-free spectrum operation, high immunity to electromagnetic interference, etc. However, deploying FSOC links between mobile platforms (satellites, UAVs presents a severe challenge of pointing, acquisition and tracking (PAT) of highly narrow laser beams. PAT typically happens in two stages: coarse alignment and fine alignment. Coarse alignment is one of the key challenges of PAT, where the transmitting terminal must first locate and maintain the remote terminal within its camera Field-of-View (FOV)."

The problem PS 26228 addresses, quoted verbatim from the official portal description for PS 26228:

> "Operational computer vision pipelines may combine training data from multiple contributors, pretrained or vendor-supplied models, and inference outputs consumed by downstream systems. This creates distinct integrity and assurance risks across the data, model and inference lifecycle. Data may contain deliberately or inadvertently mislabelled samples, duplicated content, out-of-distribution material or trigger-based backdoors. A model may be substituted, modified or contain hidden behaviour that is not apparent during routine validation. Inference records may also be replayed, replaced or altered after generation unless they are cryptographically linked to the exact input, model and processing chain that produced them."

---

## Who produced what

Three passes contributed. Knowing which one wrote a file tells you how much to trust it.

- **Folder A**, the earliest research pass. Output is in `inputs/prior-passes/`. It produced a decision (26055 primary, 26166 second, 26066 fallback) that later work superseded.
- **Session 1**, an extraction and audit pass. It re-parsed the portal scrape from scratch, produced `evidence/ps_clean.tsv`, and audited Folder A and a second research folder. Output is `inputs/00-*`, `inputs/03-*`, `inputs/04-assets.md`, `evidence/ps_clean*`, and `scripts/session1/`.
- **Session 2**, this session. Everything numbered 01, 02, 05 through 13, plus `spike/`, the portal snapshots, the full-text sweep, and the annexures.

Content type is labelled as one of: **extracted** (pulled mechanically from a local file), **fetched** (retrieved from the live web this session), **reasoned** (written by a model from the above), or **run** (produced by executing code).

## Reading order

Read in this order if you know nothing.

| # | file | what it is | pass | type |
|---|---|---|---|---|
| 1 | `README.md` | this file | Session 2 | reasoned |
| 2 | `CLAIMS.md` | every load-bearing claim with its status. **Start auditing here.** | Session 2 | reasoned |
| 3 | `GAPS.md` | what was not done, and the weakest link. **Highest value file.** | Session 2 | reasoned |
| 4 | `09-final-decision.md` | the pick, why, and why each rival lost | Session 2 | reasoned |
| 5 | `12-spike-results.md` | the working prototype's measured results and the turbulence validation | Session 2 | run |
| 6 | `13-solution-spec-for-deck.md` | the solution specified against the six template slides | Session 2 | reasoned |
| 7 | `01-event-model.md` | rubric with estimated weights, purpose model, evaluator failure modes | Session 2 | fetched + reasoned |
| 8 | `08-winner-patterns.md` | what 16 past winning teams actually built. Corrects `02` | Session 2 | fetched |
| 9 | `10-the-2026-bar.md` | why past winners are a floor, not a target | Session 2 | reasoned |
| 10 | `11-build-playbook.md` | build plan derived from a red-team of an elite competitor | Session 2 | reasoned |
| 11 | `02-competitor-model.md` | the modal LLM pitch and axes to beat it. **Partly superseded by `08`** | Session 2 | reasoned |
| 12 | `05-independent-12.md` | the independent top 12, committed before reading prior passes | Session 2 | reasoned |
| 13 | `06-verification.md` | live counts, the 26055 dataset check, elimination from 12 to 5 | Session 2 | fetched |
| 14 | `07-hidden-gems.md` | the 128-PS coverage sweep and the adversarial prior-art results | Session 2 | fetched + reasoned |
| 15 | `00-RECOMMENDATION.md` | the earlier five-pick recommendation. **Superseded by `09`**, kept for the trail | Session 2 | reasoned |

## Directories

| path | contents |
|---|---|
| `inputs/` | what the analysis consumed: guidelines and IDEA template extracted verbatim, the folder critique, the merged longlist, the asset inventory |
| `inputs/prompts/` | the four prompts that drove each stage, including the one that produced this package |
| `inputs/prior-passes/` | Folder A's six phase files and its decision, plus its HTML output |
| `inputs/raw/` | original binaries: the guidelines PDF, the IDEA template pptx, the portal HTML scrape, `ps_all.tsv`, `ps19_full.md` |
| `evidence/` | `ps_clean.tsv` (229 rows) and its build notes, the live idea counts, portal snapshots from two dates |
| `evidence/ps-full-text/` | full official descriptions for all 158 non-template software PS: 30 in the longlist file, 128 across six sweep chunks |
| `evidence/ps-annexures/` | 42 files. `PS26169-annexure-ISRO.pdf` is the one that decided the pick. The rest are every other annexure found behind a portal "Dataset Link" field, left with the fetching agent's own filenames. Three things there will look odd and are not errors: the several 2-to-5-byte `.txt` files are failed text-layer extractions from image-only PDFs, the four `folder*.html` files are Google Drive folder listings, and `A_25017.pdf` is named that way because the Ministry of Rural Development folder advertises PS 26015 to 26019 but actually ships a file numbered 25017 |
| `evidence/portal-snapshots/` | the live sih2026PS page as fetched on 2026-08-31 and 2026-09-01, so counts can be re-derived |
| `evidence/spike-output/` | the prototype's performance log and the four-panel evidence image |
| `scripts/session1/` | the parsers that built `ps_clean.tsv` and the extractions |
| `scripts/session2/` | the modal extractor, the chunker, the template differ, and the script that built this package |
| `spike/` | the working prototype and the turbulence validation code. Runs on numpy and PIL |
| `working-notes/` | intermediate drafts, kept so the reasoning trail is inspectable rather than tidy |
| `artifact/` | the published comparison page's source |

## How to check the two most important things quickly

1. **The annexure.** Open `evidence/ps-annexures/PS26169-annexure-ISRO.pdf`. Page 2 and 3 carry the marking weights and the performance targets. If that document is stale or not authoritative, the main reason for the pick is gone. See claim 5 in `CLAIMS.md`.
2. **The prototype.** `cd spike` then `python fsoc_spike.py`. It needs numpy only. Compare its output against the table in `12-spike-results.md`. Then `python test_finite_screen.py` to re-derive the turbulence validation.
