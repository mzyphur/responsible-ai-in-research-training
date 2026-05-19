<div align="center">

<a href="https://instats.org">
  <img src="assets/instats_logo.png" alt="Instats" width="240">
</a>

# Responsible AI in Academic Research
## *A Capability Framework for Research Training*

**What does responsible AI use look like for academic research, and how would a university know whether it is doing it well? Of thirty-eight top-tier doctoral universities surveyed across fifteen countries and jurisdictions, only six have AI policies that extend past research integrity into AI literacy and valid research practices. The world's major academic publishers issued a substantively identical no-AI-co-author policy across the sector within ten weeks of ChatGPT-3.5's public release. The United Kingdom's canonical PhD-researcher-development framework, refreshed in 2025, did not treat AI as a competency at all. While publishers and funders have responded to the emergence of AI, the universities that actually train researchers are lagging far behind what is needed to prepare them to use it responsibly. This report describes the significant opportunities and problems that agentic generative AI creates for research, setting out a capability framework for research training in the 21st century.**

<p>
  <a href="https://mzyphur.github.io/responsible-ai-in-research-training/">
    <img alt="Read online" src="https://img.shields.io/badge/Read%20the%20report%20online-00547B?style=for-the-badge&logo=readthedocs&logoColor=white">
  </a>
  <a href="https://github.com/mzyphur/responsible-ai-in-research-training/releases/latest">
    <img alt="Download Microsoft Word" src="https://img.shields.io/badge/Download%20.docx-3092B1?style=for-the-badge&logo=microsoftword&logoColor=white">
  </a>
</p>

<p>
  <img alt="Version" src="https://img.shields.io/github/v/release/mzyphur/responsible-ai-in-research-training?label=version&color=00547B">
  <img alt="License" src="https://img.shields.io/badge/license-CC%20BY--NC%204.0-3092B1">
  <img alt="Evidence" src="https://img.shields.io/badge/evidence-public%20audit%20package-00547B">
  <img alt="Formats" src="https://img.shields.io/badge/formats-DOCX%20%C2%B7%20HTML%20%C2%B7%20PDF-3092B1">
</p>

</div>

---

## What this is

This report is written for senior university research leadership: Deputy Vice-Chancellors and Deputy Provosts of Research, Pro-Vice-Chancellors and Deputy Vice Presidents of Research, faculty Deans and Associate Deans of Research, Deans of Graduate Schools and Associate Deans of Research Training, higher-degrees and research-integrity committees, and the peak bodies that represent graduate students. Its purpose is to give that audience a shared, evidence-anchored vocabulary for benchmarking institutional readiness on responsible AI use in research and research training, and a maturity grid that translates the vocabulary into concrete decisions on policy, curriculum, infrastructure, and governance.

The report is the global anchor of a planned regional series. The same five-dimension capability framework and the same four-level maturity grid will be re-populated in later companion reports for the US / Americas, the UK / Europe, and APAC ex Japan.

## Public audit package

This public repository contains the material needed to inspect the report's factual surface:

- the report source manuscript at [`drafts/report.md`](drafts/report.md);
- the canonical numerical manifest at [`data/values.yml`](data/values.yml);
- the public claim and source register at [`sources/claim_register.yml`](sources/claim_register.yml);
- the web edition in [`docs/`](docs/);
- the publication-formatted artefacts (DOCX, HTML, PDF) attached to the [latest GitHub Release](https://github.com/mzyphur/responsible-ai-in-research-training/releases/latest).

The report draws on eight primary-source evidence dossiers covering national research-funder AI policies (14 funders across 11 countries plus the EU's European Research Council), institutional AI policies at top-tier doctoral universities (38 universities across 15 countries and jurisdictions), existing AI-literacy and researcher-development capability frameworks (13 frameworks), publisher and journal AI policies (18 publishers plus 3 preprint servers), AI tool taxonomy (11 classes), privacy / IP / governance frameworks (14), the reproducibility-crisis intersection with AI augmentation, and adversarial-review patterns. The dossiers are working notes retained privately by Instats per the public/private boundary protocol; every load-bearing claim in this report carries a primary-source URL with a 2026-05-18 snapshot date in the body footnotes.

Instats publishes the report source, numerical manifest, public claim register, public value/caveat change log, and release files needed to inspect the report. Additional working files are retained privately by Instats. The author retains responsibility for every numerical claim, interpretation, and recommendation. Questions about public evidence can be sent to [support@instats.org](mailto:support@instats.org).

---

## Read it / cite it

| | |
|---|---|
| **Read online** | **<https://mzyphur.github.io/responsible-ai-in-research-training/>** |
| Microsoft Word (.docx) | [Latest release ->](https://github.com/mzyphur/responsible-ai-in-research-training/releases/latest) |
| PDF | [Latest release ->](https://github.com/mzyphur/responsible-ai-in-research-training/releases/latest) |
| Web edition | [`docs/index.html`](docs/index.html) for Pages; HTML and PDF builds attached to the [latest release](https://github.com/mzyphur/responsible-ai-in-research-training/releases/latest) |
| Markdown source | [`drafts/report.md`](drafts/report.md) |

**Citation.** Zyphur, M. J. (2026). *Responsible AI in Academic Research: A Capability Framework for Research Training.* Instats Policy Series, v1.2.3. <https://github.com/mzyphur/responsible-ai-in-research-training>. ORCID: [0000-0003-3237-7892](https://orcid.org/0000-0003-3237-7892). DOI: 10.61700/t31oy23grr.

BibTeX:

```bibtex
@techreport{zyphur2026responsibleai,
  author      = {Zyphur, Michael J.},
  title       = {Responsible AI in Academic Research: A Capability Framework for Research Training},
  institution = {Instats},
  type        = {Instats Policy Series},
  number      = {v1.2.3},
  year        = {2026},
  url         = {https://github.com/mzyphur/responsible-ai-in-research-training},
  note        = {ORCID: 0000-0003-3237-7892. DOI: 10.61700/t31oy23grr.},
  doi         = {10.61700/t31oy23grr}
}
```

Machine-readable citation: [`CITATION.cff`](CITATION.cff).

---

## The five-dimension capability framework

The framework's spine, set out in Part 2 of the report and operationalised as a four-level maturity grid in Part 4 and Appendix A:

1. **Human-in-the-loop discipline** — the institutional commitment that the judgement steps which define research remain human, with task-level demarcation between labour and judgement.
2. **Responsible use in practice** — operational rules for the four AI-use modes (search; co-author; validator; tutor) at PhD level.
3. **Tooling that promotes responsible use** — institutional procurement standard incorporating six observable properties (verifiable citation, data residency, uncertainty reporting, reproducibility, auditability, open-source-and-local options).
4. **AI-literate humans** — six load-bearing competencies for PhD researchers, supervisors, and examiners (citation verification; model-and-parameter specification; prompt-as-fork-in-the-garden discipline; model-heterogeneity in adversarial review; sycophancy detection and human-as-verifier discipline; structured failure-mode reporting).
5. **Institutional benchmarking grid** — the institutional capability to know where it sits on Dimensions 1-4 and act on what the answer reveals, scored across four axes: policy / people / systems / process.

Appendix G of the report carries a worked labour-vs-judgement task taxonomy that institutions can adopt and adapt.

---

## Repository map

```
responsible-ai-in-research-training/
├── docs/                  ← published GitHub Pages site (HTML + PDF mirror)
├── drafts/
│   └── report.md          ← markdown source manuscript
├── final/
│   ├── report.docx        ← Microsoft Word build (Word-for-Mac compatible)
│   └── reference.docx     ← pandoc reference template
├── data/
│   ├── values.yml         ← numerical manifest (placeholder schema; this report
│   │                        uses no headline_check entries)
│   └── change_log.yml     ← public value/caveat change log
├── sources/
│   ├── claim_register.yml ← public claim/source register
│   └── fx_rates.md        ← FX reference table (not used by this publication)
├── assets/
│   └── instats_logo.png
├── CITATION.cff           ← machine-readable citation (CFF 1.2)
├── LICENSE                ← CC BY-NC 4.0
├── README.md              ← this file
├── SECURITY.md
└── VERSION                ← single source of truth (1.1.0)
```

Working notes (evidence dossiers; Stage A/B/C/D/E review files; private launch and dissemination packs) are retained privately by Instats per the public/private boundary protocol and are not part of this public repository.

---

## How this report was made

This report was produced through a five-stage adversarial review pipeline, all stages complete before v1.0.0:

- **Stage A** — adversarial fact-checking pair (Claude Opus 4.7 + OpenAI GPT-5.5 codex, running independently against the same draft). 9 P0 release-blocking findings and 20 P1 material findings were caught and resolved in v0.5.1 and v0.5.2.
- **Stage B** — persona panel: 12 hypothetical reader personas across the five audience tiers, run as a single Opus 4.7 sub-agent. 9 of 12 personas would circulate the report at their institution unconditionally; zero negative verdicts. The Bucket C labour-vs-judgement task taxonomy (Appendix G) was added in response to convergent feedback from six personas across four tiers.
- **Stage C** — three Gemini-3-Flash-Preview copy-editor passes (sentence, paragraph, section levels) running in parallel.
- **Stage D** — codex GPT-5.5 synthesis of the 80 Stage C suggestions: 23 ACCEPT, 13 PARTIAL, 33 REJECT, 11 STALE; the accepted edits landed at v0.6.0.
- **Stage E** — voice-and-naturalness review pair (Gemini-3-Flash-Preview + codex GPT-5.5; Claude excluded by protocol because of the same-family-pair bias risk). 43 voice-sweep edits applied; prose em-dash density reduced from 79 to 52 across the 20,500-word manuscript.

The author used author-directed computational and research-assistance workflows while preparing this report. The author retains responsibility for every numerical claim, interpretation, and recommendation; every load-bearing claim was verified against the primary sources by the lead author before publication.

---

## Author

<table>
<tr>
<td valign="top" width="80">
  <img src="assets/instats_logo.png" width="64">
</td>
<td valign="top">

**Michael J. Zyphur, PhD**
Instats &nbsp;|&nbsp; [instats.org](https://instats.org)
[support@instats.org](mailto:support@instats.org)

</td>
</tr>
</table>

### License

**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** — see [LICENSE](LICENSE). Share and adapt with attribution; commercial reuse requires written permission.

---

<div align="center">

<sub>Instats Policy Series · 2026 · Published openly so any reader can audit the evidence and the framework.</sub>

</div>
