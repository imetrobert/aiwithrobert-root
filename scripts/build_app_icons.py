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
 # Marketplace generator: price tag
 'market': svg('#EA580C', f'<path d="M122 232 232 122H400V290L290 400Q260 430 230 400L122 292Q92 262 122 232Z" fill="{W}"/><circle cx="338" cy="182" r="30" fill="#EA580C"/>'),
 # Personal retirement planner: sun rising over the horizon
 'retire': svg('#1E3A5F', f'<path d="M156 316a100 100 0 0 1 200 0z" fill="#F5B83D"/><g stroke="#F5B83D" stroke-width="22" stroke-linecap="round"><line x1="256" y1="150" x2="256" y2="118"/><line x1="146" y1="196" x2="124" y2="172"/><line x1="366" y1="196" x2="388" y2="172"/><line x1="104" y1="270" x2="72" y2="264"/><line x1="408" y1="270" x2="440" y2="264"/></g><g stroke="{W}" stroke-width="22" stroke-linecap="round"><line x1="88" y1="346" x2="424" y2="346"/><line x1="144" y1="392" x2="368" y2="392" opacity=".6"/></g>'),
}
out = sys.argv[1] if len(sys.argv) > 1 else 'img/app-icons'
def png(svgpath, pngpath, size):
    subprocess.run(['rsvg-convert', '-w', str(size), '-h', str(size), svgpath, '-o', pngpath], check=True)
for name, s in APPS.items():
    d = os.path.join(out, name); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, 'favicon.svg'); open(p, 'w').write(s)
    png(p, os.path.join(d, 'favicon-32.png'), 32); png(p, os.path.join(d, 'apple-touch-icon.png'), 180); png(p, os.path.join(d, 'icon-512.png'), 512)
# preview sheet (what a bookmark page would show)
cells = ''.join(f'<g transform="translate({20+i*180},20)"><image href="{os.path.abspath(os.path.join(out,n,"icon-512.png"))}" width="160" height="160"/><text x="80" y="188" font-family="Arial" font-size="18" text-anchor="middle" fill="#222">{n}</text></g>' for i, n in enumerate(APPS))
sheet = os.path.join(out, 'icons-sheet.svg'); open(sheet, 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{40+len(APPS)*180}" height="220"><rect width="100%" height="100%" fill="#f4f5f7"/>{cells}</svg>')
subprocess.run(['rsvg-convert', sheet, '-o', os.path.join(out, 'icons-sheet.png')], check=True); os.remove(sheet)
print('OK: icons written to', out)
