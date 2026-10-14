// Render each page to a 1080×1920 PNG: node render.js 00-invite.html 01-lineup.html 02-topics.html
// HD (2160×3840) into hd/: HD=1 node render.js ...
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path'), fs = require('fs');
const hd = !!process.env.HD;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: hd ? 2 : 1 });
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + path.join(__dirname, f));
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    const out = hd ? path.join(__dirname, 'hd', f.replace('.html', '-HD.png')) : path.join(__dirname, f.replace('.html', '.png'));
    fs.mkdirSync(path.dirname(out), { recursive: true });
    await p.screenshot({ path: out });
  }
  await b.close();
})();
