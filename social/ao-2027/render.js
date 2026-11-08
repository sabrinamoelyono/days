// Builds the AO 2027 launch carousel into ./export:
//   01, 06–09  approved AO Travel & Experiences assets, copied byte-for-byte (never edited)
//   02–05      DAYS slides rendered from slides.html at 1080×1350
// Usage: node render.js [deviceScaleFactor]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const approved = {
  '01': 'AO27-cover.webp',
  '06': 'AO27-quarterfinals.png',
  '07': 'AO27-semifinals.png',
  '08': 'AO27-finals.png',
  '09': 'AO27-semifinal-final.png',
};
const daysSlides = ['02', '03', '04', '05'];

(async () => {
  const out = path.join(__dirname, 'export');
  fs.rmSync(out, { recursive: true, force: true });
  fs.mkdirSync(out, { recursive: true });

  for (const [n, f] of Object.entries(approved)) {
    fs.copyFileSync(path.join(__dirname, 'approved', f), path.join(out, `${n}-${f}`));
  }

  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: Number(process.argv[2] || 1) });
  await p.goto('file://' + path.join(__dirname, 'slides.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const slides = await p.$$('.slide');
  if (slides.length !== daysSlides.length) throw new Error(`expected ${daysSlides.length} slides, found ${slides.length}`);
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(out, `${daysSlides[i]}-DAYS.png`) });
  }
  await b.close();
})();
