#!/usr/bin/env python3
"""Validate an audit report against reference/. Python 3 standard library only.

Checks, and exits non-zero on any miss:
  1. Every finding line (FAIL, PASS, NEEDS HUMAN) cites exactly one WCAG 2.1
     success criterion, and that criterion number, name, and level appear
     verbatim in reference/wcag21-level-a-aa-success-criteria.md.
  2. Every "28 CFR § 35.xxx" or "§ 36.303" cited anywhere in the report is a
     section heading in the reference CFR files, and every paragraph letter or
     number in the citation, e.g. (c)(1), appears inside that section's text.
  3. Every FAIL and NEEDS HUMAN line carries a location in backticks
     (`file:line` or `url:line`).
  4. Every FAIL line carries one of the four severity classes.
  5. The report states both a PASS count and a FAIL count.
  6. A location that names a local file points at a line that exists in it.

What it does not check: that a PASS is true, or that a severity matches
rules.md. Those need the page, and the human pass. The checker guards the
citation chain from report to standard; it is not a second auditor.

Usage: python3 tools/check_audit.py reports/some-report.md
"""
import sys, re, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, '..', 'reference')
WCAG = open(os.path.join(REF, 'wcag21-level-a-aa-success-criteria.md')).read()
CFR = open(os.path.join(REF, '28-cfr-part-35-subpart-h-web-and-mobile-accessibility.md')).read() + open(os.path.join(REF, '28-cfr-36-303-auxiliary-aids-and-services.md')).read()
SEVERITIES = ('CRITICAL', 'SERIOUS', 'MODERATE', 'ADVISORY')


def main(path):
    text = open(path).read()
    errors = []
    lines = [l for l in text.splitlines() if l.startswith('- ')]
    if not lines:
        errors.append('no finding lines (lines starting with "- ") found')
    for n, l in enumerate(lines, 1):
        cites = re.findall(r'WCAG 2\.1 SC (\d+\.\d+\.\d+) (.+?) \(Level (A{1,2})\)', l)
        if len(cites) != 1:
            errors.append(f'line {n}: expected exactly one WCAG 2.1 SC citation, found {len(cites)}: {l[:90]}')
            continue
        sc, name, level = cites[0]
        needle = f'## SC {sc} {name} (Level {level})'
        if needle not in WCAG:
            errors.append(f'line {n}: citation not in reference/: "{needle}"')
        kind = re.search(r'\*\*(CRITICAL|SERIOUS|MODERATE|ADVISORY|PASS|NEEDS HUMAN)\*\*', l)
        if not kind:
            errors.append(f'line {n}: no class marker: {l[:90]}')
            continue
        k = kind.group(1)
        if k in SEVERITIES or k == 'NEEDS HUMAN':
            if not re.search(r'`[^`]+:\d+`', l):
                errors.append(f'line {n}: {k} finding has no `location:line`: {l[:90]}')
    for m in set(re.findall(r'28 CFR § 3[56]\.\d+(?:\([a-z0-9]+\))*', text)):
        sec = re.match(r'28 CFR (§ 3[56]\.\d+)', m).group(1)
        head = re.search(r'### ' + re.escape(sec) + r' .*?\n(.*?)(?=\n### |\Z)', CFR, re.S)
        if not head:
            errors.append(f'CFR citation not in reference/: {m}')
            continue
        body = head.group(1)
        for para in re.findall(r'\(([a-z0-9]+)\)', m[len('28 CFR ') + len(sec):]):
            if f'({para})' not in body:
                errors.append(f'CFR citation {m}: paragraph ({para}) not found in the text of {sec} in reference/')
    # 6. a location that names a local file must point at a line inside it
    for l in lines:
        for fpath, ln in re.findall(r'`([^`:]+):(\d+)`', l):
            if re.match(r'https?://', fpath) or not os.path.exists(fpath):
                continue
            n_lines = sum(1 for _ in open(fpath, errors="replace"))
            if int(ln) < 1 or int(ln) > max(n_lines, 1):
                errors.append(f'location `{fpath}:{ln}` is outside the file ({n_lines} lines)')
    if not re.search(r'FAIL: \d+', text) or not re.search(r'PASS: \d+', text):
        errors.append('report must state "FAIL: n" and "PASS: n" totals')
    if errors:
        print(f'FAIL — {len(errors)} problem(s) in {path}')
        for e in errors:
            print('  -', e)
        return 1
    print(f'OK — {len(lines)} finding lines in {path}; every citation is in reference/, every FAIL has a location and severity, PASS and FAIL totals present.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
