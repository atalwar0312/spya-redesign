# Contributing

Thanks for helping improve the SPYA redesign.

1. Create a branch from `main`.
2. Edit HTML pages in `pages/`. Shared styling, scripts, and images remain in `css/`, `js/`, and `assets/`.
3. Verify current SPYA program details and links before publishing.
4. Run `python3 scripts/stage_site.py` followed by `python3 scripts/check_structure.py`.
5. Preview the staged site: `python3 -m http.server 8000 --directory dist`.
6. Test mobile/desktop layout, keyboard navigation, and reduced-motion preferences.
7. Open a pull request titled with the next **Update N**; explain the change in the body.

Do not edit `dist/` or run the legacy `scripts/build_site.py`. Preserve relative links, accessible text, and SPYA branding. Avoid unnecessary decorative arrows, and do not claim that a registration form is open without checking.

See [Project structure](docs/PROJECT_STRUCTURE.md) and [Maintenance](docs/MAINTENANCE.md).
