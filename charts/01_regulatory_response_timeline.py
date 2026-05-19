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
    (18, "UCL Doctoral School", "May 2024"),
    (22, "Heidelberg Graduate Academy", "Sep 2024"),
    (24, "King's College London", "Nov 2024"),
    (26, "KU Leuven", "Jan 2025"),
    (28, "University of Helsinki", "Mar 2025"),
    (37, "Tsinghua University", "Dec 2025"),
]

DATE_TICKS = [
    (0, "Nov\n2022"),
    (6, "May\n2023"),
    (12, "Nov\n2023"),
    (18, "May\n2024"),
    (24, "Nov\n2024"),
    (30, "May\n2025"),
    (36, "Nov\n2025"),
    (42, "May\n2026"),
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(12, 5.5))
    fig.subplots_adjust(left=0.2, right=0.77, bottom=0.19, top=0.9)

    lane_height = 0.42
    university_lane_height = 0.58

    # Universities: the lane exists across the full period, but only six
    # institutions reached the report's Class D standard by May 2026.
    ax.barh(
        y=0,
        width=42,
        left=0,
        color=COLORS["neutral_mid"],
        alpha=0.24,
        height=university_lane_height,
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

    ax.scatter(
        [x for x, _label, _date in UNIVERSITY_DOTS],
        [0] * len(UNIVERSITY_DOTS),
        s=88,
        marker="o",
        facecolor=COLORS["accent"],
        edgecolor=COLORS["paper"],
        linewidth=1.4,
        zorder=4,
    )

    ax.text(
        3.7,
        2,
        "0-3 months\n~10 weeks",
        ha="left",
        va="center",
        color=COLORS["primary"],
        fontsize=9.2,
        fontweight="medium",
    )

    ax.text(
        25.5,
        1,
        "10-41 months\nSep 2023-Apr 2026",
        ha="center",
        va="center",
        color=COLORS["paper"],
        fontsize=9,
        fontweight="medium",
    )

    ax.text(
        1.0,
        0.09,
        "6 Class D policies by May 2026",
        ha="left",
        va="center",
        color=COLORS["ink"],
        fontsize=9,
        fontweight="medium",
        zorder=5,
    )
    ax.text(
        1.0,
        -0.15,
        "32 of 38 universities still not at Class D",
        ha="left",
        va="center",
        color=COLORS["neutral_dark"],
        fontsize=8.5,
        zorder=5,
    )

    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["UNIVERSITIES", "NATIONAL\nRESEARCH FUNDERS", "PUBLISHERS"])
    ax.set_xlabel("Months from ChatGPT-3.5 release")
    ax.set_xlim(0, 42)
    ax.set_ylim(-0.55, 2.55)
    ax.set_xticks([x for x, _label in DATE_TICKS])
    ax.set_xticklabels([label for _x, label in DATE_TICKS])

    ax.grid(axis="x", color=COLORS["rule_soft"], linewidth=0.5)
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)

    fig.lines.append(
        plt.Line2D(
            [0.8, 0.8],
            [0.22, 0.86],
            transform=fig.transFigure,
            color=COLORS["rule_soft"],
            linewidth=1,
        )
    )
    fig.text(
        0.815,
        0.82,
        "Class D university markers",
        ha="left",
        va="top",
        color=COLORS["ink"],
        fontsize=9.5,
        fontweight="medium",
    )
    fig.text(
        0.815,
        0.765,
        "\n".join(f"{date}: {label}" for _x, label, date in UNIVERSITY_DOTS),
        ha="left",
        va="top",
        color=COLORS["neutral_dark"],
        fontsize=8.4,
        linespacing=1.45,
    )
    fig.text(
        0.815,
        0.31,
        "The blank university lane is the result:\nmost audited institutions had not published\nAI-literacy + valid-practice guidance.",
        ha="left",
        va="top",
        color=COLORS["ink_soft"],
        fontsize=8.4,
        linespacing=1.35,
    )

    set_chart_title(ax, TITLE)

    fig.savefig(OUT / "01_regulatory_response_timeline.png")
    fig.savefig(SVG / "01_regulatory_response_timeline.svg")
    plt.close(fig)


if __name__ == "__main__":
    main()
