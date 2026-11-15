# START HERE: running all the AI with Robert / imetrobert apps on the free Claude plan

One page for the whole estate. Each repo has its own `CLAUDE.md` (a short map). Free Claude has small limits, so the rule
is always: **name the repo, name the one file, paste the error. Never ask it to explore.**

## The apps

| App | Address | Repo (imetrobert/...) | Read first | How it ships |
|---|---|---|---|---|
| Hub | aiwithrobert.com | aiwithrobert-root | CLAUDE.md | page built by `scripts/build_hub.py` |
| Seniors site | seniors.aiwithrobert.com | aiwithrobert | CLAUDE.md, docs/common-edits.md | push to main; CI rebuilds |
| Business site | biz.aiwithrobert.com | aiwithrobert-biz | CLAUDE.md, docs/common-edits.md | push to main; CI rebuilds |
| Blog and personal site | www.imetrobert.com | imetrobert.github.io | CLAUDE.md, docs/DIAGNOSE.md | monthly Gemini run, you approve |
| Toolkit (admin) | toolkit.aiwithrobert.com | aiwithrobert-toolkit | CLAUDE.md, docs/code-map.md | one file, push to main |
| Invoicing | invoices.aiwithrobert.com | Ai-with-Robert-Invoicing-System | CLAUDE.md | merge to main deploys |
| ETF tracker | invest.imetrobert.com | tsx-etf-signal-notifier | CLAUDE.md, RUNBOOK.md | merge to main deploys |
| Marketplace generator | fbmarket.imetrobert.com | Facebook-marketplace-generator | CLAUDE.md, RUNBOOK.md | push to main (function: manual deploy) |
| Claims tracker | tax.imetrobert.com | claims-tracker | CLAUDE.md, RUNBOOK.md | push to main |
| Job search | jobs.imetrobert.com | jobs | CLAUDE.md, RUNBOOK.md | merge to main deploys |
| Access rights | access.imetrobert.com | Supabase-platform- | README.md | push to main |

All share ONE Supabase project and one login. Who can open what is set at access.imetrobert.com.

## What watches things for you (you get an email when one goes red)
- **Monday: Weekly health check** (this repo, Actions). Opens every site, checks Supabase, every repo's latest automated runs,
  certificates, domain registration, and the dates in `ops/expiries.json`. Edit that file when you renew a key or token.
- **Sunday: Weekly Supabase backup** (this repo). Encrypted copy of every table, 90 days. Restore guide: `docs/BACKUP-RESTORE.md`.
  Setup needs two secrets once (see that guide, step 1).
- **Monthly: Dependabot** in the invoicing, ETF and jobs repos opens one update pull request; the "Build check" says if it is
  safe. Green: Merge. Red: leave it, or paste the failing log to Claude.
- Blog: Actions > Blog health report; Pipeline health page on the review page; `docs/DIAGNOSE.md` in the blog repo.

## Search and AI-answer visibility
`docs/SEO-AIO-GEO.md`: what is automatic, a 10-minute monthly routine and paste-ready prompts (add a guide, fix a Search Console issue, turn on the rating schema).

## Keys and secrets
`docs/KEYS.md` lists every key and secret, what breaks when one dies and the link to replace it.

## Prompts to paste (replace the capitals)
**Something is broken**
> Repo imetrobert/REPO. Read only CLAUDE.md and FILE. This error appeared: ERROR TEXT. Find the cause and give me the smallest
> edit as a ready-to-paste replacement for that one section. Do not read other files unless you must, and say which.

**A health check turned red**
> Open the failing run of "Weekly health check" in imetrobert/aiwithrobert-root (link in the email). Read docs/START-HERE.md and
> the line marked FAIL. Tell me what is wrong and the fix. Ask before touching any other repo.

**Change wording or a price** (a price lives in FIVE places: the Business site `index.html` + `js/i18n.js` + `llms.txt`, the toolkit
`FX_PRICE`, and the invoicing app `src/lib/services.js` BUSINESS_SERVICES; the repos' own weekly checks flag any mismatch)
> I want to change PRICE/WORDING from X to Y. Read CLAUDE.md and docs/common-edits.md in REPO and list every file and line to
> change. Then give me each edit as a small snippet.

**The blog review page or a monthly run failed**
> Repo imetrobert/imetrobert.github.io. Read docs/DIAGNOSE.md. The run log says: PASTE THE ONE LINE FROM THE HEALTH PAGE.

**Restore data**: follow `docs/BACKUP-RESTORE.md` (no computer needed).

**Someone new needs access**: access.imetrobert.com > invite. If the invite email shows a wrong app link, the app list is in
`Supabase-platform-` (docs/index.html, docs/invite.html) and the invite function (migration/invite_user.sql, run by hand).

## Cheap-editing rules that save the most credits
1. Edit on GitHub from your phone: open the one file, search for the exact text, change it, commit. Most content changes need
   no Claude at all (see each repo's "Editing without Claude Code" section).
2. Never paste a whole big file (the toolkit `index.html`, `css/style.css`, `renderer.py`). Paste the one section.
3. Do not hand-edit generated files (`fr/index.html`, `js/bundle.js`, `css/styles.css`, blog posts); edit their source.
4. After any change to a site, wait 2-3 minutes for GitHub Pages, then reload.
5. Gemini (blog) is a free key with daily limits: run at most one or two full trial issues in a day.
