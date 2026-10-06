#!/usr/bin/env python3
"""Bygger fristaende HTML-sidor for NNK-granskning 2026.

Anvander samma designtokens som kontrollrummet sa att alla sidor
ser ut som en enda produkt. Ingen extern CSS, inga externa skript.
"""
import re
import sys
import pathlib
import markdown

TOKENS = """
:root{
  color-scheme:light;
  --surface-1:#fcfcfb; --plane:#f9f9f7;
  --ink-1:#0b0b0b; --ink-2:#52514e; --ink-3:#898781;
  --grid:#e1e0d9; --axis:#c3c2b7; --ring:rgba(11,11,11,0.10);
  --p-A:#2a78d6; --p-B:#eb6834; --p-C:#1baf7a; --p-D:#eda100;
  --good:#0ca30c; --idag:#d03b3b; --skugga:rgba(0,0,0,.13);
}
@media(prefers-color-scheme:dark){:root:where(:not([data-theme="light"])){
  color-scheme:dark;
  --surface-1:#1a1a19; --plane:#0d0d0d;
  --ink-1:#fff; --ink-2:#c3c2b7; --ink-3:#898781;
  --grid:#2c2c2a; --axis:#383835; --ring:rgba(255,255,255,0.10);
  --p-A:#3987e5; --p-B:#d95926; --p-C:#199e70; --p-D:#c98500;
  --good:#0ca30c; --idag:#d03b3b; --skugga:rgba(0,0,0,.5);
}}
:root[data-theme="dark"]{
  color-scheme:dark;
  --surface-1:#1a1a19; --plane:#0d0d0d;
  --ink-1:#fff; --ink-2:#c3c2b7; --ink-3:#898781;
  --grid:#2c2c2a; --axis:#383835; --ring:rgba(255,255,255,0.10);
  --p-A:#3987e5; --p-B:#d95926; --p-C:#199e70; --p-D:#c98500;
  --good:#0ca30c; --idag:#d03b3b; --skugga:rgba(0,0,0,.5);
}
"""

BAS = """
*{box-sizing:border-box}
body{margin:0;background:var(--plane);color:var(--ink-1);
 font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:15px;line-height:1.6}
.wrap{max-width:820px;margin:0 auto;padding:28px 20px 90px}
a{color:var(--p-A);text-decoration:none}
a:hover{text-decoration:underline}
.topbar{display:flex;justify-content:space-between;align-items:center;gap:16px;
 flex-wrap:wrap;margin-bottom:26px;padding-bottom:14px;border-bottom:1px solid var(--grid)}
.crumb{font-size:12.5px;color:var(--ink-3)}
.crumb a{color:var(--ink-2)}
button{font:inherit;font-size:13px;padding:5px 12px;border-radius:8px;
 border:1px solid var(--ring);background:var(--surface-1);color:var(--ink-2);cursor:pointer}
button:hover{color:var(--ink-1)}
"""

TEMA_JS = """
(function(){
  var b=document.getElementById('themeBtn');
  if(!b)return;
  var r=document.documentElement;
  function mork(){
    var t=r.getAttribute('data-theme');
    if(t)return t==='dark';
    return window.matchMedia('(prefers-color-scheme:dark)').matches;
  }
  function rita(){b.textContent=mork()?'Ljust':'Mörkt';}
  b.addEventListener('click',function(){
    r.setAttribute('data-theme',mork()?'light':'dark');rita();
  });
  rita();
})();
"""

DOK_CSS = """
h1{font-size:26px;font-weight:650;margin:0 0 6px;letter-spacing:-.01em;line-height:1.25}
h2{font-size:19px;font-weight:620;margin:38px 0 10px;letter-spacing:-.005em;
 padding-bottom:6px;border-bottom:1px solid var(--grid)}
h3{font-size:16px;font-weight:620;margin:30px 0 8px;padding-top:4px}
h4,h5,h6{font-size:14.5px;font-weight:620;margin:20px 0 6px;color:var(--ink-2)}
p{margin:0 0 14px;max-width:74ch}
ul,ol{margin:0 0 14px;padding-left:22px;max-width:74ch}
li{margin:4px 0}
hr{border:0;border-top:1px solid var(--grid);margin:32px 0}
blockquote{margin:0 0 14px;padding:2px 0 2px 16px;border-left:3px solid var(--p-D);color:var(--ink-2)}
code{font-family:ui-monospace,"Cascadia Code",Consolas,monospace;font-size:13px;
 background:var(--surface-1);border:1px solid var(--ring);border-radius:5px;padding:1px 5px}
pre{background:var(--surface-1);border:1px solid var(--ring);border-radius:10px;
 padding:14px 16px;overflow-x:auto;margin:0 0 16px}
pre code{background:none;border:0;padding:0;font-size:12.5px}
table{border-collapse:collapse;width:100%;font-size:13.5px;margin:0 0 18px;
 background:var(--surface-1);border:1px solid var(--ring);border-radius:10px;overflow:hidden}
.tabell{overflow-x:auto;margin:0 0 18px;background:var(--surface-1);border:1px solid var(--ring);border-radius:10px}
.tabell table{margin:0;border:0;border-radius:0}
td[style*="right"],th[style*="right"]{font-variant-numeric:tabular-nums;white-space:nowrap}
td code{white-space:normal;word-break:break-word}
th,td{padding:8px 12px;text-align:left;border-bottom:1px solid var(--grid);vertical-align:top}
th{font-weight:620;font-size:12.5px;color:var(--ink-2);background:var(--plane)}
tr:last-child td{border-bottom:0}
.toc{background:var(--surface-1);border:1px solid var(--ring);border-radius:12px;
 padding:16px 20px;margin:0 0 30px}
.toc .t{font-size:12px;font-weight:620;color:var(--ink-3);text-transform:uppercase;
 letter-spacing:.06em;margin-bottom:8px}
.toc ul{margin:0;padding-left:18px;font-size:13.5px}
.toc ul ul{padding-left:16px;font-size:13px}
.toc li{margin:2px 0}
"""

# Flikar (tabbar) for langa sidor med manga top-level h2-avsnitt. Rent
# tillagg - paverkar bara sidor som byggs med flikar=True. Om JS ar
# avstangt visar CSS:en ingenting extra fel: .tabpane har ingen display
# satt via CSS (bara JS togglar den), sa allt forblir synligt i
# dokumentflodet - ren progressiv forbattring.
TAB_CSS = """
.tabbar{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 24px;padding-bottom:16px;
 border-bottom:1px solid var(--grid)}
.tabbtn{font:inherit;font-size:13px;padding:6px 12px;border-radius:8px;
 border:1px solid var(--ring);background:var(--surface-1);color:var(--ink-2);cursor:pointer}
.tabbtn:hover{color:var(--ink-1)}
.tabbtn.active{background:var(--p-A);border-color:var(--p-A);color:#fff;font-weight:620}
.tabpane.js-hidden{display:none}
"""

TAB_JS = """
(function(){
  var bar=document.querySelector('.tabbar');
  if(!bar)return;
  var btns=Array.prototype.slice.call(bar.querySelectorAll('.tabbtn'));
  var panes=Array.prototype.slice.call(document.querySelectorAll('.tabpane'));
  function activate(id){
    btns.forEach(function(b){b.classList.toggle('active',b.dataset.tabid===id);});
    panes.forEach(function(p){p.classList.toggle('js-hidden',p.dataset.tabid!==id);});
  }
  btns.forEach(function(b){
    b.addEventListener('click',function(){
      activate(b.dataset.tabid);
      history.replaceState(null,'','#'+b.dataset.target);
    });
  });
  function franHash(){
    var hash=location.hash.slice(1);
    if(!hash)return false;
    var el=document.getElementById(hash);
    if(!el)return false;
    var pane=el.closest('.tabpane');
    if(!pane)return false;
    activate(pane.dataset.tabid);
    requestAnimationFrame(function(){el.scrollIntoView();});
    return true;
  }
  window.addEventListener('hashchange',franHash);
  if(!franHash() && btns.length)activate(btns[0].dataset.tabid);
})();
"""


def flikifiera(brod):
    """Delar upp brodtexten i flikar per top-level <h2>-avsnitt.

    Allt fore forsta h2 (rubrik, TOC, ingress) forblir alltid synligt
    ovanfor fliksraden - bara sjalva "Del"-/"Bilaga"-avsnitten blir
    flikar. Fungerar bara for sidor dar h2 aldrig ligger nastlat i
    nagot annat block (sant for markdown-genererad HTML, dar rubriker
    alltid ar block pa toppniva)."""
    brod = re.sub(r"\s*<hr\s*/?>\s*", "\n", brod)
    delar = re.split(r"(?=<h2\b)", brod)
    inledning, sektioner = delar[0], delar[1:]
    if len(sektioner) < 3:
        return brod  # for fa avsnitt - inte lont att floka

    flikar, paneler = [], []
    for i, sek in enumerate(sektioner):
        m = re.match(r'<h2 id="([^"]+)">(.*?)</h2>', sek, re.S)
        tabid = f"p{i}"
        aktiv = " active" if i == 0 else ""
        dold = "" if i == 0 else " js-hidden"
        if not m:
            paneler.append(f'<div class="tabpane{dold}" data-tabid="{tabid}">{sek}</div>')
            continue
        hid, titel = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        flikar.append(
            f'<button type="button" class="tabbtn{aktiv}" data-tabid="{tabid}" '
            f'data-target="{hid}">{titel}</button>'
        )
        paneler.append(f'<div class="tabpane{dold}" data-tabid="{tabid}">{sek}</div>')

    flikrad = '<div class="tabbar">' + "".join(flikar) + "</div>"
    return inledning + flikrad + "".join(paneler)


# Kopiera-knapp pa alla kodrutor (tillagd 2026-09-30). Clipboard-API:t
# kraver https (github.io); execCommand-reserven gor att det fungerar
# aven nar sidan oppnas som lokal fil.
KOPIERA_CSS = """
.kodruta{position:relative}
.kodruta pre{padding-right:78px}
.kopiera{position:absolute;top:8px;right:8px;font:600 12px/1 system-ui,sans-serif;
 padding:6px 10px;border-radius:7px;border:1px solid var(--ring);background:var(--plane);
 color:var(--ink-2);cursor:pointer;opacity:.85}
.kopiera:hover{opacity:1;color:var(--ink)}
.kopiera.ok{color:var(--p-D);border-color:var(--p-D)}
"""

KOPIERA_JS = """
(function(){
  function reserv(t){var a=document.createElement('textarea');a.value=t;
    a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);
    a.select();var ok=false;try{ok=document.execCommand('copy');}catch(e){}
    document.body.removeChild(a);return ok;}
  document.querySelectorAll('pre').forEach(function(pre){
    var w=document.createElement('div');w.className='kodruta';
    pre.parentNode.insertBefore(w,pre);w.appendChild(pre);
    var b=document.createElement('button');b.type='button';b.className='kopiera';
    b.textContent='Kopiera';b.title='Kopiera koden';w.appendChild(b);
    b.addEventListener('click',function(){
      var t=(pre.querySelector('code')||pre).innerText;
      function klar(ok){b.textContent=ok?'Kopierat \u2713':'Markera + Ctrl+C';
        b.classList.toggle('ok',ok);
        setTimeout(function(){b.textContent='Kopiera';b.classList.remove('ok');},1800);}
      if(navigator.clipboard&&window.isSecureContext){
        navigator.clipboard.writeText(t).then(function(){klar(true);},function(){klar(reserv(t));});
      }else{klar(reserv(t));}
    });
  });
})();
"""


SIDMALL = """<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<style>{tokens}{bas}{extra}</style>
</head>
<body>
<div class="wrap">
<div class="topbar">
  <div class="crumb">{crumb}</div>
  <button id="themeBtn" type="button">Mörkt</button>
</div>
{brod}
</div>
<script>{js}</script>
</body>
</html>
"""


BRED_CSS = """
.wrap{max-width:1080px}
p,ul,ol{max-width:80ch}
.tabpane > h3{border-top:1px solid var(--grid);padding-top:22px}
"""


def bygg_dok(md_sokvag, ut_sokvag, flikar=False, bred=False, toc=True):
    """Konverterar en markdownfil till en fristaende HTML-sida."""
    text = pathlib.Path(md_sokvag).read_text(encoding="utf-8")
    md = markdown.Markdown(
        extensions=["extra", "toc", "sane_lists", "admonition"],
        extension_configs={"toc": {"permalink": False, "toc_depth": "2-3"}},
    )
    brod = md.convert(text)
    # tabeller i ett eget omslag som scrollar i sidled pa smala skarmar
    brod = re.sub(r"<table>(.*?)</table>", r'<div class="tabell"><table>\1</table></div>', brod, flags=re.S)

    forsta = re.search(r"<h1[^>]*>(.*?)</h1>", brod, re.S)
    titel = re.sub(r"<[^>]+>", "", forsta.group(1)).strip() if forsta else pathlib.Path(md_sokvag).stem

    toc = ""
    if toc and md.toc_tokens:
        toc = f'<nav class="toc"><div class="t">Innehåll</div>{md.toc}</nav>'
        # lagg innehallsforteckningen direkt efter rubriken
        if forsta:
            brod = brod[: forsta.end()] + toc + brod[forsta.end():]
        else:
            brod = toc + brod

    extra = DOK_CSS + KOPIERA_CSS + (BRED_CSS if bred else "")
    js = TEMA_JS + KOPIERA_JS
    if flikar:
        brod = flikifiera(brod)
        extra = DOK_CSS + KOPIERA_CSS + TAB_CSS + (BRED_CSS if bred else "")
        js = TEMA_JS + KOPIERA_JS + TAB_JS

    sida = SIDMALL.format(
        titel=f"{titel} — NNK 2026",
        tokens=TOKENS,
        bas=BAS,
        extra=extra,
        crumb='<a href="../index.html">← Kontrollpanel NNK 2026</a>',
        brod=brod,
        js=js,
    )
    pathlib.Path(ut_sokvag).write_text(sida, encoding="utf-8")
    return titel, len(sida)


# Namn -> installningar for bygg_dok (flikar, bred, toc).
# runbook och filterguide (2026-10-06): flikar per arbetspaket/grupp, bred
# layout och ingen innehallsforteckning (flikraden och oversiktstabellerna
# ersatter den).
DOKUMENT = {
    "arbetsplan": {},
    "runbook": {"flikar": True, "bred": True, "toc": False},
    "filterguide": {"flikar": True, "bred": True, "toc": False},
    "metodik": {},
    "typiska-arter": {},
    "vagledningar": {},
    "webbgis-publicering": {"flikar": True},
    "attributbeskrivning": {},
    "popup-arcade-uttryck": {},
}

if __name__ == "__main__":
    rot = pathlib.Path(__file__).parent
    for namn, inst in DOKUMENT.items():
        md_path = rot / "docs" / f"{namn}.md"
        if not md_path.exists():
            print(f"hoppar over {namn} - {md_path} saknas")
            continue
        titel, n = bygg_dok(md_path, rot / "docs" / f"{namn}.html", **inst)
        tagg = " [flikar]" if inst.get("flikar") else ""
        print(f"docs/{namn}.html  <- {titel}  ({n:,} tecken){tagg}")
