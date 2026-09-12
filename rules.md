# Rules

How the ADA web auditor audits: the order, the citation form, the severity classes, and what stays with a human.

## 1. Order of work

1. **Identify the artifact and the regime.** Note the URL or file, the date, and whether the owner is a public entity (Title II, 28 CFR § 35.200 applies directly) or a private business open to the public (Title III, 28 CFR § 36.303; WCAG 2.1 AA applied by courts, not codified). Say which one at the top of the report. If unknown, say so and audit against WCAG 2.1 AA regardless; the criteria are the same.
2. **Run the mechanical pass.** `python3 tools/audit.py <file-or-url> --html reports/<name>.html -o reports/<name>.md`. It runs the deterministic checks in section 5 and writes two reports: the HTML one a person reads (plain-English rule name, colour-coded class, location, measurement, then the WCAG criterion and the ADA section with the full text one click away) and the markdown one the checker validates. Standard library only; nothing to install.
3. **Do the human pass.** Open the page. Walk section 4 and turn each NEEDS HUMAN line into PASS or FAIL, keeping the citation and adding a location. Add findings for criteria the scanner cannot reach at all (section 4 lists them).
4. **Validate.** `python3 tools/check_audit.py reports/<name>.md`. It refuses any report whose citations are not in `reference/`, whose FAILs lack a location or severity, or that omits PASS and FAIL totals. A report that does not pass the checker is not delivered.
5. **Write the summary.** Three lines at most: what was audited, the FAIL/PASS/NEEDS HUMAN counts, and the single most severe finding.

## 2. Citation form

Every finding cites exactly one success criterion in this form, which is the form the checker validates:

`WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA)`

The number, the name, and the level must match the heading in `reference/wcag21-level-a-aa-success-criteria.md` character for character. The regulation is cited beside it. For a government site (Title II) it is `28 CFR § 35.200(b)(1)` for every criterion, because that paragraph requires WCAG 2.1 A/AA outright. For a business (Title III) the regulation names no web standard, so the citation is the duty the criterion serves: `28 CFR § 36.303(c)(1)` (effective communication) for 1.1.1, 1.2.2, 1.4.2, 2.4.2, 2.4.4, 3.1.1, 3.3.2 and 4.1.2; `28 CFR § 36.303(a)` (the general auxiliary-aids duty) for everything else. Every cited paragraph must exist in the reference CFR files; the checker enforces this.

A finding that also implicates a second criterion says so in its note ("Also fails SC 3.3.2"), but the line cites one. One line, one provision, one location.

Level AAA criteria are never cited. No cited regulation requires them and they are not in `reference/`.

## 3. Finding shape

In the HTML report each finding reads, in this order: the class (colour and word), the rule in plain words ("Images need a text description"), where on the page, what was measured, one sentence on what it means for a person, then the citation line: `Rule: WCAG 2.1 SC 1.1.1 Non-text Content (Level A) · ADA law: 28 CFR § 36.303(c)(1)` with a "see the full text" link that slides out both provisions verbatim from `reference/`. The ADA section is § 36.303(c)(1) for a business (Title III) or § 35.200(b) for a government site (Title II, `--regime title2`).

In the markdown report, which the checker validates, the line is:

`- <mark> **<CLASS>** — <citation> — \`<file-or-url>:<line>\` — <what was measured, with the number where there is one>. <one sentence on why it fails or what to confirm>.`

Example: `- 🟠 **SERIOUS** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — \`fixtures/bad-store.html:18\` — <p> text #999999 on #ffffff = 2.85:1, below 4.5:1. Contrast below the minimum for normal text.`

The location is a line number in the served HTML, or a CSS selector when a line is not meaningful (rendered content). The measured value is the fact a stranger can reproduce: the ratio, the missing attribute, the element.

## 4. Severity classes

Four failure classes plus two non-failure marks. The colour is part of the class and appears on every line.

| Mark | Class | Meaning |
|---|---|---|
| 🔴 | **CRITICAL** | Blocks a task for some users outright: an unlabeled form field, any `img` with no text alternative at all (linked or not, since the scanner cannot tell a product photo from decoration and a missing alt is never a conscious choice), a button or frame with no name, a video with no captions, audio that autoplays with no control. An alt that is a filename is SERIOUS, because something was written and it is wrong. |
| 🟠 | **SERIOUS** | A major barrier the user can sometimes work around: contrast below minimum, no page language, zoom disabled, no skip mechanism, a mouse-only control. |
| 🟡 | **MODERATE** | Degrades the experience but the task is still passable: duplicate ids, missing autocomplete on a user-data field. |
| 🔵 | **ADVISORY** | The scanner found a strong signal, but the criterion itself is about a result a human must confirm: a skipped heading level, a positive tabindex. Advisory findings count as FAIL in totals and are labelled so the reader knows the confidence. |
| 🟢 | **PASS** | The criterion was tested and met, with what was checked. |
| ⚪ | **NEEDS HUMAN** | The scanner cannot decide. The line carries the exact question. Never a guess. |

Severity describes user impact, not legal risk. The auditor does not rank findings by how often they appear in complaints.

## 5. What the mechanical pass tests

Deterministic, standard-library checks. Each maps to one criterion.

| Check | Criterion |
|---|---|
| `html` has a `lang` | 3.1.1 |
| `<title>` present and non-empty | 2.4.2 |
| Every `img` has an `alt`, `aria-label`, or `aria-labelledby` (or is `role="presentation"`/`aria-hidden`); alt is not a filename | 1.1.1 |
| Every visible text input, select, textarea has a `label for`, a wrapping `label`, aria-label, aria-labelledby, or title | 4.1.2 (also 3.3.2) |
| Every link has text, aria-label, or image alt | 2.4.4 |
| Every button has text or aria-label; every iframe has a title | 4.1.2 |
| ids are unique | 4.1.1 |
| Headings exist as heading elements; skipped levels flagged | 1.3.1 |
| Inline `color` and `background(-color)` pairs measured against 4.5:1 (3:1 for large text: 18pt, or 14pt bold, taken here as 24px or 18pt). Ratio = (L1 + 0.05) / (L2 + 0.05) where L is relative luminance: each sRGB channel c/255, then c/12.92 if c ≤ 0.03928 else ((c+0.055)/1.055)^2.4, and L = 0.2126 R + 0.7152 G + 0.0722 B. This is WCAG's own definition of "contrast ratio" and "relative luminance", verbatim in `reference/wcag21-definitions-contrast-and-luminance.md`; an unaided auditor uses the same formula | 1.4.3 |
| Viewport does not disable or cap zoom below 200% | 1.4.4 |
| `video` has a captions or subtitles track | 1.2.2 |
| `video`/`audio` with autoplay has controls or is muted | 1.4.2 |
| No `meta refresh` | 2.2.1 |
| `onclick` on a non-focusable element with no key handler; hover handlers with no focus handler | 2.1.1 |
| Positive `tabindex` | 2.4.3 |
| Skip link or `main`/`nav` landmark present. With neither, a page with 5 or more links is FAIL (a repeated navigation block is near-certain); fewer is NEEDS HUMAN, because the scanner sees one page and the criterion is about blocks repeated across pages | 2.4.1 |
| User-data fields carry `autocomplete` | 1.3.5 |

## 6. What only a human can test

The scanner never claims these. The human pass must cover them before a page is called conformant:

- 1.4.3 contrast set in stylesheets or on images of text (use a browser tool or a colour picker; record the measured ratio).
- 1.4.11 non-text contrast of controls and focus indicators.
- 2.1.1 and 2.1.2: tab through the whole page; every control reachable and operable, no keyboard trap.
- 2.4.7 focus visible on every focusable element.
- 1.3.1 and 1.3.2: does the programmatic structure match the visual one; is reading order sensible.
- 1.1.1 meaning: does each alt text serve the same purpose as the image.
- 2.4.4 generic link text ("Read more") in context.
- 1.4.10 reflow at 320 CSS px without two-dimensional scrolling.
- 1.4.13 content on hover or focus dismissable, hoverable, persistent.
- 4.1.3 status messages announced.
- 3.3.1, 3.3.3, 3.3.4: form error identification, suggestion, and prevention.
- Controls hidden only by CSS (`display:none` in a stylesheet or inline): the scanner still counts them, since it cannot see CSS. `hidden` and `aria-hidden="true"` are honoured.
- Anything injected after load (widgets, overlays, single-page app routes). The scanner reads served HTML only.

## 7. What the auditor refuses to do

- Certify conformance from the mechanical pass alone. Zero FAIL means the program found nothing; it does not mean the page conforms.
- Cite a criterion, regulation, or level not present in `reference/`.
- State legal outcomes. "This will get you sued" and "this is safe" are both outside the standard.
- Audit a live third party's site and publish the result under their name. Audit your own pages, your clients' pages with permission, or fixtures.
