#!/usr/bin/env python3
"""Put rows from a backup folder back into Supabase (upsert: adds missing rows, overwrites matching ones,
NEVER deletes anything). Run by .github/workflows/restore.yml.
Usage: python3 scripts/restore_supabase.py BACKUP_DIR all|table1,table2
Needs env SUPABASE_SERVICE_KEY. Tables are restored in file order; if a table fails on a foreign key,
restore its parent table first (the workflow reports which one failed).
"""
import json
import os
import sys
import urllib.request

URL = os.environ.get("SUPABASE_URL", "https://ipnajvgwtjrlecbqfwrh.supabase.co").rstrip("/")
BATCH = 500


def post(table, rows, key):
    req = urllib.request.Request(f"{URL}/rest/v1/{table}", method="POST", data=json.dumps(rows).encode("utf-8"),
                                 headers={"apikey": key, "Content-Type": "application/json", "User-Agent": "awr-restore",
                                          "Prefer": "resolution=merge-duplicates,return=minimal"})
    urllib.request.urlopen(req, timeout=60).read()


def main(folder, which):
    key = os.environ.get("SUPABASE_SERVICE_KEY", "").strip()
    if not key:
        sys.exit("SUPABASE_SERVICE_KEY is not set.")
    names = sorted(f[:-5] for f in os.listdir(folder) if f.endswith(".json") and f != "manifest.json")
    wanted = names if which == "all" else [t.strip() for t in which.split(",") if t.strip()]
    missing = [t for t in wanted if t not in names]
    if missing:
        sys.exit(f"Not in this backup: {', '.join(missing)}. Available: {', '.join(names)}")
    failed = []
    for t in wanted:
        rows = json.load(open(os.path.join(folder, t + ".json"), encoding="utf-8"))
        try:
            for i in range(0, len(rows), BATCH):
                post(t, rows[i:i + BATCH], key)
            print(f"  {t}: {len(rows)} rows restored")
        except Exception as e:
            failed.append(t)
            print(f"  {t}: FAILED ({type(e).__name__}: {e})")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
