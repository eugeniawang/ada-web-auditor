---
title: Adversarial findings — ADA web auditor
created: 2026-09-11 19:40
last_updated: 2026-09-11 20:05
owner: adversarial-review
status: final
---

Reviewer's read of the repo, cloned and run as-is. Python 3.stdlib only used throughout; nothing installed; nothing edited or deleted except this file.

Note on repo state: `tools/audit.py` and `reports/*.md` were rewritten mid-review (mtime moved from 19:32 to 19:35:1{7,8}). All findings below are against the code and reports as they stood after that edit, confirmed by `diff <(python3 tools/audit.py fixtures/bad-store.html) reports/bad-store.md` → identical. If the repo changes again before judging, re-run that diff first.

## Ranked findings, most serious first

### 1. No README.md exists at all — the README requirement fails outright
`ls ./README.md` → no such file. There is also no `examples.md`. Only `identity.md` and `rules.md` exist at the repo root.
The requirement is that a stranger can follow README.md. A stranger cloning this repo has nothing to follow — no entry point, no install step (moot, but unstated), no worked walkthrough, no explanation that `identity.md`/`rules.md` are the operating spec rather than documentation for a user. `rules.md` even refers to "The README" (in `identity.md`: "The README says this plainly to the person using you") describing content that does not exist anywhere. This is the single highest-cost defect: it directly contradicts one of the four stated requirements and cites its own missing file.
**Fix cost:** low — a README that points to `identity.md` and `rules.md`, shows the two-command flow (`audit.py` then `check_audit.py`), and states the Title II/III framing would satisfy it. But it does not exist right now.

### 2. `check_audit.py` validates form, not truth — a materially false report passes cleanly
Reproduce: build a report with (a) a finding whose location points at a file that doesn't exist and a line number that couldn't exist (`fixtures/does-not-exist-anywhere.html:99999`), (b) a PASS line asserting "every image has alt text" on a page description that says the opposite, (c) a CRITICAL severity on a check rules.md's own table (`rules.md` §4) classifies as MODERATE (missing `autocomplete`), and (d) a CFR citation with a fabricated subsection, `28 CFR § 36.303(z)(9)` (paragraph (z)(9) does not exist in the real regulation).
File: saved at `<scratch>/forged-report3.md`. Run:
```
python3 tools/check_audit.py forged-report3.md
```
Result: `OK — 3 finding lines... every citation is in reference/, every FAIL has a location and severity, PASS and FAIL totals present.` Exit code 0.
Why it slips through, mechanically:
- The location check is only `re.search(r'`[^`]+:\d+`', l)` — any backtick-quoted string ending in `:digits` counts, whether or not that file or line exists. `check_audit.py` never opens the audited HTML to confirm.
- The PASS/FAIL claim is never checked against the underlying page at all — the tool has no notion of "this PASS is false."
- Severity is checked only for being one of the four literal words; it is never cross-referenced against rules.md's own severity table, so any finding can carry any severity.
- The CFR check (`tools/check_audit.py:44-46`) extracts only the base section (`§ 36.303`) via `re.match(r'28 CFR (§ 3[56]\.\d+)', m).group(1)` and checks that substring against the reference file — it discards and never validates the subsection/paragraph letters in the citation, so `(z)(9)` (fabricated) passes as long as `36.303` (real) is present.
This matters because the stated requirement is "a reader can open a finding, open the provision, and see they match" — the checker's job is to be the machine half of that guarantee, and it can be satisfied by a report a human never wrote correctly. A hand-edited or hallucinated report can carry fabricated evidence and pass the gate that's supposed to be the trust anchor.
**Fix cost:** medium. Location could be validated against the actual source file's line count; severity could be checked against a hardcoded table matching rules.md; CFR paragraph letters could be checked against the reference file text, not just the section number. Truth-of-PASS is much harder (would need to re-run audit.py itself and diff), but is the most damaging gap of the four.

### 3. Two real false positives in `audit.py`'s own checks — reproducible in one file
File: `<scratch>/hostile-aria.html` (written for this review; not in the repo). Run `python3 tools/audit.py hostile-aria.html`.
- **`tools/audit.py:172`** (the `1.1.1` img/alt block): `<img src="icon.png" role="img" aria-label="A gear icon representing settings">` is reported CRITICAL "has no alt attribute." The check only tests `'alt' not in a` — it never looks at `aria-label`/`aria-labelledby`. An `aria-label` is a legitimate programmatic text alternative under the accessible-name computation SC 1.1.1 relies on ("a text alternative that serves the equivalent purpose" — `reference/wcag21-level-a-aa-success-criteria.md`, `## SC 1.1.1`). This is a FAIL on a conforming image.
- **`tools/audit.py:184-190`** (the `4.1.2`/`3.3.2` label block): `<label>Email address <input type="email" name="email" autocomplete="email"></label>` (implicit/wrapping label, no `for`/`id` pair) is reported CRITICAL "has no label, aria-label, aria-labelledby, or title." The `named` test is `a.get('id') in p.labels_for or aria-label or aria-labelledby or title` — it never checks whether the control is nested inside a `<label>` element with no `for`. Implicit labeling is valid HTML and satisfies 4.1.2's "name...can be programmatically determined" (`## SC 4.1.2`) exactly as much as an explicit `for` does. This is a second FAIL on conforming markup, and it is the single most common labeling pattern after explicit `for` — arguably the coverage gap most likely to appear in a page a reviewer tries.
Both are false positives specifically because the checks are narrower than the criteria they cite — the practical effect for a user is: run the tool on any ordinary hand-written form or icon-labeled button and get an incorrect CRITICAL.
**Fix cost:** low for the img case (add an `aria-label`/`aria-labelledby` check next to the alt check). Medium for the label case (needs to track, for each `<label>` open tag, whether it wraps a descendant control — the parser currently doesn't retain a tree, only a flat tag list, so this needs either a small ancestor stack or a second pass matching label spans to control positions).

### 4. `2.4.1` gets a FAIL/NEEDS-HUMAN split based on a link-count heuristic that overstates the criterion
`tools/audit.py:295-305`: pages with fewer than 5 links and no skip/landmark get NEEDS HUMAN, but pages with 5+ get a SERIOUS FAIL — even though the tool audits exactly one page and SC 2.4.1's text is explicitly about "blocks of content that are repeated on multiple web pages" (`## SC 2.4.1`, verbatim). A single-page fixture with, say, a long single-page nav (no repetition possible to observe) will get a false FAIL because it crossed a 5-link threshold invented by the tool, not derived from the standard. This is defensible as a heuristic (rules.md doesn't document the threshold anywhere though — it isn't in the "What the mechanical pass tests" table in `rules.md` §5, which just says "Skip link or main/nav landmark present," no mention of a link-count carve-out) so it's an undocumented behavior a reader comparing rules.md to the code would flag as a mismatch between the two files.
**Fix cost:** low — either document the threshold and its rationale in rules.md §5/§6, or move the FAIL branch to NEEDS HUMAN unconditionally, since the tool genuinely cannot see other pages.

### 5. Non-HTML and empty inputs produce a fabricated-looking WCAG audit with no warning
Reproduce:
```
printf '' > empty.html && python3 tools/audit.py empty.html
printf 'This is just plain text.\nNot HTML at all.\n' > notes.txt && python3 tools/audit.py notes.txt
```
Both runs complete with exit 0 and produce a full report with two SERIOUS FAILs ("no `<title>`", "no lang attribute") cited at `:1`, formatted exactly like a real finding on a real page. There's no check anywhere that the input is HTML at all (no `<html>`/`<!doctype>` sniff, no minimum-content check). A user who accidentally points the tool at a non-HTML file, a truncated download, or a WAF error page gets a confident-looking accessibility report instead of an error. It does not crash (that's good — no traceback found in this or the malformed-HTML test below), but it also never says "this doesn't look like a web page."
**Fix cost:** low — a one-line sniff (`'<html' not in html.lower()`) that emits a single top-level NEEDS HUMAN / warning line instead of running the full battery.

### 6. Malformed HTML (uppercase tags, unquoted attributes, unclosed tags, self-closing non-void element) — no crash, no false negative found
Reproduce: `<scratch>/hostile-malformed.html` (uppercase `<HTML>`/`<TITLE>`, unquoted `alt=unquoted`, `<IMG SRC="..." ALT="...">`, self-closing `<img .../>`, unclosed `<p>`, unclosed `<div class=nostyle>`). `python3 tools/audit.py hostile-malformed.html` — exit 0, no traceback, correctly caught the one truly alt-less img (the self-closed one) as CRITICAL, correctly treated the two alt-bearing images (including the uppercase-tag one) as NEEDS HUMAN, correctly flagged the missing `lang` and missing skip mechanism. `html.parser` lowercases tags and tolerates unquoted attributes and unclosed elements natively, so this class of malformation is handled well. This is a clean bill, listed for completeness since the task asked me to check it.

### 7. Five sampled `reports/bad-store.md` findings vs. `reference/wcag21-level-a-aa-success-criteria.md` — all five hold up
Checked by opening the cited heading in the reference file and comparing its sentence to the finding:
- **SC 1.1.1** (`img` no alt, line 11): reference text — "All non-text content...has a text alternative that serves the equivalent purpose." A missing `alt` on an `<img>` with no `role="presentation"` is exactly this gap. Supports the finding.
- **SC 4.1.2** (`<input type="email">` no label, line 36): reference text — "the name...can be programmatically determined." No label/aria-label/aria-labelledby/title means no determinable name. Supports the finding.
- **SC 1.4.3** (`<p>` #999999 on #fff = 2.85:1, line 18): reference text — "contrast ratio of at least 4.5:1." 2.85 < 4.5. Supports the finding, and the arithmetic is independently correct (verified against the tool's own `luminance`/`contrast` functions, which implement the standard relative-luminance formula correctly).
- **SC 2.4.1** (no skip link/landmark, line 1): reference text — "mechanism...to bypass blocks of content that are repeated on multiple web pages." Technically defensible only because bad-store.html has ≥5 links, tripping the FAIL branch discussed in finding 4 above — on a single-page audit the tool cannot actually confirm anything is "repeated on multiple pages," so the citation is correct but the certainty of the FAIL (vs. NEEDS HUMAN) is inherited from an undocumented heuristic, not from the provision text itself.
- **SC 1.3.5** (`<input name="email">` no autocomplete, line 36): reference text — "purpose of each input field...can be programmatically determined when [it] serves a purpose identified in the Input Purposes...section." "email" is one of WCAG's listed autocomplete purposes. Supports the finding.
None of the five is a bad citation. The one soft spot (2.4.1) is the same heuristic already flagged in finding 4, not a new problem.

## What I did not find
- No crash/traceback on any of malformed HTML, empty file, non-HTML text file, or the ARIA-heavy fixture. Exit code was 0 in every case tested.
- `check_audit.py` did correctly catch every "obvious" forgery I tried first: a made-up SC number, a real number paired with a fabricated name, a FAIL with no location at all, and a report missing its PASS/FAIL totals line (see the four-error run against `forged-report.md` in scratch — all four caught, exit 1).
- `identity.md` and `rules.md` are internally consistent with each other and with what the code does, with the one exception noted in finding 4 (the 2.4.1 link-count threshold is real in code but undocumented in rules.md §5's table) and the missing-README problem in finding 1 (identity.md references a README that isn't there).

## Commands to reproduce everything above
```
cd .
ls README.md examples.md                                     # finding 1: both missing
diff <(python3 tools/audit.py fixtures/bad-store.html) reports/bad-store.md   # confirms current code == current report
python3 tools/check_audit.py <path-to>/forged-report3.md      # finding 2: false report passes
python3 tools/audit.py <path-to>/hostile-aria.html            # finding 3: two false positives
sed -n '295,305p' tools/audit.py                              # finding 4: undocumented link-count threshold
python3 tools/audit.py <path-to>/empty.html                   # finding 5: fabricated report on empty input
python3 tools/audit.py <path-to>/hostile-malformed.html       # finding 6: clean bill on malformed HTML
```

## Disposition (maintainer, 2026-09-11 19:50)

| # | Finding | Action |
|---|---|---|
| 1 | No README / examples | Both existed by 19:44; the reviewer ran while they were being written. A cold clone of the public repo runs the README commands with no install. |
| 2 | Checker validates form, not truth | Partly fixed: CFR paragraph letters are now checked against the section text; local file locations are checked against the file's line count. Not fixed, by design: truth of a PASS and severity-vs-table need the page and the human pass. The checker's docstring now says exactly this. |
| 3 | img with aria-label; implicit label | Both fixed. `aria-label`/`aria-labelledby`/`role="presentation"`/`aria-hidden` accepted on img; a control inside a wrapping `<label>` is named. |
| 4 | 2.4.1 threshold undocumented | Documented in rules.md §5 with the reasoning. |
| 5 | Non-HTML input audited | Fixed: input with no html/head/body element produces one NEEDS HUMAN line and nothing else. |
| 6, 7 | Clean | No action. |
