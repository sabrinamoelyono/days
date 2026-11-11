"""Build the DAYS Raja Ampat 2027 package proposal as print-ready HTML.

Rebuilt from the original Canva draft (RAJA_AMPAT_PACKAGE.pdf) in the DAYS
brand system — see /DESIGN.md. Page size matches the original 4:5 format
(1080 x 1350 px) so pages also work as Instagram / WhatsApp slides.

Run:  python3 build.py && node render.js
"""
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent
RUNNING = "Raja Ampat · West Papua · Feb 2027"

# ---------------------------------------------------------------- content
# Facts below are carried over verbatim from the original proposal.
# Only the copy and design have changed.

FACTS = [
    ("Dates", "21–25 Feb 2027"),
    ("Length", "5 days · 4 nights"),
    ("Flights", "Bali – Sorong – Bali"),
    ("Group", "Minimum 2 guests"),
]
PRICE = "IDR 55,000,000"

DAYS_ = [
    ("21 Feb", "Arrival", "Sorong → Raja Ampat",
     "Bali to Sorong, then across the water into the islands. The rest of the afternoon is yours — the first sunset sets the tone for everything after."),
    ("22 Feb", "Piaynemo", "Piaynemo · Arborek · Pasir Timbul",
     "The climb to the Piaynemo lookout: the karst view everyone has seen, now without a screen between you and it. Then Arborek, a village that lives on and with the reef, and Pasir Timbul — a sandbar that exists only when the tide allows."),
    ("23 Feb", "The reefs", "Waringkabom · Sawandarek · Yenbuba · Friwen Monda",
     "A day in the water. Jetty reefs and channel drop-offs, back to back, at the heart of the most biodiverse marine region on the planet. Bring the underwater camera."),
    ("24 Feb", "Kabui", "Kabui Bay · Marindal Hill · Mayalibit · Kalibiru",
     "Narrow passages between limestone walls through Kabui Bay, a trek up Marindal Hill, the still water of Mayalibit, and Kalibiru to close out the last full day."),
    ("25 Feb", "Departure", "Raja Ampat → Sorong → Bali",
     "One last swim if the morning allows, then back to Sorong for the flight home to Bali."),
]

INCLUDED = [
    ("Getting there", ["Return flights, Bali – Sorong", "Airport transfers", "Destination transfers"]),
    ("Staying", ["4 nights' accommodation", "Meals throughout the trip"]),
    ("Doing", ["Snorkelling", "Trekking", "Arborek Village visit"]),
    ("On the ground", ["Private car with driver (basic English)", "10 hours of service per day", "Fuel and parking fees"]),
]

# ---------------------------------------------------------------- markup

def run(pg):
    return f'''<header class="run">
  <img class="mark" src="img/days-wordmark.png" alt="DAYS">
  <span>{e(RUNNING)}</span>
  <span class="pg">{pg:02d}</span>
</header>'''


pages = []

# 01 cover
pages.append(f'''<section class="page cover" style="--img:url(img/piaynemo.jpg)">
  <img class="cover-mark" src="img/days-wordmark.png" alt="DAYS">
  <p class="cover-kicker">A DAYS package proposal</p>
  <div class="cover-main">
    <p class="eyebrow">Beyond the Postcard</p>
    <h1>Raja<br>Ampat<span class="dot">.</span></h1>
    <p class="cover-lede">Five days in West Papua, where the karst islands rise straight out of the reef and the water does most of the talking.</p>
    <dl class="facts">{"".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in FACTS[:3])}</dl>
  </div>
</section>''')

# 02 the hook
pages.append(f'''<section class="page">
  {run(2)}
  <div class="split">
    <div class="split-text">
      <p class="eyebrow">01 — Why now</p>
      <h2 class="h">You've seen the photo. This is the trip.</h2>
      <p class="lede">Everyone knows the Piaynemo shot. Very few people have stood at the top of those steps early, before the boats arrive, with the lagoons laid out below like someone spilled the sea in two shades of blue.</p>
      <p>Raja Ampat sits at the top of the Coral Triangle — more species of coral and reef fish than anywhere else on earth. It's remote enough that it still feels like a discovery — and from Bali, it's one domestic route away.</p>
      <p>February is calm-water season. Clear visibility, easy crossings, long light. We've built five days around the four places that matter most: <strong>Piaynemo, Batanta, Kabui and Kalibiru.</strong></p>
      <p class="pull">Some places are meant to be seen. Raja Ampat is meant to be in.</p>
    </div>
    <figure class="split-img"><img src="img/viewpoint.jpg" alt="The Piaynemo lookout over the karst islands"></figure>
  </div>
</section>''')

# 03 the package
pages.append(f'''<section class="page">
  {run(3)}
  <div class="body">
    <div class="opener">
      <p class="eyebrow">02 — The package</p>
      <h1>Beyond the Postcard</h1>
      <p class="route">Piaynemo <i>—</i> Batanta <i>—</i> Kabui <i>—</i> Kalibiru</p>
    </div>
    <dl class="fact-grid">{"".join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in FACTS)}</dl>
    <div class="price">
      <div><p class="eyebrow">Per person</p><p class="amount">{e(PRICE)}</p></div>
      <p class="price-note">Flights, accommodation, meals, private car and every transfer in between. One number, nothing to chase.</p>
    </div>
    <figure class="wide"><img src="img/piaynemo.jpg" alt="Speedboat through the Piaynemo islands"></figure>
  </div>
</section>''')

# 04 itinerary
rows = "".join(f'''<li class="day">
  <div class="day-n"><span class="num">Day {i}</span><span class="date">{e(d)}</span></div>
  <div><h3>{e(t)}</h3><p class="stops">{e(s)}</p><p class="desc">{e(b)}</p></div>
</li>''' for i, (d, t, s, b) in enumerate(DAYS_, 1))
pages.append(f'''<section class="page">
  {run(4)}
  <div class="body">
    <div class="opener"><p class="eyebrow">03 — The days</p><h1>Five days, four islands</h1></div>
    <ol class="days">{rows}</ol>
  </div>
</section>''')

# 05 the stay
pages.append(f'''<section class="page">
  {run(5)}
  <div class="body">
    <div class="opener">
      <p class="eyebrow">04 — Where you stay</p>
      <h1>Dcoral Raja Ampat</h1>
      <p class="lede">Four nights on the water's edge. Wake up, walk out, and the reef is right there — the best snorkelling of the trip might be the one before breakfast.</p>
    </div>
    <div class="gallery">
      <img class="g-main" src="img/stay-aerial.jpg" alt="Aerial view of the resort">
      <img src="img/stay-bed.jpg" alt="Room interior">
      <img src="img/stay-room.jpg" alt="Room interior">
    </div>
  </div>
</section>''')

# 06 included
cols = "".join(f'''<div class="inc"><p class="eyebrow">{e(h)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>''' for h, items in INCLUDED)
pages.append(f'''<section class="page">
  {run(6)}
  <div class="body">
    <div class="opener"><p class="eyebrow">05 — What's covered</p><h1>Handled, end to end</h1>
      <p class="lede">From the moment you land in Sorong to the moment you're back in Bali, the logistics are ours. You just have to show up.</p></div>
    <div class="incs">{cols}</div>
    <aside class="contact"><p class="eyebrow">The DAYS layer</p><p>Your DAYS trip lead is on WhatsApp before, during and after. Boat times, weather calls, a change of plan on day three — that's your first message, and we'll sort it.</p></aside>
  </div>
</section>''')

# 07 closing
pages.append(f'''<section class="page cover closing-img" style="--img:url(img/lagoon.jpg)">
  <img class="cover-mark" src="img/days-wordmark.png" alt="DAYS">
  <div class="cover-main">
    <p class="eyebrow">Beyond the Postcard · Raja Ampat</p>
    <h1 class="close-h">Come back<br>with a better<br>story<span class="dot">.</span></h1>
    <p class="sign">DAYS · Jakarta &nbsp;·&nbsp; talkaboutdays.com &nbsp;·&nbsp; @talkaboutdays</p>
  </div>
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
