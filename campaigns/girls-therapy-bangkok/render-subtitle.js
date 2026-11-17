// Render the cover with alternative treatments of the "after dark: Bangkok" line (export/subtitle-options/).
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const variants = {
  '1-playfair-italic': { html: 'after dark: Bangkok', css: 'font: italic 600 140px/1 "Playfair Display", serif; letter-spacing: -.01em; color: var(--butter);' },
  '2-caps-plus-italic': { html: '<span style="font: 800 92px/1 \'Bricolage Grotesque\'; font-stretch: 80%; letter-spacing: .04em; vertical-align: 22px; margin-right: 18px">AFTER DARK:</span>Bangkok', css: 'font: italic 600 170px/1 "Playfair Display", serif; color: var(--butter);' },
  '3-instrument-serif': { html: 'after dark: Bangkok', css: 'font: italic 400 170px/1 "Instrument Serif", serif; letter-spacing: -.01em; color: var(--butter);' },
  '4-gloock': { html: 'After Dark: Bangkok', css: 'font: 400 128px/1 "Gloock", serif; letter-spacing: -.01em; color: var(--butter);' },
};
(async () => {
  const out = path.join(__dirname, 'export', 'subtitle-options');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'slides.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const cover = (await p.$$('.slide'))[0];
  for (const [name, v] of Object.entries(variants)) {
    await p.evaluate(v => {
      const el = document.querySelector('.s1 .c2');
      el.innerHTML = v.html;
      el.setAttribute('style', v.css + 'display:block; margin-top: 14px;');
    }, v);
    await p.evaluate(() => document.fonts.ready);
    await cover.screenshot({ path: `${out}/${name}.png` });
  }
  await b.close();
})();
