// Makes og.jpg, the picture shown when someone texts or posts the link.
// Runs on GitHub (see .github/workflows/og.yml), where the real photos can load.
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve('og.html')).href);
await page.waitForFunction(() => document.body.dataset.ready !== undefined, null, { timeout: 45000 });
const loaded = Number(await page.evaluate(() => document.body.dataset.ready));
if (loaded < 2) {
  console.log(`Only ${loaded} of 3 pictures loaded, so the old og.jpg is kept.`);
} else {
  await page.waitForTimeout(400);
  await page.screenshot({ path: 'og.jpg', type: 'jpeg', quality: 88 });
  console.log(`og.jpg updated (${loaded} of 3 pictures).`);
}
await browser.close();
