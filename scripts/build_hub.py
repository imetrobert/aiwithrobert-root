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

# Launch switches: while NOINDEX is True the page asks search engines not to list it.
# Flip to False (and re-add sitemap.xml) when you are ready to be found in search.
NOINDEX = True

# -- Sub-brands (add new ones here) -----------------------------------------
BRANDS = [
  dict(id="seniors", logo="/img/logo-seniors-128.png",
       accent="#3fa7e0", accent_text="#1f77ae", btn_text="#0b2540",
       en=dict(suffix="for Seniors", tag="One-on-one, patient, no jargon",
               text="Friendly AI and technology lessons for seniors, at home or online.",
               btn="Visit the Seniors site →", url="https://seniors.aiwithrobert.com/",
               alt="AI with Robert for Seniors logo", aria="Go to AI with Robert for Seniors"),
       fr=dict(suffix="pour aînés", tag="Individuel, patient, sans jargon",
               text="Cours conviviaux d’IA et de technologie pour aînés, à domicile ou en ligne.",
               btn="Visiter le site pour aînés →", url="https://seniors.aiwithrobert.com/fr/",
               alt="Logo AI with Robert pour aînés", aria="Aller à AI with Robert pour aînés")),
  dict(id="business", soon=True, logo="/img/logo-business-128.png",
       accent="#c9a227", accent_text="#8a6d0b", btn_text="#11304c",
       en=dict(suffix="for Business", tag="Get more from the AI you already pay for",
               text="AI consulting, workflow automation and team training for small businesses.",
               btn="Visit the Business site →", soon_btn="Coming soon", early="Interested early?", early_link="Get in touch", url="https://biz.aiwithrobert.com/",
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
  more="More areas will be added here as they launch.",
  foot="Robert Simon · Côte Saint-Luc, Québec", contact="Questions? Write to me at", langlabel="Language"),
 "fr": dict(path="/fr/", html_lang="fr-CA", og_locale="fr_CA",
  title="AI with Robert — De l’aide pratique en IA par un professionnel local de confiance",
  desc="De l’aide pratique en IA offerte par Robert Simon, professionnel local de confiance à Côte-Saint-Luc (Montréal). Choisissez le domaine qui vous intéresse.",
  main_alt="Logo AI with Robert",
  sub="De l’aide pratique en IA, offerte par un professionnel local de confiance.",
  who="Robert Simon · plus de 25 ans en technologie · Côte-Saint-Luc (Montréal) · français et anglais",
  choose="Choisissez le domaine qui vous intéresse",
  more="D’autres domaines s’ajouteront ici au fil de leur lancement.",
  foot="Robert Simon · Côte-Saint-Luc (Québec)", contact="Une question? Écrivez-moi à", langlabel="Langue"),
}

CSS = """*{box-sizing:border-box;margin:0}html{-webkit-text-size-adjust:100%}
body{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:#11304c;background:#fff;line-height:1.4}
.top{display:flex;justify-content:flex-end;padding:14px 22px;background:#eefaf9}
.lang{display:inline-flex;border:2px solid #cfe3e1;border-radius:10px;overflow:hidden;background:#fff;font-weight:700;font-size:.95rem}
.lang a,.lang span{padding:7px 14px;text-decoration:none;color:#11304c}.lang span{background:#11304c;color:#fff}.lang a:hover{background:#eefaf9}
.hero{text-align:center;padding:3.2rem 22px 5.5rem;background:linear-gradient(180deg,#eefaf9 0%,#fff 100%)}
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
.btn::after{content:"";position:absolute;inset:0;border-radius:22px}.card:has(.btn:hover){transform:translateY(-3px);box-shadow:0 16px 36px rgba(17,48,76,.18)}.btn:hover{filter:brightness(.95)}.btn:focus-visible,.lang a:focus-visible{outline:3px solid #11304c;outline-offset:2px}.btn:focus-visible::after{outline:3px solid #11304c;outline-offset:2px}
.card.soon{background:#fbfaf3}.btn.off{background:#e9e4cf;color:#6b5a14;cursor:default;pointer-events:none;border:2px dashed #c9a227}.early{margin-top:auto;font-size:.92rem;color:#475569}.early a{color:#11304c;font-weight:700}.badge{align-self:flex-start;background:#11304c;color:#fff;font-size:.75rem;font-weight:800;letter-spacing:.8px;text-transform:uppercase;border-radius:999px;padding:4px 12px;margin-bottom:10px}
.more{color:#64748b;font-size:.95rem;margin:2rem 0 0;text-align:center}
.foot{text-align:center;color:#475569;padding:2.4rem 20px 2.6rem;font-size:.95rem}.foot .contact{font-size:1.1rem;margin-bottom:.5rem}.foot .contact a{color:#11304c;font-weight:700}.foot .phone{font-size:.8rem;color:#94a3b8}.foot .phone a{color:#94a3b8;font-weight:400;white-space:nowrap}
@media(max-width:700px){.hero{padding:2.2rem 22px 4.5rem}.hero img{width:130px}.wm{font-size:2.3rem}.sub{font-size:1.25rem}.grid{grid-template-columns:1fr}}"""

def card(b, lang):
    t = b[lang]
    style = "--accent:%s;--accent-text:%s;--btn-text:%s" % (b["accent"], b["accent_text"], b["btn_text"])
    soon = b.get("soon")
    head = ('<section class="card%s" style="%s">\n' % (" soon" if soon else "", style))
    if soon:
        head += '<span class="badge">%s</span>\n' % t["soon_btn"]
        action = '<p class="early">%s <a href="mailto:%s">%s</a></p>' % (t["early"], EMAIL, t["early_link"])
    else:
        action = '<a class="btn" href="%s" aria-label="%s">%s</a>' % (t["url"], t["aria"], t["btn"])
    return (head +
        '<img src="%s" width="64" height="64" alt="%s">\n'
        '<h2>AI with Robert <span>%s</span></h2>\n'
        '<div class="tag">%s</div>\n'
        '<p>%s</p>\n%s\n</section>'
    ) % (b["logo"], t["alt"], t["suffix"], t["tag"], t["text"], action)

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
</head>
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
<p class="more">{t["more"]}</p>
</main>
<footer class="foot">
<p class="contact">{t["contact"]} <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>{t["foot"]}</p>
<p class="phone"><a href="{tel}">{PHONE}</a></p>
</footer>
</body>
</html>
"""

for k, p in (("en", "index.html"), ("fr", "fr/index.html")):
    os.makedirs(os.path.dirname(os.path.join(ROOT, p)) or ROOT, exist_ok=True)
    open(os.path.join(ROOT, p), "w", encoding="utf-8").write(page(k))
print("built index.html and fr/index.html")
