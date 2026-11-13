# aiwithrobert.com (hub) — working guide

GitHub Pages repo for the root domain (`CNAME` = aiwithrobert.com). It is the parent
brand's front door: a short intro plus one card per sub-brand. Tiny repo; read this,
then open only the file you need.

## Generated pages — never hand-edit

`index.html` (EN) and `fr/index.html` (FR) are built by `scripts/build_hub.py`.
Edit the script, not the pages. A GitHub Action (`build-hub.yml`) rebuilds and commits
them when `scripts/build_hub.py` changes on `main`; locally: `python3 scripts/build_hub.py`.

- Add or change a sub-brand card: edit the `BRANDS` list (EN + FR text, URL, logo, hero,
  colours). The grid grows automatically.
- Live cards are whole-card links. Seniors links to `?lang=en` (EN) or `/fr/` (FR) so the
  hub's language carries over; any new live card must use the same pattern.
- `NOINDEX` flag: currently `False` (indexable). Contact emails: `info@` general, `biz@` Business card.
- Hero images: `img/hero-<brand>-640.jpg/.webp`; logos: `img/logo-*.png`.

## Hand-edited files

| File | Purpose |
|------|---------|
| `llms.txt` | How the sites relate, independence from Bell Canada, disambiguation from aiwithrobert.live, official profiles. Keep in sync with seniors/biz `llms.txt` |
| `sitemap.xml`, `robots.txt` | Sitemap for `/` and `/fr/`; robots advertises it |
| `404.html` | Path-preserving redirect for old aiwithrobert.com URLs to seniors.aiwithrobert.com |
| `seniors/`, `seniors/fr/`, `aines/` | Noindex redirect pages to the seniors site |
| `feasibility/`, `feasability/` (misspelling), `faisabilite/` | Noindex redirects to the free feasibility check on the Business site (EN `/#feas-check`, FR `/fr/#feas-check`). Short links to send clients |
| `business/`, `business/fr/`, `biz/`, `biz/fr/`, `entreprises/`, `affaires/` | Noindex redirect pages to biz.aiwithrobert.com |

Redirect pages stay noindex and unlisted in the sitemap. The hub's JSON-LD (Organization
`https://aiwithrobert.com/#organization` with `subOrganization` links, Person
`https://www.imetrobert.com/#robert-simon`) is emitted by `jsonld()` in `build_hub.py`.

## Sibling repos

- `imetrobert/aiwithrobert` → seniors.aiwithrobert.com
- `imetrobert/aiwithrobert-biz` → biz.aiwithrobert.com
- `imetrobert/imetrobert.github.io` → www.imetrobert.com (personal site + monthly blog)
- Email lives at Name Services (forwarding to Gmail); DNS stays there.
