# DAYS Visa Series: social visuals

These are the refreshed visa-service posts, rebuilt with the DAYS brand system from [`DESIGN.md`](../../DESIGN.md): Paper/Ink surfaces, DAYS Orange accents, Inter Tight headlines and JetBrains Mono details.

| File | Format | Concept |
|---|---|---|
| `export/DAYS-visa-china-square.png` | 1080 × 1080 feed | 01: Visa Tiongkok, editorial layout |
| `export/DAYS-visa-schengen-square.png` | 1080 × 1080 feed | 02: Visa Schengen, editorial layout |
| `export/DAYS-visa-schengen-story.png` | 1080 × 1920 story | 02: Visa Schengen, editorial layout |
| `export/DAYS-visa-shanghai-square.png` | 1080 × 1080 feed | 03: Shanghai boarding pass, with a WhatsApp QR |
| `export/DAYS-visa-shanghai-story.png` | 1080 × 1920 story | 03: Shanghai boarding pass |
| `export/DAYS-visa-china-story.png` | 1080 × 1920 story | 01: Visa Tiongkok, editorial layout |

The editorial set above uses +62 812-2000-0495.

### Boarding-pass set (v2), WhatsApp +62 812-2000-0185

| File | Format |
|---|---|
| `export/DAYS-visa-pass-china-square.png` / `-story.png` | 01: Visa Tiongkok, CGK → PEK |
| `export/DAYS-visa-pass-schengen-square.png` / `-story.png` | 02: Visa Schengen, CGK → PSA |
| `export/DAYS-visa-pass-shanghai-square.png` / `-story.png` | 03: Shanghai, CGK → PVG |

The v2 posts are generated into `posts.html` by `src/add_v2.py` (run it before `render.js`). Their QR (`src/img/qr-wa-0185.svg`) opens `https://wa.me/6281220000185`.

## Rebuild

```bash
python3 src/clean_plates.py <folder-with-original-posts-1..5.jpg> src/img   # needs opencv-python-headless
node src/render.js export                                                    # needs playwright
```

`clean_plates.py` removes the old baked-in text from the original posts and crops clean photo plates. `posts.html` holds all five layouts, and `render.js` screenshots each one at its exact pixel size. Copy, the phone number and captions live in `posts.html`.

The QR code (`src/img/qr-wa.svg`) opens `https://wa.me/6281220000495`.
