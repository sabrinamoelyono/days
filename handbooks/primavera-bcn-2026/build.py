"""Build the DAYS x Primavera Sound Barcelona 2026 handbook as print-ready HTML.

Run:  python3 build.py && node render.js
"""
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent
RUNNING = "Primavera Sound · Barcelona · 2026"

# ---------------------------------------------------------------- content

TIPS = [
    ("Time", "Barcelona eats late", "Lunch is 2–4pm. Dinner kicks off at 9pm. Don't be the table asking for dinner at 7."),
    ("Book", "Book or queue", "For Paradiso, Sips, Disfrutar and El Xampanyet — either book weeks in advance or arrive when they open."),
    ("Fest", "Festival hours", "Primavera runs afternoon through 3am. Pace yourself. The best sets are always after midnight."),
    ("Move", "Getting around", "Metro until midnight weekdays, 2am Fri, all night Sat. After that: Uber or taxi. Poblenou to El Born is 30 minutes."),
    ("Cash", "Cash is still king", "Smaller tapas bars and old-school spots often prefer cash. Keep €50–€100 on you at all times."),
    ("Wear", "Dress for two climates", "Barcelona in June: warm sunny days (24–28°C), balmy evenings. Light layers for the coastal breeze at the beach stage."),
]

HOODS = [
    ("El Poblenou", "Where the festival lives", "The old industrial district that grew into a creative hub. Parc del Fòrum is here. The Rambla del Poblenou is the neighbourhood's spine — cafés, bars, easy energy. Henry's Bar and el 58 are both here."),
    ("El Born", "Cocktails & cava", "Medieval streets, the Picasso Museum, and Barcelona's best bar scene. Paradiso, El Xampanyet, Cal Pep, Bar del Pla. El Born is where most nights end up."),
    ("Barceloneta", "Seafood & beach", "The old fishing neighbourhood between the city and the sea. Back streets hold old-school tapas bars and fish that was in the water this morning. La Cova Fumada and Jai Ca are here."),
    ("Eixample", "Gaudí & great bars", "The city's orderly grid neighbourhood. Casa Batlló and La Sagrada Família are here. So are Sips, Dry Martini, Bandini's, Disfrutar, Mont Bar, and Gresca."),
    ("Poble Sec", "The local secret", "Where Barcelona that hasn't been gentrified yet survives. Quimet y Quimet and Xemei are here. The bar stools are small, the montaditos are brilliant."),
    ("Sant Antoni", "The creative quarter", "A neighbourhood in transition — in the best way. Coffee shops, natural wine bars, and chef-driven bistros have clustered around the Sant Antoni market."),
    ("Gràcia", "Village within the city", "Narrow streets, bohemian bars, square culture. Fonda Pepa and Brugarol are here. Great for aperitivo hour before heading further into the city."),
]

# (name, area, line, body, tag, image, featured)
EAT = [
    ("Gresca", "Eixample · Modern Catalan", "Dua Lipa's most-visited Barcelona restaurant",
     "Chef Rafa Peña — winner of the Premi Nacional de Gastronomia 2023 — runs this intimate Eixample spot with an open kitchen and a bar counter where you watch everything happen. Marinated anchovies, scrambled eggs with wild garlic and prawns, octopus carpaccio, and a torrija dessert that's become mythic. Dua Lipa has been back multiple times, sitting at the bar while the chef explains every dish.",
     "Dua Lipa", None, True),
    ("Xemei", "Poble Sec · Venetian", "Dua Lipa's other Barcelona obsession",
     "Venetian twins Stefano and Max Colombo brought the real cooking of Venice to Barcelona — sarde in saor, baccalà mantecato, and grilled baby squid with polenta. Dua Lipa has returned here on multiple visits for the pasta and the tiramisu. Considered the best Italian restaurant in the city. Organic wine list, cozy terrace on Passeig de l'Exposició.",
     "Dua Lipa", None, True),
    ("Disfrutar", "Eixample · Avant-garde Catalan", "Barcelona's most creative kitchen, full stop",
     "Three-Michelin-star restaurant run by alumni of elBulli. Each dish is a concept — from the signature caviar-filled panchino to the liquid salad. Playful yet precise, balancing technique and flavour in a way that feels inventive but genuinely satisfying. Book months ahead.",
     "Splurge", "disfrutar", False),
    ("Maleducat", "Eixample · Modern Catalan", "A bold, no-rules kind of place",
     "Seasonal Catalan dishes with punchy flavours, a bit unexpected, and the kind of spot you leave thinking about what you just ate. The cooking is confident without being showy — proper ingredients, properly treated.",
     "Must try", "maleducat", False),
    ("Besta", "El Born · Seafood", "Elevated yet effortless",
     "A seafood-focused restaurant where Galician and Catalan influences come together in a way that's refined but still warm and inviting. The arroz negro and the daily fish are the reasons you come. The reason you return is harder to name.",
     "Seafood", "besta", False),
    ("Brugarol", "Gràcia · Fire & produce", "Everything feels intentional",
     "A beautifully designed space where produce-driven plates meet open-fire cooking that brings out deep, honest flavours. The scallop tartare with cured egg yolk is the kind of dish that redefines a single ingredient. Book ahead.",
     "Chef's pick", "brugarol", False),
    ("La Bonaigua", "Eixample · Steakhouse", "The steak speaks for itself",
     "Perfectly matured beef, simply executed, all about the quality of the product rather than anything overcomplicated. The kind of place carnivores bookmark and return to every trip. Go hungry.",
     "Local pick", "la-bonaigua", False),
    ("Casa Amalia", "Gràcia · Seafood & paella", "Market-style Barcelona energy",
     "Seafood-led dishes served with the kind of comforting, no-fuss warmth that makes you feel like a local. The real standout is the paella — rich, deeply flavourful, and the kind you'd come back for without overthinking the rest of the menu.",
     "Casual", "casa-amalia", False),
    ("Cañete", "Raval · Tapas counter", "Best experienced at the counter",
     "Where everything moves fast and feels alive — the grilled carabineros are a standout, sweet and smoky with just enough char, alongside silky seafood dishes that keep it classic but never boring.",
     "Classic", "canete", False),
    ("Estimar", "El Born · Elevated seafood", "Where El Bulli lives on — in a marisquería",
     "Head chef Rafa Zafra is an El Bulli graduate who transformed the traditional seafood restaurant into something refined and market-fresh. Galician razor clams, Cantabrian anchovies, the famous onion & crayfish carpaccio. Book weeks ahead.",
     "Essential", None, False),
    ("Mont Bar", "Eixample · Modern tapas", "Where the food critics eat on their nights off",
     "A fresh take on fine dining without the ceremony. Mont Bar's small plates rotate with the seasons. Intimate, excellent wine list, great energy at the bar.",
     "Must try", None, False),
    ("Franca", "Eixample Dreta · Modern Catalan", "Local and very current at the same time",
     "Catalan dishes reworked in thrilling modern ways. The space is welcoming, the cooking always surprises in a good way. You never know what the dish will look like when it arrives. Roger de Llúria 46.",
     "Local pick", None, False),
]

TAPAS = [
    ("El Xampanyet", "El Born", "House cava + anchovies", "The original old-school cava bar, pouring since 1929. Always packed, always worth it. Order the house cava and whatever's on the counter. This is Barcelona in a glass.", "Iconic"),
    ("Quimet y Quimet", "Poble Sec", "Salmon montadito with honey", "Standing room only, tins of conservas stacked floor to ceiling, brilliant montaditos. The salmon tapa with honey is the one. Go early — they close when they run out.", "Legendary"),
    ("La Cova Fumada", "Barceloneta", "The original bomba", "Dating back to 1944. No sign on the door, no menu — just a blackboard. This is where the bomba was invented. Worth every bit of the effort to find it.", "Original"),
    ("Cal Pep", "El Born", "Whatever Pep is cooking that day", "The legendary seafood counter where the bar seats are the best in the house and the kitchen decides what's good that day. Trust the process.", "Seafood"),
    ("el 58", "Poblenou", "Razor clams, duck magret, pulpo", "Right on the Rambla del Poblenou — walking distance from the festival. Menu on a blackboard, terrace out back. No reservations, so show up or miss out.", "Festival zone"),
    ("Cerveceria Catalana", "Eixample", "Montaditos, grilled prawns", "The most-reviewed tapas bar in Barcelona. Long bar, wide selection, consistent quality. Fast service. No reservations — queue at peak hours but it moves quickly.", "Crowd pleaser"),
    ("Bar del Pla", "El Born", "Natural wine + market special", "Over 30 natural wines, brilliant tapas, and sommeliers who know their stuff. The go-to before a night in El Born. Sits just metres from El Xampanyet.", "Natural wine"),
    ("Bodega La Puntual", "El Born", "Arroz de Pluma Ibérica", "In an 1872 coffee roaster building on Carrer de Montcada. A casual oyster bar at the entrance; a larger room for groups further inside.", "Historic"),
    ("Paco Meralgo", "Eixample Esquerra", "Ondarroa anchovies, Cíes clams", "The seafood-tapas institution of the Eixample. Marinated anchovies from Ondarroa and razor clams from the Cíes Islands are the headliners.", "Institution"),
    ("Jai Ca", "Barceloneta", "Bombas, bravas, cod fritters", "Classic tapas bar in the old fishing district. Earthy, no-nonsense. The bombas here are the standard all others are judged against.", "Old school"),
    ("Bar Bocata", "Sarrià-Sant Gervasi", "Tortilla with caramelised onion", "From breakfast through late dinner, Bar Bocata delivers all day. The tortilla with soft caramelised onion is non-negotiable. Book ahead.", "All day"),
    ("Bar Cañete", "Raval", "Fresh Catalan seafood, seasonal", "Near the Gran Teatre del Liceu. Family-run kitchen using fish fresh from Catalan markets. Beautifully executed classics, lively room.", "Classic"),
]

BARS = [
    ("Paradiso", "El Born", "Enter through a fake paella fridge in a sandwich shop. Inside: one of the world's best cocktail bars. Conceptual menus, extraordinary technique. Also has a rooftop at Time Out Market. Queue early — no reservations at the original.", "World's best", True),
    ("Sips", "Eixample", "Consistently top-50 in the world. Conceptual and precise cocktails in a sleek room on Carrer de Muntaner. Book ahead or queue. 45-minute sitting per round — make every drink count.", "Top 50", True),
    ("Dry Martini", "Eixample", "Founded in 1978. Wood, leather, brass — and over 1.5 million martinis served. Still the best classic bar in the city. Sophisticated but never stuffy.", "Institution", False),
    ("Dr. Stravinsky", "El Born", "Designed like the lab of a mad chemist, named after a character from The Master & Margarita. Plants everywhere, drinks served in flower vases.", "Eccentric", False),
    ("Bandini's", "Eixample", "The funkiest natural wine selection in the city, plus seasonal small plates. Try a local pet-nat from Catalonia. Young, local, knowing crowd.", "Natty wine", False),
    ("Henry's Bar", "Poblenou", "Calls itself a dive bar, but the cocktails are considered and the sunny terrace is exactly right for a festival afternoon. Carrer de la Llacuna 92 — festival zone.", "Festival zone", False),
    ("Les Gens que J'aime", "Eixample Dreta", "Below street level, fringed lampshades, velvet sofas, jazz. Whiskey sours are the move. One of those bars you stumble into at 10pm and leave at 2am.", "Late night", False),
    ("Monvínic", "Eixample", "3,500 vintages, a vertical garden, a reference library, and a tablet wine list. Called 'Wineworld' in Catalan for good reason.", "Wine geek", False),
    ("Garage Beer Co", "Poblenou", "Three locations: city-centre bar, a beachfront spot in Poblenou, and a brewery in Sant Andreu. The Poblenou outpost is the natural festival companion.", "Craft beer", False),
    ("Azimuth Rooftop", "Eixample", "Seasonal rooftop with a pool, panoramic Barcelona views, and an inventive cocktail menu. Open May–September. Exactly where you want to be on a warm afternoon.", "Rooftop", False),
    ("Libertine", "Eixample (Casa Bonay)", "A Top 50 Discovery bar inside Casa Bonay, open until 3am on weekends. Upstairs there's a rooftop spa with sauna and hammam.", "Late night", False),
    ("El Quim de la Boqueria", "Raval", "A counter inside La Boqueria where the chef cooks eggs with baby squid and whatever is freshest. Opens early, closes when it's done. Best breakfast in the city.", "Morning", False),
]

NIGHT = [
    ("5pm", "Vermouth and montaditos at Quimet y Quimet or Bar del Pla"),
    ("9pm", "Dinner — tapas bar-hop El Born or a table at Gresca / Mont Bar"),
    ("11pm", "Cocktails at Paradiso (queue) or Sips (book ahead)"),
    ("1am", "Head to Poblenou for the festival's late headliners"),
    ("3am", "Whatever happens, happens"),
]

FEST = [
    ("In", "Arrival", "Gates open from 4pm. The early sets are worth catching — smaller stages, fewer people, musicians who are genuinely happy to be there."),
    ("Eat", "Eating & drinking", "The food at Primavera is actually good. Pro move: eat a proper dinner before 8pm and graze inside."),
    ("Stage", "The main stage", "The main stage faces the sea. For big acts, get there 30 minutes early or accept a great view from further back. Both are valid."),
    ("Set", "Stage logistics", "Multiple stages run simultaneously. Download the app, build your schedule, but leave gaps — the best moments are often accidental."),
    ("AM", "The late hours", "11pm to 3am is when Primavera turns into something else entirely. The sets get longer, and the festival earns its reputation."),
    ("Kit", "What to wear", "Comfortable shoes you won't regret at 2am. A light jacket for the sea breeze. One bag with a secure pocket for your phone and wallet."),
]

LOGISTICS = [
    ("From the airport", "Barcelona El Prat (BCN) is 30–40 minutes from the city centre. The Aerobus runs to Plaça Catalunya every 10 minutes. Taxi is a fixed fare (~€35). Uber also works."),
    ("Getting around", "The metro covers most of the city. T-Casual 10-trip card is the best value. Poblenou/El Fòrum is on the L4 line (yellow). Metro runs all night on Saturdays."),
    ("Festival transport", "Parc del Fòrum is right at El Maresme | Fòrum station on the L4. Walking from El Born takes about 30 minutes along the waterfront."),
    ("Money", "Spain is largely card-friendly, but old-school tapas bars prefer cash. Revolut or Wise cards are ideal — no foreign transaction fees. Keep €50–€100 in your wallet."),
    ("Phone & data", "Indonesian SIMs won't have EU roaming by default. Pick up a local SIM at the airport (Vodafone or Orange), or check your provider before you leave."),
]

# ---------------------------------------------------------------- components

def num(i):
    return f'<span class="num">{i:02d}</span>'

def head(page_no, dark=False):
    return f'''<header class="run">
  <img class="mark" src="img/days-wordmark.png" alt="DAYS">
  <span>{e(RUNNING)}</span>
  <span class="pg">{page_no:02d}</span>
</header>'''

def opener(eyebrow, title, lede, meta=None):
    m = f'<p class="meta">{e(meta)}</p>' if meta else ""
    return f'''<div class="opener">
  <p class="eyebrow">{e(eyebrow)}</p>
  <h1>{e(title)}</h1>
  <p class="lede">{e(lede)}</p>{m}
</div>'''

def page(n, body, cls=""):
    return f'<section class="page {cls}">{head(n)}<div class="body">{body}</div></section>'

def tip_grid(items):
    out = []
    for code, title, body in items:
        out.append(f'''<div class="tip"><span class="code">{e(code.upper())}</span>
<h3>{e(title)}</h3><p>{e(body)}</p></div>''')
    return '<div class="tips">' + "".join(out) + "</div>"

def eat_card(i, r):
    name, area, line, body, tag, img, feat = r
    tagcls = "tag solid" if feat else "tag"
    pic = f'<img class="pic" src="img/{img}.jpg" alt="{e(name)}">' if img else ""
    return f'''<article class="eat{' has-pic' if img else ''}{' feat' if feat else ''}">
  <div class="txt">
    <div class="top">{num(i)}<span class="{tagcls}">{e(tag)}</span></div>
    <h2>{e(name)}</h2>
    <p class="area">{e(area)}</p>
    <p class="line">{e(line)}</p>
    <p class="desc">{e(body)}</p>
  </div>{pic}
</article>'''

def tapas_card(i, r):
    name, area, order, body, tag = r
    return f'''<article class="tapa">
  <div class="top">{num(i)}<span class="tag">{e(tag)}</span></div>
  <h2>{e(name)}</h2>
  <p class="area">{e(area)}</p>
  <p class="order"><span>Order</span>{e(order)}</p>
  <p class="desc">{e(body)}</p>
</article>'''

def bar_row(i, r):
    name, area, body, tag, feat = r
    return f'''<article class="bar">
  {num(i)}
  <div><h2>{e(name)} <span class="area">{e(area)}</span></h2><p class="desc">{e(body)}</p></div>
  <span class="tag{' solid' if feat else ''}">{e(tag)}</span>
</article>'''

# ---------------------------------------------------------------- pages

pages = []

pages.append('''<section class="page cover">
  <img class="cover-mark" src="img/days-wordmark.png" alt="DAYS">
  <p class="cover-kicker">Seven DAYS in Sunny June</p>
  <div class="cover-main">
    <p class="eyebrow">The handbook · Barcelona · June 2026</p>
    <h1>Prima&shy;vera<span class="dot">.</span></h1>
    <p class="cover-lede">You booked this trip because of the lineup.<br>You'll stay because of the city.<br>Barcelona in June is something else entirely.</p>
  </div>
  <dl class="facts">
    <div><dt>Festival</dt><dd>Primavera Sound 2026</dd></div>
    <div><dt>Location</dt><dd>Parc del Fòrum, BCN</dd></div>
    <div><dt>Vibe</dt><dd>Mediterranean chaos</dd></div>
  </dl>
</section>''')

# contents
toc = [("Before you land", "Quick tips", 3), ("Barcelona, decoded", "The city", 4),
       ("Where to eat", "Restaurants", 5), ("The real Barcelona", "Tapas bars", 9),
       ("Stay out late", "Bars & drinks", 11), ("Primavera Sound", "The festival", 13),
       ("On the ground", "Logistics", 14)]
toc_html = "".join(f'<li><span class="num">{p:02d}</span><span class="t">{e(t)}</span><span class="s">{e(s)}</span></li>' for t, s, p in toc)
pages.append(page(2, f'''<div class="opener"><p class="eyebrow">Inside</p><h1>The guide.</h1>
<p class="lede">Everything we'd tell a friend flying in for the festival — where to eat, where to drink, which neighbourhood to wander, and how to get to the Fòrum and back. Built by DAYS so you spend zero time searching and all of it being there.</p></div>
<ol class="toc">{toc_html}</ol>'''))

pages.append(page(3, opener("Quick tips", "Before you land.", "Everything you need to know before you touch down in Barcelona.") + tip_grid(TIPS)))

hoods = "".join(f'<div class="hood"><div><h2>{e(n)}</h2><p class="kick">{e(k)}</p></div><p class="desc">{e(d)}</p></div>' for n, k, d in HOODS)
pages.append(page(4, opener("The city", "Barcelona, decoded.", "Barcelona rewards the curious and punishes the timid. It's a city of neighbourhoods that feel like separate cities — each with its own pace, its own regulars, its own rules.") + f'<div class="hoods">{hoods}</div>'))

dl = '''<aside class="callout"><span class="code">DL</span><div><p class="k">Dua Lipa's Barcelona favourites</p>
<p>Gresca and Xemei — she comes back every visit. Book these two before anything else.</p></div></aside>'''
pages.append(page(5, opener("Restaurants", "Where to eat.", "Twelve picks across every neighbourhood. Two are certified Dua Lipa favourites. All are worth your time.", "12 picks · All neighbourhoods")
                  + dl + eat_card(1, EAT[0]) + eat_card(2, EAT[1])))
pages.append(page(6, "".join(eat_card(i + 1, EAT[i]) for i in (2, 3, 4))))
pages.append(page(7, "".join(eat_card(i + 1, EAT[i]) for i in (5, 6, 7))))
pages.append(page(8, "".join(eat_card(i + 1, EAT[i]) for i in (8, 9, 10, 11))))

pages.append(page(9, opener("Tapas bars", "The real Barcelona.", "The tapas bar is where Barcelona actually lives. Stand at the bar. Order two or three things. Move on. That's how you do it.", "12 picks · From legendary to local")
                  + '<div class="tapas">' + "".join(tapas_card(i + 1, TAPAS[i]) for i in range(6)) + "</div>"))
pages.append(page(10, '<div class="tapas">' + "".join(tapas_card(i + 1, TAPAS[i]) for i in range(6, 12)) + "</div>"))

pages.append(page(11, opener("Bars & drinks", "Stay out late.", "Barcelona's bar scene is world-class. The cocktail movement here is technical and serious, the natural wine scene is booming, the vermouth culture is real, and the old cava bars have been doing their thing for decades.", "12 picks · Cocktails · Wine · Beer · Rooftop")
                  + '<div class="bars">' + "".join(bar_row(i + 1, BARS[i]) for i in range(6)) + "</div>"))
night = "".join(f'<li><span class="t">{e(t)}</span><span>{e(d)}</span></li>' for t, d in NIGHT)
pages.append(page(12, '<div class="bars">' + "".join(bar_row(i + 1, BARS[i]) for i in range(6, 12)) + "</div>"
                  + f'<div class="night"><p class="eyebrow">The classic Barcelona night</p><ol>{night}</ol></div>'))

pages.append(page(13, opener("The festival", "Primavera Sound.", "Parc del Fòrum is a concrete plaza jutting into the Mediterranean. At night, with the stages lit up and the sea behind everything, it's one of the most striking festival settings in the world.") + tip_grid(FEST)))

logi = "".join(f'<div class="logi"><h3>{e(t)}</h3><p>{e(b)}</p></div>' for t, b in LOGISTICS)
pages.append(page(14, opener("Logistics", "On the ground.", "Airport, metro, money and data — the practical bit, so the rest can be anything but.")
                  + f'<div class="logis">{logi}</div>'
                  + '''<aside class="contact"><p class="eyebrow">DAYS contact</p><p>Your DAYS trip lead is on WhatsApp throughout the trip. If anything goes sideways — accommodation, tickets, logistics — that's your first call.</p></aside>'''))

pages.append('''<section class="page closing">
  <img class="cover-mark" src="img/days-wordmark.png" alt="DAYS">
  <div class="letter">
    <p class="eyebrow">Seven DAYS in Sunny June</p>
    <p class="big">You didn't book this trip to tick a box. You booked it because the lineup hit different, because Barcelona in June is its own kind of argument, and because you know the difference between going somewhere and actually being there.</p>
    <p>We built this guide so you spend zero time figuring out where to eat, drink, or be — and all your time doing exactly that. The rest is yours.</p>
  </div>
  <p class="sign">DAYS · Jakarta · June 2026 &nbsp;·&nbsp; talkaboutdays.com</p>
</section>''')

css = (HERE / "handbook.css").read_text()
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>DAYS × Primavera Sound Barcelona 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,800;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>{"".join(pages)}</body></html>'''
(HERE / "handbook.html").write_text(html)
print("wrote handbook.html,", len(pages), "pages")
