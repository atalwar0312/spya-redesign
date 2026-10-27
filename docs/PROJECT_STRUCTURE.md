# Project structure

The website is organized to keep the GitHub repository compact while preserving the public page addresses visitors already use.

```text
spya-redesign/
├── pages/                       All 17 HTML pages (source)
│   ├── index.html               Homepage
│   ├── sports.html              Sports directory
│   ├── registration.html        Registration hub
│   ├── resources.html           Family resources
│   ├── community.html           Community
│   ├── about.html               About SPYA
│   ├── calendar.html            Calendar
│   ├── 404.html                 Error page
│   └── [nine sports].html       Sport-specific pages
├── assets/images/               Logos and photos
├── css/styles.css               Global design
├── js/app.js                    Site interactions
├── data/                        Content data and asset manifest
├── scripts/
│   ├── stage_site.py            Assemble the published website
│   ├── check_structure.py       Validate assembled links and pages
│   ├── build_site.py            Legacy generator (disabled by default)
│   └── download_assets.py       Existing asset utility
├── docs/                        Developer instructions
├── .github/workflows/           Tests and GitHub Pages deployment
├── README.md                    Overview
├── CONTRIBUTING.md             Contribution guide
└── .gitignore
```

## Source and publishing

**Edit HTML in `pages/`.** Site assets remain in top-level `assets/`, `css/`, and `js/`. The HTML files intentionally retain their existing relative asset paths (for example `css/styles.css`).

Run:

```bash
python3 scripts/stage_site.py
python3 scripts/check_structure.py
python3 -m http.server 8000 --directory dist
```

The first command copies `pages/*.html`, `assets/`, `css/`, and `js/` into a temporary, ignored `dist/` folder. It **does not alter source files**. The second command validates that published layout. The third opens a local preview at http://localhost:8000.

GitHub Actions uses the same staging process to publish the files from `dist/` to the root of GitHub Pages. This preserves existing URLs such as `/spya-redesign/sports.html` rather than switching them to `/spya-redesign/pages/sports.html`.

### Required GitHub Pages setting

For the new layout to publish, set **Settings > Pages > Build and deployment > Source = GitHub Actions** before merging Update 10. The new `Publish website` workflow deploys the output. If the repository remains configured to publish from a branch/root, the site will lose its homepage after the merge.

## What to edit

| Goal | File |
| --- | --- |
| Homepage | `pages/index.html` |
| Navigation and page content | `pages/*.html` |
| Sports program pages | `pages/[sport].html` |
| Styling and animations | `css/styles.css` |
| Search and mobile navigation | `js/app.js` |
| Images | `assets/images/` |
| Build and checks | `scripts/stage_site.py`, `scripts/check_structure.py` |
| Deployment | `.github/workflows/pages.yml` |

## Safety notes

- Avoid moving the `css/`, `js/`, or `assets/` source directories without updating staging and asset links.
- `scripts/build_site.py` is a legacy generator from an earlier design and remains disabled by default because it can overwrite current pages. Do not run it during normal editing.
- `data/site.json` and `data/assets.json` include historical structured content; current HTML in `pages/` is authoritative for the prototype.
- `dist/` is generated and ignored by Git. Never edit or commit it.
