#!/usr/bin/env python3
"""Dump every table in the shared Supabase project's public schema to JSON files (one per table).

Run by .github/workflows/backup.yml, which encrypts the result. Standard library only.
Needs env SUPABASE_SERVICE_KEY (a secret/service key: it bypasses row security, so the output is sensitive
and must always be encrypted before it leaves the runner). Prints table names and row COUNTS only, never data.
Usage: python3 scripts/backup_supabase.py OUT_DIR
Skips tables that are re-fetched automatically (EXCLUDE). Auth accounts (passwords) are not in this dump:
people are re-invited from the access page; their access rows (app_access) ARE in it.
"""
import datetime as dt
import json
import os
import sys
import urllib.request

URL = os.environ.get("SUPABASE_URL", "https://ipnajvgwtjrlecbqfwrh.supabase.co").rstrip("/")
# etf_prices: large, refreshed daily. The three views are computed from tables that ARE backed up
# (a view cannot be restored into).
EXCLUDE = {"etf_prices", "invoice_public_v", "invoices_et", "job_ranked"}
PAGE = 1000


def get(path, key, rng=None):
    h = {"apikey": key, "Accept": "application/json", "User-Agent": "awr-backup"}
    if rng:
        h.update({"Range-Unit": "items", "Range": rng})
    with urllib.request.urlopen(urllib.request.Request(URL + path, headers=h), timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def list_tables(key):
    spec = get("/rest/v1/", key)
    return sorted(t for t in spec.get("definitions", {}) if t not in EXCLUDE)


def dump_table(table, key):
    rows, start = [], 0
    while True:
        chunk = get(f"/rest/v1/{table}?select=*", key, f"{start}-{start + PAGE - 1}")
        rows += chunk
        if len(chunk) < PAGE:
            return rows
        start += PAGE


def main(out):
    key = os.environ.get("SUPABASE_SERVICE_KEY", "").strip()
    if not key:
        sys.exit("SUPABASE_SERVICE_KEY is not set. Add it under Settings > Secrets and variables > Actions.")
    os.makedirs(out, exist_ok=True)
    tables, manifest, failed = list_tables(key), {}, []
    if not tables:
        sys.exit("No tables found: the key may be wrong (anon keys see nothing). Nothing was saved.")
    for t in tables:
        try:
            rows = dump_table(t, key)
            json.dump(rows, open(os.path.join(out, t + ".json"), "w", encoding="utf-8"), ensure_ascii=False)
            manifest[t] = len(rows)
            print(f"  {t}: {len(rows)} rows")
        except Exception as e:
            failed.append(t)
            print(f"  {t}: FAILED ({type(e).__name__}: {e})")
    json.dump({"made_at": dt.datetime.now(dt.timezone.utc).isoformat(), "rows": manifest, "failed": failed},
              open(os.path.join(out, "manifest.json"), "w"), indent=2)
    print(f"{len(manifest)} tables saved, {sum(manifest.values())} rows, {len(failed)} failed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "backup")
