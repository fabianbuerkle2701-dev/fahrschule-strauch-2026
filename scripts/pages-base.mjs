// Setzt nach dem Bauen alle wurzelbezogenen Pfade (/images/…, /fuehrerschein/ …) auf einen Unterordner,
// damit die Seite unter https://<name>.github.io/<repo>/ läuft. Für die echte Domain nicht nötig.
// Aufruf: node scripts/pages-base.mjs /fahrschule-strauch-2026
import { readdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const base = (process.argv[2] || '').replace(/\/$/, '');
if (!base.startsWith('/')) throw new Error('Unterordner fehlt, z. B. /fahrschule-strauch-2026');

const files = [];
async function walk(dir) {
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) await walk(p);
    else if (/\.(html|css)$/.test(e.name)) files.push(p);
  }
}
await walk('dist');

const fix = (url) => (url.startsWith('/') && !url.startsWith('//') ? base + url : url);
for (const file of files) {
  let s = await readFile(file, 'utf8');
  if (file.endsWith('.html')) {
    s = s.replace(/\b(href|src|action)="([^"]*)"/g, (_, a, v) => `${a}="${fix(v)}"`);
    s = s.replace(/\b(srcset|imagesrcset)="([^"]*)"/g, (_, a, v) => `${a}="${v.split(',').map((part) => part.replace(/^(\s*)(\S+)/, (m, sp, u) => sp + fix(u))).join(',')}"`);
  }
  s = s.replace(/url\((['"]?)(\/[^)'"]*)\1\)/g, (_, q, u) => `url(${q}${fix(u)}${q})`);
  await writeFile(file, s);
}
console.log(`✓ ${files.length} Dateien auf ${base}/ umgestellt`);
