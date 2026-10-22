const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const D=__dirname+'/';
(async () => { const b = await chromium.launch();
  for (const [n,h] of [['ade-poster-b',1920],['ade-square-b',1080]]) for (const [sf,suf] of [[1,''],[2,'-HD']]) {
    const p = await b.newPage({ viewport:{width:1080,height:h}, deviceScaleFactor:sf });
    await p.goto('file://'+D+n+'.html'); await p.waitForTimeout(500);
    if (sf===1) console.log(n, await p.evaluate(()=>{const c=document.querySelector('.cards,.grid'); return [Math.round(c.getBoundingClientRect().bottom), Math.round(document.querySelector('.foot').getBoundingClientRect().top)]}));
    await p.screenshot({ path: D+n+suf+'.png' }); await p.close(); }
  await b.close(); })();
