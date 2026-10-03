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
  { src: 'photos/fuhrpark.jpg', out: 'fuhrpark-hero', crop: [0, 120, 2400, 1250], widths: [640, 960, 1440, 2000] },
  // Teamporträts (Quelle 1200×900), Hochformat 4:5 mit Person und Fahrzeugfront
  { src: 'photos/viktor-strauch.jpg', out: 'team-viktor-strauch', crop: [480, 0, 720, 900], widths: [400, 640, 720] },
  { src: 'photos/peter-harter.jpg', out: 'team-peter-harter', crop: [440, 0, 720, 900], widths: [400, 640, 720] },
  { src: 'photos/gerold-remmele.jpg', out: 'team-gerold-remmele', crop: [420, 0, 720, 900], widths: [400, 640, 720] },
  { src: 'photos/nadine-duerr.jpg', out: 'team-nadine-duerr', crop: [470, 0, 720, 900], widths: [400, 640, 720] },
  // Querformat (Instagram-Karussell auf der Startseite)
  { src: 'photos/nadine-duerr.jpg', out: 'team-nadine-duerr-wide', crop: [0, 0, 1200, 900], widths: [640, 960, 1200] },
  // Avatare (quadratisch, Gesicht)
  { src: 'photos/peter-harter.jpg', out: 'avatar-peter-harter', crop: [770, 0, 180, 180], widths: [160] },
  { src: 'photos/gerold-remmele.jpg', out: 'avatar-gerold-remmele', crop: [850, 90, 200, 200], widths: [160] },
  { src: 'photos/nadine-duerr.jpg', out: 'avatar-nadine-duerr', crop: [840, 0, 180, 180], widths: [160] },
  { src: 'photos/viktor-strauch.jpg', out: 'avatar-viktor-strauch', crop: [1000, 40, 180, 180], widths: [160] },
  // Schaufenster mit Logo und Viktor Strauch am Auto (Karussell, Schnellkurs-Karte)
  { src: 'photos/gerold-remmele.jpg', out: 'intro-schaufenster', crop: [640, 0, 560, 442], widths: [480, 720] },
  { src: 'photos/viktor-strauch.jpg', out: 'intro-viktor', crop: [0, 60, 1200, 800], widths: [640, 960, 1200] },
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

// Illustrationen (generiert, Logo eingesetzt, freigestellt: scripts/illustrations.py)
import { readdir } from 'node:fs/promises';
for (const file of (await readdir(path.join(SRC, 'illustrationen/final'))).filter((f) => f.endsWith('.png'))) {
  const name = path.basename(file, '.png');
  const input = sharp(path.join(SRC, 'illustrationen/final', file));
  const { width, height } = await input.metadata();
  const steps = name.startsWith('hero') ? [960, 1440, 2000, width] : [480, 800, width];
  const widths = steps.filter((w, i, a) => w <= width && a.indexOf(w) === i);
  manifest[`ill-${name}`] = { width, height, widths };
  for (const w of widths) {
    const pipe = input.clone().resize({ width: w });
    await pipe.clone().avif({ quality: 60, effort: 6 }).toFile(path.join(OUT, `ill-${name}-${w}.avif`));
    await pipe.clone().webp({ quality: 82, alphaQuality: 90 }).toFile(path.join(OUT, `ill-${name}-${w}.webp`));
  }
  console.log('✓ ill-' + name, width + '×' + height, widths.join('/'));
}

// Fotos (KI-erzeugt in Abacus AI Studio, echtes Logo per scripts/fotos.py aufgesetzt)
for (const file of (await readdir(path.join(SRC, 'fotos-ki/final'))).filter((f) => f.endsWith('.png'))) {
  const name = `foto-${path.basename(file, '.png')}`;
  const input = sharp(path.join(SRC, 'fotos-ki/final', file));
  const { width, height } = await input.metadata();
  const steps = width >= 2000 ? [960, 1440, width] : width >= 1500 ? [640, 1024, width] : [480, 800, width];
  const widths = steps.filter((w, i, a) => w <= width && a.indexOf(w) === i);
  manifest[name] = { width, height, widths };
  for (const w of widths) {
    const pipe = input.clone().resize({ width: w });
    await pipe.clone().avif({ quality: 55, effort: 6 }).toFile(path.join(OUT, `${name}-${w}.avif`));
    await pipe.clone().webp({ quality: 78 }).toFile(path.join(OUT, `${name}-${w}.webp`));
  }
  console.log('✓', name, widths.join('/'));
}

// Hero-Ausschnitt für schmale Bildschirme: rechte Hälfte der Szene ohne Ladenschild
// (sonst stünde das Schild-Logo direkt unter dem Logo der Kopfzeile), mit Figuren und Auto samt Logo
{
  const crop = { left: 1700, top: 300, width: 1468, height: 782 };
  const input = sharp(path.join(SRC, 'illustrationen/final/hero-szene.png')).extract(crop);
  const widths = [480, 800, 1200, 1468];
  manifest['ill-hero-rechts'] = { width: crop.width, height: crop.height, widths };
  for (const w of widths) {
    const pipe = input.clone().resize({ width: w });
    await pipe.clone().avif({ quality: 60, effort: 6 }).toFile(path.join(OUT, `ill-hero-rechts-${w}.avif`));
    await pipe.clone().webp({ quality: 82 }).toFile(path.join(OUT, `ill-hero-rechts-${w}.webp`));
  }
  console.log('✓ ill-hero-rechts');
}

// Vorschaubilder der Formulare (erste PDF-Seite, erzeugt mit: sips -s format png -Z 1400 datei.pdf)
for (const file of (await readdir(path.join(SRC, 'pdf-vorschau'))).filter((f) => f.endsWith('.png'))) {
  const name = `pdf-${path.basename(file, '.png')}`;
  const input = sharp(path.join(SRC, 'pdf-vorschau', file)).flatten({ background: '#ffffff' });
  const { width, height } = await sharp(path.join(SRC, 'pdf-vorschau', file)).metadata();
  const widths = [400, 700];
  manifest[name] = { width, height, widths };
  for (const w of widths) {
    const pipe = input.clone().resize({ width: w });
    await pipe.clone().avif({ quality: 58, effort: 6 }).toFile(path.join(OUT, `${name}-${w}.avif`));
    await pipe.clone().webp({ quality: 80 }).toFile(path.join(OUT, `${name}-${w}.webp`));
  }
  console.log('✓', name);
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

await writeFile(path.join('assets-src', 'image-manifest.json'), JSON.stringify(manifest, null, 2));
console.log('fertig');
