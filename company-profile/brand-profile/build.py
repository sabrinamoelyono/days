"""Build the DAYS Brand Profile (2027) as print-ready HTML.

Rebuilt from DAYS-Brand-Profile.pdf with the same layout, colour, imagery
and copy, set in the DAYS type pair: Inter Tight for display and body,
JetBrains Mono for labels, figures and dates (as in DESIGN.md).

Run:  python3 build.py && node render.js
"""
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent

# ---------------------------------------------------------------- motifs
# One line motif per collection, drawn in currentColor.

MOTIF = {
    "city": '<svg viewBox="0 0 240 90" fill="none" stroke="currentColor" stroke-width="2.6">'
            '<path d="M2 2H238V30"/><path d="M12 12H226V40"/>'
            + "".join(f'<path d="M{x} 12V88"/>' for x in (12, 40, 68, 96, 124, 152, 180, 208))
            + '<path d="M2 2V88"/></svg>',
    "nature": '<svg viewBox="0 0 240 90" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round">'
              + "".join(f'<path d="M2 {8+i*17} C 60 {-4+i*17}, 100 {22+i*17}, 150 {8+i*17} S 210 {-2+i*17}, 238 {10+i*17}"/>' for i in range(5))
              + "</svg>",
    "sports": '<svg viewBox="0 0 240 90" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round">'
              + "".join(f'<path d="M{4+i*36} 88 L{40+i*36} 2"/>' for i in range(6)) + "</svg>",
    "culinary": '<svg viewBox="0 0 240 130" fill="none" stroke="currentColor" stroke-width="2.6">'
                + "".join(f'<path d="M{6+i*16} 128 V{120-0} A {114-i*16} {114-i*16} 0 0 1 {234-i*16} 120 V128"/>' for i in range(3))
                + "</svg>",
    "music": '<svg viewBox="0 0 240 110" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round">'
             + "".join(f'<path d="M{6+i*22} {55-h} V{55+h}"/>' for i, h in enumerate((10, 22, 14, 26, 36, 22, 12, 30, 20, 34, 12)))
             + "</svg>",
}

COLLECTIONS = [
    # key, name, panel class, wordmark, line, desc, desc_id, experiences, extra (label, value), campaign
    ("city", "City", "wordmark-cream", "A city.<br>Your pace.",
     "For travelers who follow their curiosity through neighborhoods, culture and the city after dark.",
     "Untuk penjelajah yang ingin mengenal sudut kota, budaya lokal, dan suasana selepas senja.",
     "Tokyo neighborhood walk · Bangkok after dark · Melbourne city break",
     ("Featured places", "New York · Bangkok · Tokyo"), "Jelajahi kota, sesuai ritmemu."),
    ("nature", "Nature", "wordmark-navy", "Room to<br>breathe.",
     "For journeys where the landscape is the reason to go, with time to appreciate the view.",
     "Untuk perjalanan yang menjadikan keindahan alam sebagai tujuan utama, dengan waktu untuk menikmatinya.",
     "Lakeside escape · Mountain scenery · Coastal hideaway",
     None, "Ruang untuk menikmati alam."),
    ("sports", "Sports", "wordmark-navy", "Be there.<br>Be part of it.",
     "For the thrill of being in the crowd or taking part: iconic events and active escapes.",
     "Untuk merasakan semangat dari tribun maupun ikut beraksi lewat perjalanan aktif.",
     "F1 weekend · Australian Open · Ski trip · Surf escape · Hiking trip",
     ("Track record", "Niseko ski open trip, winter 2024–25"), "Saksikan aksinya. Rasakan serunya."),
    ("culinary", "Culinary, Leisure &amp; Wellbeing", "wordmark-navy", "Take your<br>time.",
     "For good food, unhurried stays and time to feel restored. Discovery with a gentler pace.",
     "Untuk menikmati kuliner, bersantai, dan kembali segar. Menemukan hal baru dengan ritme yang lebih tenang.",
     "Culinary journey · Slow resort stay · Spa and wellbeing escape",
     None, "Nikmati tanpa terburu-buru."),
    ("music", "Music Festival", "wordmark-yellow", "Follow<br>the sound.",
     "For journeys shaped by music, from the first set to the last shared memory.",
     "Untuk perjalanan yang mengikuti irama musik, dari penampilan pertama hingga kenangan yang dibawa pulang.",
     "Festival weekend · Multi-stage discovery · Music and city journey",
     ("Track record", "Amsterdam Dance Event, every year since 2022 · Primavera Sound, Barcelona 2027"),
     "Ikuti musiknya. Nikmati momennya."),
]

TILE_LABEL = {"music": "Music Festival", "city": "City", "nature": "Nature", "sports": "Sports",
              "culinary": "Culinary, Leisure &amp; Wellbeing"}

# Music Festival is the lead collection: it comes first everywhere.
COLLECTIONS = COLLECTIONS[-1:] + COLLECTIONS[:-1]

pages = []

# ---------------------------------------------------------------- 01 cover
tiles = "".join(f'<div class="tile t-{k}"><span class="motif">{MOTIF[k]}</span><span class="lbl">{TILE_LABEL[k]}</span></div>' for k in TILE_LABEL)
pages.append(f'''<section class="page g-cover">
  <div class="topline"><span>DAYS / Company profile</span><span>Jakarta · 2027</span></div>
  <img class="cover-mark" src="img/wordmark-orange.png" alt="DAYS">
  <div class="cover-grid">
    <div>
      <h1 class="cover-h">Experience-driven travel media and global connector between Indonesia and Europe.</h1>
      <p class="id cover-id">Media perjalanan berbasis pengalaman dan penghubung global antara Indonesia dan Eropa.</p>
    </div>
    <p class="cover-body">DAYS is a Jakarta travel company that plans journeys around the reason you want to go: a festival, a race weekend, a city, a view or a long lunch. We handle the details, including visas and passports, and leave room for the moments that make a trip yours.</p>
  </div>
  <p class="label">One brand. Five ways to go.</p>
  <div class="tiles">{tiles}</div>
  <p class="label photos-label">Highlights in Europe <span>· Sorotan di Eropa</span></p>
  <div class="cover-photos">
    <figure class="ph w2"><img src="img/primavera.jpg" alt=""><figcaption>Primavera Sound · Barcelona</figcaption></figure>
    <figure class="ph"><img src="img/barcelona.jpg" alt=""><figcaption>Barcelona</figcaption></figure>
    <figure class="ph w15"><img src="img/ade.jpg" alt=""><figcaption>ADE · Amsterdam</figcaption></figure>
  </div>
</section>''')

# ---------------------------------------------------------------- 02 who we are
side = [("Based in", "Jakarta Selatan"), ("Who we travel with", "Families, friends, solo travelers and groups"),
        ("What we plan", "Five collections, four services"), ("Languages", "English and Bahasa Indonesia"),
        ("Personality", "Curious · Warm · Confident · Considered"),
        ("Company", "PT Vakansi Media Global · est. 2024 · licensed travel agency")]
stats = [("5×", "Amsterdam Dance Event, every year 2022–2026"), ("1,000+", "visa applications processed since 2024"),
         ("97–98%", "visa approval rate"), ("2018", "handling visas and travel since")]
pages.append(f'''<section class="page g-who">
  <p class="label">Who we are</p>
  <div class="who-grid">
    <div>
      <h2 class="h">Travel with personality.</h2>
      <p class="sub">Perjalanan dengan karakter.</p>
      <p><strong>Exploring travel, culture, and the days worth talking about.</strong> DAYS plans premium, approachable journeys for Indonesian travelers aged 25–55. Every trip is designed around interests, thoughtful choices and the people you travel with.</p>
      <p>Our voice is curious, warm, confident and considered: specific, useful language from people who have been there first.</p>
      <p class="id">Keluarga, teman, solo traveler, dan grup. Gaya perjalanan boleh berbeda; perhatian terhadap pengalaman tetap sama.</p>
      <p class="promise">Our promise: make it feel personal, make the details clear, and leave room for the unexpected moments that make a trip yours.</p>
      <div class="stats">{"".join(f'<div class="card"><p class="stat">{e(n)}</p><p>{e(t)}</p></div>' for n, t in stats)}</div>
    </div>
    <dl class="side">{"".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in side)}</dl>
  </div>
  <div class="card why">
    <p class="label">Why book with DAYS</p>
    <div>
      <p class="quote">“We are not just agents; we’ve tested and vetted every aspect of the cities we suggest.”</p>
      <p>Our team has years of experience managing visa applications and has personally explored the destinations we recommend, so every suggestion comes from first-hand knowledge rather than a brochure.</p>
    </div>
    <div>
      <p class="label">Indonesia ↔ Europe</p>
      <p><strong>ADE 2026 Asia Hub panel, Amsterdam.</strong> Sabrina Moelyono spoke on “Connecting the Dots”, on regional scenes and touring across South Korea, Thailand and Indonesia (22 October 2026).</p>
      <p><strong>Nusantara Elsewhere, Jakarta.</strong> A pre-event talk leading up to the ADE 2026 departure, bringing Jakarta’s scene into the conversation.</p>
    </div>
  </div>
</section>''')

# ---------------------------------------------------------------- 03 architecture
arch = [("A festival trip with restaurants and sightseeing", "music", "Music Festival", "Music is the anchor; City and Culinary are secondary."),
        ("Skiing, surfing or a hiking-focused trip", "sports", "Sports", "The activity is the reason to travel."),
        ("A mountain or coastal scenery escape", "nature", "Nature", "The landscape and slower discovery lead."),
        ("A food-led city break or a spa retreat", "culinary", "Culinary, Leisure &amp; Wellbeing", "Food, rest or restoration shapes the itinerary."),
        ("A city break that includes one concert", "city", "City", "The city experience remains the main draw.")]
pages.append(f'''<section class="page g-arch">
  <p class="label">Brand architecture</p>
  <h2 class="h">One DAYS. Five collections.</h2>
  <p class="sub narrow">Satu DAYS, lima cara berangkat. The wordmark stays constant; the color and collection name tell travelers what kind of trip it is.</p>
  <h3 class="h3">Let the reason for the trip lead.</h3>
  <p class="narrow">Every trip gets one primary collection, chosen by its main motivation. Other experiences on the itinerary appear as supporting interests.</p>
  <table class="arch">
    <thead><tr><th>The trip</th><th>Leading collection</th><th>Why</th></tr></thead>
    <tbody>{"".join(f'<tr><td>{e(t)}</td><td><i class="sq t-{k}"></i><strong>{n}</strong></td><td>{e(w)}</td></tr>' for t, k, n, w in arch)}</tbody>
  </table>
</section>''')

# ---------------------------------------------------------------- 04–08 collections
for key, name, mark, line, desc, desc_id, exp, extra, camp in COLLECTIONS:
    extra_html = f'<p class="label sm">{e(extra[0])}</p><p>{e(extra[1])}</p>' if extra else ""
    pages.append(f'''<section class="page coll g-{key}">
  <div class="panel t-{key}">
    <img class="panel-mark" src="img/{mark}.png" alt="DAYS">
    <p class="panel-line">{line}</p>
    <span class="panel-motif">{MOTIF[key]}</span>
  </div>
  <div class="coll-body">
    <p class="label">Collection · {name}</p>
    <h2 class="h2">{name}</h2>
    <p>{e(desc)}</p>
    <p class="id">{e(desc_id)}</p>
    <div class="coll-meta">
      <p class="label sm">Experiences</p><p>{e(exp)}</p>
      {extra_html}
      <p class="label sm">Campaign line</p><p class="camp">{e(camp)}</p>
    </div>
  </div>
</section>''')

# ---------------------------------------------------------------- 09 services
services = [
    ("Music Festival", "Festival Experience", "Journeys to the world’s most iconic festivals, from high-energy dance events to laid-back classical programs.",
     ["Front-row access to favorite artists and events", "Exclusive offers and perks", "Travel planned around the lineup"]),
    ("Culinary, Leisure &amp; Wellbeing", "Culinary &amp;<br>Leisure Journey", "Gourmet experiences paired with unhurried downtime, tailored to your taste.",
     ["The finest local dining spots and exclusive food tours", "Cooking classes led by renowned chefs", "Optional wellness activities or a spa weekend"]),
    ("Any collection", "Personalized Itinerary", "Bespoke plans for adventures, cultural immersion or a simple getaway. Our travel expert handles everything from A to Z.",
     ["Accommodation, activities and transport", "Pre-departure arrangements", "Already have a plan? We’ll perfect it, down to the brunch reservation"]),
    ("Every trip", "Visa &amp; Passport Services", "Guidance through every step of the visa application and passport renewal, so your documents are in order and you can focus on the trip.",
     ["Visa application support", "Passport renewals", "Document checks before you fly"]),
]
steps = [("Start with the reason", "We match your trip to one leading collection, then add the interests around it."),
         ("Plan the details", "Stays, activities, transfers and reservations, with room for rest and personal preferences."),
         ("Sort the paperwork", "Visa applications and passport renewals are timed to your departure."),
         ("Travel with a clear plan", "A bilingual A4 itinerary: cover, day-by-day plan and a useful-details page with confirmed bookings and meeting points.")]
pages.append(f'''<section class="page g-serv">
  <p class="label">Services</p>
  <h2 class="h">What we take care of.</h2>
  <p class="sub">Dari ide perjalanan sampai urusan dokumen.</p>
  <div class="services">{"".join(f'<div class="svc"><p class="label sm">{k}</p><h3 class="h4">{t}</h3><p>{e(d)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in li)}</ul></div>' for k, t, d, li in services)}</div>
  <div class="visa">
    <div class="card"><p class="label sm">Schengen Area</p><p class="big">~15 working days</p><p>Typical visa processing time</p></div>
    <div class="card"><p class="label sm">Australia</p><p class="big">48 hours – 3 months</p><p>Typical visa processing time</p></div>
    <div class="card"><p class="label sm">Good to know</p><p>Processing times vary by embassy or consular service and can lengthen in high season. We plan applications around your departure date.</p></div>
  </div>
  <div class="steps">{"".join(f'<div><p class="label sm step">Step {i}</p><h4>{e(t)}</h4><p>{e(d)}</p></div>' for i, (t, d) in enumerate(steps, 1))}</div>
</section>''')

# ---------------------------------------------------------------- 10 open trips
trips = [("music", "Music Festival", "ade", "ADE 2022–2026", "Amsterdam, Netherlands · every October",
          "Five days and five nights when the city never sleeps: more than 1,000 events in nearly 200 locations. DAYS has taken a group every year since 2022, five editions running."),
         ("city", "City", "seoul", "Seoul: Soft Days", "Seoul, South Korea · 5 days 4 nights",
          "A girls trip to Seoul: shopping in Seongsu-dong and Hannam-dong, cafés worth the queue, a facial and skin consultation, and good food every night."),
         ("sports", "Sports", "niseko", "Ski Trip 2024–25", "Niseko, Japan · Dec 2024 – Feb 2025",
          "Led by an avid skier who has arranged snow trips in Japan since 2018. Open to all ski levels.")]
journal = [("Japan with Home Gravity", "Japan"), ("Jakarta through Reikko’s sound", "Jakarta"), ("Amsterdam through ADE", "Amsterdam"),
           ("Amsterdam through Goldie’s Craft", "Amsterdam"), ("Los Angeles through Danny’s Mudshop", "Los Angeles")]
pages.append(f'''<section class="page g-trips">
  <p class="label">Selected open trips</p>
  <h2 class="h">Days we’ve already talked about.</h2>
  <p class="sub">Open trips combine flexibility with curated experiences, and travelers join as a group.</p>
  <div class="trips">{"".join(f'<article class="card trip"><img src="img/{img}.jpg" alt=""><div><span class="chip t-{k}">{c}</span><h3 class="h4">{e(t)}</h3><p class="where">{e(w)}</p><p>{e(d)}</p></div></article>' for k, c, img, t, w, d in trips)}</div>
  <div class="journal">
    <div><p class="label sm">Travel journal</p><h3 class="h4">Cities Unwrapped</h3><p>Destinations told through the people, sounds and craft that shape them.</p></div>
    <ul>{"".join(f'<li><span>{e(t)}</span><span class="label sm">{e(p)}</span></li>' for t, p in journal)}</ul>
  </div>
</section>''')

# ---------------------------------------------------------------- 11 trusted by
logos = ["bni", "lokon-capital", "terralogiq", "prawira-indodharma", "mozio", "cikal", "metinca", "leveltujuh", "superstars", "imagineka"]
cells = "".join(
    f'<div class="logo"><img src="img/logo-{l}.png" alt="">' + ('<span>PT Metinca<br>Prima<br>Industrial<br>Works</span>' if l == "metinca" else "") + "</div>"
    for l in logos)
pages.append(f'''<section class="page g-trust">
  <p class="label">Trusted by</p>
  <h2 class="h">Companies we’ve worked with.</h2>
  <p class="sub">Companies and institutions whose teams we’ve handled visas and travel for.</p>
  <div class="logos">{cells}</div>
</section>''')

# ---------------------------------------------------------------- 12 team
team = [("sabrina", "Sabrina Moelyono", "Founder &amp; CEO"), ("ika", "Ika Putri", "Head of Operations"),
        ("anindita", "Anindita S Jati", "Head of Partnership"), ("danica", "Danica Evani", "Head of Creative")]
pages.append(f'''<section class="page g-team">
  <p class="label">Team</p>
  <h2 class="h">Women-led.</h2>
  <p class="sub">The people behind DAYS.</p>
  <div class="team">{"".join(f'<figure><img src="img/team-{k}.jpg" alt=""><figcaption><strong>{e(n)}</strong><span class="label sm">{r}</span></figcaption></figure>' for k, n, r in team)}</div>
</section>''')

# ---------------------------------------------------------------- 13 contact
contact = [("WhatsApp / Phone", "+62 812 2000 0185"), ("Email", "lets@talkaboutdays.com"),
           ("Instagram", '<a href="https://instagram.com/talkaboutdays">@talkaboutdays</a>'),
           ("Website", '<a href="https://talkaboutdays.com">talkaboutdays.com</a>'),
           ("Studio", "Jl. Tebet Barat IX No. 2, Jakarta Selatan"),
           ("Hours", "Mon–Fri · 09.00–18.00<br>Sat · 11.00–14.00<br>Sun · Closed")]
pages.append(f'''<section class="page g-contact">
  <div class="contact-grid">
    <div><p class="label">Get in touch</p><h2 class="h xl">Let’s plan your next DAYS.</h2><p class="sub">Yuk, rencanakan perjalananmu.</p></div>
    <dl class="contact">{"".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in contact)}</dl>
  </div>
  <div class="foot"><img src="img/wordmark-orange.png" alt="DAYS"><span>Sources: DAYS Brand Identity Guidelines v1.0 and talkaboutdays.com. Photography from talkaboutdays.com.</span></div>
</section>''')

css = (HERE / "brand-profile.css").read_text()
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DAYS Brand Profile</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,800;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>{"".join(pages)}</body></html>'''
(HERE / "brand-profile.html").write_text(html)
print("wrote brand-profile.html,", len(pages), "pages")
