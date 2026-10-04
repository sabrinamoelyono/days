# ADE Community Talks 2026 — e-flyer

*How Indonesia Built Its Sound* · 10 Oct 2026, 4–7 PM · Space Available, Jl. Kemang Raya No. 8B, Jakarta

| File | What it is |
|---|---|
| `00-invite.png` | Story (1080 × 1920): "We invite ____" e-invite, with a line for the guest's name or @handle |
| `01-lineup.png` | Story (1080 × 1920): title, date, time, venue and the six speakers |
| `02-topics.png` | Story (1080 × 1920): the seven talk topics |
| `03-scene.png` | Story (1080 × 1920): why the event exists, bridging Indonesia's electronic music scene |
| `04-days.png` | Story (1080 × 1920): about DAYS |
| `*.html`, `modern.css` | Source for the three pages |
| `img/` | Speaker photos, ADE logo box, partner logos (light versions for the dark background) |

All three pages keep the top 220 px clear for Instagram's profile bar and leave room at the bottom for a link sticker.

To re-render after editing: `node render.js 00-invite.html 01-lineup.html 02-topics.html` (needs Playwright).

Partner logos sit in the `.logos` row at the bottom of each page, as light (off-white) PNGs in `img/*-light.png`.
