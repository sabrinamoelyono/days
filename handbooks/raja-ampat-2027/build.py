"""Build the DAYS Raja Ampat 2027 package proposal as print-ready HTML.

Rebuilt from the original Canva draft (RAJA_AMPAT_PACKAGE.pdf) in the DAYS
Brand Profile system (2027), set in the DAYS type pair (Inter Tight +
JetBrains Mono), navy on warm
gradient paper, and the Nature collection colour + wave motif, since the
landscape is the reason for this trip. English leads, Bahasa Indonesia
follows. Page size matches the original 4:5 format (1080 x 1350 px) so pages
also work as Instagram / WhatsApp slides.

Run:  python3 build.py && node render.js
"""
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent

# ---------------------------------------------------------------- content
# Trip facts are carried over verbatim from the original proposal.

FACTS = [
    ("Dates", "Tanggal", "21–25 February 2027"),
    ("Length", "Durasi", "5 days, 4 nights"),
    ("Flights", "Penerbangan", "Bali – Sorong – Bali"),
    ("Group", "Peserta", "Minimum 2 guests"),
]
PRICE = "IDR 55,000,000"

DAYS_ = [
    ("21 Feb", "Arrival", "Kedatangan", "Sorong · Raja Ampat",
     "Fly from Bali to Sorong, then cross the water into the islands. The afternoon is yours to settle in and catch the first sunset.",
     "Terbang dari Bali ke Sorong, lalu menyeberang ke kepulauan. Sore hari bebas untuk beristirahat dan menikmati senja pertama."),
    ("22 Feb", "Piaynemo", "Piaynemo", "Piaynemo · Arborek · Pasir Timbul",
     "Climb to the Piaynemo lookout for the view of the karst islands. Then visit Arborek, a village that lives alongside the reef, and Pasir Timbul, a sandbar that appears with the tide.",
     "Mendaki ke puncak Piaynemo untuk pemandangan pulau karst, mengunjungi Desa Arborek, dan singgah di Pasir Timbul saat air surut."),
    ("23 Feb", "The reefs", "Hari di laut", "Waringkabom · Sawandarek · Yenbuba · Friwen Monda",
     "A day in the water, snorkelling jetty reefs and channels in one of the richest marine regions on earth.",
     "Seharian di laut: snorkeling di dermaga dan selat, di salah satu kawasan laut terkaya di dunia."),
    ("24 Feb", "Kabui", "Kabui", "Kabui Bay · Marindal Hill · Mayalibit · Kalibiru",
     "Weave between limestone walls in Kabui Bay, trek up Marindal Hill, take in the calm of Mayalibit Bay and end the last full day at Kalibiru.",
     "Menyusuri tebing kapur Teluk Kabui, trekking ke Bukit Marindal, menikmati tenangnya Teluk Mayalibit, dan menutup hari di Kalibiru."),
    ("25 Feb", "Departure", "Kepulangan", "Raja Ampat · Sorong · Bali",
     "A last swim if the morning allows, then back to Sorong for the flight home to Bali.",
     "Berenang sekali lagi bila waktu memungkinkan, lalu kembali ke Sorong untuk penerbangan pulang ke Bali."),
]

INCLUDED = [
    ("Getting there", "Perjalanan", ["Return flights, Bali – Sorong", "Airport transfers", "Destination transfers"]),
    ("Staying", "Menginap", ["4 nights' accommodation", "Meals throughout the trip"]),
    ("Experiences", "Pengalaman", ["Snorkelling", "Trekking", "Arborek Village visit"]),
    ("On the ground", "Selama di lokasi", ["Private car with driver (basic English)", "10 hours of service per day", "Fuel and parking fees"]),
]

CONTACT = [
    ("WhatsApp / Phone", "+62 812 2000 0185"),
    ("Email", "lets@talkaboutdays.com"),
    ("Instagram", "@talkaboutdays"),
    ("Website", "talkaboutdays.com"),
    ("Studio", "Jl. Tebet Barat IX No. 2, Jakarta Selatan"),
    ("Hours", "Mon–Fri · 09.00–18.00<br>Sat · 11.00–14.00<br>Sun · Closed"),
]

# Nature collection motif: five stacked waves, as in the Brand Profile.
WAVES = '''<svg class="waves" viewBox="0 0 310 112" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" aria-hidden="true">''' + "".join(
    f'<path d="M2 {8+i*22} C 60 {-4+i*22}, 100 {22+i*22}, 155 {10+i*22} S 250 {-4+i*22}, 308 {10+i*22}"/>' for i in range(5)
) + "</svg>"

# ---------------------------------------------------------------- markup

def run(pg):
    return f'''<header class="run">
  <span>DAYS / Nature · Raja Ampat</span>
  <span>Proposal · February 2027 · {pg:02d}</span>
</header>'''


def label(en, id_=None):
    return f'<p class="label">{e(en)}{f" <span>· {e(id_)}</span>" if id_ else ""}</p>'


pages = []

# 01 cover — Nature collection panel over the hero photo
pages.append(f'''<section class="page cover">
  <div class="cover-photo"><img src="img/piaynemo.jpg" alt="Speedboat through the Piaynemo islands, Raja Ampat"></div>
  <div class="cover-panel">
    <img class="mark" src="img/days-wordmark-navy.png" alt="DAYS">
    <div class="cover-text">
      {label("Collection · Nature")}
      <h1>Raja Ampat</h1>
      <p class="cover-sub">Beyond the Postcard</p>
      <p class="id">Lebih dari sekadar kartu pos.</p>
    </div>
    <div class="cover-foot">
      {WAVES}
      <dl class="cover-facts">{"".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, _, v in FACTS[:3])}</dl>
    </div>
  </div>
</section>''')

# 02 introduction
pages.append(f'''<section class="page">
  {run(2)}
  <div class="intro">
    <div>
      {label("Why Raja Ampat", "Mengapa Raja Ampat")}
      <h2 class="display">Room to<br>breathe.</h2>
      <p class="campaign">Ruang untuk menikmati alam.</p>
      <p class="lead">At the far western tip of Papua, Raja Ampat is a place where the landscape is the reason to go: turquoise water, limestone islands, quiet lagoons and some of the richest reefs on earth.</p>
      <p>Most people know it from one photo, the view from Piaynemo. We've planned five days to see it properly, with time to take in the view. The route takes in Piaynemo, Batanta, Kabui and Kalibiru, and February brings calm seas and clear water.</p>
      <p class="id">Di ujung barat Papua, Raja Ampat adalah tempat di mana alam menjadi alasan utama untuk berangkat: air biru toska, pulau karst, laguna yang tenang, dan terumbu karang terkaya di dunia. Lima hari, dengan waktu untuk benar-benar menikmatinya.</p>
    </div>
    <figure class="intro-img"><img src="img/viewpoint.jpg" alt="The Piaynemo lookout over the karst islands"></figure>
  </div>
</section>''')

# 03 the package
pages.append(f'''<section class="page">
  {run(3)}
  <div class="body">
    {label("The package", "Paket perjalanan")}
    <h2 class="h">Beyond the Postcard</h2>
    <p class="route">Piaynemo <i>·</i> Batanta <i>·</i> Kabui <i>·</i> Kalibiru</p>
    <dl class="fact-grid">{"".join(f'<div><dt>{e(k)} <span>· {e(i)}</span></dt><dd>{e(v)}</dd></div>' for k, i, v in FACTS)}</dl>
    <div class="price">
      <div>{label("Per person", "Per orang")}<p class="amount">{e(PRICE)}</p></div>
      <p>Flights, accommodation, meals, a private car and every transfer in between, in one clear price.<span class="id">Tiket pesawat, akomodasi, makan, mobil pribadi, dan semua transfer dalam satu harga.</span></p>
    </div>
    <figure class="wide"><img src="img/lagoon.jpg" alt="A lagoon among the karst islands"></figure>
  </div>
</section>''')

# 04 itinerary
rows = "".join(f'''<li class="day">
  <div class="day-n"><span class="n">Day {i}</span><span class="date">{e(d)}</span></div>
  <div>
    <h3>{e(t)}{f' <span>· {e(ti)}</span>' if ti != t else ''}</h3>
    <p class="stops">{e(s)}</p>
    <p>{e(b)}</p>
    <p class="id">{e(bi)}</p>
  </div>
</li>''' for i, (d, t, ti, s, b, bi) in enumerate(DAYS_, 1))
pages.append(f'''<section class="page">
  {run(4)}
  <div class="body">
    {label("Day by day", "Rencana harian")}
    <h2 class="h">Five days in the islands</h2>
    <ol class="days">{rows}</ol>
  </div>
</section>''')

# 05 the stay
pages.append(f'''<section class="page">
  {run(5)}
  <div class="body">
    {label("Where you stay", "Tempat menginap")}
    <h2 class="h">Dcoral Raja Ampat</h2>
    <p class="lead narrow">Four nights by the water, with the reef close enough for a swim before breakfast.</p>
    <p class="id narrow">Empat malam di tepi laut, dengan terumbu karang yang cukup dekat untuk berenang sebelum sarapan.</p>
    <div class="gallery">
      <img class="g-main" src="img/stay-aerial.jpg" alt="Aerial view of the resort">
      <img src="img/stay-bed.jpg" alt="Room interior">
      <img src="img/stay-room.jpg" alt="Room interior">
    </div>
  </div>
</section>''')

# 06 included
cols = "".join(f'''<div class="inc">{label(h, hi)}<ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>''' for h, hi, items in INCLUDED)
pages.append(f'''<section class="page">
  {run(6)}
  <div class="body">
    {label("What's included", "Termasuk dalam paket")}
    <h2 class="h">We take care of the details.</h2>
    <p class="lead narrow">From landing in Sorong to flying home to Bali, the planning is ours, so you have room for the moments that make the trip yours.</p>
    <div class="incs">{cols}</div>
    <aside class="quote">
      {label("Why book with DAYS", "Mengapa DAYS")}
      <p class="q">“We are not just agents; we’ve tested and vetted every aspect of the places we suggest.”</p>
      <p>Your DAYS travel expert is on WhatsApp before and during the trip, for boat times, weather calls or a change of plan.</p>
    </aside>
  </div>
</section>''')

# 07 get in touch
rows = "".join(f"<div><dt>{e(k)}</dt><dd>{v if k == 'Hours' else e(v)}</dd></div>" for k, v in CONTACT)
pages.append(f'''<section class="page closing">
  <img class="mark" src="img/days-wordmark-orange.png" alt="DAYS">
  <div class="closing-main">
    {label("Get in touch", "Hubungi kami")}
    <h2 class="display">Let’s plan your<br>next DAYS.</h2>
    <p class="campaign">Yuk, rencanakan perjalananmu.</p>
    <dl class="contact">{rows}</dl>
  </div>
  <p class="foot">PT Vakansi Media Global · Licensed travel agency · Tebet, Jakarta Selatan</p>
</section>''')

css = (HERE / "proposal.css").read_text()
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>DAYS · Raja Ampat 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,800;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>{"".join(pages)}</body></html>'''
(HERE / "proposal.html").write_text(html)
print("wrote proposal.html,", len(pages), "pages")
