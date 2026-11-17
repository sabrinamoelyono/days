// Render the cover on alternative, non-film backgrounds (export/background-options/).
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

// generic, made-up skyline silhouette (not a specific landmark)
function skyline() {
  const b = [[0,180],[70,260],[130,210],[190,330],[250,240],[300,420],[340,300],[400,520],[455,360],[520,280],[575,610],[625,380],[690,300],[740,470],[800,340],[860,560],[915,400],[980,300],[1040,500],[1100,350],[1160,640],[1215,420],[1280,330],[1340,480],[1400,280],[1460,380],[1520,240],[1600,300]];
  let d = 'M0 2000 ';
  for (let i = 0; i < b.length - 1; i++) { const [x, h] = b[i], x2 = b[i + 1][0]; d += `L${x} ${2000 - h} L${x2} ${2000 - h} `; }
  d += 'L1600 2000 Z';
  // windows
  let w = '';
  for (let i = 0; i < 260; i++) { const x = (i * 97) % 1590, y = 2000 - 40 - ((i * 53) % 520); w += `<rect x="${x}" y="${y}" width="8" height="12" fill="#F1DDAE" opacity="${0.25 + (i % 5) * 0.12}"/>`; }
  return `<svg viewBox="0 0 1600 2000" style="position:absolute;inset:0;z-index:3" preserveAspectRatio="none"><defs><clipPath id="sk"><path d="${d}"/></clipPath></defs><path d="${d}" fill="#14060F" opacity=".92"/><g clip-path="url(#sk)">${w}</g></svg>`;
}
function bubbles() {
  let c = '';
  for (let i = 0; i < 70; i++) {
    const x = (i * 211) % 1600, y = (i * 389) % 2000, r = 3 + (i * 7) % 22;
    c += `<circle cx="${x}" cy="${y}" r="${r}" fill="none" stroke="#F1DDAE" stroke-width="${r > 14 ? 3 : 2}" opacity="${0.18 + (i % 4) * 0.12}"/>`;
  }
  return `<svg viewBox="0 0 1600 2000" style="position:absolute;inset:0;z-index:3">${c}</svg>`;
}

const options = {
  '1-midnight-glow': { bg: 'radial-gradient(120% 70% at 50% 108%, #8A1442 0%, #4A0E3A 38%, #2E0B33 62%, #1A0619 100%)' },
  '2-skyline': { bg: 'linear-gradient(180deg, #14060F 0%, #2E0B33 45%, #7A1240 85%, #C7184F 100%)', extra: skyline() },
  '3-champagne-bubbles': { bg: 'radial-gradient(90% 60% at 50% 35%, #44103F 0%, #2E0B33 55%, #1A0619 100%)', extra: bubbles() },
  '4-blush-daylight': { bg: '#F6D7DF', light: true },
};

(async () => {
  const out = path.join(__dirname, 'export', 'background-options');
  fs.rmSync(out, { recursive: true, force: true });
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  for (const [name, o] of Object.entries(options)) {
    const p = await b.newPage({ viewport: { width: 1600, height: 2000 } });
    await p.goto('file://' + path.join(__dirname, 'slides.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.evaluate(o => {
      const s = document.querySelector('.s1');
      s.classList.add('clean');
      s.querySelector('.photo').remove();
      s.querySelector('.shade').remove();
      s.style.background = o.bg;
      if (o.extra) s.insertAdjacentHTML('afterbegin', o.extra);
      if (o.light) {
        s.style.color = 'var(--ink)';
        s.style.setProperty('--rule', 'rgba(34,9,31,.35)');
        s.querySelector('.logo').style.backgroundImage = 'url(img/days-cherry.png)';
        s.querySelector('.title h1').style.color = 'var(--red)';
        s.querySelector('.c2').style.color = 'var(--accent)';
        s.querySelector('.rx').style.background = '#fff';
        s.querySelector('.rx').style.boxShadow = '0 24px 50px rgba(46,11,51,.18)';
        s.querySelector('.badge').style.background = 'var(--red)';
        s.querySelector('.badge').style.color = 'var(--champ)';
        s.querySelector('.badge i').style.color = 'var(--butter)';
        s.querySelector('.chrome.bot').style.color = 'var(--ink)';
      }
    }, o);
    await p.waitForTimeout(200);
    await (await p.$('.s1')).screenshot({ path: `${out}/cover-bg-${name}.png` });
    await p.close();
  }
  await b.close();
})();
