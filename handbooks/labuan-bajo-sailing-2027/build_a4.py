"""Build the A4 portrait edition of the proposal.

Same pages and content as the 4:5 proposal (build.py), laid out on a taller
A4-proportioned page (1080 x 1527 design px) and zoomed to A4 for print.
Extra rules for the taller page live in proposal-a4.css.

Run:  python3 build_a4.py && node render_a4.js
"""
from pathlib import Path

import build  # builds the 4:5 pages (and refreshes proposal.html)

HERE = Path(__file__).parent
css = (HERE / "proposal.css").read_text() + "\n" + (HERE / "proposal-a4.css").read_text()
title = build.html.split("<title>")[1].split("</title>")[0] + " (A4)"
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,800;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body class="a4">{"".join(build.pages)}</body></html>'''
(HERE / "proposal-a4.html").write_text(html)
print("wrote proposal-a4.html,", len(build.pages), "pages")
