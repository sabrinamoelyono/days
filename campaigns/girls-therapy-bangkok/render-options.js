// Render cover-options.html sections to export/cover-options/.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const out = path.join(__dirname, 'export', 'cover-options');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'cover-options.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const s = await p.$$('.slide');
  for (let i = 0; i < s.length; i++) await s[i].screenshot({ path: `${out}/cover-option-${'ABC'[i]}.png` });
  await b.close();
})();
