# All my apps at a glance (updated 2026-11-22)

Ask Claude: "Read APPS.md and tell me about all my apps." For repos, how to fix things and paste-ready prompts, see START-HERE.md.
"Login" = the shared AI with Robert login (one email and password for everything); access per app is set at access.imetrobert.com.

## Public (no login, on purpose)
| App | Address | What it does |
|---|---|---|
| Hub | aiwithrobert.com (EN and /fr/) | Front door for the AI with Robert brand: one card per sub-brand |
| Seniors site | seniors.aiwithrobert.com (EN and /fr/) | AI tutoring for seniors in Cote Saint-Luc: services, prices, bookings, FAQ, guides |
| Business site | biz.aiwithrobert.com (EN and /fr/) | AI help for small Canadian businesses: services, prices, before/after examples, the free feasibility check (main lead form) |
| Blog and personal site | www.imetrobert.com | Robert's personal brand site plus the monthly "Practical AI for Canadian Business" blog; each issue links to the feasibility check |
| Invoice client link | invoices.aiwithrobert.com/#/invoice/public/TOKEN | A client's own invoice page. No login: anyone with that private link can view that one invoice |

## Behind the login (private)
| App | Address | What it does | Who can enter |
|---|---|---|---|
| Toolkit | toolkit.aiwithrobert.com | Admin tool: client session materials, feasibility check results, Leads pipeline, website availability (at-capacity mode), surveys | access "toolkit" |
| Invoicing | invoices.aiwithrobert.com | Create, email and track invoices for both brands, English or French, GST/QST, tax summary | access "invoicing" |
| ETF tracker | invest.imetrobert.com | TSX ETF buy/sell alerts by email, holdings import (Manulife, Wealthsimple), cost and gain/loss, export to retirement planner | access "etf" |
| Marketplace generator | fbmarket.imetrobert.com | Turns item photos into a finished Facebook Marketplace listing | access "fb-marketplace" |
| Claims tracker | tax.imetrobert.com | Tracks Manulife dental/health claims per family member by tax year for the accountant | access "claims-tracker" |
| Job search | jobs.imetrobert.com | Scans for job postings and tracks your applications | access "job" |
| Quebec Retirement Planner | retireqc.aiwithrobert.com (French: retraiteqc.aiwithrobert.com, forwards here) | Quebec retirement calculator (RRSP, QPP, OAS, LIRA, tax) in English and French, with encrypted saved plans per login and a user guide | access "retire-qc" |
| Ontario Retirement Planner | retireon.aiwithrobert.com | Same for Ontario (CPP, Ontario tax), English only | access "retire-on" |
| Personal Retirement Planner | retire.imetrobert.com | Robert's own planner (Bell-style DC pension, Manulife/Wealthsimple, ETF import); only Robert, never grant to anyone else | access "retire-personal" |
| Access rights | access.imetrobert.com | Grant or remove each person's access to each app; send invitations | platform admin only |
| Blog review pages | www.imetrobert.com/blog/staging/ (review, Pipeline health) | Review, redraft, approve or discard the monthly blog issue; see run logs | access "blog-review" |

## Not web apps
- (The retirement planners are now web apps; see the three rows above.)
- CartMatch (pricecheck.imetrobert.com): retired in November 2026.

## Automatic watchers
Monday health check, Sunday encrypted backup, monthly dependency updates, the blog's own run log. Details: START-HERE.md.

## QR code for talks and print
`img/qr-feasibility-talk.png` (navy on white, 1 inch minimum when printed) opens the Business site's free feasibility check; the visit is saved on the lead as `qr/talk` and shown in the toolkit's "Where leads come from". For a different event, regenerate with another `utm_campaign` (python `qrcode` package: URL `https://biz.aiwithrobert.com/?utm_source=qr&utm_medium=print&utm_campaign=<event>#feas-check`).
