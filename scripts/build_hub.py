#!/usr/bin/env python3
"""Builds the hub homepage: index.html (EN) and fr/index.html (FR).

This page is a front door for people who type aiwithrobert.com directly, not an
SEO page. To add a sub-brand later: add one entry to BRANDS below (EN + FR
text, URLs, logo file, colours) and re-run this script. The card grid grows
automatically (2 -> 3 -> 4 ...).
"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://aiwithrobert.com"
PHONE = "514-250-8491"
EMAIL = "info@aiwithrobert.com"
BIZ_EMAIL = "biz@aiwithrobert.com"  # Business card "get in touch"

# Launch switch: while NOINDEX is True the page asks search engines not to list it.
# (False since the Business launch; sitemap.xml is in the repo root.)
NOINDEX = False

# -- Sub-brands (add new ones here) -----------------------------------------
BRANDS = [
  dict(id="seniors", logo="/img/logo-seniors-128.png",
       accent="#3fa7e0", accent_text="#1f77ae", btn_text="#0b2540",
       en=dict(suffix="for Seniors", tag="One-on-one, patient, no jargon",
               text="Friendly AI and technology lessons for seniors, at home or online.",
               btn="Visit the Seniors site →", url="https://seniors.aiwithrobert.com/?lang=en",
               alt="AI with Robert for Seniors logo", aria="Go to AI with Robert for Seniors"),
       fr=dict(suffix="pour aînés", tag="Individuel, patient, sans jargon",
               text="Cours conviviaux d’IA et de technologie pour aînés, à domicile ou en ligne.",
               btn="Visiter le site pour aînés →", url="https://seniors.aiwithrobert.com/fr/",
               alt="Logo AI with Robert pour aînés", aria="Aller à AI with Robert pour aînés")),
  dict(id="business", logo="/img/logo-business-128.png",
       accent="#c9a227", accent_text="#8a6d0b", btn_text="#11304c",
       en=dict(suffix="for Business", tag="Get more from the AI you already pay for",
               text="AI consulting, workflow automation and team training for small businesses.",
               btn="Visit the Business site →", soon_btn="Coming soon", early="Interested early?", early_link="Get in touch", url="https://biz.aiwithrobert.com/?lang=en",
               alt="AI with Robert for Business logo", aria="Go to AI with Robert for Business"),
       fr=dict(suffix="pour entreprises", tag="Tirez plus de l’IA que vous payez déjà",
               text="Consultation en IA, automatisation des flux de travail et formation d’équipe pour les petites entreprises.",
               btn="Visiter le site pour entreprises →", soon_btn="Bientôt disponible", early="Intéressé dès maintenant?", early_link="Écrivez-moi", url="https://biz.aiwithrobert.com/fr/",
               alt="Logo AI with Robert pour entreprises", aria="Aller à AI with Robert pour entreprises")),
]

T = {
 "en": dict(path="/", html_lang="en", og_locale="en_CA",
  title="AI with Robert — Practical AI help from a local, trusted professional",
  desc="Practical AI help from Robert Simon, a local, trusted professional in Côte Saint-Luc, Montréal. Choose the area you need help with.",
  main_alt="AI with Robert logo",
  sub="Practical AI help from a local, trusted professional.",
  who="Robert Simon · 25+ years in technology · Côte Saint-Luc, Montréal · English &amp; French",
  choose="Choose the area you need help with",
  foot="Robert Simon · Côte Saint-Luc, Québec", indep="AI with Robert is an independent practice of Robert Simon. It is not affiliated with, sponsored by or endorsed by any employer, including Bell Canada.", contact="Questions? Write to me at", langlabel="Language"),
 "fr": dict(path="/fr/", html_lang="fr-CA", og_locale="fr_CA",
  title="AI with Robert — De l’aide pratique en IA par un professionnel local de confiance",
  desc="De l’aide pratique en IA offerte par Robert Simon, professionnel local de confiance à Côte-Saint-Luc (Montréal). Choisissez le domaine qui vous intéresse.",
  main_alt="Logo AI with Robert",
  sub="De l’aide pratique en IA, offerte par un professionnel local de confiance.",
  who="Robert Simon · plus de 25 ans en technologie · Côte-Saint-Luc (Montréal) · français et anglais",
  choose="Choisissez le domaine qui vous intéresse",
  foot="Robert Simon · Côte-Saint-Luc (Québec)", indep="AI with Robert est une pratique indépendante de Robert Simon. Elle n’est affiliée à aucun employeur, ni commanditée ou approuvée par aucun d’eux, y compris Bell Canada.", contact="Une question? Écrivez-moi à", langlabel="Langue"),
}

CSS = """*{box-sizing:border-box;margin:0}html{-webkit-text-size-adjust:100%}
body{position:relative;overflow-x:hidden;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:#11304c;background:#fff;line-height:1.4}
body:after{content:"";position:absolute;z-index:-1;left:0;right:0;top:0;height:560px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 560' preserveAspectRatio='xMinYMin slice'%3E%3Cdefs%3E%3ClinearGradient id='w' x1='0' y1='0' x2='0' y2='1'%3E%3Cstop offset='0' stop-color='%2356aeaa' stop-opacity='.15'/%3E%3Cstop offset='1' stop-color='%2356aeaa' stop-opacity='0'/%3E%3C/linearGradient%3E%3ClinearGradient id='t' x1='0' y1='0' x2='0' y2='1'%3E%3Cstop offset='0' stop-color='%2356aeaa' stop-opacity='.30'/%3E%3Cstop offset='.8' stop-color='%2356aeaa' stop-opacity='.05'/%3E%3Cstop offset='1' stop-color='%2356aeaa' stop-opacity='0'/%3E%3C/linearGradient%3E%3ClinearGradient id='n' x1='0' y1='0' x2='0' y2='1'%3E%3Cstop offset='0' stop-color='%231f3050' stop-opacity='.10'/%3E%3Cstop offset='.8' stop-color='%231f3050' stop-opacity='.03'/%3E%3Cstop offset='1' stop-color='%231f3050' stop-opacity='0'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='1440' height='560' fill='url%28%23w%29'/%3E%3Cpath fill='url%28%23t%29' d='M1010,0 L1440,0 L1440,260 C1330,190 1130,110 1010,0Z'/%3E%3Cpath fill='url%28%23t%29' fill-opacity='.5' d='M1150,0 L1440,0 L1440,400 C1380,270 1270,130 1150,0Z'/%3E%3Cpath fill='url%28%23n%29' d='M0,0 L300,0 C380,140 250,330 330,560 L0,560Z'/%3E%3Cpath fill='url%28%23t%29' d='M300,0 L316,0 C396,140 266,330 346,560 L330,560 C250,330 380,140 300,0Z'/%3E%3C/svg%3E") left top/cover no-repeat;pointer-events:none}.top{display:flex;justify-content:flex-end;padding:14px 22px}
.lang{display:inline-flex;border:2px solid #cfe3e1;border-radius:10px;overflow:hidden;background:#fff;font-weight:700;font-size:.95rem}
.lang a,.lang span{padding:7px 14px;text-decoration:none;color:#11304c}.lang span{background:#11304c;color:#fff}.lang a:hover{background:#eef2f6}
.hero{text-align:center;padding:3.2rem 22px 5.5rem}
.hero img{width:168px;height:auto}
.wm{font-size:3.1rem;font-weight:800;letter-spacing:-.8px;margin:1.1rem 0 .9rem}
.sub{font-size:1.5rem;font-weight:600;color:#067f78;max-width:640px;margin:0 auto 1.6rem;line-height:1.3}
.who{color:#475569;font-size:1rem;max-width:640px;margin:0 auto}
.areas{max-width:1000px;margin:0 auto;padding:0 22px 1rem;text-align:center}
.areas h1{font-size:1.15rem;font-weight:700;color:#475569;letter-spacing:.3px;margin-bottom:1.6rem;position:relative;padding-top:1.4rem}
.areas h1:before{content:"";position:absolute;top:-3.6rem;left:50%;height:3rem;border-left:3px solid #08a59c}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;text-align:left}
.card{background:#fff;border-radius:22px;padding:28px;box-shadow:0 12px 32px rgba(17,48,76,.12);border-top:8px solid var(--accent);display:flex;flex-direction:column;position:relative;transition:transform .15s,box-shadow .15s}
.card img{width:64px;height:auto}.card h2{font-size:1.35rem;margin:12px 0 4px}.card h2 span{color:var(--accent-text)}
.tag{font-weight:700;margin-bottom:10px;color:var(--accent-text)}.card p{color:#475569;line-height:1.55;margin-bottom:18px}
.btn{display:inline-block;align-self:flex-start;margin-top:auto;padding:14px 26px;border-radius:12px;font-weight:700;text-decoration:none;font-size:1.05rem;background:var(--accent);color:var(--btn-text)}
a.card{text-decoration:none;color:inherit;-webkit-tap-highlight-color:rgba(17,48,76,.08)}a.card:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(17,48,76,.18)}a.card:hover .btn{filter:brightness(.95)}.lang a:focus-visible{outline:3px solid #11304c;outline-offset:2px}a.card:focus-visible{outline:3px solid #11304c;outline-offset:3px}
.card.soon{background:#fbfaf3}.btn.off{background:#e9e4cf;color:#6b5a14;cursor:default;pointer-events:none;border:2px dashed #c9a227}.early{margin-top:auto;font-size:.92rem;color:#475569}.early a{color:#11304c;font-weight:700}.badge{align-self:flex-start;background:#11304c;color:#fff;font-size:.75rem;font-weight:800;letter-spacing:.8px;text-transform:uppercase;border-radius:999px;padding:4px 12px;margin-bottom:10px}
.foot{position:relative;margin-top:110px;background:#1f3050;color:#e6ecf3;text-align:center;padding:1.6rem 20px 2.6rem;font-size:.95rem}.foot:before{content:"";position:absolute;left:0;right:0;top:-79px;height:80px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 80' preserveAspectRatio='none'%3E%3Cpath fill='%2356aeaa' d='M0,34 C380,2 960,-4 1440,60 L1440,80 L0,80Z'/%3E%3Cpath fill='%231f3050' d='M0,48 C380,16 960,10 1440,68 L1440,80 L0,80Z'/%3E%3C/svg%3E") bottom/100% 100% no-repeat}.foot .contact{font-size:1.1rem;margin-bottom:.5rem}.foot .contact a{color:#fff;font-weight:700}.foot .indep{font-size:.78rem;line-height:1.45;color:#9fb0c6;max-width:34rem;margin:.9rem auto 0}.foot .phone{font-size:.8rem;color:#9fb0c6}.foot .phone a{color:#9fb0c6;font-weight:400;white-space:nowrap}
@media(min-width:1300px){body:before{content:"";position:fixed;z-index:-1;left:0;top:0;bottom:0;width:9vw;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100' preserveAspectRatio='none'%3E%3Cpath fill='%2356aeaa' d='M56,0 L66,0 C94,32 56,68 86,100 L72,100 C42,68 80,32 56,0Z'/%3E%3Cpath fill='%231f3050' d='M0,0 L56,0 C80,32 42,68 72,100 L0,100Z'/%3E%3C/svg%3E") left top/100% 100% no-repeat}}
@media(max-width:700px){.hero{padding:2.2rem 22px 4.5rem}.hero img{width:130px}.wm{font-size:2.3rem}.sub{font-size:1.25rem}.grid{grid-template-columns:1fr}}"""

def card(b, lang):
    t = b[lang]
    style = "--accent:%s;--accent-text:%s;--btn-text:%s" % (b["accent"], b["accent_text"], b["btn_text"])
    soon = b.get("soon")
    if soon:
        head = '<section class="card soon" style="%s">\n' % style
        close = "</section>"
    else:
        head = '<a class="card" href="%s" aria-label="%s" style="%s">\n' % (t["url"], t["aria"], style)
        close = "</a>"
    if soon:
        head += '<span class="badge">%s</span>\n' % t["soon_btn"]
        action = '<p class="early">%s <a href="mailto:%s">%s</a></p>' % (t["early"], BIZ_EMAIL, t["early_link"])
    else:
        action = '<span class="btn">%s</span>' % t["btn"]
    return (head +
        '<img src="%s" width="64" height="64" alt="%s">\n'
        '<h2>AI with Robert <span>%s</span></h2>\n'
        '<div class="tag">%s</div>\n'
        '<p>%s</p>\n%s\n%s'
    ) % (b["logo"], t["alt"], t["suffix"], t["tag"], t["text"], action, close)

import json
SEN_ID = "https://seniors.aiwithrobert.com/#business"
BIZ_ID = "https://biz.aiwithrobert.com/#business"

def jsonld(k):
    """Brand-level graph: one Organization (the parent brand), the person behind it,
    the WebSite, and links to the two service entities that live on their own sites.
    No address, ratings or social profiles are asserted that are not on the page."""
    t = T[k]; url = BASE + t["path"]
    org, person = BASE + "/#organization", "https://www.imetrobert.com/#robert-simon"  # master Person id, defined on imetrobert.com
    graph = [
        {"@type": "Organization", "@id": org, "name": "AI with Robert", "url": BASE + "/",
         "logo": BASE + "/icon-512.png", "email": EMAIL, "telephone": "+1-" + PHONE,
         "description": "Practical AI help from Robert Simon in Greater Montr\u00e9al: AI tutoring for seniors and AI consulting for small businesses.",
         "founder": {"@id": person},
         "areaServed": {"@type": "AdministrativeArea", "name": "Greater Montr\u00e9al"},
         "knowsLanguage": ["en", "fr"],
         "subOrganization": [{"@id": SEN_ID}, {"@id": BIZ_ID}]},
        {"@type": "Person", "@id": person, "name": "Robert Simon", "url": "https://www.imetrobert.com/",
         "worksFor": {"@id": org}},
        {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "AI with Robert",
         "publisher": {"@id": org}, "inLanguage": ["en-CA", "fr-CA"]},
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": t["title"],
         "isPartOf": {"@id": BASE + "/#website"}, "about": {"@id": org}, "inLanguage": t["html_lang"]},
    ]
    return '<script type="application/ld+json">\n' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1) + "\n</script>\n"

def page(k):
    t = T[k]; url = BASE + t["path"]; en, fr = BASE + "/", BASE + "/fr/"
    if k == "en":
        sw = '<span aria-current="true">EN</span><a href="/fr/" hreflang="fr-CA" lang="fr">FR</a>'
    else:
        sw = '<a href="/" hreflang="en-CA" lang="en">EN</a><span aria-current="true">FR</span>'
    cards = "\n".join(card(b, k) for b in BRANDS)
    tel = "tel:+1" + PHONE.replace("-", "")
    robots = '<meta name="robots" content="noindex, follow">\n' if NOINDEX else ""
    return f"""<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
{robots}<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-CA" href="{en}">
<link rel="alternate" hreflang="fr-CA" href="{fr}">
<link rel="alternate" hreflang="x-default" href="{en}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AI with Robert">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{t["og_locale"]}">
<meta property="og:image" content="{BASE}/og-share-1200x630.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#08a59c">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<style>{CSS}</style>
{jsonld(k)}</head>
<body>
<div class="top"><nav class="lang" aria-label="{t["langlabel"]}">{sw}</nav></div>
<header class="hero">
<img src="/img/logo-main-256.png" width="168" height="168" alt="{t["main_alt"]}">
<div class="wm">AI with Robert</div>
<p class="sub">{t["sub"]}</p>
<p class="who">{t["who"]}</p>
</header>
<main class="areas">
<h1>{t["choose"]}</h1>
<div class="grid">
{cards}
</div>
</main>
<footer class="foot">
<p class="contact">{t["contact"]} <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>{t["foot"]}</p>
<p class="phone"><a href="{tel}">{PHONE}</a></p>
<p class="indep">{t["indep"]}</p>
</footer>
</body>
</html>
"""

for k, p in (("en", "index.html"), ("fr", "fr/index.html")):
    os.makedirs(os.path.dirname(os.path.join(ROOT, p)) or ROOT, exist_ok=True)
    open(os.path.join(ROOT, p), "w", encoding="utf-8").write(page(k))
print("built index.html and fr/index.html")
