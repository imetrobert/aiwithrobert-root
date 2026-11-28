# If something breaks (read this first, then fix only what it names)

1. **A red check or an email from GitHub:** Actions tab, open the failed run, read the last 20 lines of the red step. "Pages build and deployment" red once: re-run the job (usually a transient GitHub error).
2. **A pull request (for example from Dependabot) has a red "PR build check" or "Checks":** do not merge it; open the red step and fix or close the PR.
3. **Weekly health check red:** `scripts/health_check.py` lists what failed (a domain, a certificate, a date in `ops/expiries.json`). Fix what it names; dates are edited in `ops/expiries.json` on GitHub.
4. **Hub page wrong:** never edit `index.html` or `fr/index.html`; edit `scripts/build_hub.py` (the Action rebuilds them).
5. **Backups:** `docs/BACKUP-RESTORE.md`. Keys and renewal links: `docs/KEYS.md`. The map of every app: `docs/START-HERE.md`.
