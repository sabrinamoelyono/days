"""Build the DAYS Labuan Bajo Sailing 2027 package proposal as print-ready HTML.

Rebuilt from the Canva draft (DAYS - LABUAN BAJO SAILING PACKAGE.pdf) in the
approved proposal system: DAYS Brand Profile layout, Inter Tight + JetBrains
Mono, English with Bahasa Indonesia, 4:5 pages (A4 edition via build_a4.py).

Collection: Nature. Padar, Pink Beach and the Komodo islands are the reason
to go; snorkelling and the boat support the landscape.

Run:  python3 build.py && node render.js
"""
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent

# ---------------------------------------------------------------- content
# Trip facts are carried over verbatim from the original proposal.

FACTS = [
    ("Dates", "Tanggal", "22–24 February 2027"),
    ("Length", "Durasi", "3 days, 2 nights"),
    ("Liveaboard", "Kapal", "Elrora Liveaboard"),
    ("Cabin", "Kabin", "Master Cabin, Main Deck"),
    ("Destination", "Tujuan", "Komodo National Park, Labuan Bajo"),
    ("Capacity", "Kapasitas", "2 guests"),
]
PRICE = "IDR 25,500,000"

DAYS_ = [
    ("22 Feb", "Kelor &amp; Manjarite", "Labuan Bajo · Kelor Island · Manjarite · Kalong Island",
     "Board in Labuan Bajo and sail straight into the park. A short climb on Kelor, a first swim at Manjarite, and dusk at Kalong, when thousands of flying foxes leave the mangroves.",
     "Naik kapal di Labuan Bajo, mendaki singkat di Kelor, berenang di Manjarite, dan senja di Pulau Kalong saat ribuan kalong keluar dari hutan bakau."),
    ("23 Feb", "Padar &amp; Komodo", "Padar Island · Pink Beach · Komodo Island · Taka Makassar · Manta Point",
     "Sunrise on Padar, the view of three bays in one frame. Then the pink sand, the Komodo dragons in their home ground, a sandbar in the middle of the sea at Taka Makassar, and mantas at Manta Point.",
     "Matahari terbit di Padar, Pantai Pink, komodo di habitat aslinya, gosong pasir Taka Makassar, dan pari manta di Manta Point."),
    ("24 Feb", "Sebayur &amp; home", "Sebayur Island · Labuan Bajo Harbour",
     "A last swim and snorkel at Sebayur, then back to Labuan Bajo harbour and the airport.",
     "Berenang dan snorkeling terakhir di Sebayur, lalu kembali ke pelabuhan Labuan Bajo dan bandara."),
]

INCLUDED = [
    ("On board", "Di kapal", ["2 nights aboard Elrora Liveaboard", "Master Cabin, Main Deck", "Free Wi-Fi on board", "Speaker and karaoke set"]),
    ("Food &amp; drink", "Makan &amp; minum", ["Welcome drinks", "Breakfast, lunch and dinner daily", "Afternoon snacks daily", "Free-flow water, coffee and tea"]),
    ("In the water", "Di laut", ["Snorkelling equipment", "Paddle board"]),
    ("Taken care of", "Sudah kami urus", ["Airport pick-up and drop-off", "Professional tour guide", "Photos and video by camera, drone and GoPro"]),
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
  <span>DAYS / Nature · Labuan Bajo</span>
  <span>Proposal · February 2027 · {pg:02d}</span>
</header>'''


def label(en, id_=None):
    return f'<p class="label">{en}{f" <span>· {id_}</span>" if id_ else ""}</p>'


pages = []

# 01 cover
pages.append(f'''<section class="page cover">
  <div class="cover-photo"><img src="img/padar-cover.jpg" alt="Padar Island from the ridge, Komodo National Park"></div>
  <div class="cover-panel">
    <img class="mark" src="img/days-wordmark-navy.png" alt="DAYS">
    <div class="cover-text">
      {label("Collection · Nature", "Sailing")}
      <h1>Labuan<br>Bajo</h1>
      <p class="cover-sub">Beyond the Shore,<br>Into the Blue</p>
      <p class="id">Melampaui pantai, menuju birunya laut.</p>
    </div>
    <div class="cover-foot">
      {WAVES}
      <dl class="cover-facts">
        <div><dt>Dates</dt><dd>22–24 February 2027</dd></div>
        <div><dt>Length</dt><dd>3 days, 2 nights</dd></div>
        <div><dt>Aboard</dt><dd>Elrora Liveaboard</dd></div>
      </dl>
    </div>
  </div>
</section>''')

# 02 introduction
pages.append(f'''<section class="page">
  {run(2)}
  <div class="intro">
    <div>
      {label("Why Labuan Bajo", "Mengapa Labuan Bajo")}
      <h2 class="display">Room to<br>breathe.</h2>
      <p class="campaign">Ruang untuk menikmati alam.</p>
      <p class="lead">Komodo is best seen from the water. Three days on a phinisi, moving between islands at the pace of the sea.</p>
      <p>You wake up anchored off a different island each morning: Padar’s ridges at sunrise, sand that really is pink, and the only place on earth where Komodo dragons live in the wild. The days are for swimming, snorkelling and climbing to the views; the evenings are for the deck.</p>
      <p>Close enough to Jakarta and Bali for a long weekend, far enough to feel like somewhere else entirely.</p>
      <p class="id">Komodo paling indah dinikmati dari laut. Tiga hari di atas kapal phinisi, berpindah dari pulau ke pulau mengikuti ritme laut: Padar saat matahari terbit, Pantai Pink, dan komodo di habitat aslinya.</p>
    </div>
    <figure class="intro-img"><img src="img/pink-beach.jpg" alt="Pink Beach from above"></figure>
  </div>
</section>''')

# 03 the package
pages.append(f'''<section class="page pkg">
  {run(3)}
  <div class="body">
    {label("The package", "Paket perjalanan")}
    <h2 class="h">Komodo by sea</h2>
    <p class="route">Kelor <i>·</i> Manjarite <i>·</i> Padar <i>·</i> Pink Beach <i>·</i> Komodo <i>·</i> Sebayur</p>
    <dl class="fact-grid">{"".join(f'<div><dt>{k} <span>· {i}</span></dt><dd>{e(v)}</dd></div>' for k, i, v in FACTS)}</dl>
    <div class="price">
      <div>{label("Per person", "Per orang")}<p class="amount">{e(PRICE)}</p></div>
      <p>Two nights in the master cabin, every meal on board, the guide, the gear and your airport transfers, in one clear price.<span class="id">Dua malam di master cabin, semua makan di kapal, pemandu, perlengkapan, dan antar-jemput bandara dalam satu harga.</span></p>
    </div>
    <figure class="wide"><img src="img/padar-view.jpg" alt="The three bays of Padar Island"></figure>
  </div>
</section>''')

# 04 itinerary
rows = "".join(f'''<li class="day">
  <div class="day-n"><span class="n">Day {i}</span><span class="date">{d}</span></div>
  <div>
    <h3>{t}</h3>
    <p class="stops">{s}</p>
    <p>{e(b)}</p>
    <p class="id">{e(bi)}</p>
  </div>
</li>''' for i, (d, t, s, b, bi) in enumerate(DAYS_, 1))
pages.append(f'''<section class="page">
  {run(4)}
  <div class="body">
    {label("Day by day", "Rencana harian")}
    <h2 class="h">Three days at sea</h2>
    <p class="lead narrow">Islands and timings follow the tide and the weather on the day; your guide sets the order to get the best of each stop.</p>
    <ol class="days">{rows}</ol>
    <figure class="wide itin-img"><img src="img/pink-beach.jpg" alt="Pink Beach from above"></figure>
  </div>
</section>''')

# 05 the boat
pages.append(f'''<section class="page">
  {run(5)}
  <div class="body">
    {label("The boat", "Kapal")}
    <h2 class="h">Elrora Liveaboard</h2>
    <p class="lead narrow">A traditional wooden phinisi with shaded lounges, an open bow for sunbathing, and a long table on deck for dinner under the sky.</p>
    <p class="id narrow">Kapal phinisi kayu tradisional dengan lounge teduh, haluan terbuka untuk berjemur, dan meja makan panjang di dek.</p>
    <div class="boat-grid">
      <img class="b1" src="img/phinisi-sail.jpg" alt="The phinisi under sail">
      <img class="b2" src="img/deck-bow.jpg" alt="Sun deck at the bow">
      <img class="b3" src="img/deck-lounge.jpg" alt="Shaded deck lounge">
      <img class="b4" src="img/deck-dining.jpg" alt="Dining table on deck">
    </div>
  </div>
</section>''')

# 06 the cabin
pages.append(f'''<section class="page">
  {run(6)}
  <div class="body">
    {label("Your cabin", "Kabin Anda")}
    <h2 class="h">Master Cabin, Main Deck</h2>
    <p class="lead narrow">The boat’s best room: a large bed, wide windows onto the water, a private balcony and a bathtub with a view.</p>
    <p class="id narrow">Kabin terbaik di kapal: tempat tidur besar, jendela lebar menghadap laut, balkon pribadi, dan bathtub dengan pemandangan.</p>
    <div class="gallery">
      <img class="g-main" src="img/cabin-main.jpg" alt="The master cabin">
      <img src="img/cabin-balcony.jpg" alt="Private balcony">
      <img src="img/cabin-bath.jpg" alt="Bathtub with a sea view">
    </div>
  </div>
</section>''')

# 07 included
cols = "".join(f'''<div class="inc">{label(h, hi)}<ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>''' for h, hi, items in INCLUDED)
pages.append(f'''<section class="page">
  {run(7)}
  <div class="body">
    {label("What’s included", "Termasuk dalam paket")}
    <h2 class="h">We take care of the details.</h2>
    <p class="lead narrow">From pick-up at Komodo Airport to drop-off three days later, the plan is ours. Even the photos: the crew shoots on camera, drone and GoPro.</p>
    <div class="incs">{cols}</div>
    <aside class="quote">
      {label("Good to know", "Perlu diketahui")}
      <p class="gtk-en" style="font-size:21px;line-height:1.5;color:#2C2C65;margin:0">Your DAYS contact is on WhatsApp before and during the trip. Islands and timings can shift with the tide and weather; the guide and crew decide on the day.</p>
      <p class="id" style="font-size:16px;line-height:1.55;color:#55547F;margin:10px 0 0">Tim DAYS dapat dihubungi lewat WhatsApp sebelum dan selama perjalanan. Urutan pulau dan waktu dapat berubah mengikuti pasang surut dan cuaca.</p>
    </aside>
  </div>
</section>''')

# 08 get in touch
rows = "".join(f"<div><dt>{e(k)}</dt><dd>{v if k == 'Hours' else e(v)}</dd></div>" for k, v in CONTACT)
pages.append(f'''<section class="page closing">
  <img class="mark" src="img/days-wordmark-orange.png" alt="DAYS">
  <div class="closing-main">
    {label("Get in touch", "Hubungi kami")}
    <h2 class="display">Let’s plan your<br>next DAYS.</h2>
    <p class="campaign">Yuk, rencanakan perjalananmu.</p>
    <dl class="contact">{rows}</dl>
  </div>
  <p class="foot">PT Vakansi Media Global · Licensed travel agency · Jakarta Selatan</p>
</section>''')

css = (HERE / "proposal.css").read_text()
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>DAYS · Labuan Bajo Sailing 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,800;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>{"".join(pages)}</body></html>'''
(HERE / "proposal.html").write_text(html)
print("wrote proposal.html,", len(pages), "pages")
