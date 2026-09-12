# ADA web accessibility audit (mechanical pass)

Generated 2026-09-11 20:14 by tools/audit.py. Standard: WCAG 2.1 Level A and AA as adopted by 28 CFR § 35.200(b) and applied by courts under 28 CFR § 36.303 (see reference/). Every finding below cites one success criterion whose verbatim text is in reference/wcag21-level-a-aa-success-criteria.md.

Severity key (rules.md): 🔴 CRITICAL blocks a task for some users · 🟠 SERIOUS major barrier · 🟡 MODERATE degrades but passable · 🔵 ADVISORY likely issue, criterion needs judgment · 🟢 PASS · ⚪ NEEDS HUMAN.

This is the mechanical pass only. It cannot see rendered styling, keyboard focus behaviour, dynamic content, or meaning. rules.md section 4 lists what a human must still check before calling a page conformant.


## https://www.craigslist.org/about/sites

Page title: craigslist > sites

Result: 9 FAIL · 5 PASS · 1 NEEDS HUMAN

- 🟠 **SERIOUS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — `https://www.craigslist.org/about/sites:1` — no skip link and no main/nav landmark or role; page has 727 links. No mechanism to bypass what is almost certainly a repeated navigation block. Confirm the block repeats across pages.
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.craigslist.org/about/sites:2` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/about/sites:46` — heading level jumps from h2 to h4 ("Alabama"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/about/sites:630` — heading level jumps from h2 to h4 ("Alberta"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/about/sites:727` — heading level jumps from h2 to h4 ("Austria"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/about/sites:920` — heading level jumps from h2 to h4 ("Bangladesh"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/about/sites:1054` — heading level jumps from h2 to h4 ("Australia"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/about/sites:1082` — heading level jumps from h2 to h4 ("Argentina"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/about/sites:1187` — heading level jumps from h2 to h4 ("Egypt"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "craigslist > sites"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 727 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — 2 ids, all unique
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 148 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width,initial-scale=1" does not block zoom
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.craigslist.org/about/sites:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## https://www.craigslist.org/area/auburn

Page title: craigslist: auburn jobs, apartments, for sale, services, community, and events

Result: 7 FAIL · 5 PASS · 2 NEEDS HUMAN

- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/auburn:667` — <select name="lang" type="text"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.craigslist.org/area/auburn:2` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟠 **SERIOUS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/auburn:217` — <iframe src="https://www.craigslist.org/static/www/localStorage-092e9f9e2"> has no title. The frame has no accessible name.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/auburn:310` — id="post" appears 2 times (lines 289, 310). IDs are not unique; label/for and aria references become ambiguous.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/auburn:384` — id="about_craigslist" appears 2 times (lines 375, 384). IDs are not unique; label/for and aria references become ambiguous.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/auburn:316` — heading level jumps from h1 to h4 ("event calendar"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/auburn:673` — heading level jumps from h3 to h5 ("nearby cl"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "craigslist: auburn jobs, apartments, for sale, services, com"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 452 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 23 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width,initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (landmark only)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `https://www.craigslist.org/area/auburn:925` — link text "more...": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.craigslist.org/area/auburn:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## https://www.craigslist.org/area/bham

Page title: craigslist: birmingham, AL jobs, apartments, for sale, services, community, and events

Result: 7 FAIL · 5 PASS · 2 NEEDS HUMAN

- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/bham:667` — <select name="lang" type="text"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.craigslist.org/area/bham:2` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟠 **SERIOUS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/bham:217` — <iframe src="https://www.craigslist.org/static/www/localStorage-092e9f9e2"> has no title. The frame has no accessible name.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/bham:310` — id="post" appears 2 times (lines 289, 310). IDs are not unique; label/for and aria references become ambiguous.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/bham:384` — id="about_craigslist" appears 2 times (lines 375, 384). IDs are not unique; label/for and aria references become ambiguous.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/bham:316` — heading level jumps from h1 to h4 ("event calendar"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/bham:673` — heading level jumps from h3 to h5 ("nearby cl"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "craigslist: birmingham, AL jobs, apartments, for sale, servi"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 452 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 23 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width,initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (landmark only)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `https://www.craigslist.org/area/bham:925` — link text "more...": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.craigslist.org/area/bham:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## https://www.craigslist.org/area/dothan

Page title: craigslist: dothan, AL jobs, apartments, for sale, services, community, and events

Result: 7 FAIL · 5 PASS · 2 NEEDS HUMAN

- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/dothan:667` — <select name="lang" type="text"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.craigslist.org/area/dothan:2` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟠 **SERIOUS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/dothan:217` — <iframe src="https://www.craigslist.org/static/www/localStorage-092e9f9e2"> has no title. The frame has no accessible name.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/dothan:310` — id="post" appears 2 times (lines 289, 310). IDs are not unique; label/for and aria references become ambiguous.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/dothan:384` — id="about_craigslist" appears 2 times (lines 375, 384). IDs are not unique; label/for and aria references become ambiguous.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/dothan:316` — heading level jumps from h1 to h4 ("event calendar"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/dothan:673` — heading level jumps from h3 to h5 ("nearby cl"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "craigslist: dothan, AL jobs, apartments, for sale, services,"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 452 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 23 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width,initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (landmark only)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `https://www.craigslist.org/area/dothan:925` — link text "more...": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.craigslist.org/area/dothan:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## https://www.craigslist.org/area/shoals

Page title: craigslist: the shoals jobs, apartments, for sale, services, community, and events

Result: 7 FAIL · 5 PASS · 2 NEEDS HUMAN

- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/shoals:667` — <select name="lang" type="text"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.craigslist.org/area/shoals:2` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟠 **SERIOUS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/shoals:217` — <iframe src="https://www.craigslist.org/static/www/localStorage-092e9f9e2"> has no title. The frame has no accessible name.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/shoals:310` — id="post" appears 2 times (lines 289, 310). IDs are not unique; label/for and aria references become ambiguous.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/shoals:384` — id="about_craigslist" appears 2 times (lines 375, 384). IDs are not unique; label/for and aria references become ambiguous.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/shoals:316` — heading level jumps from h1 to h4 ("event calendar"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/shoals:673` — heading level jumps from h3 to h5 ("nearby cl"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "craigslist: the shoals jobs, apartments, for sale, services,"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 452 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 23 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width,initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (landmark only)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `https://www.craigslist.org/area/shoals:925` — link text "more...": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.craigslist.org/area/shoals:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## https://www.craigslist.org/area/gadsden

Page title: craigslist: gadsden jobs, apartments, for sale, services, community, and events

Result: 7 FAIL · 5 PASS · 2 NEEDS HUMAN

- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/gadsden:667` — <select name="lang" type="text"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.craigslist.org/area/gadsden:2` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟠 **SERIOUS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/gadsden:217` — <iframe src="https://www.craigslist.org/static/www/localStorage-092e9f9e2"> has no title. The frame has no accessible name.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/gadsden:310` — id="post" appears 2 times (lines 289, 310). IDs are not unique; label/for and aria references become ambiguous.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/gadsden:384` — id="about_craigslist" appears 2 times (lines 375, 384). IDs are not unique; label/for and aria references become ambiguous.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/gadsden:316` — heading level jumps from h1 to h4 ("event calendar"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/gadsden:673` — heading level jumps from h3 to h5 ("nearby cl"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "craigslist: gadsden jobs, apartments, for sale, services, co"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 452 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 23 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width,initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (landmark only)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `https://www.craigslist.org/area/gadsden:925` — link text "more...": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.craigslist.org/area/gadsden:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## https://www.craigslist.org/area/huntsville

Page title: craigslist: huntsville jobs, apartments, for sale, services, community, and events

Result: 7 FAIL · 5 PASS · 2 NEEDS HUMAN

- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/huntsville:667` — <select name="lang" type="text"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.craigslist.org/area/huntsville:2` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟠 **SERIOUS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/huntsville:217` — <iframe src="https://www.craigslist.org/static/www/localStorage-092e9f9e2"> has no title. The frame has no accessible name.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/huntsville:310` — id="post" appears 2 times (lines 289, 310). IDs are not unique; label/for and aria references become ambiguous.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/huntsville:384` — id="about_craigslist" appears 2 times (lines 375, 384). IDs are not unique; label/for and aria references become ambiguous.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/huntsville:316` — heading level jumps from h1 to h4 ("event calendar"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/huntsville:673` — heading level jumps from h3 to h5 ("nearby cl"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "craigslist: huntsville jobs, apartments, for sale, services,"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 452 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 23 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width,initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (landmark only)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `https://www.craigslist.org/area/huntsville:925` — link text "more...": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.craigslist.org/area/huntsville:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## https://www.craigslist.org/area/mobile

Page title: craigslist: mobile, AL jobs, apartments, for sale, services, community, and events

Result: 7 FAIL · 5 PASS · 2 NEEDS HUMAN

- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/mobile:667` — <select name="lang" type="text"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `https://www.craigslist.org/area/mobile:2` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟠 **SERIOUS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `https://www.craigslist.org/area/mobile:217` — <iframe src="https://www.craigslist.org/static/www/localStorage-092e9f9e2"> has no title. The frame has no accessible name.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/mobile:310` — id="post" appears 2 times (lines 289, 310). IDs are not unique; label/for and aria references become ambiguous.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `https://www.craigslist.org/area/mobile:384` — id="about_craigslist" appears 2 times (lines 375, 384). IDs are not unique; label/for and aria references become ambiguous.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/mobile:316` — heading level jumps from h1 to h4 ("event calendar"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `https://www.craigslist.org/area/mobile:673` — heading level jumps from h3 to h5 ("nearby cl"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "craigslist: mobile, AL jobs, apartments, for sale, services,"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 452 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 23 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width,initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (landmark only)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `https://www.craigslist.org/area/mobile:925` — link text "more...": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `https://www.craigslist.org/area/mobile:1` — no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.

## Totals

FAIL: 58 · PASS: 40 · NEEDS HUMAN: 15

A page with zero FAIL in this report is not thereby conformant. It has passed the checks a program can run. See rules.md section 4.

