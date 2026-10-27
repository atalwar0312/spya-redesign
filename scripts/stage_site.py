"""Stage SPYA's static site for publishing without changing source files.

HTML source lives in pages/. Published HTML, assets, CSS and JavaScript
are assembled at the root of dist/ to keep existing public URLs stable.
"""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "pages"
DEST = ROOT / "dist"

if not SOURCE.is_dir():
    raise SystemExit("Missing pages/ source folder")
if not (SOURCE / "index.html").is_file():
    raise SystemExit("Missing pages/index.html")
if DEST.exists():
    shutil.rmtree(DEST)
DEST.mkdir()

for page in SOURCE.glob("*.html"):
    shutil.copy2(page, DEST / page.name)

for dirname in ("assets", "css", "js"):
    src = ROOT / dirname
    if not src.is_dir():
        raise SystemExit(f"Missing required directory: {dirname}")
    shutil.copytree(src, DEST / dirname)

# GitHub Pages should not use Jekyll processing.
(DEST / ".nojekyll").write_text("", encoding="utf-8")
print(f"Staged {len(list(SOURCE.glob('*.html')))} pages into {DEST.relative_to(ROOT)}/")
