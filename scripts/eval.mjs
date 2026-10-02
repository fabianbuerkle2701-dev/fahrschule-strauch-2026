// QA-Hilfe: node scripts/eval.mjs <pfad> <breite>x<höhe> "<js-ausdruck>"
import puppeteer from 'puppeteer-core';
const [, , path = '/', size = '1440x900', expr = 'document.title'] = process.argv;
const [w, h] = size.split('x').map(Number);
const b = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new' });
const p = await b.newPage();
await p.setViewport({ width: w, height: h, isMobile: w < 768, hasTouch: w < 768 });
await p.goto('http://localhost:5191' + path, { waitUntil: 'networkidle0' });
await new Promise((r) => setTimeout(r, 800));
console.log(await p.evaluate(`(async () => { return ${expr} })()`));
await b.close();
