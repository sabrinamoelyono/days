const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const D=__dirname+'/';
const names=['00-invite','01-lineup','02-topics','03-why','04-days'];
(async () => {
  const b = await chromium.launch();
  for (const n of names) for (const [sf,suf] of [[1,''],[2,'-HD']]) {
    const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: sf });
    await p.goto('file://'+D+n+'.html'); await p.waitForTimeout(400);
    if (sf===1) {
      const r = await p.evaluate(()=>{
        const foot=document.querySelector('.logos')||document.querySelector('.page > .row');
        let max=0; for (const el of document.querySelectorAll('.page > *')) { if (el===foot) continue; max=Math.max(max, el.getBoundingClientRect().bottom); }
        return {contentBottom:Math.round(max), footTop:Math.round(foot.getBoundingClientRect().top)};
      });
      console.log(n, JSON.stringify(r), 'gap', r.footTop-r.contentBottom);
    }
    await p.screenshot({ path: D+n+suf+'.png' }); await p.close();
  }
  await b.close();
})();
