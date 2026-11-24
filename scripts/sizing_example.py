"""Rebuild the 180 mm Illustrator example with simulated observations."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

from panel import panel_style, save_panel, size_mm

WIDTH, HEIGHT, GAP = 180, 107, 4
INK = "#25313A"
CD4, CD8, OTHER = "#396F99", "#AD5137", "#8D999F"


def make_figure():
    rng = np.random.default_rng(17)
    fig = plt.figure(figsize=size_mm(WIDTH, HEIGHT))

    def axes_mm(x, top, width, height):
        return fig.add_axes([x / WIDTH, 1 - (top + height) / HEIGHT,
                             width / WIDTH, height / HEIGHT])

    def text_mm(x, top, text, **kwargs):
        return fig.text(x / WIDTH, 1 - top / HEIGHT, text,
                        va="top", color=INK, **kwargs)

    def heading(x, top, letter, title):
        text_mm(x, top, letter, weight="bold")
        text_mm(x + 5, top, title)

    # Three independently labelled panels. Each has a 57.33 mm allocation.
    slot = (WIDTH - 2 * GAP) / 3
    left = [i * (slot + GAP) for i in range(3)]
    for x, letter, title in zip(left, "abc",
                                ["Paired samples", "Differential expression", "Cell embedding"]):
        heading(x + 1.5, 2, letter, title)

    paired = axes_mm(left[0] + 12, 10, 40, 29)
    pre = rng.uniform(14, 41, 11)
    post = np.clip(pre + rng.normal(7, 7, len(pre)), 3, 57)
    for a, b in zip(pre, post):
        paired.plot([0, 1], [a, b], color="#A1A9AD", lw=0.6)
    paired.scatter(np.repeat([0, 1], len(pre)), np.r_[pre, post],
                   s=11, color=INK, linewidths=0, zorder=3)
    paired.set(xlim=(-0.4, 1.4), ylim=(0, 60), yticks=[0, 20, 40, 60],
               ylabel="CD8 T cells (%)")
    paired.set_xticks([0, 1], ["Pre", "Week 6"])

    volcano = axes_mm(left[1] + 11, 10, 42, 29)
    fc = rng.normal(0, 1.03, 2500)
    score = np.maximum(0, 0.43 * np.abs(fc) ** 2 + rng.gamma(1.2, 0.42, fc.size))
    fc = np.r_[fc, -2.55, 2.60]
    score = np.r_[score, 5.25, 5.1]
    threshold = -np.log10(0.05)
    colors = np.where((fc < -1) & (score >= threshold), "#397C71",
                      np.where((fc > 1) & (score >= threshold), "#79598B", "#C1C9CC"))
    volcano.scatter(fc, score, s=2.2, c=colors, linewidths=0, rasterized=True)
    for x in (-1, 1):
        volcano.axvline(x, color="#6B7377", lw=0.55, ls="--")
    volcano.axhline(threshold, color="#6B7377", lw=0.55, ls="--")
    for i, label, dx in [(-2, "A", 3), (-1, "B", -8)]:
        volcano.annotate(label, (fc[i], score[i]), xytext=(dx, 2),
                         textcoords="offset points", color=INK)
    volcano.set(xlim=(-4.3, 4.3), ylim=(0, 6.5), xticks=[-4, 0, 4], yticks=[0, 3, 6],
                xlabel="log2 fold change", ylabel="−log10(FDR)")

    embedding = axes_mm(left[2] + 2, 9, slot - 5, 38)
    for center, shape, shade in [((-1.8, 0.95), (0.62, 0.46), CD4),
                                  ((1.5, 0.85), (0.63, 0.52), CD8),
                                  ((0.0, -1.30), (0.88, 0.43), OTHER)]:
        xy = rng.normal(center, shape, size=(1450, 2))
        embedding.scatter(xy[:, 0], xy[:, 1], s=2, c=shade, alpha=0.7,
                          lw=0, rasterized=True)
    for x, y, label in [(-1.9, 2.48, "CD4 T"), (1.6, 2.48, "CD8 T"),
                        (0.3, -2.65, "Other")]:
        embedding.text(x, y, label, ha="center", va="center", color=INK)
    embedding.set(xlim=(-4, 4), ylim=(-3.2, 2.7), aspect="equal")
    embedding.set_axis_off()

    # Four equal 38 mm data areas share a left margin, units, scales and legend.
    heading(1.5, 52, "d", "T-cell frequencies over time")
    handles = [Line2D([], [], color=CD4, marker="o", lw=0.9, markersize=3.2, label="CD4 T"),
               Line2D([], [], color=CD8, marker="s", lw=0.9, markersize=3.2, label="CD8 T")]
    fig.legend(handles=handles, loc="upper right", bbox_to_anchor=(0.99, 1 - 51 / HEIGHT),
               frameon=False, ncol=2, borderaxespad=0, handlelength=1.5,
               handletextpad=0.5, columnspacing=1.4)
    days = np.array([0, 3, 7, 14])
    data_width = (WIDTH - 13 - 3 - 3 * GAP) / 4
    for i in range(4):
        x = 13 + i * (data_width + GAP)
        text_mm(x + data_width / 2, 60, f"Patient {i + 1}", ha="center")
        ax = axes_mm(x, 67, data_width, 23.5)
        cd4 = [36, 39, 40, 43] + rng.normal(0, 3.6, 4)
        cd8 = [16, 20, 27, 32] + rng.normal(0, 3.1, 4)
        ax.plot(days, cd4, "o-", color=CD4, lw=0.9, markersize=3.2)
        ax.plot(days, cd8, "s-", color=CD8, lw=0.9, markersize=3.2)
        ax.set(xlim=(-0.7, 14.7), xticks=[0, 7, 14], ylim=(0, 60), yticks=[0, 30, 60])
        if i == 0:
            ax.set_ylabel("Immune cells (%)")
        else:
            ax.spines.left.set_visible(False)
            ax.tick_params(axis="y", left=False, labelleft=False)
    text_mm(95, 97, "Time (days)", ha="center")
    text_mm(177, 102, "Simulated data", ha="right", style="italic")
    for ax in fig.axes:
        ax.tick_params(length=2.2, pad=2, colors=INK)
        ax.xaxis.label.set_color(INK)
        ax.yaxis.label.set_color(INK)
    return fig


if __name__ == "__main__":
    with panel_style():
        figure = make_figure()
        output = Path(__file__).resolve().parents[1] / "assets" / "180mm拼版示例"
        save_panel(figure, output, dpi=600)
        plt.close(figure)
