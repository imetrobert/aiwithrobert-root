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
Where: access.name-services.com, Domain Settings, Host Records (DNS Settings = Default). Domain expires 2031-01-12. Public information only; no passwords. Other domain (imetrobert.com) not yet recorded here.
| Host | Type | Value |
|------|------|-------|
| @ (4 rows) | A | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (GitHub Pages) |
| @ | TXT | SPF: `v=spf1 include:_spf.google.com include:spf.emailj...` (end of line cut off on screen; open the row to read it all) |
| @ | TXT | `brevo-code:bc67496265e240afb0ce9d91f7405044` (Brevo domain check) |
| _dmarc | TXT | `v=DMARC1; p=quarantine; rua=mailto:rua@dmar...` (end cut off on screen) |
| brevo1._domainkey | CNAME | b1.aiwithrobert-com.dkim.brevo.com. |
| brevo2._domainkey | CNAME | b2.aiwithrobert-com.dkim.brevo.com. |
| q7pam4nsvc6x | CNAME | gv-ex4nm2isbhxxtx.dv.googlehosted.com. (Google verification record) |
| www, biz, invoices, seniors, toolkit, retireon, retireqc, retraiteqc | CNAME | imetrobert.github.io. (GitHub Pages) |
- No MX records are listed: mail is received through the registrar's Email Forwarding (biz@, forms@, info@, invoices@, robert@, seniors@ forward to Robert's Gmail, all enabled). Forwarding changes can take up to 60 minutes.
- The SPF line lists Google and EmailJS but no Brevo include on screen; check the cut-off part for Brevo. Brevo's DKIM records above are present. This may relate to the open deliverability question; not confirmed.
- To finish this table: open the two cut-off TXT rows and paste the full values to Claude.

## Related
Invoices are emailed through EmailJS (200 per cycle, resets on the 10th), a separate path. See `docs/KEYS.md`.
