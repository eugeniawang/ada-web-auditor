"""Standard-library tests for the scanner and the checker. Run: python3 -m unittest discover tests"""
import os, sys, unittest, tempfile, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import audit as A


def scan(html):
    f = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False)
    f.write(html); f.close()
    return A.audit(f.name)


def scs(r, kind):
    return [x[1] for x in r['findings']] if kind == 'fail' else ([x[0] for x in r['passes']] if kind == 'pass' else [x[0] for x in r['human']])


BASE = '<html lang="en"><head><title>t</title></head><body><main><h1>h</h1>%s</main></body></html>'


class Scanner(unittest.TestCase):
    def test_missing_alt_is_critical_1_1_1(self):
        r = scan(BASE % '<img src="a.png">')
        self.assertIn('1.1.1', scs(r, 'fail'))
        self.assertEqual(r['findings'][0][0][0], 'CRITICAL')

    def test_aria_label_on_img_passes(self):
        self.assertNotIn('1.1.1', scs(scan(BASE % '<img src="a.png" role="img" aria-label="gear">'), 'fail'))

    def test_implicit_label_passes(self):
        self.assertNotIn('4.1.2', scs(scan(BASE % '<label>Email <input type="email" name="e" autocomplete="email"></label>'), 'fail'))

    def test_unlabeled_input_is_4_1_2(self):
        self.assertIn('4.1.2', scs(scan(BASE % '<input type="text" name="q">'), 'fail'))

    def test_contrast_ratio_matches_wcag_formula(self):
        self.assertAlmostEqual(A.contrast('#000000', '#ffffff'), 21.0, places=2)
        self.assertAlmostEqual(A.contrast('#999999', '#ffffff'), 2.85, places=2)

    def test_low_contrast_is_1_4_3(self):
        self.assertIn('1.4.3', scs(scan(BASE % '<p style="color:#999999;background-color:#ffffff">x</p>'), 'fail'))

    def test_missing_lang_is_3_1_1(self):
        self.assertIn('3.1.1', scs(scan('<html><head><title>t</title></head><body><main><p>x</p></main></body></html>'), 'fail'))

    def test_muted_video_without_captions_is_human_not_fail(self):
        r = scan(BASE % '<video src="a.mp4" muted></video>')
        self.assertNotIn('1.2.2', scs(r, 'fail')); self.assertIn('1.2.2', scs(r, 'human'))

    def test_video_without_captions_is_critical(self):
        self.assertIn('1.2.2', scs(scan(BASE % '<video src="a.mp4" controls></video>'), 'fail'))

    def test_noscript_iframe_ignored(self):
        self.assertNotIn('4.1.2', scs(scan(BASE % '<noscript><iframe src="x"></iframe></noscript>'), 'fail'))

    def test_zoom_blocked_is_1_4_4(self):
        r = scan('<html lang="en"><head><meta name="viewport" content="width=device-width, user-scalable=no"><title>t</title></head><body><main><h1>h</h1></main></body></html>')
        self.assertIn('1.4.4', scs(r, 'fail'))

    def test_non_html_input_is_one_human_line(self):
        r = scan('just some text with no tags at all')
        self.assertEqual(r['findings'], []); self.assertEqual(len(r['human']), 1)

    def test_clean_fixture_has_zero_fail(self):
        self.assertEqual(A.audit(os.path.join(ROOT, 'fixtures', 'clean-store.html'))['findings'], [])

    def test_every_emitted_sc_is_in_reference(self):
        r = A.audit(os.path.join(ROOT, 'fixtures', 'bad-store.html'))
        for sc in scs(r, 'fail') + scs(r, 'pass') + scs(r, 'human'):
            self.assertIn(sc, A.SC_INDEX)


class Checker(unittest.TestCase):
    def run_checker(self, text):
        f = tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, dir=ROOT); f.write(text); f.close()
        p = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'check_audit.py'), f.name], capture_output=True, text=True, cwd=ROOT)
        os.unlink(f.name); return p.returncode, p.stdout

    def test_real_report_passes(self):
        p = subprocess.run([sys.executable, 'tools/check_audit.py', 'reports/bad-store.md'], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(p.returncode, 0, p.stdout)

    def test_fake_criterion_rejected(self):
        code, out = self.run_checker('- 🔴 **CRITICAL** — WCAG 2.1 SC 9.9.9 Made Up (Level A) — `fixtures/bad-store.html:1` — x.\n\nFAIL: 1 · PASS: 0\n')
        self.assertEqual(code, 1); self.assertIn('not in reference', out)

    def test_fake_cfr_paragraph_rejected(self):
        code, out = self.run_checker('- 🔴 **CRITICAL** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/bad-store.html:1` — 28 CFR § 36.303(z)(9).\n\nFAIL: 1 · PASS: 0\n')
        self.assertEqual(code, 1); self.assertIn('paragraph (z)', out)

    def test_line_outside_file_rejected(self):
        code, out = self.run_checker('- 🔴 **CRITICAL** — WCAG 2.1 SC 1.1.1 Non-text Content (Level A) — `fixtures/bad-store.html:99999` — x.\n\nFAIL: 1 · PASS: 0\n')
        self.assertEqual(code, 1); self.assertIn('outside the file', out)


if __name__ == '__main__':
    unittest.main()
