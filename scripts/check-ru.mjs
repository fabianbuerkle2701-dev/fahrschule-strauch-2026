import puppeteer from 'puppeteer-core';
const b = await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:'new'});
const allow = /Schwarzwaldstra(ß|ss)e|Lahr|Viktor Strauch|Peter Harter|Gerold Remmele|Nadine Dürr|Fahrschulmanager|Fahren Lernen MAX|Heinrich Vogel|Credit Europe Bank|STARTHILFE|Deutsche Version|Impressum|Fahrschule Strauch|Fahrschule Viktor Strauch|BKrFQG|Frankfurt/g;
for (const path of ['/ru/','/ru/fuehrerschein/','/ru/berufskraftfahrer/','/ru/ueber-uns/','/ru/anmeldung/']) {
  const p = await b.newPage(); await p.goto('http://localhost:5191'+path,{waitUntil:'networkidle0'});
  const hits = await p.evaluate((allowSrc) => {
    const allow = new RegExp(allowSrc, 'g');
    const out = [];
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n; while ((n = w.nextNode())) {
      const el = n.parentElement; if (!el || el.closest('script,style,[lang="de"],svg')) continue;
      const t = n.textContent.replace(allow,'').trim(); if (!t) continue;
      if (/[äöüßÄÖÜ]|\b(und|der|die|das|mit|für|Klasse|Fahr|bei|ist|nicht|oder|dich|du)\b/.test(t) && !/[а-яё]/i.test(t)) out.push(t.slice(0,80));
    }
    // auch Attribute
    document.querySelectorAll('[alt],[aria-label],[title],[data-quote],[data-role]').forEach(e=>{ if(e.closest('[lang="de"]')) return; for (const a of ['alt','aria-label','title','data-quote','data-role']) { const v=(e.getAttribute(a)||'').replace(allow,'').trim(); if (v && /[äöüß]|\b(und|der|die|mit|für|Klasse|zur|Startseite)\b/.test(v) && !/[а-яё]/i.test(v)) out.push(a+': '+v.slice(0,70)); } });
    return [...new Set(out)];
  }, allow.source);
  console.log(path, hits.length ? hits : 'sauber');
  await p.close();
}
await b.close();
