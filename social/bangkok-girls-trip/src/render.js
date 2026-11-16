// Render each slide in slides.html to ../export/DAYS-bangkok-girls-trip-<id>.jpg (1600x2000).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1700, height: 2100 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'slides.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  for (const el of await p.$$('.s')) {
    const id = await el.getAttribute('id');
    const out = path.join(__dirname, '..', 'export', `DAYS-bangkok-girls-trip-${id}.jpg`);
    await el.screenshot({ path: out, type: 'jpeg', quality: 92 });
    console.log('wrote', id);
  }
  await b.close();
})();
