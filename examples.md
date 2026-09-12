# Examples

Three audits produced by this folder, unedited, each validated by `tools/check_audit.py`. The readable versions are `reports/bad-store.html`, `reports/clean-store.html`, and `reports/partial-clinic.html`; the markdown lines below are what the checker reads. The fixtures are invented pages in `fixtures/`; no real business is named. Each finding cites one WCAG 2.1 success criterion whose text is in `reference/wcag21-level-a-aa-success-criteria.md`; open the heading `## SC <number> <name> (Level <level>)` there to check the finding against the provision.

Regime for all three: private business open to the public (Title III). No codified web standard; WCAG 2.1 AA applied as the measure, with 28 CFR § 36.303(c)(1) as the operative obligation (effective communication through auxiliary aids and services). For a public entity the same findings would be measured under 28 CFR § 35.200(b).

## Example 1 — an online store that fails almost everything (`fixtures/bad-store.html`)

Summary: 25 FAIL, 1 PASS, 6 NEEDS HUMAN. Most severe: four images and a submit button with no accessible name, two unlabeled form fields, and a video that autoplays with no captions and no controls. This is the shape of the page named in most Title III complaints: image-only navigation, unlabeled newsletter form, no page language.

## fixtures/bad-store.html

Page title: (none)

Result: 25 FAIL · 1 PASS · 6 NEEDS HUMAN

- 🔴 **CRITICAL** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/bad-store.html:11` — <img src="logo-final-v2.png"> has no alt, aria-label, or aria-labelledby. No text alternative; a screen reader announces the filename or nothing.
- 🔴 **CRITICAL** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/bad-store.html:12` — <img src="cart.png"> has no alt, aria-label, or aria-labelledby. No text alternative; a screen reader announces the filename or nothing.
- 🔴 **CRITICAL** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/bad-store.html:27` — <img src="p2.jpg"> has no alt, aria-label, or aria-labelledby. No text alternative; a screen reader announces the filename or nothing.
- 🔴 **CRITICAL** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/bad-store.html:38` — <img src="arrow.png"> has no alt, aria-label, or aria-labelledby. No text alternative; a screen reader announces the filename or nothing.
- 🔴 **CRITICAL** — WCAG 2.1 SC 1.2.2 Captions (Prerecorded) (Level A) — `fixtures/bad-store.html:31` — <video> has no <track kind="captions">. Prerecorded synchronized media with no captions track. If the video has no audio track, this is instead a human check.
- 🔴 **CRITICAL** — WCAG 2.1 SC 1.4.2 Audio Control (Level A) — `fixtures/bad-store.html:31` — <video autoplay> with no controls and not muted. Audio plays automatically with no mechanism to pause, stop, or control volume.
- 🔴 **CRITICAL** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `fixtures/bad-store.html:12` — <a href="/cart"> has no link text, aria-label, or image alt. The link purpose cannot be determined from the link text.
- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `fixtures/bad-store.html:36` — <input name="email" type="email"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `fixtures/bad-store.html:37` — <input name="zip" type="text"> has no label, aria-label, aria-labelledby, or title. The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).
- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `fixtures/bad-store.html:38` — <button> has no text, aria-label, aria-labelledby, or named child. The button has no accessible name.
- 🟠 **SERIOUS** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/bad-store.html:17` — alt="hero-banner.jpg" is a filename. A filename is not a text alternative that serves the equivalent purpose.
- 🟠 **SERIOUS** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `fixtures/bad-store.html:18` — <p> text #999999 on #ffffff = 2.85:1, below 4.5:1. Contrast below the minimum for normal text.
- 🟠 **SERIOUS** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — `fixtures/bad-store.html:24` — <span> text #777777 on #ffffff = 4.48:1, below 4.5:1. Contrast below the minimum for normal text.
- 🟠 **SERIOUS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — `fixtures/bad-store.html:5` — viewport content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no". Pinch zoom disabled or capped below 200%.
- 🟠 **SERIOUS** — WCAG 2.1 SC 2.1.1 Keyboard (Level A) — `fixtures/bad-store.html:22` — <div onclick> is not focusable (no tabindex) and has no key handler. Function operable by mouse only.
- 🟠 **SERIOUS** — WCAG 2.1 SC 2.1.1 Keyboard (Level A) — `fixtures/bad-store.html:26` — <div onclick> is not focusable (no tabindex) and has no key handler. Function operable by mouse only.
- 🟠 **SERIOUS** — WCAG 2.1 SC 2.2.1 Timing Adjustable (Level A) — `fixtures/bad-store.html:6` — meta refresh content="300". Time limit or redirect the user cannot turn off, adjust, or extend.
- 🟠 **SERIOUS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — `fixtures/bad-store.html:1` — no <title> or empty <title>. The page has no programmatic title.
- 🟠 **SERIOUS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — `fixtures/bad-store.html:2` — html element has no lang attribute. Screen readers cannot pick a pronunciation ruleset.
- 🟠 **SERIOUS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `fixtures/bad-store.html:41` — <iframe src="https://maps.example.com/embed?store=1"> has no title. The frame has no accessible name.
- 🟡 **MODERATE** — WCAG 2.1 SC 1.3.5 Identify Input Purpose (Level AA) — `fixtures/bad-store.html:36` — <input name="email"> collects user data but has no autocomplete attribute. Input purpose for a user-information field is not programmatically identified.
- 🟡 **MODERATE** — WCAG 2.1 SC 1.3.5 Identify Input Purpose (Level AA) — `fixtures/bad-store.html:37` — <input name="zip"> collects user data but has no autocomplete attribute. Input purpose for a user-information field is not programmatically identified.
- 🟡 **MODERATE** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — `fixtures/bad-store.html:34` — id="top" appears 2 times (lines 10, 34). IDs are not unique; label/for and aria references become ambiguous.
- 🔵 **ADVISORY** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — `fixtures/bad-store.html:14` — heading level jumps from h1 to h3 ("Free shipping on orders over $50"). Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.
- 🔵 **ADVISORY** — WCAG 2.1 SC 2.4.3 Focus Order (Level A) — `fixtures/bad-store.html:42` — <a tabindex="5">. Positive tabindex overrides document order; focus order may not preserve meaning. Advisory because the criterion is about the resulting order, which a human must confirm.
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 2 headings present as heading elements
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/bad-store.html:23` — alt="Hand-thrown stoneware mug, speckled cream": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 3.3.2 Labels or Instructions (Level A) — `fixtures/bad-store.html:36` — placeholder text is the only visible label; it disappears on input. A human should confirm a persistent label exists.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 3.3.2 Labels or Instructions (Level A) — `fixtures/bad-store.html:37` — placeholder text is the only visible label; it disappears on input. A human should confirm a persistent label exists.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — `fixtures/bad-store.html:19` — link text "Click here": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.1.1 Keyboard (Level A) — `fixtures/bad-store.html:16` — <div> has a mouse-hover handler and no focus handler. If the hover reveals content or function, keyboard users cannot reach it.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — `fixtures/bad-store.html:1` — no skip link or landmark, but only 3 links. SC 2.4.1 applies to blocks repeated on multiple pages; a human must say whether any exist.

How to read one of these against the standard: the third line cites SC 1.4.3. Open `reference/wcag21-level-a-aa-success-criteria.md`, find `## SC 1.4.3 Contrast (Minimum) (Level AA)`, and the provision reads "The visual presentation of text and images of text has a contrast ratio of at least 4.5:1" with the large-text exception at 3:1. The finding measured 2.85:1 on 14px text. The two match.

## Example 2 — the same store, fixed (`fixtures/clean-store.html`)

Summary: 0 FAIL, 12 PASS, 3 NEEDS HUMAN. The three open items are alt-text meaning, which no program can judge. This report is what "the mechanical pass found nothing" looks like; it is not a conformance claim, and the report says so in its last line.

## fixtures/clean-store.html

Page title: Maple & Wren Home Goods — Handmade ceramics and linens

Result: 0 FAIL · 12 PASS · 3 NEEDS HUMAN

- 🟢 **PASS** — WCAG 2.1 SC 3.1.1 Language of Page (Level A) — html lang="en"
- 🟢 **PASS** — WCAG 2.1 SC 2.4.2 Page Titled (Level A) — title = "Maple & Wren Home Goods — Handmade ceramics and linens"
- 🟢 **PASS** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — 4 img elements all carry a text alternative (alt, aria-label, or aria-labelledby; empty alt on decorative images is allowed)
- 🟢 **PASS** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — 2 form controls all have an accessible name
- 🟢 **PASS** — WCAG 2.1 SC 3.3.2 Labels or Instructions (Level A) — 2 form controls all have a label or instruction
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — 9 links all have a text, aria-label, or image alt
- 🟢 **PASS** — WCAG 2.1 SC 4.1.1 Parsing (Level A) — 3 ids, all unique
- 🟢 **PASS** — WCAG 2.1 SC 1.3.1 Info and Relationships (Level A) — 4 headings present as heading elements
- 🟢 **PASS** — WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA) — line 20: #333333 on #ffffff = 12.63:1, meets 4.5:1
- 🟢 **PASS** — WCAG 2.1 SC 1.4.4 Resize Text (Level AA) — viewport "width=device-width, initial-scale=1" does not block zoom
- 🟢 **PASS** — WCAG 2.1 SC 1.2.2 Captions (Prerecorded) (Level A) — line 28: video has a captions/subtitles track
- 🟢 **PASS** — WCAG 2.1 SC 2.4.1 Bypass Blocks (Level A) — skip link or main/nav landmark present (skip link)
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/clean-store.html:11` — alt="Maple and Wren Home Goods": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/clean-store.html:24` — alt="Hand-thrown stoneware mug, speckled cream glaze": does this describe the image's purpose? The scanner cannot judge meaning.
- ⚪ **NEEDS HUMAN** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/clean-store.html:25` — alt="Linen tea towel, natural with navy stripe": does this describe the image's purpose? The scanner cannot judge meaning.

## Example 3 — a clinic booking page, mostly right (`fixtures/partial-clinic.html`)

Summary: 3 FAIL, 9 PASS, 2 NEEDS HUMAN. A select with a visible caption in a span but no programmatic label, a phone field with no autocomplete, and a heading that jumps from h2 to h4. The alt="Office" and the "Read more" link go to a human.

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

## Example 4 — the clinic page after the human pass (completed audit)

The mechanical report for `fixtures/partial-clinic.html` left two ⚪ lines. A person opened the page and resolved them. This is what a finished audit looks like; it passes `tools/check_audit.py` unchanged.

- 🟠 **SERIOUS** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/partial-clinic.html:30` — alt="Office" on a photograph of the reception desk and waiting area. "Office" does not serve the equivalent purpose of the image; a screen reader user learns nothing a sighted user learns. Rewrite as "Riverbend Family Dental reception desk and waiting area".
- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — "Read more" at line 31 sits in the sentence "Questions? Read more", whose programmatically determined context (the same paragraph) identifies the purpose as the FAQ.
- 🟢 **PASS** — WCAG 2.1 SC 2.1.1 Keyboard (Level A) — tabbed through the page: nav links, three form fields, the select, and the submit button are all reachable and operable; no trap.
- 🟢 **PASS** — WCAG 2.1 SC 2.4.7 Focus Visible (Level AA) — the browser default focus ring is not suppressed on any control.
- 🟢 **PASS** — WCAG 2.1 SC 1.3.2 Meaningful Sequence (Level A) — reading order in the source matches the visual order.
- 🔴 **CRITICAL** — WCAG 2.1 SC 4.1.2 Name, Role, Value (Level A) — `fixtures/partial-clinic.html:24` — carried from the mechanical pass: the day select has a visible caption in a span but no programmatic label. Wrap it in a label or add aria-labelledby.

Completed totals for this page: FAIL: 4 · PASS: 12 · NEEDS HUMAN: 0

## Totals across the three examples

FAIL: 28 · PASS: 22 · NEEDS HUMAN: 11

These totals let `tools/check_audit.py examples.md` run clean, so a reader can validate this file the same way as any report.

## What a completed human pass adds

After the mechanical report, the auditor opens the page and resolves each ⚪ line. For Example 3 that would produce, for instance:

`- 🟠 **SERIOUS** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — \`fixtures/partial-clinic.html:30\` — alt="Office" on a photograph of the reception desk and waiting area. "Office" does not serve the equivalent purpose of the image; a screen reader user learns nothing a sighted user learns.`

and

`- 🟢 **PASS** — WCAG 2.1 SC 2.4.4 Link Purpose (In Context) (Level A) — "Read more" at line 31 sits in the sentence "Questions? Read more", whose programmatically determined context (the same paragraph) identifies the purpose.`

Both keep the citation form the checker validates, so the completed report still passes `tools/check_audit.py`.
