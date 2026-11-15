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
print("OK")
