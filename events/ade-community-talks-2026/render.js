// Render each page to a 1080×1920 PNG: node render.js 00-invite.html 01-lineup.html 02-topics.html
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + path.join(__dirname, f));
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    await p.screenshot({ path: path.join(__dirname, f.replace('.html', '.png')) });
  }
  await b.close();
})();
