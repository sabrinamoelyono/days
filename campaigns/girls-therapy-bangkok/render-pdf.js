// Compile the 4:5 feed slides (slides.html) into one PDF, one slide per page.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'slides.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.addStyleTag({ content: `
    @page { size: 1600px 2000px; margin: 0; }
    html, body { margin: 0; background: none; }
    .slide { margin: 0; break-after: page; }
    .slide:last-of-type { break-after: auto; }
    * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }` });
  await p.pdf({ path: path.join(__dirname, 'export', 'Girls-Therapy-NYE-Bangkok.pdf'), width: '1600px', height: '2000px', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
