---
review_opus_sha256: 6156c342b8a9d9c0ec885ba3ed330df3a1e77ad9f281859fa29c957ebe78942c
review_codex_sha256: 982893d4d3f9fcacf803c5e50a086d9484395b843a75918970d49f884b2093b5
drafts_report_sha256: 6ee79e0b29c721338416afa41301c01cd04a15f0cdfc11773b89f757423b6fa3
release_waiver: []
---

# Stage A carry-over — v1.0.0

**Manuscript:** drafts/report.md @ v1.0.0
**Stage A pair:** Opus 4.7 (`final/review_opus.md`) + codex GPT-5.5 xhigh (`final/review_codex.md`).
**Carryover authored:** 2026-05-18, post-v1.0.0, as part of the general-repo 0.22.15 verify-publication-gates fix. The carryover file was not written in the original v1.0.0 publish flow because pre-0.22.15 `verify-publication` aborted on consistency-gate failures before reaching the carryover gate; the substantive Stage A fixes had already landed in v0.5.1, v0.5.2, and v0.6.0 commits, and v1.0.0 captured the publication-ready state.

## Disposition table

| Finding ID | Description (source · resolution) | Status |
|---|---|---|
| P0-1 | (Opus) Headline denominator: 38 institutional entries in dossier vs "thirty" in body. ALSO (codex) Kyoto makes 38-university sample internally unstable. | CLOSED in v0.5.1 (Opus); CLOSED in v0.5.2 (codex — Kyoto removed from sample) |
| P0-2 | (Opus) Exec summary geographic mis-attribution (Helsinki labelled UK; KU Leuven labelled German). ALSO (codex) "Plagiarism-policy ceiling" headline overstates evidence. | CLOSED in v0.5.1 (Opus); CLOSED in v0.5.2 (codex — line 166 rewritten to bound "one in six" to AI literacy + examiner discipline) |
| P0-3 | (Opus) "Twenty-four of twenty-nine plagiarism-confined" exec-summary arithmetic overstates by 2x. ALSO (codex) Appendix D not release-ready: AI-routing leakage + COI stub. | CLOSED in v0.5.1 (Opus); CLOSED in v0.5.2 (codex — Appendix D rewritten; COI affirmative statement; AI-use disclosure compressed) |
| P0-4 | (Opus) §3.2 sub-region counts diverge from enumerated institutions. | CLOSED in v0.5.1 |
| P0-5 | (Opus) Australian Go8 "uniformly Class C" — UWA is Class B. | CLOSED in v0.5.1 |
| P0-6 | (Opus) "Same calendar quarter of 2025" NIH-vs-Vetenskapsrådet timing claim is impossible. | CLOSED in v0.5.1 |
| P1-1 | (Opus) Publisher count discrepancy in §3.3 (fifteen vs eighteen). ALSO (codex) University dossier footnote stale "thirty-university" counts. | CLOSED in v0.5.1 (Opus); CLOSED in v0.5.2 (codex — footnote ^university_dossier rewritten to A=4, B=11, C=17, D=6 / Total 38) |
| P1-2 | (Opus) Footnote ^cup_hill misattributes source to *The Bookseller*. ALSO (codex) Funder geography count inconsistent and arithmetically unclear. | CLOSED in v0.5.1 (Opus); CLOSED in v0.5.2 (codex — reconciled to 14 funders / 11 countries + EU ERC supranational) |
| P1-3 | (Opus) Footnote ^bmj_disclosure_rate URL inconsistent with dossier. ALSO (codex) Dossier-only footnotes conflict with primary-URL methodology claim. | CLOSED in v0.5.1 (Opus); CLOSED in v0.5.2 (codex — Appendix D methodology language distinguishes primary-URL claims from synthesis-claim citations) |
| P1-4 | (Opus) Footnote ^plos_2025 title and URL diverge from dossier. ALSO (codex) UKRI "only funder" claim conflicts with the Norway caveat. | CLOSED in v0.5.1 (Opus); CLOSED in v0.5.2 (codex — exec summary + §3.1 qualified to "funder-policy and CDT-scale investment"; Norway parallel posture made explicit) |
| P1-5 | (Opus) "Twelve countries" claim vs funder dossier 14-funders/13-countries inconsistent. ALSO (codex) "Unprecedented in publisher-policy history" too strong. | CLOSED in v0.5.1 (Opus); CLOSED in v0.5.2 (codex — softened to "unusually fast compared with the years-long convergence of prior publisher-policy adoptions") |
| P1-6 | (Opus) Class A includes Kyoto but Kyoto has no discrete dossier entry. ALSO (codex) Stale source-dossier headline still says "thirty" universities. | CLOSED in v0.5.2 (both — Kyoto removed from classified sample; dossier_02 opening sentence reconciled to "thirty-eight... reconciled at Stage A") |
| P1-7 | (Opus) Russell Group 2023 principle invoked in §2.4 for AI literacy in research training is teaching-focused. ALSO (codex) Methodology and signoff language presents incomplete review stages as completed. | CLOSED in v0.5.1 (Opus); CLOSED in v0.5.2 (codex — Appendix D rewritten to remove specific-stage completed-tense language) |
| P1-8 | (Opus) EU AI Act Annex III §3 description omits §3(c). ALSO (codex) Appendix C tool-class evidence has numerical claims without direct footnotes. | CLOSED in v0.5.1 (Opus — level-assignment added to admissions/learning-outcome/proctoring formulation); DEFERRED for codex Appendix C row-level footnotes — figures inherit citation through body's other footnote citations |
| P1-9 | (Opus) "First publisher-level disclosure instrument of its kind" phrasing for BMJ. | CLOSED in v0.5.1 |
| P1-10 | (Opus) Class B membership understated in §1.3 body claim. | CLOSED in v0.5.1 (per-class arithmetic recalibrated; Class B = 11 of 38) |
| P1-11 | (Opus) §1.1 publisher cascade dates: ACM "April 2023" attribution framing. | DEFERRED — minor framing; Stage E candidate; not release-blocking |
| P1-12 | (Opus) Em-dash density above scoping-brief target. | CLOSED in v1.0.0 (Stage E pair both flagged; sweep reduced 79 to 52 em-dashes; prose ratio now well under 2/1000 target) |

## Stage E voice review pair (Gemini + codex) — landed v1.0.0

Voice-sweep findings: 43 edits applied across the manuscript. Em-dash density reduced 79 → 52. The two Stage B Bucket B candidates (Conclusion closing line; §3.2 "US laggard cluster" framing) both flagged independently by Gemini and codex; both softened in v1.0.0.

## Stage B persona panel — landed v0.6.0

| Bucket | Disposition |
|---|---|
| Bucket A (factual / claim / numeric) | §1.3 paragraph 3 Class C vs Class D operational-difference clarifying sentence added (v0.6.0). Citation-completeness deferrals (Singapore Model AI Governance Framework, Concordat, Hochschulrektorenkonferenz, UA AI Statement, OfS, ORI) carried as a known deferral pending regional adaptations. |
| Bucket B (voice / framing) | "US laggard cluster" and Conclusion closing line softened in v1.0.0 via Stage E. |
| Bucket C (operational addition) | Appendix G — Labour-vs-judgement task taxonomy added (v0.6.0). |

---

## v1.1.0 disposition — framing redraft (2026-05-19)

v1.1.0 is a comprehensive framing redraft on the same factual evidence base as v1.0.0. The Stage A findings recorded above remain CLOSED — the redraft did NOT re-open any v1.0.0 P0 / P1 factual finding. Every empirical claim, source citation, dossier count, and per-class arithmetic from v1.0.0 is preserved verbatim in v1.1.0.

**What changed.** The cover-page abstract, executive-summary "The finding" section, body section closings, Conclusion, and Appendix B closing were rewritten to drop the v1.0.0 cascade-stratum metaphor cluster ("regulatory cascade" / "publishing tip" / "funding head" / "institutional layer" / "fourth layer") and the three-claims-with-verdicts opening device, replacing them with a position-paper opening built around two new structural moves: (1) the SPSS-analogy reframe of LLMs as agentic research tools, and (2) the explicit position that universities require purpose-built adaptive frameworks rather than extensions to plagiarism policies or bolt-ons to pre-2022 researcher-development frameworks. Headline-binary terminology shifted from "AI literacy and examiner discipline" to "AI literacy and valid research practices" at five characterising positions while preserving "examiner discipline" at the Class D taxonomic position and four other feature-level mentions.

**Review pipeline for v1.1.0.**

- **Pre-rewrite focused Stage E voice-pair** on the cover + "The finding" rewrite (Gemini 3 Flash Preview + GPT-5.5 xhigh, parallel). Six small register/structure fixes applied before the body sweep was dispatched.
- **Phase 1 parallel framing-coherence triage**: Opus 4.7 sub-agent (inheriting orchestrator context) + GPT-5.5 xhigh (pattern-matched per-section audit). Two independent reads of the whole 683-line manuscript. Convergent + divergent findings synthesised into 5 scoped implementation briefs (Pass A through Pass E).
- **Phase 2 sequential codex implementation passes**: Pass A (Conclusion + Appendix B closing) → Pass B (Part 3 sub-section closes + examiner→valid swap) → Pass C (§1.3 reframe) → Pass D (§2.2 + Part 5 cascade-stratum swaps) → Pass E (smoothing + agentic glossary preamble + appendix cosmetic). Orchestrator verification of every diff against actual file state between passes.
- **Phase 4 anchor chart**: new Figure 1 (`charts/01_regulatory_response_timeline.py`) rendered to PNG + SVG; visualises the lag with three lanes (publishers / national research funders / universities) on a months-from-ChatGPT-3.5 X-axis. Six accent-red dots mark the Class D universities. The per-chart `# red-clusters: 6` directive declares the intentional six-cluster usage to satisfy the publication-audit gate.
- **Phase 5 full-manuscript Stage E voice-pair**: Gemini 3 Flash Preview + GPT-5.5 xhigh, parallel reviews of the completed redraft. Five small line edits applied (figure caption ceiling-phrase swap; finding-section closing split; Tier 5 "advocacy frame" register fix; §3.4 "literature's blind spot" abstract-heavy fix; Part 2 opener "decoration" → "lacks a substantive foundation"). Both reviewers' headline verdict: ship-ready after small tightening.

**Decorative-metaphor scanner outcome.** Pre-redraft: 10 multi-compound flags. Post-redraft: 1 multi-compound flag (line 442 "row axis / column axis" — literal description of the maturity-grid table's axes; known false-positive). The canonical defect sentence (*"the regulatory cascade has hardened at the publishing tip and the funding head"*) is no longer present anywhere in the manuscript.

**Build state at carryover refresh:** drafts/report.md @ v1.1.0; HTML / DOCX / PDF / Pages-package built locally and verified; this carryover file supersedes the mtime of drafts/report.md per the build pipeline's Stage-A carry-over freshness gate.
