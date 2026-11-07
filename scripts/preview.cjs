// Screenshots + a scroll video of the page with real pictures (run by .github/workflows/preview.yml)
const { chromium } = require('playwright'); const fs = require('fs');
const URL = 'http://127.0.0.1:8899/index.html'; fs.mkdirSync('shots', { recursive: true });
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const b = await chromium.launch();
  // warm the picture cache once so every shot has photos
  for (const [tag, w, h, scheme, dsf] of [['desktop-light', 1440, 900, 'light', 2], ['desktop-dark', 1440, 900, 'dark', 2], ['tablet-light', 820, 1180, 'light', 2], ['phone-light', 390, 844, 'light', 3], ['phone-dark', 390, 844, 'dark', 3]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, colorScheme: scheme, deviceScaleFactor: dsf }); const p = await ctx.newPage();
    await p.goto(URL); await sleep(6000); await p.reload(); await sleep(4000);
    const stops = [['0-hero', 0], ['1-mid', .4], ['2-shelf', 1]];
    for (const [n, f] of stops) { await p.evaluate(f => { const hh = document.querySelector('#hero'); scrollTo(0, (hh.offsetHeight - innerHeight) * f); }, f); await sleep(2200); await p.screenshot({ path: `shots/${tag}-${n}.png` }); }
    for (const id of ['picks', 'how', 'match', 'share', 'private', 'wall', 'final']) { await p.evaluate(s => document.getElementById(s).scrollIntoView({ block: 'start' }), id); await sleep(2000); await p.screenshot({ path: `shots/${tag}-s-${id}.png` }); }
    await ctx.close();
  }
  // scroll videos
  for (const [tag, w, h] of [['desktop', 1440, 900], ['phone', 390, 844]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, colorScheme: 'light', recordVideo: { dir: 'shots/vid-' + tag, size: { width: w, height: h } } }); const p = await ctx.newPage();
    await p.goto(URL); await sleep(5000);
    const total = await p.evaluate(() => document.querySelector('#hero').offsetHeight + innerHeight * 3);
    for (let y = 0; y <= total; y += 14) { await p.mouse.wheel(0, 14); await sleep(16); }
    await sleep(1500); await ctx.close();
  }
  await b.close();
})();
