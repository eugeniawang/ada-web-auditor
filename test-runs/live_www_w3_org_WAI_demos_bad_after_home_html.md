# ADA web accessibility audit (mechanical pass)

Generated 2026-09-11 19:34 by tools/audit.py. Standard: WCAG 2.1 Level A and AA as adopted by 28 CFR § 35.200(b) and applied by courts under 28 CFR § 36.303 (see reference/). Every finding below cites one success criterion whose verbatim text is in reference/wcag21-level-a-aa-success-criteria.md.

Severity key (rules.md): 🔴 CRITICAL blocks a task for some users · 🟠 SERIOUS major barrier · 🟡 MODERATE degrades but passable · 🔵 ADVISORY likely issue, criterion needs judgment · 🟢 PASS · ⚪ NEEDS HUMAN.

This is the mechanical pass only. It cannot see rendered styling, keyboard focus behaviour, dynamic content, or meaning. rules.md section 4 lists what a human must still check before calling a page conformant.


## https://www.w3.org/WAI/demos/bad/after/home.html

Page title: Welcome to CityLights! [Accessible Home Page]

Result: 0 FAIL · 9 PASS · 7 NEEDS HUMAN

- 🟢 **PASS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — html lang="en"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "Welcome to CityLights! [Accessible Home Page]"
- 🟢 **PASS** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — 10 img elements all carry an alt attribute (empty alt on decorative images is allowed)
- 🟢 **PASS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — 1 form controls all have an accessible name
- 🟢 **PASS** — WCAG 2.1 SC 3.3.2 Labels or Instructions (Level A) — 1 form controls all have a label or instruction
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 55 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — 23 ids, all unique
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 9 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (skip link)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://www.w3.org/WAI/demos/bad/after/home.html:13` — alt="W3C logo": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://www.w3.org/WAI/demos/bad/after/home.html:13` — alt="Web Accessibility Initiative (WAI) logo": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://www.w3.org/WAI/demos/bad/after/home.html:42` — alt="Citylights: your access to the city.": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://www.w3.org/WAI/demos/bad/after/home.html:42` — alt="Sunny Spells": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://www.w3.org/WAI/demos/bad/after/home.html:109` — alt="Free Penguins playing on stage": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://www.w3.org/WAI/demos/bad/after/home.html:112` — alt="Anemone-Snowdrop flower blooming": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.w3.org/WAI/demos/bad/after/home.html:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## Totals

FAIL: 0 · PASS: 9 · NEEDS HUMAN: 7

A page with zero FAIL in this report is not thereby conformant. It has passed the checks a program can run. See rules.md section 4.

