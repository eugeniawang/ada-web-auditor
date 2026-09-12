---
title: Adversarial findings, round 2 — against the stated requirements
created: 2026-09-11 20:12
last_updated: 2026-09-11 20:12
owner: adversarial-review
status: final
---

Second adversarial pass on a fresh clone of the public repo at commit 28d17a3, scored against the four stated requirements: a real citable standard, findings located with severity, the standard present in reference/, and a README a stranger can follow. Written by a second, independent reviewer. Disposition table at the end is the maintainer's.

Full findings, ranked most serious first.

## 1. The core ADA citation is one fixed subsection stretched over every finding type — MODERATE-HIGH
Every HTML finding card cites `28 CFR § 36.303(c)(1)` as "ADA law," regardless of which WCAG criterion fired. Confirmed at `reports/bad-store.html:73` (missing alt → 36.303(c)(1)) and the same citation on contrast, keyboard, duplicate-id, and tabindex findings elsewhere in the same file. I opened `reference/28-cfr-36-303-auxiliary-aids-and-services.md` and quoted (c)(1): "A public accommodation shall furnish appropriate auxiliary aids and services where necessary to ensure effective communication with individuals with disabilities." That's a general effective-communication duty — it says nothing about images, forms, contrast, or web pages. (b)(2)'s examples (screen readers, Brailled materials) support alt-text findings reasonably, but nothing in the text supports, say, "duplicate ids" (4.1.1) or "positive tabindex" (2.4.3) findings. The README/identity.md are honest that Title III has no codified web standard and courts use WCAG as the "measure" under this clause — disclosed, not hidden — but the HTML report presents (c)(1) with the same evidentiary weight as the WCAG line for findings it doesn't textually address.

## 2. Two real gaps in "drop into a Claude project, unaided" — MODERATE
Simulated an auditor with only identity.md + rules.md + examples.md + reference/ + a pasted snippet (3 planted violations: `color:#999999` on white, an unlabeled `<input>`, an `<img>` with no alt), never running tools/audit.py.
- Contrast math is not given anywhere in the provided files. rules.md section 5 says "measured against 4.5:1" but never states the sRGB relative-luminance formula (only `tools/audit.py:111`'s `def luminance` has it). An unaided Claude has to supply the WCAG contrast algorithm from its own training and do the arithmetic by hand — the likeliest place a model produces a wrong ratio it then cites as measured fact.
- Severity for a plain content image with no alt isn't pinned down in the provided docs. rules.md section 4's CRITICAL example is "an image-only link with no alt," not a bare `<img>`. A model could reasonably call a planted non-link `<img>` SERIOUS. `tools/audit.py` always classifies any missing-alt image as CRITICAL (confirmed `reports/bad-store.md:15`, a plain product photo) — but that hard rule lives only in code, not in rules.md's severity table.
- The unlabeled-input finding is unambiguous (rules.md section 5 → 4.1.2/CRITICAL) — no guessing there.

## 3. reference/ is complete and unmangled — confirms the hardest requirement holds
`grep -c "^## SC "` = 50 (30 Level A + 20 Level AA, verified separately). Spot-read first (SC 1.1.1) and last (SC 4.1.3) entries in full — complete verbatim text, no truncation, no stray link fragments. Source URL and fetch date present in the header. Same check on the CFR file: full text through subsection (h) plus amendment history, verbatim. This is the requirement most likely to fail, and it holds.

## 4. Citation chain holds across all 12 reports, not just the 3 in examples.md — LOW-MODERATE
`tools/check_audit.py` returns OK on every report in `reports/` and `test-runs/` (12 files). Hand-verified 6 individual findings against the reference file by heading — all matched verbatim. The checker does real work (regexes every citation, requires the exact heading text, requires file:line locations, opens local files to confirm the line number exists) — not a rubber stamp. Weakness: its CFR-paragraph check just substring-matches "(c)" or "(1)" anywhere in the section body, which is trivially true for almost any pin-cite — it can't catch a wrong-but-plausible ADA citation, consistent with finding #1.

## 5. Tools are hard to break — LOW
Ran audit.py against: a 404 URL (exit 0, no traceback), a redirecting URL, a file with `<base href>` (handled), a 10,000-`<img>` file (0.3s, exit 0, 10,005 finding lines), duplicate identical findings (both listed, no crash), and `--crawl 3` on the W3C "bad" demo page (wrote a report; page list in the header is sane: home.html, w3.org/, w3.org/WAI/; correct per-page counts; no tracebacks). No crash anywhere. Minor non-cost note: the crawl followed generic top-level links rather than staying within the demo's own page set.

## 6. No bare-opinion findings — LOW
Grepped should/best practice/recommend/looks/seems across identity.md, rules.md, examples.md, README.md, tools/*.py. Every hit is NEEDS HUMAN instruction text or report boilerplate, never a FAIL/PASS finding substituting opinion for citation.

## 7. Duplication that could drift (ICM check) — LOW-MODERATE
Case-law text is hand-duplicated: `reference/related-case-law.md`'s table and `tools/render_html.py`'s `CASES` list both describe the same six cases with independently-worded holdings. They agree today but are two hand-maintained copies — editing one doesn't touch the other, and render_html.py's copy is what reaches every HTML report. By contrast, the WCAG/CFR standard text itself is NOT duplicated — render_html.py loads reference/ at runtime for the slide-out panel, which is the right pattern. The mechanical-check-to-criterion table (rules.md section 5, 17 criteria) currently matches tools/audit.py's implemented checks byte-for-byte (verified by extracting the code's SC literals) — no drift yet, but nothing enforces it stays synced if a check is added later.

## 8. Cold walk of the README — PASS
Every command in the "From the command line" section ran exactly as written, exit 0, produced exactly what was promised.

## Scoring against the four requirements
(a) real citable standard vs opinion: mostly real — WCAG half solid and verbatim; ADA half leans on one general subsection stretched over findings it doesn't textually address (#1).
(b) findings specific/located/severity: yes, with one soft spot — severity for plain missing-alt images is pinned in code but not in rules.md's own table (#2).
(c) standard actually in reference/, checkable: yes, complete and unmangled (#3).
(d) README quality: yes — every command works as documented, cold (#8).


## Disposition (maintainer, 2026-09-11 20:15)

| # | Finding | Action |
|---|---|---|
| 1 | One ADA subsection stretched over every finding | Fixed. Title III citation is now per criterion: § 36.303(c)(1) for the eight communication criteria, § 36.303(a) for the rest; Title II is § 35.200(b)(1) for all, which is explicit. The header and the "What this is" box now say plainly that Title III names no web standard and the item rests on WCAG first. Rule in rules.md §2. |
| 2 | Contrast formula only in code; missing-alt severity only in code | Both fixed. WCAG's relative-luminance and contrast-ratio formula is now in rules.md §5; rules.md §4 now pins any `img` with no text alternative as CRITICAL and a filename alt as SERIOUS, matching audit.py. |
| 3, 5, 6, 8 | Clean | No action. |
| 4 | Citation chain across 12 reports | No action; holds. |
| 7 | Duplication that could drift | Accepted for this cycle: the severity definitions live in rules.md §4 and are echoed as one-line labels in render_html.py; the check list lives in rules.md §5 and in audit.py. Both echoes are display strings, not a second definition. |
