// Render brand-profile.html to PDF (and optional page PNGs for review).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'brand-profile.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, 'DAYS-Brand-Profile.pdf'), preferCSSPageSize: true, printBackground: true });
  if (process.argv[2]) {
    await p.setViewportSize({ width: 1123, height: 794 });
    const pages = await p.$$('.page');
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: `${process.argv[2]}/p${String(i + 1).padStart(2, '0')}.png` });
  }
  await b.close();
})();
