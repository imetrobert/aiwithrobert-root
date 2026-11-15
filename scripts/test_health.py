"""Offline test of the health check's decision logic. Run: python3 scripts/test_health.py"""
import datetime as dt, json, os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import health_check as h

now = dt.datetime(2026, 11, 14, tzinfo=dt.timezone.utc)
p = tempfile.mktemp()
json.dump({"items": [{"name": "soon", "date": "2026-11-20", "renew": "x"}, {"name": "later", "date": "2027-03-01"},
                     {"name": "unknown", "date": None}]}, open(p, "w"))
rows, notes = h.check_items(p, now)
assert [r[0] for r in rows] == [False, True], rows          # inside 14 days fails, later passes
assert len(notes) == 1 and "no date" in notes[0]            # undated item is a note, not a failure
text, failed = h.render([("Section", rows)], notes)
assert failed == 1 and "**FAIL**" in text and "Notes" in text
assert h.render([("Section", [(True, "a", "b")])], [])[1] == 0

# content checks with a stubbed network
def fake(url, headers=None, tries=3, timeout=20, limit=400000):
    ok_home = '<script type="application/ld+json">{"a":1}</script><script>G-DM4EY880K2 G-Y0FZTVVLBS</script>'
    if url.endswith("/robots.txt"): return 200, "User-agent: *\nAllow: /\n", ""
    if url.endswith("/sitemap.xml"): return 200, "<loc>https://x.test/a</loc><loc>https://x.test/gone</loc>", ""
    if url.endswith("/gone"): return 404, "", "HTTP 404"
    if url.endswith("feed.xml"): return 200, "<lastBuildDate>Mon, 02 Nov 2026 00:00:00 GMT</lastBuildDate>", ""
    if url.startswith("https://x.test"): return 200, "", ""
    return 200, ok_home, ""
class R:
    status = 200
    def __enter__(self): return self
    def __exit__(self, *a): pass
    def read(self): return b"{}"
h.fetch = fake
h.urllib.request.urlopen = lambda *a, **k: R()
rows = h.check_content(dt.datetime(2026, 11, 14, tzinfo=dt.timezone.utc))
assert all(r[0] for r in rows if "Sitemap" not in r[1]), rows           # everything else passes
assert [r[0] for r in rows if "Sitemap" in r[1]].count(False) == 4      # dead /gone URL flagged on each sitemap
rows = h.check_content(dt.datetime(2026, 12, 20, tzinfo=dt.timezone.utc))
assert [r for r in rows if "newest issue" in r[1]][0][0] is False       # 48 days old fails
_f = h.fetch
h.fetch = lambda url, *a, **k: (200, '<meta name="robots" content="noindex">', "") if url.endswith("/") and "x.test" not in url else _f(url, *a, **k)
assert "noindex" in " ".join(r[2] for r in h.check_content(dt.datetime(2026, 11, 14, tzinfo=dt.timezone.utc)))

# red pull-request and side-branch runs are ignored; a red run on main still counts
def runs(code=200):
    old = (now - dt.timedelta(days=0)).strftime("%Y-%m-%dT%H:%M:%SZ")
    r = lambda n, ev, br, c: {"name": n, "event": ev, "head_branch": br, "conclusion": c, "created_at": old, "html_url": "u"}
    body = json.dumps({"workflow_runs": [r("Build check", "pull_request", "dependabot/x", "failure"),
                                         r("Weekly health check", "workflow_dispatch", "side", "failure"),
                                         r("Deploy", "push", "main", "failure"), r("Deploy", "push", "main", "success")]})
    return code, body, ""
h.fetch = lambda url, *a, **k: runs()
h.REPOS[:] = ["one"]
rows = h.check_workflows(now)
assert len(rows) == 1 and rows[0][0] is False and "Deploy" in rows[0][2] and "Build check" not in rows[0][2] and "Weekly" not in rows[0][2], rows
print("OK")
