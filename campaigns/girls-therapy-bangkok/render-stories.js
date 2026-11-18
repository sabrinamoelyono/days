// Render each slide as a 9:16 Instagram Story (export/stories/, 1080×1920).
// The 4:5 layout sits centred in a 1600×2844 canvas; background, cover photo and grain
// run full height, so the extra space top and bottom becomes Instagram's UI safe zone.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { execFileSync } = require('child_process');

const W = 1600, H = 2844, FRAME = 2000, OFF = (H - FRAME) / 2;
const names = ['01-cover', '02-safe-space', '03-treatment', '04-two-sessions', '05-cool-down', '06-fine-print'];

(async () => {
  const out = path.join(__dirname, 'export', 'stories');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: W, height: H } });
  await p.goto('file://' + path.join(__dirname, 'slides.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.evaluate(({ W, H, OFF }) => {
    const css = document.createElement('style');
    css.textContent = `
      body { background: #444; }
      .story { width: ${W}px; height: ${H}px; position: relative; overflow: hidden; margin: 0 auto 40px; }
      .story > .slide { position: absolute; left: 0; top: ${OFF}px; margin: 0; background: transparent !important; overflow: visible; }
      .story > .slide::after { display: none; }
      .story::after { content: ""; position: absolute; inset: 0; pointer-events: none; z-index: 50;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E");
        opacity: .22; mix-blend-mode: multiply; }
      .story > .photo, .story > .shade { position: absolute; inset: 0; }
      .story > .photo { background-size: cover; background-position: center; filter: saturate(1.15) contrast(1.05); }
      .story > .shade { z-index: 1;
        background: linear-gradient(180deg, rgba(18,10,12,.95) 0%, rgba(18,10,12,.55) 20%, rgba(18,10,12,.2) 45%, rgba(18,10,12,.2) 58%, rgba(18,10,12,.9) 85%, rgba(18,10,12,.97) 100%); }
      .story > .slide { z-index: 2; }`;
    document.head.appendChild(css);
    for (const s of [...document.querySelectorAll('body > .slide')]) {
      const story = document.createElement('div');
      story.className = 'story';
      story.style.background = getComputedStyle(s).backgroundColor;
      s.replaceWith(story);
      story.appendChild(s);
      // cover: move the photo and shade up to the full-height story
      const photo = s.querySelector(':scope > .photo'), shade = s.querySelector(':scope > .shade');
      if (photo && shade) { story.prepend(shade); story.prepend(photo); }
    }
  }, { W, H, OFF });
  await p.waitForTimeout(300);
  const stories = await p.$$('.story');
  for (let i = 0; i < stories.length; i++) {
    const big = path.join(out, `_tmp-${i}.png`);
    await stories[i].screenshot({ path: big });
    execFileSync('python3', ['-c',
      'import sys;from PIL import Image;Image.open(sys.argv[1]).convert("RGB").resize((1080,1920),Image.LANCZOS).save(sys.argv[2],quality=95)',
      big, path.join(out, `girls-therapy-story-${names[i]}.png`)]);
    fs.unlinkSync(big);
  }
  await b.close();
})();
