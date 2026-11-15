# Supabase backup and restore (phone-friendly)

Every Sunday a job saves every table of the shared Supabase project (invoices, leads, feasibility checks, sessions,
ETF holdings, access rows and so on) as an ENCRYPTED file you can download from the run page for 90 days.
Prices (`etf_prices`) and three computed views are skipped. Passwords/accounts live in Supabase Auth
and are not in the file: people are re-invited from access.imetrobert.com (their access rows are in the backup).

## 1. One-time setup (two secrets)
GitHub > imetrobert/aiwithrobert-root > Settings > Secrets and variables > Actions > New repository secret:
- `SUPABASE_SERVICE_KEY`: Supabase dashboard > Project Settings > API Keys > the **secret** key (not the publishable one).
- `BACKUP_PASSPHRASE`: a long passphrase you invent. **Save it in your password manager: without it a backup cannot be opened.**
Then Actions > Weekly Supabase backup > Run workflow, and check it goes green. Do this once now, then look at it monthly.
  **Where the passphrase is kept:** in Bitwarden, in the Notes of the invoices.imetrobert.com entry (hint only; the passphrase itself is never in this repo).

## 2. Check it worked
Actions > Weekly Supabase backup > latest run > the file under "Artifacts" (supabase-backup-encrypted). A red run emails you.
The run log lists each table and its row count (never the data).

## 3. Restore
Actions > Restore from a Supabase backup > Run workflow, then fill in:
- run_id: the number at the end of the backup run's address (github.com/imetrobert/aiwithrobert-root/actions/runs/NUMBER)
- tables: `all`, or names like `invoices,site_inquiries`
- confirm: `RESTORE`
It adds back missing rows and overwrites matching ones; it never deletes. If a table fails on a "foreign key" error,
restore its parent table first and run again.
Tip: restore one table first (for example `site_inquiries`) to confirm it works before restoring `all`.

## 4. If something looks wrong, paste this to Claude (free is fine)
"My Supabase backup or restore run in imetrobert/aiwithrobert-root failed. Read docs/BACKUP-RESTORE.md,
scripts/backup_supabase.py and the failing run's log (here is the error: ...) and tell me the smallest fix."
