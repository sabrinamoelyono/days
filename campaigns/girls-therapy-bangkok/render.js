// Render each .slide in slides.html to a 1600×2000 PNG (export/).
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const out = path.join(__dirname, 'export');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'slides.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const names = ['01-cover', '02-safe-space', '03-treatment', '04-two-sessions', '05-cool-down'];
  const slides = await p.$$('.slide');
  for (let i = 0; i < slides.length; i++) await slides[i].screenshot({ path: `${out}/girls-therapy-${names[i]}.png` });
  await b.close();
})();
