"""Regulatory response timeline for the Responsible AI report.

# red-clusters: 6

The chart intentionally uses six accent-red markers, one per Class D
university (UCL Doctoral School, KCL Centre for Education Studies,
Heidelberg Graduate Academy, KU Leuven, University of Helsinki,
Tsinghua University). The visual story depends on showing all six
Class D institutions as the leading tier in an otherwise empty
universities lane — each red dot is a load-bearing data point, not
decorative emphasis. The Instats single-accent-cluster convention is
intentionally relaxed here per the published audit directive above.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from style import apply_style, COLORS, set_chart_title

apply_style()

OUT = Path(__file__).parent / "png"
SVG = Path(__file__).parent / "svg"
OUT.mkdir(exist_ok=True)
SVG.mkdir(exist_ok=True)


TITLE = (
    "Publishers responded in months. National research funders responded "
    "over years. Universities still mostly haven't."
)

UNIVERSITY_DOTS = [
    (18, "UCL Doctoral School"),
    (22, "Heidelberg Graduate Academy"),
    (24, "King's College London"),
    (26, "KU Leuven"),
    (28, "University of Helsinki"),
    (37, "Tsinghua University"),
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(10, 4.35))

    lane_height = 0.5

    # Universities: the lane exists across the full period, but only six
    # institutions reached the report's Class D standard by May 2026.
    ax.barh(
        y=0,
        width=42,
        left=0,
        color=COLORS["neutral_mid"],
        alpha=0.3,
        height=lane_height,
        edgecolor="none",
        zorder=1,
    )

    ax.barh(
        y=1,
        width=31,
        left=10,
        color=COLORS["secondary"],
        height=lane_height,
        edgecolor="none",
        zorder=2,
    )

    ax.barh(
        y=2,
        width=3,
        left=0,
        color=COLORS["primary"],
        height=lane_height,
        edgecolor="none",
        zorder=3,
    )

    for x, _label in UNIVERSITY_DOTS:
        ax.plot(
            x,
            0,
            marker="o",
            markersize=8,
            markerfacecolor=COLORS["accent"],
            markeredgecolor=COLORS["paper"],
            markeredgewidth=1.2,
            linestyle="none",
            zorder=4,
        )

    ax.axvline(0, color=COLORS["ink_soft"], linewidth=0.8, zorder=0)
    ax.axvline(42, color=COLORS["ink_soft"], linewidth=0.8, zorder=0)

    ax.text(
        0.25,
        2.58,
        "ChatGPT-3.5 release\nNov 2022",
        ha="left",
        va="bottom",
        color=COLORS["ink_soft"],
        fontsize=8.5,
    )
    ax.text(
        42,
        2.58,
        "May 2026",
        ha="right",
        va="bottom",
        color=COLORS["ink_soft"],
        fontsize=8.5,
    )

    ax.annotate(
        "sector-wide policy adoption\n~10 weeks",
        xy=(3, 2),
        xytext=(6.1, 2.18),
        ha="left",
        va="center",
        color=COLORS["ink"],
        fontsize=9,
        arrowprops={
            "arrowstyle": "-|>",
            "color": COLORS["primary"],
            "lw": 0.9,
            "shrinkA": 3,
            "shrinkB": 2,
        },
    )

    ax.text(
        25.5,
        1,
        "Sep 2023 to Apr 2026",
        ha="center",
        va="center",
        color=COLORS["paper"],
        fontsize=9,
        fontweight="medium",
    )

    ax.annotate(
        "Vitae RDF refresh\nmissed AI · May 2025",
        xy=(30, 0),
        xytext=(30, 0.74),
        ha="center",
        va="bottom",
        color=COLORS["ink"],
        fontsize=8.5,
        arrowprops={
            "arrowstyle": "-|>",
            "color": COLORS["neutral_dark"],
            "lw": 0.8,
            "shrinkA": 4,
            "shrinkB": 5,
        },
    )

    ax.annotate(
        "Tsinghua AI framework · Dec 2025\nintegrated teaching, research, and theses",
        xy=(37, 0),
        xytext=(36.3, -0.62),
        ha="right",
        va="top",
        color=COLORS["ink"],
        fontsize=8.5,
        arrowprops={
            "arrowstyle": "-|>",
            "color": COLORS["accent"],
            "lw": 0.8,
            "shrinkA": 4,
            "shrinkB": 5,
        },
    )

    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["UNIVERSITIES", "NATIONAL\nRESEARCH FUNDERS", "PUBLISHERS"])
    ax.set_xlabel("Months from ChatGPT-3.5 release (Nov 2022)")
    ax.set_xlim(-2, 44)
    ax.set_ylim(-0.85, 2.85)
    ax.set_xticks(range(0, 43, 6))

    ax.grid(axis="x", color=COLORS["rule_soft"], linewidth=0.5)
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)

    set_chart_title(ax, TITLE)

    fig.savefig(OUT / "01_regulatory_response_timeline.png")
    fig.savefig(SVG / "01_regulatory_response_timeline.svg")
    plt.close(fig)


if __name__ == "__main__":
    main()
