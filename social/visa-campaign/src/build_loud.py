"""Generate loud.html: the bold 'feed style' visa set (4:5 feed + 9:16 story).
Matches the DAYS Instagram feed look: flat saturated colour, heavy white caps with a hard
black shadow, an overlapping script word, a 'THE · stamp · EDITION' header, photo block."""
from pathlib import Path

TEL = "+62 812-2000-0185"

POSTS = [
    dict(id="china", bg="#D61B53", top="VISA", script="ke Tiongkok", bottom="BERES SAMA DAYS.",
         img="plate-china.jpg", pos="0 62%", stamp="Beijing"),
    dict(id="schengen", bg="#FFBABA", top="EROPA", script="dimulai dari satu", bottom="VISA.",
         img="plate-schengen.jpg", pos="88% 85%", stamp="Pisa"),
    dict(id="shanghai", bg="#EC5B39", top="SHANGHAI", script="bukan sekadar", bottom="WISHLIST.",
         img="plate-panda.jpg", pos="50% 68%", stamp="Shanghai"),
]

CSS = """
:root{--ink:#1B1714;--white:#FFFFFF}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#999;-webkit-font-smoothing:antialiased}
.post{position:relative;overflow:hidden;margin:40px;color:#fff;font-family:'Archivo Black',sans-serif;display:flex;flex-direction:column;align-items:center}
.fd{width:1080px;height:1350px;padding:84px 70px 70px}
.st{width:1080px;height:1920px;padding:150px 64px 150px}
.loud{color:#fff;text-transform:uppercase;line-height:.9;letter-spacing:-.01em;text-align:center;
  text-shadow:var(--sh) var(--sh) 0 var(--ink);-webkit-text-stroke:var(--sk) var(--ink);paint-order:stroke fill}
.script{font-family:'Pinyon Script',cursive;color:#fff;line-height:1;white-space:nowrap;text-align:center;
  -webkit-text-stroke:var(--sk2) var(--ink);paint-order:stroke fill;text-shadow:calc(var(--sh)*.6) calc(var(--sh)*.6) 0 var(--ink);position:relative;z-index:3}
.head{width:100%;display:flex;align-items:center;justify-content:space-between;font-size:var(--hf);letter-spacing:.02em;
  text-shadow:3px 3px 0 var(--ink)}
.stamp{text-shadow:2px 2px 0 var(--ink)}
.stamp{position:relative;padding:var(--stp);border-radius:50%;
  border:3px dotted rgba(255,255,255,.95);outline:2px solid rgba(255,255,255,.95);outline-offset:6px}
.photo{position:relative;width:100%;overflow:hidden;border:5px solid var(--ink);box-shadow:var(--sh2) var(--sh2) 0 var(--ink)}
.photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.foot{margin-top:auto;width:100%;display:flex;align-items:center;justify-content:space-between}
.foot .mark{height:var(--mh);filter:brightness(0) invert(1) drop-shadow(3px 3px 0 #1B1714)}
.tel{display:flex;flex-direction:column;align-items:flex-end;gap:10px}
.tel small{font-size:var(--tl);letter-spacing:.08em;text-shadow:2px 2px 0 var(--ink)}
.pill{background:#fff;color:var(--ink);border:4px solid var(--ink);border-radius:999px;font-size:var(--pf);padding:var(--pp);box-shadow:5px 5px 0 var(--ink);white-space:nowrap}

.fd{--sh:7px;--sh2:12px;--sk:2px;--sk2:3px;--hf:24px;--stp:10px 34px;--mh:46px;--tl:18px;--pf:30px;--pp:14px 30px}
.fd .t1{font-size:var(--t1);margin-top:70px}
.fd .script{font-size:var(--sc);margin-top:-70px;margin-bottom:-40px}
.fd .photo{height:560px}
.fd .t2{font-size:var(--t2);margin-top:34px}
.st{--sh:9px;--sh2:14px;--sk:2.5px;--sk2:3.5px;--hf:30px;--stp:12px 40px;--mh:62px;--tl:22px;--pf:38px;--pp:18px 38px}
.st .t1{font-size:var(--t1s);margin-top:110px}
.st .script{font-size:var(--sc);margin-top:-84px;margin-bottom:-50px}
.st .photo{height:860px}
.st .t2{font-size:var(--t2s);margin-top:46px}
"""


def size(word, base, width):
    """Shrink caps so long words fit the line (Archivo Black ~0.74em per glyph)."""
    return min(base, int(width / (0.74 * len(word))))


def post(d, fmt):
    fd = fmt == "feed"
    w = 940 if fd else 952
    t1 = size(d["top"], 210 if fd else 240, w)
    t2 = size(d["bottom"], 170 if fd else 180, w)
    sc = min(136 if fd else 170, int(w / (0.42 * len(d["script"]))))
    style = f'background:{d["bg"]};--t1:{t1}px;--t2:{t2}px;--t1s:{t1}px;--t2s:{t2}px;--sc:{sc}px'
    return f'''
<section class="post {"fd" if fd else "st"}" id="loud-{d["id"]}-{fmt}" style="{style}">
  <div class="head"><span>THE</span><span class="stamp">{d["stamp"]}</span><span>VISA EDITION</span></div>
  <h1 class="loud t1">{d["top"]}</h1>
  <p class="script">{d["script"]}</p>
  <div class="photo"><img src="img/{d["img"]}" style="object-position:{d["pos"]}" alt=""></div>
  <h2 class="loud t2">{d["bottom"]}</h2>
  <div class="foot">
    <img class="mark" src="img/days-wordmark.png" alt="DAYS">
    <div class="tel"><small>BUAT VISA SEKARANG</small><span class="pill">{TEL}</span></div>
  </div>
</section>'''


html = f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><title>DAYS Visa Loud</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Pinyon+Script&display=block" rel="stylesheet">
<style>{CSS}</style></head><body>
{"".join(post(d, f) for d in POSTS for f in ("feed", "story"))}
</body></html>'''
Path(__file__).with_name("loud.html").write_text(html)
print("ok")
