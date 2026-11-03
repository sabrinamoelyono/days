"""Generate loud.html: visa visuals in the style of the DAYS Instagram feed.
Feed reference: white centred DAYS wordmark, full-bleed moody photos, condensed white display
type, hand-drawn white doodles, yellow marker lettering + stars, solid red panel with an oval
photo cut-out, sky-blue panels with underlined caps, tilted label boxes.
Each concept renders at 1080x1350 (feed) and 1080x1920 (story)."""
from pathlib import Path

TEL = "+62 812-2000-0185"
RED, BLUE, YELLOW, INK = "#F94141", "#6DAAE5", "#F1E541", "#1B1714"

# ---- hand-drawn doodles -----------------------------------------------------------------
STAR_OUT = ('<svg viewBox="0 0 100 100" class="{c}" style="{s}"><path d="M50 6 C53 22 58 33 62 38 C70 39 84 38 95 40 '
            'C86 48 76 55 70 60 C72 72 76 84 79 94 C68 86 58 79 50 74 C42 80 31 87 20 94 C24 82 28 71 30 60 '
            'C22 54 12 47 5 40 C17 38 30 39 38 38 C42 30 46 20 50 6 Z" fill="none" stroke="currentColor" '
            'stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/></svg>')
STAR_FILL = ('<svg viewBox="0 0 100 100" class="{c}" style="{s}"><path d="M50 2 L57 38 L96 30 L63 52 L88 86 L52 66 '
             'L44 98 L38 62 L6 80 L30 50 L4 22 L40 36 Z" fill="currentColor"/></svg>')
ASTER = ('<svg viewBox="0 0 100 100" class="{c}" style="{s}"><g stroke="currentColor" stroke-width="7" '
         'stroke-linecap="round"><path d="M50 8 L51 92"/><path d="M12 30 L88 70"/><path d="M14 72 L86 28"/>'
         '</g></svg>')
PLANE = ('<svg viewBox="0 0 300 160" class="{c}" style="{s}"><path d="M10 140 C60 150 90 120 80 95 C70 70 30 85 '
         '50 110 C80 140 150 120 190 70" fill="none" stroke="currentColor" stroke-width="4" '
         'stroke-dasharray="10 12" stroke-linecap="round"/><path d="M200 60 L290 18 L250 100 L232 76 Z M232 76 '
         'L290 18" fill="none" stroke="currentColor" stroke-width="5" stroke-linejoin="round" '
         'stroke-linecap="round"/></svg>')
TICKS = ('<svg viewBox="0 0 40 40" class="{c}" style="{s}"><g stroke="currentColor" stroke-width="5" '
         'stroke-linecap="round"><path d="M8 30 L16 10"/><path d="M22 34 L30 14"/></g></svg>')


def d(svg, c="", s=""):
    return svg.format(c=c, s=s)


CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#888;-webkit-font-smoothing:antialiased}}
.post{{position:relative;overflow:hidden;margin:40px;width:1080px;container-type:size;color:#fff;
  font-family:'Montserrat',sans-serif}}
.fd{{height:1350px}} .st{{height:1920px}}
.abs{{position:absolute}}
.cover{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.mark{{position:absolute;left:50%;transform:translateX(-50%);top:var(--mt,3.4cqh);height:5.4cqw;
  filter:brightness(0) invert(1);z-index:5}}
.caps{{font-weight:800;text-transform:uppercase;letter-spacing:.02em}}
.cond{{font-family:'Anton',sans-serif;text-transform:uppercase;line-height:.86;letter-spacing:-.005em}}
.marker{{font-family:'Permanent Marker',cursive;line-height:.9}}
.pill{{display:inline-block;background:#fff;color:{INK};border-radius:999px;font-weight:800;
  font-size:4.2cqw;padding:1.6cqw 4cqw;white-space:nowrap;letter-spacing:.01em}}
.row{{position:absolute;left:5.2cqw;right:5.2cqw;display:flex;justify-content:space-between;align-items:center}}
.sm{{font-size:2.5cqw}}
svg{{position:absolute;overflow:visible}}
.white{{color:#fff}} .yellow{{color:{YELLOW}}}

/* A: red panel + oval cut-out (China) */
.a .bg{{filter:blur(10px) brightness(.45) saturate(1.1);transform:scale(1.08)}}
.a .panel{{left:5.2cqw;right:5.2cqw;top:9.4cqh;bottom:var(--pb);background:{RED}}}
.a .panel .kick{{position:absolute;left:3.4cqw;top:3cqw;font-size:2.7cqw}}
.a .oval{{position:absolute;left:50%;transform:translateX(-50%);top:9cqw;width:62cqw;bottom:6cqw;
  border-radius:50%;overflow:hidden}}
.a .oval img{{object-position:12% 50%}}
.a .oval .note{{position:absolute;right:6cqw;top:30%;font-size:2.5cqw;z-index:2;text-shadow:0 1px 6px rgba(0,0,0,.4)}}
.a .big{{left:0;right:0;bottom:var(--bb);text-align:center;font-size:15.2cqw;white-space:nowrap;transform:scaleY(1.9);
  transform-origin:bottom center;z-index:4}}
.a .bigsub{{left:0;right:0;text-align:center;font-size:3.4cqw;bottom:var(--bs);z-index:4}}

/* B: blue + doodles (Europe) */
.b{{background:{BLUE}}}
.b .shot{{right:5.2cqw;top:var(--pt);width:60cqw;height:var(--ph);overflow:hidden;background:#000}}
.b .shot img{{object-position:88% 70%}}
.b .copy{{left:5.2cqw;right:5.2cqw;top:var(--cb);font-size:4.3cqw;line-height:1.45}}
.b .copy span{{text-decoration:underline;text-decoration-thickness:.3cqw;text-underline-offset:.9cqw}}
.b .hand{{left:6cqw;font-size:9.5cqw;transform:rotate(-8deg);top:var(--ht)}}

/* C: photo + yellow marker + tilted labels (Shanghai) */
.c{{background:{INK}}}
.c .photo{{position:absolute;left:0;top:var(--it);width:100%;height:auto}}
.c .fade{{left:0;right:0;top:var(--ft);height:22cqw;background:linear-gradient(180deg,rgba(27,23,20,0),{INK})}}
.c .topfade{{left:0;right:0;top:0;height:30cqw;background:linear-gradient(180deg,rgba(27,23,20,.55),rgba(27,23,20,0))}}
.c .hand{{left:5cqw;top:var(--ht);font-size:16cqw;transform:rotate(-9deg);color:{YELLOW};
  text-shadow:.5cqw .5cqw 0 rgba(0,0,0,.25)}}
.c .lab{{right:5cqw;top:var(--lt);display:flex;flex-direction:column;align-items:flex-end;gap:1.2cqw;transform:rotate(-6deg)}}
.c .lab span{{background:{YELLOW};color:{INK};font-weight:800;text-transform:uppercase;font-size:7.4cqw;
  line-height:1;padding:1.4cqw 2.6cqw 1.6cqw;border-radius:1.6cqw}}
.c .lab span:nth-child(2){{margin-right:5cqw}}
"""


def foot(bottom, left="Buat visa sekarang", pill_style=""):
    return (f'<div class="row" style="bottom:{bottom}"><span class="caps sm">{left}</span>'
            f'<span class="pill" style="{pill_style}">{TEL}</span></div>')


def post_a(fmt):
    fd = fmt == "feed"
    v = "--pb:29cqh;--bb:15.4cqh;--bs:11.3cqh" if fd else "--pb:30cqh;--bb:18cqh;--bs:14.6cqh;--mt:5.2cqh"
    return f'''
<section class="post {"fd" if fd else "st"} a" id="loud-china-{fmt}" style="{v}">
  <img class="cover bg" src="img/plate-china.jpg" alt="">
  <img class="mark" src="img/days-wordmark.png" alt="DAYS">
  <div class="abs panel">
    <p class="kick caps">Beijing · Shanghai · Chengdu</p>
    <div class="oval"><img class="cover" src="img/plate-china.jpg" alt=""><span class="note caps">Visa-nya kami urus</span></div>
  </div>
  <h1 class="abs cond big">Visa Tiongkok</h1>
  <p class="abs caps bigsub">Jangan cuma masuk wishlist.</p>
  {d(STAR_FILL, "yellow", "width:9cqw;right:7cqw;top:12.4cqh;transform:rotate(12deg)")}
  {d(ASTER, "white", "width:5cqw;left:9cqw;top:" + ("62cqh" if fd else "64cqh"))}
  {foot("4.2cqh" if fd else "6.5cqh")}
</section>'''


def post_b(fmt):
    fd = fmt == "feed"
    v = ("--pt:12.5cqh;--ph:44cqh;--cb:71cqh;--ht:61cqh" if fd
         else "--pt:12.5cqh;--ph:46cqh;--cb:70cqh;--ht:62cqh;--mt:5.2cqh")
    return f'''
<section class="post {"fd" if fd else "st"} b" id="loud-schengen-{fmt}" style="{v}">
  <img class="mark" src="img/days-wordmark.png" alt="DAYS">
  <div class="abs shot"><img class="cover" src="img/plate-schengen.jpg" alt=""></div>
  {d(PLANE, "white", "width:42cqw;left:4cqw;top:" + ("20cqh" if fd else "19cqh"))}
  {d(STAR_OUT, "white", "width:17cqw;right:2cqw;top:" + ("8.5cqh" if fd else "9.6cqh") + ";transform:rotate(14deg)")}
  {d(STAR_OUT, "white", "width:11cqw;left:42cqw;top:" + ("52cqh" if fd else "54cqh") + ";transform:rotate(-10deg)")}
  {d(STAR_OUT, "white", "width:8cqw;left:52cqw;top:" + ("55cqh" if fd else "56.4cqh") + ";transform:rotate(18deg)")}
  {d(ASTER, "white", "width:5.5cqw;left:10cqw;top:" + ("42cqh" if fd else "38cqh"))}
  {d(ASTER, "white", "width:4.4cqw;right:7cqw;top:" + ("61cqh" if fd else "62cqh"))}
  {d(TICKS, "white", "width:4cqw;left:30cqw;top:" + ("47cqh" if fd else "45cqh"))}
  <p class="abs marker hand white">Ciao, Eropa!</p>
  <p class="abs caps copy"><span>Eropa dimulai dari satu visa.</span><br><span>Dokumen, formulir, biometrik:</span><br><span>DAYS yang urus prosesnya.</span></p>
  {foot("4.2cqh" if fd else "6.5cqh", pill_style="color:#2F6FB0")}
</section>'''


def post_c(fmt):
    fd = fmt == "feed"
    # plate-panda is 900x925 -> 1080x1110 at full width
    v = ("--it:-60px;--ft:63cqh;--ht:8.5cqh;--lt:49cqh" if fd
         else "--it:0px;--ft:47cqh;--ht:10cqh;--lt:46cqh;--mt:5.2cqh")
    return f'''
<section class="post {"fd" if fd else "st"} c" id="loud-shanghai-{fmt}" style="{v}">
  <img class="photo" src="img/plate-panda.jpg" alt="">
  <div class="abs topfade"></div><div class="abs fade"></div>
  <img class="mark" src="img/days-wordmark.png" alt="DAYS">
  <p class="abs marker hand">Shanghai</p>
  {d(STAR_FILL, "yellow", "width:10cqw;right:4cqw;top:" + ("20cqh" if fd else "17cqh") + ";transform:rotate(-8deg)")}
  {d(STAR_FILL, "yellow", "width:6cqw;right:20cqw;top:" + ("27cqh" if fd else "22cqh") + ";transform:rotate(20deg)")}
  {d(STAR_FILL, "yellow", "width:7cqw;left:8cqw;top:" + ("71cqh" if fd else "60cqh"))}
  <div class="abs lab"><span>Bukan sekadar</span><span>wishlist.</span></div>
  <p class="abs caps" style="left:5.2cqw;right:5.2cqw;top:{"80cqh" if fd else "68cqh"};font-size:4.4cqw;line-height:1.3">
    Apply visa Tiongkok sekarang.<br><span style="color:{YELLOW}">DAYS yang bantu sampai beres.</span></p>
  {foot("4.2cqh" if fd else "6.5cqh")}
</section>'''


html = f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><title>DAYS Visa Loud</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@600;700;800&family=Permanent+Marker&display=block" rel="stylesheet">
<style>{CSS}</style></head><body>
{"".join(f(fmt) for f in (post_a, post_b, post_c) for fmt in ("feed", "story"))}
</body></html>'''
Path(__file__).with_name("loud.html").write_text(html)
print("ok")
