# DAYS Girls Trip: Bangkok After Dark (New Year's 2027)

Six-slide Instagram carousel (1600 × 2000), adapted from the "After Dark Bangkok" carousel.

**Trip:** 30 Dec 2026 – 2 Jan 2027 · 4 days / 3 nights · Rp 18,900,000 / person

| # | File | Slide |
|---|---|---|
| 1 | `export/DAYS-bangkok-girls-trip-s1-cover.jpg` | Cover: GIRLS TRIP / Bangkok, dates, "Strangers by day. The crew after dark." |
| 2 | `export/DAYS-bangkok-girls-trip-s2-days.jpg` | Four days. One group chat, no solo nights. |
| 3 | `export/DAYS-bangkok-girls-trip-s3-hotel.jpg` | Hotel: central, design-driven, made for getting ready |
| 4 | `export/DAYS-bangkok-girls-trip-s4-nights.jpg` | The nights are better together (bar crawls, route, NYE countdown) |
| 5 | `export/DAYS-bangkok-girls-trip-s5-escape.jpg` | The extra escape: Toscana Valley, Khao Yai |
| 6 | `export/DAYS-bangkok-girls-trip-s6-details.jpg` | Dates, duration, price |

## Rebuild

```bash
python3 src/clean.py src/orig src/clean   # strips the old copy from the original slides
node src/render.js                        # sets the new copy (src/slides.html) and exports JPGs
```
