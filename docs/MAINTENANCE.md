# Maintenance and release guide

A practical checklist for maintaining the SPYA prototype without breaking current pages.

## Before editing

1. Pull the latest `main`.
2. Create a branch with a short, numbered update name (for example `update-10`).
3. Identify which pages are affected; keep public filenames and their links stable.
4. Confirm all changing association details against [spya.org](https://spya.org/).
5. Do **not** run the legacy `scripts/build_site.py` generator; it was created for an earlier design and overwrites root HTML files.

## Typical editing workflow

```bash
git switch main
git pull origin main
git switch -c update-10

# Edit the required HTML/CSS/JS files

python3 scripts/check_structure.py
python3 -m http.server 8000
```

Review locally at `http://localhost:8000`. Open a pull request titled **Update 10** or the next available number. Describe the actual changes **in the PR body**, not the title.

## Desktop and mobile QA

- [ ] Homepage, Sports, Registration, Families, Community, and About load successfully.
- [ ] Each individual sport card opens its expected page.
- [ ] The selected navigation item highlights only on its own page. In particular, Registration must not have a special oval/pill on unrelated pages.
- [ ] Mobile menu opens and closes; Escape dismisses it; links remain usable.
- [ ] Sports search filters results correctly.
- [ ] Links and buttons have discernible names and visible keyboard focus.
- [ ] Images display properly and provide suitable alternative text.
- [ ] Text is readable and content does not overflow at mobile widths.
- [ ] Scroll animations do not hide essential content and honor **Reduce Motion**.
- [ ] No unnecessary decorative arrows appear on buttons or navigation.
- [ ] If CSS changes, confirm the newly deployed version loads without stale cached styles.

## Content checks

- [ ] Registration links resolve to the intended TeamSnap forms; do **not** infer that registration is accepting entries merely because a form loads.
- [ ] Featured dates and promotions are not expired.
- [ ] Program divisions, ages, seasons, and commissioner emails are current.
- [ ] Association board names and contact details match official announcements.
- [ ] Financial assistance and bylaws documents point to the current appropriate editions.
- [ ] Images are appropriate and their use is authorized.

## Before merging

```bash
python3 scripts/check_structure.py
```

Review the GitHub checks, diff, and rendered site. Keep `main` as the stable publishing source and merge only when the changes have been reviewed.

## After merging

1. Confirm the pull request was merged.
2. Open the [live GitHub Pages site](https://atalwar0312.github.io/spya-redesign/).
3. Check the homepage and the changed pages in a private browser window.
4. Verify **Settings > Pages** points to the intended source/branch if updates don't appear.
5. If old CSS persists, inspect the browser's Network tab for the actual stylesheet URL and response before adding further overrides.

## Release boundaries

- This repository is an **independent redesign/prototype**, not the authoritative site for SPYA operations.
- Avoid publishing unverified registration claims, personally identifying youth-athlete details, or third-party imagery without permission.
- Do not include local exports, credentials, environment files, or temporary staging folders in commits.
