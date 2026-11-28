# START HERE: running all the AI with Robert / imetrobert apps on the free Claude plan

**Single source of truth for Claude (any plan): this file, `docs/START-HERE.md` in `imetrobert/aiwithrobert-root`.** Read it first,
then only the one doc it points to for the task. Last reviewed: 2026-11-26 (the weekly health check goes red after 150 days; re-read this page, fix anything stale, then change the date. `docs/EMAIL-SETUP.md` carries its own "Last reviewed" date and goes red the same way: check addresses, repo names and counts against reality, then update both dates. The red row reads "START-HERE last reviewed N days ago" under "Docs for free Claude".). Claude's memory is a backup copy of the same facts: if memory and a repo file
disagree, the repo file wins.

One page for the whole estate. Each repo has its own `CLAUDE.md` (a short map). Free Claude has small limits, so the rule
is always: **name the repo, name the one file, paste the error. Never ask it to explore.**

## How to open a file (read this if you cannot find a file)
Claude on the free plan opens WEB LINKS, not names like "imetrobert/REPO, docs/FILE". Every doc named in this page has a full link in `docs/LINKS.md`: https://raw.githubusercontent.com/imetrobert/aiwithrobert-root/main/docs/LINKS.md . Open that link, find the repo and file, open its link. Never guess a link and never say the repo is private: all repos are public. If a link fails, say which one and ask Robert to paste the file.

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

## Task router (the common jobs: go straight to the file)
| Job | Repo and file to read | Note |
|---|---|---|
| Change a Seniors price or wording | `aiwithrobert`: CLAUDE.md, `docs/common-edits.md` "Change a price" | Group workshop is $35 per person; $275 is the 5-hour Starter. Confirm which price before editing |
| Change a Business price or wording | `aiwithrobert-biz`: CLAUDE.md, `docs/common-edits.md` | Also toolkit `FX_PRICE` and invoicing `BUSINESS_SERVICES` |
| Change the Prospect finder (who to pitch: search prompt, list import, queue into the Pitch builder) | `aiwithrobert-toolkit`: CLAUDE.md, `docs/common-edits.md` "Prospect finder", then `docs/code-map.md` | Search `fdPrompt`, `fdRead`; paste only that block into the chat. List is kept on the phone only |
| Change the pitch follow-up emails (day 4 nudge, day 10 last note), or the Reply helper (draft an answer to a prospect's reply) | `aiwithrobert-toolkit`: CLAUDE.md, `docs/common-edits.md` "Pitch follow-up messages" and "Reply helper", then `docs/code-map.md` | Search `FU_MAIL`, `fuDue`, `rpPrompt`; paste only that block. New lead fields must also go in `cleanLead` |
| Change the workshop flyer PDF (from a talk card in Speaking engagements) | `aiwithrobert-toolkit`: CLAUDE.md, `docs/common-edits.md` "Workshop flyer", then `docs/code-map.md` | Search `flyerPage`, `FL_TXT`; paste only that block |
| Change the Pitch builder (find-clients pitch: wording, services named, PDF layout, follow-up days) | `aiwithrobert-toolkit`: CLAUDE.md, `docs/common-edits.md` "Pitch builder", then `docs/code-map.md` | Edit only the block named in the recipe (search `ptPrompt`, `ptPage`, `PT_TXT`); paste just that block into the chat, never the whole index.html. Rules: no invented results, plain-text email |
| Weekly health check is red | this repo: the FAIL line of the run, then this file | Re-run: Actions > Weekly health check > Run workflow |
| Mail goes to spam or does not arrive | this repo: `docs/EMAIL-SETUP.md` | Needs DNS facts the doc may lack: ask Robert to paste the registrar records |
| Blog run failed | `imetrobert.github.io`: `docs/DIAGNOSE.md`, the Step 2 error-code table (top of the file) | Read the first 40 lines only |
| Yearly tax update (3 planners) | this repo: `docs/JANUARY-CHECKLIST.md`, then each planner's `docs/common-edits.md` recipe 1 | Recipe 1, not 9 |
| Small planner feature or fix | the planner repo: CLAUDE.md, `docs/common-edits.md` recipe 9 | |
| Planner compare / stress-test tools, one-page summary, text size, life-event presets (same code in all 3 planners) | the planner repo: CLAUDE.md, `docs/common-edits.md` recipe 16 (`grep -n "COMPARE AND STRESS-TEST TOOLS" index.html`) | Fix or change it in all three; test: `python3 scripts/test_planning_tools.py` |
| Planner Monte Carlo results: the "This run" box, Re-run another scenario, and the "Judge the plan by" on-track toggle (same code in all 3 planners) | the planner repo: CLAUDE.md, `docs/common-edits.md` recipe 17 (`grep -n "mcRunBannerHtml\|mcSetJudge" index.html`); test `python3 scripts/test_mc_run.py` | Display only; never change `runMonteCarlo` maths for this. Quebec: French entries too |
| Planner "sell your home" option (downsize or rent, proceeds into TFSA / non-registered; same code in all 3 planners) | the planner repo: CLAUDE.md, `docs/common-edits.md` recipe 18 (`grep -n "hsNetProceeds\|homeSaleCard" index.html`); test `python3 scripts/test_home_sale.py` | Per person (couple: one form only). Never add tax to the sale: principal residence. Quebec: French entries too |
| Planner save and load (results "Save scenario" button, menu "Load scenario", optional cloud copy, delete on device or device and cloud; same code in all 3 planners) | the planner repo: CLAUDE.md, `docs/common-edits.md` recipe "Save and load (3 principles)" (`grep -n "saveScenario\|renderCloudBox\|awrDeletePlan" index.html account.js`); tests `python3 scripts/test_account.py`, `scripts/test_planning_tools.py` step 6d | Local first, cloud optional. `account.js` must stay identical in all three planners (Quebec Checks fails otherwise). Quebec: add French entries |
| Planner results chart and headline: stacked withdrawal bars, solid lines at the QPP/CPP and OAS start ages, tap a bar to open that year, green tick / red X beside the verdict (same code in all 3 planners) | the planner repo: `docs/common-edits.md` (`grep -n "withdrawChartSvg\|heroIcon\|goToYear" index.html`); test `python3 scripts/test_planning_tools.py` | Display only; never change a calculation. Quebec needs French entries |
| Planner wording: renaming "Everyday spending" (Money label, results year cards, French) or any shared label | the planner repo: CLAUDE.md "Words to keep the same everywhere", `docs/common-edits.md` recipe 19; test `python3 scripts/test_home_sale.py` | Change English, the (i) note, French entries (Quebec) and the guide together. Never reintroduce "living costs" |
| Spam, keys, accounts, DNS | `docs/KEYS.md` | Sign-ins are Robert's to click |

All share ONE Supabase project and one login. Who can open what is set at access.imetrobert.com.

## What watches things for you (you get an email when one goes red)
- **Monday: Weekly health check** (this repo, Actions). Opens every site, checks Supabase, every repo's latest automated runs,
  certificates, domain registration, and the dates in `ops/expiries.json`. Edit that file when you renew a key or token.
- **Sunday: Weekly Supabase backup** (this repo). Encrypted copy of every table, 90 days. Restore guide: `docs/BACKUP-RESTORE.md`.
  Setup needs two secrets once (see that guide, step 1).
- **Monthly: Dependabot** in the invoicing, ETF and jobs repos opens one update pull request; the "Build check" says if it is
  safe. Green: Merge. Red: leave it, or paste the failing log to Claude.
- **1st and 15th: Keepalive commit** (workflow `keepalive-commit.yml` in the hub, seniors, business, toolkit, ETF, marketplace, the three retirement planners, the invoicing app, and `keepalive.yml` in the blog). One tiny bot commit so GitHub never switches off a repo's scheduled jobs after 60 days with no commits (all repos are public). Nothing to do. If a scheduled job ever stops firing, run this workflow by hand from Actions, then re-enable the scheduled workflow if GitHub shows it as disabled.
- Blog: Actions > Blog health report; Pipeline health page on the review page; `docs/DIAGNOSE.md` in the blog repo.

## Tool versions (upgraded 28 Nov 2026; do not re-do these)
Invoicing, jobs and ETF run **React 19, Vite 8 and plugin-react 6**; the blog's workflows run **Python 3.13**; ETF reads PDFs with **pdfjs-dist 6** and screenshots with **tesseract.js 7**. Each was one pull request with a build check and a browser test, so one tap on **Revert** on that merged PR undoes it.
- **Left on purpose:** `@emailjs/browser` stays on **v4** in the invoicing app (v5 exists, no end-of-support date found, and a real send cannot be tested). Dependabot ignores major npm updates, so none of these will pop up as a pull request. Re-check only if EmailJS announces an end date.
- **Two checks run on every pull request** in the app repos (`pr-build.yml` / the Checks workflow), so a green PR means it builds. A red "Commit the code map" step on a push is only a race between two quick merges and fixes itself on the next push.
- **ETF test quirk:** `npm test` shows one failure for the 9.5-month pension contribution figure ($1 off) when run in Toronto time; it passes in UTC, which is what CI uses. Not a live bug.
- **Not yet confirmed on a phone:** a real Manulife statement PDF and a real pension screenshot on the ETF Import and Pension pages after the pdfjs/tesseract upgrade. If either fails, Revert PR #35 in `tsx-etf-signal-notifier`.

## Once a year
`docs/JANUARY-CHECKLIST.md`: the new tax numbers for the three retirement planners (and the few other yearly renewals). The health check goes red from 1 January until it is done.

## Search and AI-answer visibility
`docs/SEO-AIO-GEO.md`: what is automatic, a 10-minute monthly routine and paste-ready prompts (add a guide, fix a Search Console issue, turn on the rating schema).

## Email (how imetrobert.com and aiwithrobert.com mail is set up)
`docs/EMAIL-SETUP.md`: receiving (registrar forwarding into Gmail), sending (Brevo SMTP; Gmail send-as until January 2027, then Apple Mail),
agent rules and known quirks. Open it for any "I can't send / didn't receive / landed in spam" question.

## Robert's tools and habits (so free Claude never has to ask)
- **Works on an iPhone only**: edits through GitHub's web pages and Safari. Give phone-friendly steps; never ask him to use a terminal or a desktop.
- **Analytics**: one shared Google Analytics property (539541576) for the Seniors and Business sites, split by the "Site" dimension; link: https://analytics.google.com/analytics/web/#/p539541576/reports/intelligenthome. His Looker Studio report "Website results" sits in his Google account (https://lookerstudio.google.com/); its link is pasted into the toolkit's Website analytics screen, kept per device in the browser, so a new phone shows empty boxes until he pastes it again. If the link is lost, he re-copies it from Looker Studio (Share, Copy link).
- **Own-visit opt-out**: opening any of his sites once with `?countme=1` stops counting that device in the toolkit counters and Google Analytics; `?countme=0` counts again. His Home Screen shortcuts carry it.
- **Agents he uses**: Muse (his email and day-to-day agent; any @aiwithrobert.com mail is business mail and it gives a paste-ready draft; it only needs his GitHub sign-in for on-request code changes, nothing scheduled depends on it) and Instinct (keeps his list of prompts to give free Claude). Both are his; free Claude cannot reach them.
- **GitHub upkeep needs no sign-in**: `keepalive-commit.yml` (1st and 15th) stops GitHub pausing scheduled jobs; the blog uses `keepalive.yml`.
- **Free-tier rules**: free tools only, no paid services. Quota note: the blog's free Gemini allowance is about four full runs a day.
- **Public channels**: YouTube channel and intro videos are listed in `docs/APPS.md`. YouTube cannot be edited by Claude; he does that in YouTube Studio.

## Keys and secrets
`docs/KEYS.md` lists every key and secret, what breaks when one dies and the link to replace it.

## Prompts to paste (replace the capitals)
Add the start link to every prompt (free Claude cannot open a repo by name): https://raw.githubusercontent.com/imetrobert/aiwithrobert-root/main/docs/START-HERE.md . Other files: use their link from `docs/LINKS.md`.

**Something is broken**
> Repo imetrobert/REPO. Read only CLAUDE.md and FILE. This error appeared: ERROR TEXT. Find the cause and give me the smallest
> edit as a ready-to-paste replacement for that one section. Do not read other files unless you must, and say which.

**A health check turned red**
> Open the failing run of "Weekly health check" in imetrobert/aiwithrobert-root (link in the email). Read docs/START-HERE.md and
> the line marked FAIL. Tell me what is wrong and the fix. Ask before touching any other repo.

**Change wording or a price** (SENIORS prices live in the Seniors site `index.html`, `js/i18n.js`, `js/language.js`, `llms.txt`, `scripts/articles_data.py` AND the invoicing app `src/lib/services.js` (starter-package, complete-package); derived text such as "save $25" and "$55/hr" must be recomputed. A BUSINESS price lives in FIVE places: the Business site `index.html` + `js/i18n.js` + `llms.txt`, the toolkit
`FX_PRICE`, and the invoicing app `src/lib/services.js` BUSINESS_SERVICES; the repos' own weekly checks flag any mismatch)
> I want to change PRICE/WORDING from X to Y. Read CLAUDE.md and docs/common-edits.md in REPO and list every file and line to
> change. Then give me each edit as a small snippet.

**The blog review page or a monthly run failed**
> Repo imetrobert/imetrobert.github.io. Read docs/DIAGNOSE.md. The run log says: PASTE THE ONE LINE FROM THE HEALTH PAGE.

**Add a small feature or fix to a retirement planner** (Quebec, Ontario or Personal; each is one `index.html` plus a small `account.js`)
> Repo imetrobert/REPO (aiwithrobert-retireqc, aiwithrobert-retireon or imetrobert-retire). Read only CLAUDE.md and
> docs/common-edits.md (recipe 9; for the yearly tax update use recipe 1 and docs/JANUARY-CHECKLIST.md instead). I want: WHAT I SEE AND WHERE. Use grep or docs/code-map.md, never read index.html whole. Give me
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
A person who never accepted can be sent a fresh invitation from their card ("Resend invitation"); the app list also lives in migration/resend_invite.sql (four copies in all; see COMMON-EDITS.md in that repo). If it says Supabase's email limit was reached, that is Supabase's hourly auth-email cap (nothing was sent): wait an hour and try one person; recipe in the same file.

## What free Claude cannot do (say so quickly instead of trying)
- It may not remember earlier chats: always open with the START-HERE opener and name the repo, the one file and the error. The opener is: "Read docs/START-HERE.md in imetrobert/aiwithrobert-root first (link: https://raw.githubusercontent.com/imetrobert/aiwithrobert-root/main/docs/START-HERE.md). Then read FILE in imetrobert/REPO. Then TASK. Do not read anything else." (Capitals are what Robert fills in.)
- It cannot run code or tests; the repo's own CI does ("Checks" or "Build Assets" in Actions). Commit, wait 2-3 minutes, read the run.
- It can open only web links (see "How to open a file"); it cannot open repo names, Actions logs or anything behind a sign-in. Paste the one section or the failing log lines.
- It cannot log in anywhere for you: Supabase, Brevo, EmailJS, the registrar, GitHub tokens, YouTube Studio and Search Console are yours to click. KEYS.md has the links.
- Needs a desktop (rare): the Google Cloud setup for a Search Console data pull. Everything else here works from the phone.

## Cheap-editing rules that save the most credits
1. Edit on GitHub from your phone: open the one file, search for the exact text, change it, commit. Most content changes need
   no Claude at all (see each repo's "Editing without Claude Code" section).
2. Never paste a whole big file (the toolkit `index.html`, `css/style.css`, `renderer.py`). Paste the one section.
3. Do not hand-edit generated files (`fr/index.html`, `js/bundle.js`, `css/styles.css`, blog posts); edit their source.
4. After any change to a site, wait 2-3 minutes for GitHub Pages, then reload.
5. Gemini (blog) is a free key with daily limits: run at most one or two full trial issues in a day.
