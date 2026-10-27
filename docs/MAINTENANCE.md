# Maintenance and release checklist

## Local development

```bash
git switch main
git pull origin main
git switch -c update-11
# Edit pages/*.html, css/styles.css, js/app.js, etc.
python3 scripts/stage_site.py
python3 scripts/check_structure.py
python3 -m http.server 8000 --directory dist
```

Review the website at http://localhost:8000. All HTML pages stay together in `pages/`, but the local preview and published site use normal root URLs (like `sports.html`).

Every time you edit source content, re-run `stage_site.py` before reviewing `dist/`.

## Pull request checks

- [ ] Site staging and structural validation pass
- [ ] Home page and each major navigation page display at desktop and mobile sizes
- [ ] Current-page highlight appears only on the correct navigation tab
- [ ] The mobile menu is operable with keyboard and touch
- [ ] Sports search filters and counts results
- [ ] Registration TeamSnap links point to the intended program
- [ ] No outdated claims about registration availability, fees, leadership, or events
- [ ] Reduced-motion preferences are respected
- [ ] Images have appropriate alternate text and usage rights
- [ ] No unexpected styling/asset changes or root-absolute links

Pull request titles should be compact, e.g. **Update 11**. Put change details and testing notes in the description.

## Publishing

**This layout requires GitHub Pages Source = GitHub Actions.** Configure it in GitHub repository Settings > Pages > Build and deployment. The `Publish website` workflow stages and deploys `dist/` on a push to `main`. Do not merge Update 10 while Pages is still configured for branch/root publishing.

After merging, check the GitHub Actions run, then test:

- https://atalwar0312.github.io/spya-redesign/
- https://atalwar0312.github.io/spya-redesign/sports.html
- https://atalwar0312.github.io/spya-redesign/registration.html

If the site appears unchanged, check the workflow and Pages settings rather than adding more CSS overrides. Browser cache may also affect presentation; opening a private browser window helps.

## Legacy generator

Never run `scripts/build_site.py` during ordinary editing. It belongs to an earlier design and can overwrite the current HTML. Use `scripts/stage_site.py` instead, which only copies source files into the ignored output folder.
