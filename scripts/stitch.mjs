// Ganzseiten-Aufnahme in echter Fensterhöhe (Kacheln zusammengesetzt), damit svh-Einheiten stimmen.
// node scripts/stitch.mjs <pfad> <breite>x<höhe> <datei>
import puppeteer from 'puppeteer-core';
import sharp from 'sharp';
const [, , path = '/', size = '1440x900', out = 'stitch.png'] = process.argv;
const [w, h] = size.split('x').map(Number);
const b = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new', args: ['--hide-scrollbars'] });
const p = await b.newPage();
await p.setViewport({ width: w, height: h, isMobile: w < 768, hasTouch: w < 768 });
await p.goto('http://localhost:5191' + path, { waitUntil: 'networkidle0' });
await p.evaluate(() => document.querySelectorAll('img[loading="lazy"]').forEach((i) => i.setAttribute('loading', 'eager')));
await p.evaluate(() => document.querySelectorAll('[data-reveal]').forEach((e) => e.classList.add('is-visible')));
await new Promise((r) => setTimeout(r, 1500));
const total = await p.evaluate(() => document.documentElement.scrollHeight);
const tiles = [];
for (let y = 0; y < total; y += h) {
  await p.evaluate((y) => window.scrollTo(0, y), y);
  await new Promise((r) => setTimeout(r, 350));
  if (y > 0) await p.evaluate(() => (document.querySelector('[data-header]').style.visibility = 'hidden'));
  const actual = await p.evaluate(() => window.scrollY);
  tiles.push({ buf: await p.screenshot(), top: actual });
}
const composite = tiles.map((t) => ({ input: t.buf, top: t.top, left: 0 }));
await sharp({ create: { width: w, height: total, channels: 3, background: '#ffffff' } }).composite(composite).png().toFile(out);
console.log(out, total, tiles.length);
await b.close();
