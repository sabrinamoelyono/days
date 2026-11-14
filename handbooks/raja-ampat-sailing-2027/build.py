"""Build the DAYS Raja Ampat Sailing 2027 package proposal as print-ready HTML.

Rebuilt from the Canva draft (RAJA_AMPAT_SAILING_PACKAGE.pdf) in the same
system as the Raja Ampat proposal: DAYS Brand Profile 2027 layout, set in
Inter Tight + JetBrains Mono, English with Bahasa Indonesia, 4:5 pages.

Collection: Sports. With ~20 dives and an Advanced Open Water requirement,
the activity is the reason to travel (Brand Profile, brand architecture).

Run:  python3 build.py && node render.js
"""
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent

# ---------------------------------------------------------------- content
# Trip facts are carried over verbatim from the original proposal.

FACTS = [
    ("Duration", "Durasi", "8 days, 7 nights"),
    ("Liveaboard", "Kapal", "Amaya Explorer"),
    ("Route", "Rute", "Sorong – Waisai – Central Raja Ampat – Sorong"),
    ("Diving", "Penyelaman", "Approximately 20 dives"),
]
QUAL = "Advanced Open Water, with a minimum of 20 logged dives"
PRICE = "IDR 139,900,000"

DAYS_ = [
    ("Sorong to Waisai", "Sorong ke Waisai", "Sorong Harbour · Waisai"),
    ("Piaynemo", None, "Piaynemo · Melissa Garden · Rufus · My Reef · Galaxy"),
    ("Gam Island", "Pulau Gam", "Gam Island · Citrus Ridge · Mayhem · Gam Corner"),
    ("Dampier Strait", "Selat Dampier", "Manta Sandy · Yenbuba Jetty"),
    ("Mansuar Island", "Pulau Mansuar", "Sawandarek · Cape Kri · Chicken Reef · Sapokren"),
    ("Dampier Strait", "Selat Dampier", "Blue Magic · Cape Mansuar · Mioskon"),
    ("Central Raja Ampat", "Raja Ampat Tengah", "Blue Magic · Mioskon · Mayalibit Bay · Kali Biru"),
    ("Sorong &amp; departure", "Sorong &amp; kepulangan", "Sorong Harbour · Sorong Airport"),
]

INCLUDED = [
    ("Getting there", "Perjalanan", ["Return flights", "Shore–vessel transfers at check-in and check-out"]),
    ("On board", "Di kapal", ["7 nights aboard Amaya Explorer", "All onboard meals",
                              "Snacks, tea, coffee, mineral water and refreshments (alcohol not included)"]),
    ("Diving &amp; activities", "Selam &amp; aktivitas", ["3–4 dives a day (except the first and last day, subject to itinerary)",
                                                    "Shore excursions as outlined in the itinerary",
                                                    "Sea kayaks and stand-up paddle boards (subject to local regulations)"]),
    ("Crew", "Kru", ["English-speaking cruise director", "Professional onboard crew"]),
]

CONTACT = [
    ("WhatsApp / Phone", "+62 812 2000 0185"),
    ("Email", "lets@talkaboutdays.com"),
    ("Instagram", "@talkaboutdays"),
    ("Website", "talkaboutdays.com"),
    ("Studio", "Jl. Tebet Barat IX No. 2, Jakarta Selatan"),
    ("Hours", "Mon–Fri · 09.00–18.00<br>Sat · 11.00–14.00<br>Sun · Closed"),
]

# Sports collection motif: diagonal stripes, as in the Brand Profile.
STRIPES = '<svg class="waves" viewBox="0 0 240 90" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true">' + "".join(
    f'<path d="M{4+i*36} 88 L{40+i*36} 2"/>' for i in range(6)) + "</svg>"

# ---------------------------------------------------------------- markup

def run(pg):
    return f'''<header class="run">
  <span>DAYS / Sports · Raja Ampat by sea</span>
  <span>Proposal · 2027 · {pg:02d}</span>
</header>'''


def label(en, id_=None):
    return f'<p class="label">{en}{f" <span>· {id_}</span>" if id_ else ""}</p>'


pages = []

# 01 cover — Sports collection panel under the hero
pages.append(f'''<section class="page cover sports">
  <div class="cover-photo"><img src="img/phinisi-hero.jpg" alt="A traditional phinisi under sail"></div>
  <div class="cover-panel">
    <img class="mark" src="img/days-wordmark-navy.png" alt="DAYS">
    <div class="cover-text">
      {label("Collection · Sports", "Liveaboard")}
      <h1>Raja<br>Ampat</h1>
      <p class="cover-sub">Sail Beyond the Ordinary</p>
      <p class="id">Berlayar melampaui yang biasa.</p>
    </div>
    <div class="cover-foot">
      {STRIPES}
      <dl class="cover-facts">
        <div><dt>Length</dt><dd>8 days, 7 nights</dd></div>
        <div><dt>Aboard</dt><dd>Amaya Explorer</dd></div>
        <div><dt>Diving</dt><dd>~20 dives</dd></div>
      </dl>
    </div>
  </div>
</section>''')

# 02 sail with DAYS
pages.append(f'''<section class="page">
  {run(2)}
  <div class="body">
    {label("Sail with DAYS", "Berlayar bersama DAYS")}
    <h2 class="display">Be there.<br>Be part of it.</h2>
    <p class="campaign">Saksikan aksinya. Rasakan serunya.</p>
    <div class="cols">
      <div>
        <p class="lead">Some places are best seen from the water. Raja Ampat is one of them.</p>
        <p>Together with Amaya Explorer Indonesia – Phinisi Archipelago, we’ve planned eight days aboard a traditional phinisi through the centre of Raja Ampat: around twenty dives across Piaynemo, Gam, the Dampier Strait and Mansuar, with the boat as your base between them.</p>
        <p>It’s a chance to slow down, switch off, and see Indonesia from a different angle.</p>
      </div>
      <div>
        <p class="id">Bersama Amaya Explorer Indonesia – Phinisi Archipelago, kami merancang delapan hari di atas kapal phinisi tradisional melintasi Raja Ampat bagian tengah: sekitar dua puluh kali penyelaman di Piaynemo, Gam, Selat Dampier, dan Mansuar.</p>
        <p class="pull">Beyond the destination, it’s about the journey.</p>
      </div>
    </div>
    <figure class="wide tall"><img src="img/boat-anchor.jpg" alt="Amaya Explorer at anchor"></figure>
  </div>
</section>''')

# 03 the boat
pages.append(f'''<section class="page">
  {run(3)}
  <div class="body">
    {label("The boat", "Kapal")}
    <h2 class="h">Amaya Explorer</h2>
    <p class="lead narrow">A 35-metre phinisi, built by hand in Bulukumba, South Sulawesi, by craftsmen carrying on generations of boatbuilding. Two years in the making.</p>
    <div class="cols">
      <p>The crew comes from across Indonesia, experienced on the water and ready for whatever the day needs. Diving leads, but it isn’t the only way to spend the day: stand-up paddling, kayaking, snorkelling, freediving and yoga are all on board.</p>
      <p class="id">Phinisi sepanjang 35 meter, dibuat tangan oleh pengrajin di Bulukumba, Sulawesi Selatan. Selain menyelam, tersedia paddle board, kayak, snorkeling, freediving, dan yoga.</p>
    </div>
    <div class="boat-grid">
      <img class="b1" src="img/deck-lounge.jpg" alt="Shaded deck lounge">
      <img class="b2" src="img/boat-aerial.jpg" alt="Amaya Explorer from above">
      <img class="b3" src="img/dive-deck.jpg" alt="Dive deck with tanks">
      <img class="b4" src="img/diver.jpg" alt="A diver gearing up">
      <img class="b5" src="img/dining.jpg" alt="Dinner table set on board">
      <img class="b6" src="img/crew.jpg" alt="Crew on deck">
    </div>
  </div>
</section>''')

# 04 the package
pages.append(f'''<section class="page page4">
  {run(4)}
  <div class="body">
    {label("The package", "Paket perjalanan")}
    <h2 class="h">Raja Ampat Central</h2>
    <p class="route">Piaynemo <i>·</i> Gam Island <i>·</i> Dampier Strait <i>·</i> Mansuar Island <i>·</i> Kali Biru</p>
    <dl class="fact-grid">{"".join(f'<div><dt>{k} <span>· {i}</span></dt><dd>{e(v)}</dd></div>' for k, i, v in FACTS)}</dl>
    <div class="notice">
      {label("Who it’s for", "Syarat peserta")}
      <p><strong>{e(QUAL)}.</strong> The dives are planned for experienced divers.</p>
      <p class="id">Minimal sertifikasi Advanced Open Water dengan 20 log penyelaman.</p>
    </div>
    <div class="price">
      <div>{label("Per person", "Per orang")}<p class="amount">{e(PRICE)}</p></div>
      <p>Flights, seven nights on board, every meal, the diving and the crew, in one clear price.<span class="id">Tiket pesawat, tujuh malam di kapal, makan, penyelaman, dan kru dalam satu harga.</span></p>
    </div>
    <figure class="wide"><img src="img/piaynemo.jpg" alt="The Piaynemo islands"></figure>
  </div>
</section>''')

# 05 eight days
rows = "".join(f'''<li>
  <span class="num">Day {i}</span>
  <div><h3>{t}{f' <span>· {ti}</span>' if ti else ''}</h3><p class="stops">{s}</p></div>
</li>''' for i, (t, ti, s) in enumerate(DAYS_, 1))
pages.append(f'''<section class="page">
  {run(5)}
  <div class="body">
    {label("Day by day", "Rencana harian")}
    <h2 class="h">Eight days at sea</h2>
    <p class="lead narrow">Three to four dives a day, with the first and last day for boarding and the trip home. Dive sites are subject to conditions on the day.</p>
    <ol class="dives">{rows}</ol>
    <figure class="wide short"><img src="img/lagoon.jpg" alt="A lagoon in Raja Ampat"></figure>
  </div>
</section>''')

# 06 included
cols = "".join(f'''<div class="inc">{label(h, hi)}<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>''' for h, hi, items in INCLUDED)
pages.append(f'''<section class="page">
  {run(6)}
  <div class="body">
    {label("What’s included", "Termasuk dalam paket")}
    <h2 class="h">We take care of the details.</h2>
    <p class="lead narrow">You bring your certification and logbook. The boat, the crew and the plan are ours.</p>
    <div class="incs">{cols}</div>
    <aside class="quote">
      {label("Good to know", "Perlu diketahui")}
      <p class="gtk-en" style="font-size:21px;line-height:1.5;color:#2C2C65;margin:0">Your DAYS contact is on WhatsApp before and during the trip. Dive sites can change with conditions; the cruise director decides on the day.</p>
      <p class="id" style="font-size:16px;line-height:1.55;color:#55547F;margin:10px 0 0">Tim DAYS dapat dihubungi lewat WhatsApp sebelum dan selama perjalanan. Titik selam dapat berubah mengikuti kondisi laut.</p>
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
  <p class="foot">PT Vakansi Media Global · Licensed travel agency · In partnership with Amaya Explorer Indonesia</p>
</section>''')

css = (HERE / "proposal.css").read_text()
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>DAYS · Raja Ampat Sailing 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,800;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>{"".join(pages)}</body></html>'''
(HERE / "proposal.html").write_text(html)
print("wrote proposal.html,", len(pages), "pages")
