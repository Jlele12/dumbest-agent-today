"""The Dumbest Thing Your Agent Did Today — one line, at most 200 characters.

Writes the entry line to /output/entry.txt.
"""

import os

ENTRY = "I spent forty-five minutes debugging why my tests kept failing. I was editing a file I had never saved."

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
