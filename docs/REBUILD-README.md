# SPYA Polished Update

This package updates https://atalwar0312.github.io/spya-redesign/.
It has not been uploaded to your GitHub account by the assistant.

## Publish From Your Mac

1. Save `SPYA-Polished-Update.zip` in `Desktop/Draft - 1`.
2. Run:

```bash
(
  set -e
  cd "$HOME/Desktop/Draft - 1"
  unzip -o "SPYA-Polished-Update.zip" -d "polished-update"
  bash "polished-update/spya-polished/publish.command"
)
```

The script downloads SPYA images, rebuilds and validates the pages, creates a fresh checkout on your Desktop, and commits and pushes to `atalwar0312/spya-redesign` on `main`. It uses the Git authentication already set up on your Mac. No force push; earlier versions remain in Git history. It preserves unrelated repository files. Your existing GitHub Pages configuration remains unchanged. Wait for its deployment to finish, then refresh the website.

If an image download fails, the build uses its original SPYA image URL and prints the affected file. That image then depends on the source website remaining available.

## Preview Without Publishing

From the extracted `spya-polished` folder:

```bash
python3 scripts/download_assets.py
python3 scripts/build_site.py
python3 scripts/validate_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000 in your browser. This preview address is local to your computer. Stop it with Control-C.

## Update Content

- `data/site.json`: sports, program descriptions, contacts.
- `data/assets.json`: original SPYA assets and local filenames.
- `scripts/build_site.py`: page layout, registration statuses, event dates, community content.
- `css/styles.css`: responsive layout and visual design.
- `js/app.js`: mobile menu, sport search, dated-announcement expiry.
- `docs/CONTENT-REVIEW.md`: verified scope and remaining uncertainties.
- `docs/CONTENT-MAP.md`: disposition of the supplied source pages.

Run the builder after editing data or templates. Generated HTML is the publication output.

## Editorial Rules

Each main task has one navigation item. The footer does not repeat navigation. Registration forms appear on Registration only; raffle entry appears on Home only. Program email contacts may appear in a registration row because they serve the specific task of obtaining a current form.

Headings use Title Case. Body text uses sentence case. SPYA, NFL, PYL, and other initialisms keep their proper capitalization. No CSS all-caps transformation.

Past achievements are retained with their years. Expired promotions are omitted. The raffle is excluded by the builder from November 8, 2026 (Eastern Time), conservatively at the start of drawing day; the actual entry cutoff has not been verified. JavaScript also removes it from older generated pages after that time. With JavaScript disabled, an old deployment will need rebuilding to remove dated content. Rebuild regularly and review forms manually; this is a static site, not a live registration feed.

## Review Before Presenting

Structural checks pass. A full visual/mobile/screen-reader review of this new build was not completed in the assistant environment. Check the published site at phone and desktop widths, menu keyboard behavior, calendar display, photo loading, and current TeamSnap form destinations. No form was submitted and no payment was attempted.
