const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const D=__dirname+'/';
(async () => { const b = await chromium.launch();
  for (const [n,h] of [['ade-poster',1920],['ade-square',1080]]) for (const [sf,suf] of [[1,''],[2,'-HD']]) {
    const p = await b.newPage({ viewport:{width:1080,height:h}, deviceScaleFactor:sf });
    await p.goto('file://'+D+n+'.html'); await p.waitForTimeout(500);
    if (sf===1) console.log(n, await p.evaluate(()=>{const f=document.querySelector('.foot'); let m=0; for(const e of document.querySelectorAll('.page > *')) if(e!==f) m=Math.max(m,e.getBoundingClientRect().bottom); return [Math.round(m), Math.round(f.getBoundingClientRect().top)]}));
    await p.screenshot({ path: D+n+suf+'.png' }); await p.close(); }
  await b.close(); })();
