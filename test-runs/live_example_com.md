# ADA web accessibility audit (mechanical pass)

Generated 2026-09-11 19:34 by tools/audit.py. Standard: WCAG 2.1 Level A and AA as adopted by 28 CFR § 35.200(b) and applied by courts under 28 CFR § 36.303 (see reference/). Every finding below cites one success criterion whose verbatim text is in reference/wcag21-level-a-aa-success-criteria.md.

Severity key (rules.md): 🔴 CRITICAL blocks a task for some users · 🟠 SERIOUS major barrier · 🟡 MODERATE degrades but passable · 🔵 ADVISORY likely issue, criterion needs judgment · 🟢 PASS · ⚪ NEEDS HUMAN.

This is the mechanical pass only. It cannot see rendered styling, keyboard focus behaviour, dynamic content, or meaning. rules.md section 4 lists what a human must still check before calling a page conformant.


## https://example.com

Page title: Example Domain

Result: 0 FAIL · 5 PASS · 3 NEEDS HUMAN

- 🟢 **PASS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — html lang="en"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "Example Domain"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 1 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 1 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width, initial-scale=1" does not block zoom
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `https://example.com:1` — link text "Learn more": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://example.com:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — `https://example.com:1` — no skip link or landmark, but only 1 links. SC 2.4.1 applies to blocks repeated on multiple pages; a human must say whether any exist.

## Totals

FAIL: 0 · PASS: 5 · NEEDS HUMAN: 3

A page with zero FAIL in this report is not thereby conformant. It has passed the checks a program can run. See rules.md section 4.

