# KI-Fotos (Symbolbilder)

Erzeugt am 03.10.2026 in Abacus AI Studio (Konto von Fabian, Modell GPT Image 2.5, Qualität „High“),
je zwei Varianten pro Motiv. Stil für alle: ruhiges Editorial-Foto, warmes Licht, gedämpfte
Salbei-/Beigetöne, leichte Körnung, keine Gesichter, keine Schrift, keine Logos.

| Datei (Auswahl) | Motiv | Format | eingesetzt |
|---|---|---|---|
| `strauch-ki-hero-a.png` | Fahrschulauto in ruhiger Straße, Abendlicht | 2048 × 1152 | Startseite Hero, Karussell, Kontakt-Kreis Auffrischung |
| `strauch-ki-klasse-b-b.png` | Fahrschulauto auf Schwarzwald-Landstraße | 1024 × 1280 | Kachel Klasse B, Kreis, Karussell, Kontakt-Band, 404 |
| `strauch-ki-klasse-be-a.png` | Fahrschulauto mit Kastenanhänger | 1024 × 1280 | Kachel Klasse BE, Kreis |
| `strauch-ki-b197-a.png` | Automatik-Wählhebel, Schaltknüppel dahinter | 1024 × 1280 | Kachel B197, Kreis, B197-Band |
| `strauch-ki-bf17-a.png` | Fahrerin am Steuer, Begleitperson von hinten | 1024 × 1280 | Kachel BF17, Kreis, Karte „Mit 16 anfangen“ |
| `strauch-ki-lkw-b.png` | Lkw auf der Autobahn bei Abendlicht | 1024 × 1280 | Kachel BKF, Kopf der BKF-Seite, Karussell |
| `strauch-ki-theorie-b.png` | heller Theorieraum, leer | 1536 × 1024 | Schnellkurs-Karte, Kreis Schnellkurs |

Die anderen Varianten (`-a`/`-b`) bleiben als Ersatz liegen.

**Logo:** Das echte Logo wird mit `python3 scripts/fotos.py` perspektivisch auf Fahrertür bzw.
Trailer gesetzt (multiplizierend, damit Licht und Schatten bleiben). Positionen stehen dort in `JOBS`.
Danach `npm run images`.

**Kennzeichnung:** Im Footer steht, dass Fahrzeug- und Raumbilder KI-erzeugte Symbolbilder sind;
die Alt-Texte enden mit „(KI-Symbolbild)“. Die Teamfotos sind echt.
