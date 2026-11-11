// Builds the AO 2027 Instagram story set (1080×1920) into ./export/stories.
// AO-approved story assets are copied byte-for-byte; DAYS stories are rendered from stories.html.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const out = path.join(__dirname, 'export', 'stories');
const approved = { '01': 'AO27-story-cover.webp', '05': 'AO27-story-quarterfinals.png' };
const days = { '02': 't1', '03': 't2', '04': 't3', '06': 't4' };
const templates = { 'template-choose-your-round-no-players': 't5' };
(async () => {
  fs.rmSync(out, { recursive: true, force: true });
  fs.mkdirSync(out, { recursive: true });
  for (const [n, f] of Object.entries(approved)) fs.copyFileSync(path.join(__dirname, 'approved', f), path.join(out, `${n}-${f}`));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'stories.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  for (const [n, id] of Object.entries(days)) await (await p.$(`.slide[data-id="${id}"]`)).screenshot({ path: path.join(out, `${n}-DAYS-story.png`) });
  for (const [n, id] of Object.entries(templates)) await (await p.$(`.slide[data-id="${id}"]`)).screenshot({ path: path.join(out, `${n}.png`) });
  await b.close();
})();
