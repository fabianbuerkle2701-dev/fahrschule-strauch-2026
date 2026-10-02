# Fahrschule Strauch – Website

Neubau der Website der Fahrschule Viktor Strauch in Lahr. Statisches Mehrseiten-Projekt mit Vite, ohne Framework und ohne Backend.

Aufbau, Abstände, Radien und Schriften folgen 1:1 shophoki.com (Startseite und Produktseite), Farben, Fotos und Illustrationen sind die der Fahrschule. Details in `DESIGN.md`.

## Befehle

```bash
npm install
npm run dev       # Entwicklung auf http://localhost:5173
npm run build     # fertige Seite in dist/
npm run preview   # dist/ lokal ansehen
npm run images    # Bilder aus assets-src/ neu erzeugen (AVIF + WebP)
python3 scripts/translate_ru.py   # russische Seiten aus den deutschen neu erzeugen
node scripts/check-ru.mjs         # russische Seiten auf übrig gebliebenes Deutsch prüfen (Dev-Server muss laufen)
```

## Aufbau

```text
index.html, fuehrerschein/, berufskraftfahrer/, ueber-uns/, anmeldung/, ru/, impressum/, datenschutz/, 404.html
src/partials/   gemeinsame Bausteine (head, header, footer, contact; jeweils mit -ru-Fassung)
src/styles/     tokens.css (Farben, Schriften), base.css, hoki.css (alle Bausteine nach HOKI)
src/scripts/    main.js (schwebende Kopfzeile, Menü, Reveals, Reihen mit Fortschrittsbalken, Karussell, FAQ-Filter)
public/         Bilder, Schriften, Icons, PDFs, robots.txt, sitemap.xml, Weiterleitungen
assets-src/     Originalfotos und Logo (Provenienz in assets-src/README.md)
scripts/        images.mjs (Bildpipeline), sprite.mjs (Icons), illustrations.py (Logo auf Illustrationen),
                translate_ru.py (russische Seiten), stitch.mjs, shots.mjs, eval.mjs, check-ru.mjs (QA mit Chrome)
```

Beim Bauen setzt ein kleines Plugin in `vite.config.js` zwei Kürzel ein:

- `<!-- @include name param="…" -->` fügt einen Baustein aus `src/partials/` ein.
- `<!-- @pic src="ill-auto-seite" sizes="…" alt="…" -->` erzeugt ein `<picture>` mit AVIF und WebP in allen Breiten aus `assets-src/image-manifest.json`.

Die Formular-Vorschauen (`pdf-*`) sind die ersten Seiten der PDFs, erzeugt mit `sips -s format png -Z 1400 datei.pdf --out assets-src/pdf-vorschau/name.png`, danach `npm run images`.

## Veröffentlichung

- Die Seite erwartet, im Wurzelverzeichnis der Domain zu liegen (`https://www.fahrschule-strauch.de/`).
- `dist/` vor dem Bauen löschen und frisch bauen (`rm -rf dist && npm run build`): Der Ordner liegt in iCloud, das legt sonst Kopien wie „index 2.html“ an.
- Inhalt von `dist/` hochladen. Weiterleitungen von den alten Adressen liegen als `.htaccess` (Apache) und `_redirects` (Netlify) bei.
- Schriften, Icons und Bilder sind selbst gehostet; es werden keine Drittanbieter geladen. Externe Links: Fahrschulmanager (Online-Anmeldung), STARTHILFE, Google Maps (nur Link), Instagram, Facebook.

## Vorschau auf GitHub Pages

https://fabianbuerkle2701-dev.github.io/fahrschule-strauch-2026/ (russisch: …/ru/)

Aktualisieren mit `sh scripts/deploy-pages.sh`: baut die Seite, setzt alle Pfade auf den Unterordner (`scripts/pages-base.mjs`) und schiebt `dist/` in den Branch `gh-pages`. Ein automatischer GitHub-Workflow ist nicht eingerichtet, weil die GitHub-Anmeldung keine Rechte für Workflow-Dateien hat (`gh auth refresh -s workflow` würde das ändern).

## Offene Punkte für die Fahrschule

1. **Telefonnummer klären**: Kopf/Footer der alten Seite nennen +49 155 60 41 04 13, Impressum, Preis-PDFs und Schaufenster 0151 42522180. Die Website nutzt die erste als Kontaktnummer, das Impressum unverändert die zweite.
2. **Datenschutzerklärung aktualisieren** (Stand 2018, nennt YouTube und TMG). Text wurde unverändert übernommen.
3. **Schnellkurs-Termine**: Der letzte Termin (24.–31.08.2026) ist vorbei; die Seite verweist auf Anfrage.
4. **Russische Fassung** von einer Muttersprachlerin oder einem Muttersprachler gegenlesen lassen. Alle Inhaltsseiten gibt es auf Russisch (Anrede „вы“); der DE/RU-Umschalter springt jeweils zur passenden Seite. Impressum, Datenschutz, PDF-Formulare und die Online-Anmeldung bleiben deutsch.
   Wichtig bei Textänderungen: deutsche Seite ändern, dann `python3 scripts/translate_ru.py` ausführen. Das Skript bricht ab, wenn ein geänderter deutscher Satz noch keine russische Entsprechung hat.
5. Fotos liegen nur in 640×480 vor (hochskaliert). Neue Fotos in höherer Auflösung würden die großen Fotokarten (Team mit Fuhrpark, Fahrlehrer-Kacheln) deutlich schärfer machen.
6. **Instagram-Bereich**: Die Startseite zeigt wie HOKI ein Karussell „Folge uns auf Instagram“, gefüllt mit unseren eigenen Fotos und Illustrationen (keine echten Instagram-Beiträge). Ob das Profil instagram.com/fahrschulestrauch aktiv gepflegt wird, sollte die Fahrschule bestätigen.
