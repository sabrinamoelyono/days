"""Inject the China editorial story and the boarding-pass set (v2) into posts.html.
Idempotent: everything between the V2 markers is regenerated."""
from pathlib import Path

P = Path(__file__).with_name("posts.html")
s = P.read_text()

CSS = """
  /* ---------- Boarding pass set (v2) ---------- */
  .bp{background:var(--ink);color:var(--ink)}
  .bp .bg{position:absolute;left:0;top:0;width:100%;object-fit:cover}
  .bp .shade{position:absolute;left:0;right:0}
  .bp .mark{position:absolute;filter:brightness(0) invert(1);z-index:2}
  .bp .tag{position:absolute;z-index:2;font-family:var(--mono);letter-spacing:.14em;text-transform:uppercase;color:#fff}
  .bp .card{position:absolute;background:var(--paper);border-radius:18px;overflow:hidden;box-shadow:0 40px 80px -30px rgba(0,0,0,.65)}
  .bp .strip{display:flex;justify-content:space-between;align-items:center;background:var(--orange);color:#fff;font-family:var(--mono);letter-spacing:.16em;text-transform:uppercase}
  .bp .body{position:relative}
  .bp .rt{display:flex;align-items:center;justify-content:space-between}
  .bp .rt .code{font-family:var(--mono);font-weight:500;line-height:1;letter-spacing:.02em}
  .bp .rt .city{font-family:var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-top:8px}
  .bp .rt .r{text-align:right}
  .bp .rt .path{flex:1;display:flex;align-items:center;gap:12px}
  .bp .rt .path::before,.bp .rt .path::after{content:"";flex:1;height:1px;background:repeating-linear-gradient(90deg,var(--muted) 0 6px,transparent 6px 12px)}
  .bp .rt .path svg{flex:none;fill:var(--orange)}
  .bp h1 em{color:var(--orange)}
  .bp .tear{position:relative;height:0;border-top:2px dashed var(--line)}
  .bp .tear::before,.bp .tear::after{content:"";position:absolute;top:-17px;width:32px;height:32px;border-radius:50%;background:var(--ink)}
  .bp .tear::before{left:-16px}.bp .tear::after{right:-16px}
  .bp .stub{display:flex;align-items:center;justify-content:space-between}
  .bp .grid{display:grid;grid-template-columns:auto auto;column-gap:56px}
  .bp .grid div{font-family:var(--mono);font-weight:500;letter-spacing:.03em}
  .bp .grid span{display:block;font-weight:400;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
  .bp .grid .tel{grid-column:1 / -1;font-family:var(--sans);font-weight:600;letter-spacing:-.01em;color:var(--ink)}
  .bp .qr{display:flex;flex-direction:column;align-items:center;gap:10px}
  .bp .qr img{display:block}
  .bp .qr p{font-family:var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);text-align:center}
  .bp .caption{position:absolute;z-index:2;bottom:auto}

  .bp.sq .mark{left:56px;top:52px;height:40px}
  .bp.sq .tag{right:56px;top:62px;font-size:15px}
  .bp.sq .card{left:48px;right:48px;bottom:48px}
  .bp.sq .strip{padding:14px 32px;font-size:13px}
  .bp.sq .body{padding:26px 32px 26px}
  .bp.sq .rt .code{font-size:46px}.bp.sq .rt .city{font-size:12px}
  .bp.sq .rt .path svg{width:26px;height:26px}
  .bp.sq h1{font-size:46px;margin-top:20px}
  .bp.sq .stub{padding:22px 32px 24px}
  .bp.sq .grid{row-gap:12px}.bp.sq .grid div{font-size:15px}.bp.sq .grid span{font-size:11px}
  .bp.sq .grid .tel{font-size:30px}
  .bp.sq .qr img{width:112px}.bp.sq .qr p{font-size:10px}
  .bp.sq .caption{left:56px;top:112px}

  .bp.st .mark{left:64px;top:100px;height:54px}
  .bp.st .tag{right:64px;top:114px;font-size:19px}
  .bp.st .card{left:56px;right:56px;bottom:150px}
  .bp.st .strip{padding:22px 44px;font-size:17px}
  .bp.st .body{padding:44px 44px 44px}
  .bp.st .rt .code{font-size:72px}.bp.st .rt .city{font-size:16px;margin-top:12px}
  .bp.st .rt .path svg{width:38px;height:38px}
  .bp.st h1{font-size:76px;margin-top:36px}
  .bp.st .sub{font-size:28px;margin-top:20px}
  .bp.st .stub{padding:40px 44px 44px}
  .bp.st .grid{row-gap:24px}.bp.st .grid div{font-size:21px}.bp.st .grid span{font-size:14px}
  .bp.st .grid .tel{font-size:44px}
  .bp.st .qr img{width:170px}.bp.st .qr p{font-size:13px}
  .bp.st .caption{left:64px;top:186px;--cf:15px}
"""

PLANE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z" transform="rotate(90 12 12)"/></svg>'

SETS = [
    # id, series no, photo, bg style (square), bg style (story), caption, dest code, dest city, visa label, headline, sub
    dict(id="china", no="01", img="plate-china.jpg",
         sq="height:760px;object-position:0 60%", st="height:1240px;object-position:0 50%",
         cap="Summer Palace · Beijing", code="PEK", city="Beijing", visa="Tiongkok · L",
         h1='Sudah lama di wishlist. <em>Saatnya berangkat.</em>',
         sub="Dokumen sampai jadwal pengajuan — <strong>DAYS yang siapkan.</strong> Kamu tinggal pilih tanggal."),
    dict(id="schengen", no="02", img="plate-schengen.jpg",
         sq="height:760px;object-position:0 35%", st="height:1240px;object-position:88% 50%",
         cap="Piazza dei Miracoli · Pisa", code="PSA", city="Pisa", visa="Schengen · C",
         h1='Eropa dimulai dari <em>satu&nbsp;visa.</em>',
         sub="Dokumen, formulir, jadwal biometrik — <strong>DAYS yang urus.</strong> Kamu fokus ke itinerary."),
    dict(id="shanghai", no="03", img="plate-panda.jpg",
         sq="height:700px;object-position:50% 72%", st="height:1240px;object-position:50% 40%",
         cap=None, code="PVG", city="Shanghai", visa="Tiongkok · L",
         h1='Shanghai, <em>bukan sekadar wishlist.</em>',
         sub="Apply visa Tiongkok sekarang — <strong>DAYS yang bantu</strong> dari awal sampai beres."),
]

TEL = "+62 812-2000-0185"


def post(d, fmt):
    sq = fmt == "square"
    bg = d["sq"] if sq else d["st"]
    shade_top = "top:0;height:240px" if sq else "top:0;height:380px"
    h = int(bg.split("height:")[1].split("px")[0])
    shade_bot = f"top:{h-260}px;height:262px"
    cap = f'<span class="caption">{d["cap"]}</span>' if d["cap"] else ""
    sub = "" if sq else f'<p class="sub">{d["sub"]}</p>'
    return f'''
<!-- v2 · {d["id"]} · {fmt} -->
<section class="post {"sq" if sq else "st"} bp" id="pass-{d["id"]}-{fmt}">
  <img class="bg" src="img/{d["img"]}" style="{bg}" alt="">
  <div class="shade" style="{shade_top};background:linear-gradient(180deg,rgba(27,23,20,.55),rgba(27,23,20,0))"></div>
  <div class="shade" style="{shade_bot};background:linear-gradient(180deg,rgba(27,23,20,0),var(--ink))"></div>
  <img class="mark" src="img/days-wordmark.png" alt="DAYS">
  <span class="tag">Visa Series — {d["no"]}</span>
  {cap}
  <div class="card">
    <div class="strip"><span>Boarding pass</span><span>Visa {d["visa"].split(" ·")[0]}</span></div>
    <div class="body">
      <div class="rt">
        <div><p class="code">CGK</p><p class="city">Jakarta</p></div>
        <div class="path">{PLANE}</div>
        <div class="r"><p class="code">{d["code"]}</p><p class="city">{d["city"]}</p></div>
      </div>
      <h1>{d["h1"]}</h1>
      {sub}
    </div>
    <div class="tear"></div>
    <div class="stub">
      <div class="grid">
        <div><span>Penumpang</span>Kamu</div>
        <div><span>Visa</span>{d["visa"]}</div>
        <div class="tel"><span>WhatsApp DAYS</span>{TEL}</div>
      </div>
      <div class="qr"><img src="img/qr-wa-0185.svg" alt="QR WhatsApp DAYS"><p>Scan untuk<br>chat</p></div>
    </div>
  </div>
</section>
'''


CHINA_STORY = '''
<!-- 06 · China visa · story (editorial) -->
<section class="post st ed" id="china-story">
  <div class="top">
    <img class="mark" src="img/days-wordmark.png" alt="DAYS">
    <span class="eyebrow">Visa Series — 01</span>
  </div>
  <div class="photo" style="height:880px">
    <img src="img/plate-china.jpg" style="object-position:0 50%" alt="">
    <span class="caption">Summer Palace · Beijing</span>
  </div>
  <div class="copy">
    <p class="eyebrow"><b>●</b>&nbsp; Visa Tiongkok</p>
    <h1>Sudah lama di wishlist. <em>Saatnya berangkat.</em></h1>
    <p class="sub">Shanghai, Beijing, Chengdu — dokumen sampai jadwal, <strong>DAYS yang siapkan.</strong></p>
  </div>
  <div class="foot">
    <div class="rule"></div>
    <div class="cta">
      <div><p class="label">Konsultasi via WhatsApp</p><p class="num">+62 812-2000-0495</p></div>
      <span class="pill"><i></i>Apply visa</span>
    </div>
  </div>
</section>
'''

A, B = "<!-- V2:BEGIN -->", "<!-- V2:END -->"
CA, CB = "/* V2CSS:BEGIN */", "/* V2CSS:END */"
html = CHINA_STORY + "".join(post(d, f) for d in SETS for f in ("square", "story"))
if A in s:
    s = s[:s.index(A)] + s[s.index(B) + len(B):]
    s = s[:s.index(CA)] + s[s.index(CB) + len(CB):]
s = s.replace("</body>", f"{A}{html}{B}\n</body>")
s = s.replace("</style>", f"{CA}{CSS}{CB}\n</style>")
P.write_text(s)
print("ok")
