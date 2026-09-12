#!/usr/bin/env python3
"""Render audit results as a self-contained HTML report a business owner can read.

Used by tools/audit.py when --html is given. Standard library only.
Every line keeps the technical citation (WCAG 2.1 success criterion, verbatim
in reference/) and adds the ADA regulation that adopts it and a plain-English
sentence saying what the rule means for a person using the site.
"""
import html as H
import datetime
import os
import re
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, '..', 'reference')


def load_provisions():
    """Map 'SC 1.1.1' -> verbatim criterion text, and '§ 36.303' -> verbatim section text, from reference/."""
    prov = {}
    w = open(os.path.join(REF, 'wcag21-level-a-aa-success-criteria.md'), encoding='utf-8').read()
    for m in re.finditer(r'\n## (SC [\d.]+ .*?)\n(.*?)(?=\n---\n|\Z)', w, re.S):
        prov[m.group(1).split(' ')[1]] = (m.group(1), m.group(2).strip())
    for fn in ('28-cfr-part-35-subpart-h-web-and-mobile-accessibility.md', '28-cfr-36-303-auxiliary-aids-and-services.md'):
        c = open(os.path.join(REF, fn), encoding='utf-8').read()
        for m in re.finditer(r'\n### (§ 3[56]\.\d+) (.*?)\n(.*?)(?=\n### |\Z)', c, re.S):
            prov[m.group(1)] = (f'28 CFR {m.group(1)} {m.group(2)}', m.group(3).strip())
    return prov

# Plain-English meaning of each criterion the scanner can emit.
PLAIN = {
    '1.1.1': ('Images need a text description', 'A blind visitor hears the description instead of seeing the picture. Without one, the screen reader says the filename or nothing.'),
    '1.2.2': ('Videos need captions', 'A deaf visitor reads the captions. Without them, the video is silent to them.'),
    '1.3.1': ('Structure must be real, not just visual', 'Headings, lists, and labels must be coded as what they are, so a screen reader can announce the page the way a sighted person sees it.'),
    '1.3.5': ('Form fields should say what they collect', 'Fields for name, email, phone, or address must be tagged so browsers and assistive tools can fill them in for people who struggle to type.'),
    '1.4.2': ('Sound must not play on its own without a way to stop it', 'Audio that starts by itself drowns out a screen reader. The visitor needs a pause or volume control.'),
    '1.4.3': ('Text must have enough contrast', 'Light grey on white is unreadable for people with low vision. Normal text needs at least 4.5 to 1 contrast, large text 3 to 1.'),
    '1.4.4': ('Visitors must be able to zoom', 'People with low vision enlarge the page to 200 percent. Turning off pinch-zoom locks them out.'),
    '2.1.1': ('Everything must work with a keyboard', 'Many people cannot use a mouse. Every button, link, and menu has to work with Tab and Enter.'),
    '2.2.1': ('No timers the visitor cannot control', 'A page that refreshes or redirects on its own cuts off people who read or move slowly.'),
    '2.4.1': ('A way to skip the repeated menu', 'A keyboard user should not have to Tab through forty menu links on every page to reach the content.'),
    '2.4.2': ('Every page needs a title', 'The title is the first thing a screen reader announces. Without it the visitor does not know where they are.'),
    '2.4.3': ('Tab order must make sense', 'Keyboard focus should move through the page in the order a sighted person reads it.'),
    '2.4.4': ('Links must say where they go', 'A screen reader can list every link on a page. Twelve links that all say "click here" tell the visitor nothing.'),
    '3.1.1': ('The page must declare its language', 'Screen readers pick a voice from this. A missing language attribute makes English pages read in the wrong accent or not at all.'),
    '3.3.2': ('Form fields need labels', 'A blind visitor must hear "Email address" when they land on the box, not "edit text".'),
    '4.1.1': ('The code must be well-formed', 'Duplicate ids and broken markup make assistive tools misread the page.'),
    '4.1.2': ('Every control must have a name', 'Buttons, fields, and frames need a name a screen reader can announce. An icon-only button with no name is a mystery button.'),
}

# Real, widely reported ADA website cases, keyed by the checks they map to. Details in reference/related-case-law.md.
CASES = [
    ('Robles v. Domino\'s Pizza, LLC, 913 F.3d 898 (9th Cir. 2019)', 'A blind customer could not order with a screen reader; the ADA was held to apply to the website and app.', {'1.1.1', '4.1.2', '2.1.1', '2.4.4', '3.3.2'}),
    ('National Federation of the Blind v. Target Corp., 452 F. Supp. 2d 946 (N.D. Cal. 2006)', 'Missing alt text and mouse-only checkout; settled for $6 million.', {'1.1.1', '2.1.1', '2.4.4'}),
    ('Gil v. Winn-Dixie Stores, Inc., 257 F. Supp. 3d 1340 (S.D. Fla. 2017)', 'Prescription refills and coupons unusable with a screen reader; trial court ordered WCAG conformance (later vacated on appeal).', {'1.1.1', '3.3.2', '4.1.2'}),
    ('Andrews v. Blick Art Materials, LLC, 268 F. Supp. 3d 381 (E.D.N.Y. 2017)', 'A commercial website held to be a place of public accommodation.', {'*'}),
    ('National Association of the Deaf v. Netflix, Inc., 869 F. Supp. 2d 196 (D. Mass. 2012)', 'Video without captions; ADA claim allowed against a web-only service.', {'1.2.2', '1.4.2'}),
    ('National Association of the Deaf v. Harvard University (D. Mass., settled 2019)', 'Public online video without accurate captions.', {'1.2.2'}),
]
STATS = ('3,117 federal website accessibility suits were filed under ADA Title III in 2025, about 36 percent of all Title III filings that year', 'https://www.levelaccess.com/blog/2024-u-s-web-accessibility-litigation-key-trends-and-strategies-for-mitigating-risk/')

ECFR = {'§ 36.303': 'https://www.ecfr.gov/current/title-28/chapter-I/part-36/subpart-C/section-36.303', '§ 35.200': 'https://www.ecfr.gov/current/title-28/chapter-I/part-35/subpart-H/section-35.200'}

# Title III has no web-specific provision. Communication barriers (a blind or deaf visitor cannot perceive or operate the content) rest on the effective-communication duty in § 36.303(c)(1); the rest rest on the general auxiliary-aids duty in § 36.303(a). Title II is explicit for every criterion: § 35.200(b)(1).
COMM_SC = {'1.1.1', '1.2.2', '1.4.2', '2.4.2', '2.4.4', '3.1.1', '3.3.2', '4.1.2'}


def ada_for(sc, regime):
    if regime == 'title2':
        return ('28 CFR § 35.200(b)(1)', 'web content must comply with WCAG 2.1 Level A and AA')
    if sc in COMM_SC:
        return ('28 CFR § 36.303(c)(1)', 'furnish auxiliary aids and services where necessary to ensure effective communication')
    return ('28 CFR § 36.303(a)', 'take the steps necessary so no one with a disability is excluded or treated differently for want of auxiliary aids and services')


ADA_TITLE_III = ('28 CFR § 36.303(c)(1)', 'ADA Title III, public accommodations: a business open to the public must furnish auxiliary aids and services so that people with disabilities are not excluded and communication with them is as effective as with others. The regulation names no web standard; courts and settlements apply WCAG 2.1 AA as the measure, so every item here rests on a WCAG criterion first and names the ADA duty it falls under second.')
ADA_TITLE_II = ('28 CFR § 35.200(b)', 'ADA Title II, state and local government: web content must comply with WCAG 2.1 Level A and AA success criteria (compliance dates 2027-04-26 and 2028-04-26).')

CSS = """
:root{--bg:#f7f7f5;--card:#fff;--ink:#1c1c1a;--muted:#5f5f5a;--line:#e4e4df;
--crit:#b3261e;--ser:#c2570a;--mod:#a8891b;--adv:#2b5fa8;--pass:#2e7d4f;--hum:#6b6b66}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.wrap{max-width:960px;margin:0 auto;padding:32px 20px 64px}
h1{font-size:28px;margin:0 0 4px}h2{font-size:20px;margin:40px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--line)}
.sub{color:var(--muted);margin:0 0 24px}
h1 a:hover{text-decoration:underline}
.meta{border-collapse:collapse;margin:12px 0 18px;width:100%;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}
.meta th{text-align:left;padding:10px 14px;width:220px;color:var(--muted);font-weight:600;vertical-align:top;border-bottom:1px solid var(--line)}
.meta td{padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top}.meta tr:last-child th,.meta tr:last-child td{border-bottom:0}
.meta ul{margin:6px 0 0 18px;padding:0;font-size:14px}.meta li{margin:2px 0}
.verdict{padding:18px 20px;border-radius:10px;color:#fff;font-size:18px;font-weight:600;margin:16px 0 24px}
.v-fail{background:var(--crit)}.v-warn{background:var(--ser)}.v-ok{background:var(--pass)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:12px;margin:0 0 8px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.card .n{font-size:30px;font-weight:700;line-height:1}.card .l{color:var(--muted);font-size:13px;margin-top:4px}
.c-crit .n{color:var(--crit)}.c-ser .n{color:var(--ser)}.c-mod .n{color:var(--mod)}.c-adv .n{color:var(--adv)}.c-pass .n{color:var(--pass)}.c-hum .n{color:var(--hum)}
.f{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--line);border-radius:10px;padding:14px 18px;margin:10px 0}
.f-CRITICAL{border-left-color:var(--crit)}.f-SERIOUS{border-left-color:var(--ser)}.f-MODERATE{border-left-color:var(--mod)}.f-ADVISORY{border-left-color:var(--adv)}.f-PASS{border-left-color:var(--pass)}.f-HUMAN{border-left-color:var(--hum)}
.tag{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.04em;padding:2px 8px;border-radius:999px;color:#fff;margin-right:8px;vertical-align:middle}
.t-CRITICAL{background:var(--crit)}.t-SERIOUS{background:var(--ser)}.t-MODERATE{background:var(--mod)}.t-ADVISORY{background:var(--adv)}.t-PASS{background:var(--pass)}.t-HUMAN{background:var(--hum)}
.f h3{display:inline;font-size:17px;margin:0;vertical-align:middle}
.f p{margin:8px 0 0}.f .why{color:var(--muted)}
.f .where{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;background:#f1f1ee;padding:2px 6px;border-radius:4px}
.cite{font-size:13px;color:var(--muted);margin-top:8px;border-top:1px dashed var(--line);padding-top:8px}
.cite b{color:var(--ink)}
.note{background:#fff8e6;border:1px solid #f0dca0;border-radius:10px;padding:12px 16px;margin:24px 0;font-size:14px}
.foot{color:var(--muted);font-size:13px;margin-top:40px}
.verdict ul{margin:8px 0 0 18px;padding:0;font-weight:500;font-size:16px}.verdict li{margin:4px 0}.verdict a{color:#fff}
details.sec{margin:18px 0;border:1px solid var(--line);border-radius:12px;background:var(--card);overflow:hidden}
details.sec>summary{cursor:pointer;list-style:none;padding:14px 18px;display:flex;align-items:center;gap:12px;font-size:17px;font-weight:600}
details.sec>summary::-webkit-details-marker{display:none}
details.sec>summary::before{content:"▶";font-size:18px;line-height:1;color:var(--ink);background:#e9e9e4;border-radius:8px;width:34px;height:34px;display:inline-flex;align-items:center;justify-content:center;flex:0 0 34px;transition:transform .2s}details.sec[open]>summary::before{transform:rotate(90deg)}
details.sec>summary:hover::before{background:#dcdcd5}
details.sec .body{padding:0 14px 14px}
.stag{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.04em;padding:3px 10px;border-radius:999px;color:#fff}
.s-CRITICAL{background:var(--crit)}.s-SERIOUS{background:var(--ser)}.s-MODERATE{background:var(--mod)}.s-ADVISORY{background:var(--adv)}.s-PASS{background:var(--pass)}.s-HUMAN{background:var(--hum)}
.count{color:var(--muted);font-weight:500;font-size:14px}
details.sec[open]>summary{color:#fff}details.sec[open]>summary .count{color:rgba(255,255,255,.85)}
details.sec[open]>summary::before{background:rgba(255,255,255,.22);color:#fff}details.sec[open]>summary:hover::before{background:rgba(255,255,255,.35)}
details.sec-CRITICAL[open]>summary{background:var(--crit)}details.sec-SERIOUS[open]>summary{background:var(--ser)}details.sec-MODERATE[open]>summary{background:var(--mod)}details.sec-ADVISORY[open]>summary{background:var(--adv)}details.sec-PASS[open]>summary{background:var(--pass)}details.sec-HUMAN[open]>summary{background:var(--hum)}
details.sec-CRITICAL[open]>summary .stag{background:#fff;color:var(--crit)}details.sec-SERIOUS[open]>summary .stag{background:#fff;color:var(--ser)}details.sec-MODERATE[open]>summary .stag{background:#fff;color:var(--mod)}details.sec-ADVISORY[open]>summary .stag{background:#fff;color:var(--adv)}details.sec-PASS[open]>summary .stag{background:#fff;color:var(--pass)}details.sec-HUMAN[open]>summary .stag{background:#fff;color:var(--hum)}
details.sec[open] .body{padding-top:12px}
.cases{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-top:32px}
.cases h2{margin-top:0;border:0;padding:0}.cases li{margin:8px 0}.cases .m{color:var(--muted);font-size:14px}
.f .head{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.reflink{color:var(--adv);font-weight:600;font-size:13px;text-decoration:none;white-space:nowrap;margin-left:auto}.reflink:hover{text-decoration:underline}
.drawer{position:fixed;top:0;right:0;height:100%;width:min(560px,92vw);background:var(--card);border-left:1px solid var(--line);box-shadow:-8px 0 30px rgba(0,0,0,.15);transform:translateX(105%);transition:transform .25s ease;overflow-y:auto;padding:24px 28px 40px;z-index:20}
.drawer.open{transform:none}.drawer h3{margin:0 0 4px;font-size:18px}.drawer h4{margin:22px 0 6px;font-size:15px;color:var(--muted)}
.drawer pre{white-space:pre-wrap;font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;background:#f6f6f3;border:1px solid var(--line);border-radius:8px;padding:12px 14px;margin:0}
.drawer .x{position:absolute;top:14px;right:16px;border:0;background:#eee;border-radius:999px;width:32px;height:32px;font-size:18px;cursor:pointer}
.drawer .src{font-size:12px;color:var(--muted);margin-top:6px}
.shade{position:fixed;inset:0;background:rgba(0,0,0,.25);opacity:0;pointer-events:none;transition:opacity .25s;z-index:10}.shade.on{opacity:1;pointer-events:auto}
@media(max-width:520px){.wrap{padding:20px 16px 48px}h1{font-size:22px}}
"""


def _tag(cls):
    return {'CRITICAL': 'CRITICAL', 'SERIOUS': 'SERIOUS', 'MODERATE': 'MODERATE', 'ADVISORY': 'ADVISORY', 'PASS': 'PASS', 'NEEDS HUMAN': 'HUMAN'}[cls]


def _finding(cls, sc, sc_name, level, location, measured, note, ada, regime='title3'):
    plain_title, plain_why = PLAIN.get(sc, (sc_name, ''))
    ada = ada_for(sc, regime)
    k = _tag(cls)
    where = f'<p>Where: <span class="where">{H.escape(location)}</span></p>' if location else ''
    link = f'<a class="reflink" href="#" data-sc="{H.escape(sc)}" data-ada="{H.escape(ada[0].split("(")[0].replace("28 CFR ", "").strip())}" onclick="return showRef(this)">Click to see the full text reference →</a>'
    return f"""<div class="f f-{k}"><div class="head"><span class="tag t-{k}">{H.escape(cls)}</span><h3>{H.escape(plain_title)}</h3>{link}</div>
{where}<p>{H.escape(measured)}</p><p class="why">{H.escape(note)} {H.escape(plain_why)}</p>
<div class="cite"><b>Rule:</b> WCAG 2.1 SC {H.escape(sc)} {H.escape(sc_name)} (Level {H.escape(level)}) · <b>ADA law:</b> {H.escape(ada[0])}, {H.escape(ada[1])}</div></div>"""


def render_html(results, sc_index, regime='title3'):
    ada = ADA_TITLE_II if regime == 'title2' else ADA_TITLE_III
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    tot = {'CRITICAL': 0, 'SERIOUS': 0, 'MODERATE': 0, 'ADVISORY': 0, 'PASS': 0, 'NEEDS HUMAN': 0}
    body = []
    for r in results:
        F, P, Hm = r['findings'], r['passes'], r['human']
        for (sev, _), *_x in F:
            tot[sev] += 1
        tot['PASS'] += len(P)
        tot['NEEDS HUMAN'] += len(Hm)
    nfail = tot['CRITICAL'] + tot['SERIOUS'] + tot['MODERATE'] + tot['ADVISORY']
    if tot['CRITICAL'] or tot['SERIOUS']:
        vcls = 'v-fail'
    elif nfail:
        vcls = 'v-warn'
    else:
        vcls = 'v-ok'
    bullets = [f"{tot['CRITICAL']} critical and {tot['SERIOUS']} serious barriers found across {len(results)} page{'s' if len(results) != 1 else ''}." if (tot['CRITICAL'] or tot['SERIOUS']) else f"No critical or serious barriers found by the automated checks."]
    if tot['MODERATE'] or tot['ADVISORY']:
        bullets.append(f"{tot['MODERATE']} moderate and {tot['ADVISORY']} advisory issues.")
    bullets.append(f"{tot['PASS']} checks in compliance. {tot['NEEDS HUMAN']} items need a person to confirm.")
    bullets.append(f'These are the kinds of barriers named in ADA website lawsuits: <a href="{STATS[1]}">{H.escape(STATS[0])}</a>. Related cases are listed at the bottom of this report.')
    first = results[0]['src']
    is_site = first.startswith('http')
    if is_site:
        site = urllib.parse.urlparse(first)
        site_url = f'{site.scheme}://{site.netloc}/'
        headline = f'<a href="{H.escape(site_url)}" style="color:inherit;text-decoration:none">ADA Website Compliance Audit</a>'
        what_label, what_value = 'Website audited', f'<a href="{H.escape(site_url)}">{H.escape(site_url)}</a>'
    else:
        headline = 'ADA Website Compliance Audit'
        what_label, what_value = 'Test file audited (not a live website)', H.escape(first)
    pages = ''.join(f'<li><a href="#p{i}">{H.escape(r["src"])}</a> — {sum(1 for _ in r["findings"])} fail · {len(r["passes"])} pass · {len(r["human"])} needs a person</li>' for i, r in enumerate(results))
    sec_key = ada[0].split('(')[0].replace('28 CFR ', '').strip()
    ecfr = ECFR.get(sec_key, '#')
    now_dt = datetime.datetime.now()
    body.append(f"""<div class="wrap"><h1>{headline}</h1>
<table class="meta"><tr><th>{what_label}</th><td>{what_value}</td></tr>
<tr><th>Pages audited</th><td>{len(results)}<ul>{pages}</ul></td></tr>
<tr><th>Date audited</th><td>{now_dt.strftime('%B %-d, %Y')}</td></tr>
<tr><th>Time</th><td>{now_dt.strftime('%-I:%M %p')} Pacific Time</td></tr>
<tr><th>ADA standard</th><td><a href="{ecfr}">{H.escape(ada[0].split('(')[0].strip())}</a> — the regulation, which {'requires' if regime == 'title2' else 'is applied by courts using'} <a href="https://www.w3.org/TR/WCAG21/">WCAG 2.1 Level A and AA</a> as the technical measure. Both are in this folder's reference/ verbatim. Each item below names the WCAG criterion it fails or meets and the ADA paragraph that duty falls under.</td></tr></table>
<p class="sub"><a href="#" onclick="return showAll()" style="color:var(--adv);font-weight:600;text-decoration:none">Click here to see the full text of the ADA standards that apply to websites →</a></p>
<div class="verdict {vcls}">What was found<ul>{''.join('<li>' + b + '</li>' for b in bullets)}</ul></div>
<div class="cards">
<div class="card c-crit"><div class="n">{tot['CRITICAL']}</div><div class="l">Critical: blocks a task</div></div>
<div class="card c-ser"><div class="n">{tot['SERIOUS']}</div><div class="l">Serious: major barrier</div></div>
<div class="card c-mod"><div class="n">{tot['MODERATE']}</div><div class="l">Moderate: degrades use</div></div>
<div class="card c-adv"><div class="n">{tot['ADVISORY']}</div><div class="l">Advisory: likely issue</div></div>
<div class="card c-pass"><div class="n">{tot['PASS']}</div><div class="l">In compliance</div></div>
<div class="card c-hum"><div class="n">{tot['NEEDS HUMAN']}</div><div class="l">Needs a person to check</div></div>
</div>
<div class="note"><b>What this is.</b> {H.escape(ada[1])} Each item below names the rule in plain words, where on the page it was found, what was measured, and the exact provision, with the full text one click away. The provision text is in the reference/ folder so anyone can check the finding against the law. This is a technical conformance report, not legal advice.</div>""")
    groups = [('CRITICAL', 'Critical', 'blocks a task for some visitors', True), ('SERIOUS', 'Serious', 'major barrier', True), ('MODERATE', 'Moderate', 'degrades use but passable', False), ('ADVISORY', 'Advisory', 'likely issue, needs judgment', False)]
    scs_found = set()
    for r in results:
        F, P, Hm = r['findings'], r['passes'], r['human']
        i = results.index(r)
        body.append(f'<h2 id="p{i}">{"Page: " if len(results) > 1 else ""}{H.escape(r["src"])}</h2>' if len(results) > 1 else f'<span id="p{i}"></span>')
        body.append('<h2>Where you are out of compliance</h2>' if len(results) == 1 else '<h3>Where you are out of compliance</h3>')
        if not F:
            body.append('<p>Nothing found by the automated checks.</p>')
        for key, label, desc, openit in groups:
            items = [x for x in F if x[0][0] == key]
            if not items:
                continue
            scs_found.update(x[1] for x in items)
            body.append(f'<details class="sec sec-{key}"{" open" if openit else ""}><summary><span class="stag s-{key}">{label}</span> {H.escape(desc)} <span class="count">· {len(items)} found</span></summary><div class="body">')
            for (sev, _), sc, location, measured, note in sorted(items, key=lambda x: x[1]):
                d = sc_index[sc]
                body.append(_finding(sev, sc, d['name'], d['level'], location, measured, note, ada, regime))
            body.append('</div></details>')
        body.append('<h2>Where you are in compliance</h2>')
        body.append(f'<details class="sec sec-PASS"><summary><span class="stag s-PASS">In compliance</span> checks this page passed <span class="count">· {len(P)}</span></summary><div class="body">')
        for sc, what in P:
            d = sc_index[sc]
            body.append(_finding('PASS', sc, d['name'], d['level'], '', what, '', ada, regime))
        body.append('</div></details>')
        body.append('<h2>Needs a person to check</h2>')
        body.append(f'<details class="sec sec-HUMAN"><summary><span class="stag s-HUMAN">Needs a person</span> the program cannot decide these <span class="count">· {len(Hm)}</span></summary><div class="body">')
        for sc, location, q in Hm:
            d = sc_index[sc]
            body.append(_finding('NEEDS HUMAN', sc, d['name'], d['level'], location, q, '', ada, regime))
        body.append('</div></details>')
    # related case law, filtered to the barriers found (general cases always shown)
    rel = [c for c in CASES if '*' in c[2] or (c[2] & scs_found)]
    body.append('<div class="cases"><h2>Related case law</h2><p class="m">Real ADA website cases involving the kinds of barriers found above. Background for the reader; the findings themselves cite the standard, not these cases. Full list with the barrier each case turned on: reference/related-case-law.md.</p><ul>')
    for cap, what, scs in rel:
        q = H.escape(cap.split(',')[0])
        body.append(f'<li><b>{H.escape(cap)}</b> — {H.escape(what)} <a href="https://www.courtlistener.com/?q={q.replace(" ", "+")}">docket search →</a></li>')
    body.append(f'</ul><p class="m">Volume: <a href="{STATS[1]}">{H.escape(STATS[0])}</a>. The barriers named most often in complaints are missing image descriptions, unlabeled form fields, and pages that cannot be used with a keyboard (<a href="https://accessible.org/lawsuits/">Accessible.org</a>).</p></div>')
    prov = load_provisions()
    import json
    pj = json.dumps({k: {'title': v[0], 'text': v[1]} for k, v in prov.items()})
    body.append(f"""<div class="shade" id="shade" onclick="closeRef()"></div>
<div class="drawer" id="drawer" role="dialog" aria-modal="true" aria-labelledby="dtitle"><button class="x" onclick="closeRef()" aria-label="Close">×</button><h3 id="dtitle"></h3><div class="src">Verbatim from reference/. WCAG 2.1: W3C, fetched 2026-09-11. CFR: eCFR edition 2026-09-01.</div><h4 id="h1"></h4><pre id="t1"></pre><h4 id="h2"></h4><pre id="t2"></pre></div>
<script>
var PROV = {pj};
function showRef(a) {{
  var sc = PROV[a.getAttribute('data-sc')] || {{title:'', text:'(not found)'}};
  var ada = PROV[a.getAttribute('data-ada')] || {{title:'', text:'(not found)'}};
  document.getElementById('dtitle').textContent = 'Full text of the rule and the law';
  document.getElementById('h1').textContent = 'WCAG 2.1 ' + sc.title;
  document.getElementById('t1').textContent = sc.text;
  document.getElementById('h2').textContent = ada.title;
  document.getElementById('t2').textContent = ada.text;
  document.getElementById('drawer').classList.add('open');
  document.getElementById('shade').classList.add('on');
  return false;
}}
function showAll() {{
  var ada = PROV['{ada[0].split('(')[0].replace('28 CFR ', '').strip()}'] || {{title:'', text:''}};
  var keys = Object.keys(PROV).filter(function(k) {{ return k.indexOf('§') < 0; }}).sort(function(a, b) {{ return a.localeCompare(b, undefined, {{numeric: true}}); }});
  var all = keys.map(function(k) {{ return 'WCAG 2.1 ' + PROV[k].title + '\\n\\n' + PROV[k].text; }}).join('\\n\\n' + '—'.repeat(30) + '\\n\\n');
  document.getElementById('dtitle').textContent = 'The ADA standards that apply to websites';
  document.getElementById('h1').textContent = ada.title;
  document.getElementById('t1').textContent = ada.text;
  document.getElementById('h2').textContent = 'WCAG 2.1, all ' + keys.length + ' Level A and AA success criteria (the technical measure the regulation adopts)';
  document.getElementById('t2').textContent = all;
  document.getElementById('drawer').classList.add('open');
  document.getElementById('shade').classList.add('on');
  return false;
}}
function closeRef() {{
  document.getElementById('drawer').classList.remove('open');
  document.getElementById('shade').classList.remove('on');
}}
document.addEventListener('keydown', function(e) {{ if (e.key === 'Escape') closeRef(); }});
</script>""")
    body.append(f"""<p class="foot">Totals — FAIL: {nfail} · PASS: {tot['PASS']} · NEEDS HUMAN: {tot['NEEDS HUMAN']}. Zero failures from the automated pass is not a compliance certificate; the "needs a person" items and the checks in rules.md section 6 must be done by hand. Generated by ada-web-auditor, tools/audit.py.</p></div>""")
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>ADA Website Compliance Audit</title><style>{CSS}</style></head><body>{"".join(body)}</body></html>'
