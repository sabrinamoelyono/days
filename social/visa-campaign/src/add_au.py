"""Inject the Australia editorial (clean) feed post + story into posts.html.
Idempotent: everything between the AU markers is regenerated."""
from pathlib import Path
from au_art import draw

P = Path(__file__).with_name("posts.html")
s = P.read_text()
TEL = "+62 812-2000-0185"

CSS = """
  /* ---------- Australia illustration panel ---------- */
  .illo{background:linear-gradient(180deg,#FDEEE9 0%,#FBF8F5 100%);display:flex;align-items:flex-end;justify-content:center}
  .illo svg{position:relative;width:88%;height:auto;margin-bottom:6%}
"""


def section(fmt):
    sq = fmt == "square"
    art = draw()
    photo_style = "" if sq else ' style="height:760px"'
    h1 = 'Ke Australia,<br><em>tinggal urus visanya.</em>' if not sq else 'Ke Australia,<br><em>tinggal urus visanya.</em>'
    sub = ('Visitor visa (subclass 600): dokumen sampai pengajuan di ImmiAccount, <strong>DAYS yang urus.</strong>'
           if not sq else 'Visitor visa 600: dokumen sampai ImmiAccount, <strong>DAYS yang urus.</strong>')
    return f'''
<section class="post {"sq" if sq else "st"} ed" id="australia-{fmt}">
  <div class="top">
    <img class="mark" src="img/days-wordmark.png" alt="DAYS">
    <span class="eyebrow">Visa Series — 04</span>
  </div>
  <div class="photo illo"{photo_style}>
    {art}
    <span class="caption">Sydney Harbour · Sydney</span>
  </div>
  <div class="copy">
    <p class="eyebrow"><b>●</b>&nbsp; Visa Australia</p>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
  </div>
  <div class="foot">
    <div class="rule"></div>
    <div class="cta">
      <div><p class="label">Konsultasi via WhatsApp</p><p class="num">{TEL}</p></div>
      <span class="pill"><i></i>{"Mulai apply visa" if sq else "Apply visa"}</span>
    </div>
  </div>
</section>
'''


A, B = "<!-- AU:BEGIN -->", "<!-- AU:END -->"
CA, CB = "/* AUCSS:BEGIN */", "/* AUCSS:END */"
if A in s:
    s = s[:s.index(A)] + s[s.index(B) + len(B):]
    s = s[:s.index(CA)] + s[s.index(CB) + len(CB):]
s = s.replace("</body>", f"{A}{section('square')}{section('story')}{B}\n</body>")
s = s.replace("</style>", f"{CA}{CSS}{CB}\n</style>")
P.write_text(s)
print("ok")
