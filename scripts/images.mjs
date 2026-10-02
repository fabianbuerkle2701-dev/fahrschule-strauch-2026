// Erzeugt optimierte Bildvarianten (AVIF + WebP, mehrere Breiten) aus assets-src/.
// Aufruf: npm run images
import sharp from 'sharp';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const SRC = 'assets-src';
const OUT = 'public/images';

// crop: [left, top, width, height] in Pixeln der Quelldatei
const jobs = [
  // Fuhrpark: Team mit vier Autos vor der Fahrschule (Quelle 2400×1800)
  { src: 'photos/fuhrpark.jpg', out: 'fuhrpark-wide', crop: [0, 300, 2400, 840], widths: [640, 960, 1440, 2000] },
  { src: 'photos/fuhrpark.jpg', out: 'fuhrpark-hero', crop: [0, 120, 2400, 1250], widths: [640, 960, 1440, 2000] },
  { src: 'photos/fuhrpark.jpg', out: 'fuhrpark-close', crop: [560, 380, 1240, 780], widths: [480, 800, 1200] },
  // Teamporträts (Quelle 1200×900), Hochformat 4:5 mit Person und Fahrzeugfront
  { src: 'photos/viktor-strauch.jpg', out: 'team-viktor-strauch', crop: [480, 0, 720, 900], widths: [400, 640, 720] },
  { src: 'photos/peter-harter.jpg', out: 'team-peter-harter', crop: [440, 0, 720, 900], widths: [400, 640, 720] },
  { src: 'photos/gerold-remmele.jpg', out: 'team-gerold-remmele', crop: [420, 0, 720, 900], widths: [400, 640, 720] },
  { src: 'photos/nadine-duerr.jpg', out: 'team-nadine-duerr', crop: [470, 0, 720, 900], widths: [400, 640, 720] },
  // Querformat-Fassungen für die Über-uns-Seite
  { src: 'photos/viktor-strauch.jpg', out: 'team-viktor-strauch-wide', crop: [0, 0, 1200, 900], widths: [640, 1200] },
];

const manifest = {};

for (const job of jobs) {
  const [left, top, width, height] = job.crop;
  const base = sharp(path.join(SRC, job.src)).extract({ left, top, width, height });
  const dir = path.join(OUT);
  await mkdir(dir, { recursive: true });
  manifest[job.out] = { width, height, widths: job.widths };
  for (const w of job.widths) {
    const pipeline = base.clone().resize({ width: w, withoutEnlargement: true }).sharpen({ sigma: 0.6 });
    await pipeline.clone().avif({ quality: 52, effort: 6 }).toFile(path.join(dir, `${job.out}-${w}.avif`));
    await pipeline.clone().webp({ quality: 74 }).toFile(path.join(dir, `${job.out}-${w}.webp`));
  }
  console.log('✓', job.out);
}

// Logo: verlustarm verkleinert, als PNG (Original-Design unverändert)
await sharp(path.join(SRC, 'brand/logo.png')).png({ palette: true, quality: 90, compressionLevel: 9 }).toFile(path.join(OUT, 'logo.png'));
await sharp(path.join(SRC, 'brand/logo.png')).webp({ lossless: true }).toFile(path.join(OUT, 'logo.webp'));

// Social-Preview 1200×630 aus dem Fuhrparkfoto
await sharp(path.join(SRC, 'photos/fuhrpark.jpg'))
  .extract({ left: 0, top: 260, width: 2400, height: 1260 })
  .resize(1200, 630)
  .jpeg({ quality: 80, mozjpeg: true })
  .toFile(path.join(OUT, 'og-fahrschule-strauch.jpg'));

await writeFile(path.join(OUT, 'manifest.json'), JSON.stringify(manifest, null, 2));
console.log('fertig');
