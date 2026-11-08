# DAYS x Primavera Sound 2027: package posters

## Package (current)

6 days / 5 nights, 2–7 June 2027 (festival 3–5 June), min. 2 pax. Flights not included.

| Package | Price |
|---|---|
| The Fòrum Edit (Regular) | Rp 47,500,000 / pax |
| VIP | Rp 59,500,000 / pax |

All include: 3-day Primavera Sound pass (Regular / VIP), 5 nights accommodation (3-star Regular / 4-star VIP), airport transfers, Sagrada Família, Casa Batlló, a curated guide to Barcelona's food, culture and local scene.

## Files

| File | What |
|---|---|
| `export/DAYS-primavera-2027-price.jpg` | Price poster with both packages |
| `export/DAYS-primavera-2027-enquire.jpg` | "Enquire Now" poster, same package details |
| `src/price-original.jpg`, `src/enquire-original.jpg` | Originals (old 4D/3N package; Enquire Now wrongly listed flights) |

## Rebuild

```bash
python3 src/clean_panel.py src/enquire-original.jpg src/enquire-clean.png 1803
python3 src/clean_panel.py src/price-original.jpg src/price-clean.png 1733 1650,1733,2061,1960
node src/render.js
```

The text lives in `src/price.html` and `src/enquire.html`.
