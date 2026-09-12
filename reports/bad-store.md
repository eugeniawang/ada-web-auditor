# ADA web accessibility audit (mechanical pass)

Generated 2026-09-11 20:13 by tools/audit.py. Standard: WCAG 2.1 Level A and AA as adopted by 28 CFR § 35.200(b) and applied by courts under 28 CFR § 36.303 (see reference/). Every finding below cites one success criterion whose verbatim text is in reference/wcag21-level-a-aa-success-criteria.md.

Severity key (rules.md): 🔴 CRITICAL blocks a task for some users · 🟠 SERIOUS major barrier · 🟡 MODERATE degrades but passable · 🔵 ADVISORY likely issue, criterion needs judgment · 🟢 PASS · ⚪ NEEDS HUMAN.

This is the mechanical pass only. It cannot see rendered styling, keyboard focus behaviour, dynamic content, or meaning. rules.md section 4 lists what a human must still check before calling a page conformant.


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

## Totals

FAIL: 25 · PASS: 1 · NEEDS HUMAN: 6

A page with zero FAIL in this report is not thereby conformant. It has passed the checks a program can run. See rules.md section 4.

