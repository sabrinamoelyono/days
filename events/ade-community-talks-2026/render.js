const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  const bg = fs.readFileSync(path.join(__dirname, 'bg.html'), 'utf8');
  for (const f of process.argv.slice(2)) {
    const html = fs.readFileSync(path.join(__dirname, f), 'utf8').replace('<!--BG-->', bg);
    const tmp = path.join(__dirname, '_' + f); fs.writeFileSync(tmp, html);
    await p.goto('file://' + tmp); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    await p.screenshot({ path: path.join(__dirname, f.replace('.html', '.png')) });
    fs.unlinkSync(tmp);
  }
  await b.close();
})();
