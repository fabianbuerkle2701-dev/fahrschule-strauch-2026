---
name: Fahrschule Strauch
description: Das S im Logo ist eine Straße; die Website ist die Strecke von der Anmeldung zum Führerschein.
colors:
  brand: "#0199a6"
  brand-ink: "#00717b"
  brand-dark: "#0b5258"
  brand-night: "#0e3b3f"
  brand-light: "#e3f3f4"
  brand-mist: "#f1f8f8"
  brand-glow: "#a5e1e6"
  neutral-950: "#1c2224"
  neutral-800: "#3e4547"
  neutral-600: "#565d60"
  neutral-400: "#8a8f92"
  neutral-300: "#acadaf"
  neutral-200: "#d9dcdd"
  neutral-100: "#eceeef"
  neutral-50: "#f6f7f7"
  background: "#ffffff"
typography:
  display:
    fontFamily: "Barlow Semi Condensed, Barlow Fallback, Arial Narrow, sans-serif"
    fontSize: "clamp(3.25rem, 2rem + 5.2vw, 6rem)"
    fontWeight: 600
    lineHeight: 0.95
    letterSpacing: "-0.02em"
  h1:
    fontFamily: "Barlow Semi Condensed, Barlow Fallback, Arial Narrow, sans-serif"
    fontSize: "clamp(2.5rem, 1.6rem + 4vw, 4.75rem)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Barlow Semi Condensed, Barlow Fallback, Arial Narrow, sans-serif"
    fontSize: "clamp(2.125rem, 1.45rem + 3vw, 4rem)"
    fontWeight: 600
    lineHeight: 1.02
    letterSpacing: "-0.015em"
  h3:
    fontFamily: "Barlow Semi Condensed, Barlow Fallback, Arial Narrow, sans-serif"
    fontSize: "clamp(1.375rem, 1.15rem + 1vw, 2rem)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.01em"
  lead:
    fontFamily: "Onest, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.125rem, 1.05rem + 0.35vw, 1.375rem)"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Onest, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1rem, 0.97rem + 0.15vw, 1.0625rem)"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "-0.005em"
  small:
    fontFamily: "Onest, ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Onest, ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0.02em"
  button:
    fontFamily: "Onest, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0"
rounded:
  sm: "12px"
  md: "20px"
  lg: "clamp(20px, 1rem + 1.4vw, 36px)"
  pill: "999px"
spacing:
  "1": "0.25rem"
  "2": "0.5rem"
  "3": "0.75rem"
  "4": "1rem"
  "5": "1.5rem"
  "6": "2rem"
  "7": "3rem"
  "8": "4rem"
  "9": "6rem"
  "10": "8rem"
  "11": "10rem"
  section: "clamp(5rem, 3rem + 8vw, 10rem)"
  gutter: "clamp(1rem, 0.5rem + 2.5vw, 3rem)"
  grid-gap: "clamp(1rem, 0.5rem + 1.5vw, 2rem)"
  container: "1320px"
  container-narrow: "760px"
components:
  button-primary:
    backgroundColor: "{colors.brand-ink}"
    textColor: "{colors.background}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0 1.75rem"
    height: "52px"
  button-primary-hover:
    backgroundColor: "{colors.brand-dark}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.neutral-950}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0 1.75rem"
    height: "52px"
  button-secondary-hover:
    textColor: "{colors.brand-ink}"
  button-light:
    backgroundColor: "{colors.background}"
    textColor: "{colors.brand-dark}"
    rounded: "{rounded.pill}"
    height: "52px"
  button-light-hover:
    backgroundColor: "{colors.brand-light}"
    textColor: "{colors.brand-night}"
  button-roll:
    backgroundColor: "{colors.brand-ink}"
    textColor: "{colors.background}"
    rounded: "{rounded.pill}"
    padding: "0 6px 0 1.6rem"
    height: "52px"
  button-roll-arrow:
    backgroundColor: "{colors.background}"
    textColor: "{colors.brand-ink}"
    rounded: "{rounded.pill}"
    size: "40px"
  nav-link:
    textColor: "{colors.neutral-800}"
    rounded: "{rounded.pill}"
    padding: "0 0.85rem"
    height: "44px"
  nav-link-hover:
    backgroundColor: "{colors.neutral-100}"
    textColor: "{colors.neutral-950}"
  subnav-chip:
    textColor: "{colors.neutral-950}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: "0 1.1rem"
    height: "44px"
  subnav-chip-current:
    backgroundColor: "{colors.neutral-950}"
    textColor: "{colors.background}"
  class-tile-mint:
    backgroundColor: "{colors.brand-light}"
    textColor: "{colors.neutral-950}"
    rounded: "{rounded.lg}"
    padding: "clamp(1.5rem, 1rem + 2vw, 2.5rem)"
  class-tile-line:
    backgroundColor: "{colors.background}"
    textColor: "{colors.neutral-950}"
    rounded: "{rounded.lg}"
    padding: "clamp(1.5rem, 1rem + 2vw, 2.5rem)"
  class-tile-night:
    backgroundColor: "{colors.brand-night}"
    textColor: "{colors.background}"
    rounded: "{rounded.lg}"
    padding: "clamp(1.5rem, 1rem + 2vw, 2.5rem)"
  panel:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.lg}"
    padding: "clamp(1.5rem, 1rem + 2vw, 2.5rem)"
  panel-tint:
    backgroundColor: "{colors.brand-mist}"
    rounded: "{rounded.lg}"
    padding: "clamp(1.5rem, 1rem + 2vw, 2.5rem)"
  finale:
    backgroundColor: "{colors.brand-ink}"
    textColor: "{colors.background}"
---

# Design

Leitidee: **Das S im Logo ist eine Straße.** Zwei Randlinien, eine Kurve. Aus dieser Fahrbahn entsteht das Bildsystem der Website: Die Startseite ist eine Strecke, auf der ein Fahrschulauto beim Scrollen von der Anmeldung bis zum Führerschein fährt. Das zweite echte Markenelement kommt von den Autos selbst: das Schrägstreifen-Band der Fahrzeugbeklebung (petrolfarbene Parallelogramme an Front und Flanke).

Haltung: Editorial-Layout einer Consumer-Marke, ruhig und präzise wie HOKI, aber mit eigener Welt (Straße, Fahrbahnmarkierung, Streifen-Band, DIN-artige Straßenschrift statt Wellness-Groteske).

Die Token im Kopf dieser Datei (YAML) sind verbindlich und entsprechen `src/styles/tokens.css`. Der Text erklärt, wo und warum sie eingesetzt werden. Bewegung, Schatten und Breakpoints stehen zusätzlich maschinenlesbar in `.impeccable/design.json`.

---

## Brand

### Farben (aus dem Logo extrahiert)
Pixelauswertung von `Logo_Viktor_Strauch.png`: Logo-Petrol `brand` (#0199A6, dominant), Logo-Grau `neutral-300` (#ACADAF, Schriftzug „Viktor Strauch“). Petrol erreicht auf Weiß nur 3,44:1, deshalb gibt es eine dunklere Text-Stufe.

| Rolle | Token | Einsatz |
|---|---|---|
| Logo-Petrol | `brand` #0199A6 | Grafik, Straßen-Randlinien, Fahrspur hinter dem Auto, Klassen-Buchstaben, Fokus-Ring, Auswahl; als Schrift nur ab 24 px |
| Petrol-Ink | `brand-ink` #00717B | Eingefärbtes Wort in Überschriften, Links, Haupt-Button, Abschluss-Fläche (5,76:1 auf Weiß) |
| Petrol dunkel | `brand-dark` #0B5258 | Hover von Button und Links, Asphalt der Abschluss-Straße |
| Nacht-Petrol | `brand-night` #0E3B3F | Linien der Illustrationen, dunkle Flächen (B197-Kachel, Team-Bühne, Anmelde-Block) |
| Mint | `brand-light` #E3F3F4 | Klasse-B-Kachel, offener Akkordeon-Knopf, Hover heller Button |
| Nebel | `brand-mist` #F1F8F8 | Grund des Ablaufs, getönte Panels, Hover der Angebotszeilen |
| Petrol hell (Glow) | `brand-glow` #A5E1E6 | Hervorhebung auf dunklem Petrol: eingefärbtes Wort in Überschriften (Team, Abschluss, Footer-Claim, B197), Schaltpfeil der B197-Grafik, Hover des Team-Links |
| Text | `neutral-950` #1C2224 | Text, Footer-Grund, aktiver Unterseiten-Chip |
| Asphalt | `neutral-800` #3E4547 | Fahrbahn, Footer-Fahrstreifen, Navigationslinks |
| Sekundärtext | `neutral-600` #565D60 | Leads, Beschreibungen, noch nicht erreichte Etappen (6,7:1) |
| Deko-Grau | `neutral-400` #8A8F92 | nur Pfeile im Mobilmenü, nie Fließtext |
| Logo-Grau | `neutral-300` #ACADAF | Rahmen sekundärer Buttons, Stationen, Schildmast |
| Linie | `neutral-200` #D9DCDD | Trennlinien, Kartenrand (innen, 1 px) |
| Fläche | `neutral-100` / `neutral-50` | Hover-Grund, Bildplatzhalter / Abschnittsgrund Klassen und Kontakt |

**Die Ein-Fläche-Regel.** Weiß trägt die Seite. Petrol erscheint als eingefärbtes Wort, auf dem Haupt-Button und in den Illustrationen; als ganze Fläche besitzt es pro Seite nur den Abschluss (Petrol-Ink). Dunkle Flächen sind Nacht-Petrol, nicht Logo-Petrol. Keine weiteren Buntfarben.

**Die Verlaufs-Regel.** Keine dekorativen Farbverläufe. Verläufe gibt es nur funktional: als Abdunklung über Teamfotos (Lesbarkeit), als Ausblendkante unter der Sticky-Straße und als wachsende Unterstreichung der Textlinks.

### Logo
Original-Logo als Bild, unverändert, Höhe 40 px mobil und 44 px ab 1024 px (Header und Mobilmenü); in der schwebenden Navigation auf 85 % skaliert. Kein Nachzeichnen des Logos. Der Footer zeigt nicht das Logo-Bild, sondern eine Petrol-Kreismarke mit gezeichnetem Straßen-S und die übergroße Wortmarke „Fahrschule Strauch“ in Straßenschrift. Das Straßen-S ist eine eigene Zeichnung, angelehnt an die Logo-Kurve.

### Motive
- **Fahrbahn**: Petrol-Randlinien (Strich 84, darin Asphalt 70), weiße Mittellinie 3 px gestrichelt 16/14. Einsatz: Ablauf (mit Petrol-Spur 6 px hinter dem Auto), Abschluss (Asphalt Petrol-dunkel, Rand Weiß 12 %). Nicht in jeder Sektion.
- **Streifen-Band (Beklebung)**: schräge Petrol-Parallelogramme. Als SVG-Muster (`#livery`, 13 × 10) auf den gezeichneten Autos (Flanke, Dachkanten). Genau einmal als Kante: 12 px hohe Oberkante des Klassen-Abschnitts (SVG-Kachel 26 × 12).
- **Footer-Fahrstreifen**: 64 px Asphalt mit 5 px Petrol-Kanten oben und unten, weiße Mittellinie (34/28) läuft endlos nach links.
- **Fahrschulauto**: von oben (weiß, Dachschild Petrol, Beklebung an den Flanken) fährt im Ablauf; von der Seite (SUV) in den Klassen-Kacheln und Seitenköpfen.
- **Straßenschild**: weißes Schild mit dunklem Rand und Petrol-Hausnummernschild im Kontakt.

**Die Beklebungs-Regel.** Das Streifen-Band gehört an Fahrzeuge und erscheint als Kante genau einmal (Klassen-Oberkante). Nicht als Trennlinie wiederholen.

---

## Typografie

| Rolle | Schrift | Grund |
|---|---|---|
| Display, Überschriften | **Barlow Semi Condensed** 600 (selbst gehostet, Latin + Latin-Ext) | Abgeleitet von Straßen- und Kennzeichenschriften, erinnert an DIN 1451 der Verkehrsschilder. Leicht schmal, damit lange deutsche Wörter in große Größen passen. Metrisch angepasste Ersatzschrift („Barlow Fallback“, Arial Narrow 88 %) gegen Layoutsprünge. |
| Text, UI | **Onest** variabel (selbst gehostet, mit Kyrillisch) | Gut lesbar, freundlich, trägt die russische Seite. Genutzte Gewichte 400, 500, 520 (Navigation), 560, 600, 620 (fett), 650. |

Keine dritte Schrift, keine Monospace-Labels.

| Stufe | Größe (clamp, 360→1440 px) | Zeilenhöhe | Tracking | Gewicht |
|---|---|---|---|---|
| Display | 52 → 96 px | 0,95 | −0,02em | 600 |
| H1 (Unterseiten) | 40 → 76 px | 1,0 | −0,02em | 600 |
| H2 | 34 → 64 px | 1,02 | −0,015em | 600 |
| H3 | 22 → 32 px | 1,12 | −0,01em | 600 |
| Lead | 18 → 22 px | 1,5 | −0,01em | 400 (Intro: 500) |
| Body | 16 → 17 px | 1,6 | −0,005em | 400 |
| Small | 15 px | 1,5 | 0 | 400 |
| Label | 14 px | 1,3 | +0,02em | 600 (Onest, nicht versal) |
| Button | 16 px | 1 | 0 | 600 |

Sondergrößen in Straßenschrift: Klassen-Buchstabe bis 240 px (Zeilenhöhe 0,78, −0,04em), Footer-Wortmarke bis 184 px (0,8, −0,035em), Telefonnummer 32 → 60 px, Angebotstitel 26 → 40 px, Mobilmenü 32 → 44 px.

**Die Straßenschrift-Regel.** Alles, was man wie ein Schild liest (Überschriften, Klassen, Telefonnummer, Jahreszahlen, Namen, Wortmarke), steht in Barlow Semi Condensed 600; alles, was man liest wie einen Satz, in Onest.

Regeln: Fließtext max. 64ch, Lead max. 34em. Überschriften `text-wrap: balance` ohne automatische Trennung, Fließtext `text-wrap: pretty` mit `hyphens: auto` unter `lang="de"` (schmale Spalten wie Intro-Lead und Team-Zitat ohne Trennung). Zweifarbige Überschriften: der zweite Satzteil in Petrol-Ink, auf dunklem Petrol in `brand-glow`. Keine Versal-Kicker über Überschriften.

---

## Spacing

Skala im 4er-Raster (`spacing.1`–`spacing.11`): 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 160 px.

- **Container**: 1320 px Inhalt plus Rand `gutter` (16 → 48 px). Schmaler Container 760 px für Rechtstexte und Lesetext.
- **Abschnittsabstand** `section`: 80 → 160 px oben und unten. Abschnitte variieren bewusst: Ablauf ist überhoch (Scroll-Strecke, Etappen 40svh mobil, 62svh Desktop), Abschluss hat unten mehr Raum (144 → 208 px) für die auslaufende Straße.
- **Abschnittskopf**: max. 52rem breit, darunter 40 → 72 px bis zum Inhalt; Lead 20 px unter der H2.
- **Rasterabstand** `grid-gap`: 16 → 32 px; zweispaltige Desktop-Layouts nehmen das Doppelte oder Dreifache.
- Über einer Überschrift mehr Raum als darunter.

---

## UI

### Buttons
Genau drei Grundtypen, alle als Pille, 52 px hoch (unter 480 px 56 px), Onest 600 16 px.
- **Primär** „Jetzt anmelden“: Petrol-Ink mit Weiß; Hover Petrol dunkel, Pfeil 3 px nach rechts; aktiv `scale(.98)`.
- **Sekundär**: transparent, 1,5 px Rand Logo-Grau, Text dunkel; Hover Rand und Text Petrol-Ink.
- **Textlink**: Petrol-Ink, 600; Unterstreichung 1,5 px wächst beim Hover von links (320 ms), Pfeil 3 px nach rechts.
- **Auf Dunkel/Petrol**: hell (Weiß, Text Petrol dunkel; Hover Mint) und Geist-hell (transparent, Rand Weiß 55 %).
- **Roll-Variante** (nach MotionSites „Axion About“): Beschriftung rollt beim Hover oder Fokus eine Zeile nach oben, der Pfeil im 40-px-Kreis (mobil 44 px) dreht sich von −45° auf 0° (beides 500 ms, `cubic-bezier(.25,.1,.25,1)`). Kreis weiß auf Primär, dunkel auf Sekundär (Hover Petrol-Ink), Petrol-Ink auf Hell. Für Pfeil-CTAs im Inhalt („Jetzt anmelden“ im Hero, „Mehr über uns“). Der kompakte Header-Button (44 px) bleibt einfach.
- **Sprachumschalter DE | RU**: Pillen-Segment auf `neutral-100` mit 1-px-Innenlinie, zwei Felder je min. 44 × 38 px, Onest 650 / 14 px / +0,04em. Ein Petrol-Ink-Daumen markiert die aktive Sprache (weiße Schrift), die andere steht in `neutral-600`. Aktive Sprache mit `aria-current`, Gruppenname „Sprache / Язык“.

### Links, Navigation, Chips
- **Links im Fließtext**: Petrol-Ink, unterstrichen 1,5 px mit 0,22em Abstand; Hover Petrol dunkel.
- **Navigationslinks**: 44 px hohe Pillen, Asphalt-Text; Hover Grund `neutral-100`; aktuelle Seite Petrol-Ink mit 4-px-Punkt darunter.
- **Unterseiten-Sprungleiste**: sticky Chips (44 px, Weiß 90 % mit Blur, innere 1-px-Linie); Hover 1,5-px-Linie Petrol-Ink, aktueller Chip dunkel gefüllt.

### Karten und Flächen
Nur wo echte Gruppierung: Klassen-Kacheln, Module, Panels, Anmelde-Block, Downloads, Team. Keine Karten in Karten.

**Die Inset-Linien-Regel.** Karten werfen keinen Schatten. Hierarchie entsteht über Fläche: Mint, Weiß mit innerer 1-px-Linie (`box-shadow: inset`), Nebel oder Nacht-Petrol.

### Formfelder
Keine eigenen Felder: die Anmeldung läuft extern (Fahrschulmanager), auf der Seite ist sie nur ein Formular mit hellem Button auf Nacht-Petrol. Falls Felder nötig werden: Label über dem Feld, 52 px hoch, Radius `sm`, Rand Logo-Grau, Fokus 3-px-Petrol-Ring.

### Akkordeon (FAQ)
Fragen in Onest 600 (17 → 20 px), mindestens 72 px hoch, Linien oben und unten. Plus-Zeichen in einem 40-px-Kreis (`neutral-100`), dreht beim Öffnen 45° und wird Mint. Höhe animiert über `::details-content` (320 ms).

### Radien, Borders, Schatten
- **Radien**: `sm` 12 px kleine Elemente und Hover-Flächen, `md` 20 px Module, kleines Intro-Foto, Hinweise; `lg` 20 → 36 px Kacheln, Panels, Bildrahmen, Team-Bühne; `pill` Buttons, Navigation, Chips. Avatare, Pfeil-Knöpfe, Footer-Marke kreisrund.
- **Borders**: 1 px `neutral-200` für Trennungen und Kartenränder (innen), 1,5 px für sekundäre Buttons und Karussell-Pfeile, 1 px `neutral-950` als kräftige Oberkante der Angebotsliste.
- **Schatten**: ein UI-Schatten (`shadow-float`, Petrol-getönt) für die schwebende Navigation und den Hero-Bildrahmen. Die gezeichneten Autos und das Straßenschild tragen eigene, ebenfalls Petrol-getönte Bodenschatten als Teil der Illustration.

**Die Ein-Schatten-Regel.** Es gibt genau einen UI-Schatten, und er ist Petrol-getönt, nie grau oder schwarz.

### Fokus und Details
Fokus: 3-px-Ring Logo-Petrol mit 3 px Abstand, auf dunklem Grund Weiß. Textauswahl Petrol mit Weiß, Caret und Formular-Akzent Petrol-Ink, Scrollbar Logo-Grau. Icons stammen aus einem SVG-Sprite (Pfeile, Menü, Schließen, Telefon), Größe 1,25em.

---

## Layout

- **Mobile first.** Breakpoints im Code: 480 (nur Button-Höhe), 640, 768, **1024** (Hauptumbruch zu Desktop), 1100 (nur Footer-Spalten).
- **Raster**: Ein 12-Spalten-Raster nutzt nur das Klassen-Mosaik ab 1024 px (B 7 Spalten über zwei Zeilen, BE und B197 je 5 Spalten rechts, BF17 volle Breite). Alle anderen Abschnitte sind zweispaltige Verhältnisse: Hero-Kopf 1fr : 27rem, Ablauf 5:6, Kontakt 7:5, Angebote und FAQ 4:7 mit sticky Überschrift links, Anmelde-Block 7:4, Intro 26 % · Text · 48 %. Zwischen 768 und 1023 px meist zwei Spalten, darunter eine.
- **Asymmetrie**: Text startet links; im Hero steht die Headline links unten, Lead und Buttons rechts.
- **Hero**: Kopfzeile, darunter gerahmte Bild-Bühne in Containerbreite (Seitenverhältnis 2400:820), darunter Info-Leiste mit vier Spalten (ab 1024 px), zwei Spalten ab 480 px, darunter eine. Unter 860 px Bühnenbreite lässt sich das Bild seitlich wischen.
- **Header**: fest, 76 px hoch; Desktop-Links ab 1024 px, Anmelde-Button ab 640 px, darunter Menü-Knopf (48 px) mit Vollbild-Menü.
- **Footer**: Claim und drei Spalten (ab 768 px drei Spalten mit Claim darüber, ab 1100 px vier Spalten in einer Zeile), darunter die Wortmarke und die Rechtszeile.

---

## Animation

| Token | Wert | Verwendung |
|---|---|---|
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` | Reveals, Hero, Auto, Header-Morph, Pfeile |
| `--ease-ui` | `cubic-bezier(.4, 0, .2, 1)` | Hover, Menü, Akkordeon, Etappen-Farben |
| `--dur-ui` | 180 ms | Buttons, Links, Farben |
| `--dur-med` | 320 ms | Akkordeon, Menü, Header, Unterstreichung |
| `--dur-reveal` | 800 ms | Scroll-Reveal |
| Roll-Kurve | `cubic-bezier(.25, .1, .25, 1)`, 500 ms | Roll-Button |

- **Hero beim Laden**: Headline-Zeilen und rechte Spalte steigen 22 px auf (0,9 s, versetzt 0 / 0,08 / 0,18 s). Der Bildrahmen öffnet sich per `clip-path` von `inset(6% 4% 0 4%)` auf voll (1,1 s, ab 0,2 s), das Foto skaliert dabei von 1,06 auf 1 (1,6 s). Danach blenden die vier Punkte nacheinander ein (0,6 s, ab 0,9 s, je 0,12 s versetzt).
- **Hero-Punkte**: inaktive Punkte pulsieren (Schein 6 → 13 px, 2,6 s, je 0,35 s versetzt); der aktive Punkt wird Petrol-Ink, das Plus dreht sich zum Minus, das Etikett gleitet 6 px nach oben ein (320 ms). Die aktive Spalte der Info-Leiste bekommt eine Petrol-Linie, die sich von links aufzieht (500 ms). Hover (nur Maus), Klick, Tipp und die Spaltentitel schalten um; auf dem Handy wischt das Bild zum gewählten Punkt.
- **Sprachumschalter**: Der Petrol-Daumen gleitet vor dem Seitenwechsel auf die andere Sprache (320 ms, Wechsel nach 220 ms).
- **Reveal**: Opacity 0→1, Y 24→0 px, 800 ms, per IntersectionObserver (Schwelle 12 %, unterer Rand −6 %), einmalig. Ohne JS sichtbar (Klasse `js` am `<html>` schaltet Reveal erst ein).
- **Stagger**: 70 ms je Stufe, im Markup Stufen 0–4 (Intro-Bilder und Text, Klassen-Kacheln, Angebote, Kontakt). Mobilmenü: Links steigen 12 px auf, 520 ms, 45 ms Versatz plus 60 ms.
- **Parallax**: nur das große Intro-Porträt von Viktor Strauch, ±5 % Versatz (Bild 112 % hoch), nur ab 1024 px und ohne reduzierte Bewegung.
- **Header-Morph**: Nach 24 px Scroll (Sentinel) wird die volle weiße Leiste (96 %) zur schwebenden Pille: `translateY(12px)`, max. 1120 px breit, 64 px hoch, Weiß 86 % mit Blur 16 px und Sättigung 1,4, UI-Schatten plus 1-px-Innenlinie; das Logo skaliert auf `scale(.85)`. Alles 320 ms, über Transform statt Positionswechsel.
- **Signatur: Fahrt durch die Ausbildung.** Im Ablauf ist die Straße sticky (Desktop: senkrechte Straße links neben den Etappen; mobil: waagrechte Straße oben mit Nebel-Ausblendkante). Der Scrollfortschritt durch sechs Etappen bewegt das Auto (`getPointAtLength`, Rotation per Tangente) und färbt die Spur dahinter Petrol. Erreichte Stationen füllen sich Petrol, die Etappennummer wird Petrol-Ink. Noch nicht erreichte Etappen sind über die Farbe gedämpft (`neutral-600` für Titel und Text, 6:1 lesbar), nicht über Deckkraft; Farbwechsel 300–400 ms.
- **Team-Bühne**: Fotos überblenden in 700 ms ease-out, Zitat und Name blenden 500 ms mit 4 px Hub ein, Avatar hebt sich beim Hover 2 px, Pfeiltasten wechseln zwischen Fahrlehrern.
- **Klassen-Kacheln**: Beim Hover fährt das Auto 10 px nach rechts, Schaltknauf und Sitze heben sich 4 px (600–700 ms).
- **Angebotszeilen**: Hover-Fläche Nebel wächst aus `scaleY(.85)`, Pfeil 6 px nach rechts.
- **Footer-Fahrstreifen**: Mittellinie läuft in 18 s linear endlos nach links (nur ohne reduzierte Bewegung).
- **prefers-reduced-motion**: alle Dauern auf 0,01 ms, kein Reveal (Inhalte sofort sichtbar), keine Parallaxe, keine Straßenzeichnung, kein laufender Footer-Streifen, Ablauf ohne Sticky, Auto steht am Ziel, alle Stationen aktiv.

---

## Informationsarchitektur

| Seite | Pfad | Zweck |
|---|---|---|
| Startseite | `/` | Geführte Geschichte, beantwortet die Kernfragen von „wer, was, wo“ bis „wie anmelden“ |
| Führerschein | `/fuehrerschein/` | Klassen B, BE, B197, BF17 im Detail, Schnellkurs, Auffrischung, Preis-PDFs; sticky Sprungleiste |
| Berufskraftfahrer | `/berufskraftfahrer/` | BKF-Weiterbildung Module 1–5, Schlüsselzahl 95 (eigene Zielgruppe) |
| Über uns | `/ueber-uns/` | Team, Haltung, Fuhrpark, Stellenanzeige (`#jobs`) |
| Anmeldung & Kontakt | `/anmeldung/` | Online-Anmeldung (extern), Unterlagen, Formulare, App MAX, Finanzierung, Kontakt (`#kontakt`), Anfahrt |
| По-русски | `/ru/` | Kompakte russische Seite mit den wichtigsten Fakten |
| Impressum | `/impressum/` | Text unverändert vom Original |
| Datenschutz | `/datenschutz/` | Text unverändert vom Original |
| 404 | `/404.html` | „Falsch abgebogen.“ mit Weg zurück |

Hauptnavigation (Desktop): Führerschein · Ablauf · Über uns · Kontakt · [DE | RU] · [Jetzt anmelden]. Der Sprachumschalter steht auf allen Seiten und Größen in der Kopfzeile (mobil zwischen Logo und Menü-Button); DE führt zur Startseite, RU zur russischen Seite. Mobilmenü zusätzlich mit Berufskraftfahrer. Footer: Kontakt, Fahrschule (inkl. „Fahrlehrer gesucht“), Folgen (Instagram, Facebook), Impressum, Datenschutz. Die alten Menüpunkte „Information“, „Maxi“, „BF17“, „BKF“ gehen in sprechenden Seiten auf.

## Übernommene Vorlagen (MotionSites)

Auf Wunsch wurden Muster aus der MotionSites-Bibliothek übernommen. Übernommen wurden nur Aufbau und Bewegung, keine Bilder, Texte oder Schriften; umgesetzt in Vanilla-HTML/CSS/JS im eigenen Designsystem.

| Vorlage | Einsatz | Anpassung |
|---|---|---|
| Veyra Electric | Startseite, Hero | Nachgebaut nach der öffentlichen Vorschau (der Bauplan-Text war nach Ausschöpfen des Gratis-Kontingents gesperrt): Kopfzeile mit Headline und Hinweis, gerahmte Bild-Bühne mit leuchtenden Punkten und Etikett mit Pfeil, Info-Leiste mit vier Spalten. Petrol statt Neongelb, echtes Fuhrparkfoto statt Studio-Auto, Punkte zeigen nur überprüfbare Fakten |
| Axion About | Startseite, Intro | Raster 26 % · Text · 48 % ab 1024 px: kleines Schaufensterfoto unten links (Radius `md`), Text oben in der Mitte, großes Porträt von Inhaber Viktor Strauch rechts mit Parallaxe; Roll-Button „Mehr über uns“. Keine Jahreszahlen im Intro. 640–1023 px: Text über zwei Fotos (45:55). |
| Talent Collective | Startseite, Team | Bühne im Container statt Vollbild, weil die Fotos nur 1200 px breit sind. Ab 1024 px steht das Foto nur in den rechten 60 %, links eine Nacht-Petrol-Fläche (40 %) mit Überschrift, Zitat, Avatar-Leiste und Meta-Zeile; unter 1024 px liegt die Überschrift auf einem Nacht-Petrol-Band über dem Foto, damit kein Gesicht verdeckt wird. 700-ms-Überblendung; Avatar-Leiste mit Jahreszahl (1984 · 1988 · 2000 · 2007) statt Punkt, aktiver Avatar mit Petrol- und Weißring; Meta-Zeile Name · seit · Link. |
| Stark Minimal Footer | Footer aller Seiten | Punkte-Band ersetzt durch Footer-Fahrstreifen (Asphalt, Petrol-Kanten, laufende Mittellinie 18 s, aus bei reduzierter Bewegung). Claim „Wir sehen uns auf der Straße.“ plus drei Spalten, übergroße Wortmarke mit Straßen-S-Kreismarke, Rechtszeile 15 px statt 9 px. |

Die passenderen Auto- und Scroll-Vorlagen (z. B. „Scroll Landing Page“, „Avelon Drive“) sind Premium und ohne MotionSites-Abo nicht abrufbar.

## Startseite

1. **Hero** (Muster nach MotionSites „Veyra Electric“) – „Führerschein in Lahr.“ groß links (Lahr in Petrol), rechts Lead, Roll-Button „Jetzt anmelden“ und „Klassen ansehen“. Darunter das echte Fuhrparkfoto als große Bühne mit vier Punkten: Hyundai → Klasse B und BE, VW → Automatik + Schaltung, Peter Harter → seit 1984, Schaufenster-Logo → Schwarzwaldstraße 93. Die Info-Leiste darunter erklärt die vier Punkte und verlinkt in die Seite. Beantwortet sofort: wer, was, wo, und zeigt die echten Menschen und Autos.
2. **Intro: Bei uns darfst du Fehler machen** – Haltung in zwei Sätzen, Hinweis auf Russisch, Schaufensterfoto und Porträt von Viktor Strauch im asymmetrischen Raster. Vertrauen kommt vor dem Angebot, weil Eltern zuerst wissen wollen, wem sie ihr Kind anvertrauen; der Inhaber steht mit Gesicht dafür.
3. **Führerscheinklassen** – Streifen-Band als Oberkante, dann ein Mosaik aus vier unterschiedlich großen Kacheln: B (Mint, groß), BE (Weiß mit Linie), B197 („Automatik oder Schaltung? Beides.“, Nacht-Petrol), BF17 (Weiß, Querformat). Große Klassen-Buchstaben, eigene Fahrzeug-Illustrationen. Direkt nach dem Vertrauen, weil hier die Entscheidung fällt.
4. **Ablauf** – Die Straße wird sticky, das Auto fährt durch Anmelden, Unterlagen, Theorie, Fahrstunden, Prüfung, Führerschein. Signatur-Moment und Antwort auf „Wie läuft das ab?“.
5. **Team** – Bühne mit den vier Fahrlehrern am eigenen Auto; die Avatar-Leiste zeigt die Jahreszahlen 1984 · 1988 · 2000 · 2007 als Beleg, ein Klick wechselt Foto, Spruch und Name. Echte Menschen als Bildmoment nach dem abstrakten Ablauf.
6. **Mehr als die erste Fahrstunde** – Editoriale Liste mit sticky Überschrift: Theorie-Schnellkurs, Auffrischung, BKF-Weiterbildung, Finanzierung, App Fahren Lernen MAX. Für die zweite Zielgruppe (Erwachsene, Profis), deshalb nach dem Kernangebot.
7. **Kontakt & Standort** – Telefonnummer groß in Straßenschrift, E-Mail, Adresse, Unterrichtszeiten, Routenlink, russischer Hinweis; daneben das gezeichnete Straßenschild mit Hausnummer. Kein Formular, weil Anruf und Online-Anmeldung die echten Wege sind.
8. **FAQ** – Sieben echte Fragen (Alter, Unterlagen, Automatik, Kosten, Russisch, Schnellkurs, Finanzierung) mit Antworten aus den Originalinhalten; räumt die letzten Einwände vor dem Abschluss aus.
9. **Abschluss** – Petrol-Ink-Fläche: „Bereit für die erste Fahrstunde?“, Anmelden und Anrufen. Die Straße läuft unten aus; danach folgt der Footer mit dem Fahrstreifen.
