# Design

Leitidee: **Das S im Logo ist eine Straße.** Zwei Randlinien, eine Kurve. Aus dieser Fahrbahn entsteht das Bildsystem der Website: Die Startseite ist eine Strecke, auf der ein Fahrschulauto beim Scrollen von der Anmeldung bis zum Führerschein fährt. Das zweite echte Markenelement kommt von den Autos selbst: das Schrägstreifen-Band der Fahrzeugbeklebung (petrolfarbene Parallelogramme an Front und Flanke).

Haltung: Editorial-Layout einer Consumer-Marke, ruhig und präzise wie HOKI, aber mit eigener Welt (Straße, Fahrbahnmarkierung, Streifen-Band, DIN-artige Straßenschrift statt Wellness-Groteske).

---

## Brand

### Farben (aus dem Logo extrahiert)
Pixelauswertung von `Logo_Viktor_Strauch.png`: Petrol **#0199A6** (2.100 Pixel, dominant), Grau **#ACADAF** (Schriftzug „Viktor Strauch“). Petrol erreicht auf Weiß nur 3,44:1, deshalb gibt es eine dunklere Text-Stufe.

```css
:root {
  --color-brand:        #0199A6; /* Logo-Petrol: Grafik, Flächen, große Schrift ≥ 24 px */
  --color-brand-ink:    #00717B; /* Petrol für Text, Links, Buttons (5,76:1 auf Weiß) */
  --color-brand-dark:   #0B5258; /* Hover, Text auf Mint (7,8:1) */
  --color-brand-night:  #0E3B3F; /* Linien der Illustrationen, dunkle Flächen */
  --color-brand-light:  #E3F3F4; /* Mint: Kachelflächen, Markierungen */
  --color-brand-mist:   #F1F8F8; /* Abschnittsgrund */

  --color-neutral-950:  #1C2224; /* Text, Footer */
  --color-neutral-800:  #3E4547; /* Asphalt */
  --color-neutral-600:  #565D60; /* Sekundärtext (6,7:1) */
  --color-neutral-400:  #8A8F92; /* nur Deko, nie Text */
  --color-neutral-300:  #ACADAF; /* Logo-Grau: Linien, Rahmen */
  --color-neutral-200:  #D9DCDD;
  --color-neutral-100:  #ECEEEF;
  --color-neutral-50:   #F6F7F7;

  --color-background:   #FFFFFF;
  --color-surface:      #F6F7F7;
}
```
Strategie: zurückhaltend mit einem Farbblock. Weiß trägt die Seite, Petrol erscheint als eingefärbtes Wort in Überschriften, auf dem Haupt-Button und in den Illustrationen. Einmal pro Seite darf Petrol eine ganze Fläche besitzen (Abschluss-CTA). Keine weiteren Farben, keine Verläufe.

### Logo
Original-PNG, unverändert, Höhe 44 px (Header) bzw. 56 px (Footer, auf Dunkel). Kein Nachzeichnen des Logos. Das Straßen-S der Illustrationen ist eine eigene Zeichnung, angelehnt an die Logo-Kurve, nicht das Logo selbst.

### Motive
- **Fahrbahn**: zwei parallele Randlinien (Petrol), dazwischen Asphalt (#3E4547) und weiße Mittelstreifen (gestrichelt 18/14). Einsatz: Hero, Ablauf, Kontakt, Abschluss. Nicht in jeder Sektion.
- **Streifen-Band**: schräg gestellte Petrol-Parallelogramme auf Weiß, wie an Front und Flanke der Fahrschulautos. Einsatz: Seitenlinie der Auto-Illustrationen, Trennlinie über dem Footer, Fokus auf kleine Details.
- **Fahrschulauto von oben**: weiß, Dachschild Petrol. Fährt im Ablauf.

---

## Typografie

| Rolle | Schrift | Grund |
|---|---|---|
| Display, Überschriften | **Barlow Semi Condensed** 600 (selbst gehostet) | Abgeleitet von Straßen- und Kennzeichenschriften, erinnert an DIN 1451 der deutschen Verkehrsschilder. Leicht schmal, damit lange deutsche Wörter („Führerscheinklassen“) in große Größen passen. |
| Text, UI | **Onest** variabel 400–650 (selbst gehostet) | Sehr gut lesbar, freundlich, mit Kyrillisch für die russische Seite. |

Keine dritte Schrift, keine Monospace-Labels.

| Stufe | Größe (clamp, 360→1440 px) | Zeilenhöhe | Tracking | Gewicht |
|---|---|---|---|---|
| Display | `clamp(2.75rem, 1.4rem + 5.9vw, 6rem)` 44→96 | 0,95 | −0,02em | 600 |
| H1 (Unterseiten) | `clamp(2.5rem, 1.6rem + 4vw, 4.75rem)` 40→76 | 1,0 | −0,02em | 600 |
| H2 | `clamp(2.125rem, 1.45rem + 3vw, 4rem)` 34→64 | 1,02 | −0,015em | 600 |
| H3 | `clamp(1.375rem, 1.15rem + 1vw, 2rem)` 22→32 | 1,12 | −0,01em | 600 |
| Lead | `clamp(1.125rem, 1.05rem + .35vw, 1.375rem)` 18→22 | 1,5 | −0,01em | 400 |
| Body | `clamp(1rem, .97rem + .15vw, 1.0625rem)` 16→17 | 1,6 | −0,005em | 400 |
| Small | 0,9375rem / 15 | 1,5 | 0 | 400 |
| Label | 0,875rem / 14 | 1,3 | +0,02em | 600 (Onest, nicht versal) |
| Button | 1rem / 16 | 1 | 0 | 600 |

Regeln: Fließtext max. 64ch. Überschriften `text-wrap: balance`, Fließtext `text-wrap: pretty`, `hyphens: auto` mit `lang="de"`. Zweifarbige Überschriften: Der zweite Satzteil steht in `--color-brand-ink` bzw. `--color-brand` ab 32 px. Keine Versal-Kicker über Überschriften.

---

## Spacing

Skala (rem): 0,25 · 0,5 · 0,75 · 1 · 1,5 · 2 · 3 · 4 · 6 · 8 · 10 (4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 160 px).

- Container: `max-width: 1320px`, Rand `clamp(1rem, .5rem + 2.5vw, 3rem)` (16→48 px). Schmaler Container 760 px für Lesetext.
- Abschnittsabstand: `--section: clamp(5rem, 3rem + 8vw, 10rem)` (80→160 px). Abschnitte variieren bewusst: Ablauf ist überhoch (Scroll-Strecke), FAQ kompakt, Abschluss vollflächig.
- Über einer Überschrift mehr Raum als darunter (H2 → Inhalt 1,5–2 rem).

---

## UI

- **Buttons** (genau drei Typen):
  - Primär „Jetzt anmelden“: Pille, Höhe 52 px (mobil 56), Polster 0 28 px, `--color-brand-ink` mit Weiß, Hover `--color-brand-dark` + Pfeil 3 px nach rechts, aktiv `scale(.98)`.
  - Sekundär: Pille, transparent, 1,5 px Rand `--color-neutral-300`, Text `--color-neutral-950`; Hover Rand Petrol.
  - Textlink: Text `--color-brand-ink`, Unterstreichung 1,5 px, Abstand 0,2em; Hover wächst die Linie von links.
- **Links im Fließtext**: unterstrichen, Petrol-Ink.
- **Karten**: nur wo echte Gruppierung (Klassen-Kacheln, Team). Keine Karten-in-Karten. Kein Schatten auf Karten, Hierarchie über Fläche (Mint, Weiß mit Linie, Night).
- **Formfelder**: nicht benötigt (Anmeldung extern). Falls doch: Label über Feld, 52 px hoch, Radius 12 px, Rand neutral-300, Fokus 3 px Petrol-Ring.
- **Radien** (fest): 12 px kleine Elemente, 20 px Kacheln und Karten, `clamp(20px, 1rem + 1.4vw, 36px)` große Bildflächen, 999 px Buttons, Navigation, Chips.
- **Borders**: 1 px `--color-neutral-200` für Trennungen, 1,5 px für sekundäre Buttons.
- **Schatten** (genau einer): `0 18px 40px -18px rgb(14 59 63 / .28)` für die schwebende Navigation und das Auto.
- **Fokus**: 3 px Ring `--color-brand` mit 3 px Abstand, auf dunklem Grund Weiß.
- **Auswahl, Caret, Scrollbar** in Petrol.

## Layout

- Mobile first. Breakpoints (min-width): 480 · 768 · 1024 · 1280 · 1600.
- 12-Spalten-Grid ab 1024 px, Spaltenabstand `clamp(1rem, .5rem + 1.5vw, 2rem)`. Darunter 1 Spalte, 768–1023 teils 2 Spalten.
- Asymmetrie: Text startet in Spalte 1, Bilder brechen rechts aus dem Container aus (bis zum Viewport-Rand) oder sitzen versetzt.
- Hero nutzt `min-height: 100svh`, nie `100vh`.

## Animation

| Token | Wert | Verwendung |
|---|---|---|
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` | Reveals, Auto |
| `--ease-ui` | `cubic-bezier(.4, 0, .2, 1)` | Hover, Menü, Accordion |
| `--dur-ui` | 180 ms | Buttons, Links |
| `--dur-med` | 320 ms | Accordion, Menü |
| `--dur-reveal` | 800 ms | Scroll-Reveal |

- **Reveal**: Opacity 0→1, Y 24→0 px, ausgelöst per IntersectionObserver (Schwelle 15 %), einmalig. Inhalte sind ohne JS sichtbar (Klasse `js` am `<html>` schaltet Reveal erst ein).
- **Stagger**: 70 ms je Element, max. 6 Elemente (Klassen-Kacheln, Team, Angebote).
- **Parallax**: nur Fuhrpark-Foto im Intro, max. 6 % Versatz, nur ab 1024 px.
- **Signatur: Fahrt durch die Ausbildung.** Im Ablauf ist die Straße sticky; der Scrollfortschritt durch sechs Stationen bewegt das Auto (`getPointAtLength`, Rotation per Tangente) und färbt die Strecke hinter ihm Petrol. Jede Station wird aktiv, wenn das Auto sie erreicht.
- **Hero**: Fahrbahn zeichnet sich einmal beim Laden (stroke-dashoffset, 1,4 s).
- **Navigation**: wird nach 24 px Scroll zur schwebenden Pille (Hintergrund Weiß 88 %, Blur 16 px, Schatten).
- **prefers-reduced-motion**: kein Reveal (Inhalte sofort sichtbar), kein Parallax, keine Fahrbahn-Zeichnung, Ablauf ohne Sticky, Auto steht am Ziel, alle Stationen aktiv.

---

## Informationsarchitektur

| Seite | Pfad | Zweck |
|---|---|---|
| Startseite | `/` | Geführte Geschichte, beantwortet die sechs Kernfragen |
| Führerschein | `/fuehrerschein/` | Klassen B, BE, B197, BF17 im Detail, Schnellkurs, Auffrischung, Preis-PDFs |
| Berufskraftfahrer | `/berufskraftfahrer/` | BKF-Weiterbildung Module 1–5 (eigene Zielgruppe) |
| Über uns | `/ueber-uns/` | Team, Haltung, Fuhrpark, Stellenanzeige |
| Anmeldung & Kontakt | `/anmeldung/` | Online-Anmeldung, Unterlagen, Formulare, App MAX, Finanzierung, Kontakt, Anfahrt |
| По-русски | `/ru/` | Kompakte russische Seite mit den wichtigsten Fakten |
| Impressum | `/impressum/` | Text unverändert vom Original |
| Datenschutz | `/datenschutz/` | Text unverändert vom Original |

Hauptnavigation: Führerschein · Ablauf · Über uns · Kontakt · RU · [Jetzt anmelden]. Die alten Menüpunkte „Information“, „Maxi“, „BF17“, „BKF“ gehen in sprechenden Seiten auf.

## Startseite

1. **Hero** – „Führerschein in Lahr.“ in großer Straßenschrift, darunter ein Satz zu Klassen und Ort, „Jetzt anmelden“ und „Klassen ansehen“. Rechts schlängelt sich das Straßen-S aus dem Logo durch den Bildschirm, im Bogen sitzt das echte Fuhrparkfoto. Beantwortet sofort: wer, was, wo.
2. **Intro: Seit 1984 am Beifahrersitz** – Kurze Haltung (Fehler dürfen passieren, Fragen sind erwünscht) und die vier Jahreszahlen des Teams als Beleg. Vertrauen kommt vor dem Angebot, weil Eltern zuerst wissen wollen, wem sie ihr Kind anvertrauen.
3. **Führerscheinklassen** – Vier unterschiedlich große Kacheln: B, BE, B197 („Automatik oder Schaltung? Beides.“), BF17. Große Klassen-Typografie, eigene Fahrzeug-Illustrationen. Direkt nach dem Vertrauen, weil hier die Entscheidung fällt.
4. **Ablauf** – Die Straße wird sticky, das Auto fährt durch Anmelden, Unterlagen, Theorie, Fahrstunden, Prüfung, Führerschein. Signatur-Moment und Antwort auf „Wie läuft das ab?“.
5. **Team** – Die vier Fahrlehrer mit Foto am eigenen Auto, Jahreszahl und eigenem Spruch. Echte Menschen als Bildmoment nach dem abstrakten Ablauf.
6. **Mehr als die erste Fahrstunde** – Editoriale Liste: Schnellkurs, Auffrischung, BKF-Weiterbildung, Finanzierung, App MAX. Für die zweite Zielgruppe (Erwachsene, Profis), deshalb nach dem Kernangebot.
7. **Kontakt & Standort** – Telefonnummer groß, E-Mail, Adresse, Unterrichtszeiten, Routenlink, russischer Hinweis. Kein Formular.
8. **FAQ** – Sieben echte Fragen (Alter, Unterlagen, Automatik, Kosten, Russisch, Schnellkurs, Finanzierung) mit Antworten aus den Originalinhalten.
9. **Abschluss** – Petrol-Fläche: „Bereit für die erste Fahrstunde?“, Anmelden und Anrufen. Die Straße endet hier.
