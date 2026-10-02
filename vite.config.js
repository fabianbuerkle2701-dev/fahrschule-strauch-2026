import { defineConfig } from 'vite';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

// Einfache Include-Funktion für gemeinsame Bausteine (Header, Footer):
// <!-- @include header page="fuehrerschein" -->
// Im Baustein setzt {{current:fuehrerschein}} ein aria-current="page", wenn die Seite passt.
// Bilder: <!-- @pic src="ill-auto-seite" sizes="…" alt="…" class="…" eager="1" -->
// erzeugt <picture> mit AVIF und WebP in allen Breiten aus assets-src/image-manifest.json.
function picture(attrs) {
  const p = Object.fromEntries([...attrs.matchAll(/([\w-]+)="([^"]*)"/g)].map((m) => [m[1], m[2]]));
  const manifest = JSON.parse(readFileSync(resolve(import.meta.dirname, 'assets-src/image-manifest.json'), 'utf8'));
  const m = manifest[p.src];
  if (!m) throw new Error(`@pic: Bild ${p.src} fehlt im Manifest`);
  const set = (ext) => m.widths.map((w) => `/images/${p.src}-${w}.${ext} ${w}w`).join(', ');
  const fallback = m.widths[Math.min(1, m.widths.length - 1)];
  const load = p.eager ? 'fetchpriority="high"' : 'loading="lazy"';
  const cls = p.class ? ` class="${p.class}"` : '';
  const style = p.style ? ` style="${p.style}"` : '';
  // Bildausschnitt für schmale Bildschirme: narrow="name" narrow-media="(max-width: …)" narrow-sizes="…"
  let narrow = '';
  if (p.narrow) {
    const n = manifest[p.narrow];
    if (!n) throw new Error(`@pic: Bild ${p.narrow} fehlt im Manifest`);
    const nset = (ext) => n.widths.map((w) => `/images/${p.narrow}-${w}.${ext} ${w}w`).join(', ');
    for (const ext of ['avif', 'webp']) narrow += `<source media="${p['narrow-media']}" type="image/${ext}" srcset="${nset(ext)}" sizes="${p['narrow-sizes']}" />`;
  }
  return `<picture${cls}>${narrow}<source type="image/avif" srcset="${set('avif')}" sizes="${p.sizes}" /><img src="/images/${p.src}-${fallback}.webp" srcset="${set('webp')}" sizes="${p.sizes}" width="${m.width}" height="${m.height}" alt="${p.alt ?? ''}"${style} ${load} decoding="async" /></picture>`;
}

function includes() {
  const render = (html, depth = 0) =>
    html.replace(/<!--\s*@include\s+([\w-]+)((?:\s+\w+="[^"]*")*)\s*-->/g, (_, name, attrs) => {
      const params = Object.fromEntries([...attrs.matchAll(/(\w+)="([^"]*)"/g)].map((m) => [m[1], m[2]]));
      let part = readFileSync(resolve(import.meta.dirname, 'src/partials', `${name}.html`), 'utf8');
      part = part.replace(/\{\{current:([\w-]+)\}\}/g, (_, p) => (params.page === p ? 'aria-current="page"' : ''));
      part = part.replace(/\{\{(\w+)\}\}/g, (_, k) => params[k] ?? '');
      return depth < 3 ? render(part, depth + 1) : part;
    }).replace(/<!--\s*@pic((?:\s+[\w-]+="[^"]*")*)\s*-->/g, (_, attrs) => picture(attrs));
  return {
    name: 'html-includes',
    transformIndexHtml: { order: 'pre', handler: (html) => render(html) },
    handleHotUpdate({ file, server }) {
      if (file.includes('/src/partials/') || file.endsWith('image-manifest.json')) server.ws.send({ type: 'full-reload' });
    },
  };
}

const pages = [
  '', 'fuehrerschein', 'berufskraftfahrer', 'ueber-uns', 'anmeldung', 'impressum', 'datenschutz',
  'ru', 'ru/fuehrerschein', 'ru/berufskraftfahrer', 'ru/ueber-uns', 'ru/anmeldung',
];

export default defineConfig({
  plugins: [includes()],
  build: {
    rollupOptions: {
      input: Object.fromEntries([
        ...pages.map((p) => [p.replace('/', '-') || 'home', resolve(import.meta.dirname, p, 'index.html')]),
        ['404', resolve(import.meta.dirname, '404.html')],
      ]),
    },
  },
});
