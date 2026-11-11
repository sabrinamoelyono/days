"""Build the A4 landscape edition of the DAYS Raja Ampat 2027 proposal.

A companion to the 4:5 proposal (build.py): same content, laid out on the
DAYS Brand Profile page system (A4 landscape, Nature collection panel,
warm grainy gradients, Inter Tight + JetBrains Mono) so it sits next to the
company profile as a matching client document.

Content is imported from build.py (which also regenerates proposal.html).

Run:  python3 build_a4.py && node render_a4.js
"""
from html import escape as e
from pathlib import Path

from build import FACTS, PRICE, DAYS_, INCLUDED, CONTACT, label

HERE = Path(__file__).parent

WAVES = '<svg viewBox="0 0 240 90" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true">' + "".join(
    f'<path d="M2 {8+i*17} C 60 {-4+i*17}, 100 {22+i*17}, 150 {8+i*17} S 210 {-2+i*17}, 238 {10+i*17}"/>' for i in range(5)) + "</svg>"


def top(pg):
    return f'<div class="topline"><span>DAYS / Nature · Raja Ampat</span><span>Proposal · February 2027 · {pg:02d}</span></div>'


# How booking works, adapted from the Brand Profile's four steps.
STEPS = [
    ("Start with the reason", "Tell us your dates and who's coming. The package runs with a minimum of two guests."),
    ("Plan the details", "We confirm flights, your stay at Dcoral and every transfer, with room for personal preferences."),
    ("Travel with a clear plan", "Before you fly, you get a bilingual A4 itinerary with confirmed bookings and meeting points."),
]

pages = []

# 01 cover — Nature panel + hero
pages.append(f'''<section class="page split g-nature">
  <div class="panel">
    <img class="panel-mark" src="img/days-wordmark-navy.png" alt="DAYS">
    <p class="panel-line">Room to<br>breathe.</p>
    <span class="panel-motif">{WAVES}</span>
  </div>
  <div class="cover-r">
    <figure class="hero"><img src="img/piaynemo.jpg" alt="Speedboat through the Piaynemo islands"></figure>
    <div class="cover-text">
      <div>
        {label("Collection · Nature", "Proposal")}
        <h1>Raja Ampat</h1>
        <p class="cover-sub">Beyond the Postcard</p>
        <p class="id">Lebih dari sekadar kartu pos. Ruang untuk menikmati alam.</p>
      </div>
      <dl class="mini">{"".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, _, v in FACTS[:3])}</dl>
    </div>
  </div>
</section>''')

# 02 why + the package
pages.append(f'''<section class="page g-who">
  {top(2)}
  <div class="two">
    <div>
      {label("Why Raja Ampat", "Mengapa Raja Ampat")}
      <h2 class="h">Where the landscape is the reason to go.</h2>
      <p class="lead">At the far western tip of Papua, Raja Ampat is turquoise water, limestone islands, quiet lagoons and some of the richest reefs on earth.</p>
      <p>Most people know it from one photo, the view from Piaynemo. We’ve planned five days to see it properly, with time to take in the view. The route takes in Piaynemo, Batanta, Kabui and Kalibiru, and February brings calm seas and clear water.</p>
      <p class="id">Di ujung barat Papua, Raja Ampat adalah tempat di mana alam menjadi alasan utama untuk berangkat. Lima hari, dengan waktu untuk benar-benar menikmatinya.</p>
      <figure class="strip"><img src="img/viewpoint.jpg" alt="The Piaynemo lookout"></figure>
    </div>
    <div>
      {label("The package", "Paket perjalanan")}
      <h3 class="h3">Beyond the Postcard</h3>
      <p class="route">Piaynemo <i>·</i> Batanta <i>·</i> Kabui <i>·</i> Kalibiru</p>
      <dl class="facts">{"".join(f'<div><dt>{e(k)} <span>· {e(i)}</span></dt><dd>{e(v)}</dd></div>' for k, i, v in FACTS)}</dl>
      <div class="price">
        <div>{label("Per person", "Per orang")}<p class="amount">{e(PRICE)}</p></div>
        <p>Flights, accommodation, meals, a private car and every transfer in between, in one clear price.<span class="id">Tiket pesawat, akomodasi, makan, mobil pribadi, dan semua transfer dalam satu harga.</span></p>
      </div>
      <div class="steps">{"".join(f'<div><p class="label sm step">Step {i}</p><h4>{e(h)}</h4><p>{e(d)}</p></div>' for i, (h, d) in enumerate(STEPS, 1))}</div>
    </div>
  </div>
</section>''')

# 03 day by day — five columns
cols = "".join(f'''<article class="day">
  <p class="dn">Day {i} <span>· {e(d)}</span></p>
  <h3>{e(t)}</h3>{f'<p class="ti">{e(ti)}</p>' if ti != t else '<p class="ti">&nbsp;</p>'}
  <p class="stops">{e(s)}</p>
  <p>{e(b)}</p>
  <p class="id">{e(bi)}</p>
</article>''' for i, (d, t, ti, s, b, bi) in enumerate(DAYS_, 1))
pages.append(f'''<section class="page g-arch">
  {top(3)}
  {label("Day by day", "Rencana harian")}
  <h2 class="h">Five days in the islands.</h2>
  <p class="sub">21–25 February 2027 · Bali – Sorong – Raja Ampat – Sorong – Bali</p>
  <figure class="band"><img src="img/lagoon.jpg" alt="A lagoon among the karst islands"></figure>
  <div class="days">{cols}</div>
</section>''')

# 04 stay + included
incs = "".join(f'''<div class="inc">{label(h, hi)}<ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>''' for h, hi, items in INCLUDED)
pages.append(f'''<section class="page g-serv">
  {top(4)}
  <div class="two wide-l">
    <div>
      {label("Where you stay", "Tempat menginap")}
      <h2 class="h">Dcoral Raja Ampat</h2>
      <p>Four nights by the water, with the reef close enough for a swim before breakfast.</p>
      <p class="id">Empat malam di tepi laut, dengan terumbu karang yang cukup dekat untuk berenang sebelum sarapan.</p>
      <div class="gallery">
        <img class="g-main" src="img/stay-aerial.jpg" alt="Aerial view of the resort">
        <img src="img/stay-bed.jpg" alt="Room interior">
        <img src="img/stay-room.jpg" alt="Room interior">
      </div>
    </div>
    <div>
      {label("What's included", "Termasuk dalam paket")}
      <h2 class="h">We take care of the details.</h2>
      <div class="incs">{incs}</div>
      <aside class="card why">
        {label("Why book with DAYS", "Mengapa DAYS")}
        <p class="quote">“We are not just agents; we’ve tested and vetted every aspect of the places we suggest.”</p>
        <p>Your DAYS travel expert is on WhatsApp before and during the trip, for boat times, weather calls or a change of plan.</p>
      </aside>
    </div>
  </div>
</section>''')

# 05 get in touch
rows = "".join(f"<div><dt>{e(k)}</dt><dd>{v if k == 'Hours' else e(v)}</dd></div>" for k, v in CONTACT)
pages.append(f'''<section class="page g-contact">
  <div class="contact-grid">
    <div>
      {label("Get in touch", "Hubungi kami")}
      <h2 class="h xl">Let’s plan your next DAYS.</h2>
      <p class="sub">Yuk, rencanakan perjalananmu.</p>
      <div class="recap card">
        <p class="label sm">Your trip</p>
        <p><strong>Raja Ampat · Beyond the Postcard</strong></p>
        <p>21–25 February 2027 · 5 days, 4 nights · from {e(PRICE)} per person</p>
      </div>
    </div>
    <dl class="contact">{rows}</dl>
  </div>
  <div class="foot"><img src="img/days-wordmark-orange.png" alt="DAYS"><span>PT Vakansi Media Global · Licensed travel agency · Tebet, Jakarta Selatan</span></div>
</section>''')

css = (HERE / "proposal-a4.css").read_text()
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>DAYS · Raja Ampat 2027 (A4)</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,800;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>{"".join(pages)}</body></html>'''
(HERE / "proposal-a4.html").write_text(html)
print("wrote proposal-a4.html,", len(pages), "pages")
