---
name: Fahrschule Strauch
description: Aufbau, Radien, Abstände und Schriftgrade 1:1 nach shophoki.com, besetzt mit dem Petrol des Logos, echten Fotos und eigenen Illustrationen.
colors:
  paper: "#ffffff"
  mint: "#e3f3f4"
  mint2: "#d2e9eb"
  cream: "#f1f8f8"
  forest: "#0b5258"
  forest-hover: "#0d6269"
  forest2: "#0e3b3f"
  forest3: "#0a2c2f"
  forest-glow: "#12676e"
  green: "#00717b"
  accent: "#0199a6"
  lime: "#a5e1e6"
  lime-hover: "#bdeaee"
  ink: "#1c2224"
  muted: "#565d60"
  line: "#dbe7e8"
  footer: "#d4e6e7"
typography:
  display:
    fontFamily: "Schibsted Grotesk, Geist, system-ui, sans-serif"
    fontSize: "clamp(34px, 6vw, 64px)"
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "-0.03em"
  h1:
    fontFamily: "Schibsted Grotesk, Geist, system-ui, sans-serif"
    fontSize: "clamp(37px, 8.7vw, 78px)"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.8px"
  headline:
    fontFamily: "Schibsted Grotesk, Geist, system-ui, sans-serif"
    fontSize: "clamp(36px, 8.2vw, 72px)"
    fontWeight: 600
    lineHeight: 1.03
    letterSpacing: "-1.4px"
  title:
    fontFamily: "Schibsted Grotesk, Geist, system-ui, sans-serif"
    fontSize: "26px"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.4px"
  lead:
    fontFamily: "Geist, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(16px, 2.3vw, 19px)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Geist, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Space Mono, Geist Mono, ui-monospace, Menlo, monospace"
    fontSize: "11px"
    fontWeight: 400
    letterSpacing: "0.12em"
  button:
    fontFamily: "Geist, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.2
rounded:
  sm: "12px"
  md: "16px"
  card: "22px"
  tile: "24px"
  media: "28px"
  stage: "34px"
  pill: "999px"
spacing:
  pad: "22px"
  wrap: "1180px"
  wrap-wide: "1240px"
  header: "72px"
  header-desktop: "98px"
components:
  button-primary:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.paper}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "14px 28px"
  button-primary-hover:
    backgroundColor: "{colors.forest-hover}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.forest}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "12px 28px"
  button-outline-hover:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.paper}"
  button-lime:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.forest3}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "15px 30px"
  button-lime-hover:
    backgroundColor: "{colors.lime-hover}"
  button-small:
    rounded: "{rounded.pill}"
    padding: "7px 18px"
  chip:
    backgroundColor: "{colors.mint}"
    textColor: "{colors.forest}"
    rounded: "{rounded.pill}"
    padding: "5px 11px"
  filter-chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.forest}"
    rounded: "{rounded.pill}"
    padding: "7px 13px"
  filter-chip-active:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.paper}"
  tile-mint:
    backgroundColor: "{colors.mint}"
    textColor: "{colors.ink}"
    rounded: "{rounded.tile}"
    padding: "26px"
  tile-dark:
    backgroundColor: "{colors.forest2}"
    textColor: "{colors.paper}"
    rounded: "{rounded.tile}"
    padding: "26px"
  review-card:
    backgroundColor: "{colors.mint}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "26px"
  faq-item:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "16px 18px"
  header-pill:
    backgroundColor: "rgb(255 255 255 / 0.85)"
    rounded: "{rounded.pill}"
    height: "44px"
    width: "780px"
    padding: "0 16px"
  footer:
    backgroundColor: "{colors.footer}"
    textColor: "#000000"
    padding: "72px 0 34px"
---

# Design System: Fahrschule Strauch

## Overview

**Creative North Star: "HOKI in Petrol"**

Die Website übernimmt den Aufbau von shophoki.com 1:1: Gliederung der Abschnitte, Radien, Abstände, Schriftgrade und das Verhalten der Bausteine. Eigen sind nur die Besetzung und der Inhalt: HOKIs Waldgrün wird durch das Petrol des Logos ersetzt, Produktfotos durch echte Fotos von Team und Fuhrpark, Produktbilder durch eigene Fahrzeug-Illustrationen mit dem echten Logo. Die Token im Kopf dieser Datei sind verbindlich und entsprechen `src/styles/tokens.css`; die Bausteine stehen in `src/styles/hoki.css`, das Verhalten in `src/scripts/main.js`. Bewegung, Schatten, Breakpoints und Beispiel-Bausteine stehen maschinenlesbar in `.impeccable/design.json`.

Die Seite ist eine Folge von Bausteinen, die je einen HOKI-Abschnitt spiegeln: Vollbild-Foto mit Abdunklung und weißer Headline, waagrechte Kachelreihen mit Fortschrittsbalken, Mint-Karten, dunkle Petrol-Bänder mit fließendem Verlauf, Akkordeon mit Filter-Chips, Mint-Footer. Weiß trägt die Seite, Mint gruppiert, Nacht-Petrol setzt die dunklen Momente. Mobil zuerst: fast jede Reihe ist auf dem Handy wischbar.

Was entfernt wurde und nicht zurückkommt: Barlow Semi Condensed und Onest, die Straßen-Animation im Ablauf, die Team-Bühne, der Veyra-Hero, der Footer-Fahrstreifen und das Streifen-Band als Kante.

**Key Characteristics:**
- Aufbau, Radien, Abstände und Schriftgrade wie HOKI, Farben aus dem Logo
- Schibsted Grotesk für Überschriften, Geist für Text, Space Mono für kleine Etiketten
- Vollbild-Fotos mit Abdunklung (Scrim), weiße Headline unten links, Akzentwort in Petrol hell
- Waagrechte, wischbare Reihen mit 2-px-Fortschrittsbalken statt Raster auf dem Handy
- Pillen-Knöpfe, Kacheln mit 22 bis 34 px Radius
- Fließende Petrol-Verläufe als einzige Dauerbewegung, alles aus bei reduzierter Bewegung

### HOKI-Referenz: Farbzuordnung

| HOKI | Unser Token | Rolle |
|---|---|---|
| forest #26401F | `forest` | Knöpfe, Fortschrittsbalken, Text auf Mint |
| forest2 #1A2C18 | `forest2` | dunkle Flächen, Foto-Platzhalter |
| (tiefster Verlaufston) | `forest3` | dunkles Ende der Verläufe, Schrift auf Lime |
| #3c5b35 | `forest-glow` | heller Ton der Verläufe |
| lime #C6E09B | `lime` | Akzent auf dunklem Grund |
| mint #EAF2E6 | `mint` | Kacheln, Karten, Chips |
| #E1EDDB | `mint2` | 1-px-Rand der Mint-Karten |
| #f4f1ea | `cream` | Grund der Kreis-Karten |
| Salbei-/Grün-Akzente #7ba64c / #6f9a45 | `accent` | Akzentwort in großen Überschriften |
| #56613E | `green` | Mono-Etiketten auf Weiß |
| #1C2419 | `ink` | Text |
| #6B7563 | `muted` | Sekundärtext, für AA etwas dunkler gesetzt |
| #DDE6D7 | `line` | Linien, Balkenspur |
| Footer rgb(213 222 205) | `footer` | Footer-Fläche |
| Scrim rgba(14,22,10,…) | `--scrim` 8 34 37 | Abdunklung über Fotos (als RGB-Tripel mit variabler Deckkraft) |

## Colors

Weißes Papier, Mint als Gruppierung, Petrol in sechs Stufen vom Akzent bis zur Nacht; keine Fremdfarbe.

### Primary
- **Petrol-Wald** (`forest`): Füllung aller Haupt-Knöpfe, Fortschrittsbalken, aktiver Filter-Chip, aktiver Sprach-Daumen, Text und Icons auf Mint. Hover hebt auf `forest-hover`.
- **Logo-Petrol** (`accent`): das Petrol des Logos. Als Schrift nur im Akzentwort großer Überschriften (Unterseiten-H1, Abschnittsköpfe, `revhead`, aktueller Menüpunkt), außerdem Fokus-Ring, Textauswahl und Hausnummernschild der Straßenschild-Grafik.
- **Petrol-Tinte** (`green`): Mono-Etiketten, Häkchen-Icons und kleine Akzente auf Weiß; Caret- und Formular-Akzentfarbe.

### Secondary
- **Nacht-Petrol** (`forest2`): dunkle Kacheln, Expertenkarte, Hintergrund hinter Fotos. Mit `forest3` (tiefster Ton) und `forest-glow` (heller Ton) bildet es alle Verläufe der dunklen Flächen.
- **Mint** (`mint`, Rand `mint2`): Kacheln, Bewertungs-Karten, Chips, Hover-Grund runder Icon-Knöpfe, Sprachumschalter.
- **Nebel** (`cream`): Grund der Kreis-Karten im nf-Baustein.

### Tertiary
- **Petrol hell** (`lime`): der Akzent auf dunklem Grund. Akzentwort in Hero- und Band-Headlines, Etiketten auf Fotos, Icons auf dunklen Flächen, Häkchen-Punkte, heller Knopf (`button-lime`) mit `forest3`-Schrift.

### Neutral
- **Tinte** (`ink`): Text und Überschriften auf Weiß.
- **Grau** (`muted`): Leads, Beschreibungen, Fußnoten, Hinweise.
- **Linie** (`line`): Trennlinien, Spur des Fortschrittsbalkens, Kartenränder.
- **Footer-Mint** (`footer`): nur die Footer-Fläche, Schrift darauf Schwarz.
- **Papier** (`paper`): Seitengrund, Kopfzeile, FAQ-Einträge.

### Named Rules
**The Großschrift-Akzent Rule.** Logo-Petrol (`accent`) erreicht auf Weiß nur 3,44:1 und steht als Schrift ausschließlich ab 24 px. Kleine farbige Schrift auf Weiß ist `green` oder `forest`.

**The Hell-auf-Dunkel Rule.** Auf Nacht-Petrol und auf Fotos ist `lime` die einzige Akzentfarbe; Text bleibt Weiß oder Weiß mit 82 bis 96 % Deckkraft.

**The Scrim Rule.** Jedes Foto, auf dem Text steht, trägt eine Abdunklung aus `--scrim` (Verlauf nach unten dunkler, mobil unter 700 px stärker: bis 0,9) und zusätzlich einen weichen Textschatten. Kein Text direkt auf ungedunkeltem Foto.

## Typography

**Display Font:** Schibsted Grotesk (variabel 400–900, selbst gehostet, Latein und Latein-Ext), Rückfall Geist
**Body Font:** Geist (variabel, selbst gehostet, mit Kyrillisch)
**Label/Mono Font:** Space Mono 400 (Latein), Kyrillisch in Geist Mono

**Character:** Eine kompakte, leicht kantige Groteske mit enger Laufweite für Überschriften, eine neutrale, klare Groteske für alles Lesbare, eine Monospace nur für kleine Etiketten in Versalien.

**Russisch:** Schibsted Grotesk und Space Mono haben kein Kyrillisch. Unter `html:lang(ru)` wird `--disp` auf Geist und `--mono` auf Geist Mono umgestellt, damit Überschriften und Etiketten nicht in einer gemischten Schrift erscheinen.

### Hierarchy
- **Display** (500, 34 → 64 px, 1,02): nur die Headline im Startseiten-Hero, weiß auf Foto, max. 20ch.
- **H1** (600, 37 → 78 px, 1,05): Unterseiten-Köpfe, Akzentwort in `accent`; Rechtstexte 37 → 64 px.
- **Headline** (600, 36 → 72 px, 1,03, −1,4 px): Abschnittsköpfe. Varianten nach Baustein: qa 44 → 82 px, ki 40 → 72 px, pz 32 → 56 px, faq 31 → 52 px, Instagram-Kopf 26 → 32 px, `revhead` 24 → 34 px (Gewicht 500).
- **Title** (600, 26 px, 1,1): Kacheltitel; verwandte Stufen 17–29 px für Karten, Schritte und Foto-Kacheln.
- **Lead** (400, 16 → 19 px, 1,55): Unterzeile unter Überschriften in `muted`, max. 46ch.
- **Body** (400, 16 px, 1,55): Grundtext; Rechtstexte 1,6 Zeilenhöhe, max. 68ch.
- **Label** (Space Mono 400, 9–12 px, 0,1–0,2em, Versalien): Etiketten auf Kacheln, Badges, Brotkrumen, Begriffe in Datenlisten, Bildunterschriften im Karussell, Sprachumschalter.
- **Button** (Geist 600, 15 px, 1,2; klein 13 px).

Überschriften: `text-wrap: balance`, keine automatische Trennung. Absätze: `text-wrap: pretty`; Silbentrennung nur in deutschen Rechtstexten.

### Named Rules
**The Zwei-Ton-Überschrift Rule.** Große Überschriften setzen den zweiten Satzteil farbig: auf Weiß in `accent`, auf Foto und Nacht-Petrol in `lime`. Nur ein farbiger Teil pro Überschrift.

## Layout

- **Container**: `wrap` 1180 px mit seitlichem Rand `pad` 22 px; Produkt-Hero ab 1200 px `wrap-wide` 1240 px; Rechtstexte 760 px.
- **Mobil zuerst.** Breakpoints im Code: 640, 700, 760, 820, 880, 900, 1000 (Kopfzeile Desktop), 1100, 1200, 1300 px; dazu `max-width: 699px` für stärkere Scrims.
- **Reihen statt Raster**: Kacheln, Karten und Videos liegen in waagrechten Scroll-Reihen mit Scroll-Snap, ohne Scrollbar; darunter ein 2-px-Fortschrittsbalken mit Pfeil-Knopf (springt eine Kachel weiter, am Ende zurück an den Anfang). Der Balken verschwindet, wenn nichts zu scrollen ist.
- **Abschnittsabstände** sind je Baustein fest gesetzt wie bei HOKI (z. B. sol unten 64 px, nf 24/54 px, pz 58/62 px, faq 56/56 px, Footer 72/34 px), keine globale Abstandsskala.
- **Produkt-Hero**: ab 900 px zweispaltig (1,05fr : 0,95fr, Bild max. 440 px, ab 1200 px 500 px), darunter einspaltig.
- **Kopfzeile**: drei Spalten (Menü und Telefon | Logo mittig | Sprache), 72 px hoch, ab 1000 px 98 px. Scroll-Rand oben 90 px.

## Elevation & Depth

Hybrid: Tiefe entsteht zuerst über Fläche (Weiß, Mint, Nacht-Petrol) und über Fotos mit Scrim; Schatten sind weich, groß und Petrol-getönt (`rgb(10 44 47 / …)`), nie hart.

### Shadow Vocabulary
- **Knopf** (`0 8px 22px rgb(10 44 47 / .14)`): Haupt-Knopf.
- **Kachel klein** (`0 6px 16px rgb(10 44 47 / .06)`): Icon-Feld in ki-Kacheln.
- **Kreis-Karte** (`0 14px 32px rgb(10 44 47 / .08)`, Hover `0 24px 46px … / .14`): nf-Kreise.
- **Offenes Akkordeon** (`0 14px 34px rgb(10 44 47 / .08)`).
- **Bildkachel** (`0 16px 38px … / .16` bis `0 18px 40px … / .18`): Hochkant-Videos, Coverflow-Bilder, Dokument-Vorschau.
- **Große Karte** (`0 20px 46px rgb(10 44 47 / .2)`): Foto- und Petrol-Karten im nf-Baustein.
- **Schwebende Kopfzeile** (`0 8px 24px rgb(0 0 0 / .08)` plus 1-px-Rand Weiß 80 %).

### Named Rules
**The Weich-und-Getönt Rule.** Schatten sind groß und weich, auf Inhalten Petrol-getönt (rgb(10 44 47)); kein harter Versatz, keine Kontur-Schatten.

## Shapes

- **Radien**: `sm` 12 px (Kennzahl-Kasten, quadratische Bildkarten), `md` 16 px (Coverflow-Bilder, FAQ-Einträge), `card` 22 px (Startseiten-Kacheln, Bewertungs-Karten, Hochkant-Videos), `tile` 24 px (Kacheln der Unterseiten, große Karten, ki-Kacheln), `media` 28 px (Produktbild), `stage` 34 px (Foto-Bühne im cm-Baustein), `pill` 999 px (Knöpfe, Chips, Sprachumschalter, schwebende Kopfzeile). Einzelwerte: 20 px Schritt-Karten im pz-Band, 15 px und 14 px Icon-Felder, 8 px Ecksymbol im Karussell.
- **Kreise**: Icon-Knöpfe, Avatare, Häkchen-Punkte, Schritt-Nummern, Kreis-Karten.
- **Ränder**: 1 px `mint2` an Mint-Karten, 1 px `line` an weißen Karten und Chips, 2 px `forest` am Outline-Knopf.
- **Seitenverhältnisse**: 4:5 Startseiten-Kacheln und Produktbild, 3:4 Unterseiten-Kacheln, 9:16 Videos, 4:3 Karussell, 1:1 Bildkarten und Kreise.

## Components

### Bausteine und ihre HOKI-Vorlage

| Baustein | HOKI-Vorlage | Einsatz |
|---|---|---|
| `hd` Kopfzeile | dreispaltiger Header, beim Scrollen schwebende Pille | alle Seiten |
| `sol` | hoki-solution: Vollbild-Foto-Hero, darunter Kachelreihe 4:5 mit Chips „Gut zu wissen“ | Startseite |
| `cm` | hoki-cm: große Zahl auf Foto (1984), Bewertungs-Karten, Hochkant-Kacheln | Startseite |
| `ig` | Instagram-Coverflow | Startseite |
| `pr` + `tiles` | Produkt-Hero (geteilt, wechselndes Wort, Kennzahl-Kasten, Banner) und Kachelreihe 3:4 | alle Unterseiten |
| `nf` | hoki-nf: Kreis-Karten und zwei große Karten | Führerschein, Anmeldung |
| `ki` | hoki-ki: fließender Petrol-Verlauf mit Eingabe-Pille, darunter Kacheln | Führerschein (B197), Kontakt mit Straßenschild |
| `qa` | hoki-qa: quadratische Bildkarten | Führerschein, Über uns, Anmeldung |
| `pz` | hoki-pz: dunkles Band mit drei Schritten | Führerschein, Berufskraftfahrer, Über uns |
| `faq` | hoki-faq: Filter-Chips und Akkordeon | Führerschein |
| `ft` | Mint-Footer | alle Seiten |

### Buttons
- **Shape:** Pille (999 px), 15 px Geist 600, Icon 16 px rechts.
- **Primär:** `forest` mit Weiß, Knopf-Schatten; Hover `forest-hover` und 1 px nach oben; aktiv `scale(.98)`; Übergang 150 ms.
- **Outline:** transparent, 2 px Rand `forest`; Hover gefüllt mit Weiß.
- **Lime:** `lime` mit `forest3`-Schrift, für dunkle Bänder.
- **Klein:** 13 px, 7 × 18 px Innenabstand.
- **Pill-Button und Eingabe-Pille** im ki-Band: Weiß 95 %, runder `forest`-Sendeknopf.

### Chips
- **Effekt-Chips**: `mint` mit 1-px-Rand `mint2`, 12,5 px Geist 500 in `forest`.
- **Glas-Chips** auf Fotos: Weiß 12 % mit 1-px-Rand Weiß 24 % und Blur 7 px.
- **Filter-Chips** (FAQ): weiß mit `line`-Rand; gedrückt (`aria-pressed`) `forest` gefüllt mit Weiß.

### Cards / Containers
- **Kacheln** (`tile`): Mint, Petrol-Verlauf (`forest-glow` → `forest` → `forest2`) oder Foto mit Scrim; Innenabstand 26 px; Inhalte unten (Häkchen-Liste, Kennzahlen mit 31-px-Zahlen).
- **Bewertungs-Karte**: Mint mit `mint2`-Rand; Expertenkarte Nacht-Petrol mit Zitat in Schibsted.
- **Illustrations-Flächen**: radialer Verlauf Weiß → Mint hinter freigestellten Illustrationen.
- **Kreis-Karten** (nf): Weiß → `cream`, Hover hebt und färbt den Rand `lime`.

### Inputs / Fields
Keine eigenen Formularfelder: die Anmeldung läuft extern (Fahrschulmanager) oder per PDF. Die Eingabe-Pille im ki-Band ist ein Link im Aussehen eines Eingabefelds.

### Navigation
- **Kopfzeile**: weiß, Menü- und Telefon-Knopf links (36-px-Kreis, Hover Mint), Logo mittig (36 px, ab 1000 px 46 px), Sprachumschalter rechts.
- **Schwebende Pille**: Sobald ein 40-px-Wächter oben aus dem Bild ist, wird die Leiste fest, 20 px vom Rand, max. 780 px breit, 44 px hoch, Weiß 85 % mit Blur 18 px; Logo 26 px; gleitet in 320 ms aus −12 px ein.
- **Sprachumschalter DE | RU**: Mint-Pille, Space Mono 11 px; ein `forest`-Daumen markiert die aktive Sprache (`aria-current`). Beim Wechsel gleitet der Daumen (320 ms), der Seitenwechsel folgt nach 240 ms.
- **Menü-Schublade** von links (max. 440 px, 420 ms), Hintergrund Scrim 45 % mit Blur; Links in Schibsted 26 px mit Linie darunter, aktuelle Seite in `accent`; unten Anmelde- und Anruf-Knopf.

### Footer
Fläche `footer`, Schrift Schwarz, drei Spalten ab 760 px. Links unterstrichen (1 px, Hover 2 px), Social-Icons 24 px, Sprachwahl als helle Pillen, Rechtszeile 12,5 px mit Punkt-Trennern, Logo mit `mix-blend-mode: multiply`.

### Bewegung
- **Reveal**: Deckkraft 0 → 1 und 22 px Hub, 800 ms `ease-out`, einmalig per IntersectionObserver (Schwelle 12 %, unterer Rand −6 %), Versatz 80 ms je Stufe. Erst mit Klasse `js` aktiv, ohne JS sichtbar.
- **Coverflow**: aktives Bild mittig, Nachbarn verkleinert (je Stufe −16 %) und abgedunkelt; dreht alle 4,2 s weiter, solange sichtbar und nicht berührt (Pause bei Zeiger, Fokus, außerhalb des Bildes); Klick, Pfeiltasten und Wischen (ab 40 px) schalten; Übergang 600 ms.
- **Wechselndes Wort** in der Unterseiten-H1: alle 2,4 s, Wort gleitet von unten ein und nach oben aus (280 ms); für Screenreader steht der volle Text versteckt daneben.
- **Fließende Verläufe**: ki-Band 16 s plus Lichtflecken 12 s im Wechsel, Banner-Chip im Produktbild 5 s.
- **Hover**: Kacheln heben 4 px, Illustration skaliert 1,04, Pfeile rücken 2–3 px.
- **prefers-reduced-motion**: alle Dauern 0,01 ms, Animationen einmalig, Reveal aus (Inhalt sofort sichtbar), kein Autoplay im Coverflow, kein wechselndes Wort, keine Verzögerung beim Sprachwechsel, Scrollen ohne Glätten.

### Barrierefreiheit
Fokus: 3-px-Ring `accent` mit 3 px Abstand, auf dunklem Grund Weiß. Skip-Link als Pille. Icons aus dem SVG-Sprite (`/icons/sprite.svg`), dekorativ mit `aria-hidden`, Beschriftung über versteckten Text.

## Do's and Don'ts

### Do:
- **Do** neue Abschnitte aus den vorhandenen HOKI-Bausteinen bauen und deren Maße, Radien und Schriftgrade übernehmen.
- **Do** `accent` als Schrift nur ab 24 px einsetzen; kleine Akzente in `green` oder `forest`.
- **Do** jedes Foto mit Text darauf mit einem `--scrim`-Verlauf abdunkeln, mobil stärker.
- **Do** auf dunklem Grund `lime` als einzige Akzentfarbe nutzen.
- **Do** jede Bewegung unter `prefers-reduced-motion` abschalten und Inhalte ohne JS sichtbar lassen.
- **Do** Bilder über `<!-- @pic -->` einbinden (AVIF und WebP aus `assets-src/image-manifest.json`), gemeinsame Teile über `<!-- @include -->`.

### Don't:
- **Don't** HOKIs Grün- und Salbeitöne verwenden; jede Farbe kommt aus den Petrol-Token.
- **Don't** Schibsted Grotesk oder Space Mono für russischen Text erzwingen; die Umstellung über `html:lang(ru)` bleibt.
- **Don't** harte, versetzte Schatten oder graue Kontur-Schatten.
- **Don't** das Logo nachzeichnen oder verändern.

---

## Seiten und Inhalte

| Seite | Pfad | Bausteine |
|---|---|---|
| Startseite | `/` | sol, cm, ig |
| Führerschein | `/fuehrerschein/` | pr + tiles, nf, ki (B197), qa (BF17), pz, faq |
| Berufskraftfahrer | `/berufskraftfahrer/` | pr + tiles, pz |
| Über uns | `/ueber-uns/` | pr + tiles, qa, pz |
| Anmeldung und Kontakt | `/anmeldung/` | pr + tiles, nf, qa, Kontakt im ki-Band mit Straßenschild |
| Impressum, Datenschutz | `/impressum/`, `/datenschutz/` | Rechtstext (760 px), Text unverändert vom Original |
| 404 | `/404.html` | Kopf, Illustration, Weg zurück |

**Keine erfundenen Fakten.** Keine Preise, Bewertungen, Erfolgsquoten, Schülerzahlen oder Auszeichnungen erfinden; Preise nur über die vorhandenen PDFs. Belegt werden darf nur, was die Originalinhalte hergeben: Jahreszahlen des Teams (1984, 1988, 2000, 2007), Klassen, Adresse, echte Fotos und Sprüche.

## Russische Fassung

Die Seiten unter `ru/` (Start, Führerschein, Berufskraftfahrer, Über uns, Anmeldung) werden ausschließlich mit `scripts/translate_ru.py` aus den deutschen Seiten erzeugt und nie von Hand bearbeitet. Das Skript ersetzt jede deutsche Textstelle gezielt und bricht ab, wenn eine Stelle fehlt, damit keine halb übersetzte Seite entsteht. Deshalb: deutschen Text ändern, dann das Skript anpassen und neu laufen lassen. Kopf, Footer und Kontakt haben eigene `-ru`-Teile in `src/partials/`. Impressum und Datenschutz bleiben deutsch. Anrede auf Russisch „вы“.

## Illustrationen

Jede Illustration trägt das echte Logo der Fahrschule, nie ein vom Bildgenerator gezeichnetes. `scripts/illustrations.py` setzt `assets-src/brand/logo.png` per Compositing auf Türen, Anhänger und Lkw (auf dunklem Grund mit weißem Schild darunter), stellt den Hintergrund frei und schneidet zu. Illustrationen stehen freigestellt auf dem radialen Weiß-Mint-Verlauf.

## Scroll-Animationen (seit 02.10.2026, Kundenwunsch)

- **Ablauf mit Etappen-Fahrt (Startseite, `.jr`):** Statt der Kartenreihe eine mintfarbene Fläche (Radius 34). Desktop: Straße links (bleibt beim Scrollen stehen), rechts die sechs Etappen; mobil: Straße waagerecht oben. Das Fahrschulauto (gleiches SVG mit Logo, als `#car-top`) fährt mit dem Scrollen von Station zu Station, die Spur hinter ihm färbt sich hellpetrol, erreichte Stationen werden petrol, die aktuelle Etappe wird zur weißen Karte. Pfadpunkte und Etappenpositionen werden nur bei Größenänderungen vermessen, beim Scrollen nur nachgeschlagen.
- **Überschriften** unterhalb des ersten Bildschirms blenden Wort für Wort leicht ein (`data-split`, 0,3 em, 25 ms Versatz). Überschriften im ersten Bildschirm stehen sofort, damit der sichtbare Inhalt schnell lädt.
- **Kartenreihen** gleiten gestaffelt 16 px von rechts herein, Kreis-Karten, Schritte und FAQ-Einträge blenden mit 97 % Größe ein.
- **Parallaxe:** Der Hero bewegt sich nicht. Das Fuhrparkfoto zoomt heraus, Fotokarten driften leicht, Illustrationen der Autos fahren seitlich ins Bild, die Illustration im Petrol-Band schwebt.
- **Zähler:** „1984“ und Kennzahlen wie „3.500 kg“ zählen hoch.
- **Drei Schritte** leuchten nacheinander auf, während man durch den Abschnitt scrollt.
- Am 02.10.2026 auf Wunsch abgeschwächt: Hero-Bild 0,12, Hero-Text 0,05, Fotozoom 6 %, Drift 2–2,5 %, Einfahren 8 %, Lenken max. 4°.
- **Technik gegen Ruckeln:** Parallaxe, Zoom und einfahrende Autos über View-Timelines (`data-fx`). Der Browser rechnet das selbst, Browser ohne diese Technik lassen die Parallaxe weg.
- Alles wird erst ab dem ersten Scrollen berechnet und läuft nur für sichtbare Elemente. Bei „Bewegung reduzieren“ entfällt alles, die Straße wird ausgeblendet.

## Bildsprache (seit 03.10.2026)

Fotorealistische, ruhige Editorial-Bilder wie bei HOKI statt Illustrationen: warmes Licht, gedämpfte Salbei- und Beigetöne, leichte Körnung, viel Ruhe im Bild, keine Gesichter. Fahrzeuge tragen immer das echte Logo (per `scripts/fotos.py` aufgesetzt). Klassen-Kacheln sind Foto-Kacheln mit Verlauf nach unten und weißer Beschrift (Marke in Hell-Akzent), wie HOKIs Produktkacheln. Kreis-Karten zeigen die Fotos rund beschnitten, das B197-Band ein gerahmtes Hochformatfoto (Radius 28). KI-Bilder sind im Footer und in den Alt-Texten als Symbolbilder gekennzeichnet; Teamfotos sind echt.

## Kopfzeile (seit 03.10.2026)

Dunkles Petrol (`--forest2`) statt Weiß, Logo als weiße Negativ-Version (`/images/logo-weiss.webp`, aus dem Original-Logo eingefärbt), Symbole weiß, Anmelde-Knopf und Sprachschalter-Daumen in Hell-Akzent (`--lime`) mit dunkler Schrift. Die schwebende Pille beim Scrollen ist ebenfalls dunkles Petrol, halbtransparent mit Unschärfe. Menü-Schublade bleibt weiß mit Original-Logo.

## Hell- und Dunkelmodus (seit 07.10.2026)

Umschalter (Mond/Sonne) in der Kopfzeile; ohne eigene Wahl gilt die Geräte-Einstellung (`prefers-color-scheme`), die Wahl wird in `localStorage` (`theme`) gemerkt und vor dem ersten Zeichnen gesetzt (kein Aufblitzen). Alle Farben laufen über Tokens in `tokens.css`; der Dunkelmodus überschreibt sie unter `:root[data-theme='dark']` bzw. per Media-Query.

| Rolle | Hell | Dunkel |
|---|---|---|
| Kopfzeile `--hd-bg` | #0199a6 (Logo-Petrol) | #016a74 |
| Seitengrund `--paper` | #ffffff | #032226 (tiefes Logo-Petrol) |
| Mint `--mint` | #e3f3f4 (Tönung des Logo-Petrols) | #062e33 |
| Karten `--surface` / hervorgehoben `--surface-raised` | #ffffff / #ffffff | #08353b / #0d4a52 |
| Schrift `--ink` / leise `--muted` | #1c2224 / #565d60 | #e8f4f5 / #a6c3c6 |
| Petrol als Schrift `--forest` | #00717b | #a5e1e6 |
| Petrol als Fläche `--brand-bg` (Knöpfe, weiße Schrift ≥ 4,7:1) | #00808b | #007f8a |
| Akzentwort `--accent` (nur ≥ 24 px) | #0199a6 | #4cc6d0 |
| Hell-Akzent auf dunklem Grund `--lime` | #a5e1e6 | #a5e1e6 |
| Footer `--footer` | #d2eaec | #042a2e |

Seit 07.10.2026 auf Wunsch wieder durchgehend in der Fahrschulfarbe: Logo-Petrol #0199A6 (aus dem Logo gemessen) und seine Tönungen statt der gedämpften Salbei-Töne. Weißer Text direkt auf #0199A6 erreicht nur 3,44:1, deshalb tragen Knöpfe #00808B und der Sprachschalter in der Kopfzeile einen leicht abgedunkelten Grund.

Fotos und die Kopfzeile bleiben in beiden Modi gleich. Logos auf dunklem Grund (Footer, Menü-Schublade) wechseln im Dunkelmodus auf die weiße Version.
