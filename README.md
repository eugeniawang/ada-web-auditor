# ADA website compliance auditor

Drop this folder into a Claude project and Claude becomes an auditor that checks a web page for **ADA compliance**: can people who are blind, deaf, or cannot use a mouse use this site. It reports where the page is in compliance, where it is out of compliance, how serious each problem is, and which section of the ADA regulations and the underlying technical standard each finding rests on. The law and the standard are in `reference/`, verbatim and dated, so anyone can open a finding and check it against the text.

The output is a colour-coded HTML report a business owner can read without knowing what any of the rule numbers mean. Every item has a "see the full text" link that slides out the exact provision. A markdown twin is what the checker validates. Open `reports/bad-store.html` to see one.

Under the hood the technical measure is WCAG 2.1 Level A and AA, which is what the Department of Justice adopted in 28 CFR § 35.200 and what courts apply to businesses under 28 CFR § 36.303. The report says "images need a text description" first and "WCAG 2.1 SC 1.1.1 · 28 CFR § 36.303(c)(1)" second.

Written 2026-09-11.

## Run it

```
python3 tools/audit.py https://example.com --html reports/ex.html -o reports/ex.md   # HTML for people, markdown for the checker
python3 tools/check_audit.py reports/ex.md                                          # validate every citation against reference/
python3 tools/audit.py city.gov --regime title2 --html reports/city.html            # a government site (Title II)
```

Python 3.8 or later, nothing to install. Open `reports/bad-store.html` for a finished example. Tests: `python3 -m unittest discover tests` (18 tests, stdlib).

## Why this exists

Federal website accessibility suits under ADA Title III reached 3,117 in 2025, about 36% of all Title III filings, and industry trackers project more than 5,000 in 2026 counting state courts ([Level Access](https://www.levelaccess.com/blog/2024-u-s-web-accessibility-litigation-key-trends-and-strategies-for-mitigating-risk/), [Abledly mid-year 2026](https://abledly.com/ada-lawsuit-statistics), [UserWay](https://userway.org/blog/web-accessibility-lawsuit/)). Most defendants are small businesses; the three issues plaintiffs' complaints name most are missing image alt text, unlabeled form fields, and pages that cannot be used with a keyboard ([Accessible.org](https://accessible.org/lawsuits/), [Saul Ewing](https://www.saul.com/insights/blog/ada-website-accessibility-risk), [accessiBe](https://accessibe.com/blog/ada-website-lawsuits)). Small-business owners describe getting the summons with no idea which rule they broke ([r/smallbusiness, 2025](https://www.reddit.com/r/smallbusiness/comments/1o929d2/small_ecommerce_business_got_sued_for_ada/), [r/smallbusiness, 2026](https://www.reddit.com/r/smallbusiness/comments/1qit2zl/received_a_federal_summons_ada_website_compliance/), [r/legaladvice](https://www.reddit.com/r/legaladvice/comments/ncmbp4/sued_for_ada_violation_on_website_by/)).

For state and local governments the rule is now codified: the Department of Justice adopted WCAG 2.1 AA in **28 CFR § 35.200** (final rule 2024-04-24), with compliance dates of 2027-04-26 for entities serving 50,000 or more people and 2028-04-26 for the rest after the 2026-04-20 one-year extension ([Federal Register](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web), [ADA.gov first steps](https://www.ada.gov/resources/web-rule-first-steps/)). For private businesses there is no codified web standard; courts measure against WCAG 2.1 AA under **28 CFR § 36.303**. This auditor uses the same criteria for both and names the regime at the top of every report.

This is not legal advice. It reports conformance to a published technical standard. Whether a page will draw a complaint, or whether a complaint would succeed, is a question for a lawyer.

## What is in the folder

| File | Job |
|---|---|
| `identity.md` | Who the auditor is, what standard it enforces, what it refuses to do. |
| `rules.md` | Order of work, citation form, the six classes (🔴 CRITICAL · 🟠 SERIOUS · 🟡 MODERATE · 🔵 ADVISORY · 🟢 PASS · ⚪ NEEDS HUMAN), what the program tests, what only a human can. |
| `examples.md` | Three complete audits with citations, produced from the fixtures. |
| `reference/related-case-law.md` | Six real ADA website cases (Domino's, Target, Winn-Dixie, Blick, Netflix, Harvard) mapped to the barrier each turned on. Background only; findings never cite it. |
| `reference/wcag21-definitions-contrast-and-luminance.md` | WCAG's own contrast-ratio and relative-luminance definitions, verbatim, which the 1.4.3 measurement implements. |
| `reference/` | The standard. `wcag21-level-a-aa-success-criteria.md`: all 50 Level A and AA success criteria, verbatim from the W3C Recommendation, fetched 2026-09-11. `28-cfr-part-35-subpart-h-web-and-mobile-accessibility.md`: §§ 35.200–35.204 verbatim from eCFR, 2026-09-01 edition. `28-cfr-36-303-auxiliary-aids-and-services.md`: § 36.303 verbatim. `raw/` holds the unmodified downloads; `wcag21-sc-index.json` is the machine index the tools use. |
| `tools/audit.py` | The mechanical pass. Python 3 standard library only. Reads a file or URL, writes the HTML report (`--html`) and the markdown one (`-o`). |
| `tools/render_html.py` | The HTML report: plain-English rule names, colour-coded severity, ADA section on every item, slide-out panel with the provision text. |
| `tools/check_audit.py` | Validates any report: every citation must be a heading in `reference/`, every FAIL must carry a location and a class, totals must be present. Exit 1 on any miss. |
| `tests/` | 18 standard-library unit tests: scanner checks, the contrast formula against WCAG's definition, and the checker's rejection of forged citations, paragraphs, and line numbers. |
| `fixtures/` | Three invented pages: a store that fails almost everything, the same store fixed, a clinic page mostly right. |
| `reports/` | The three audits in `examples.md`, as HTML and markdown. |
| `test-runs/` | The real test runs, unedited: HTML and markdown reports for W3C's broken and fixed demo pages, example.com, ada.gov, accessible.org, Berkshire Hathaway (whole-site crawl), Craigslist, Domino's, and Apple. What each run taught and what was fixed is in `_intel/live-run-log.md`. |
| `_intel/` | Working notes: the live-run log and two independent adversarial reviews with what was fixed. Not part of the auditor. |

## How to use it

**As a Claude project.** Add the folder. Give Claude a page: paste the HTML, attach a file, or give a URL and ask it to fetch. Say: "Audit this site for ADA compliance." Claude runs the order in `rules.md` section 1 and writes both reports.

**From the command line, no install:**

```
python3 tools/audit.py https://example.com --html reports/ex.html -o reports/ex.md   # HTML for people, markdown for the checker
python3 tools/check_audit.py reports/ex.md                                          # validate every citation against reference/
python3 tools/audit.py city.gov --regime title2 --html reports/city.html            # a government site (Title II)
```

Requires Python 3.8 or later. Nothing else. A URL fetch uses the standard library and reads the served HTML only; it does not run scripts, so content injected after load is not seen. Pages behind a login or a bot wall will not fetch; save the HTML and pass the file.

**What to feed it.** A website address. By default it audits the page you give it plus up to seven more pages it finds by following that site's own links (`--crawl 8`; raise it for a bigger sweep, `--crawl 1` for one page). Or a saved HTML file. The report header says exactly which pages were audited. The pages plaintiffs actually test are the home page, a product or service page, the checkout or booking form, and the contact page; if the crawl misses one, pass its URL too.

**What you get back.** An HTML report with what was found at the top in plain bullets, then counts by severity, then three sections: where you are out of compliance, where you are in compliance, and what needs a person to check. Each item names the rule in plain words, where on the page, what was measured, and then the citation: the WCAG 2.1 criterion and the ADA regulation section, with a link that slides out the full text of both. The markdown twin has the same content, one finding per line: mark, class, the WCAG 2.1 criterion (number, name, level), the file and line, what was measured, one sentence on why. PASS lines say what was checked. NEEDS HUMAN lines carry the exact question. Totals at the bottom. The last line reminds you that zero FAIL from the program is not conformance.

**Then do the human pass.** `rules.md` section 6 lists what a program cannot test: stylesheet contrast, keyboard operation, focus visibility, reading order, alt-text meaning, reflow, error handling. Resolve each ⚪ line to PASS or FAIL with a location, keep the citation form, and run the checker again.

## How to verify a finding

1. Open the report line. Note the criterion, for example `WCAG 2.1 SC 1.4.3 Contrast (Minimum) (Level AA)`.
2. Open `reference/wcag21-level-a-aa-success-criteria.md`. Find `## SC 1.4.3 Contrast (Minimum) (Level AA)`. Read the provision.
3. Open the file at the cited line. Reproduce the measurement (the report gives the colours and the ratio).
4. If the three do not agree, the finding is wrong. Please file it.

`tools/check_audit.py` does step 2 for every line automatically. It cannot do steps 3 and 4.

## What it is not

Not a Lighthouse or axe replacement: those run in a browser and see rendered CSS and scripts; this reads served HTML with no dependencies and cites the provision for every line, which those tools do not. Not an overlay: it does not certify a page because a widget is installed. Not a legal opinion.

## Versioning of the standard

WCAG 2.1 was fetched from https://www.w3.org/TR/WCAG21/ on 2026-09-11 (the 2023-09-21 edition at that URL; 28 CFR § 35.200(b)(3) incorporates the 2018-06-05 edition by reference, and the success criteria text is unchanged between them). The CFR text is the eCFR 2026-09-01 point-in-time edition. Both dates are in the reference file headers. If the standard changes, re-fetch, re-date, and re-run the checker; a stale reference is the one way this folder can be wrong without anyone noticing.

## Sources consulted while building

Cited above, plus: [DigitalA11Y ADA compliance guide](https://www.digitala11y.com/compliance/ada/), [Accessible.org, can you get sued](https://accessible.org/sued-website-not-ada-compliant/), [Accessible.org, ADA website compliance](https://accessible.org/ada-website-compliance/), [Coates' Canons on the Title II rule](https://canons.sog.unc.edu/blog/2026/01/14/understanding-the-new-ada-web-accessibility-requirements-for-state-and-local-governments/), and [a walkthrough of Lighthouse accessibility audits](https://medium.com/accessibility-a11y/do-an-accessibility-audit-using-google-chrome-lighthouse-30ff7887901c) for what a browser-based tool covers that this one deliberately does not.

## Licence

Code and prose: MIT. `reference/` reproduces W3C and U.S. federal government text under their own terms (W3C Document License; U.S. government works are public domain).
