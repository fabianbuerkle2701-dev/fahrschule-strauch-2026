# Analyse

Stand: 02.10.2026. Untersucht wurden https://www.fahrschule-strauch.de (alle verlinkten Seiten, Bilder, PDFs, Quelltext) und https://shophoki.com (Startseite, Produktseite, Desktop 1440 px und Mobil 390 px, berechnete Stile per DOM).

Hinweis zum Werkzeug: „Claude in Chrome“ war in dieser Sitzung nicht verbunden. Mit Zustimmung wurde der eingebaute Browser der App verwendet (gleiche Möglichkeiten: Screenshots, DOM, Computed Styles, Viewport-Emulation). Cookie-Banner wurden nicht akzeptiert, sondern für die Messung nur ausgeblendet.

---

## A. Bestehende Website Fahrschule Strauch

### Seiten

| Datei | Inhalt |
|---|---|
| `index.html` | Slider (4 Stockfotos), Kacheln Kursangebote / BKF / Klassen / Finanzierung, Schnellkurs, Auffrischung, BF17-Teaser, Seitenleiste mit „Fahrlehrer gesucht“, B197-Plakat, Terminbox |
| `ueber_uns.html` | Langer Willkommenstext, 4 Fahrlehrer mit Foto, Jahr und Spruch |
| `information.html` | Klassen B und BE mit Rechtstext, Mindestalter, PDF „Info & Preise“, Formulare, Online-Anmeldung (Fahrschulmanager) |
| `begleitetes-fahren-ab-17.html` | BF17-Regeln, Liste der Unterlagen, 3 PDF-Formulare |
| `maxi.html` / `kursangebot.html` | (identischer Inhalt) Anmeldung mit MAXI, App „Fahren Lernen MAX“, 2 Videos, QR-Code, Online-Anmeldung |
| `berufskraftfahrer.html` | BKF-Weiterbildung, Schlüsselzahl 95, Module 1–5 |
| `impressum.html` | Impressum **und** Datenschutzerklärung auf einer Seite (eRecht24, Stand 2018) |
| `index-ru.html`, `information-ru.html`, `kursangebot-ru.html`, `impressum-ru.html` | Russische Teilübersetzung, lückenhaft (Teile auf Deutsch, „Далее“-Links ins Leere) |
| `datenschutz.html` | existiert nicht (404); Datenschutz steckt im Impressum |

### Navigation
Start · Über Uns · Information · BF17 · Maxi · BKF. Die Labels sind intern gedacht („Maxi“, „BKF“, „Information“ sagen Erstbesuchern nichts). Auf `kursangebot.html` heißt der Menüpunkt „Kurse“, sonst „Maxi“: inkonsistent. Sprachwahl DE/RU in der Kopfleiste.

### Führerscheinklassen und Leistungen (verifiziert)
- **Klasse B**: Pkw und leichte Lkw bis 3.500 kg, max. 8 Personen außer Fahrer. Anhänger bis 750 kg oder Kombination bis 3.500 kg. Mindestalter 18, mit BF17 17. Kein Vorbesitz. Beinhaltet L und AM.
- **Klasse BE**: Kombination aus Klasse-B-Fahrzeug und größerem Anhänger. Mindestalter 18, mit BF17 17. Vorbesitz B.
- **B197** (Plakat „Schaltung oder Automatik? Beides!“ und PDF Formular-B): Prüfung im Automatikfahrzeug, danach ohne Beschränkung Schaltwagen fahren. Mindestens 10 Übungsstunden auf dem Schaltfahrzeug und eine Testfahrt von mindestens 15 Minuten vor der praktischen Prüfung.
- **Begleitetes Fahren ab 17**: Antrag ab 16½, Einwilligung der Erziehungsberechtigten, Unterlagen: Ausweis/Pass, biometrisches Lichtbild, Sehtest (max. 2 Jahre alt), Erste-Hilfe-Nachweis, je Begleitperson Formular „Anlage zum Antrag BF17“ mit Kopie Ausweis und Führerschein.
- **Schnellkurse** (Intensivkurse). Letzter beworbener Termin Theorieschnellkurs Klasse B: 24.08.–31.08.2026, Mo–Fr 17:15–20:30, Sa 09:00–12:15.
- **Führerschein-Auffrischung** für B und BE. Inhalte: Verkehrsregeln über Theorieunterricht, Schalt- oder Automatikfahrzeug, Angstbewältigung, schwierige Verkehrssituationen, Einparken, Fahren bei Dunkelheit, Eis und Schnee (saisonbedingt, nur Pkw). Voraussetzung: Besitz der Klasse.
- **BKF-Weiterbildung** nach BKrFQG, Schlüsselzahl 95, amtlich anerkannte Ausbildungsstätte. Module 1 Eco-Training & Assistenzsysteme, 2 Sozialvorschriften & Fahrtenschreiber, 3 Gefahrenwahrnehmung, 4 Schadensprävention, 5 Sicherheit für Ladung und Fahrgast. Letzter Termin 20.04.2024 (auskommentiert).
- **Anmeldung**: online über Fahrschulmanager (POST-Formular, `api.fahrschulmanager.de/v1/onlineanmeldung/...`), Anmeldeformular als PDF, App „Fahren Lernen MAX“.
- **Finanzierung**: STARTHILFE (Verlag Heinrich Vogel und Credit Europe Bank), Link `starthilfe.fahren-lernen.de`.
- **Russischsprachige Beratung**: „Говорим по Русски“ im Footer.
- **Stellenanzeige**: „Fahrlehrer gesucht“ (Bild in der Seitenleiste).

### Team (verifiziert, Über-uns-Seite)
| Name | Angabe | Spruch |
|---|---|---|
| Viktor Strauch | Fahrlehrer seit 2007 | „Fährst du rückwärts gegen Baum, verkleinert sich dein Kofferraum!“ |
| Peter Harter | Fahrlehrer aller Klassen seit 1984 | „Der Weg ist das Ziel – viel Spaß auf Deinen neuen Wegen“ |
| Gerold Remmele | Fahrlehrer aller Klassen seit 1988, „Das Hobby zum Beruf gemacht.“ | „Ein Stop-Schild ist keine Empfehlung“ |
| Nadine Dürr | Fahrlehrerin seit 2000 | „Und immer noch Spaß daran, Jugendliche sicher auf die Straße zu bringen…“ |

### Standort, Kontakt, Zeiten
- Adresse: Schwarzwaldstraße 93, 77933 Lahr (Impressum: „Schwarzwaldstr. 93, 77933 Lahr/Schwarzwald“). Einziger Standort, im Footer „Filiale“ genannt.
- E-Mail: service@fahrschule-strauch.de (im Preis-PDF: info@fahrschule-strauch.de)
- Unterrichtszeiten: Montag 19:00–20:30 Uhr, Mittwoch nach Vereinbarung
- Bürozeiten: nicht angegeben
- Instagram `fahrschulestrauch`, Facebook-Profil (ID 100063727025765)

**Widerspruch Telefonnummer (offen, muss die Fahrschule klären):**
- Kopfleiste und Footer jeder Seite: **+49 155 60 41 04 13** (mit „Говорим по Русски“)
- Impressum, Datenschutz, Preis-PDFs, BKF-Plakat und die Beschriftung am Schaufenster (Foto): **0151 / 42522180**

Entscheidung für den Neubau: Die Nummer aus Kopf und Footer bleibt die zentrale Kontaktnummer (sie ist auf jeder Seite als Kontaktweg ausgewiesen). Das Impressum behält unverändert seine Nummer, weil rechtliche Angaben nicht eigenmächtig geändert werden.

### Bilder
| Bild | Größe | Herkunft | Verwendbar |
|---|---|---|---|
| `Logo_Viktor_Strauch.png` | 350×112, transparent | eigen | ja (nur als PNG vorhanden, kein Vektor) |
| `Fahrschule-1.jpg` | 640×480 | eigen: Team mit 4 Fahrschulautos vor der Fahrschule | ja, wichtigstes Bild |
| 4 Teamfotos | je 640×480 | eigen: Fahrlehrer neben ihrem Fahrschulauto | ja |
| `b197.jpg` | 830×1179 | Plakat Verlag Heinrich Vogel | nein (fremde Kampagne, Text im Bild) |
| `Fahrlehrer-gesucht.jpg`, `BKF-04-2024.jpg` | Plakate | eigen, Text im Bild | nein (Inhalt wird als Text übernommen) |
| Slider 1–4 | 1000×478 | Fotolia-Stock (im Impressum belegt) | nein (keine Stockbilder) |
| `begleitetes-fahren-ab-17.jpg`, `mpu.jpg`, `auffrischungskurs.jpg`, `Punktesystem*.jpg` | Mini-Thumbnails | Stock bzw. Grafik | nein |
| `anmeldung-qr.jpg` | 200×200 | QR zur Online-Anmeldung | nein (Link reicht, QR auf derselben Seite ist sinnlos) |

Für Foto und Teamfotos liegen im früheren Projekt (`fahrschule-strauch-website/images`) hochskalierte Fassungen vor (2400×1800 bzw. 1200×900). Sie sind sichtbar weicher als echte Hochauflösung, reichen aber für Darstellungsbreiten bis ca. 800 CSS-px bei 2× Pixeldichte. **Konsequenz für das Design: Kein Foto darf vollflächig über 1440 px laufen.** Der Hero wird nicht von einem Foto getragen, sondern von Typografie und einer eigenen Grafik; Fotos sitzen in gerahmten Fenstern.

### PDFs (werden verlinkt, nicht abgeschrieben)
`Formular-B.pdf`, `Formular-BE.pdf` (Info & Preise, Pflichtaushang), `Anmeldung.pdf`, `Fuehrerscheinantrag.pdf`, drei BF17-Formulare. Preise werden nicht auf die Website übernommen, weil Stand und Gültigkeit nicht prüfbar sind; die PDFs bleiben die Quelle.

### Probleme
**Veraltet**
- Theorieschnellkurs 24.–31.08.2026 wird am 02.10.2026 noch als „Aktueller Termin“ und in einer Slide-Down-Leiste beworben.
- BKF-Termin 2024 (auskommentiert), Copyright-Jahr aktualisiert, Inhalt nicht.
- Datenschutzerklärung von 2018: nennt YouTube-Plugins und TMG; Kontaktformular erwähnt, das es nicht gibt. **Muss von der Fahrschule rechtlich aktualisiert werden** (nicht Teil dieses Redesigns, Text wird unverändert übernommen).
- Stockfotos mit Fotolia-Nachweis, Fotolia existiert nicht mehr.

**UX**
- Kein `<h1>` auf der Startseite. `maximum-scale=1` sperrt das Zoomen (Barrierefreiheitsfehler).
- Zentrale Fakten (welche Klassen, wo, wie anmelden) sind über Kacheln, Seitenleiste, Slider und Footer verstreut. Die Startseite zeigt „Weiterlesen“-Links statt Antworten.
- Doppelte Inhalte: `maxi.html` = `kursangebot.html`; Schnellkurs/Auffrischung stehen auf der Startseite und im Slider; die Terminbox steht dreimal.
- Der Klassentext ist Gesetzessprache aus der FeV, ohne Übersetzung in Alltagsdeutsch.
- Der Über-uns-Text ist eine Textwand aus Allgemeinplätzen („modernste Lehrmethoden“), die echten Stärken (Team mit Fahrlehrern seit 1984, eigener Fuhrpark, russischsprachige Beratung, B197, BKF-Ausbildungsstätte) gehen darin unter.
- Online-Anmeldung, der wichtigste Weg, ist ein kleiner grauer Button „Online“ unter „NEU: Der Fahrschulmanager“.
- Telefonnummer und E-Mail sind nur 12–13 px klein in der Kopfleiste.

**Mobil**
- Sticky-Kopfleiste mit Kontakt, Sprachwahl und Avatar nimmt ca. 100 px ein, danach folgen Logo (≈120 px) und ein quadratischer Menü-Button: Das erste Bildschirmdrittel enthält keinen Inhalt.
- Slider-Fotos werden auf Hochformat beschnitten, Text der Slides fehlt.
- Boxed-Layout aus einem Template von ca. 2013 (jQuery, Flexslider, Isotope, Tweets, Flickr).

### Chancen
1. **Echte Menschen und echte Autos**: Das Fuhrparkfoto und die Teamfotos sind authentischer als jedes Stockbild. Die Sprüche der Fahrlehrer geben der Marke Humor.
2. **Erfahrung belegen statt behaupten**: „seit 1984, 1988, 2000, 2007“ ist ein überprüfbarer Beleg.
3. **Das Logo erzählt eine Straße**: Das S im Logo ist eine Fahrbahn mit zwei Randlinien. Daraus entsteht das gesamte Bildsystem.
4. **Die Fahrzeugbeklebung**: Die Autos tragen ein Band aus schräg gestellten petrolfarbenen Parallelogrammen an Front und Flanke. Ein zweites, echtes Markenelement.
5. **B197 und BF17** sind die Fragen, die Jugendliche und Eltern wirklich haben („Automatik oder Schaltung?“, „Ab wann?“). Sie gehören auf die Startseite.
6. **Russisch** als echter Service, nicht nur als Fußnote.
7. Lokales SEO fehlt fast vollständig (kein H1, kein strukturiertes Datum, Title nur „Fahrschule Viktor Strauch in Lahr“).

### Content-Inventur

| Inhalt | Quelle | Neue Verwendung |
|---|---|---|
| Name, Logo | alle Seiten | Header, Footer, Favicon-Ableitung |
| „Klassen B und BE“ | index, information | Hero-Untertitel, Klassen-Sektion, Klassen-Seite |
| Klassen-Rechtstext B/BE | information | Klassen-Seite, in Alltagssprache gekürzt, Original-Eckdaten (Gewicht, Alter, Vorbesitz) erhalten |
| B197-Regel | b197.jpg, Formular-B.pdf | Startseite (Klassen), FAQ, Klassen-Seite |
| BF17 Regeln + Unterlagen + 3 Formulare | begleitetes-fahren-ab-17 | Startseite (Klassen), Ablauf, FAQ, Klassen-Seite (#bf17) |
| Schnellkurs-Text | index | Angebote-Liste, Klassen-Seite |
| Auffrischung + Inhalte | index | Angebote-Liste, Klassen-Seite (#auffrischung) |
| BKF Module 1–5 | berufskraftfahrer | eigene Seite `/berufskraftfahrer/`, Teaser in Angebote |
| Willkommenstext | ueber_uns | gekürzt auf drei Kernaussagen (Fehler dürfen passieren, Fragen sind erwünscht, Ziel: sicher und selbstbewusst fahren) |
| Team, Jahre, Sprüche, Fotos | ueber_uns | Startseite „Fahrschule erleben“, Über-uns-Seite |
| Fuhrparkfoto | ueber_uns (Seitenleiste) | Hero-Fenster, Über-uns-Seite |
| Online-Anmeldung Fahrschulmanager | information, maxi | Haupt-CTA „Jetzt anmelden“ auf der Anmeldeseite |
| Fahren Lernen MAX | maxi | Ablauf (Theorie), Anmeldeseite, gekürzt |
| STARTHILFE Finanzierung | index | Angebote-Liste, FAQ, Anmeldeseite |
| Formulare (PDF) | information, bf17 | Anmeldeseite „Unterlagen“ |
| Info & Preise B/BE (PDF) | information | Klassen-Seite, FAQ „Was kostet …“ |
| Adresse, Telefon, E-Mail, Unterrichtszeiten | Footer | Kontakt-Sektion, Footer, Schema.org |
| „Говорим по Русски“ | Footer | Hero-Nähe als Service-Hinweis, eigene kompakte Seite `/ru/` |
| Fahrlehrer gesucht | index (Seitenleiste) | Über-uns-Seite, Footer-Zeile |
| Impressum, Datenschutz | impressum | `/impressum/`, `/datenschutz/` (Text unverändert, getrennt) |
| Theorieschnellkurs-Termin 08/2026 | index | **entfällt** (abgelaufen), Hinweis „Termine auf Anfrage“ |
| Slider, Stockfotos, MPU-, Punktesystem-Teaser (nur RU) | index, index-ru | **entfällt** |
| QR-Code Anmeldung | maxi | **entfällt** |

---

## B. HOKI-Analyse (shophoki.com)

### Layout
- Container `--container-max-width: 1300px`, schmal `1050px`. Innenabstand Desktop 48–64 px, mobil 20–22 px (`--container-gutter: 1.25rem`).
- Abschnitte sind **keine gleich hohen Bänder**: Hero 780 px Vollbild, dann ein Karussell, dann ein Bild-Block von 1136×760 mit 34 px Radius, der als eingesetzte Fläche im Weißraum schwebt. Section-Innenabstände schwanken bewusst zwischen 30 und 96 px.
- Inhalte liegen meist linksbündig an einer Kante, nicht zentriert. Zentriert sind nur Logo, Einzel-CTA unter Karussells.
- Karussells laufen über den rechten Rand hinaus (Anschnitt der nächsten Karte zeigt „hier geht es weiter“), darunter eine dünne Fortschrittslinie mit Pfeil statt Punkten.
- Spacing-Skala als Token-Leiter in 0,25-rem-Schritten bis 24 rem; in der Praxis genutzt: 8 · 16 · 20 · 32 · 48 · 64 · 96.

### Typografie
- Body: Geist 17 px / 27,2 px (1,6), `letter-spacing: -0.02em` auch im Fließtext.
- Display: Schibsted Grotesk 600, 64–82 px, `line-height` 1,0–1,05, Tracking −0,02 em. Produktseite H1 78 px, Zwischenüberschriften 52–72 px. Kleine Kartentitel 19–31 px, Gewicht 500–600.
- Verhältnis Headline zu Body ca. 4,5:1 auf Desktop, ca. 2:1 mobil (H2 mobil 34 px / 34,7 px).
- Lead-Absätze 19 px / 29,5 px in gedämpftem Grün-Grau (#6B7563), Zeilenlänge ≈ 58–63 Zeichen.
- Labels: Space Mono 12 px, Versalien, +0,2 em. Pro Abschnitt höchstens eins.
- **Zweifarbige Headline**: das letzte Wort oder die zweite Zeile in Akzentfarbe („Symptome von Dauer-Stress gezielt *ausgleichen.*“). Das ist das stärkste wiederkehrende Typo-Merkmal.
- CTA: 15 px, 600, Pillenform 52–56 px hoch, 14×28 px Polster.

### Bildsprache
- Fotos sind groß, ruhig, nah am Menschen, mit viel Himmel/Fläche. Nie kleine Thumbnails.
- Drei Radien: 20–22 px (Karten), 34 px (große Bildflächen), 999 px (Buttons, Chips, Header). Konsequent.
- Seitenverhältnisse wechseln: 1,85 (Hero), 0,8 (Hochkant-Karten), 1,49 (Bildblock), 1,33 (Testimonials).
- Text liegt direkt auf dem Foto (unten links, mit dunklem Verlauf), Statistik auf Bild.

### Animation
- Header: beim Scrollen wird die volle Leiste zu einer schwebenden Pille (780 px breit, 44 px hoch, `rgba(255,255,255,.85)`, `backdrop-filter: blur(18px)`, Schatten `0 8px 24px rgba(0,0,0,.08)`), Hintergrund-Transition 0,25 s.
- Bildkarten: Hover-Zoom `transform 0.5s cubic-bezier(0.4,0,0.2,1)`, Testimonial-Bilder 0,7 s ease-in-out.
- Buttons: 0,15–0,18 s `cubic-bezier(0.4,0,0.2,1)`.
- Produktseite: Headline mit Schreibmaschinen-Effekt im Akzentwort („weniger Müdigk…“).
- Kaum Scroll-Reveal-Bibliotheken; Bewegung entsteht durch Karussells, Sticky-Header und Hover. Dauern 120–700 ms, kein Bounce.

### Gesamtwirkung: Warum wirkt HOKI hochwertig und modern?
1. **Eine Stimme, zwei Gewichte.** Eine Groteske für alles, Gewicht 500–600 statt Bold. Wertigkeit entsteht durch Größe und enges Tracking, nicht durch Fettdruck.
2. **Farbe als Satzzeichen.** Der Akzent erscheint fast nur als eingefärbtes Wort in der Headline und auf dem Haupt-Button. Weil er selten ist, wirkt er.
3. **Bilder als Flächen, nicht als Beiwerk.** Ein Foto belegt einen ganzen Bildschirm oder eine 1100-px-Fläche. Dazwischen bleibt echter Weißraum, also wird jeder Block zum eigenen Moment.
4. **Strenges Formsystem.** Nur drei Radien, ein Schatten, eine Button-Form. Deshalb wirkt auch ein kleiner Chip „aus einem Guss“.
5. **Rhythmuswechsel.** Vollbild, Karussell, schwebende Bildfläche, Karten, Vollbild-Farbe: Kein Layout wiederholt sich direkt.
6. **Bewegung nur wo sie etwas erklärt.** Der Header schrumpft, damit Inhalt Platz bekommt; Karussells zeigen durch Anschnitt, dass es weitergeht. Keine Effekte zum Selbstzweck.
7. **Ruhige Mikrotypografie.** Negatives Tracking auch im Fließtext, gedämpfte Sekundärfarbe statt Grau, Zeilenlängen um 60 Zeichen.

### Was übertragen wird (und was nicht)
Übertragen: Prinzip zweifarbige Headline, schwebende Pillen-Navigation, Formsystem mit drei Radien, große gerahmte Bildflächen, Karussell mit Anschnitt und Fortschrittslinie, Rhythmuswechsel, gedämpfte Sekundärtexte, kurze präzise Transitions.
Nicht übertragen: Schriften (Geist, Schibsted Grotesk, Space Mono), Grüntöne, Inhalte, Bewertungs- und Zahlen-Social-Proof (die Fahrschule hat keine verifizierten Zahlen), Vollbild-Fotohero (die vorhandenen Fotos sind dafür zu klein).
