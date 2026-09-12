#!/usr/bin/env python3
"""ADA web auditor, mechanical pass. Python 3 standard library only.

Reads one or more HTML files (or URLs), runs deterministic checks that map to
WCAG 2.1 Level A / AA success criteria, and writes a markdown report whose
every finding carries: location (file:line), severity, measured value, and the
provision cited. It also prints PASS for every check that passed and marks
anything it cannot decide as NEEDS HUMAN. It never guesses.

Usage:
  python3 tools/audit.py fixtures/bad-store.html                          # markdown to stdout
  python3 tools/audit.py page.html --html reports/page.html               # readable HTML report
  python3 tools/audit.py https://example.com --html r.html -o r.md        # whole site: home page plus up to 7 same-site pages
  python3 tools/audit.py https://example.com --crawl 1 --html r.html      # this page only
  python3 tools/audit.py city.gov --regime title2 --html r.html           # government site

Exit code: 0 always (the report is the output). Use tools/check_audit.py to
validate a report against reference/.
"""
import sys, re, json, os, argparse, datetime, urllib.request, urllib.parse
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, '..', 'reference')
SC_INDEX = {d['sc']: d for d in json.load(open(os.path.join(REF, 'wcag21-sc-index.json')))}

# Severity classes, defined in rules.md. Colour marks are part of the class.
CRITICAL = ('CRITICAL', '🔴')
SERIOUS = ('SERIOUS', '🟠')
MODERATE = ('MODERATE', '🟡')
ADVISORY = ('ADVISORY', '🔵')
PASS = ('PASS', '🟢')
HUMAN = ('NEEDS HUMAN', '⚪')

GENERIC_LINK_TEXT = {'click here', 'here', 'read more', 'more', 'learn more', 'link', 'this', 'continue', 'details'}


def cite(sc):
    d = SC_INDEX[sc]
    return f"WCAG 2.1 SC {sc} {d['name']} (Level {d['level']})"


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []            # (tag, attrs, line)
        self.stack = []           # open tags for text capture
        self.text_of = {}         # index in tags -> collected text
        self.ids = {}
        self.lang = None
        self.title = None
        self.title_open = False
        self.headings = []
        self.labels_for = set()
        self.has_skip_link = False
        self.first_focusable_line = None
        self.in_noscript = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        idx = len(self.tags)
        if self.in_noscript:
            a['_noscript'] = '1'
        self.tags.append((tag, a, line))
        # a child's alt, aria-label, or svg <title> contributes to the accessible name of an open a/button/label
        child_name = a.get('alt') or a.get('aria-label') or ''
        if child_name:
            for open_idx in self.stack:
                self.text_of[open_idx] += ' ' + child_name
        if tag in ('a', 'button', 'label', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title'):
            self.stack.append(idx)
            self.text_of[idx] = ''
        if tag == 'noscript':
            self.in_noscript += 1
        if tag == 'html':
            self.lang = (a.get('lang') or '').strip()
        if tag == 'title':
            self.title_open = True
        if tag == 'label' and a.get('for'):
            self.labels_for.add(a['for'])
        # ids: only elements a user or assistive tech can reach; head-only resources and noscript fallbacks are excluded
        if a.get('id') and tag not in ('link', 'style', 'script', 'meta', 'noscript') and not self.in_noscript:
            self.ids.setdefault(a['id'], []).append(line)
        if tag in ('input', 'select', 'textarea') and any(self.tags[i][0] == 'label' for i in self.stack):
            a['_implicit_label'] = '1'
        if tag in ('a', 'button', 'input', 'select', 'textarea') and self.first_focusable_line is None:
            self.first_focusable_line = line

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag in ('a', 'button', 'label', 'title'):
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag == 'noscript' and self.in_noscript:
            self.in_noscript -= 1
        if self.stack and self.tags[self.stack[-1]][0] == tag:
            idx = self.stack.pop()
            if tag == 'title':
                self.title = self.text_of[idx].strip()
                self.title_open = False
            if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                self.headings.append((int(tag[1]), self.text_of[idx].strip(), self.tags[idx][2]))

    def handle_data(self, data):
        for idx in self.stack:
            self.text_of[idx] += data


def luminance(hexcol):
    hexcol = hexcol.lstrip('#')
    if len(hexcol) == 3:
        hexcol = ''.join(c * 2 for c in hexcol)
    if len(hexcol) != 6:
        return None
    try:
        r, g, b = (int(hexcol[i:i + 2], 16) / 255 for i in (0, 2, 4))
    except ValueError:
        return None
    lin = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast(fg, bg):
    l1, l2 = luminance(fg), luminance(bg)
    if l1 is None or l2 is None:
        return None
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def load(src):
    if re.match(r'https?://', src):
        req = urllib.request.Request(src, headers={'User-Agent': 'ada-web-auditor/1.0 (stdlib)', 'Accept-Encoding': 'gzip, identity'})
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read()
            enc = (r.headers.get('Content-Encoding') or '').lower()
            if 'gzip' in enc or raw[:2] == b'\x1f\x8b':
                import gzip
                raw = gzip.decompress(raw)
            elif enc in ('br', 'zstd'):
                raise ValueError(f'server sent {enc} compression, which the Python standard library cannot decode; save the page from a browser (File > Save Page As, HTML only) and pass the file')
            return raw.decode('utf-8', errors='replace')
    return open(src, encoding='utf-8', errors='replace').read()


def audit(src):
    html = load(src)
    if not re.search(r'<\s*(!doctype\s+html|html|head|body|title|div|p|table|a|img|h[1-6]|form)\b', html, re.I):
        return dict(src=src, findings=[], passes=[], human=[('4.1.1', f'{src}:1', f'input does not look like an HTML document ({len(html)} bytes, no html/head/body element). Nothing was audited. Pass the served HTML of a web page.')], title=None)
    p = Page()
    p.feed(html)
    F = []   # findings: (severity, sc, location, measured, note)
    P = []   # passes: (sc, check)
    H = []   # needs human: (sc, location, question)
    loc = lambda line: f"{src}:{line}"

    # 3.1.1 Language of Page
    html_line = next((t[2] for t in p.tags if t[0] == 'html'), 1)
    if not p.lang:
        F.append((SERIOUS, '3.1.1', loc(html_line), 'html element has no lang attribute', 'Screen readers cannot pick a pronunciation ruleset.'))
    else:
        P.append(('3.1.1', f'html lang="{p.lang}"'))

    # 2.4.2 Page Titled
    if p.title is None or not p.title:
        F.append((SERIOUS, '2.4.2', loc(1), 'no <title> or empty <title>', 'The page has no programmatic title.'))
    else:
        P.append(('2.4.2', f'title = "{p.title[:60]}"'))

    # 1.1.1 Non-text Content: img alt
    imgs = [(a, l) for t, a, l in p.tags if t == 'img' and '_noscript' not in a]
    missing = [(a, l) for a, l in imgs if 'alt' not in a and a.get('role') not in ('presentation', 'none') and not a.get('aria-label') and not a.get('aria-labelledby') and a.get('aria-hidden') != 'true']
    for a, l in missing:
        F.append((CRITICAL, '1.1.1', loc(l), f"<img src=\"{a.get('src', '')[:60]}\"> has no alt, aria-label, or aria-labelledby", 'No text alternative; a screen reader announces the filename or nothing.'))
    if imgs and not missing:
        P.append(('1.1.1', f'{len(imgs)} img elements all carry a text alternative (alt, aria-label, or aria-labelledby; empty alt on decorative images is allowed)'))
    for a, l in imgs:
        if a.get('alt') and re.search(r'\.(png|jpe?g|gif|svg|webp)$', a['alt'].strip(), re.I):
            F.append((SERIOUS, '1.1.1', loc(l), f"alt=\"{a['alt']}\" is a filename", 'A filename is not a text alternative that serves the equivalent purpose.'))
        elif a.get('alt') and 'alt' in a and 'aria-hidden' not in a:
            H.append(('1.1.1', loc(l), f"alt=\"{a['alt'][:80]}\": does this describe the image's purpose? The scanner cannot judge meaning."))

    # 1.3.1 / 3.3.2 / 4.1.2 form controls without an accessible name
    controls = [(t, a, l) for t, a, l in p.tags if t in ('input', 'select', 'textarea') and a.get('type') not in ('hidden', 'submit', 'button', 'reset', 'image') and 'hidden' not in a and a.get('aria-hidden') != 'true' and '_noscript' not in a]
    unlabeled = []
    for t, a, l in controls:
        named = a.get('id') in p.labels_for or a.get('_implicit_label') or a.get('aria-label') or a.get('aria-labelledby') or a.get('title')
        if not named:
            unlabeled.append((t, a, l))
            F.append((CRITICAL, '4.1.2', loc(l), f"<{t} name=\"{a.get('name', '')}\" type=\"{a.get('type', 'text')}\"> has no label, aria-label, aria-labelledby, or title", 'The control has no accessible name. Also fails SC 3.3.2 Labels or Instructions (Level A).'))
    if controls and not unlabeled:
        P.append(('4.1.2', f'{len(controls)} form controls all have an accessible name'))
        P.append(('3.3.2', f'{len(controls)} form controls all have a label or instruction'))
    for t, a, l in controls:
        if a.get('placeholder') and not (a.get('id') in p.labels_for or a.get('_implicit_label') or a.get('aria-label') or a.get('aria-labelledby')):
            H.append(('3.3.2', loc(l), 'placeholder text is the only visible label; it disappears on input. A human should confirm a persistent label exists.'))

    # 2.4.4 Link Purpose (In Context)
    links = [(i, a, l) for i, (t, a, l) in enumerate(p.tags) if t == 'a' and 'href' in a]
    empty_links, generic = [], []
    for i, a, l in links:
        text = re.sub(r'\s+', ' ', p.text_of.get(i, '')).strip()
        name = text or a.get('aria-label') or a.get('title') or ''
        if not name:
            # an <img alt> inside would be caught as text only if we tracked it; check following tag
            nxt = p.tags[i + 1] if i + 1 < len(p.tags) else None
            if nxt and nxt[0] == 'img' and nxt[1].get('alt'):
                name = nxt[1]['alt']
        if not name:
            empty_links.append(l)
            F.append((CRITICAL, '2.4.4', loc(l), f"<a href=\"{a['href'][:60]}\"> has no link text, aria-label, or image alt", 'The link purpose cannot be determined from the link text.'))
        elif name.lower().strip('.!') in GENERIC_LINK_TEXT:
            generic.append(l)
            H.append(('2.4.4', loc(l), f"link text \"{name}\": SC 2.4.4 allows purpose to come from the programmatically determined context (same sentence, paragraph, list item, or table cell). A human must read the context; the scanner only sees the generic text."))
    if links and not empty_links:
        P.append(('2.4.4', f'{len(links)} links all have a text, aria-label, or image alt'))

    # 4.1.2 buttons and iframes with no name
    for i, (t, a, l) in enumerate(p.tags):
        if t == 'button':
            name = re.sub(r'\s+', ' ', p.text_of.get(i, '')).strip() or a.get('aria-label') or a.get('aria-labelledby') or a.get('title')
            if not name:
                F.append((CRITICAL, '4.1.2', loc(l), '<button> has no text, aria-label, aria-labelledby, or named child', 'The button has no accessible name.'))
        if t == 'iframe' and '_noscript' not in a and not (a.get('title') or a.get('aria-label')):
            F.append((SERIOUS, '4.1.2', loc(l), f"<iframe src=\"{a.get('src', '')[:60]}\"> has no title", 'The frame has no accessible name.'))

    # 4.1.1 Parsing: duplicate ids
    dups = {k: v for k, v in p.ids.items() if len(v) > 1}
    for k, v in dups.items():
        F.append((MODERATE, '4.1.1', loc(v[1]), f"id=\"{k}\" appears {len(v)} times (lines {', '.join(map(str, v))})", 'IDs are not unique; label/for and aria references become ambiguous.'))
    if p.ids and not dups:
        P.append(('4.1.1', f'{len(p.ids)} ids, all unique'))

    # 1.3.1 heading structure (advisory: WCAG does not forbid a skipped level; it requires structure be programmatic)
    if p.headings:
        if not any(h[0] == 1 for h in p.headings):
            H.append(('1.3.1', loc(p.headings[0][2]), 'page has headings but no h1. WCAG 2.1 does not require an h1; a human should confirm the visual structure is conveyed programmatically.'))
        prev = 0
        for lvl, txt, l in p.headings:
            if prev and lvl > prev + 1:
                F.append((ADVISORY, '1.3.1', loc(l), f'heading level jumps from h{prev} to h{lvl} ("{txt[:40]}")', 'Skipped level; structure may not match the visual hierarchy. Advisory because WCAG 2.1 does not prohibit skips outright.'))
            prev = lvl
        P.append(('1.3.1', f'{len(p.headings)} headings present as heading elements'))
    else:
        H.append(('1.3.1', loc(1), 'no heading elements at all. If the page visually has section titles, that is a 1.3.1 failure; a human must look.'))

    # 1.4.3 Contrast (Minimum): inline style with both color and background-color in hex
    for t, a, l in p.tags:
        st = a.get('style', '')
        fg = re.search(r'(?<![-\w])color\s*:\s*(#[0-9a-fA-F]{3,6})', st)
        bg = re.search(r'background(?:-color)?\s*:\s*(#[0-9a-fA-F]{3,6})', st)
        if fg and bg:
            r = contrast(fg.group(1), bg.group(1))
            if r is None:
                continue
            big = re.search(r'font-size\s*:\s*(\d+)(px|pt)', st)
            large = bool(big and ((big.group(2) == 'px' and int(big.group(1)) >= 24) or (big.group(2) == 'pt' and int(big.group(1)) >= 18)))
            need = 3.0 if large else 4.5
            if r < need:
                F.append((SERIOUS, '1.4.3', loc(l), f"<{t}> text {fg.group(1)} on {bg.group(1)} = {r:.2f}:1, below {need}:1", 'Contrast below the minimum for ' + ('large' if large else 'normal') + ' text.'))
            else:
                P.append(('1.4.3', f'line {l}: {fg.group(1)} on {bg.group(1)} = {r:.2f}:1, meets {need}:1'))
    if not any(x[1] == '1.4.3' for x in F) and not any(x[0] == '1.4.3' for x in P):
        H.append(('1.4.3', loc(1), 'no inline colour pairs to measure. Contrast set in a stylesheet needs a rendered-page tool (a browser) or a human with a colour picker.'))

    # 1.4.4 Resize text: viewport that blocks zoom
    for t, a, l in p.tags:
        if t == 'meta' and a.get('name', '').lower() == 'viewport':
            c = a.get('content', '').replace(' ', '').lower()
            ms = re.search(r'maximum-scale=([\d.]+)', c)
            if 'user-scalable=no' in c or 'user-scalable=0' in c or (ms and float(ms.group(1)) < 2):
                F.append((SERIOUS, '1.4.4', loc(l), f'viewport content="{a.get("content")}"', 'Pinch zoom disabled or capped below 200%.'))
            else:
                P.append(('1.4.4', f'viewport "{a.get("content")}" does not block zoom'))

    # 1.2.2 captions, 1.4.2 audio control
    for i, (t, a, l) in enumerate(p.tags):
        if t == 'video':
            j, has_track = i + 1, False
            while j < len(p.tags) and p.tags[j][0] in ('source', 'track'):
                if p.tags[j][0] == 'track' and p.tags[j][1].get('kind', 'subtitles') in ('captions', 'subtitles'):
                    has_track = True
                j += 1
            if not has_track and ('muted' in a or a.get('aria-hidden') == 'true'):
                H.append(('1.2.2', loc(l), '<video muted> with no captions track. A muted animation with no audio needs no captions; if the file carries speech or meaningful sound, captions are required. A human must play it.'))
            elif not has_track:
                F.append((CRITICAL, '1.2.2', loc(l), '<video> has no <track kind="captions">', 'Prerecorded synchronized media with no captions track. If the video has no audio track, this is instead a human check.'))
            else:
                P.append(('1.2.2', f'line {l}: video has a captions/subtitles track'))
        if t in ('video', 'audio') and 'autoplay' in a and 'controls' not in a and 'muted' not in a:
            F.append((CRITICAL, '1.4.2', loc(l), f'<{t} autoplay> with no controls and not muted', 'Audio plays automatically with no mechanism to pause, stop, or control volume.'))

    # 2.2.1 Timing Adjustable: meta refresh
    for t, a, l in p.tags:
        if t == 'meta' and a.get('http-equiv', '').lower() == 'refresh':
            F.append((SERIOUS, '2.2.1', loc(l), f'meta refresh content="{a.get("content")}"', 'Time limit or redirect the user cannot turn off, adjust, or extend.'))

    # 2.1.1 Keyboard: mouse-only handlers, positive tabindex (2.4.3)
    for t, a, l in p.tags:
        if ('onmouseover' in a or 'onmouseenter' in a) and 'onfocus' not in a:
            H.append(('2.1.1', loc(l), f'<{t}> has a mouse-hover handler and no focus handler. If the hover reveals content or function, keyboard users cannot reach it.'))
        if 'onclick' in a and t not in ('a', 'button', 'input', 'select', 'textarea') and 'tabindex' not in a and 'onkeydown' not in a and 'onkeypress' not in a:
            F.append((SERIOUS, '2.1.1', loc(l), f'<{t} onclick> is not focusable (no tabindex) and has no key handler', 'Function operable by mouse only.'))
        ti = a.get('tabindex')
        if ti and ti.lstrip('-').isdigit() and int(ti) > 0:
            F.append((ADVISORY, '2.4.3', loc(l), f'<{t} tabindex="{ti}">', 'Positive tabindex overrides document order; focus order may not preserve meaning. Advisory because the criterion is about the resulting order, which a human must confirm.'))

    # 2.4.1 Bypass Blocks
    skip = any(t == 'a' and a.get('href', '').startswith('#') and re.search(r'skip|main|content', (p.text_of.get(i, '') + a.get('href', '')).lower()) for i, (t, a, l) in enumerate(p.tags))
    landmark = any(t in ('main', 'nav') or a.get('role') in ('main', 'navigation') for t, a, l in p.tags)
    if skip or landmark:
        P.append(('2.4.1', 'skip link or main/nav landmark present' + (' (skip link)' if skip else ' (landmark only)')))
    else:
        n_links = len(links)
        if n_links >= 5:
            F.append((SERIOUS, '2.4.1', loc(1), f'no skip link and no main/nav landmark or role; page has {n_links} links', 'No mechanism to bypass what is almost certainly a repeated navigation block. Confirm the block repeats across pages.'))
        else:
            H.append(('2.4.1', loc(1), f'no skip link or landmark, but only {n_links} links. SC 2.4.1 applies to blocks repeated on multiple pages; a human must say whether any exist.'))

    # 1.3.5 identify input purpose (advisory heuristic)
    for t, a, l in controls:
        n = (a.get('name', '') + ' ' + a.get('id', '')).lower()
        if re.search(r'email|phone|tel|postal|zip|first.?name|last.?name|address', n) and not a.get('autocomplete'):
            F.append((MODERATE, '1.3.5', loc(l), f'<{t} name="{a.get("name")}"> collects user data but has no autocomplete attribute', 'Input purpose for a user-information field is not programmatically identified.'))

    return dict(src=src, findings=F, passes=P, human=H, title=p.title, links=[a.get('href', '') for t, a, l in p.tags if t == 'a' and a.get('href')])


def crawl(start, limit):
    """Breadth-first over same-host links from the start page, up to `limit` pages. Skips files, mailto, anchors, and query-string duplicates."""
    host = urllib.parse.urlparse(start).netloc
    seen, queue, out = set(), [start], []
    while queue and len(out) < limit:
        u = queue.pop(0)
        key = u.split('#')[0].rstrip('/')
        if key in seen:
            continue
        seen.add(key)
        try:
            r = audit(u)
        except Exception as e:
            out.append(dict(src=u, findings=[], passes=[], human=[('4.1.1', f'{u}:1', f'could not fetch or read this page ({e.__class__.__name__}: {str(e)[:160]}). Nothing was audited.')], title=None, links=[]))
            continue
        out.append(r)
        for href in r.get('links', []):
            v = urllib.parse.urljoin(u, href).split('#')[0]
            pu = urllib.parse.urlparse(v)
            if pu.scheme not in ('http', 'https') or pu.netloc != host:
                continue
            if re.search(r'\.(pdf|jpe?g|png|gif|svg|zip|mp4|mp3|css|js|xml|ico)$', pu.path, re.I):
                continue
            if v.rstrip('/') not in seen and v not in queue:
                queue.append(v)
    return out


def render(results):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    out = [f"# ADA web accessibility audit (mechanical pass)\n", f"Generated {now} by tools/audit.py. Standard: WCAG 2.1 Level A and AA as adopted by 28 CFR § 35.200(b) and applied by courts under 28 CFR § 36.303 (see reference/). Every finding below cites one success criterion whose verbatim text is in reference/wcag21-level-a-aa-success-criteria.md.\n",
           "Severity key (rules.md): 🔴 CRITICAL blocks a task for some users · 🟠 SERIOUS major barrier · 🟡 MODERATE degrades but passable · 🔵 ADVISORY likely issue, criterion needs judgment · 🟢 PASS · ⚪ NEEDS HUMAN.\n",
           "This is the mechanical pass only. It cannot see rendered styling, keyboard focus behaviour, dynamic content, or meaning. rules.md section 4 lists what a human must still check before calling a page conformant.\n"]
    tf = tp = th = 0
    for r in results:
        F, P, H = r['findings'], r['passes'], r['human']
        tf += len(F); tp += len(P); th += len(H)
        out.append(f"\n## {r['src']}\n")
        out.append(f"Page title: {r['title'] or '(none)'}\n")
        out.append(f"Result: {len(F)} FAIL · {len(P)} PASS · {len(H)} NEEDS HUMAN\n")
        order = {'CRITICAL': 0, 'SERIOUS': 1, 'MODERATE': 2, 'ADVISORY': 3}
        for (sev, mark), sc, location, measured, note in sorted(F, key=lambda x: (order[x[0][0]], x[1])):
            out.append(f"- {mark} **{sev}** — {cite(sc)} — `{location}` — {measured}. {note}")
        for sc, what in P:
            out.append(f"- 🟢 **PASS** — {cite(sc)} — {what}")
        for sc, location, q in H:
            out.append(f"- ⚪ **NEEDS HUMAN** — {cite(sc)} — `{location}` — {q}")
    out.append(f"\n## Totals\n\nFAIL: {tf} · PASS: {tp} · NEEDS HUMAN: {th}\n")
    out.append("A page with zero FAIL in this report is not thereby conformant. It has passed the checks a program can run. See rules.md section 4.\n")
    return '\n'.join(out) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sources', nargs='+')
    ap.add_argument('-o', '--out', help='markdown report path')
    ap.add_argument('--html', help='HTML report path (the readable one)')
    ap.add_argument('--regime', choices=['title2', 'title3'], default='title3', help='title2 = government site (28 CFR 35.200); title3 = business (28 CFR 36.303)')
    ap.add_argument('--crawl', type=int, default=8, help='for a URL: follow same-site links and audit up to this many pages (default 8; 1 = this page only)')
    args = ap.parse_args()
    results = []
    for src in args.sources:
        if re.match(r'https?://', src) and args.crawl > 1:
            results.extend(crawl(src, args.crawl))
        else:
            try:
                results.append(audit(src))
            except Exception as e:
                results.append(dict(src=src, findings=[], passes=[], human=[('4.1.1', f'{src}:1', f'could not fetch or read this page ({e.__class__.__name__}: {str(e)[:160]}). Nothing was audited.')], title=None, links=[]))
    report = render(results)
    if args.html:
        sys.path.insert(0, HERE)
        from render_html import render_html
        open(args.html, 'w').write(render_html(results, SC_INDEX, args.regime))
        print(f'wrote {args.html}')
    if args.out:
        open(args.out, 'w').write(report)
        print(f'wrote {args.out}')
    elif not args.html:
        sys.stdout.write(report)


if __name__ == '__main__':
    main()
