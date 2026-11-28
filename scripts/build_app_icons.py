#!/usr/bin/env python3
"""Builds the icon set for Robert's personal apps (original artwork, one colour + one symbol per app).
Run from the repo root:  python3 scripts/build_app_icons.py [outdir]   (needs rsvg-convert; default outdir img/app-icons)
Writes <app>/favicon.svg, favicon-32.png, apple-touch-icon.png (180), icon-512.png and a preview sheet icons-sheet.png.
To change a colour or symbol edit APPS below and re-run; then copy the files into the app repo (see docs/APPS.md "App icons")."""
import os, subprocess, sys
W = '#ffffff'
def svg(bg, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="112" fill="{bg}"/>{body}</svg>'
APPS = {
 # ETF tracker: rising bars with a trend arrow
 'etf': svg('#0F7B4F', f'<g fill="{W}"><rect x="112" y="300" width="64" height="110" rx="14" opacity=".85"/><rect x="224" y="236" width="64" height="174" rx="14" opacity=".85"/><rect x="336" y="160" width="64" height="250" rx="14" opacity=".85"/></g><g fill="none" stroke="{W}" stroke-width="24" stroke-linecap="round" stroke-linejoin="round"><polyline points="104,236 200,176 280,204 398,104"/><polyline points="334,100 398,104 394,168"/></g>'),
 # Job Match: briefcase with a check mark
 'jobs': svg('#4F46E5', f'<path d="M196 196v-32a26 26 0 0 1 26-26h68a26 26 0 0 1 26 26v32" fill="none" stroke="{W}" stroke-width="26" stroke-linecap="round"/><rect x="96" y="190" width="320" height="220" rx="40" fill="{W}"/><polyline points="184,300 236,352 336,248" fill="none" stroke="#4F46E5" stroke-width="28" stroke-linecap="round" stroke-linejoin="round"/>'),
 # Claims tracker: receipt with a medical cross
 'claims': svg('#0E7C86', f'<path d="M136 96h240v320l-40-30-40 30-40-30-40 30-40-30-40 30z" fill="{W}"/><g fill="#0E7C86"><rect x="238" y="156" width="36" height="104" rx="9"/><rect x="204" y="190" width="104" height="36" rx="9"/></g><g stroke="#0E7C86" stroke-width="16" stroke-linecap="round" opacity=".75"><line x1="190" y1="300" x2="322" y2="300"/><line x1="190" y1="338" x2="280" y2="338"/></g>'),
 # Marketplace generator: shopping bag with a check (blue gradient; the same glyph is the in-app logo in facebook-marketplace-generator index.html)
 'market': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2D88FF"/><stop offset="1" stop-color="#0A5BD0"/></linearGradient></defs><rect width="512" height="512" rx="112" fill="url(#g)"/><g transform="translate(96 96) scale(10)" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 11h18l-1.4 14.2a1.5 1.5 0 0 1-1.5 1.3H9.9a1.5 1.5 0 0 1-1.5-1.3z"/><path d="M12 11V9a4 4 0 0 1 8 0v2"/><path d="M12.5 18.5l2.5 2.5 4.5-5"/></g></svg>',
 # Personal retirement planner: sun rising over the horizon
 'retire': svg('#1E3A5F', f'<path d="M156 316a100 100 0 0 1 200 0z" fill="#F5B83D"/><g stroke="#F5B83D" stroke-width="22" stroke-linecap="round"><line x1="256" y1="150" x2="256" y2="118"/><line x1="146" y1="196" x2="124" y2="172"/><line x1="366" y1="196" x2="388" y2="172"/><line x1="104" y1="270" x2="72" y2="264"/><line x1="408" y1="270" x2="440" y2="264"/></g><g stroke="{W}" stroke-width="22" stroke-linecap="round"><line x1="88" y1="346" x2="424" y2="346"/><line x1="144" y1="392" x2="368" y2="392" opacity=".6"/></g>'),
 # Invoicing app: invoice page with a paid check (brand navy and gold)
 'invoices': svg('#11304C', f'<path d="M140 76h172l64 64v292a28 28 0 0 1-28 28H140a28 28 0 0 1-28-28V104a28 28 0 0 1 28-28z" fill="{W}"/><path d="M312 76v64h64z" fill="#C9A227"/><g stroke="#11304C" stroke-width="18" stroke-linecap="round" opacity=".35"><line x1="160" y1="196" x2="300" y2="196"/><line x1="160" y1="244" x2="340" y2="244"/></g><circle cx="320" cy="354" r="76" fill="#C9A227"/><polyline points="284,356 313,386 364,326" fill="none" stroke="{W}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>'),
 # Access page: shield with a keyhole
 'access': svg('#1E293B', f'<path d="M256 82l150 54v110c0 98-62 160-150 196-88-36-150-98-150-196V136z" fill="{W}"/><circle cx="256" cy="232" r="42" fill="#1E293B"/><path d="M236 252h40l16 90h-72z" fill="#1E293B"/>'),
 # Quebec planner: fleurdelise (blue, white cross, fleurs-de-lis) with a sunrise badge in the centre
 'retireqc': svg('#003DA5', f'<defs><g id="fl"><path d="M50 6C38 22 38 44 50 62 62 44 62 22 50 6z"/><path d="M42 60C28 64 10 60 10 44 10 33 24 27 33 36 23 38 23 49 31 51 35 52 39 51 44 47z"/><path d="M58 60C72 64 90 60 90 44 90 33 76 27 67 36 77 38 77 49 69 51 65 52 61 51 56 47z"/><rect x="32" y="62" width="36" height="9" rx="3"/><path d="M42 72h16l4 18H38z"/></g></defs><clipPath id="c"><rect width="512" height="512" rx="112"/></clipPath><g clip-path="url(#c)"><rect x="221" width="70" height="512" fill="{W}"/><rect y="221" width="512" height="70" fill="{W}"/></g><g fill="{W}"><use href="#fl" transform="translate(48 48) scale(1.5)"/><use href="#fl" transform="translate(314 48) scale(1.5)"/><use href="#fl" transform="translate(48 314) scale(1.5)"/><use href="#fl" transform="translate(314 314) scale(1.5)"/></g><circle cx="256" cy="256" r="92" fill="#003DA5" stroke="{W}" stroke-width="14"/><path d="M196 280a60 60 0 0 1 120 0z" fill="#F5B83D"/><g stroke="#F5B83D" stroke-width="12" stroke-linecap="round"><line x1="256" y1="190" x2="256" y2="170"/><line x1="206" y1="212" x2="192" y2="198"/><line x1="306" y1="212" x2="320" y2="198"/></g><line x1="190" y1="296" x2="322" y2="296" stroke="{W}" stroke-width="12" stroke-linecap="round"/>'),
 # Ontario planner: red ensign (Union Jack canton on red) with a sunrise
 'retireon': svg('#BF0A30', f'<defs><clipPath id="r"><rect width="512" height="512" rx="112"/></clipPath><clipPath id="k"><rect width="290" height="250"/></clipPath></defs><g clip-path="url(#r)"><rect width="512" height="512" fill="#BF0A30"/><g clip-path="url(#k)"><rect width="290" height="250" fill="#012169"/><path d="M0 0L290 250M290 0L0 250" stroke="{W}" stroke-width="40"/><path d="M0 0L290 250M290 0L0 250" stroke="#BF0A30" stroke-width="14"/><path d="M145 0V250M0 125H290" stroke="{W}" stroke-width="70"/><path d="M145 0V250M0 125H290" stroke="#BF0A30" stroke-width="40"/></g></g><path d="M290 374a82 82 0 0 1 164 0z" fill="#F5B83D"/><g stroke="#F5B83D" stroke-width="16" stroke-linecap="round"><line x1="372" y1="262" x2="372" y2="236"/><line x1="314" y1="286" x2="298" y2="266"/><line x1="430" y1="286" x2="446" y2="266"/></g><g stroke="{W}" stroke-width="18" stroke-linecap="round"><line x1="270" y1="394" x2="474" y2="394"/><line x1="320" y1="436" x2="424" y2="436" opacity=".6"/></g>'),
}
out = sys.argv[1] if len(sys.argv) > 1 else 'img/app-icons'
def png(svgpath, pngpath, size):
    subprocess.run(['rsvg-convert', '-w', str(size), '-h', str(size), svgpath, '-o', pngpath], check=True)
for name, s in APPS.items():
    d = os.path.join(out, name); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, 'favicon.svg'); open(p, 'w').write(s)
    png(p, os.path.join(d, 'favicon-32.png'), 32); png(p, os.path.join(d, 'apple-touch-icon.png'), 180); png(p, os.path.join(d, 'icon-512.png'), 512)
names = list(APPS)
# preview sheet (what a bookmark page would show)
cells = ''.join(f'<g transform="translate({20+i*180},20)"><image href="{os.path.abspath(os.path.join(out,n,"icon-512.png"))}" width="160" height="160"/><text x="80" y="188" font-family="Arial" font-size="18" text-anchor="middle" fill="#222">{n}</text></g>' for i, n in enumerate(APPS))
sheet = os.path.join(out, 'icons-sheet.svg'); open(sheet, 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{40+len(APPS)*180}" height="220"><rect width="100%" height="100%" fill="#f4f5f7"/>{cells}</svg>')
subprocess.run(['rsvg-convert', sheet, '-o', os.path.join(out, 'icons-sheet.png')], check=True); os.remove(sheet)
print('OK: icons written to', out)
