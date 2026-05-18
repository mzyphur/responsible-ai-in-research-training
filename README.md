<div align="center">

<a href="https://instats.org">
  <img src="assets/instats_logo.png" alt="Instats" width="240">
</a>

# <PROJECT_TITLE>
## *<SUBTITLE>*

**<ABSTRACT>**

<p>
  <a href="<PAGES_URL>">
    <img alt="Read online" src="https://img.shields.io/badge/Read%20the%20report%20online-00547B?style=for-the-badge&logo=readthedocs&logoColor=white">
  </a>
  <a href="<REPO_URL>/releases/latest">
    <img alt="Download Microsoft Word" src="https://img.shields.io/badge/Download%20.docx-3092B1?style=for-the-badge&logo=microsoftword&logoColor=white">
  </a>
</p>

<p>
  <img alt="Version" src="https://img.shields.io/github/v/release/<USER>/<REPO>?label=version&color=00547B">
  <img alt="License" src="https://img.shields.io/badge/license-CC%20BY--NC%204.0-3092B1">
  <img alt="Evidence" src="https://img.shields.io/badge/evidence-public%20audit%20package-00547B">
  <img alt="Formats" src="https://img.shields.io/badge/formats-DOCX%20%C2%B7%20HTML%20%C2%B7%20PDF-3092B1">
</p>

</div>

---

## What this is

<2–3 paragraphs explaining the topic and the headline finding. Open
with the strongest claim — readers should know in three sentences
whether to keep reading.>

## Public audit package

- **Public audit package** — source manuscript, numerical manifest, public claim register, change log, chart scripts, rendered charts, cleaned source dossiers, and primary-source footnotes.
- **N evidence dossiers** in [`research/`](research/), each focused on the public sources behind a material part of the report.
- **Calculation transparency** — formulas, assumptions, FX rates, and native-currency values are disclosed where they affect headline numbers.
- **All figures in the audience's currency** (default AUD) at RBA-verified FX rates; native-currency figures retained in parentheses.
- **Evidence boundary** — this repository is designed to let readers audit the public claims, not to publish private working notes or internal production materials.

Instats publishes the report source, numerical manifest, chart code, rendered
charts, source dossiers, public claim/source register, public value/caveat
change log, and release files needed to inspect the report.
Additional working files are retained privately by Instats. The author retains
responsibility for every numerical claim, interpretation, and recommendation.
Questions about public evidence can be sent to [support@instats.org](mailto:support@instats.org).

---

## Read it / cite it

| | |
|---|---|
| **Read online** | **<PAGES_URL>** |
| Microsoft Word (.docx) | [Latest release](<REPO_URL>/releases/latest) |
| HTML web edition | [<PAGES_URL>](<PAGES_URL>) |
| PDF | [docs/report.pdf](docs/report.pdf) |
| Markdown source | [`drafts/report.md`](drafts/report.md) |
| Numerical manifest | [`data/values.yml`](data/values.yml) |
| Public claim register | [`sources/claim_register.yml`](sources/claim_register.yml) |
| Public change log | [`data/change_log.yml`](data/change_log.yml) |

**Citation.** <AUTHOR>. (<CITATION_YEAR>). *<PROJECT_TITLE>: <SUBTITLE>.* Instats Policy Series, v<VERSION>. <REPO_URL>

**BibTeX**

```bibtex
@misc{<REPO>_<CITATION_YEAR>,
  author = {<AUTHOR>},
  title = {<PROJECT_TITLE>: <SUBTITLE>},
  year = {<CITATION_YEAR>},
  howpublished = {Instats Policy Series, v<VERSION>},
  url = {<REPO_URL>}
}
```

Machine-readable citation: [`CITATION.cff`](CITATION.cff).

---

## A few of the charts

<table>
<tr>
<td width="33%"><img src="charts/png/<CHART_1>.png" alt="<chart 1 description>"></td>
<td width="33%"><img src="charts/png/<CHART_2>.png" alt="<chart 2 description>"></td>
<td width="33%"><img src="charts/png/<CHART_3>.png" alt="<chart 3 description>"></td>
</tr>
<tr>
<td width="33%"><img src="charts/png/<CHART_4>.png" alt="<chart 4 description>"></td>
<td width="33%"><img src="charts/png/<CHART_5>.png" alt="<chart 5 description>"></td>
<td width="33%"><img src="charts/png/<CHART_6>.png" alt="<chart 6 description>"></td>
</tr>
</table>

All charts live in [`charts/png/`](charts/png/) and are reproducible
via the Python scripts in [`charts/`](charts/).

---

## Repository map

```
<REPO>/
├── docs/             ← published GitHub Pages site (HTML)
├── drafts/
│   └── report.md     ← markdown source
├── final/
│   ├── report.docx   ← Microsoft Word build
│   └── report.pdf    ← PDF build, if published outside docs/
├── research/         ← evidence dossiers
├── charts/           ← matplotlib + PNG output
├── data/
│   ├── values.yml     ← numerical manifest
│   └── change_log.yml ← public value/caveat change log
├── sources/
│   ├── claim_register.yml ← public claim/source/value map
│   └── fx_rates.md   ← FX reference table
├── assets/
│   └── instats_logo.png
└── README.md
```

---

## Reproducing the report

```bash
python3 -m pip install -r requirements.txt

# Regenerate public chart outputs
for f in charts/[0-9]*.py; do python3 "$f"; done
```

From a clean clone, readers should be able to inspect the manuscript,
source dossiers, [`data/values.yml`](data/values.yml),
[`sources/claim_register.yml`](sources/claim_register.yml),
[`data/change_log.yml`](data/change_log.yml), chart scripts, rendered charts,
and release files that substantiate the public claims. If a specific artefact
cannot be regenerated from public files, the limitation should be stated in the
relevant source note or release note.

## How this report was made

This public repository is an evidence-and-publication package. It includes the
materials needed to audit the report's factual and numerical claims: source
manuscript, public source dossiers, numerical manifest, chart scripts, rendered
charts, public claim/source/value map, public value/caveat change log, citation
metadata, and release artefacts. Additional working files are retained
privately by Instats. Public readers should be able to verify what the report
relies on without needing access to those private working files.

---

## Author

<table>
<tr>
<td valign="top" width="80">
  <img src="assets/instats_logo.png" width="64">
</td>
<td valign="top">

**<AUTHOR>**
Instats &nbsp;|&nbsp; [instats.org](https://instats.org)
[support@instats.org](mailto:support@instats.org)

</td>
</tr>
</table>

### AI assistance

The author used author-directed computational and research-assistance workflows
while preparing this report. The author retains responsibility for every
numerical claim, interpretation, and recommendation.

### License

**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** — see [LICENSE](LICENSE). Share and adapt with attribution; commercial reuse requires written permission.

---

<div align="center">

<sub>Instats Policy Series · <CITATION_YEAR> · Published openly so any reader can audit the evidence and calculations.</sub>

</div>
