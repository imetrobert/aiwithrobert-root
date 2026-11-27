# Email setup: imetrobert.com and aiwithrobert.com

How every address receives and sends, and where each setting lives. No passwords are kept here. Last reviewed: 2026-11-26.

## Addresses
- Sending addresses: robert@imetrobert.com, robert@aiwithrobert.com, biz@aiwithrobert.com, invoices@aiwithrobert.com.
- Contact addresses on the sites: info@ and biz@ (hub), seniors@ (Seniors site), biz@ (Business site).
- None of these has a real mailbox. The registrar (access.name-services.com, also where DNS lives) only does **Email Forwarding** into Robert's Gmail.

## Receiving
Registrar Email Forwarding, both domains, everything to Gmail. Nothing is stored at the domain. An old Sympatico account fetched by POP3 is unused and may be purged.

## Sending
- All four addresses send through the **Brevo SMTP relay** (smtp-relay.brevo.com, port 587). Brevo DKIM records are set on both domains. Brevo is on the free plan (300 per day; about 20 a day are sent).
- **Until January 2027:** Gmail iPhone app, "Send mail as" entries for these addresses.
- **From January 2027:** Gmail ends send-as for third-party addresses. Replacement: **Apple Mail on iPhone**, same Brevo SMTP. The iPhone Mail account was set up on 2026-11-20 and test sends from both domains worked.
- Google Workspace was weighed as the paid alternative and not chosen.

## Where sent copies appear
Mail sent through Brevo from Apple Mail has no server-side Sent folder (the domains have no mailbox), so it does not show in the Mail app's Sent or All Sent. Robert accepts this (2026-11-24). Gmail-app sends are saved in Gmail's Sent.

## Agents (Instinct, Muse)
- Plan: personal and non-AIWithRobert mail goes out as his Gmail address with Reply-To robert@imetrobert.com. AIWithRobert.com mail is sent by hand from Apple Mail.
- Rule given to both agents (2026-11-20): mail from any @aiwithrobert.com address is business mail and never falls back to Gmail; the agent gives a paste-ready draft instead. robert@imetrobert.com may fall back to Gmail only if the send definitely failed. Robert approves recipients and wording first. No test sends or settings changes.
- Muse cannot see Gmail send-as addresses, so it gives drafts for all @aiwithrobert.com mail.
- Open question: whether Instinct keeps its Gmail send-as ability after January 2027.

## Deliverability
Priorities: 1) keep sending from these addresses after January 2027; 2) avoid spam folders. A November 2026 email from imetrobert.com to a gmail.com recipient landed in Promotions/Spam; the investigation was started and is not closed.

## DNS records for aiwithrobert.com (copied from the registrar screen, 2026-11-26)
Where: access.name-services.com, Domain Settings, Host Records (DNS Settings = Default). Domain expires 2031-01-12. Public information only; no passwords.
| Host | Type | Value |
|------|------|-------|
| @ (4 rows) | A | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (GitHub Pages) |
| @ | TXT | SPF: `v=spf1 include:_spf.google.com include:spf.emailjs.com include:spf.brevo.com ~all` (Google, EmailJS, Brevo; complete) |
| @ | TXT | `brevo-code:bc67496265e240afb0ce9d91f7405044` (Brevo domain check) |
| _dmarc | TXT | `v=DMARC1; p=quarantine; rua=mailto:rua@dmarc.brevo.com` (complete; reports go to Brevo) |
| brevo1._domainkey | CNAME | b1.aiwithrobert-com.dkim.brevo.com. |
| brevo2._domainkey | CNAME | b2.aiwithrobert-com.dkim.brevo.com. |
| q7pam4nsvc6x | CNAME | gv-ex4nm2isbhxxtx.dv.googlehosted.com. (Google verification record) |
| www, biz, invoices, seniors, toolkit, retireon, retireqc, retraiteqc | CNAME | imetrobert.github.io. (GitHub Pages) |
- No MX records are listed: mail is received through the registrar's Email Forwarding (biz@, forms@, info@, invoices@, robert@, seniors@ forward to Robert's Gmail, all enabled). Forwarding changes can take up to 60 minutes.
- SPF includes Brevo, and Brevo's DKIM records are present, so aiwithrobert.com is correctly set up for Brevo sending.

## DNS records for imetrobert.com (copied from the registrar screen, 2026-11-26)
Same registrar screen, DNS Settings = Default. Domain expires 2036-09-29. No passwords. Family forwarding addresses are deliberately not listed here.
| Host | Type | Value |
|------|------|-------|
| @ (4 rows) | A | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (GitHub Pages) |
| @ | TXT | `brevo-code:bc67496265e240afb0ce9d91f7405044` |
| @ | TXT | SPF: `v=spf1 include:_spf.hostedemail.com include:_spf.emfwd.name-services.com include:spf.brevo.com mx ~all` (Brevo added 2026-11-26 by Robert; he re-opened the row and the saved value matched) |
| _dmarc | TXT | `v=DMARC1; p=none; rua=mailto:rua@dmarc.brevo.com` (monitoring only) |
| brevo1._domainkey / brevo2._domainkey | CNAME | b1.imetrobert-com.dkim.brevo.com. / b2.imetrobert-com.dkim.brevo.com. |
| enoms1._domainkey | TXT | `v=DKIM1;t=s;p=MIGfMA0GCSqGSIb3DQEBAQUA...` (registrar's own DKIM public key, complete on the registrar screen) |
| hguv54hap5ji | CNAME | gv-kbjvsiuz2iqdcv.dv.googlehosted.com. (Google verification) |
| www, access, fbmarket, invest, jobs, retire, tax | CNAME | imetrobert.github.io. (GitHub Pages) |
| ebook | CNAME | domains.gumroad.com. |
| ai, aimarketing | URL redirect | a Gumroad product page |
| blog | URL redirect | https://www.imetrobert.com/blog |
| facebook, linkedin, twitter, youtube, videochat | URL redirect | his profile and video-room links |
- No MX records. Email Forwarding is on for about 13 addresses (robert@, forms@, invest@, eq@, junk@, tangerine@, test@, Windscribe@, three belltest addresses, and two family addresses), most to Robert's Gmail.
- Differences from aiwithrobert.com: DMARC here is p=none (aiwithrobert.com is p=quarantine). The SPF here had no Brevo include until 2026-11-26, when Robert added `include:spf.brevo.com` (before: only hostedemail and the registrar's forwarding include). DMARC stays p=none until a header test shows Brevo mail passing DKIM and every sender uses Brevo. Not confirmed as the cause of the November spam-folder case.

## Test result: mail-tester, 2026-11-26
Sent from robert@imetrobert.com (Apple Mail through Brevo SMTP) to mail-tester.com: 7.5/10. Authenticated: DKIM valid and aligned with imetrobert.com (this is what satisfies DMARC), SPF pass (for Brevo's own sending domain, so the SPF include added to imetrobert.com is harmless but not what carries the mail), good sender reputation, not blocklisted, no broken links. Lost points were content only: HTML-only message with little text, a remote image, and the normal "From and envelope-from differ" for Brevo. A retest with a few sentences of plain text and no signature image should score higher. The earlier November spam-folder case is still not explained.
Second test, from biz@aiwithrobert.com (same route): 8.5/10, properly authenticated (DKIM valid and aligned with aiwithrobert.com, SPF pass, good reputation, not blocklisted). Lost points: 2 images without alt text in the message (-0.5), HTML and plain-text parts differ (-0.7), and the normal Brevo From/envelope difference. So the stricter DMARC p=quarantine on aiwithrobert.com is safe for mail sent this way. Small gain available: add alt text to images in the email signature or template.

## Related
Invoices are emailed through EmailJS (200 per cycle, resets on the 10th), a separate path. See `docs/KEYS.md`.
