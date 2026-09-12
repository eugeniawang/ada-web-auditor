# ADA web accessibility audit (mechanical pass)

Generated 2026-09-11 20:13 by tools/audit.py. Standard: WCAG 2.1 Level A and AA as adopted by 28 CFR § 35.200(b) and applied by courts under 28 CFR § 36.303 (see reference/). Every finding below cites one success criterion whose verbatim text is in reference/wcag21-level-a-aa-success-criteria.md.

Severity key (rules.md): 🔴 CRITICAL blocks a task for some users · 🟠 SERIOUS major barrier · 🟡 MODERATE degrades but passable · 🔵 ADVISORY likely issue, criterion needs judgment · 🟢 PASS · ⚪ NEEDS HUMAN.

This is the mechanical pass only. It cannot see rendered styling, keyboard focus behaviour, dynamic content, or meaning. rules.md section 4 lists what a human must still check before calling a page conformant.


## fixtures/partial-clinic.html

Page title: Riverbend Family Dental — Book an appointment

Result: 3 FAIL · 9 PASS · 2 NEEDS HUMAN

- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `fixtures/partial-clinic.html:24` — <select name="day" type="text"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🟡 **MODERATE** — WCAG 2.1 SC 1.3.5 Identify Input Purpose (Level AA) — `fixtures/partial-clinic.html:22` — <input name="phone"> collects user data but has no autocomplete attribute. Input purpose for a user-information field is not programmatically identified.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `fixtures/partial-clinic.html:32` — heading level jumps from h2 to h4 ("Hours"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🟢 **PASS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — html lang="en"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "Riverbend Family Dental — Book an appointment"
- 🟢 **PASS** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — 1 img elements all carry a text alternative (alt, aria-label, or aria-labelledby; empty alt on decorative images is allowed)
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 4 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — 2 ids, all unique
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 4 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — line 16: #5a5a5a on #ffffff = 6.90:1, meets 4.5:1
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width, initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (landmark only)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/partial-clinic.html:30` — alt="Office": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `fixtures/partial-clinic.html:31` — link text "Read more": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.

## Totals

FAIL: 3 · PASS: 9 · NEEDS HUMAN: 2

A page with zero FAIL in this report is not thereby conformant. It has passed the checks a program can run. See rules.md section 4.

