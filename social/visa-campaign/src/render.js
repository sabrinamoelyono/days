// Render each .post in posts.html to a PNG at its exact pixel size.
// Usage: node render.js [out_dir]   (default: ../export)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const out = process.argv[2] || path.join(__dirname, '..', 'export');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 2100 }, deviceScaleFactor: 1 });
  for (const page of ['posts.html', 'loud.html']) {
    await p.goto('file://' + path.join(__dirname, page), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    for (const el of await p.$$('.post')) {
      const id = await el.getAttribute('id');
      await el.screenshot({ path: path.join(out, `DAYS-visa-${id}.png`) });
      console.log('wrote', id);
    }
  }
  await b.close();
})();
