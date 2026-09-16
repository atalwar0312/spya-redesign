# SPYA refined draft

A separate, quieter revision of the first redesign: 16 static pages, a shorter homepage, sentence-case typography, expandable program details and fewer repeated calls to action.

## Preview on a Mac

Open Terminal in the extracted spya-refined folder and run:

    python3 -m http.server 8001 --bind 127.0.0.1

Open http://localhost:8001. This is local to the Mac. No public site changes until files are committed and uploaded to GitHub.

## Editing

- data/site.json: sport summaries, program descriptions and public email contacts.
- scripts/build_site.py: shared layout and general page copy.
- css/styles.css: responsive layout and typography.
- js/app.js: mobile menu and sports search.

After editing templates or data, run:

    python3 scripts/build_site.py
    python3 scripts/validate_site.py

Do not edit generated HTML unless you also change the template. Rebuilding overwrites generated HTML.

## Optional installation into the previous project

The included install.py backs up replaced files into a timestamped sibling folder. It accepts an existing website folder containing index.html or a Git repository. Run it only when ready to replace the older local draft. It does not publish, commit or push.

## Assets

The homepage uses one remote SPYA photograph of the 2023 Senior Legion championship team with a matching caption. Google Fonts supplies DM Sans and Manrope; system fonts are fallbacks. Internet access is needed for remote assets. Confirm SPYA photo permissions before official launch.

## Content and publishing

Read CONTENT-REVIEW.md for the three review passes and unresolved facts. No general link points back to the old SPYA website. The two financial assistance PDF document links are retained. Stale or inaccessible enrollment forms are not promoted. Registration provides contact routes until current forms are confirmed.

The site remains a preview with noindex metadata. It is not a complete replacement for the operational registration platform or team scheduling system. Publishing to the user's existing GitHub Pages repository is a separate step.
