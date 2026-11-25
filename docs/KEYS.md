# Keys and secrets: what each one is, what breaks, how to replace it

Where a secret lives in GitHub: `https://github.com/imetrobert/REPO/settings/secrets/actions` (tap the name, paste the new value, Update secret).
Never paste a key into a chat or a file. After replacing a key, re-run the failed workflow from the repo's Actions tab, then delete the old key where you made it.
Most keys never expire. They stop working only if you delete, rotate or reset them, or the service closes the account. Dates that do expire go in `ops/expiries.json`.

## Supabase (one project for everything: ipnajvgwtjrlecbqfwrh)
| Secret | Used by | Where it lives | What breaks | Replace at |
|---|---|---|---|---|
| Anon / publishable key (VITE_SUPABASE_ANON_KEY, public by design) | every site's sign-in | repo secrets of invoicing, ETF, jobs; in the code of the others | site cannot sign in or load data | https://supabase.com/dashboard/project/ipnajvgwtjrlecbqfwrh/settings/api-keys |
| Secret key SUPABASE_SERVICE_ROLE_KEY | ETF daily signals, Jobs scan and digest | repo secrets of tsx-etf-signal-notifier and jobs | red run, message names the secret and links this page | same page: create a new secret key, paste it into the secret |
| Secret key SUPABASE_SERVICE_KEY (named "backups") | Sunday backup | repo secret of aiwithrobert-root | backup run fails with fix steps | same page |
| Secret key auth_secret_key | invite function (access page) | Supabase vault | invitations fail; the error message gives the fix | same page, then the vault command shown in the error |
| SUPABASE_URL / VITE_SUPABASE_URL | scheduled jobs and builds | repo secrets | everything fails to connect | it is `https://ipnajvgwtjrlecbqfwrh.supabase.co`; do not change |
| SUPABASE_DB_URL (database connection string) | ETF schema auto-apply | repo secret of tsx-etf-signal-notifier | schema changes stop applying | https://supabase.com/dashboard/project/ipnajvgwtjrlecbqfwrh/settings/database (copy the connection string; it holds the database password) |
| SUPABASE_ACCESS_TOKEN (personal token) | deploying the Marketplace and Claims tracker edge functions | repo secret of Facebook-marketplace-generator and of claims-tracker | "Deploy Supabase function" workflow fails | https://supabase.com/dashboard/account/tokens |

## Gemini and other AI keys
| Secret | Used by | What breaks | Replace at |
|---|---|---|---|
| GEMINI_API_KEY (blog) | monthly blog, redrafts, Model Scout | no issue gets generated; the run log says why | https://aistudio.google.com/apikey, then update the secret in imetrobert.github.io |
| GEMINI_API_KEY (jobs) | weekly job scoring; cover letter and CV button | scan scores nothing, or the cover letter button fails | same page; update the secret in jobs, and also the copy in Supabase (https://supabase.com/dashboard/project/ipnajvgwtjrlecbqfwrh/functions > generate-application > Secrets) |
| GEMINI_API_KEY (Marketplace) | listing generator | listings fail | same page; update the GitHub secret, then run the "Deploy Supabase function" workflow with the box "Also update GEMINI_API_KEY from the repository secret" ticked (it copies the key into Supabase for you) |
| CLAIMS_GEMINI_API_KEY (Claims tracker) | reads receipts and claim forms for tax.imetrobert.com | receipt scanning fails | https://aistudio.google.com/apikey, then set it as a Supabase function secret: https://supabase.com/dashboard/project/ipnajvgwtjrlecbqfwrh/functions > claims-extract > Secrets (it is not in GitHub) |
| ANTHROPIC_API_KEY (jobs, optional) | used for scoring and cover letters only if it is set; otherwise Gemini is used | nothing, if unset | https://console.anthropic.com/settings/keys |

## Email
| Secret | Used by | What breaks | Replace at |
|---|---|---|---|
| EMAILJS_PUBLIC_KEY, EMAILJS_PRIVATE_KEY, EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, NOTIFY_EMAIL | ETF alert emails | no alerts (prices still refresh) | https://dashboard.emailjs.com/admin (Account > API keys; IDs are on the Email Services and Email Templates pages). NOTIFY_EMAIL is just the address alerts go to |
| VITE_EMAILJS_PUBLIC_KEY, _SERVICE_ID, _TEMPLATE_ID | invoicing app emails | invoices cannot be emailed | same dashboard; secrets in the invoicing repo; redeploy by merging any change or running Deploy |
| Brevo SMTP login and key (the same Brevo account also sends the Gmail "Send mail as" / Apple Mail mail, see EMAIL-SETUP.md) | the email service behind EmailJS: ETF alerts, invoice emails, blog review notices; keeps the sender checks (DKIM, DMARC) passing | emails stop or land in spam | make a new SMTP key in your Brevo account (SMTP & API), then paste it into the email service at https://dashboard.emailjs.com/admin (Email Services > your Brevo service). It is stored there, not in any GitHub secret |

EmailJS free plan: 200 emails per cycle, resets on the 10th (the invoicing dashboard shows usage).

## Job search feeds (jobs repo, all optional sources)
ADZUNA_APP_ID and ADZUNA_APP_KEY (https://developer.adzuna.com/), JOOBLE_API_KEY (https://jooble.org/api/about), JSEARCH_RAPIDAPI_KEY (https://rapidapi.com/developer/apps). If one dies the scan skips that source; the rest keep working.

## Passphrase and browser tokens
- **BACKUP_PASSPHRASE** (aiwithrobert-root secret): opens the encrypted backups. It is saved in the notes section of the password-manager entry for invoices.imetrobert.com. If it is lost the backups cannot be opened, so check the note exists. To change it, set a new value; old backups still need the old one.
- **Browser GitHub tokens** (blog review page, Jobs Refresh button): both are fine-grained, limited to their own repo, no expiry. When GitHub rejects one, the page shows links to make a new one and delete the old one. Lists: https://github.com/settings/personal-access-tokens and https://github.com/settings/tokens

## Quick rule
Red run or broken page with the word "key", "token", "401" or "rejected" in the message: find the name in this page, replace it at the link, re-run, delete the old one.
