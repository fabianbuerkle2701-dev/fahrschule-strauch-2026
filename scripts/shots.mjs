// Screenshots für die QA: node scripts/shots.mjs <url-pfad> <breite>x<höhe> <datei> [full] [scrollTo-Selector]
import puppeteer from 'puppeteer-core';
const [, , path = '/', size = '1440x900', out = 'shot.png', mode = 'view', target = ''] = process.argv;
const [w, h] = size.split('x').map(Number);
const browser = await puppeteer.launch({
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  headless: 'new',
  args: ['--hide-scrollbars'],
});
const page = await browser.newPage();
await page.setViewport({ width: w, height: h, deviceScaleFactor: 1, isMobile: w < 768, hasTouch: w < 768 });
const errors = [];
page.on('console', (m) => m.type() === 'error' && errors.push(m.text()));
page.on('pageerror', (e) => errors.push(e.message));
page.on('requestfailed', (r) => errors.push('FAILED ' + r.url()));
page.on('response', (r) => r.status() >= 400 && errors.push(r.status() + ' ' + r.url()));
await page.goto('http://localhost:5191' + path, { waitUntil: 'networkidle0' });
await new Promise((r) => setTimeout(r, 1800));
if (mode === 'full') {
  // einmal durchscrollen, damit Lazy-Loading-Bilder laden
  await page.evaluate(async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 600) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 60));
    }
    window.scrollTo(0, 0);
  });
  await new Promise((r) => setTimeout(r, 800));
  // alle Reveals sofort sichtbar, damit der ganzseitige Screenshot vollständig ist
  await page.evaluate(() => document.querySelectorAll('[data-reveal]').forEach((e) => e.classList.add('is-visible')));
  await new Promise((r) => setTimeout(r, 1200));
}
if (target) {
  await page.evaluate((sel) => {
    document.querySelectorAll('[data-reveal]').forEach((e) => e.classList.add('is-visible'));
    const el = document.querySelector(sel);
    el && el.scrollIntoView({ block: sel.startsWith('[data-step') ? 'center' : 'start', behavior: 'instant' });
  }, target);
  await new Promise((r) => setTimeout(r, 900));
}
await page.screenshot({ path: out, fullPage: mode === 'full' });
const sw = await page.evaluate(() => document.documentElement.scrollWidth);
console.log(out, 'scrollWidth', sw, 'errors', JSON.stringify(errors));
await browser.close();
