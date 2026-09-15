# SPYA professional rebuild

This package replaces the first scaffold with 16 static HTML pages, shared styling, a mobile menu and a searchable sports directory. It uses no paid services or build dependencies. Python's standard library generates pages.

## Install on the existing Mac project

1. Unzip the package.
2. Run `.venv/bin/python /path/to/spya-professional/install.py "$HOME/Documents/SPYA Re-design/spya-redesign"` from your original project.
3. Start `.venv/bin/python -m http.server 8000 --bind 127.0.0.1` and visit http://localhost:8000.

The installer backs up files it replaces into a timestamped folder next to the repository. It leaves the repository history, virtual environment and extraction data untouched. It does not push or deploy.

## Maintain the website

- `data/site.json`: edit sport descriptions, contacts, seasons, program summaries and review notes here.
- `scripts/build_site.py`: shared page templates and general page content.
- `css/styles.css`: palette, typography, layout and responsive breakpoints.
- `js/app.js`: mobile menu and sport search.
- Run `.venv/bin/python scripts/build_site.py` after changing data or templates. Direct edits to generated HTML will be overwritten by this command.

## Assets and availability

Typography uses Barlow Condensed and DM Sans from Google Fonts, with system font fallbacks. Two existing SPYA image URLs are referenced remotely. Internet access is required to load these images and fonts. SPYA imagery is included by reference for this local redesign review; confirm reuse authorization before official launch. Images have not been copied into the package.

The baseball photograph is sourced from the official Senior Legion page's 2023 championship photo. The lacrosse image is sourced from the original Lacrosse page. If SPYA moves these assets, replace their URLs in `scripts/build_site.py`, or place approved images at `assets/images/baseball.jpg` and `assets/images/lacrosse.jpg`, then rebuild.

## Content and launch status

This is a redesign preview, not an approved live replacement. Pages have `noindex` metadata. Reviewed source date: September 15, 2026. The calendar links to the official calendar; it does not mirror or fabricate events. Registration directs users to official SPYA pages and does not accept payments or player information. Old and inconsistent deadlines are not presented as open registrations. Published season labels are informational, not a live availability feed.

All nine sports have local summary pages. Detailed league rules and official documents remain linked to their sources. Older near-empty lacrosse subpages are consolidated. Full board membership is maintained at the official directory rather than duplicated here.

Before official launch: obtain current dates, fees, policies and contacts; approve imagery; check desktop and mobile layouts, keyboard focus and screen-reader navigation; test external registration destinations; confirm financial assistance instructions; remove preview/noindex only when authorized. Map old URLs when migrating the domain. Hosting and domain settings have not been changed.

## Validation performed

Generated all 16 pages and checked local asset/page references, page titles, primary headings and local fragment targets. Browser visual review was blocked in the build environment. Mobile, font rendering, image cropping and screen-reader behavior still require review on the user's Mac. No accessibility-conformance certification is claimed.
