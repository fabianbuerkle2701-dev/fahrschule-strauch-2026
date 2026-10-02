# Illustrationen zum Austausch

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
| `auto-seite.png` | Fahrschulauto (kompakter SUV) in Seitenansicht, nach rechts | 2,2 : 1 | 1320 × 600 px | transparent, steht auf hellem Mint bzw. Weiß | Startseite Kachel „Klasse B“, Führerschein-Seite Abschnitt Klasse B, 404-Seite |
| `auto-anhaenger.png` | dasselbe Auto mit Kastenanhänger, nach rechts | 3,5 : 1 | 2080 × 600 px | transparent auf Weiß | Startseite Kachel „Klasse BE“, Kopf der Führerschein-Seite |
| `automatik-schaltung.png` | Automatik-Wählhebel (P R N D) und Schaltkulisse (1 bis 5, R), dazwischen ein Pfeil | 2 : 1 | 1200 × 600 px | transparent, steht auf **dunklem Petrol `#0E3B3F`**, also helle Motive | Startseite Kachel „B197“ |
| `begleitet-17.png` | Fahrschülerin oder Fahrschüler am Steuer, daneben die Begleitperson, gern von oben oder schräg | 1,5 : 1 | 1040 × 680 px | transparent auf Weiß | Startseite Kachel „Begleitetes Fahren ab 17“ |
| `lkw.png` | Sattelzug in Seitenansicht, nach rechts | 2,7 : 1 | 1840 × 680 px | transparent auf Weiß | Kopf der Seite Berufskraftfahrer |
| `strassenschild.png` | deutsches Straßenschild „Schwarzwaldstraße“ mit Hausnummer 93 (Text muss exakt stimmen, sonst lieber ohne Text liefern; ich setze ihn dann) | 1,9 : 1 | 1120 × 600 px | transparent auf Hellgrau | Abschnitt Kontakt (Startseite und Anmeldeseite) |
| `auto-oben.png` | Fahrschulauto **genau von oben**, Front zeigt nach **rechts**, Dachschild sichtbar | 1,8 : 1 | 400 × 220 px | transparent | Fährt im Abschnitt Ablauf die Straße entlang (wird beim Scrollen gedreht) |

## Was bleibt, wie es ist

- **Die Straßen** im Ablauf, im Abschluss und im Footer sind keine Bilder, sondern Linien, an denen das Auto entlangfährt. Sie müssen gezeichnet (SVG) bleiben, sonst funktioniert die Fahrt nicht.
- **Logo, Favicon und das Straßen-S im Footer** bleiben unverändert.
- **Icons** (Pfeile, Telefon, PDF) stammen aus der Icon-Bibliothek Phosphor und sind keine Illustrationen.
