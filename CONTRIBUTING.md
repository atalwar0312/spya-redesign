# Contributing to the SPYA redesign

Thank you for helping improve the South Parkland Youth Association website prototype.

## Principles

Make it easy for families to find accurate information. Keep layouts consistent, the site accessible, and the implementation lightweight. Use concise link labels without decorative arrows.

## Proposing changes

1. Open a branch from `main`.
2. Edit only the files needed for your change.
3. Preserve the existing root HTML page names and relative URLs.
4. Run `python3 scripts/check_structure.py`.
5. Test the affected pages at desktop and mobile widths.
6. Open a pull request using the repository template.

Pull request titles use short sequential names such as **Update 9**. Put the purpose, affected pages, screenshots (if applicable), and test notes in the pull request description.

## Code and content conventions

- Use semantic HTML, appropriate `alt` attributes, and explicit `aria-current` on the active navigation link.
- Prefer shared rules in `css/styles.css` instead of page-specific style overrides.
- Respect `prefers-reduced-motion`; do not make animation necessary for accessing content.
- Keep JavaScript dependency-free unless there is a clear need.
- Use relative links for internal pages and assets so GitHub Pages project hosting works.
- Never advertise registration as open without recent verification from SPYA or TeamSnap.
- Review SPYA policies, program contacts, and board names against official sources.
- Avoid changing copyrighted images or logos without permission.

## Build safety

`scripts/build_site.py` is a legacy HTML generator that can overwrite the redesigned pages. **Do not run it during ordinary editing.** Refer to [Project structure](docs/PROJECT_STRUCTURE.md) for context.

## Useful documentation

- [README](README.md)
- [Project structure](docs/PROJECT_STRUCTURE.md)
- [Maintenance and QA](docs/MAINTENANCE.md)

This is a community-focused prototype; contribution acceptance does not imply official SPYA endorsement.
