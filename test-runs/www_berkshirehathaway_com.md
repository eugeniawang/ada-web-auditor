# ADA web accessibility audit (mechanical pass)

Generated 2026-09-11 20:14 by tools/audit.py. Standard: WCAG 2.1 Level A and AA as adopted by 28 CFR § 35.200(b) and applied by courts under 28 CFR § 36.303 (see reference/). Every finding below cites one success criterion whose verbatim text is in reference/wcag21-level-a-aa-success-criteria.md.

Severity key (rules.md): 🔴 CRITICAL blocks a task for some users · 🟠 SERIOUS major barrier · 🟡 MODERATE degrades but passable · 🔵 ADVISORY likely issue, criterion needs judgment · 🟢 PASS · ⚪ NEEDS HUMAN.

This is the mechanical pass only. It cannot see rendered styling, keyboard focus behaviour, dynamic content, or meaning. rules.md section 4 lists what a human must still check before calling a page conformant.


## https://www.berkshirehathaway.com/

Page title: BERKSHIRE HATHAWAY INC.

Result: 2 FAIL · 3 PASS · 3 NEEDS HUMAN

- 🟠 **SERIOUS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — `https://www.berkshirehathaway.com/:1` — no skip link and no main/nav landmark or role; page has 18 links. No mechanism to bypass what is almost certainly a repeated navigation block. Confirm the block repeats across pages.
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.berkshirehathaway.com/:11` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "BERKSHIRE HATHAWAY INC."
- 🟢 **PASS** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — 1 img elements all carry a text alternative (alt, aria-label, or aria-labelledby; empty alt on decorative images is allowed)
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 18 links all have a text, aria-label, or image alt
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `https://www.berkshirehathaway.com/:120` — alt="GEICO logo": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.berkshirehathaway.com/:1` — no heading elements at all. If the page visually has section titles, that is a 1.3.1 failure; a human must look.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.berkshirehathaway.com/:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## https://www.berkshirehathaway.com/message.html

Page title: (none)

Result: 0 FAIL · 0 PASS · 1 NEEDS HUMAN

- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.berkshirehathaway.com/message.html:1` — could not fetch or read this page (ValueError: server sent br compression, which the Python standard library cannot decode; save the page from a browser (File > Save Page As, HTML only) and pass the file). Nothing was audited.

## https://www.berkshirehathaway.com/reports.html

Page title: (none)

Result: 0 FAIL · 0 PASS · 1 NEEDS HUMAN

- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.berkshirehathaway.com/reports.html:1` — could not fetch or read this page (ValueError: server sent br compression, which the Python standard library cannot decode; save the page from a browser (File > Save Page As, HTML only) and pass the file). Nothing was audited.

## https://www.berkshirehathaway.com/news/2026news.html

Page title: 2026 News Menu

Result: 2 FAIL · 4 PASS · 2 NEEDS HUMAN

- 🟠 **SERIOUS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — `https://www.berkshirehathaway.com/news/2026news.html:1` — no skip link and no main/nav landmark or role; page has 37 links. No mechanism to bypass what is almost certainly a repeated navigation block. Confirm the block repeats across pages.
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.berkshirehathaway.com/news/2026news.html:11` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "2026 News Menu"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 37 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — 1 ids, all unique
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 1 headings present as heading elements
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.berkshirehathaway.com/news/2026news.html:24` — page has headings but no h1. WCAG 2.1 does not require an h1; a human should confirm the visual structure is conveyed programmatically.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.berkshirehathaway.com/news/2026news.html:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## https://www.berkshirehathaway.com/sharehold.html

Page title: (none)

Result: 0 FAIL · 0 PASS · 1 NEEDS HUMAN

- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.berkshirehathaway.com/sharehold.html:1` — could not fetch or read this page (ValueError: server sent br compression, which the Python standard library cannot decode; save the page from a browser (File > Save Page As, HTML only) and pass the file). Nothing was audited.

## https://www.berkshirehathaway.com/letters/letters.html

Page title: (none)

Result: 0 FAIL · 0 PASS · 1 NEEDS HUMAN

- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.berkshirehathaway.com/letters/letters.html:1` — could not fetch or read this page (ValueError: server sent br compression, which the Python standard library cannot decode; save the page from a browser (File > Save Page As, HTML only) and pass the file). Nothing was audited.

## https://www.berkshirehathaway.com/letters/gealetters.html

Page title: (none)

Result: 0 FAIL · 0 PASS · 1 NEEDS HUMAN

- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.berkshirehathaway.com/letters/gealetters.html:1` — could not fetch or read this page (ValueError: server sent br compression, which the Python standard library cannot decode; save the page from a browser (File > Save Page As, HTML only) and pass the file). Nothing was audited.

## https://www.berkshirehathaway.com/SpecialLetters/WEBCTMLtr.html

Page title: (none)

Result: 0 FAIL · 0 PASS · 1 NEEDS HUMAN

- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.berkshirehathaway.com/SpecialLetters/WEBCTMLtr.html:1` — could not fetch or read this page (ValueError: server sent br compression, which the Python standard library cannot decode; save the page from a browser (File > Save Page As, HTML only) and pass the file). Nothing was audited.

## Totals

FAIL: 4 · PASS: 7 · NEEDS HUMAN: 11

A page with zero FAIL in this report is not thereby conformant. It has passed the checks a program can run. See rules.md section 4.

