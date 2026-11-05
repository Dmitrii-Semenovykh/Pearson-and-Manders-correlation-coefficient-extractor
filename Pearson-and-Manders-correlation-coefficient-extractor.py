import re
from pathlib import Path
import pandas as pd

FOLDER = Path(r"C:\Users\path to your files")   # folder with your .txt files
OUTPUT = FOLDER / "coefficients.xlsx"

NUM = r"(-?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?)"

pearson_re = re.compile(r"Pearson'?s\s+Coefficient[^\n]*?\n?[^\d\-]*?" + NUM, re.IGNORECASE)
heading_re = re.compile(r"Manders'?\s+Coefficients[^\n]*", re.IGNORECASE)
m1_re = re.compile(r"M1\D*?" + NUM, re.IGNORECASE)
m2_re = re.compile(r"M2\D*?" + NUM, re.IGNORECASE)

def to_float(s):
    return float(s.replace(",", "."))

def parse_manders(text):
    """Return {"orig": (m1, m2), "thr": (m1, m2)} based on each heading."""
    result = {"orig": (None, None), "thr": (None, None)}
    headings = list(heading_re.finditer(text))
    for i, h in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        section = text[h.end():end]
        m1, m2 = m1_re.search(section), m2_re.search(section)
        vals = (to_float(m1.group(1)) if m1 else None,
                to_float(m2.group(1)) if m2 else None)
        key = "thr" if "threshold" in h.group(0).lower() else "orig"
        result[key] = vals
    return result

rows = []
for f in sorted(FOLDER.glob("*.txt")):
    text = f.read_text(encoding="utf-8", errors="ignore")

    p = pearson_re.search(text)
    man = parse_manders(text)

    row = {
        "File": f.name,
        "Pearson": to_float(p.group(1)) if p else None,
        "M1_original": man["orig"][0],
        "M2_original": man["orig"][1],
        "M1_threshold": man["thr"][0],
        "M2_threshold": man["thr"][1],
    }
    rows.append(row)
    if any(v is None for v in row.values()):
        print(f"Warning: missing value(s) in {f.name}")

df = pd.DataFrame(rows)
df.to_excel(OUTPUT, index=False)
print(f"Saved {len(df)} files to {OUTPUT}")