// Render announcement.html frames to PNG.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 } });
  await p.goto('file://' + path.join(__dirname, 'announcement.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  for (const [id, name] of [['feed', 'DAYS_WhatsApp_Update_Feed_1080x1350.png'], ['story', 'DAYS_WhatsApp_Update_Story_1080x1920.png']])
    await (await p.$('#' + id)).screenshot({ path: path.join(__dirname, name) });
  await b.close();
})();
