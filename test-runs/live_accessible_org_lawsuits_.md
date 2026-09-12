# ADA web accessibility audit (mechanical pass)

Generated 2026-09-11 19:35 by tools/audit.py. Standard: WCAG 2.1 Level A and AA as adopted by 28 CFR § 35.200(b) and applied by courts under 28 CFR § 36.303 (see reference/). Every finding below cites one success criterion whose verbatim text is in reference/wcag21-level-a-aa-success-criteria.md.

Severity key (rules.md): 🔴 CRITICAL blocks a task for some users · 🟠 SERIOUS major barrier · 🟡 MODERATE degrades but passable · 🔵 ADVISORY likely issue, criterion needs judgment · 🟢 PASS · ⚪ NEEDS HUMAN.

This is the mechanical pass only. It cannot see rendered styling, keyboard focus behaviour, dynamic content, or meaning. rules.md section 4 lists what a human must still check before calling a page conformant.


## https://accessible.org/lawsuits/

Page title: Chat icon

Result: 0 FAIL · 10 PASS · 5 NEEDS HUMAN

- 🟢 **PASS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — html lang="en-US"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "Chat icon"
- 🟢 **PASS** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — 4 img elements all carry an alt attribute (empty alt on decorative images is allowed)
- 🟢 **PASS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — 12 form controls all have an accessible name
- 🟢 **PASS** — WCAG 2.1 SC 3.3.2 Labels or Instructions (Level A) — 12 form controls all have a label or instruction
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 73 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — 77 ids, all unique
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 26 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width, initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (skip link)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://accessible.org/lawsuits/:221` — alt="Accessible.org": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://accessible.org/lawsuits/:252` — alt="Accessible.org": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://accessible.org/lawsuits/:1339` — alt="Kris Rivenburgh, Founder of Accessible.org holding his new Published Book.": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://accessible.org/lawsuits/:2114` — alt="Accessible.org": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://accessible.org/lawsuits/:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## Totals

FAIL: 0 · PASS: 10 · NEEDS HUMAN: 5

A page with zero FAIL in this report is not thereby conformant. It has passed the checks a program can run. See rules.md section 4.

