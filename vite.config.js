import { defineConfig } from 'vite';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

// Einfache Include-Funktion für gemeinsame Bausteine (Header, Footer):
// <!-- @include header page="fuehrerschein" -->
// Im Baustein setzt {{current:fuehrerschein}} ein aria-current="page", wenn die Seite passt.
function includes() {
  const render = (html, depth = 0) =>
    html.replace(/<!--\s*@include\s+([\w-]+)((?:\s+\w+="[^"]*")*)\s*-->/g, (_, name, attrs) => {
      const params = Object.fromEntries([...attrs.matchAll(/(\w+)="([^"]*)"/g)].map((m) => [m[1], m[2]]));
      let part = readFileSync(resolve(import.meta.dirname, 'src/partials', `${name}.html`), 'utf8');
      part = part.replace(/\{\{current:([\w-]+)\}\}/g, (_, p) => (params.page === p ? 'aria-current="page"' : ''));
      part = part.replace(/\{\{(\w+)\}\}/g, (_, k) => params[k] ?? '');
      return depth < 3 ? render(part, depth + 1) : part;
    });
  return {
    name: 'html-includes',
    transformIndexHtml: { order: 'pre', handler: (html) => render(html) },
    handleHotUpdate({ file, server }) {
      if (file.includes('/src/partials/')) server.ws.send({ type: 'full-reload' });
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
