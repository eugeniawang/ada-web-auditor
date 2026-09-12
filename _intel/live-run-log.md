---
title: Live-site runs — what the scanner got right and wrong
created: 2026-09-11 19:45
last_updated: 2026-09-11 19:50
owner: Gina Wang
status: active
---

# Live-site runs, 2026-09-11 evening

Purpose: run `tools/audit.py` against real served pages to find crashes, false positives, and false negatives before users do. Results are about the tool, not the sites.

| Page | Why chosen | First run | After fixes | What it taught |
|---|---|---|---|---|
| W3C WAI "Before" demo home (`/WAI/demos/bad/before/home.html`) | Built by W3C to be inaccessible on purpose | 42 FAIL · 4 PASS · 18 NEEDS HUMAN | same | The scanner finds what W3C planted: missing alt, no lang, unlabeled fields, low contrast, mouse-only handlers. Full report kept as `../test-runs/live_www_w3_org_WAI_demos_bad_before_home_html.md`. |
| W3C WAI "After" demo home (fixed version) | The same page, repaired by W3C | 0 FAIL · 9 PASS · 7 NEEDS HUMAN | same | A page W3C calls conformant produces zero mechanical FAIL. The seven open items are meaning questions (alt text, context), which is correct. |
| example.com | Smallest real page on the web | 1 FAIL (2.4.1 no skip link) | 0 FAIL · 5 PASS · 3 NEEDS HUMAN | **False positive fixed.** SC 2.4.1 applies to blocks repeated across pages; a one-paragraph page has none. Rule now: no landmark AND 5+ links → SERIOUS; fewer → NEEDS HUMAN with the question. |
| ada.gov home | The regulator's own site, USWDS design system | 1 FAIL (4.1.2 button no name, line 212) | 0 FAIL · 10 PASS · 19 NEEDS HUMAN | **False positive fixed.** The button's name came from a child `<img alt="close menu">`. Child alt and aria-label now contribute to the accessible name of an open link or button; `aria-labelledby` accepted. |
| accessible.org/lawsuits | A WordPress page from an accessibility vendor | 29 FAIL | 0 FAIL · 10 PASS · 5 NEEDS HUMAN | **Two false positives fixed.** (1) 25 duplicate-id findings were `<link id>` stylesheets inside `<noscript>` fallbacks: no user impact, not what 4.1.1 is about. ids on head-only elements and inside noscript are now excluded. (2) Four "unlabeled" fields used implicit labels (`<label>Name <input></label>`); implicit labels now count. A display:none honeypot textarea is still counted if it lacks `hidden`/`aria-hidden`, because the scanner cannot see CSS; that is recorded as a known limit in rules.md §6. |

## Known limits confirmed by these runs

- No CSS or script execution: stylesheet contrast, `display:none`, and injected content are invisible. Every such case is a NEEDS HUMAN line, never a guess.
- Pages behind a bot wall return an HTTP error; the user saves the HTML and passes the file.
- The scanner does not follow links; one page per source argument.

## Second round, 19:44–19:50: four real sites, HTML reports in `test-runs/`

| Site | First run | After fixes | What it taught |
|---|---|---|---|
| berkshirehathaway.com | 2 FAIL · 3 PASS · 3 NEEDS HUMAN | same | **Both real.** `<html>` has no `lang` (line 11, confirmed) and there is no skip link or landmark on a page with 18 links. |
| craigslist.org/about/sites | 9 FAIL · 5 PASS · 1 NEEDS HUMAN | same | **Real.** No `lang`, no landmark on a page with 727 links, and seven h2→h4 heading jumps (advisory). |
| dominos.com | 1 FAIL (iframe with no title) | 0 FAIL · 4 PASS · 3 NEEDS HUMAN | **False positive fixed.** The frame was the Google Tag Manager fallback inside `<noscript>`, invisible to users. Elements inside `noscript` are now excluded from image, control, and frame checks. |
| apple.com | 4 CRITICAL (videos with no captions) | 0 FAIL · 10 PASS · 16 NEEDS HUMAN | **False positive fixed.** All four are `<video muted>` hero animations with no audio track; captions are not required for silent video. A muted or aria-hidden video with no captions is now NEEDS HUMAN ("play it; if there is speech, captions are required"), not a FAIL. |

Net: two false positives found and fixed, two sites with real findings. Every report passed `tools/check_audit.py`.
