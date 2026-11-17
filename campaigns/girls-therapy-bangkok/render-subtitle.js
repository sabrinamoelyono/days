// Render the cover title area with alternative treatments of the "after dark: Bangkok" line,
// plus a labelled contact sheet (export/subtitle-options/).
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const variants = {
  '1-same-as-title': { html: 'AFTER DARK: BANGKOK', css: 'font: 800 118px/1 "Bricolage Grotesque", sans-serif; font-stretch: 100%; font-variation-settings: "opsz" 96; letter-spacing: -.02em; color: var(--butter);' },
  '2-neon-script': { html: 'after dark: Bangkok', css: 'font: 400 170px/1 "Yellowtail", cursive; color: #FF4F8B; text-shadow: 0 0 10px rgba(255,79,139,.9), 0 0 34px rgba(215,25,90,.8), 0 0 70px rgba(215,25,90,.6);' },
  '3-neon-caps': { html: 'AFTER DARK: BANGKOK', css: 'font: 700 104px/1 "Bricolage Grotesque", sans-serif; font-stretch: 80%; letter-spacing: .06em; color: #FFE3EC; text-shadow: 0 0 8px #FF4F8B, 0 0 26px #D7195A, 0 0 60px #D7195A;' },
  '4-pen-handwritten': { html: 'after dark: Bangkok', css: 'font: 700 150px/1 "Caveat", cursive; color: #FF4F8B; transform: rotate(-3deg);' },
  '5-form-typewriter': { html: '— AFTER DARK: BANGKOK —', css: 'font: 500 66px/1 "DM Mono", monospace; letter-spacing: .14em; color: var(--butter); margin-top: 40px !important;' },
  '6-extended-wide': { html: 'AFTER DARK: BANGKOK', css: 'font: 700 72px/1 "Unbounded", sans-serif; letter-spacing: .01em; color: var(--butter); margin-top: 30px !important;' },
};
(async () => {
  const out = path.join(__dirname, 'export', 'subtitle-options');
  fs.rmSync(out, { recursive: true, force: true });
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'slides.html'), { waitUntil: 'networkidle' });
  await p.addStyleTag({ url: 'https://fonts.googleapis.com/css2?family=Yellowtail&family=Caveat:wght@700&family=Unbounded:wght@700&display=swap' });
  const cover = (await p.$$('.slide'))[0];
  const shots = [];
  for (const [name, v] of Object.entries(variants)) {
    await p.evaluate(v => {
      const el = document.querySelector('.s1 .c2');
      el.innerHTML = v.html;
      el.setAttribute('style', 'display:block; margin-top: 14px;' + v.css);
    }, v);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    const f = `${out}/${name}.png`;
    await cover.screenshot({ path: f });
    shots.push([name, f]);
  }
  // contact sheet: title area of each, labelled
  const sheet = await b.newPage({ viewport: { width: 2400, height: 1200 } });
  const cells = shots.map(([n, f]) => `<figure><div style="background-image:url(file://${f})"></div><figcaption>${n.replace(/^(\d)-/, '$1 · ').replace(/-/g, ' ')}</figcaption></figure>`).join('');
  await sheet.setContent(`<style>body{margin:0;background:#111;display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:16px;font:600 26px system-ui;color:#fff}
    figure{margin:0}figure div{height:520px;background-size:1600px 2000px;background-position:-0px -240px;width:780px;transform-origin:0 0}
    figcaption{padding:10px 4px;text-transform:capitalize}</style>${cells}`);
  await sheet.waitForTimeout(500);
  await sheet.screenshot({ path: `${out}/_sheet.png`, fullPage: true });
  await b.close();
})();
