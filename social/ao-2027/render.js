// Builds the two AO 2027 launch posts into ./export:
//   post-1-announcement/  01 = AO-approved cover, 02–05 = DAYS slides rendered from slides.html
//   post-2-packages/      01 = DAYS cover (player cut-outs), 02–05 = the four AO-approved package cards
// Approved assets are copied byte-for-byte and never edited.
// Usage: node render.js [deviceScaleFactor]   (needs the licensed fonts in ./fonts — see caption.md)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const posts = {
  'post-1-announcement': {
    approved: { '01': 'AO27-cover.webp' },
    days: { '02': '2', '03': '3', '04': '4', '05': '5' },
  },
  'post-2-packages': {
    approved: {
      '02': 'AO27-quarterfinals.png',
      '03': 'AO27-semifinals.png',
      '04': 'AO27-finals.png',
      '05': 'AO27-semifinal-final.png',
    },
    days: { '01': 'c2' },
  },
};

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

  for (const [name, post] of Object.entries(posts)) {
    const out = path.join(root, name);
    fs.mkdirSync(out, { recursive: true });
    for (const [n, f] of Object.entries(post.approved)) {
      fs.copyFileSync(path.join(__dirname, 'approved', f), path.join(out, `${n}-${f}`));
    }
    for (const [n, id] of Object.entries(post.days)) {
      const el = await p.$(`.slide[data-id="${id}"]`);
      if (!el) throw new Error(`no slide with data-id="${id}"`);
      await el.screenshot({ path: path.join(out, `${n}-DAYS.png`) });
    }
  }
  await b.close();
})();
