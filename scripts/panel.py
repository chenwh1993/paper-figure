"""Illustrator panel defaults for Matplotlib. Dimensions are specified at final size."""
from pathlib import Path
import re

import matplotlib as mpl
from matplotlib import font_manager
from matplotlib.legend import Legend
from matplotlib.text import Text


def size_mm(width=85, height=65):
    return width / 25.4, height / 25.4


def panel_style():
    font_manager.findfont(font_manager.FontProperties(family="Arial"),
                          fallback_to_default=False)
    return mpl.rc_context({
        "font.family": "Arial", "font.size": 8, "axes.titlesize": 8,
        "axes.labelsize": 8, "xtick.labelsize": 8, "ytick.labelsize": 8,
        "legend.fontsize": 8, "legend.title_fontsize": 8,
        "figure.titlesize": 8, "axes.linewidth": 0.6,
        "xtick.major.width": 0.6, "ytick.major.width": 0.6,
        "axes.spines.top": False, "axes.spines.right": False,
        "pdf.fonttype": 42, "pdf.use14corefonts": False,
        "svg.fonttype": "none", "svg.image_inline": True,
        "text.usetex": False, "savefig.bbox": None,
    })


def save_panel(fig, stem, dpi=600):
    """Rasterize only the artists designated by the caller. Keep the full artboard."""
    stem = Path(stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    with panel_style():
        fig.canvas.draw()
        for label in fig.findobj(Text):
            label.set_fontfamily("Arial")
            label.set_fontsize(8)
        for legend in fig.findobj(Legend):
            for item in legend.findobj():
                if item.get_rasterized():
                    item.set_rasterized(False)
        for ext in ("pdf", "svg"):
            fig.savefig(stem.parent / f"{stem.name}.{ext}", dpi=dpi,
                        bbox_inches=None, facecolor=fig.get_facecolor())
    # Illustrator reads Matplotlib's numeric bold shorthand as 12 pt on SVG import.
    svg_path = stem.parent / f"{stem.name}.svg"
    svg = svg_path.read_text(encoding="utf-8")
    fixed, count = re.subn(
        r'(<(?:text|tspan)\b[^>]*?\bfont:\s*(?:(?:italic|oblique)\s+)?)700(?=\s)',
        r'\1bold', svg,
    )
    if count:
        svg_path.write_text(fixed, encoding="utf-8")

