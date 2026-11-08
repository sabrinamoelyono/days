// Render enquire.html and price.html to ../export/DAYS-primavera-2027-<name>.jpg at full size.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2061, height: 2576 }, deviceScaleFactor: 1 });
  for (const name of ['enquire', 'price']) {
    await p.goto('file://' + path.join(__dirname, name + '.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const out = path.join(__dirname, '..', 'export', `DAYS-primavera-2027-${name}.jpg`);
    await (await p.$('#poster')).screenshot({ path: out, type: 'jpeg', quality: 92 });
    console.log('wrote', out);
  }
  await b.close();
})();
