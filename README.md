# Fahrschule Strauch – Website

Neubau der Website der Fahrschule Viktor Strauch in Lahr. Statisches Mehrseiten-Projekt mit Vite, ohne Framework und ohne Backend.

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
src/partials/   gemeinsame Bausteine (head, header, footer, contact, finale, symbols)
src/styles/     tokens.css, base.css, components.css, sections.css, pages.css
src/scripts/    main.js (Navigation, Reveals, Autofahrt im Ablauf, Team-Bühne, Parallaxe)
public/         Bilder, Schriften, Icons, PDFs, robots.txt, sitemap.xml, Weiterleitungen
assets-src/     Originalfotos und Logo (Provenienz in assets-src/README.md)
scripts/        images.mjs (Bildpipeline), shots.mjs und eval.mjs (QA mit Chrome)
```

Bausteine werden beim Bauen über `<!-- @include name -->` eingesetzt (kleines Plugin in `vite.config.js`).

## Veröffentlichung

- Die Seite erwartet, im Wurzelverzeichnis der Domain zu liegen (`https://www.fahrschule-strauch.de/`).
- Inhalt von `dist/` hochladen. Weiterleitungen von den alten Adressen liegen als `.htaccess` (Apache) und `_redirects` (Netlify) bei.
- Schriften, Icons und Bilder sind selbst gehostet; es werden keine Drittanbieter geladen. Externe Links: Fahrschulmanager (Online-Anmeldung), STARTHILFE, Google Maps (nur Link), Instagram, Facebook.

## Offene Punkte für die Fahrschule

1. **Telefonnummer klären**: Kopf/Footer der alten Seite nennen +49 155 60 41 04 13, Impressum, Preis-PDFs und Schaufenster 0151 42522180. Die Website nutzt die erste als Kontaktnummer, das Impressum unverändert die zweite.
2. **Datenschutzerklärung aktualisieren** (Stand 2018, nennt YouTube und TMG). Text wurde unverändert übernommen.
3. **Schnellkurs-Termine**: Der letzte Termin (24.–31.08.2026) ist vorbei; die Seite verweist auf Anfrage.
4. **Russische Fassung** von einer Muttersprachlerin oder einem Muttersprachler gegenlesen lassen. Alle Inhaltsseiten gibt es auf Russisch (Anrede „вы“); der DE/RU-Umschalter springt jeweils zur passenden Seite. Impressum, Datenschutz, PDF-Formulare und die Online-Anmeldung bleiben deutsch.
   Wichtig bei Textänderungen: deutsche Seite ändern, dann `python3 scripts/translate_ru.py` ausführen. Das Skript bricht ab, wenn ein geänderter deutscher Satz noch keine russische Entsprechung hat.
5. Fotos liegen nur in 640×480 vor (hochskaliert). Neue Fotos in höherer Auflösung würden Hero, Team-Bühne und Intro deutlich schärfer machen.
