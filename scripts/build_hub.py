#!/usr/bin/env python3
"""Builds the hub homepage: index.html (EN) and fr/index.html (FR). Edit copy here, then run."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://aiwithrobert.com"
S = "https://seniors.aiwithrobert.com/"
B = "https://biz.aiwithrobert.com/"
PHONE = "514-250-8491"

T = {
 "en": dict(
  lang="en", path="/", html_lang="en",
  title="AI with Robert — Practical AI for real people and real businesses",
  desc="Practical AI training and strategy from Robert Simon in Côte Saint-Luc, Montréal. AI with Robert for Seniors and AI with Robert for Business. English and French.",
  tagline="Practical AI for real people and real businesses",
  intro="Hands-on training and strategy from Robert Simon — 25+ years in technology, based in Côte Saint-Luc, Montréal. In English and French.",
  s_name="for Seniors", s_tag="One-on-one, patient, no jargon",
  s_p="Friendly AI and technology lessons for seniors, at home or online.", s_btn="Visit the Seniors site →",
  s_url=S, s_alt="AI with Robert for Seniors logo",
  b_name="for Business", b_tag="Real ROI, used safely",
  b_p="AI strategy, team training and workflow automation for small and mid-sized businesses.", b_btn="Visit the Business site →",
  b_url=B, b_alt="AI with Robert for Business logo",
  main_alt="AI with Robert logo", path_label="Choose your path",
  foot="Robert Simon · Côte Saint-Luc, Québec",
  langlabel="Language", s_aria="Go to AI with Robert for Seniors", b_aria="Go to AI with Robert for Business",
  og_locale="en_CA"),
 "fr": dict(
  lang="fr", path="/fr/", html_lang="fr-CA",
  title="AI with Robert — L’IA pratique pour de vraies personnes et de vraies entreprises",
  desc="Formation et stratégie en IA pratique avec Robert Simon, à Côte-Saint-Luc (Montréal). AI with Robert pour aînés et AI with Robert pour entreprises. En français et en anglais.",
  tagline="L’IA pratique pour de vraies personnes et de vraies entreprises",
  intro="Formation pratique et stratégie avec Robert Simon — plus de 25 ans en technologie, à Côte-Saint-Luc (Montréal). En français et en anglais.",
  s_name="pour aînés", s_tag="Individuel, patient, sans jargon",
  s_p="Cours conviviaux d’IA et de technologie pour aînés, à domicile ou en ligne.", s_btn="Visiter le site pour aînés →",
  s_url=S + "fr/", s_alt="Logo AI with Robert pour aînés",
  b_name="pour entreprises", b_tag="Un vrai rendement, en toute sécurité",
  b_p="Stratégie d’IA, formation d’équipes et automatisation des processus pour les petites et moyennes entreprises.", b_btn="Visiter le site pour entreprises →",
  b_url=B + "fr/", b_alt="Logo AI with Robert pour entreprises",
  main_alt="Logo AI with Robert", path_label="Choisissez votre voie",
  foot="Robert Simon · Côte-Saint-Luc (Québec)",
  langlabel="Langue", s_aria="Aller à AI with Robert pour aînés", b_aria="Aller à AI with Robert pour entreprises",
  og_locale="fr_CA"),
}

CSS = """*{box-sizing:border-box;margin:0}html{-webkit-text-size-adjust:100%}
body{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:#11304c;background:#fff;line-height:1.4}
.top{display:flex;justify-content:flex-end;padding:14px 22px;background:#eefaf9}
.lang{display:inline-flex;border:2px solid #cfe3e1;border-radius:10px;overflow:hidden;background:#fff;font-weight:700;font-size:.95rem}
.lang a,.lang span{padding:7px 14px;text-decoration:none;color:#11304c}.lang span{background:#11304c;color:#fff}.lang a:hover{background:#eefaf9}
.hero{text-align:center;padding:4px 22px 0;background:linear-gradient(180deg,#eefaf9,#fff)}
.hero img{width:150px;height:auto}
.wm{font-size:2.6rem;font-weight:800;letter-spacing:-.5px;margin:6px 0 2px}
h1{font-size:1.5rem;font-weight:600;color:#067f78;margin:0 auto 10px;max-width:720px}
.hero p{color:#475569;font-size:1.1rem;max-width:620px;margin:0 auto}
.branch{position:relative;max-width:960px;margin:0 auto;height:56px}
.branch:before{content:"";position:absolute;left:50%;top:0;height:28px;border-left:3px solid #08a59c}
.branch:after{content:"";position:absolute;left:25%;right:25%;top:28px;height:28px;border:3px solid #08a59c;border-bottom:0;border-radius:14px 14px 0 0}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:24px;max-width:960px;margin:0 auto 22px;padding:0 22px}
.card{background:#fff;border-radius:22px;padding:28px;box-shadow:0 12px 32px rgba(17,48,76,.12);border-top:8px solid}
.card img{width:64px;height:auto}.card h2{font-size:1.35rem;margin:12px 0 4px}
.tag{font-weight:700;margin-bottom:10px}.card p{color:#475569;line-height:1.55;margin-bottom:18px}
.btn{display:inline-block;padding:14px 26px;border-radius:12px;font-weight:700;text-decoration:none;font-size:1.05rem}
.s{border-color:#3fa7e0}.s h2 span,.s .tag{color:#1f77ae}.s .btn{background:#3fa7e0;color:#0b2540}
.b{border-color:#c9a227}.b h2 span,.b .tag{color:#8a6d0b}.b .btn{background:#c9a227;color:#11304c}
.btn:hover{filter:brightness(.95)}.btn:focus-visible,.lang a:focus-visible{outline:3px solid #11304c;outline-offset:2px}
.foot{text-align:center;color:#475569;padding:6px 20px 26px;font-size:.95rem}.foot a{color:#11304c;font-weight:600;white-space:nowrap}
@media(max-width:700px){.cards{grid-template-columns:1fr}.branch{height:34px}.branch:after{display:none}.branch:before{height:34px}.hero img{width:120px}.wm{font-size:2.1rem}h1{font-size:1.35rem}}"""

def page(k):
    t = T[k]; url = BASE + t["path"]
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "AI with Robert",
       "inLanguage": ["en-CA", "fr-CA"], "publisher": {"@id": BASE + "/#org"}},
      {"@type": "Organization", "@id": BASE + "/#org", "name": "AI with Robert", "url": BASE + "/",
       "logo": BASE + "/img/logo-main-512.png", "telephone": "+1-" + PHONE,
       "founder": {"@id": BASE + "/#robert"},
       "address": {"@type": "PostalAddress", "addressLocality": "Côte Saint-Luc", "addressRegion": "QC", "addressCountry": "CA"},
       "areaServed": {"@type": "City", "name": "Montréal"},
       "subOrganization": [
         {"@type": "LocalBusiness", "name": "AI with Robert for Seniors", "url": S},
         {"@type": "ProfessionalService", "name": "AI with Robert for Business", "url": B}]},
      {"@type": "Person", "@id": BASE + "/#robert", "name": "Robert Simon",
       "jobTitle": "AI trainer and digital transformation consultant", "worksFor": {"@id": BASE + "/#org"},
       "knowsLanguage": ["en", "fr"]}]}
    en, fr = BASE + "/", BASE + "/fr/"
    if k == "en":
        sw = '<span aria-current="true">EN</span><a href="/fr/" hreflang="fr-CA" lang="fr">FR</a>'
    else:
        sw = '<a href="/" hreflang="en-CA" lang="en">EN</a><span aria-current="true">FR</span>'
    return f'''<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<link rel="canonical" href="{url}">
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
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
<style>{CSS}</style>
</head>
<body>
<div class="top"><nav class="lang" aria-label="{t["langlabel"]}">{sw}</nav></div>
<header class="hero">
<img src="/img/logo-main-256.png" width="150" height="150" alt="{t["main_alt"]}">
<div class="wm">AI with Robert</div>
<h1>{t["tagline"]}</h1>
<p>{t["intro"]}</p>
</header>
<div class="branch" role="presentation"></div>
<main class="cards" aria-label="{t["path_label"]}">
<section class="card s">
<img src="/img/logo-seniors-128.png" width="64" height="64" alt="{t["s_alt"]}">
<h2>AI with Robert <span>{t["s_name"]}</span></h2>
<div class="tag">{t["s_tag"]}</div>
<p>{t["s_p"]}</p>
<a class="btn" href="{t["s_url"]}" aria-label="{t["s_aria"]}">{t["s_btn"]}</a>
</section>
<section class="card b">
<img src="/img/logo-business-128.png" width="64" height="64" alt="{t["b_alt"]}">
<h2>AI with Robert <span>{t["b_name"]}</span></h2>
<div class="tag">{t["b_tag"]}</div>
<p>{t["b_p"]}</p>
<a class="btn" href="{t["b_url"]}" aria-label="{t["b_aria"]}">{t["b_btn"]}</a>
</section>
</main>
<footer class="foot">{t["foot"]} · <a href="tel:+1{PHONE.replace("-","")}">{PHONE}</a></footer>
</body>
</html>
'''

for k, p in (("en", "index.html"), ("fr", "fr/index.html")):
    os.makedirs(os.path.dirname(os.path.join(ROOT, p)) or ROOT, exist_ok=True)
    open(os.path.join(ROOT, p), "w", encoding="utf-8").write(page(k))
print("built index.html and fr/index.html")
