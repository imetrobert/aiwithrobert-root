# START HERE: running all the AI with Robert / imetrobert apps on the free Claude plan

**Single source of truth for Claude (any plan): this file, `docs/START-HERE.md` in `imetrobert/aiwithrobert-root`.** Read it first,
then only the one doc it points to for the task. Last reviewed: 2026-11-24 (the weekly health check goes red after 150 days; re-read this page, fix anything stale, then change the date). Claude's memory is a backup copy of the same facts: if memory and a repo file
disagree, the repo file wins.

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
| Quebec planner (EN + FR) | retireqc.aiwithrobert.com, retraiteqc.aiwithrobert.com | aiwithrobert-retireqc (French address: aiwithrobert-retraiteqc, redirect only) | CLAUDE.md, docs/common-edits.md | push to main; CI checks |
| Ontario planner | retireon.aiwithrobert.com | aiwithrobert-retireon | CLAUDE.md, docs/common-edits.md | push to main; CI checks |
| Personal planner (only Robert) | retire.imetrobert.com | imetrobert-retire (public repo, no personal figures in it) | CLAUDE.md, docs/common-edits.md | push to main; CI checks |
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

## Once a year
`docs/JANUARY-CHECKLIST.md`: the new tax numbers for the three retirement planners (and the few other yearly renewals). The health check goes red from 1 January until it is done.

## Search and AI-answer visibility
`docs/SEO-AIO-GEO.md`: what is automatic, a 10-minute monthly routine and paste-ready prompts (add a guide, fix a Search Console issue, turn on the rating schema).

## Email (how imetrobert.com and aiwithrobert.com mail is set up)
`docs/EMAIL-SETUP.md`: receiving (registrar forwarding into Gmail), sending (Brevo SMTP; Gmail send-as until January 2027, then Apple Mail),
agent rules and known quirks. Open it for any "I can't send / didn't receive / landed in spam" question.

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

**Add a small feature or fix to a retirement planner** (Quebec, Ontario or Personal; each is one `index.html` plus a small `account.js`)
> Repo imetrobert/REPO (aiwithrobert-retireqc, aiwithrobert-retireon or imetrobert-retire). Read only CLAUDE.md and
> docs/common-edits.md (recipe 9). I want: WHAT I SEE AND WHERE. Use grep or docs/code-map.md, never read index.html whole. Give me
> the smallest edit as a ready-to-paste snippet with the line to find. Quebec: include the French text. Keep index.html free of
> network calls. After I commit, the Checks workflow tells me if something broke.

**Planner sign-in, welcome banner or saved plans** (all in `account.js`, recipe 10 in each planner repo): same prompt, but read
the "Two files, two jobs" section of CLAUDE.md first. The Quebec and Ontario copies of account.js should stay in step.

**An email problem** (cannot send, did not arrive, spam folder)
> Repo imetrobert/aiwithrobert-root. Read only docs/EMAIL-SETUP.md. The problem: DESCRIBE IT, WITH THE ADDRESS AND THE APP I USED.
> Tell me the most likely cause and the one setting to check first (Brevo, Gmail send-as, Apple Mail or the registrar).

**Restore data**: follow `docs/BACKUP-RESTORE.md` (no computer needed).

**Someone new needs access**: access.imetrobert.com > invite. If the invite email shows a wrong app link, the app list is in
`Supabase-platform-` (docs/index.html, docs/invite.html) and the invite function (migration/invite_user.sql, run by hand).

## What free Claude cannot do (say so quickly instead of trying)
- It may not remember earlier chats: always open with the START-HERE opener and name the repo, the one file and the error.
- It cannot run code or tests; the repo's own CI does ("Checks" or "Build Assets" in Actions). Commit, wait 2-3 minutes, read the run.
- It cannot read private repo files or logs without a connected repo or a pasted copy; paste the one section or the failing log lines.
- It cannot log in anywhere for you: Supabase, Brevo, EmailJS, the registrar, GitHub tokens, YouTube Studio and Search Console are yours to click. KEYS.md has the links.
- Needs a desktop (rare): the Google Cloud setup for a Search Console data pull. Everything else here works from the phone.

## Cheap-editing rules that save the most credits
1. Edit on GitHub from your phone: open the one file, search for the exact text, change it, commit. Most content changes need
   no Claude at all (see each repo's "Editing without Claude Code" section).
2. Never paste a whole big file (the toolkit `index.html`, `css/style.css`, `renderer.py`). Paste the one section.
3. Do not hand-edit generated files (`fr/index.html`, `js/bundle.js`, `css/styles.css`, blog posts); edit their source.
4. After any change to a site, wait 2-3 minutes for GitHub Pages, then reload.
5. Gemini (blog) is a free key with daily limits: run at most one or two full trial issues in a day.
