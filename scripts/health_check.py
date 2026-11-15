#!/usr/bin/env python3
"""Weekly health check of every AI with Robert / imetrobert app. Run by .github/workflows/health.yml.

Prints a Markdown report (also written to the job summary) and exits 1 if anything needs action, so
GitHub emails the owner. Standard library only. Sections: live sites, Supabase, latest result of every
repo's workflows, TLS certificates, domain registration, and ops/expiries.json.
Run locally: python3 scripts/health_check.py   (needs network)
"""
import concurrent.futures
import datetime as dt
import email.utils
import json
import os
import re
import socket
import ssl
import sys
import urllib.error
import urllib.request

OWNER = "imetrobert"
SUPABASE = "https://ipnajvgwtjrlecbqfwrh.supabase.co"
ANON = "sb_publishable_oPa7fZdSTeXKuCwpOF338Q_PcXS57go"   # publishable key, already public in every app

# (label, [candidate urls; ONE must work], text that must appear or None)
SITES = [
    ("Hub aiwithrobert.com", ["https://aiwithrobert.com/"], "AI with Robert"),
    ("Hub (French)", ["https://aiwithrobert.com/fr/"], "AI with Robert"),
    ("Seniors site", ["https://seniors.aiwithrobert.com/"], "AI with Robert"),
    ("Seniors site (French)", ["https://seniors.aiwithrobert.com/fr/"], "AI with Robert"),
    ("Business site", ["https://biz.aiwithrobert.com/"], "AI with Robert"),
    ("Business feasibility check script", ["https://biz.aiwithrobert.com/js/feascheck.js"], None),
    ("Blog home", ["https://www.imetrobert.com/"], "Robert"),
    ("Blog index", ["https://www.imetrobert.com/blog/"], None),
    ("Blog latest post", ["https://www.imetrobert.com/blog/posts/latest.html"], None),
    ("Blog feed", ["https://www.imetrobert.com/blog/feed.xml"], None),
    ("Toolkit", ["https://toolkit.aiwithrobert.com/"], None),
    ("Invoicing app", ["https://invoices.imetrobert.com/", "https://invoices.aiwithrobert.com/"], None),
    ("ETF tracker", ["https://invest.imetrobert.com/"], None),
    ("Marketplace generator", ["https://fbmarket.imetrobert.com/"], None),
    ("Claims tracker", ["https://tax.imetrobert.com/"], None),
    ("Job search", ["https://jobs.imetrobert.com/"], None),
    ("Access rights page", ["https://access.imetrobert.com/"], None),
]
REPOS = ["aiwithrobert", "aiwithrobert-biz", "aiwithrobert-root", "aiwithrobert-toolkit",
         "Ai-with-Robert-Invoicing-System", "Facebook-marketplace-generator", "tsx-etf-signal-notifier",
         "imetrobert.github.io", "claims-tracker", "jobs", "Supabase-platform-"]
DOMAINS = {"aiwithrobert.com": "com", "imetrobert.com": "com"}
TLS_HOSTS = ["aiwithrobert.com", "seniors.aiwithrobert.com", "biz.aiwithrobert.com", "www.imetrobert.com",
             "toolkit.aiwithrobert.com", "invest.imetrobert.com", "fbmarket.imetrobert.com", "tax.imetrobert.com",
             "jobs.imetrobert.com", "access.imetrobert.com"]
# (label, home page, Google Analytics id that must be in the page or None)
CONTENT_SITES = [
    ("Hub", "https://aiwithrobert.com/", None),
    ("Seniors site", "https://seniors.aiwithrobert.com/", "G-DM4EY880K2"),
    ("Business site", "https://biz.aiwithrobert.com/", None),
    ("Blog and personal site", "https://www.imetrobert.com/", "G-Y0FZTVVLBS"),
]
BLOG_FEED = "https://www.imetrobert.com/blog/feed.xml"
BLOG_MAX_AGE_DAYS = 40          # a monthly issue is due on the 1st; 40 days without a new one means a missed or unapproved issue
TLS_WARN_DAYS, DOMAIN_WARN_DAYS, ITEM_WARN_DAYS, RUN_MAX_AGE_DAYS = 10, 45, 14, 21


def fetch(url, headers=None, tries=3, timeout=20, limit=400000):
    """Return (status, body_text, error). Retries so one blip does not email anyone."""
    last = ""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=dict({"User-Agent": "awr-health-check"}, **(headers or {})))
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(limit).decode("utf-8", "replace"), ""
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code < 500:
                return e.code, "", last
        except Exception as e:  # network, DNS, TLS, timeout
            last = f"{type(e).__name__}: {e}"
        if i < tries - 1:
            import time
            time.sleep(4 * (i + 1))
    return 0, "", last


def check_sites():
    rows = []
    for label, urls, needle in SITES:
        problems = []
        for u in urls:
            code, body, err = fetch(u)
            if code == 200 and (needle is None or needle.lower() in body.lower()):
                rows.append((True, label, u))
                break
            problems.append(f"{u}: {err or ('HTTP %d' % code) if code != 200 else 'missing text ' + repr(needle)}")
        else:
            rows.append((False, label, "; ".join(problems)))
    return rows


def host_of(url):
    return url.split("/")[2]


def check_content(today):
    """Silent breakages the plain 'is it up' check cannot see: accidental noindex or robots block, broken JSON-LD,
    lost analytics tag, dead sitemap URLs, the Business feasibility table, and a missed monthly blog issue."""
    rows = []
    for label, url, ga in CONTENT_SITES:
        code, body, err = fetch(url)
        if code != 200:
            rows.append((False, f"{label}: home page", err or f"HTTP {code}"))
            continue
        problems = []
        if re.search(r'<meta[^>]+name=["\']robots["\'][^>]*noindex', body, re.I):
            problems.append("home page has a noindex tag (hidden from Google)")
        bad_ld = 0
        for block in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', body, re.S | re.I):
            try:
                json.loads(block)
            except Exception:
                bad_ld += 1
        if bad_ld:
            problems.append(f"{bad_ld} JSON-LD block(s) are not valid JSON")
        if ga and ga not in body:
            problems.append(f"analytics tag {ga} is missing")
        rcode, rbody, _ = fetch(f"https://{host_of(url)}/robots.txt", tries=2, limit=20000)
        if rcode == 200 and re.search(r"^\s*Disallow:\s*/\s*$", rbody, re.M | re.I):
            problems.append("robots.txt blocks the whole site")
        rows.append((not problems, f"{label}: page, schema, analytics, robots", "; ".join(problems) or "ok"))

    for sm in sorted({f"https://{host_of(u)}/sitemap.xml" for _, u, _ in CONTENT_SITES}):
        code, body, err = fetch(sm, tries=2)
        if code != 200:
            rows.append((False, f"Sitemap {host_of(sm)}", err or f"HTTP {code}"))
            continue
        urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", body)
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
            results = list(ex.map(lambda u: (u, fetch(u, tries=2, limit=2000)[0]), urls))
        dead = [f"{u} (HTTP {c})" for u, c in results if c != 200]
        rows.append((bool(urls) and not dead, f"Sitemap {host_of(sm)}: {len(urls)} URLs",
                     "; ".join(dead[:5]) + (f" and {len(dead) - 5} more" if len(dead) > 5 else "") if dead else ("ok" if urls else "no URLs listed")))

    req = urllib.request.Request(SUPABASE + "/rest/v1/rpc/public_caps", method="POST", data=b"{}",
                                 headers={"apikey": ANON, "Content-Type": "application/json", "User-Agent": "awr-health-check"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            ok = r.status == 200 and isinstance(json.loads(r.read()), dict)
        rows.append((ok, "Feasibility check table (public_caps)", "ok" if ok else "unexpected answer"))
    except Exception as e:
        rows.append((False, "Feasibility check table (public_caps)", f"{type(e).__name__}: {e}"))

    code, body, err = fetch(BLOG_FEED)
    m = re.search(r"<lastBuildDate>([^<]+)</lastBuildDate>", body)
    if code != 200 or not m:
        rows.append((False, "Blog: newest issue date", err or "feed has no lastBuildDate"))
    else:
        age = (today - email.utils.parsedate_to_datetime(m.group(1))).days
        rows.append((age <= BLOG_MAX_AGE_DAYS, "Blog: newest issue date",
                     f"{age} days old" + ("" if age <= BLOG_MAX_AGE_DAYS else f" (more than {BLOG_MAX_AGE_DAYS}: this month's issue was not generated or not approved)")))
    return rows


def check_supabase():
    rows = []
    h = {"apikey": ANON}
    code, body, err = fetch(SUPABASE + "/auth/v1/health", h)
    rows.append((code == 200, "Supabase sign-in service", err or f"HTTP {code}"))
    for app in ("seniors", "business"):
        req = urllib.request.Request(SUPABASE + "/rest/v1/rpc/site_capacity", method="POST",
                                     data=json.dumps({"p_site": app}).encode(),
                                     headers={"apikey": ANON, "Content-Type": "application/json", "User-Agent": "awr-health-check"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                rows.append((r.status == 200, f"Supabase site_capacity({app})", f"HTTP {r.status}"))
        except urllib.error.HTTPError as e:
            # a 4xx on a wrong argument name still proves the database answers; only 5xx/network means down
            rows.append((e.code < 500, f"Supabase site_capacity({app})", f"HTTP {e.code}"))
        except Exception as e:
            rows.append((False, f"Supabase site_capacity({app})", f"{type(e).__name__}: {e}"))
    return rows


def check_workflows(today):
    """Latest completed run of every workflow in every repo; flag a failure still unresolved."""
    rows = []
    token = os.environ.get("GITHUB_TOKEN", "")
    h = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = "Bearer " + token
    for repo in REPOS:
        code, body, err = fetch(f"https://api.github.com/repos/{OWNER}/{repo}/actions/runs?per_page=40&status=completed", h, limit=8000000)
        if code != 200:
            rows.append((False, repo, f"could not read Actions ({err or code})"))
            continue
        latest = {}
        for run in json.loads(body).get("workflow_runs", []):
            # only real runs on the main branch count: a red pull request (e.g. a Dependabot update that fails its
            # Build check) or a test run on a side branch is not an outage and must not email you
            if run.get("event", "").startswith("pull_request") or run.get("head_branch") not in ("main", "master"):
                continue
            latest.setdefault(run["name"], run)          # newest first
        bad = []
        for name, run in latest.items():
            if run["conclusion"] != "failure":
                continue
            age = (today - dt.datetime.fromisoformat(run["created_at"].replace("Z", "+00:00"))).days
            if age <= RUN_MAX_AGE_DAYS:
                bad.append(f"{name} (failed {age}d ago: {run['html_url']})")
        rows.append((not bad, repo, "; ".join(bad) if bad else f"{len(latest)} workflows, none failing"))
    return rows


def tls_days_left(host):
    ctx = ssl.create_default_context()
    with socket.create_connection((host, 443), timeout=15) as s:
        with ctx.wrap_socket(s, server_hostname=host) as t:
            exp = ssl.cert_time_to_seconds(t.getpeercert()["notAfter"])
    return int((exp - dt.datetime.now(dt.timezone.utc).timestamp()) // 86400)


def check_tls():
    rows = []
    for host in TLS_HOSTS:
        try:
            d = tls_days_left(host)
            rows.append((d >= TLS_WARN_DAYS, host, f"certificate valid for {d} more days"))
        except Exception as e:
            rows.append((False, host, f"{type(e).__name__}: {e}"))
    return rows


def check_domains(today):
    rows, notes = [], []
    for dom, tld in DOMAINS.items():
        code, body, err = fetch(f"https://rdap.verisign.com/{tld}/v1/domain/{dom}", tries=2)
        exp = None
        if code == 200:
            for ev in json.loads(body).get("events", []):
                if ev.get("eventAction") == "expiration":
                    exp = dt.datetime.fromisoformat(ev["eventDate"].replace("Z", "+00:00"))
        if exp is None:
            notes.append(f"{dom}: registration date could not be read ({err or code}); check it by hand")
            continue
        d = (exp - today).days
        rows.append((d >= DOMAIN_WARN_DAYS, dom, f"registration expires {exp.date()} ({d} days)"))
    return rows, notes


def check_items(path, today):
    rows, notes = [], []
    try:
        items = json.load(open(path, encoding="utf-8"))["items"]
    except Exception as e:
        return [(False, "ops/expiries.json", f"unreadable: {e}")], notes
    for it in items:
        if not it.get("date"):
            notes.append(f"{it['name']}: no date set (edit ops/expiries.json)")
            continue
        d = (dt.datetime.fromisoformat(it["date"]).replace(tzinfo=dt.timezone.utc) - today).days
        rows.append((d > ITEM_WARN_DAYS, it["name"], f"expires {it['date']} ({d} days). Renew: {it.get('renew', '')}"))
    return rows, notes


# One line of "what to do" shown under a section that has a FAIL, so the summary alone is enough to act on.
HINTS = {
    "Live sites": "Reload the site yourself. Still down: open the repo's Settings > Pages (is it published?) and its Actions tab (did the last deploy fail?).",
    "Content and search visibility": "Open the line marked FAIL. noindex, robots or JSON-LD: the last push to that repo broke it; paste the line to Claude with that repo's CLAUDE.md. Dead sitemap URL: the page was renamed or deleted. Blog issue date: open www.imetrobert.com/blog/staging/preview.html and approve, or see docs/DIAGNOSE.md in the blog repo. public_caps: the toolkit's capability table was not published.",
    "Supabase": "Check https://status.supabase.com, then https://supabase.com/dashboard/project/ipnajvgwtjrlecbqfwrh (a paused project has a Restore button). All sign-ins depend on it.",
    "Latest automated runs in every repo": "Open that repo's Actions tab, tap the red run and read the error. Key or token errors include the fix steps; every key is listed in docs/KEYS.md. An old red clears itself after the next green run.",
    "TLS certificates": "In the repo's Settings > Pages turn Enforce HTTPS off and on again; if the domain is not verified, check DNS at Name Services.",
    "Domain registration": "Renew the domain at Name Services (billing), then the date here clears by itself.",
    "Renewals you track": "Renew the item named, then update its date in ops/expiries.json (https://github.com/imetrobert/aiwithrobert-root/edit/main/ops/expiries.json).",
}


def render(sections, notes):
    out, failed = ["# Weekly health check", f"_{dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC_", ""], 0
    for title, rows in sections:
        bad = [r for r in rows if not r[0]]
        failed += len(bad)
        out.append(f"## {title}: {'ALL OK' if not bad else str(len(bad)) + ' NEED ACTION'}")
        for ok, label, detail in rows:
            out.append(f"- {'OK' if ok else '**FAIL**'} {label}: {detail}")
        if bad and title in HINTS:
            out.append(f"  - **What to do:** {HINTS[title]}")
        out.append("")
    if notes:
        out.append("## Notes (do not fail the check)")
        out += [f"- {n}" for n in notes] + [""]
    out.append("Next step if anything failed: open docs/START-HERE.md in this repo and use the matching prompt.")
    return "\n".join(out), failed


def safe(name, fn, *args):
    try:
        return fn(*args)
    except Exception as e:                      # the check itself broke: say so loudly
        return [(False, name, f"the check crashed: {type(e).__name__}: {e}")]


def main():
    today = dt.datetime.now(dt.timezone.utc)
    dom_rows, dom_notes = check_domains(today)
    item_rows, item_notes = check_items(os.path.join(os.path.dirname(__file__), "..", "ops", "expiries.json"), today)
    sections = [("Live sites", safe("sites", check_sites)), ("Supabase", safe("supabase", check_supabase)),
                ("Content and search visibility", safe("content", check_content, today)),
                ("Latest automated runs in every repo", safe("workflows", check_workflows, today)),
                ("TLS certificates", safe("tls", check_tls)), ("Domain registration", dom_rows), ("Renewals you track", item_rows)]
    text, failed = render(sections, dom_notes + item_notes)
    print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8").write(text + "\n")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
