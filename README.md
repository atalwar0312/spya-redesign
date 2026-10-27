<div align="center">

<img src="assets/images/logo.png" alt="South Parkland Youth Association logo" width="110">

# South Parkland Youth Association
### A place to play. A team to belong to.

**A modern, responsive website redesign for SPYA, a volunteer-powered youth sports association serving the Allentown, Pennsylvania community.**

[**Explore the live redesign**](https://atalwar0312.github.io/spya-redesign/) · [Official SPYA website](https://spya.org/) · [View the code](https://github.com/atalwar0312/spya-redesign)

</div>

---

## Overview

The **SPYA Website Redesign** is a community-focused front-end project built to make youth sports information easier to discover and navigate. It gives families a clear starting point for sports programs, registration, financial assistance, association contacts, and community activities.

Rather than requiring visitors to hunt through multiple pages, the redesign prioritizes three simple questions:

1. **What can my child play?** Find SPYA's nine sports and explore each program.
2. **How do we get started?** Find registration resources and links to the relevant TeamSnap forms.
3. **How can we participate?** Learn about financial assistance, volunteering, leadership, and community events.

The result is a lightweight website with a stronger visual identity, accessible interactions, and layouts designed for both mobile and desktop visitors.

> **Project status:** This repository is an independent website redesign/prototype. It is **not** the official SPYA website. For authoritative announcements, registration availability, eligibility, and program policies, refer to [spya.org](https://spya.org/) and the linked registration provider.

## Website preview

<div align="center">
  <img src="assets/images/legion.jpg" alt="South Parkland Senior Legion baseball championship team featured on the homepage" width="760">
  <p><sub>Real SPYA team photography used in the redesign.</sub></p>
</div>

**[Visit the redesigned website](https://atalwar0312.github.io/spya-redesign/)**

## Highlights

| Area | What it offers |
| --- | --- |
| **Modern homepage** | Large typography, athlete photography, a clear mission statement, prominent next steps, and featured association announcements. |
| **Nine sports** | A searchable sports directory with individual program pages and contact information. |
| **Registration hub** | Seasonal registration information and links to TeamSnap, with reminders to confirm actual form availability. |
| **Family resources** | Financial assistance policy and application, volunteer information, common questions, and association documents. |
| **Community** | Championship highlights, event/calendar access, and links to SPYA social channels. |
| **About & leadership** | Association mission, location, executive-board contacts, and links to current official information. |
| **Motion & interaction** | Subtle entrance animations, scroll reveals, hover feedback, and an accessible mobile navigation menu. |
| **Responsive design** | Fluid layouts for smaller phones, tablets, laptops, and larger screens. |

### Sports at SPYA

The sports directory includes:

| | | |
| --- | --- | --- |
| Baseball | Basketball | Cheer |
| Field Hockey | Football | Lacrosse |
| NFL Flag | Soccer | Softball |

Every sports page should be treated as a guide, not as a guarantee that registration is currently open. Program dates and arrangements can change between seasons.

## Design philosophy

The visual direction is **confident, welcoming, and community-centered**.

- **Athletes first:** Authentic youth-sports photography and strong headlines give the site a human focus.
- **Clear paths:** Visitors can reach Sports, Registration, Families, Community, and About through a consistent main navigation.
- **SPYA identity:** The existing association logo and a restrained red, dark-green, and neutral palette anchor the design.
- **Purposeful motion:** Transitions should make navigation feel polished without distracting users from essential information.
- **Simple, readable controls:** Buttons and text links communicate their destination without unnecessary decorative arrows.
- **Accessibility-conscious choices:** Semantic markup, a skip-to-content link, keyboard focus styles, descriptive image text, and reduced-motion behavior.

### Accessibility and performance considerations

The implementation includes accessibility-minded features, but **it has not been certified against a particular WCAG conformance level**.

- Navigation uses semantic links and `aria-current` on the active page.
- The mobile menu exposes its expanded state using `aria-expanded`, and supports Escape to close.
- The sports search reports the visible result count.
- Scroll effects use `IntersectionObserver` when available and avoid running for users who prefer reduced motion.
- Images use responsive sizing and lazy loading where appropriate.
- The website uses plain HTML, CSS, and JavaScript without a required application framework.

## Technology stack

| Technology | Role |
| --- | --- |
| **HTML5** | Page structure, content, navigation, and semantic markup |
| **CSS3** | Responsive layouts, typography, visual identity, hover states, and animations |
| **Vanilla JavaScript** | Mobile navigation, sports filtering, announcement expiry, and scroll reveals |
| **Git & GitHub** | Source control and collaborative review |
| **GitHub Pages** | Static-site publishing |
| **TeamSnap** | External registration forms linked from the website |

No package installation, bundler, or JavaScript framework is required to view the static pages locally.

## Repository layout

All 17 HTML pages live in a single **`pages/`** folder. Published URLs stay unchanged because a lightweight deployment step assembles the public website into `dist/`.

```text
spya-redesign/
├── pages/                   # All 17 HTML pages, including sports
├── assets/images/           # Team photography and logo
├── css/styles.css           # Styles and motion
├── js/app.js                # Site interactions
├── data/                    # Content sources and asset records
├── scripts/                 # Site staging and validation
├── docs/                    # Architecture and maintenance
├── .github/workflows/       # Checks and deployment
├── CONTRIBUTING.md
└── README.md
```

**[Full project structure](docs/PROJECT_STRUCTURE.md)** · **[Maintenance guide](docs/MAINTENANCE.md)** · **[Contributing](CONTRIBUTING.md)**

The `dist/` folder is generated automatically and is not committed.

## Getting started

### Option A: View online

Open the **[live demo](https://atalwar0312.github.io/spya-redesign/)**. No installation is required.

### Option B: Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/atalwar0312/spya-redesign.git
   cd spya-redesign
   ```

2. Assemble and validate the website:

   ```bash
   python3 scripts/stage_site.py
   python3 scripts/check_structure.py
   ```

3. Preview the published layout:

   ```bash
   python3 -m http.server 8000 --directory dist
   ```

4. Visit **http://localhost:8000**.

Edit source pages inside `pages/` and re-run the staging script after each change.

## Deployment

The [live demo](https://atalwar0312.github.io/spya-redesign/) is deployed on GitHub Pages.

**Deployment source must be set to GitHub Actions** in **Settings > Pages > Build and deployment**. The `Publish website` workflow automatically copies all HTML pages from `pages/`, along with CSS, JavaScript, and images, into `dist/` and deploys that directory.

The deployed pages remain at their original public addresses, such as `/spya-redesign/sports.html`. **Do not configure Pages to publish from the repository root** after this layout migration.

For each change:

1. Create a new branch and edit source files.
2. Run `python3 scripts/stage_site.py` and `python3 scripts/check_structure.py`.
3. Review the locally staged site and open a pull request.
4. Merge after review and check the **Publish website** GitHub Actions run.
5. Verify the live site and its links.

For more detail, see the [release checklist](docs/MAINTENANCE.md).

## Content maintenance

Youth sports details are time-sensitive. The site should be reviewed at the start of each season and whenever SPYA publishes an announcement.

| Content | Maintenance check |
| --- | --- |
| Registration | Verify TeamSnap form URLs, dates, and whether the forms still accept registrations. |
| Sports pages | Confirm divisions, seasons, commissioner contacts, and equipment information. |
| Leadership | Compare names and email contacts with SPYA's official board page. |
| Financial assistance | Confirm that the policy and application link to the newest published versions. |
| Featured announcements | Remove or replace expired dates, events, and promotions. |
| Photos | Confirm appropriate permission and attribution for published team imagery. |
| Navigation & layout | Test links, responsive views, and active navigation states after edits. |

**Source of truth:** [Official SPYA website](https://spya.org/). The redesign is an informational prototype and should not be treated as a replacement for official program communications.

## Contribution and review

Feedback is welcome, especially around clarity for families, accessibility, mobile usability, visual consistency, and information accuracy.

For contributions, edit pages inside `pages/`, run the staging and validation scripts, and submit a pull request with review notes. Keep pull request titles short—**Update 10**, **Update 11**, and so on—and put detailed explanations inside the pull request body. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Project goals

- Make it easy for a parent to find the right program.
- Reduce friction between discovering a sport and finding registration information.
- Represent SPYA's community, volunteers, and achievements with care.
- Provide an appealing prototype that can be reviewed by stakeholders and board members.
- Keep the website maintainable without adding unnecessary technical complexity.

## Credits and acknowledgments

- **South Parkland Youth Association:** The community, sports programs, association identity, and information that inspired the redesign.
- **SPYA athletes, coaches, families, and volunteers:** The people at the heart of the website's story.
- **Website redesign:** Developed and maintained in this repository by [atalwar0312](https://github.com/atalwar0312).

SPYA's logo, photographs, and other association assets belong to their respective owners. Their presence in this prototype does not imply an endorsement or transfer of rights. External links such as TeamSnap and the official SPYA website are operated independently.

---

<div align="center">

### More than a game. A place to belong.

Made with care for the South Parkland youth sports community.

**[Live website](https://atalwar0312.github.io/spya-redesign/)** · **[Official SPYA](https://spya.org/)**

</div>
