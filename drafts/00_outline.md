# Report outline — v0.1.0

**Status:** WORKING DRAFT — Mike to review before Tier 1 dossiers land. Locks the report's spine. Subsequent revisions land here, not in a sibling file.
**Working title:** Responsible AI in Research and Research Training
**Working subtitle:** A Global Competency Framework for University Research Leadership
**Report ID:** INSTATS-PS-2026-04
**Date target:** First public release window opens after Tier 1 + Tier 2 dossiers and full Stage A/B/C/D/E review. Plan for a working pace, not a deadline; gas-tax shipped at v3.2.5 and that pace is the model.

---

## Step 0 — Why / Purpose / Audience / How

Per `general-repo/methodology/drafting_protocol.md` § Step 0 (v0.22.5+ discipline). These answers anchor every drafting and review decision. They appear here, and the same answers appear in the executive summary's "This report is written for…" paragraph after the headline finding (the gas-tax v3.2.4 §The finding paragraph is the worked exemplar).

### Why does this report exist?

University research leadership is being asked, often by their own councils and boards, what their institution's posture on AI in research is. Most institutional answers in 2026 are derivatives of plagiarism policy with an AI clause appended. That answer is not adequate for the strategic moment: it gets the threat model wrong, it gets the opportunity model wrong, and it does not tell faculty deans, graduate-school deans, or higher-degrees committees what to do on Monday morning. This report supplies a global competency framework that does.

### What is the report's purpose?

To give senior university research leadership a shared, evidence-anchored vocabulary for benchmarking institutional readiness on responsible AI use in research and research training, and a maturity grid that translates that vocabulary into concrete decisions on policy, curriculum, infrastructure, and governance. The framework is the deliverable; the international evidence is what makes the framework defensible.

### Who is the audience?

Five tiers, in order of how often each tier touches the framework's decisions in practice:

- Tier 1 — Executive research leadership. DVC-Rs, Deputy Provosts (Research), Deputy Vice Presidents (Research), Pro-Vice-Chancellors (Research).
- Tier 2 — Faculty research leadership. Faculty Deans, Associate Deans of Research.
- Tier 3 — Graduate-school leadership. Deans of Graduate Schools, Associate Deans of Research Training, Directors of Doctoral Training.
- Tier 4 — Governance committees. Higher-degrees committees, research-integrity committees, research-ethics committees.
- Tier 5 — Peak bodies for graduate students. National graduate-student associations, councils of graduate schools, postdoc associations.

Secondary readers: research-administration directors, IT-procurement leads with research-systems remit, AI-policy advisors at universities, sector commentators, national funders.

### How is the report written so it serves the audience?

- Forensic, source-anchored, plain English. Same register as gas-tax. Every claim with a numerator and denominator carries a primary-source URL and a snapshot date.
- No Instats product mentions in the body. Single AI-use line in the colophon, same wording as gas-tax. Test bar for every paragraph: would it survive being read aloud at a peer university's senate-research committee.
- The competency framework is the spine. Topics 1-4 (Mike's locked scope, see scoping brief §3) supply the dimensions; international evidence populates the dimensions. The framework is reusable so the planned regional adaptations (US/Americas, UK/Europe, APAC ex Japan) can re-populate it without restructuring it.
- Formatting discipline per v0.22.9+: bolding ≤5%, em-dashes ≤2/1000, italics ≤5/1000, bullet ratio ≤30%, words/heading ≥150. Anti-LLM-tic patterns banned at Stage E.

---

## Content exemplar note

Before locking this outline, read:

- `docs/content_exemplars.md`
- `policy_docs/content_exemplar_cards/index.yml`
- `policy_docs/content_exemplar_cards/patterns.md`

Select two or three structurally relevant examples; read only their cards; record what each is good for, what each is not good for, which structural moves this report adopts, and which moves it rejects because they do not fit Instats's evidence standard, audience, licence, or public/private boundary.

Use exemplars as models for form, not authority for facts. Do not copy external prose, section names, visual metaphors, charts, house style, campaign language, or topic-specific rhetorical posture.

**Anticipated structural moves (provisional, finalise after card review):**

- The competency-framework spine pattern (UNESCO AI Competency Framework structure adapted to research-training).
- The international-comparator table pattern (gas-tax Norway / Qatar / US comparator → here: funder positions across UKRI / NSF / ARC / DFG / ERC / NORDIS / A*STAR).
- The maturity grid (rows = framework dimensions; columns = "absent / nascent / established / leading").
- The audience-tiered recommendations chapter (one short chapter per audience tier; concrete asks per tier).

---

## Front matter (per gas-tax pattern, v0.22.6+ ordering)

1. Cover
2. Colophon (date, version, report ID, author, ORCID, licence, AI-use disclosure, COI disclosure)
3. Executive summary (1 page)
4. TOC
5. Body

The exec-summary-before-TOC order is locked in `methodology/publication_workflow.md` (v0.22.6+).

---

## Executive summary (1 page)

A working sketch; refine after Tier 1 dossiers land. The summary's headline finding is the cover-table comparator (provisional candidates in scoping brief §6); the three "things sector leaders get wrong" are the gap claims that motivate Parts 1 and 2.

- **Headline finding (provisional).** A defensible comparator of the form "X% of top-100 doctoral programmes have a research-methods unit on statistics; Y% have one on responsible AI use in research", or "Z% of top-100 universities publish AI policies that extend past plagiarism into research integrity and reproducibility". The choice is data-driven, locked after dossier work.
- **Three things sector leaders get wrong about this debate** (working list, refine).
    1. AI in research is treated as a student-conduct problem (plagiarism) when the binding constraint is a research-integrity problem (validity, reproducibility, adversarial validation).
    2. AI literacy is treated as a tooling-skills problem (which buttons to push) when the binding constraint is a judgement problem (which tasks AI is good at, which ones it ruins, and how to tell the difference).
    3. AI-in-research policy is treated as a single document when the binding constraint is a five-dimension competency grid that crosses policy, people, systems, and process.
- **What changes if you adopt the framework.** The grid is the change. Section 4 makes the grid operational.
- **Audience paragraph.** "This report is written for…" — Tier 1-5 named, two sentences on the planned regional adaptations.

---

## Part 1 — The factual baseline: where research training stands on AI today

The "where the gap is" section. Pulls Candidate A (competency inventory + gap analysis) into the report. Feeds Topic 5's "does policy go beyond plagiarism?" question and Topic 1's "human-in-the-loop" claim by establishing the present condition.

### 1.1 The shift in research practice 2022 → 2026

Quantified where possible: PhD-student AI-use surveys (Nature 2023/2024 surveys; AAU+APLU work; specific journal special issues). What changed in the underlying research practice while university policies were being drafted around plagiarism.

### 1.2 What "responsible AI use" lacks a clear definition for

The vacuum that Topic 2 (define + embed responsible use in practice) is going to fill. Inventory what national funders, journals, and universities currently say "responsible AI use" means, and where they do not converge.

### 1.3 The plagiarism-policy ceiling

The "does the AI policy go beyond plagiarism?" question (Topic 5). Inventory: of the top-100 doctoral universities whose AI policies are publicly accessible, how many extend past plagiarism into (a) research integrity, (b) reproducibility, (c) AI literacy, (d) data governance, (e) co-authorship discipline. Likely the source of the headline comparator.

---

## Part 2 — A competency framework

The spine. Five dimensions, each derived from one of Mike's locked topics. Each dimension carries (a) a one-sentence definition, (b) what observable institutional behaviours mark "absent / nascent / established / leading" on the dimension, (c) the international evidence that anchors the level claims.

### 2.1 Dimension 1 — Human-in-the-loop discipline (Topic 1)

AI tools are useful but human experts remain epistemically central. Failure mode: outsourcing the judgement step that defines research, not just the labour step. Worked through with concrete research-task examples (literature synthesis, statistical reasoning, methodological design, peer review).

### 2.2 Dimension 2 — Responsible use in practice (Topic 2)

What "responsible AI use" looks like in PhD-level research and research training, operationalised. Distinguishes the four use-modes (search; co-author; validator; tutor) and what counts as responsible behaviour in each. The dimension where the report differs sharpest from "use AI ethically, do not plagiarise" filler.

### 2.3 Dimension 3 — Tooling that promotes responsible use (Topic 3)

AI tools that promote responsible use, by design: privacy-preserving, do not encourage plagiarism, validating models that do not hallucinate, replicability and accuracy by construction. The taxonomy is the content here. The body argues from observable tool properties, not from any vendor.

### 2.4 Dimension 4 — AI-literate humans (Topic 4)

Human experts central plus AI augmentation equals AI-literate humans needed. The competency list (validity reasoning, co-authorship discipline, AI-model use, adversarial review with advanced AI, reproducibility, ethics) becomes the curriculum spine for research-training programmes.

### 2.5 Dimension 5 — Institutional benchmarking grid (Topic 5)

The competency framework for benchmarking, at "whole of education system" level and at organisational level. Crosses the four preceding dimensions with four operational axes: policy (does the AI policy exist, and does it go beyond plagiarism?); people (who is responsible at each level?); systems (which platforms, with what governance?); process (what is the actual workflow for a PhD student or supervisor?).

---

## Part 3 — International comparison

Populates the framework with worked examples. Mirrors gas-tax's Norway / Qatar / US comparator structure adapted to the research-training landscape.

### 3.1 National research-funder positions

The funder spine. UKRI, NSF, ARC, NHMRC, DFG, ERC, NORDIS, A*STAR, JSPS/AIST, SSHRC/CIHR/NSERC, NWO, SNSF, JST. For each: AI-use disclosure on grant applications; AI-use disclosure on outputs; expectations on AI literacy in funded research-training environments; explicit responsible-use guidance. Cross-references Dimension 5's policy axis.

### 3.2 Top-tier university institutional policies

The institutional spine. Russell Group, Go8, Ivy+, Canadian U15, German U15, RU11 (Japan), European research-intensive sample (KTH, ETH Zürich, EPFL, KU Leuven, Karolinska, NTNU, Helsinki, Aarhus). Four-class taxonomy from §1.3: generic-with-AI-clause; AI-specific-plagiarism-only; AI-specific-extended-to-integrity; AI-specific-extended-to-literacy.

### 3.3 Publisher / journal AI co-authorship and use policies

The publisher spine. Nature family, Science, Elsevier, Wiley, Springer Nature, Taylor & Francis, Lancet, BMJ, JAMA, NEJM, ACM, IEEE. Trajectory 2023 → 2026. Cross-references Dimension 2's responsible-use-in-practice operationalisation.

### 3.4 Existing AI-literacy and researcher-development frameworks

The framework precursors. UNESCO AI Competency Framework, OECD AI Literacy, JISC, EDUCAUSE, Vitae UK Researcher Development Framework, Council of Graduate Schools (US), European University Association, US National Academies. What each gets right, what each leaves to institutional choice, where the Instats framework adds value over the union of the existing ones.

---

## Part 4 — The maturity grid: applying the framework

The framework operationalised. Five dimensions cross four maturity levels: absent / nascent / established / leading.

### 4.1 The five-by-three grid (5 dimensions × 4 levels)

The grid itself, presented as a single full-page table. Each cell is one short paragraph describing what "this dimension at this level" looks like in observable institutional practice (policy document language, curriculum content, infrastructure choice, governance flow). The cell content is anchored in Part 3's international evidence.

### 4.2 What "ready" looks like by dimension

For each dimension, a one-page worked description of the "established" → "leading" gap. This is the readable, non-table version of the grid; the table is the reference, this section is what makes the grid memorable.

### 4.3 Worked institutional examples

Three to five institutional examples drawn from Part 3, mapped onto the grid. Examples are real institutions where the public evidence is good (institutional AI policies plus funder context plus public curriculum documents); references in Appendix B.

---

## Part 5 — Recommendations for university research leadership

One short chapter per audience tier from §Step 0 / scoping brief §2. Each chapter answers: what does this tier do on Monday morning if they adopt the framework? Each recommendation is a single concrete action, with the framework dimension it targets and the maturity-level move it represents.

### 5.1 For DVC-R / executive research leadership (Tier 1)
### 5.2 For faculty deans and associate deans of research (Tier 2)
### 5.3 For deans of graduate schools and A/Deans of research training (Tier 3)
### 5.4 For higher-degrees committees and research-integrity committees (Tier 4)
### 5.5 For peak bodies for graduate students (Tier 5)

---

## Appendices

- **A. The maturity grid: full version.** Five dimensions by four levels in a single full-page table, with citation footnotes.
- **B. Country dossiers (long-form).** Six to eight countries; one page each. Drawn from the Tier 1 national-research-funder dossier.
- **C. Glossary of AI tool classes.** LLM-as-search / co-author / validator / tutor / coder, plus RAG-anchored research assistants, retrieval pipelines, automated literature-synthesis tools. Functional taxonomy, no vendor names in the public body.
- **D. Methodology + AI-use disclosure.** What was drafted with which AI agent. The disclosure is the AI-in-research-about-AI-in-research disclosure paradox handled head-on. Same template as gas-tax's colophon, expanded to identify which sections used which agent class.
- **E. Sources (long-form, alphabetised).** Every primary URL with a snapshot date.
- **F. Regional-adaptation note (lightweight).** How a sister report (US/Americas, UK/Europe, APAC ex Japan) re-populates the framework without restructuring it. Two pages, designed to be useful to a future agent doing the next report.

---

## Cross-reference: topic → chapter

The five locked topics (scoping brief §3) map onto the body as follows.

| Topic | Locked text | Primary chapter | Secondary chapters |
|---|---|---|---|
| Topic 1 | AI tools are useful but human experts must remain in the loop | §2.1 (Dimension 1) | §1.1, §5.* |
| Topic 2 | Define and embed responsible, effective, accurate AI tools and methods in research and research training | §2.2 (Dimension 2) | §1.2, §3.3, §5.* |
| Topic 3 | AI tools that promote responsible use (privacy, no plagiarism encouragement, validating models, replicability/accuracy) | §2.3 (Dimension 3) | §3.4, Appendix C |
| Topic 4 | AI-literate humans needed; training on validity, co-authorship, AI model use, adversarial review | §2.4 (Dimension 4) | §3.4, §5.3 |
| Topic 5 | Competency framework for benchmarking at system and organisational level | §2.5 (Dimension 5), Part 4 | §1.3, §3.1, §3.2, Appendix A |

---

## Cross-reference: dossier → chapter

The four Tier 1 dossiers (scoping brief §4) feed the report as follows.

| Dossier | Primary chapter | Secondary chapters |
|---|---|---|
| National research-funder AI policies | §3.1 | §1.2, §2.5, Appendix B, Appendix E |
| Top-tier university institutional AI policies | §3.2 | §1.3, §2.5, §4.3, Appendix B, Appendix E |
| Existing AI-literacy / competency frameworks | §3.4 | §2.* (all dimensions reference these as priors), Appendix E |
| Publisher / journal AI policies | §3.3 | §2.2, §2.4, Appendix C, Appendix E |

The four Tier 2 dossiers (AI tool taxonomy; privacy/IP/governance; reproducibility intersection; adversarial-review patterns) feed §2.3 / Appendix C, §2.5, §1.1 + §2.4, and §2.4 respectively.

---

## Review state (updates with each round)

| Stage | Status | Artefact | Notes |
|---|---|---|---|
| Outline lock | DRAFT (2026-05-18) | this file | Mike review pending |
| Tier 1 dossiers | PENDING | `research/dossier_*.md` (4 files) | spawned at outline lock |
| Tier 2 dossiers | NOT STARTED | `research/dossier_*.md` (4 files) | queue after Tier 1 |
| Drafting v0.1.0 → v0.5.0 | NOT STARTED | `drafts/report.md` | starts when Tier 1 lands |
| Stage A — Opus + codex | NOT STARTED | `final/review_opus.md`, `final/review_codex.md` | adversarial pair |
| Stage A carry-over | NOT STARTED | `final/p0_p1_carryover.md` | Mike-approved disposition |
| Stage C — Gemini × 3 | NOT STARTED | `final/reviews/23..25_*.md` | sentence/paragraph/section |
| Stage D — GPT-5.5 synthesis | NOT STARTED | `final/reviews/26_*.md` | ACCEPT/PARTIAL/REJECT/STALE |
| Stage B — persona panel | NOT STARTED | `final/reviews/persona_*.md` | 12-20 personas, mapped to Tier 1-5 |
| Stage E — voice review | NOT STARTED | `final/reviews/11_voice_*.md` | Gemini + GPT-5.5 pair, propagation sweep |
| Publish-release | NOT STARTED | `final/report.html/docx/pdf`, DOI minted | `make publish-release` |
