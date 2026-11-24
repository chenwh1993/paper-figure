"""Check a single exported Illustrator panel against its intended size and layer design."""
import argparse
from pathlib import Path
import xml.etree.ElementTree as ET

import pymupdf


def check(stem, width, height, mixed, required):
    pdf, svg = (stem.parent / f"{stem.name}.{ext}" for ext in ("pdf", "svg"))
    with pymupdf.open(pdf) as doc:
        if len(doc) != 1:
            raise ValueError("Expected a single panel page")
        page = doc[0]
        actual = [v * 25.4 / 72 for v in (page.rect.width, page.rect.height)]
        bounds_ok = all(abs(x - y) < 0.12 for x, y in zip(actual, (width, height)))
        blocks = page.get_text("dict", flags=pymupdf.TEXTFLAGS_TEXT)["blocks"]
        spans = [s for b in blocks for ln in b.get("lines", []) for s in ln["spans"]
                 if s["text"].strip()]
        pdf_text = page.get_text()
        families = sorted({s["font"] for s in spans})
        sizes = sorted({round(s["size"], 2) for s in spans})
        editable = bool(spans) and all("arial" in s["font"].lower()
                                       and abs(s["size"] - 8) < 0.08 for s in spans)
        images = len(page.get_image_info())
        paths = len(page.get_drawings())
        embedded = all(len(doc.extract_font(x[0])[-1]) > 0 for x in page.get_fonts())
    root = ET.parse(svg).getroot()
    ns = "{http://www.w3.org/2000/svg}"
    texts = root.findall(".//" + ns + "text")
    svg_text = "\n".join("".join(n.itertext()) for n in texts)
    bitmaps = root.findall(".//" + ns + "image")
    linked = [n for n in bitmaps if not (n.get("{http://www.w3.org/1999/xlink}href")
                                         or n.get("href") or "").startswith("data:image/")]
    def svg_mm(value):
        for unit, factor in (("mm", 1), ("pt", 25.4/72), ("in", 25.4),
                             ("cm", 10), ("px", 25.4/96)):
            if value.endswith(unit):
                return float(value[:-len(unit)]) * factor
        return float(value) * 25.4/96
    svg_bounds = all(abs(svg_mm(root.get(k, "0")) - v) < 0.12
                     for k, v in (("width", width), ("height", height)))
    print(f"PDF {actual[0]:.2f} x {actual[1]:.2f} mm | fonts {families} {sizes} pt | "
          f"{images} images, {paths} paths | SVG {len(texts)} text, {len(bitmaps)} images")
    checks = {"physical size": bounds_ok and svg_bounds, "PDF live Arial 8 pt": editable,
              "PDF font embedding": embedded, "PDF vector geometry": paths > 0,
              "SVG live text": bool(texts), "SVG images embedded": not linked,
              "selected raster mode": ((images > 0) == mixed and (len(bitmaps) > 0) == mixed),
              "expected labels in both": all(s in pdf_text and s in svg_text for s in required)}
    failed = [k for k, v in checks.items() if not v]
    if failed:
        raise ValueError(", ".join(failed))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stem", type=Path, help="Output path without the .pdf or .svg extension")
    parser.add_argument("--mm", nargs=2, type=float, required=True, metavar=("WIDTH", "HEIGHT"))
    parser.add_argument("--mode", choices=["vector", "mixed"], required=True)
    parser.add_argument("--label", action="append", default=[])
    args = parser.parse_args()
    check(args.stem, *args.mm, args.mode == "mixed", args.label)

