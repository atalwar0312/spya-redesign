# Repository architecture

This document describes how the SPYA redesign is organized and what should be edited for different types of changes.

## Deployment contract

**Keep the published `.html` pages at the repository root.** GitHub Pages serves the project at `/spya-redesign/`, and internal navigation uses relative links such as `sports.html`. Moving public pages into a `src/` directory without coordinating a build/deployment migration would break existing links.

```text
spya-redesign/
├── README.md                 Project overview, demo, and setup
├── CONTRIBUTING.md           Review process and conventions
├── .gitignore                Local and temporary files to exclude
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── site-checks.yml  Automated structural sanity checks
├── index.html                Home page
├── sports.html               Sport directory
├── registration.html         Registration hub
├── resources.html            Family resources
├── community.html            Community stories
├── about.html                Organization and leadership
├── calendar.html             Calendar
├── 404.html                  Missing-page fallback
├── *sport*.html              Nine individual sport pages
├── assets/images/            Site imagery and SPYA logo
├── css/styles.css            Shared design system and motion rules
├── js/app.js                 Navigation, filtering, interactions
├── data/
│   ├── site.json             Historical structured sport/source data
│   └── assets.json           Asset provenance and local paths
├── scripts/
│   ├── check_structure.py    Non-destructive CI checks
│   ├── validate_site.py      Stricter historical content/style validation
│   ├── build_site.py         LEGACY generator: see warning below
│   └── download_assets.py    Existing asset download helper
└── docs/
    ├── PROJECT_STRUCTURE.md  This file
    └── MAINTENANCE.md        Editing, QA, and release checklist
```

The sport pages currently include `baseball.html`, `basketball.html`, `cheer.html`, `field-hockey.html`, `football.html`, `lacrosse.html`, `nfl-flag.html`, `soccer.html`, and `softball.html`.

## Which file should I change?

| Goal | Primary files |
| --- | --- |
| Adjust the homepage | `index.html`, `css/styles.css` |
| Change registration content | `registration.html`, and verify the linked TeamSnap form |
| Edit a sport's information | Its corresponding sport HTML page |
| Update organization information | `about.html` |
| Edit financial aid and family resources | `resources.html` |
| Update championship/community information | `community.html` |
| Change the visual design or responsiveness | `css/styles.css` |
| Change mobile menu or sports filtering | `js/app.js` |
| Change images | `assets/images/`; check `data/assets.json` for provenance |
| Update project documentation | `README.md`, `docs/`, `CONTRIBUTING.md` |

## Important: source-of-truth distinction

**The checked-in root HTML files are the current website source of truth.** Some entries in `data/site.json` and the older `scripts/build_site.py` reflect an earlier site iteration.

Do **not** run `scripts/build_site.py` to update the current website. It generates and overwrites the root HTML pages from older templates and could erase the newer visual design, navigation fixes, and registration content. The legacy generator is retained as historical tooling only. It now requires an explicit opt-in before it will run.

For now, edit the current HTML directly. A future generator migration should reconcile the current design into templates, then verify a zero-unexpected-diff build before changing the deployment process.

## Validation

Run this lightweight, non-destructive check before creating a pull request:

```bash
python3 scripts/check_structure.py
```

It checks for essential pages and referenced local assets/links. It does not verify external sites, JavaScript behavior, responsive layout, or accessibility conformance. See [Maintenance](MAINTENANCE.md) for manual tests.

The existing `scripts/validate_site.py` is a more opinionated historical check and may need updating when current content or presentation rules change.

## GitHub Pages and caching

The repository uses relative links. Avoid root-absolute paths like `/css/styles.css`, which would point to the wrong location on a project Pages site. Shared styles may be referenced with version query strings; update them consistently if cache invalidation is required. GitHub Pages deployment settings are managed in the repository's **Settings > Pages** panel.
