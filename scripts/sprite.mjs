// Baut public/icons/sprite.svg aus Phosphor Icons (MIT).
// Aufruf: node scripts/sprite.mjs
import { readFileSync, writeFileSync } from 'node:fs';

const DIR = 'node_modules/@phosphor-icons/core/assets';
// [id, Phosphor-Name, Gewicht]
const icons = [
  ['phone', 'phone', 'regular'], ['arrow-right', 'arrow-right', 'bold'], ['arrow-left', 'arrow-left', 'bold'],
  ['arrow-up-right', 'arrow-up-right', 'bold'], ['map-pin', 'map-pin', 'regular'], ['envelope', 'envelope', 'regular'],
  ['plus', 'plus', 'bold'], ['list', 'list', 'regular'], ['x', 'x', 'regular'], ['instagram-logo', 'instagram-logo', 'regular'],
  ['facebook-logo', 'facebook-logo', 'fill'], ['file-pdf', 'file-pdf', 'regular'], ['clock', 'clock', 'regular'],
  ['navigation-arrow', 'navigation-arrow', 'regular'], ['check', 'check', 'bold'], ['caret-down', 'caret-down', 'bold'],
  ['steering-wheel', 'steering-wheel', 'regular'], ['chalkboard-teacher', 'chalkboard-teacher', 'regular'],
  ['seal-check', 'seal-check', 'regular'], ['clipboard-text', 'clipboard-text', 'regular'], ['road-horizon', 'road-horizon', 'regular'],
  ['translate', 'translate', 'regular'], ['device-mobile', 'device-mobile', 'regular'], ['wallet', 'wallet', 'regular'],
  ['calendar-check', 'calendar-check', 'regular'], ['gear-six', 'gear-six', 'regular'], ['users-three', 'users-three', 'regular'],
  ['eye', 'eye', 'regular'], ['first-aid', 'first-aid', 'regular'], ['identification-card', 'identification-card', 'regular'],
  ['certificate', 'certificate', 'regular'], ['truck', 'truck', 'regular'], ['shield-check', 'shield-check', 'regular'],
  ['lightning', 'lightning', 'regular'], ['moon-stars', 'moon-stars', 'regular'], ['snowflake', 'snowflake', 'regular'],
  ['package', 'package', 'regular'], ['warning-circle', 'warning-circle', 'regular'], ['heartbeat', 'heartbeat', 'regular'],
  ['leaf', 'leaf', 'regular'], ['camera', 'camera', 'regular'], ['images', 'images', 'regular'], ['chat-circle', 'chat-circle', 'regular'], ['whatsapp-logo', 'whatsapp-logo', 'regular'],
];

let out = '<svg xmlns="http://www.w3.org/2000/svg">\n<!-- Phosphor Icons (MIT), gebaut mit scripts/sprite.mjs -->\n';
for (const [id, name, weight] of icons) {
  const file = weight === 'regular' ? `${DIR}/regular/${name}.svg` : `${DIR}/${weight}/${name}-${weight}.svg`;
  const svg = readFileSync(file, 'utf8');
  const inner = svg.replace(/^[\s\S]*?<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '').replace(/<rect width="256" height="256" fill="none"\/>/, '');
  out += `<symbol id="i-${id}" viewBox="0 0 256 256" fill="currentColor">${inner.trim()}</symbol>\n`;
}
out += '</svg>\n';
writeFileSync('public/icons/sprite.svg', out);
console.log(`✓ ${icons.length} Icons`);
