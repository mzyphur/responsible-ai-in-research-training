# Changelog

All notable changes to *Responsible AI in Academic Research: A Competency Framework for Research Training* are recorded in this file. The publication uses [Semantic Versioning](https://semver.org/).

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [1.2.9] — DOCX TOC anchor fix-up (2026-05-21)

Rebuilds the generated publication artifacts with the general-repo v0.22.42
DOCX TOC-anchor fix, then applies the same anchor rewrite after the
LibreOffice Word round-trip. This resolves the issue where Word TOC entries
clicked to the top of the document instead of their target sections. No
content findings change.

## [1.2.8] — Hero byline: primary role only (2026-05-21)

Removes long-form UQ affiliation from the hero. Appendix D About-the-author
and the COI disclosure retain the full UQ affiliation. No content findings
change.

## [1.2.7] — Mobile body-width fix (2026-05-21)

Mobile @media rules: .wrap padding 36px → 20px; .exec padding 24px → 16px;
.colophon margins -36px → -20px. Body text on phone viewports now matches
the hero width.

## [1.2.6] — COI clarification + PhD phrasing tidy (2026-05-21)

Two small edits: (1) COI disclosure now explicitly notes the author's UQ
employment given UQ's inclusion in the sample; (2) "at PhD level" → "at
the PhD level" for natural phrasing. No content findings change.

## [1.2.5] — 2026-05-20

### Changed — terminology: capability framework renamed to competency framework

Renamed the report terminology from "capability framework" to "competency framework" throughout source metadata, README, report prose, research dossiers, and retained working notes to align the publication with researcher-skill and research-training language used in UK/Australia pedagogy. This is a terminology update only: the evidence base, five-dimension framework structure, maturity grid, DOI, and substantive recommendations are unchanged.

Generated publication artifacts were rebuilt from the updated source so HTML, PDF, DOCX, citation metadata, and Open Graph metadata carry the new terminology consistently. External proper names and URL slugs that genuinely contain "Capability" / "capability" were preserved.

## [1.2.4] — 2026-05-19

### Changed — canonical AI-assistance disclosure paragraph (general-repo v0.22.21)

The AI-assistance disclosure paragraph in Appendix D now uses the canonical Instats Policy Series wording introduced in general-repo v0.22.21 (`methodology/public_private_boundary_protocol.md` § Single allowed AI-assistance disclosure sentence): names the three tool families used across the publication round (Anthropic Claude Code Opus 4.7, OpenAI Codex GPT-5.5, Google Gemini 3 Flash Preview), asserts author responsibility, contains no other production-discipline detail.

The previous wording was generic ("large language models for evidence synthesis, structural review, and copy editing"). The canonical wording is more specific about which tools were used and is consistent in shape with other Instats publications (gas-tax v3.2.8 ships the identical canonical paragraph in the same publication round).

### Rebuilt on general-repo v0.22.21 pipeline (defense-in-depth gates active)

Same substantive content as v1.2.3; rebuilt through the general-repo v0.22.21 pipeline so the docx benefits from the post-build defense-in-depth gates: bookmark-name normaliser + Mac-Word-strict validator + RGBA → RGB PNG flatten (from v0.22.20) plus degenerate-zero-width-WordprocessingShape normaliser + validator (new in v0.22.21).

v1.2.3's source-level chart RGB conversion remains in place; the v0.22.20 + v0.22.21 build-time gates act as belt-and-braces against any future regression. SHA256 of `report.docx` differs from v1.2.3's (new build + new disclosure paragraph), but the substantive evidence, framework, recommendations, and DOI are unchanged from v1.2.3.

## [1.2.3] — 2026-05-19

### Fixed — Chart PNG now RGB (no alpha channel) for Mac Word compatibility

Lead-author reported v1.2.2 docx STILL did not open in Mac Word — two errors: *"Word experienced an error trying to open the file"* and *"Word found unreadable content in report.docx. Do you want to recover the contents..."* This was a regression from v1.2.1 (which the user confirmed opens cleanly).

**Diagnosis:** the only substantive difference between v1.2.1's docx (works) and v1.2.2's docx (fails) is the Figure 1 chart PNG. All 53 bookmark names remain Word-compatible after the v1.2.1 + v1.2.2 builds; document.xml differs only in the chart's cy (height) attribute and the version string. The v1.2.2 PNG is larger (3384x1390 vs 2784x1182, 233 KB vs 154 KB) but both are RGBA from matplotlib's default `savefig`.

**Suspected root cause:** matplotlib outputs RGBA PNGs (4 channels with alpha). Mac Microsoft Word has documented compatibility issues with PNGs that have alpha channels — specifically the "Word found unreadable content" recovery flow when an embedded image's alpha channel cannot be processed cleanly. LibreOffice tolerates RGBA PNGs; Mac Word does not always.

**Fix:** added a post-savefig RGB conversion step at the end of `charts/01_regulatory_response_timeline.py` — PIL flattens the RGBA chart onto a white background (the chart's intended background colour per Instats style) and re-saves as RGB. No alpha channel reaches Mac Word.

```python
from PIL import Image
with Image.open(png_path) as img:
    if img.mode == "RGBA":
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        bg.save(png_path, "PNG", optimize=True, dpi=img.info.get("dpi", (300, 300)))
```

The chart visual is unchanged (the background was already white; we're just flattening the alpha layer that was always 255). PNG file size: 233 KB → 222 KB. Embedded in docx after rebuild: `mode=RGB, size=(3384, 1390)`.

**General-repo v0.22.20 follow-up** (documented in working notes): the RGBA→RGB conversion belongs in `general-repo/charts/style.py` or a post-savefig helper so all future chart scripts get the Word-safe PNG output for free. Combined with the bookmark-name normaliser (now also queued for v0.22.20), the docx-broken-in-Mac-Word class of defect will be permanently closed.

No prose, framework, or evidence changes from v1.2.2.

verify-publication: 19 passed, 0 failed; Stage-A carry-over PASS.

## [1.2.2] — 2026-05-19

### Changed — Figure 1 chart redesign (eliminate overlapping annotations; publication-quality)

Lead-author feedback after v1.2.1: *"Figure 1 in the responsible AI document looks like shit. ... The text on the graph is blocking everything. It looks like a robot made it! Make it very pretty and clear with no overlapping text."*

Specific failure modes in the v1.2.1 chart:

1. The "Vitae RDF refresh / missed AI · May 2025" callout block was positioned at month 30, overlapping the "Sep 2023 to Apr 2026" label INSIDE the funders bar.
2. The "Tsinghua AI framework · Dec 2025" annotation sat below the universities lane, crowding the X-axis label area.
3. Corner labels ("ChatGPT-3.5 release Nov 2022" + "May 2026") competed with lane labels for visual attention.
4. Multiple arrow leader lines intersected the bars and dots.

Redesign (codex GPT-5.5 xhigh, executed against the chart-redesign brief at `private/reviews/chart_redesign_brief.md`):

- **Figure size increased** from (10, 4.35) to (12, 5.5) — more breathing room.
- **Right-side callout panel** (figure x=0.8 onwards) — lists the six Class D universities by publication date, separated from the chart proper by a thin vertical rule. No more leader-line callouts pointing into the bars/dots.
- **Inline lane summary labels** — each lane has a single in-bar (or below-bar) summary positioned to never overlap anything else:
  - PUBLISHERS bar: "0-3 months / ~10 weeks" in primary teal-navy
  - NATIONAL RESEARCH FUNDERS bar: "10-41 months / Sep 2023-Apr 2026" in paper-white against the secondary mid-teal
  - UNIVERSITIES lane: "6 Class D policies by May 2026" + "32 of 38 universities still not at Class D" below the lane
- **Real date X-axis** — replaces the abstract "months from ChatGPT-3.5 release" ticks (0-42) with actual two-line dates (Nov 2022, May 2023, Nov 2023, May 2024, Nov 2024, May 2025, Nov 2025, May 2026). The X-axis title remains "Months from ChatGPT-3.5 release" as a unit reminder.
- **Bottom-right caption block** in the right callout panel: "The blank university lane is the result: most audited institutions had not published AI-literacy + valid-practice guidance." Explains the visual emptiness for the skim reader.
- **6 red Class D markers** preserved (`# red-clusters: 6` directive in chart-script header unchanged).

The chart now visually delivers the headline finding without any text overlap. Codex's redesign artefact preserved at `private/reviews/chart_redesign_codex_2026-05-19.md`.

No prose changed in the report; the chart caption (Figure 1 markdown) is unchanged (it still describes the same data; the chart now renders it cleanly).

verify-publication: 19 passed, 0 failed; Stage-A carry-over PASS.

## [1.2.1] — 2026-05-19

### Fixed — DOCX now opens in Mac Microsoft Word (bookmark-name compatibility)

**Root cause** (identified by codex GPT-5.5 xhigh research, with the smoking-gun diff between gas-tax v3.2.5 — which opens in Mac Word — and responsible-ai v1.2.0 — which did not): the Figure 1 chart embed used pandoc's anchor syntax `{#fig:timeline}`, where the colon in the anchor name produced an OOXML bookmark named `fig%3Atimeline` (pandoc URL-encodes the colon to `%3A`). **Mac Microsoft Word's stricter OOXML schema validator rejects bookmark names containing `%`** — per Microsoft's documentation, Word bookmark names must begin with a letter and contain only letters, numbers, and underscores. LibreOffice tolerates `%` in bookmark names; Mac Word does not. Each `soffice` round-trip made it worse (the existing `%` got re-encoded to `%25`, producing `fig%253Atimeline`).

**Fix**: changed `{#fig:timeline}` → `{#fig-timeline}` in `drafts/report.md:63` (the only chart anchor). Rebuilt the DOCX. Verified all 53 bookmark names are now Word-compatible: zero contain `%` or `:`.

**Why no earlier publication hit this**: gas-tax does not use pandoc figure anchors of the form `{#fig:NAME}`. Its 12 chart embeds use the default pandoc image syntax without anchor IDs, so no bookmark with a colon was generated. The responsible-ai chart embed was the first time a figure anchor was added with the colon-bearing convention.

**Why local LibreOffice round-trip didn't catch it**: LibreOffice's OOXML parser is more permissive than Mac Word's. The verify-publication DOCX gates check style references, footnote resolution, and required parts — but did not check bookmark-name validity against the OOXML spec's stricter rules that Mac Word enforces.

**General-repo v0.22.20 follow-up** (documented in `private/redraft_v1_1_0_working_notes.md`):
1. Add a build-time check that rejects bookmark names containing `%` or `:` after the DOCX is built. Fail-loud, before publish_pages copies the file to docs/.
2. Document the anchor-name discipline in `methodology/drafting_protocol.md`: figure anchors MUST use only letters, numbers, and hyphens — never colons, percent signs, spaces, or other characters that pandoc URL-encodes.
3. Consider a pre-pandoc lint step on `drafts/report.md` that scans for `{#X:Y}` patterns and warns the drafter.

verify-publication: 19 passed, 0 failed; Stage-A carry-over PASS.

## [1.2.0] — 2026-05-19

### Added — Definitional paragraph (§1.2) + societal-stakes paragraph (Conclusion)

Lead-author feedback after v1.1.2: the report uses *"ethical, valid, reproducible, and transparent"* as the operational test for responsible AI use at lines 51, 434, and elsewhere, but never explicitly **defines** the four-way standard or **justifies** why these four properties (vs others) constitute responsibility. The connection to "the goals of research and research training" was implicit. The connection to society was absent. v1.2.0 closes both gaps.

Two paragraphs added — synthesised from parallel codex GPT-5.5 xhigh and Gemini 3 Flash Preview drafts of the same brief:

1. **§1.2 closing paragraph (new):** the explicit definition of "responsible" the report uses. Names the four properties, justifies them ("the conditions under which AI-augmented research remains research"), and defines each one in a short clause: *Ethical* (does not harm research participants, communities, or third parties whose data is processed); *Valid* (inferences meet the same methodological and evidentiary standards as human-produced inferences); *Reproducible* (another researcher with the same inputs, prompts, parameters, and tool version can reproduce the output); *Transparent* (AI's role is disclosed with enough specificity for supervisors, examiners, reviewers, and readers to assess it). Ends with the necessary-together claim: *"no three substitute for the fourth."*

2. **Conclusion middle paragraph (new):** the societal-stakes paragraph. Explicitly connects the four-way standard to the broader public interest in knowledge that the public can trust. Frames universities as *"epistemic infrastructure: institutions that organise knowledge production, discipline claims, and sustain trust in evidence."* Names the failure modes (fabricated citations, unreproducible findings, biased analyses, methods that cannot be assessed). Closes with *"Responsible AI in research is an obligation universities owe society, because the social licence of research depends on knowledge that remains ethical, valid, reproducible, and transparent."*

Conclusion now reads in three paragraphs: lag-story → why-it-matters-beyond-the-institution → universities-not-passive-consumers + framework-as-response. Classic problem → stakes → solution structure.

No substantive content changed in the empirical body, the framework, the chart, or any source citation. The definitional and societal-stakes additions sharpen the report's argumentative spine without disturbing the evidence base.

### Production discipline

Both paragraphs drafted by parallel agents (codex GPT-5.5 xhigh + Gemini 3 Flash Preview) against the same scoped brief, then synthesised by the orchestrator. The brief specified the audience (senior university research leadership), the voice (position-paper, declarative, restrained), the word counts (80–130 per paragraph), and the placement. Each agent's draft preserved verbatim in `private/reviews/definitional_paragraphs_{codex,gemini}.md` for audit.

verify-publication: 19 passed, 0 failed; Stage-A carry-over PASS.

## [1.1.2] — 2026-05-19

### Changed — Cover-abstract closing sentence: plant "agentic generative AI" + preview the deliverable

Lead-author feedback after the v1.1.1 ship: the cover-page abstract closes on the lag story ("the universities that actually train researchers are lagging far behind what is needed to prepare them to use it responsibly") but the reader doesn't yet know what the report *delivers* until they turn the page. A reader who skims only the cover never encounters the term "agentic" (which first appears in "The finding" paragraph 3, line 51 as part of the SPSS-reframe).

One-sentence addition to the cover-page abstract (`drafts/report.md:13`) and to the README headline paragraph:

> *This report describes the significant opportunities and problems that agentic generative AI creates for research, setting out a competency framework for research training in the 21st century.*

Five things this sentence does:

1. **Plants "agentic generative AI" at the cover** — one noun phrase, no typographic gymnastics. When the reader hits the SPSS-reframe ("LLMs are agentic research tools") on the next page, the term is already familiar.
2. **Previews the deliverable** — *"setting out a competency framework"* — so the reader knows what the report produces, not just what it diagnoses.
3. **Echoes the subtitle** — *"competency framework for research training"* nearly verbatim mirrors the subtitle ("A Competency Framework for Research Training"). Cover-design cohesion.
4. **Frames opportunities AND problems** — disarms the "anti-AI report" misread.
5. **Anchors the temporal stakes** — *"in the 21st century"* makes the historical inflection visible.

No substantive content changed. Same title, framing, body, evidence base, DOI, and chart as v1.1.1. The cover abstract gains one sentence; the README headline paragraph gains the same sentence; VERSION + CITATION.cff + colophon citation bump 1.1.1 → 1.1.2.

## [1.1.1] — 2026-05-19

### Changed — Trim front-matter colophon; move scope and methodology notes into Appendix D

Lead-author feedback after the v1.1.0 push: the front-matter colophon was running three substantial paragraphs (citation + license + scope-and-method + appendix pointers), and Appendix D's AI-assistance disclosure was longer than it needed to be. Readers should hit the executive summary quickly; the document-production notes belong in an appendix, not in front of the exec summary.

Two changes:

1. **Trim the cover-page colophon to citation + license only.** Drop the "Scope and method" paragraph (which talked about the planned regional series, the four primary dossiers, and the snapshot date) and drop the appendix-pointer paragraph (which was redundant with the TOC). The Instats involvement is implicit in the "Instats Policy Series" citation line; no need for a separate Instats paragraph.
2. **Move the scope content into Appendix D and shorten the AI-assistance disclosure.** Appendix D now opens with Author + Contact, then Scope (the moved content), then Methodology (slightly tightened), then a shorter AI assistance disclosure, then the Conflict-of-interest disclosure. Drop the redundant License line at the end of Appendix D (already covered in the colophon).

No substantive content removed — just relocated and shortened. The factual claims about the four dossiers, the snapshot date, the AI assistance scope, and the conflict-of-interest position are all preserved in Appendix D. The cover page now reads citation + license + author byline + scan to the executive summary, which is the right shape for the first impression of a policy publication.

This is a structural rule that will apply to all future Instats Policy Series publications; the general-repo template (forthcoming v0.22.20) will codify it.

## [1.1.0] — 2026-05-19

### Changed — Comprehensive framing redraft on the same evidence base

The v1.0.0 cover-page abstract, executive summary, body, and conclusion were structured around a "regulatory cascade" / "publishing tip" / "funding head" / "institutional layer" metaphor cluster, and around an opening "three claims that get distorted" device adapted from a debate-driven policy publication. After the v1.0.0 release the lead author identified two structural problems with that framing:

1. **The plagiarism framing is a category error.** Reducing LLMs to a plagiarism-policy question is the same mistake as treating SPSS output as plagiarism. LLMs are agentic research tools — task-directed systems that produce usable outputs incorporated into the research record, in the same family as statistical packages, transcription engines, code-generation assistants, and data-cleaning pipelines. The right question of any research tool is whether the use is ethical, valid, reproducible, and transparent — not who wrote the output.

2. **AI in research training is not yet an adversarial public debate.** The three-claims-with-verdicts opening device works for topics with identifiable parties making identifiable circulating claims (gas tax, fiscal policy, etc.) but reads as theatre for a topic where the sector is *drifting* rather than *arguing*. The v1.0.0 three "claims" were either tautologies the report immediately reframed or soft straw men the report set up to knock down.

v1.1.0 is a comprehensive framing redraft that preserves the entire empirical evidence base (thirty-eight top-tier doctoral universities in fifteen countries and jurisdictions; fourteen national research funders plus the European Research Council; eighteen publishers plus three preprint servers; thirteen competency-framework dossiers; eleven AI tool classes) while rebuilding the cover, executive summary, and body around two new structural moves:

- **The SPSS-analogy reframe of LLMs as agentic research tools** — explicit in the new "The finding" section, glossary preamble, and Conclusion. The plagiarism framing is named as a category error driven by surface mimicry.
- **The new-frameworks position** — universities require purpose-built, adaptive frameworks that address AI as an agentic research tool, NOT extensions to plagiarism policies and NOT bolt-ons to researcher-development frameworks designed for a pre-2022 world. The Vitae 2025 refresh is the worked exemplar of a framework refresh that still missed AI.

### Specific changes

- **Title and subtitle.** *"Responsible AI in Research and Research Training: A Global Competency Framework for University Research Leadership"* → *"Responsible AI in Academic Research: A Competency Framework for Research Training."* Title-broad, subtitle-specific-lever; "Global" and "University Research Leadership" carried in body rather than crowding the cover.
- **Cover-page abstract** (drafts/report.md:13) — fully rewritten by the lead author. Drops the canonical defect sentence ("the regulatory cascade has hardened at the publishing tip and the funding head"). Opens with the audience question, lands the only-six-of-thirty-eight headline early, contrasts publishers vs. universities, lands the Vitae 2025 punctuation, closes with the lag thesis.
- **"The finding" executive summary** (drafts/report.md:45-61) — rewritten as six paragraphs + three bullets. New paragraph 3 introduces the agentic-research-tools reframe with the SPSS analogy. The three "points the debate consistently gets wrong" bullets from v1.0.0 are preserved as the unpacking of the category-error claim. New paragraph 5 articulates the new-frameworks position. Removed: the three-claims-with-verdicts block, which was dropped entirely.
- **Figure 1** (new) — anchor regulatory-response-timeline chart added at the report's opening, visualising the lag with three lanes (publishers / national research funders / universities) on a months-from-ChatGPT-3.5 X-axis. Six accent-red dots mark the Class D universities. Caption lands the headline finding for skimmers.
- **§1.3** (drafts/report.md:150-161) — heading renamed from "The plagiarism-policy ceiling" to "The institutional baseline in 2026"; opener reframed around competency-scope axis; Class A/B/C labels smoothed to drop "Beyond plagiarism" lead-ins. "Plagiarism-policy ceiling" preserved as the empirical term for what institutions have built (the term still names a real institutional finding).
- **§2.2** (drafts/report.md:185-191) — three-actor convergence comparison reframed from "three different layers" to "three actor groups" with direct-actor framing (publishers / national research funders / competency-framework literature).
- **Part 3 sub-section closes** (lines 256, 264, 268, 274, 288, 304, 318) — cascade-stratum metaphors removed; "the institutional layer" / "the funder layer" / "the publisher layer" replaced with direct-actor framing. Cover-handoff binary swapped from "AI literacy and examiner discipline" → "AI literacy and valid research practices" at characterising positions. "Examiner discipline" preserved as the specific Class D taxonomic feature (line 157) and at four other feature-level positions where it names the institutional viva-voce examination practice.
- **Part 5 recommendations** (lines 380, 392, 410, 424) — "the institutional layer has not yet achieved convergence" → "universities have not yet achieved convergence"; "extends past plagiarism" → "anchored in research-integrity adjudication"; "the institutional layer is the layer the framework's evidence shows is least developed" → "universities are the actor the framework's evidence shows is least developed."
- **Conclusion** (lines 428-432) — fully rewritten as two paragraphs. Lands the agentic-tools reframe + new-frameworks position + the goal of excellent research achieved through excellent research training.
- **Appendix B closing sentence** (line 478) — canonical defect sentence replaced with direct-actor framing.
- **Appendix C glossary preamble** (line 482) — new preamble paragraph added before the eleven AI tool classes, defining *agentic research tools* and naming the plagiarism-policy framing as a category error.
- **Appendix C Class 11 close** (AI-detection tools) — reframed from "the plagiarism-policy ceiling" reference to "the category error this report's framework displaces."
- **README.md** — title and headline paragraph updated to match the new framing.
- **CITATION.cff, project.yml** — title and version metadata updated.

### Preserved (unchanged in substance)

- The empirical evidence base: thirty-eight top-tier doctoral universities in fifteen countries; fourteen national research funders plus ERC; eighteen publishers plus three preprint servers; thirteen competency-framework dossiers; eleven AI tool classes.
- The five-dimension competency framework and four-level maturity grid.
- The labour-vs-judgement task taxonomy (Appendix G).
- The audience-tier recommendation structure (Part 5: five tiers).
- All source citations and DOI (10.61700/t31oy23grr).

### Production discipline

The redraft used the same five-stage adversarial review pipeline as v1.0.0 with two additional discipline upgrades:

1. **A focused Stage E voice-pair (Gemini 3 Flash Preview + GPT-5.5 xhigh) on the rewritten cover + finding** immediately after the framing rewrite, BEFORE extending to the body. Caught six small register/structure issues (semicolon+em-dash stack; wooden "position of this report"; residual "lagging end" metaphor; framework-Framework stutter; passive-voice publisher clause) that would have propagated into the body sweep if not caught early.
2. **A parallel Phase 1 triage (Opus 4.7 + GPT-5.5 xhigh)** of the whole manuscript to identify every site where the body's framing was out of step with the rewritten cover. Two independent reads converged on a list of ~14 P0 sites + ~10 P1 sites; both reviewers' different training caught different defect classes (Opus surfaced the examiner-discipline→valid-research-practices terminology handoff that codex missed; codex surfaced the §1.3 plagiarism-spine reframe that Opus underplayed).
3. **Five sequential codex implementation passes** (A → E) with orchestrator verification between each. Each pass had a tight scoped brief (≤6 sites, explicit preserve/touch acceptance criteria). Race conditions avoided by serial dispatch; all five passes landed cleanly.
4. **A full-manuscript Stage E voice-pair** on the completed redraft. Surfaced four small line edits (figure caption ceiling-phrase; finding-section closing overpacked; Tier 5 "advocacy frame" register; §3.4 "literature's blind spot" abstract-heavy) plus one Gemini-only finding (Part 2 opener "decoration" → "lacks a substantive foundation"). All five applied.

The voice-tic and decorative-metaphor scanner (`scripts/check_voice_tics.py` from general-repo v0.22.19) reports zero multi-compound flags in the rewritten manuscript except line 442 ("row axis / column axis") — a literal description of the maturity-grid table's rows and columns, confirmed acceptable.

## [1.0.0] — 2026-05-18

### Added

- Initial public release of the Instats Policy Series publication *Responsible AI in Research and Research Training: A Global Competency Framework for University Research Leadership.* Five-dimension competency framework with four-level maturity grid; thirty-eight-university institutional dossier; fourteen-funder national-research-funder dossier; eighteen-publisher publisher dossier; thirteen-framework competency-framework dossier. DOI 10.61700/t31oy23grr.
