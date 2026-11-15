# Search, AI answers (AIO/GEO) and local visibility: what is automatic, what is a 10-minute monthly job

## Already automatic (no action)
- Every push to a site repo rebuilds the French page, guide/service pages, `sitemap.xml` (EN/FR hreflang) and `llms.txt`, then
  pings IndexNow (Bing and others). Schema (JSON-LD) lives in each site's `index.html`.
- Weekly health check (Actions > Weekly health check) now also fails, and emails you, if a site gets a `noindex` tag, robots.txt
  blocks the site, JSON-LD breaks, the analytics tag disappears, a sitemap URL goes dead, the feasibility table stops answering
  or the blog has no new issue for 40 days.

## Monthly, from your phone (about 10 minutes)
1. Search Console (seniors, biz, blog): Pages > any "not indexed" new reason? Performance > top 5 queries. Paste anything odd to Claude.
2. Google Business Profile (Seniors only): one photo or post, reply to every review.
3. After each session ask for a Google review (the review count is the biggest local-ranking lever; the rating schema below waits on it).
4. AI answer check: ask ChatGPT, Gemini, Perplexity and Claude: "AI tutor for seniors in Côte Saint-Luc", "AI training for small businesses
   in Montreal", "who is Robert Simon AI Montreal". Note whether the sites or the blog are named or cited. Missing: add or sharpen a guide on that exact question.
5. Add ONE guide or service page (answer a real question a client asked). It is a single data entry, see below.

## Prompts to paste into free Claude (replace the capitals)
**Add a guide (Seniors)**
> Repo imetrobert/aiwithrobert. Read only CLAUDE.md and scripts/articles_data.py. Add one guide answering: QUESTION. Match the existing
> entries (EN and FR, short answer first, 3-5 sections, independence note). Give me the new entry as a snippet to paste at the end of the list.
> CI builds the page, sitemap, llms.txt and IndexNow.

**Add a page (Business)** same prompt with imetrobert/aiwithrobert-biz and scripts/pages_data.py. Then ALSO update `TARGETS`
(scripts/promo_kit.py) and `RELATED_PAGES` (scripts/utils.py) in imetrobert.github.io, or blog links will not point to it.

**Search Console reports a problem**
> Repo imetrobert/REPO. Read only CLAUDE.md. Search Console says: PASTE THE MESSAGE AND THE EXAMPLE URL. Tell me the cause and the one smallest edit.

**Turn on the star rating (Seniors, only when there are at least 3 real Google reviews)**
> Repo imetrobert/aiwithrobert. Read CLAUDE.md. I now have N Google reviews averaging X.X. Find the aggregateRating block in index.html
> (and any matching text in llms.txt), activate it with these exact numbers and tell me every place that must change.

## Rules that protect the rankings (do not break)
- Phone, email, prices and hours must be identical everywhere (each repo's CLAUDE.md lists the places; `scripts/check_site.py` catches drift).
- Ratings, reviews and client results only if real and public (Google reviews). Examples on the Business site stay labelled illustrations.
- One Google Business Profile only (Seniors). Do not add one for Business.
- Renaming or deleting a page: leave a redirect, update the sitemap script data and the blog's TARGETS/RELATED_PAGES.
- Keep `llms.txt` facts equal to the home page (check_site.py enforces prices).
