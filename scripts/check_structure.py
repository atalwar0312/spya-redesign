"""Non-destructive link and structure checks for SPYA's static GitHub Pages site.

Uses only the Python standard library. Never rewrites the published pages.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted(ROOT.glob("*.html"))
REQUIRED = {
    "index.html", "sports.html", "registration.html", "resources.html",
    "community.html", "about.html", "calendar.html", "404.html",
    "baseball.html", "basketball.html", "cheer.html", "field-hockey.html",
    "football.html", "lacrosse.html", "nfl-flag.html", "soccer.html",
    "softball.html",
}

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.h1 = 0
        self.titles = 0
        self.lang = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.titles += 1
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.refs.append((tag, attrs[attr]))
        if tag == "img" and "alt" not in attrs:
            issues.append(f"{current}: image missing alt text")

issues = []
pages = {}
for missing in sorted(REQUIRED - {p.name for p in PAGES}):
    issues.append(f"Missing required page: {missing}")

for file in PAGES:
    current = file.name
    parsed = PageParser()
    parsed.feed(file.read_text(encoding="utf-8"))
    pages[file.name] = parsed
    if parsed.h1 != 1:
        issues.append(f"{file.name}: expected one h1, got {parsed.h1}")
    if parsed.titles != 1:
        issues.append(f"{file.name}: expected one title, got {parsed.titles}")
    if parsed.lang != "en":
        issues.append(f"{file.name}: expected html lang=en")

for name, page in pages.items():
    for tag, value in page.refs:
        url = urlsplit(value)
        if url.scheme or url.netloc or value.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
            continue
        local = unquote(url.path)
        if not local:
            target = ROOT / name
        elif local.startswith("/"):
            issues.append(f"{name}: root-absolute reference not suitable for project Pages: {value}")
            continue
        else:
            target = (ROOT / local).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            issues.append(f"{name}: reference escapes repository: {value}")
            continue
        if not target.is_file():
            issues.append(f"{name}: missing local asset/page: {value}")
        elif url.fragment and target.suffix.lower() == ".html":
            relative = target.relative_to(ROOT.resolve()).as_posix()
            if relative in pages and unquote(url.fragment) not in pages[relative].ids:
                issues.append(f"{name}: missing anchor: {value}")

if issues:
    print("Site check FAILED:")
    for issue in issues:
        print(" -", issue)
    sys.exit(1)
print(f"PASS: {len(PAGES)} HTML pages; essential pages, page titles, headings, and local asset references.")
print("Note: external links, visual layouts, browser interactivity and accessibility conformance require manual testing.")
