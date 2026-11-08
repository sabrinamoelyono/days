// Builds the AO 2027 launch carousel into ./export.
// Slides 02–05 are rendered from slides.html; slides 01 and 06–09 are the AO-approved assets, copied byte-for-byte (never edited).
// Usage: node render.js [deviceScaleFactor]   (needs the licensed fonts in ./fonts — see caption.md)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const approved = {
  '01': 'AO27-cover.webp',
  '06': 'AO27-quarterfinals.png',
  '07': 'AO27-semifinals.png',
  '08': 'AO27-finals.png',
  '09': 'AO27-semifinal-final.png',
};
const days = { '02': '2', '03': '3', '04': '4', '05': '5' };

(async () => {
  for (const f of ['Sequel100Wide-85.ttf', 'SharpSans-No2-Bold.otf']) {
    if (!fs.existsSync(path.join(__dirname, 'fonts', f))) throw new Error(`missing fonts/${f}`);
  }
  const root = path.join(__dirname, 'export');
  fs.rmSync(root, { recursive: true, force: true });

  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: Number(process.argv[2] || 1) });
  await p.goto('file://' + path.join(__dirname, 'slides.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);

  fs.mkdirSync(root, { recursive: true });
  for (const [n, f] of Object.entries(approved)) {
    fs.copyFileSync(path.join(__dirname, 'approved', f), path.join(root, `${n}-${f}`));
  }
  for (const [n, id] of Object.entries(days)) {
    const el = await p.$(`.slide[data-id="${id}"]`);
    if (!el) throw new Error(`no slide with data-id="${id}"`);
    await el.screenshot({ path: path.join(root, `${n}-DAYS.png`) });
  }
  await b.close();
})();
