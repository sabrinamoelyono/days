"""Build the DAYS partner one-pager (A4 landscape) from the Brand Profile.

For partners and potential partners: who DAYS is, why it is different,
and the proof. Reuses the Brand Profile's motifs, collection order, colours
and type (brand-profile.css + one-pager.css), so facts stay in one place.

Run:  python3 one_pager.py && node render_one_pager.js
"""
from pathlib import Path

import build  # Brand Profile source (also refreshes brand-profile.html)
from build import MOTIF, ORDER, TILE_LABEL, AO_BADGE

HERE = Path(__file__).parent

# One line per collection, plus one real trip as proof.
LINES = {
    "city": ("A city the way locals live it.", "Seoul: Soft Days"),
    "music": ("Europe’s festivals, planned around the lineup. Our core.", "ADE 2022–2026 · Primavera Sound 2024–2026 · Dekmantel 2026"),
    "nature": ("Journeys where the landscape is the reason to go.", "Dolomites · Positano · Sorrento, 2025"),
    "sports": ("Formula 1, Grand Slams and active escapes.", "Australian Open · Niseko 2024–25"),
    "culinary": ("Slow travel for food, wine and rest.", "Tuscany · Florence · Bologna · Rome, 2025"),
}

WHY = [
    ("A festival-first audience", "Indonesian travelers aged 25–55 who plan their year around lineups, race weekends and Grand Slams."),
    ("Group departures, year after year", "Five editions of ADE in a row, and Primavera Sound three years running."),
    ("Voice in the scene", "ADE 2026 Asia Hub panel in Amsterdam, and the Cities Unwrapped travel journal, in English and Bahasa Indonesia."),
    ("End to end, documents included", "Itineraries, tickets, stays and transfers, with in-house visa and passport handling."),
]

# Highlights: four moments, each with an image or a collection panel.
HIGHLIGHTS = [
    ("img", "ade", "ADE, Amsterdam", "Five editions in a row, 2022–2026, and the ADE 2026 Asia Hub panel."),
    ("img", "primavera", "Primavera Sound", "Barcelona, with a DAYS group three years running, 2024–2026."),
    ("img", "niseko", "Niseko, Japan", "Ski open trip for all levels, winter 2024–25."),
    ("img", "dolomites", "Italy, 2025", "Seven places in one year, from the Dolomites and Positano to Florence and Rome."),
]

# Timeline: what DAYS has done, year by year.
TIMELINE = [
    ("2022", "DAYS founded in Jakarta. First group to Amsterdam Dance Event."),
    ("2024", "First group to Primavera Sound, Barcelona. Ski open trip to Niseko, winter 2024–25."),
    ("2025", "Italy: Dolomites, Positano, Sorrento, Tuscany, Florence, Bologna and Rome."),
    ("2026", "Fifth ADE, Dekmantel, and the ADE Asia Hub panel in Amsterdam."),
]

LOGOS = ["bni", "cikal", "mozio", "terralogiq", "superstars", "imagineka"]

tiles = "".join(f'''<div class="op-col">
  <div class="op-tile t-{k}"><span class="motif">{MOTIF[k]}</span><span class="lbl">{TILE_LABEL[k]}</span></div>
  <p class="op-line">{LINES[k][0]}</p>
  <p class="op-proof">{LINES[k][1]}</p>
</div>''' for k in ORDER)

import sys
VARIANT = sys.argv[1] if len(sys.argv) > 1 else "highlights"

def media(kind, ref):
    if kind == "img":
        return f'<img src="img/{ref}.jpg" alt="">'
    if kind == "ao":
        return f'<span class="hl-panel ao">{AO_BADGE}</span>'
    return f'<span class="hl-panel t-{ref}">{MOTIF[ref]}</span>'

SECTIONS = {
    "why": ("Why partner with DAYS",
            '<div class="op-why">' + "".join(f'<div><h4>{h}</h4><p>{p}</p></div>' for h, p in WHY) + "</div>"),
    "highlights": ("Our highlights",
            '<div class="op-hl">' + "".join(f'<div class="hl">{media(k, r)}<h4>{t}</h4><p>{d}</p></div>' for k, r, t, d in HIGHLIGHTS) + "</div>"),
    "timeline": ("Our story so far",
            '<ol class="op-tl">' + "".join(f'<li><span class="yr">{y}</span><p>{d}</p></li>' for y, d in TIMELINE) + "</ol>"),
}
section_label, section_html = SECTIONS[VARIANT]
logos = "".join(f'<img src="img/logo-{l}.png" alt="">' for l in LOGOS)

page = f'''<section class="page g-cover one">
  <div class="topline"><span>DAYS / Partner one-pager</span><span>Jakarta · since 2022</span></div>
  <div class="op-head">
    <img class="op-mark" src="img/wordmark-orange.png" alt="DAYS">
    <div>
      <h1 class="op-h">Experience-driven travel media<br>and global connector between<br>Indonesia and Europe.</h1>
      <p class="id">Media perjalanan berbasis pengalaman dan penghubung global antara Indonesia dan Eropa.</p>
    </div>
  </div>
  <p class="op-idea"><strong>It starts with the music.</strong> DAYS takes Indonesian travelers to Europe’s festivals, and no one else in Indonesia does it the way we do. Around that core, we plan cities, nature, sport and slow travel.</p>
  <div class="op-proofs">
    <div class="card"><p class="stat">5×</p><p>Amsterdam Dance Event, every year 2022–2026</p></div>
    <div class="card"><p class="stat">2,000+</p><p>visa applications processed since 2022</p></div>
    <div class="card"><p class="stat">97–98%</p><p>visa approval rate</p></div>
    <div class="card op-ao">{AO_BADGE}</div>
  </div>
  <p class="label">One brand. Five ways to go.</p>
  <div class="op-cols">{tiles}</div>
  <div class="op-bottom">
    <div>
      <p class="label">{section_label}</p>
      {section_html}
    </div>
    <div>
      <p class="label">Trusted by</p>
      <div class="op-logos">{logos}</div>
    </div>
  </div>
  <div class="op-foot">
    <strong>Let’s plan your next DAYS.</strong>
    <span>+62 812 2000 0185</span><span>lets@talkaboutdays.com</span><span>@talkaboutdays</span><span>talkaboutdays.com</span>
  </div>
</section>'''

css = (HERE / "brand-profile.css").read_text() + "\n" + (HERE / "one-pager.css").read_text()
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DAYS One-Pager</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,800;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>{page}</body></html>'''
out = HERE / ("one-pager.html" if len(sys.argv) < 3 else sys.argv[2])
out.write_text(html)
print("wrote", out.name, "·", VARIANT)
