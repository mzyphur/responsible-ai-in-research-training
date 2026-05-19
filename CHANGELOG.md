# Changelog

All notable changes to *Responsible AI in Academic Research: A Capability Framework for Research Training* are recorded in this file. The publication uses [Semantic Versioning](https://semver.org/).

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [1.1.0] — 2026-05-19

### Changed — Comprehensive framing redraft on the same evidence base

The v1.0.0 cover-page abstract, executive summary, body, and conclusion were structured around a "regulatory cascade" / "publishing tip" / "funding head" / "institutional layer" metaphor cluster, and around an opening "three claims that get distorted" device adapted from a debate-driven policy publication. After the v1.0.0 release the lead author identified two structural problems with that framing:

1. **The plagiarism framing is a category error.** Reducing LLMs to a plagiarism-policy question is the same mistake as treating SPSS output as plagiarism. LLMs are agentic research tools — task-directed systems that produce usable outputs incorporated into the research record, in the same family as statistical packages, transcription engines, code-generation assistants, and data-cleaning pipelines. The right question of any research tool is whether the use is ethical, valid, reproducible, and transparent — not who wrote the output.

2. **AI in research training is not yet an adversarial public debate.** The three-claims-with-verdicts opening device works for topics with identifiable parties making identifiable circulating claims (gas tax, fiscal policy, etc.) but reads as theatre for a topic where the sector is *drifting* rather than *arguing*. The v1.0.0 three "claims" were either tautologies the report immediately reframed or soft straw men the report set up to knock down.

v1.1.0 is a comprehensive framing redraft that preserves the entire empirical evidence base (thirty-eight top-tier doctoral universities in fifteen countries and jurisdictions; fourteen national research funders plus the European Research Council; eighteen publishers plus three preprint servers; thirteen capability-framework dossiers; eleven AI tool classes) while rebuilding the cover, executive summary, and body around two new structural moves:

- **The SPSS-analogy reframe of LLMs as agentic research tools** — explicit in the new "The finding" section, glossary preamble, and Conclusion. The plagiarism framing is named as a category error driven by surface mimicry.
- **The new-frameworks position** — universities require purpose-built, adaptive frameworks that address AI as an agentic research tool, NOT extensions to plagiarism policies and NOT bolt-ons to researcher-development frameworks designed for a pre-2022 world. The Vitae 2025 refresh is the worked exemplar of a framework refresh that still missed AI.

### Specific changes

- **Title and subtitle.** *"Responsible AI in Research and Research Training: A Global Capability Framework for University Research Leadership"* → *"Responsible AI in Academic Research: A Capability Framework for Research Training."* Title-broad, subtitle-specific-lever; "Global" and "University Research Leadership" carried in body rather than crowding the cover.
- **Cover-page abstract** (drafts/report.md:13) — fully rewritten by the lead author. Drops the canonical defect sentence ("the regulatory cascade has hardened at the publishing tip and the funding head"). Opens with the audience question, lands the only-six-of-thirty-eight headline early, contrasts publishers vs. universities, lands the Vitae 2025 punctuation, closes with the lag thesis.
- **"The finding" executive summary** (drafts/report.md:45-61) — rewritten as six paragraphs + three bullets. New paragraph 3 introduces the agentic-research-tools reframe with the SPSS analogy. The three "points the debate consistently gets wrong" bullets from v1.0.0 are preserved as the unpacking of the category-error claim. New paragraph 5 articulates the new-frameworks position. Removed: the three-claims-with-verdicts block, which was dropped entirely.
- **Figure 1** (new) — anchor regulatory-response-timeline chart added at the report's opening, visualising the lag with three lanes (publishers / national research funders / universities) on a months-from-ChatGPT-3.5 X-axis. Six accent-red dots mark the Class D universities. Caption lands the headline finding for skimmers.
- **§1.3** (drafts/report.md:150-161) — heading renamed from "The plagiarism-policy ceiling" to "The institutional baseline in 2026"; opener reframed around capability-scope axis; Class A/B/C labels smoothed to drop "Beyond plagiarism" lead-ins. "Plagiarism-policy ceiling" preserved as the empirical term for what institutions have built (the term still names a real institutional finding).
- **§2.2** (drafts/report.md:185-191) — three-actor convergence comparison reframed from "three different layers" to "three actor groups" with direct-actor framing (publishers / national research funders / capability-framework literature).
- **Part 3 sub-section closes** (lines 256, 264, 268, 274, 288, 304, 318) — cascade-stratum metaphors removed; "the institutional layer" / "the funder layer" / "the publisher layer" replaced with direct-actor framing. Cover-handoff binary swapped from "AI literacy and examiner discipline" → "AI literacy and valid research practices" at characterising positions. "Examiner discipline" preserved as the specific Class D taxonomic feature (line 157) and at four other feature-level positions where it names the institutional viva-voce examination practice.
- **Part 5 recommendations** (lines 380, 392, 410, 424) — "the institutional layer has not yet achieved convergence" → "universities have not yet achieved convergence"; "extends past plagiarism" → "anchored in research-integrity adjudication"; "the institutional layer is the layer the framework's evidence shows is least developed" → "universities are the actor the framework's evidence shows is least developed."
- **Conclusion** (lines 428-432) — fully rewritten as two paragraphs. Lands the agentic-tools reframe + new-frameworks position + the goal of excellent research achieved through excellent research training.
- **Appendix B closing sentence** (line 478) — canonical defect sentence replaced with direct-actor framing.
- **Appendix C glossary preamble** (line 482) — new preamble paragraph added before the eleven AI tool classes, defining *agentic research tools* and naming the plagiarism-policy framing as a category error.
- **Appendix C Class 11 close** (AI-detection tools) — reframed from "the plagiarism-policy ceiling" reference to "the category error this report's framework displaces."
- **README.md** — title and headline paragraph updated to match the new framing.
- **CITATION.cff, project.yml** — title and version metadata updated.

### Preserved (unchanged in substance)

- The empirical evidence base: thirty-eight top-tier doctoral universities in fifteen countries; fourteen national research funders plus ERC; eighteen publishers plus three preprint servers; thirteen capability-framework dossiers; eleven AI tool classes.
- The five-dimension capability framework and four-level maturity grid.
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

- Initial public release of the Instats Policy Series publication *Responsible AI in Research and Research Training: A Global Capability Framework for University Research Leadership.* Five-dimension capability framework with four-level maturity grid; thirty-eight-university institutional dossier; fourteen-funder national-research-funder dossier; eighteen-publisher publisher dossier; thirteen-framework capability-framework dossier. DOI 10.61700/t31oy23grr.
