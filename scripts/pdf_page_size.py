"""Keep R Cairo's vector artwork and replace its integer-point PDF page box."""
from pathlib import Path
import sys

import pymupdf

if __name__ == "__main__":
    path, width_mm, height_mm = sys.argv[1:]
    with pymupdf.open(Path(path)) as doc:
        width, height = (float(x) * 72 / 25.4 for x in (width_mm, height_mm))
        page = doc[0]
        if len(doc) != 1 or abs(page.rect.width-width) > 1.01 or abs(page.rect.height-height) > 1.01:
            raise ValueError("Unexpected PDF dimensions. Expected only Cairo's point rounding.")
        page.set_mediabox(pymupdf.Rect(0, 0, width, height))
        doc.saveIncr()

