"""Build the DAYS Luwuk Banggai (Central Sulawesi) package proposal as print-ready HTML.

Rebuilt from the Canva draft (DAYS - SULAWESI PACKAGE.pdf) and the team's
package copy, in the approved proposal system: Nature collection, Inter
Tight + JetBrains Mono, English with Bahasa Indonesia, 4:5 pages (A4 edition
via build_a4.py). Where the PDF and the copy differ, the copy wins; price
confirmed separately as IDR 21,950,000.

Run:  python3 build.py && node render.js
"""
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent

# ---------------------------------------------------------------- content

FACTS = [
    ("Destination", "Tujuan", "Luwuk, Banggai, Central Sulawesi"),
    ("Length", "Durasi", "4 days, 3 nights"),
    ("Stay", "Menginap", "Santika Luwuk, 3 nights"),
    ("Flights", "Penerbangan", "Jakarta – Luwuk – Jakarta"),
]
PRICE = "IDR 21,950,000"

DAYS_ = [
    ("Piala &amp; Laumarang Waterfalls", "Air Terjun Piala &amp; Laumarang",
     "Luwuk Airport · Piala Waterfall · Laumarang Waterfall · Santika Luwuk",
     "Our local team meets you at Luwuk Airport and takes you straight into the forest: Piala Waterfall first, then Laumarang. Check in at Santika Luwuk in the afternoon, then dinner.",
     "Disambut tim lokal di Bandara Luwuk, lalu menuju Air Terjun Piala dan Laumarang. Check-in di Santika Luwuk dan makan malam.",
     "Dinner"),
    ("Paisupok", "Paisupok",
     "Harbour · Paisupok · Paisubatango · Pantai Poganda",
     "A speedboat from the harbour to Paisupok, the lake so clear the boats seem to float on air. Swim and explore Paisubatango, lunch and slow beach time at Pantai Poganda, then back to Luwuk.",
     "Speedboat menuju Paisupok yang airnya sebening kaca, berenang di Paisubatango, makan siang dan bersantai di Pantai Poganda, lalu kembali ke Luwuk.",
     "Breakfast · Lunch · Dinner"),
    ("Pulo Dua", "Pulo Dua",
     "Harbour · Pulo Dua · Luwuk",
     "By boat to Pulo Dua. Trek up to the viewpoint for the panorama of green hills and deep blue water, then come down to snorkel. Lunch on the island and sail back to Luwuk.",
     "Naik kapal ke Pulo Dua, trekking ke puncak untuk melihat panorama pulau dan laut, lalu snorkeling. Makan siang dan kembali berlayar ke Luwuk.",
     "Breakfast · Lunch · Dinner"),
    ("Kamumu &amp; departure", "Kamumu &amp; kepulangan",
     "Santika Luwuk · Kamumu Waterfall · Luwuk Airport",
     "Breakfast and check-out, then one last waterfall at Kamumu before the transfer to Luwuk Airport.",
     "Sarapan dan check-out, mampir ke Air Terjun Kamumu, lalu diantar ke Bandara Luwuk.",
     "Breakfast"),
]

HIGHLIGHTS = [
    ("img", "paisupok-boat", "Paisupok", "Crystal-clear water hidden in the green of Banggai. A place to swim, explore and slow right down."),
    ("img", "pulo-dua", "Pulo Dua", "Green hills meet deep blue sea. Trek to the viewpoint for the whole panorama from above."),
    ("img", "piala", "Piala &amp; Laumarang", "Waterfalls tucked into tropical forest, on the wild side of Sulawesi."),
    ("img", "kamumu", "Kamumu Waterfall", "One more glimpse of Banggai’s nature before you fly home."),
]

INCLUDED = [
    ("Getting there", "Perjalanan", ["Return flights from Jakarta", "Private transportation throughout", "Private local guide"]),
    ("Staying &amp; eating", "Menginap &amp; makan", ["3 nights at Santika Luwuk", "Breakfast, lunch and dinner daily"]),
    ("On the water", "Di laut", ["Speedboat to Paisupok", "Boat at Paisupok", "Boat to Pulo Dua"]),
    ("Documentation", "Dokumentasi", ["Drone and mirrorless camera (minimum 8 participants)"]),
]
EXCLUDED = ["Personal expenses", "Meals and drinks outside the package", "Tips for guide and crew", "Anything not listed as included"]

CONTACT = [
    ("WhatsApp / Phone", "+62 812 2000 0185"),
    ("Email", "lets@talkaboutdays.com"),
    ("Instagram", "@talkaboutdays"),
    ("Website", "talkaboutdays.com"),
    ("Studio", "Jl. Tebet Barat IX No. 2, Jakarta Selatan"),
    ("Hours", "Mon–Fri · 09.00–18.00<br>Sat · 11.00–14.00<br>Sun · Closed"),
]

WAVES = '''<svg class="waves" viewBox="0 0 310 112" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" aria-hidden="true">''' + "".join(
    f'<path d="M2 {8+i*22} C 60 {-4+i*22}, 100 {22+i*22}, 155 {10+i*22} S 250 {-4+i*22}, 308 {10+i*22}"/>' for i in range(5)
) + "</svg>"

# ---------------------------------------------------------------- markup

def run(pg):
    return f'''<header class="run">
  <span>DAYS / Nature · Luwuk, Banggai</span>
  <span>Proposal · 2027 · {pg:02d}</span>
</header>'''


def label(en, id_=None):
    return f'<p class="label">{en}{f" <span>· {id_}</span>" if id_ else ""}</p>'


pages = []

# 01 cover
pages.append(f'''<section class="page cover">
  <div class="cover-photo"><img src="img/cover-aerial.jpg" alt="Aerial view of a boat over the reef, Banggai"></div>
  <div class="cover-panel">
    <img class="mark" src="img/days-wordmark-navy.png" alt="DAYS">
    <div class="cover-text">
      {label("Collection · Nature", "Central Sulawesi")}
      <h1>Luwuk<br>Banggai</h1>
      <p class="cover-sub">Where the Wild<br>Meets the Blue</p>
      <p class="id">Tempat alam liar bertemu birunya laut.</p>
    </div>
    <div class="cover-foot">
      {WAVES}
      <dl class="cover-facts">
        <div><dt>Where</dt><dd>Luwuk, Central Sulawesi</dd></div>
        <div><dt>Length</dt><dd>4 days, 3 nights</dd></div>
        <div><dt>Stay</dt><dd>Santika Luwuk</dd></div>
      </dl>
    </div>
  </div>
</section>''')

# 02 introduction
pages.append(f'''<section class="page">
  {run(2)}
  <div class="intro">
    <div>
      {label("Why Luwuk, Banggai", "Mengapa Luwuk, Banggai")}
      <h2 class="display">Room to<br>breathe.</h2>
      <p class="campaign">Ruang untuk menikmati alam.</p>
      <p class="lead">On the eastern arm of Central Sulawesi, Banggai is still a quiet secret: clear lakes under a canopy of green, islands rising out of deep blue water, and waterfalls hidden in the forest.</p>
      <p>Four days to see the best of it at an easy pace. A speedboat to Paisupok, a lake so clear the boats seem to float. A trek to the top of Pulo Dua. Three waterfalls, from Piala and Laumarang to Kamumu. Every evening back to a comfortable room at Santika Luwuk.</p>
      <p>Clear water. Wild islands. Good stories.</p>
      <p class="id">Di lengan timur Sulawesi Tengah, Banggai masih menjadi rahasia: danau sebening kaca, pulau-pulau di tengah laut biru, dan air terjun di dalam hutan. Empat hari untuk menikmatinya dengan santai.</p>
    </div>
    <figure class="intro-img"><img src="img/paisupok-canoe.jpg" alt="A canoe on the clear water of Paisupok"></figure>
  </div>
</section>''')

# 03 the package
hl = "".join(
    f'''<article class="hl-card">{f'<img src="img/{r}.jpg" alt="">' if k == "img" else f'<span class="hl-panel">{WAVES}</span>'}<div><h3>{t}</h3><p>{e(d)}</p></div></article>'''
    for k, r, t, d in HIGHLIGHTS)
pages.append(f'''<section class="page pkg">
  {run(3)}
  <div class="body">
    {label("The package", "Paket perjalanan")}
    <h2 class="h">Luwuk, Banggai</h2>
    <p class="route">Piala <i>·</i> Laumarang <i>·</i> Paisupok <i>·</i> Pulo Dua <i>·</i> Kamumu</p>
    <dl class="fact-grid">{"".join(f'<div><dt>{k} <span>· {i}</span></dt><dd>{e(v)}</dd></div>' for k, i, v in FACTS)}</dl>
    <div class="price">
      <div>{label("Per person", "Per orang")}<p class="amount">{e(PRICE)}</p></div>
      <p>Return flights from Jakarta, three nights at Santika Luwuk, every meal, the boats, a private car and a private local guide, in one clear price.<span class="id">Tiket pesawat pulang-pergi dari Jakarta, tiga malam di Santika Luwuk, semua makan, kapal, mobil pribadi, dan pemandu lokal dalam satu harga.</span></p>
    </div>
    {label("Highlights", "Sorotan")}
    <div class="hls">{hl}</div>
  </div>
</section>''')

# 04 itinerary
rows = "".join(f'''<li class="day">
  <div class="day-n"><span class="n">Day {i}</span><span class="date">{m}</span></div>
  <div>
    <h3>{t}{f' <span>· {ti}</span>' if ti != t else ''}</h3>
    <p class="stops">{s}</p>
    <p>{e(b)}</p>
    <p class="id">{e(bi)}</p>
  </div>
</li>''' for i, (t, ti, s, b, bi, m) in enumerate(DAYS_, 1))
pages.append(f'''<section class="page">
  {run(4)}
  <div class="body">
    {label("Day by day", "Rencana harian")}
    <h2 class="h">Four days in Banggai</h2>
    <p class="lead narrow">Every night at Santika Luwuk, with meals noted under each day.</p>
    <ol class="days">{rows}</ol>
  </div>
</section>''')

# 05 included
cols = "".join(f'''<div class="inc">{label(h, hi)}<ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>''' for h, hi, items in INCLUDED)
pages.append(f'''<section class="page">
  {run(5)}
  <div class="body">
    {label("What’s included", "Termasuk dalam paket")}
    <h2 class="h">We take care of the details.</h2>
    <p class="lead narrow">From the airport on day one to the airport on day four: the flights, the boats, the car and the guide are arranged.</p>
    <div class="incs">{cols}</div>
    <div class="excl">
      {label("Not included", "Tidak termasuk")}
      <p>{" · ".join(e(x) for x in EXCLUDED)}</p>
    </div>
    <aside class="quote">
      {label("Good to know", "Perlu diketahui")}
      <p class="gtk-en" style="font-size:21px;line-height:1.5;color:#2C2C65;margin:0">Your DAYS contact is on WhatsApp before and during the trip. Boat crossings and timings can shift with the weather; the local team decides on the day.</p>
      <p class="id" style="font-size:16px;line-height:1.55;color:#55547F;margin:10px 0 0">Tim DAYS dapat dihubungi lewat WhatsApp sebelum dan selama perjalanan. Jadwal kapal dapat berubah mengikuti cuaca.</p>
    </aside>
  </div>
</section>''')

# 06 get in touch
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
<title>DAYS · Luwuk Banggai 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,800;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>{"".join(pages)}</body></html>'''
(HERE / "proposal.html").write_text(html)
print("wrote proposal.html,", len(pages), "pages")
