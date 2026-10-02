# Illustrationen zum Austausch

**Stand 02.10.2026:** Sechs Illustrationen sind generiert (inklusive der Hero-Szene auf der Startseite), alle tragen das echte Logo der Fahrschule. Die fünf kleineren sind mit dem echten Logo versehen und eingebaut (Auto, Auto mit Anhänger, Automatik/Schaltung, Begleitetes Fahren, Lkw). Herkunft und Job-Nummern stehen in `assets-src/illustrationen/README.md`. Das Straßenschild (Kontakt auf der Anmeldeseite) ist weiterhin SVG, mit Logo-Tafel. Seit dem Umbau nach HOKI-Vorbild gibt es kein fahrendes Auto im Ablauf mehr. Ein Bild lässt sich austauschen, indem die PNG in `assets-src/illustrationen/` ersetzt und danach `python3 scripts/illustrations.py` und `npm run images` ausgeführt werden (Logo-Position in `scripts/illustrations.py` anpassen).

Alle selbst gezeichneten SVG-Illustrationen der Website, mit den Maßen, die neue (generierte) Bilder haben sollten. Fotos sind nicht betroffen.

**So geht der Austausch:** Lege die fertigen Dateien unter dem angegebenen Namen in `assets-src/illustrationen/` ab (PNG mit transparentem Hintergrund, wo angegeben) und sag Bescheid. Ich baue sie dann ein: Bildvarianten in AVIF und WebP, Lazy-Loading, Alt-Text, die bestehenden Hover-Bewegungen und die russischen Seiten gleich mit.

## Stil, damit alles zusammenpasst

- Ein Stil für alle Bilder: gleiche Perspektive, gleiche Lichtrichtung, gleiche Strichstärke oder Materialität.
- Farben der Marke: Petrol `#0199A6`, dunkles Petrol `#0E3B3F`, Mint `#E3F3F4`, Grau `#ACADAF`, Weiß. Keine weiteren Akzentfarben.
- Die Fahrschulautos sind weiß mit petrolfarbenem Dachschild und einem Band aus schrägen Petrol-Streifen an der Flanke, wie die echten Autos.
- Kein Text, keine Kennzeichen, keine fremden Logos im Bild.
- Freigestellt (transparenter Hintergrund), mit etwas Rand, damit nichts abgeschnitten wird.

## Die Stellen

| Datei | Motiv | Seitenverhältnis | Mindestgröße | Hintergrund | Wo es erscheint |
|---|---|---|---|---|---|
| `auto-seite.png` | Fahrschulauto (kompakter SUV) in Seitenansicht, nach rechts | 2,2 : 1 | 1320 × 600 px | transparent, steht auf hellem Mint bzw. Weiß | Startseite Kachel „Klasse B“, Führerschein-Seite Kreis „Klasse B“, Instagram-Karussell, 404-Seite |
| `auto-anhaenger.png` | dasselbe Auto mit Kastenanhänger, nach rechts | 3,5 : 1 | 2080 × 600 px | transparent auf Weiß | Startseite Kachel „Klasse BE“, Führerschein-Seite Kreis „Klasse BE“ |
| `automatik-schaltung.png` | Automatik-Wählhebel (P R N D) und Schaltkulisse (1 bis 5, R), dazwischen ein Pfeil | 2 : 1 | 1200 × 600 px | transparent, steht auf **dunklem Petrol `#0E3B3F`**, also helle Motive | Startseite Kachel „B197“, Führerschein-Seite B197-Band |
| `begleitet-17.png` | Fahrschülerin oder Fahrschüler am Steuer, daneben die Begleitperson, gern von oben oder schräg | 1,5 : 1 | 1040 × 680 px | transparent auf Weiß | Startseite Kachel „BF17“, Führerschein-Seite Abschnitt Begleitetes Fahren |
| `lkw.png` | Sattelzug in Seitenansicht, nach rechts | 2,7 : 1 | 1840 × 680 px | transparent auf Weiß | Startseite Kachel „BKF“, Kopf der Seite Berufskraftfahrer, Instagram-Karussell |
| `strassenschild.png` | deutsches Straßenschild „Schwarzwaldstraße“ mit Hausnummer 93 (Text muss exakt stimmen, sonst lieber ohne Text liefern; ich setze ihn dann) | 1,9 : 1 | 1120 × 600 px | transparent, steht auf dunklem Petrol | Kontakt-Band auf der Anmeldeseite |

## Was bleibt, wie es ist

- **Logo und Favicon** bleiben unverändert.
- **Wo die Illustrationen jetzt stehen:** Hero der Startseite (Szene), Kachelreihe der Klassen auf der Startseite, Kreis-Karten und B197-Band auf der Führerschein-Seite, Kopf der BKF-Seite, Instagram-Karussell.
- **Icons** (Pfeile, Telefon, PDF) stammen aus der Icon-Bibliothek Phosphor und sind keine Illustrationen.
