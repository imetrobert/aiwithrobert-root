# January checklist (once a year)

Do this in the first half of January. The weekly health check turns red from 1 January because of the dated item in
`ops/expiries.json` ("Update tax numbers for the new year"). When done, move that date to the next 15 January: in `ops/expiries.json` find the entry named "Update tax numbers for the new year" and change its date field to the next 15 January. If the official 2027 tables are not published yet, wait and paste them when they are; never guess a number.

Rule: never invent a number. Open the official table (links below), copy the figures, and name the table in your commit.

## 1. The three retirement planners (about 20 minutes each with Claude)
Repos: `aiwithrobert-retireqc` (Quebec), `aiwithrobert-retireon` (Ontario), `imetrobert-retire` (personal).
Each repo has the full steps in `docs/common-edits.md`, recipe 1 "Yearly tax update", which now ends with a "January checklist, key by key" listing every `getDefaultTaxRules()` key that usually changes and every one that normally stays. In short, in each repo:
1. `getDefaultTaxRules()` in `index.html`: brackets, basic amounts, age and pension credits, `verifiedDate`.
2. `TFSA_ANNUAL_LIMIT` (grep it).
3. Default maximum QPP/CPP and OAS monthly amounts (OAS changes each quarter).
4. `APP_VERSION` and the `<title>` ("2026 rules" becomes the new year). Also search each repo for "2026" in the page text and in `docs/guide/en.md` (and `fr.md` in Quebec); the guide PDF is rebuilt by its workflow.
5. `scripts/test_tax.py`: update its own "PARAMETERS" block at the top to the same official numbers.
   It is a deliberate second copy, so a typo in one shows up as a red check.
6. Quebec only: `python3 scripts/audit_french.py` if any English wording changed.
Sources: canada.ca (CRA indexation of tax brackets and amounts), revenuquebec.ca, ontario.ca (Ontario income tax rates),
canada.ca (OAS payment amounts, TFSA dollar limit), retraitequebec.gouv.qc.ca (QPP maximums), canada.ca (CPP maximums).
Free Claude prompt: use the "Add a small feature or fix" prompt in `docs/START-HERE.md`, say "do recipe 1, Yearly tax update, for YEAR".
Check afterwards: the Checks workflow is green; open the page, press "Show my plan", money in equals money out each year.

## 2. Invoicing app
GST (5%) and QST (9.975%) rarely change. Only if the government announces a change: `src/lib/invoiceUtils.js`, then
`node scripts/check_money.mjs`. EmailJS quota resets on the 10th each month.

## 3. ETF tracker and jobs
Nothing yearly. If the weekly health check shows a red run there, use the "Something is broken" prompt in `START-HERE.md`.

## 4. Renewals and dates
Open `ops/expiries.json` and `docs/KEYS.md`: renew anything dated in the next 3 months and update the date.
