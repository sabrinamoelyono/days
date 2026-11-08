# DAYS x Primavera Sound 2027: package posters

| File | What |
|---|---|
| `src/price-original.jpg` | Price poster (source of truth): festival ticket, 4D/3N accommodation, airport transfers, Sagrada Família, Casa Batlló, curated guide. No flights. |
| `src/enquire-original.jpg` | Original "Enquire Now" poster, which wrongly listed flights and a Jakarta departure |
| `export/DAYS-primavera-2027-enquire.jpg` | Revised "Enquire Now" poster, matching the price poster |

Revision: removed "Flights" and "Departure: Jakarta (CGK)"; duration line now reads "4 Days / 3 Nights | Barcelona, June 3–5, 2027"; includes now list exactly what the price poster lists; added "*Flights not included".

Rebuild: `python3 src/clean_enquire.py src/enquire-original.jpg src/enquire-clean.png && node src/render.js` (text is in `src/enquire.html`).
