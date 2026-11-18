// Render stories.html (native 9:16 layouts) to export/stories/ at 1080×1920.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const names = ['01-cover', '02-safe-space', '03-treatment', '04-two-sessions', '05-cool-down', '06-fine-print', '07-schedule'];
(async () => {
  const out = path.join(__dirname, 'export', 'stories');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'stories.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const s = await p.$$('.st');
  for (let i = 0; i < s.length; i++) await s[i].screenshot({ path: `${out}/girls-therapy-story-${names[i]}.png` });
  await b.close();
})();
