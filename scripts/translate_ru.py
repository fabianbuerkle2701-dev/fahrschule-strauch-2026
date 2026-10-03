#!/usr/bin/env python3
"""Erzeugt die russischen Seiten unter ru/ aus den deutschen Seiten.

Jede deutsche Textstelle wird gezielt ersetzt. Fehlt eine Stelle (weil der
deutsche Text geändert wurde), bricht das Skript mit einer Meldung ab, damit
keine Seite halb übersetzt veröffentlicht wird. Danach prüft es, dass keine
bekannten deutschen Wörter im sichtbaren Text übrig sind.

Aufruf: python3 scripts/translate_ru.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://www.fahrschule-strauch.de'

# Seiten mit eigener russischer Fassung (Rechtstexte bleiben deutsch)
PAGES = ['', 'fuehrerschein', 'berufskraftfahrer', 'ueber-uns', 'anmeldung']


def replace_all(text, pairs, page):
    for de, ru in pairs:
        if de not in text:
            sys.exit(f'[{page or "start"}] Text nicht gefunden: {de[:90]!r}')
        text = text.replace(de, ru)
    return text


def common(text, page):
    slug = f'{page}/' if page else ''
    de_url, ru_url = f'/{slug}', f'/ru/{slug}'
    text = text.replace('<html lang="de">', '<html lang="ru">')
    text = text.replace('<!-- @include head locale="de_DE" -->',
                        '<!-- @include head locale="ru_RU" -->\n    <link rel="preload" href="/fonts/geist-cyrillic-wght-normal.woff2" as="font" type="font/woff2" crossorigin />')
    text = re.sub(r'<!-- @include header page="([\w-]+)" de="[^"]*" ru="[^"]*" -->',
                  lambda m: f'<!-- @include header-ru page="{m.group(1)}" de="{de_url}" ru="{ru_url}" -->', text)
    text = re.sub(r'<!-- @include footer de="[^"]*" ru="[^"]*" -->',
                  f'<!-- @include footer-ru de="{de_url}" ru="{ru_url}" -->', text)
    text = text.replace('<!-- @include contact -->', '<!-- @include contact-ru -->')
    # interne Links auf die russischen Seiten umbiegen (Dateien, Bilder, Rechtstexte bleiben)
    text = re.sub(r'href="/(fuehrerschein|ueber-uns|anmeldung|berufskraftfahrer)/', r'href="/ru/\1/', text)
    text = text.replace('href="/#', 'href="/ru/#')
    # Canonical und hreflang
    text = text.replace(f'<link rel="canonical" href="{BASE}{de_url}" />',
                        f'<link rel="canonical" href="{BASE}{ru_url}" />\n'
                        f'    <link rel="alternate" hreflang="de" href="{BASE}{de_url}" />\n'
                        f'    <link rel="alternate" hreflang="ru" href="{BASE}{ru_url}" />')
    text = text.replace(f'<meta property="og:url" content="{BASE}{de_url}" />',
                        f'<meta property="og:url" content="{BASE}{ru_url}" />')
    # doppelte hreflang-Zeilen entfernen
    text = re.sub(r'(\s*<link rel="alternate" hreflang="(de|ru)" href="[^"]+" />)(?=[\s\S]*\1)', '', text)
    return text


# --------------------------------------------------------------------------
# Bausteine, die auf mehreren Seiten vorkommen
ANMELDEN = ('Jetzt anmelden <svg', 'Записаться <svg')
WEITER = ('<span class="visually-hidden">Weiter</span>', '<span class="visually-hidden">Далее</span>')
ANRUFEN = ('</svg>Anrufen</a>', '</svg>Позвонить</a>')
MAIL = ('</svg>E-Mail schreiben</a>', '</svg>Написать письмо</a>')
QUOTE_PETER = ('Der Weg ist das Ziel, viel Spaß auf deinen neuen Wegen.', 'Путь и есть цель. Удачи на новых дорогах!')
QUOTE_GEROLD = ('Ein Stop-Schild ist keine Empfehlung.', 'Знак «Стоп» не рекомендация.')
QUOTE_NADINE = ('Und immer noch Spaß daran, Jugendliche sicher auf die Straße zu bringen.',
                'И мне до сих пор нравится помогать молодым людям безопасно выезжать на дорогу.')
QUOTE_VIKTOR = ('Fährst du rückwärts gegen Baum, verkleinert sich dein Kofferraum!', 'Сдашь назад в дерево, и багажник станет меньше!')
ALT_PETER = ('alt="Peter Harter neben einem Fahrschulauto"', 'alt="Peter Harter рядом с учебным автомобилем"')
ALT_GEROLD = ('alt="Gerold Remmele neben einem Fahrschulauto"', 'alt="Gerold Remmele рядом с учебным автомобилем"')
ALT_NADINE = ('alt="Nadine Dürr an der geöffneten Fahrertür eines Fahrschulautos"', 'alt="Nadine Dürr у открытой водительской двери учебного автомобиля"')
ALT_VIKTOR = ('alt="Viktor Strauch lehnt an einem Fahrschulauto"', 'alt="Viktor Strauch у учебного автомобиля"')
PDF_KB = [(f'PDF, {n} KB', f'PDF, {n} КБ') for n in ('653', '216', '15', '12', '286', '504', '306')]

# --------------------------------------------------------------------------
START = [
    ('<title>Fahrschule Strauch in Lahr | Führerschein Klasse B, BE, BF17 und B197</title>',
     '<title>Автошкола Strauch в Ларе | Права категорий B, BE, BF17 и B197</title>'),
    ('content="Fahrschule Viktor Strauch in Lahr: Führerschein Klasse B und BE, Begleitetes Fahren ab 17 und Automatik mit B197. Jetzt online anmelden, auch auf Russisch."',
     'content="Автошкола Viktor Strauch в Ларе: права категорий B и BE, вождение с 17 лет и автомат с B197. Говорим по-русски. Запишитесь онлайн."'),
    ('<meta property="og:title" content="Fahrschule Strauch: Führerschein in Lahr" />', '<meta property="og:title" content="Автошкола Strauch: права в Ларе" />'),
    ('<meta property="og:description" content="Klasse B und BE, Begleitetes Fahren ab 17 und B197. Schwarzwaldstraße 93, Lahr." />',
     '<meta property="og:description" content="Категории B и BE, вождение с 17 лет и B197. Schwarzwaldstraße 93, Лар. Говорим по-русски." />'),
    ('"url": "https://www.fahrschule-strauch.de/",', '"url": "https://www.fahrschule-strauch.de/ru/",'),
    # Hero
    ('alt="Weißes Fahrschulauto mit dem Logo der Fahrschule Strauch in einer ruhigen Straße bei Abendlicht (KI-Symbolbild)"',
     'alt="Белый учебный автомобиль с логотипом автошколы Strauch на тихой улице в вечернем свете (символическое изображение, создано ИИ)"'),
    ('<span class="sol__label">Fahrschule Viktor Strauch in Lahr</span>', '<span class="sol__label">Автошкола Viktor Strauch в Ларе</span>'),
    ('<span class="visually-hidden">: </span><span class="sol__h">', '<span class="visually-hidden">: </span><span class="sol__h">'),
    ANMELDEN,
    ANRUFEN,
    ('<h2 class="visually-hidden">Führerscheinklassen</h2>', '<h2 class="visually-hidden">Категории прав</h2>'),
    ('Fragen? Ruf an: <a', 'Вопросы? Звоните: <a'),
    ('Sicher und selbstbewusst <em>ans Steuer.</em>', 'Уверенно и спокойно <em>за руль.</em>'),
    ('Klasse B und BE, Begleitetes Fahren ab 17 und Automatik mit Schaltberechtigung. In der Schwarzwaldstraße 93, auf Deutsch und Russisch.',
     'Категории B и BE, вождение с сопровождением с 17 лет и автомат с правом вождения механики. На <span lang="de">Schwarzwaldstraße 93</span>, на немецком и русском.'),
    ('aria-label="Führerscheinklassen"', 'aria-label="Категории прав"'),
    ('<span class="sol__brand">Klasse B <svg', '<span class="sol__brand">Категория B <svg'),
    ('<span class="visually-hidden">Klasse B: </span>Der Führerschein fürs Auto', '<span class="visually-hidden">Категория B: </span>Права на легковой автомобиль'),
    ('<span class="sol__brand">Klasse BE <svg', '<span class="sol__brand">Категория BE <svg'),
    ('<span class="visually-hidden">Klasse BE: </span>Für den großen Anhänger', '<span class="visually-hidden">Категория BE: </span>Для большого прицепа'),
    ('<span class="visually-hidden">B197: </span>Automatik oder Schaltung? Beides.', '<span class="visually-hidden">B197: </span>Автомат или механика? И то и другое.'),
    ('<span class="visually-hidden">BF17: </span>Begleitetes Fahren ab 17', '<span class="visually-hidden">BF17: </span>Вождение с сопровождением с 17 лет'),
    ('<span class="visually-hidden">BKF: </span>Weiterbildung für Berufskraftfahrer', '<span class="visually-hidden">BKF: </span>Повышение квалификации профводителей'),
    ('<p class="lbl">Gut zu wissen</p>', '<p class="lbl">Полезно знать</p>'),
    ('<li>Ab 18</li><li>Mit Begleitung ab 17</li><li>Bis 3.500 kg</li><li>Anhänger bis 750 kg</li>',
     '<li>С 18 лет</li><li>С сопровождением с 17</li><li>До 3500 кг</li><li>Прицеп до 750 кг</li>'),
    ('<li>Ab 18</li><li>Klasse B vorher</li><li>Größere Gespanne</li>', '<li>С 18 лет</li><li>Сначала категория B</li><li>Большие автопоезда</li>'),
    ('<li>Prüfung im Automatikauto</li><li>10 Stunden Schaltwagen</li><li>Testfahrt ab 15 Minuten</li>',
     '<li>Экзамен на автомате</li><li>10 часов на механике</li><li>Пробная поездка от 15 минут</li>'),
    ('<li>Antrag ab 16½</li><li>Begleitperson eingetragen</li><li>Klasse B oder BE</li>',
     '<li>Заявление с 16½</li><li>Сопровождающий вписан</li><li>Категория B или BE</li>'),
    ('<li>Module 1 bis 5</li><li>Schlüsselzahl 95</li><li>Amtlich anerkannt</li>', '<li>Модули 1–5</li><li>Код 95</li><li>Официально признано</li>'),
    ('<span class="visually-hidden">Weitere Klassen</span>', '<span class="visually-hidden">Другие категории</span>'),
    ('Grundbetrag und Preise je Fahrstunde stehen in der Preisinformation für <a href="/files/info-preise-klasse-b.pdf">Klasse B</a> und <a href="/files/info-preise-klasse-be.pdf">Klasse BE</a> (PDF). Theorieunterricht montags von 19:00 bis 20:30 Uhr.',
     'Базовая стоимость и цена урока вождения указаны в информации о ценах для <a href="/files/info-preise-klasse-b.pdf">категории B</a> и <a href="/files/info-preise-klasse-be.pdf">категории BE</a> (PDF, на немецком). Теория по понедельникам с 19:00 до 20:30.'),
    # Zahl auf Foto
    ('alt="Das Team der Fahrschule Strauch mit vier Fahrschulautos vor dem Gebäude in der Schwarzwaldstraße"',
     'alt="Команда автошколы Strauch с четырьмя учебными автомобилями перед зданием на Schwarzwaldstraße"'),
    ('<p class="cm__label">Vier Fahrlehrer, ein Team</p>', '<p class="cm__label">Четыре инструктора, одна команда</p>'),
    ('<span class="small">Fahrlehrer <em>seit 1984.</em></span>', '<span class="small">Инструкторы <em>с 1984 года.</em></span>'),
    ('Peter Harter bringt seit 1984 Menschen das Fahren bei. Mit Gerold Remmele (seit 1988), Nadine Dürr (seit 2000) und Inhaber Viktor Strauch (seit 2007) sitzt bei uns Erfahrung neben dir.',
     'Peter Harter учит людей водить с 1984 года. Вместе с Gerold Remmele (с 1988), Nadine Dürr (с 2000) и владельцем Viktor Strauch (с 2007) рядом с вами сидит опыт.'),
    ('<b>4</b> Fahrlehrer <span', '<b>4</b> инструктора <span'),
    ('</span> Deutsch und Russisch</p>', '</span> Немецкий и русский</p>'),
    # Ablauf
    ('<h2>So läuft deine <em>Ausbildung</em></h2>', '<h2>Как проходит <em>обучение</em></h2>'),
    ('<p>in sechs Etappen, von der Anmeldung bis zum Führerschein</p>', '<p>шесть этапов, от записи до получения прав</p>'),
    ('Online über den Fahrschulmanager, mit dem Anmeldeformular oder direkt bei uns in der Schwarzwaldstraße&nbsp;93.',
     'Онлайн через Fahrschulmanager, с помощью бланка записи или прямо у нас на <span lang="de">Schwarzwaldstraße&nbsp;93</span>.'),
    ('<h3 class="jr__title">Anmelden</h3>', '<h3 class="jr__title">Запись</h3>'),
    ('Zur Anmeldung <svg', 'К записи <svg'),
    *[(f'<span class="jr__num">Etappe {i}</span>', f'<span class="jr__num">Этап {i}</span>') for i in range(1, 7)],
    ('Sehtest, Erste-Hilfe-Kurs, biometrisches Passfoto und Ausweis. Den Führerscheinantrag bekommst du bei uns als Formular.',
     'Проверка зрения, курс первой помощи, биометрическое фото и удостоверение личности. Бланк заявления на права вы получите у нас.'),
    ('<h3 class="jr__title">Unterlagen</h3>', '<h3 class="jr__title">Документы</h3>'),
    ('Unterricht montags von 19:00 bis 20:30 Uhr, mittwochs nach Vereinbarung. Zwischendurch lernst du mit der App Fahren Lernen MAX.',
     'Занятия по понедельникам с 19:00 до 20:30, по средам по договорённости. В промежутках вы учитесь с приложением Fahren Lernen MAX.'),
    ('<h3 class="jr__title">Theorie</h3>', '<h3 class="jr__title">Теория</h3>'),
    ('Grundausbildung und die Sonderfahrten über Land, auf der Autobahn und bei Dunkelheit. Im Schalt- oder im Automatikwagen.',
     'Базовое обучение и особые поездки: за городом, по автобану и в темноте. На механике или на автомате.'),
    ('<h3 class="jr__title">Fahrstunden</h3>', '<h3 class="jr__title">Уроки вождения</h3>'),
    ('Erst die Theorieprüfung, dann die praktische Prüfung. Wir melden dich an, wenn du so weit bist.',
     'Сначала теоретический экзамен, потом практический. Мы запишем вас, когда вы будете готовы.'),
    ('<h3 class="jr__title">Prüfung</h3>', '<h3 class="jr__title">Экзамен</h3>'),
    ('Bestanden. Mit Begleitetem Fahren ab 17 fährst du zunächst mit Begleitung, sonst ab sofort allein.',
     'Сдано. При вождении с 17 лет сначала ездите с сопровождающим, иначе сразу самостоятельно.'),
    ('<h3 class="jr__title">Führerschein</h3>', '<h3 class="jr__title">Права</h3>'),
    # Fahrlehrer
    ('<h2>Wer neben dir <em>sitzt</em></h2>', '<h2>Кто сидит <em>рядом с вами</em></h2>'),
    ('<p>vier Fahrlehrer, in ihren eigenen Worten</p>', '<p>четыре инструктора, своими словами</p>'),
    ALT_PETER, ALT_GEROLD, ALT_NADINE, ALT_VIKTOR,
    *[(f'</svg>Seit {y}</span>', f'</svg>С {y} года</span>') for y in (1984, 1988, 2000, 2007)],
    QUOTE_PETER, QUOTE_GEROLD, QUOTE_NADINE, QUOTE_VIKTOR,
    ('„Путь', '«Путь'), ('дорогах!“', 'дорогах!»'), ('„Знак', '«Знак'), ('рекомендация.“', 'рекомендация.»'),
    ('„И мне', '«И мне'), ('дорогу.“', 'дорогу.»'), ('„Сдашь', '«Сдашь'), ('меньше!“', 'меньше!»'),
    ('</b>Fahrlehrer aller Klassen</p>', '</b>Инструктор по всем категориям</p>'),
    ('</b>Fahrlehrerin</p>', '</b>Инструктор</p>'),
    ('</b>Inhaber und Fahrlehrer</p>', '</b>Владелец и инструктор</p>'),
    ('<span class="visually-hidden">Nächster Fahrlehrer</span>', '<span class="visually-hidden">Следующий инструктор</span>'),
    ('Mehr über unser Team und wie wir unterrichten, liest du auf der Seite <a href="/ueber-uns/">Über uns</a>.',
     'Больше о нашей команде и о том, как мы учим, читайте на странице <a href="/ueber-uns/">О нас</a>.'),
    # Instagram
    ('Folge uns auf Instagram</h2>', 'Мы в Instagram</h2>'),
    ('Die Fahrschule Strauch auf Instagram und Facebook.', 'Автошкола Strauch в Instagram и Facebook.'),
    ('aria-label="Bilder aus der Fahrschule"', 'aria-label="Фотографии из автошколы"'),
    ('alt="Das Team der Fahrschule Strauch mit vier Fahrschulautos"', 'alt="Команда автошколы Strauch с четырьмя учебными автомобилями"'),
    ('<span class="ig__cap"><span>Das Team</span><b>Vier Fahrlehrer</b></span>', '<span class="ig__cap"><span>Команда</span><b>Четыре инструктора</b></span>'),
    ('alt="Inhaber Viktor Strauch lehnt an seinem Fahrschulauto"', 'alt="Владелец Viktor Strauch у своего учебного автомобиля"'),
    ('<span class="ig__cap"><span>Inhaber</span><b>Viktor Strauch</b></span>', '<span class="ig__cap"><span>Владелец</span><b>Viktor Strauch</b></span>'),
    ('alt="Fahrschulauto mit dem Logo der Fahrschule Strauch auf einer Landstraße (KI-Symbolbild)"', 'alt="Учебный автомобиль с логотипом автошколы Strauch на загородной дороге (символическое изображение, создано ИИ)"'),
    ('<span class="ig__cap"><span>Klasse B</span><b>Auf der Landstraße</b></span>', '<span class="ig__cap"><span>Категория B</span><b>На загородной дороге</b></span>'),
    ('alt="Fahrschulauto mit dem Logo der Fahrschule Strauch in einer ruhigen Straße (KI-Symbolbild)"', 'alt="Учебный автомобиль с логотипом автошколы Strauch на тихой улице (символическое изображение, создано ИИ)"'),
    ('<span class="ig__cap"><span>Unterwegs</span><b>Sicher ans Steuer</b></span>', '<span class="ig__cap"><span>В пути</span><b>Уверенно за руль</b></span>'),
    ('alt="Fahrlehrer Gerold Remmele vor dem Schaufenster der Fahrschule mit dem Logo"', 'alt="Инструктор Gerold Remmele перед витриной автошколы с логотипом"'),
    ('<span class="ig__cap"><span>Lahr</span><b>Unser Schaufenster</b></span>', '<span class="ig__cap"><span>Лар</span><b>Наша витрина</b></span>'),
    ('alt="Lkw mit dem Logo der Fahrschule Strauch auf der Autobahn (KI-Symbolbild)"', 'alt="Грузовик с логотипом автошколы Strauch на автобане (символическое изображение, создано ИИ)"'),
    ('<span class="ig__cap"><span>BKF</span><b>Weiterbildung</b></span>', '<span class="ig__cap"><span>BKF</span><b>Повышение квалификации</b></span>'),
    ('<span class="ig__cap"><span>Seit 2000</span><b>Nadine Dürr</b></span>', '<span class="ig__cap"><span>С 2000 года</span><b>Nadine Dürr</b></span>'),
    ('target="_blank">Instagram ansehen</a>', 'target="_blank">Открыть Instagram</a>'),
]

FUEHRERSCHEIN = [
    ('<title>Führerschein Klasse B, BE, B197 und BF17 in Lahr | Fahrschule Strauch</title>',
     '<title>Права категорий B, BE, B197 и BF17 в Ларе | Автошкола Strauch</title>'),
    ('content="Führerschein in Lahr: Klasse B und BE, B197 für Automatik und Schaltung, Begleitetes Fahren ab 17, Theorie-Schnellkurs und Auffrischung. Infos und Preise."',
     'content="Права в Ларе: категории B и BE, B197 (автомат и механика), вождение с 17 лет, экспресс-курс теории и освежение навыков."'),
    ('<meta property="og:title" content="Führerschein in Lahr: Klassen und Kurse" />', '<meta property="og:title" content="Права в Ларе: категории и курсы" />'),
    ('<meta property="og:description" content="Klasse B, BE, B197, BF17, Schnellkurs und Auffrischung bei der Fahrschule Strauch in Lahr." />',
     '<meta property="og:description" content="Категории B, BE, B197, BF17, экспресс-курс и освежение навыков в автошколе Strauch в Ларе." />'),
    # Hero
    ('</span>Führerschein in Lahr</span>', '</span>Права в Ларе</span>'),
    ('Dein Führerschein: <span class="ac"><span class="visually-hidden">Klasse B, Klasse BE, B197 oder ab 17</span><span class="rot" data-rot aria-hidden="true"><span class="rot__sizer" data-w="Klasse BE"></span><span class="rot__w is-on" data-w="Klasse B"></span><span class="rot__w" data-w="Klasse BE"></span><span class="rot__w" data-w="B197"></span><span class="rot__w" data-w="ab 17"></span></span></span>',
     'Ваши права: <span class="ac"><span class="visually-hidden">категория B, категория BE, B197 или с 17 лет</span><span class="rot" data-rot aria-hidden="true"><span class="rot__sizer" data-w="категория BE"></span><span class="rot__w is-on" data-w="категория B"></span><span class="rot__w" data-w="категория BE"></span><span class="rot__w" data-w="B197"></span><span class="rot__w" data-w="с 17 лет"></span></span></span>'),
    ('Wir bilden in den Klassen B und BE aus, auch mit Begleitetem Fahren ab 17 und mit Automatik und Schaltberechtigung. Dazu kommen Schnellkurse und Auffrischungsstunden.',
     'Мы обучаем по категориям B и BE, в том числе вождению с сопровождением с 17 лет и на автомате с правом вождения механики. Кроме того, экспресс-курсы и занятия для освежения навыков.'),
    ('<div class="social__i"><b>B · BE</b><span>Klassen</span></div>', '<div class="social__i"><b>B · BE</b><span>Категории</span></div>'),
    ('<div class="social__i"><b>ab 17</b><span>mit Begleitung</span></div>', '<div class="social__i"><b>с 17</b><span>с сопровождением</span></div>'),
    ('<div class="social__i"><b>B197</b><span>Automatik + Schaltung</span></div>', '<div class="social__i"><b>B197</b><span>Автомат + механика</span></div>'),
    ('alt="Fahrlehrerin Nadine Dürr an der geöffneten Fahrertür eines Fahrschulautos"', 'alt="Инструктор Nadine Dürr у открытой водительской двери учебного автомобиля"'),
    ('</svg>Mit B197 auch Schaltwagen</span>', '</svg>С B197 и механика</span>'),
    # Kacheln
    ('<span class="tag">Klasse B</span>', '<span class="tag">Категория B</span>'),
    ('Der Klassiker für den Alltag.</h2>', 'Классика на каждый день.</h2>'),
    ('<li>Kraftfahrzeuge bis 3.500 kg, für höchstens acht Personen außer dem Fahrer</li>',
     '<li>Автомобили до 3500 кг, не более восьми пассажиров кроме водителя</li>'),
    ('<li>Anhänger bis 750 kg, oder schwerer, solange die Kombination 3.500 kg nicht übersteigt</li>',
     '<li>Прицеп до 750 кг или тяжелее, если сцепка не превышает 3500 кг</li>'),
    ('<li>Ab 18, mit Begleitetem Fahren ab 17</li>', '<li>С 18 лет, с сопровождением с 17</li>'),
    ('<li>Klassen L und AM eingeschlossen</li>', '<li>Включает категории L и AM</li>'),
    ('<span class="mini">Klasse BE</span>', '<span class="mini">Категория BE</span>'),
    ('Für Gespanne mit größerem Anhänger.</h2>', 'Для автопоездов с большим прицепом.</h2>'),
    ('<li>Ab 18</li><li>Mit Begleitung ab 17</li><li>Vorbesitz Klasse B</li>', '<li>С 18 лет</li><li>С сопровождением с 17</li><li>Нужна категория B</li>'),
    ('<li>Kombinationen aus einem Fahrzeug der Klasse B und einem Anhänger</li>', '<li>Сцепки из автомобиля категории B и прицепа,</li>'),
    ('<li>die die Grenzwerte der Klasse B oder B96 übersteigen</li>', '<li>превышающие пределы категории B или B96</li>'),
    ('alt="Fahrlehrer Peter Harter neben einem Fahrschulauto"', 'alt="Инструктор Peter Harter рядом с учебным автомобилем"'),
    ('<span class="kicker">Eckdaten Klasse B</span>', '<span class="kicker">Категория B в цифрах</span>'),
    ('<b>3.500 kg</b><span>zulässige Gesamtmasse</span>', '<b>3500 кг</b><span>разрешённая полная масса</span>'),
    ('<b>750 kg</b><span>Anhänger</span>', '<b>750 кг</b><span>прицеп</span>'),
    ('<b>17</b><span>mit Begleitung</span>', '<b>17</b><span>с сопровождением</span>'),
    ('<span class="tag">Kosten</span>', '<span class="tag">Стоимость</span>'),
    ('Info und Preise zum Herunterladen.</h2>', 'Информация и цены для скачивания.</h2>'),
    ('Grundbetrag, Preise je Fahrstunde und Prüfungsvorstellungen. Was du am Ende zahlst, hängt davon ab, wie viele Fahrstunden du brauchst.',
     'Базовая стоимость, цена урока вождения и экзаменов. Итоговая сумма зависит от того, сколько уроков вам понадобится. Документы на немецком.'),
    ('</svg>Klasse B</a>', '</svg>Категория B</a>'),
    ('</svg>Klasse BE</a>', '</svg>Категория BE</a>'),
    WEITER,
    ANMELDEN,
    ('Alle Preise stehen in der Preisinformation der jeweiligen Klasse.', 'Все цены указаны в информации о ценах для каждой категории.'),
    # Kreise
    ('</span>Alle Angebote</span>', '</span>Все предложения</span>'),
    ('Sechs Wege <b>ans Steuer.</b>', 'Шесть путей <b>за руль.</b>'),
    ('Vom ersten Führerschein bis zur Auffrischung, wenn du schon lange fährst.', 'От первых прав до освежения навыков, если вы водите уже давно.'),
    ('<h3 class="nf__cn">Klasse B</h3>', '<h3 class="nf__cn">Категория B</h3>'),
    ('<span class="nf__tag">Pkw</span>', '<span class="nf__tag">Легковой</span>'),
    ('Pkw und leichte Lkw bis 3,5 t. Ab 18 Jahren, mit Begleitung ab 17.', 'Легковые и лёгкие грузовые до 3,5 т. С 18 лет, с сопровождением с 17.'),
    ('<h3 class="nf__cn">Klasse BE</h3>', '<h3 class="nf__cn">Категория BE</h3>'),
    ('<span class="nf__tag">Anhänger</span>', '<span class="nf__tag">Прицеп</span>'),
    ('Für größere Anhänger hinter dem Pkw. Voraussetzung ist Klasse B.', 'Для больших прицепов за легковым автомобилем. Нужна категория B.'),
    ('<span class="nf__tag">Automatik</span>', '<span class="nf__tag">Автомат</span>'),
    ('Prüfung im Automatikauto, danach auch Schaltwagen fahren.', 'Экзамен на автомате, потом можно водить и механику.'),
    ('<h3 class="nf__cn">Begleitetes Fahren</h3>', '<h3 class="nf__cn">С сопровождением</h3>'),
    ('<span class="nf__tag">ab 17</span>', '<span class="nf__tag">с 17 лет</span>'),
    ('Antrag ab 16½, danach mit eingetragener Begleitperson.', 'Заявление с 16½, потом поездки с вписанным сопровождающим.'),
    ('<h3 class="nf__cn">Theorie-Schnellkurs</h3>', '<h3 class="nf__cn">Экспресс-курс теории</h3>'),
    ('<span class="nf__tag">Theorie</span>', '<span class="nf__tag">Теория</span>'),
    ('Intensivkurs für alle mit wenig Zeit.', 'Интенсивный курс для тех, у кого мало времени.'),
    ('<h3 class="nf__cn">Auffrischung</h3>', '<h3 class="nf__cn">Освежение навыков</h3>'),
    ('<span class="nf__tag">Training</span>', '<span class="nf__tag">Тренировка</span>'),
    ('Wieder sicher fahren, in Klasse B und BE.', 'Снова уверенно за рулём, категории B и BE.'),
    ('<h3 class="bt">Theorie-Schnellkurs</h3>', '<h3 class="bt">Экспресс-курс теории</h3>'),
    ('Wenig Zeit für die Führerscheinausbildung? Im Intensivkurs, oft auch Crashkurs genannt, schaffst du die Theorie in kürzester Zeit. Die nächsten Termine für Klasse B erfährst du telefonisch oder per E-Mail.',
     'Мало времени на обучение? На интенсивном курсе вы пройдёте теорию в кратчайшие сроки. Ближайшие даты для категории B можно узнать по телефону или по электронной почте.'),
    ('Termine erfragen <svg', 'Узнать даты <svg'),
    ('<h3 class="bt">Führerschein auffrischen</h3>', '<h3 class="bt">Освежить навыки вождения</h3>'),
    ('Separate Auffrischungsstunden für die Klassen B und BE. Was trainiert wird, vereinbarst du mit deinem Fahrlehrer. Voraussetzung: Du besitzt die jeweilige Führerscheinklasse.',
     'Отдельные занятия для категорий B и BE. Что тренировать, вы решаете вместе с инструктором. Условие: у вас есть права соответствующей категории.'),
    ('<li>Verkehrsregeln im Theorieunterricht</li>', '<li>Правила на занятиях по теории</li>'),
    ('<li>Schalt- oder Automatikfahrzeug</li>', '<li>Механика или автомат</li>'),
    ('<li>Angstbewältigung</li>', '<li>Преодоление страха</li>'),
    ('<li>Schwierige Verkehrssituationen</li>', '<li>Сложные ситуации на дороге</li>'),
    ('<li>Einparken</li>', '<li>Парковка</li>'),
    ('<li>Fahren bei Dunkelheit</li>', '<li>Вождение в темноте</li>'),
    ('<li>Eis und Schnee (saisonbedingt, nur Pkw)</li>', '<li>Лёд и снег (по сезону, только легковой)</li>'),
    ('Anrufen <svg', 'Позвонить <svg'),
    ('Info und Preise Klasse B (PDF) <svg', 'Информация и цены, категория B (PDF) <svg'),
    # B197
    ('<span class="eyebrow" style="color: var(--lime)">Schlüsselzahl B197</span>', '<span class="eyebrow" style="color: var(--lime)">Код B197</span>'),
    ('<span class="l1">Automatik oder Schaltung? <em>Beides.</em></span><span class="l2">Ein Führerschein, beide Getriebe.</span>',
     '<span class="l1">Автомат или механика? <em>И то и другое.</em></span><span class="l2">Одни права, обе коробки передач.</span>'),
    ('Du machst die Prüfung im Automatikauto und darfst danach ohne Einschränkung auch Schaltwagen fahren. In der Theorie gibt es keinen Unterschied.',
     'Вы сдаёте экзамен на автомате, а потом без ограничений можете водить и механику. В теории разницы нет.'),
    ('<span class="ph">Mit B197 anmelden</span>', '<span class="ph">Записаться на B197</span>'),
    ('alt="Automatik-Wählhebel, dahinter ein Schaltknüppel (KI-Symbolbild)"',
     'alt="Селектор автоматической коробки, за ним рычаг механики (символическое изображение, создано ИИ)"'),
    ('<h3>So läuft <b>B197.</b></h3>', '<h3>Как проходит <b>B197.</b></h3>'),
    ('<p>Fünf Schritte zwischen Automatik und Schaltwagen.</p>', '<p>Пять шагов между автоматом и механикой.</p>'),
    *[(f'<span class="lead">Schritt {i}</span>', f'<span class="lead">Шаг {i}</span>') for i in range(1, 6)],
    ('Grundausbildung</h4><p class="dd">Zum Großteil im Automatikauto. Du kannst aber auch im Schaltwagen beginnen.',
     'Базовое обучение</h4><p class="dd">В основном на автомате. Но можно начать и на механике.'),
    ('Besondere Ausbildungsfahrten</h4><p class="dd">Über Land, auf der Autobahn und bei Dunkelheit, teils im Automatik-, teils im Schaltwagen.',
     'Особые учебные поездки</h4><p class="dd">За городом, по автобану и в темноте, частично на автомате, частично на механике.'),
    ('Mindestens 10 Übungsstunden im Schaltwagen</h4><p class="dd">Erst danach darf die Testfahrt stattfinden.',
     'Не менее 10 часов на механике</h4><p class="dd">Только после этого возможна пробная поездка.'),
    ('Testfahrt von mindestens 15 Minuten</h4><p class="dd">Dein Fahrlehrer stellt fest, dass du den Schaltwagen sicher, verantwortungsvoll und umweltbewusst fährst. Dafür bekommst du eine Bescheinigung.',
     'Пробная поездка не менее 15 минут</h4><p class="dd">Инструктор подтверждает, что вы водите механику безопасно, ответственно и экономично. Об этом вы получаете справку.'),
    ('Praktische Prüfung im Automatikauto</h4><p class="dd">Prüfungsvorbereitung und Prüfung finden im Automatikauto statt.',
     'Практический экзамен на автомате</h4><p class="dd">Подготовка к экзамену и сам экзамен проходят на автомате.'),
    # BF17
    ('</span>Begleitetes Fahren</span>', '</span>Вождение с сопровождением</span>'),
    ('Ab 17 <b>am Steuer.</b>', 'За рулём <b>с 17 лет.</b>'),
    ('Mit 17 Jahren die Klasse B oder BE erwerben und mit einer Begleitperson fahren, die in der Prüfungsbescheinigung namentlich eingetragen ist. Den Antrag stellst du ab 16½ Jahren, mit Einwilligung deiner Erziehungsberechtigten.',
     'В 17 лет получить категорию B или BE и ездить с сопровождающим, который поимённо вписан в экзаменационное свидетельство. Заявление можно подать с 16½ лет с согласия родителей.'),
    ('Antrag als PDF <svg', 'Заявление (PDF) <svg'),
    ('alt="Junge Fahrerin am Steuer, daneben die Begleitperson (KI-Symbolbild)"', 'alt="Молодая ученица за рулём, рядом сопровождающий (символическое изображение, создано ИИ)"'),
    ('<h3 class="qa__title">Mit 16 anfangen</h3>', '<h3 class="qa__title">Начать в 16</h3>'),
    ('Wer mit 16 anfängt, kann zum 17. Geburtstag fertig sein. Die Prüfung legst du kurz vor dem Geburtstag ab.',
     'Кто начинает в 16, может закончить к 17-летию. Экзамен сдаётся незадолго до дня рождения.'),
    ('<li>Personalausweis oder Pass</li>', '<li>Удостоверение личности или паспорт</li>'),
    ('<li>Biometrisches Lichtbild</li>', '<li>Биометрическое фото</li>'),
    ('<li>Sehtest, nicht älter als zwei Jahre</li>', '<li>Проверка зрения не старше двух лет</li>'),
    ('<li>Nachweis Erste Hilfe</li>', '<li>Справка о курсе первой помощи</li>'),
    ('<li>Anlage für jede Begleitperson</li>', '<li>Приложение на каждого сопровождающего</li>'),
    ('<h3 class="qa__title">Diese Unterlagen brauchst du</h3>', '<h3 class="qa__title">Какие документы нужны</h3>'),
    ('Die Anlage zum Antrag enthält Personalien und Unterschrift der Begleitperson, dazu eine Kopie ihres Personalausweises und ihres Führerscheins.',
     'В приложении к заявлению указываются данные и подпись сопровождающего, к нему прилагаются копии его удостоверения личности и прав.'),
    *PDF_KB[4:],
    ('<h3 class="qa__title">Antrag Begleitetes Fahren ab 17</h3>', '<h3 class="qa__title">Заявление на вождение с 17 лет</h3>'),
    ('Ausdrucken, ausfüllen und zur Anmeldung mitbringen.', 'Распечатайте, заполните и принесите на запись. Бланк на немецком.'),
    ('<h3 class="qa__title">Erklärung der Begleitperson</h3>', '<h3 class="qa__title">Заявление сопровождающего</h3>'),
    ('Für jede Begleitperson ein eigenes Formular.', 'Отдельный бланк на каждого сопровождающего.'),
    ('<h3 class="qa__title">Vordruck Kartenführerschein</h3>', '<h3 class="qa__title">Бланк для пластиковых прав</h3>'),
    ('Der Vordruck für deinen Kartenführerschein.', 'Бланк для ваших прав в формате карты.'),
    # Drei Schritte
    ('<span class="eyebrow">In drei Schritten</span>', '<span class="eyebrow">Три шага</span>'),
    ('So meldest du dich an.</h2>', 'Как записаться.</h2>'),
    ('Online, mit dem Formular oder persönlich bei uns in der Schwarzwaldstraße&nbsp;93.',
     'Онлайн, с помощью бланка или лично у нас на <span lang="de">Schwarzwaldstraße&nbsp;93</span>.'),
    ('<h3 class="pz__st">Anmelden</h3>', '<h3 class="pz__st">Записаться</h3>'),
    ('Online über den Fahrschulmanager oder mit dem Anmeldeformular.', 'Онлайн через Fahrschulmanager или с помощью бланка записи.'),
    ('<span class="pz__pill">Online oder auf Papier</span>', '<span class="pz__pill">Онлайн или на бумаге</span>'),
    ('<h3 class="pz__st">Unterlagen sammeln</h3>', '<h3 class="pz__st">Собрать документы</h3>'),
    ('Sehtest, Erste-Hilfe-Kurs, biometrisches Passfoto und Ausweis.', 'Проверка зрения, курс первой помощи, биометрическое фото и удостоверение личности.'),
    ('<span class="pz__pill">Führerscheinantrag bei uns</span>', '<span class="pz__pill">Заявление на права у нас</span>'),
    ('<h3 class="pz__st">Theorie starten</h3>', '<h3 class="pz__st">Начать теорию</h3>'),
    ('Unterricht montags von 19:00 bis 20:30 Uhr, mittwochs nach Vereinbarung.', 'Занятия по понедельникам с 19:00 до 20:30, по средам по договорённости.'),
    ('<span class="pz__pill">Montag 19:00 Uhr</span>', '<span class="pz__pill">Понедельник, 19:00</span>'),
    ('Wir beraten dich auf Deutsch und Russisch.</span>', 'Консультируем на немецком и русском.</span>'),
    # FAQ
    ('<span class="eyebrow">Häufige Fragen</span>', '<span class="eyebrow">Частые вопросы</span>'),
    ('Fragen und Antworten</h2>', 'Вопросы и ответы</h2>'),
    ('Die häufigsten Fragen rund um Führerschein, Unterlagen und Kosten, klar beantwortet.', 'Самые частые вопросы о правах, документах и стоимости, с понятными ответами.'),
    ('aria-label="Fragen filtern"', 'aria-label="Фильтр вопросов"'),
    ('data-faq-chip="alle">Alle</button>', 'data-faq-chip="alle">Все</button>'),
    ('data-faq-chip="start">Voraussetzungen</button>', 'data-faq-chip="start">Условия</button>'),
    ('data-faq-chip="ausbildung">Ausbildung</button>', 'data-faq-chip="ausbildung">Обучение</button>'),
    ('data-faq-chip="kosten">Kosten</button>', 'data-faq-chip="kosten">Стоимость</button>'),
    ('data-faq-chip="sprache">Sprache</button>', 'data-faq-chip="sprache">Язык</button>'),
    ('Ab wann kann ich mit dem Führerschein anfangen?', 'С какого возраста можно начать?'),
    ('Für Klasse B bist du mit 18 dabei. Mit Begleitetem Fahren ab 17 kannst du den Antrag schon ab 16½ Jahren stellen, mit Einwilligung deiner Erziehungsberechtigten. So kannst du pünktlich zum 17. Geburtstag fertig sein.',
     'Для категории B с 18 лет. При вождении с сопровождением с 17 лет заявление можно подать уже с 16½ лет с согласия родителей. Так вы успеете точно к 17-летию.'),
    ('Welche Unterlagen brauche ich?', 'Какие документы нужны?'),
    ('<li>Ausweis oder Pass</li><li>Biometrisches Passfoto</li><li>Sehtest</li><li>Erste Hilfe</li>',
     '<li>Удостоверение или паспорт</li><li>Биометрическое фото</li><li>Проверка зрения</li><li>Первая помощь</li>'),
    ('Die Sehtestbescheinigung darf nicht älter als zwei Jahre sein. Für BF17 kommt für jede Begleitperson ein eigenes Formular dazu. <a href="/anmeldung/#unterlagen">Alle Formulare zum Herunterladen</a>',
     'Справка о проверке зрения должна быть не старше двух лет. Для BF17 на каждого сопровождающего нужен отдельный бланк. <a href="/anmeldung/#unterlagen">Все бланки для скачивания</a>'),
    ('Automatik oder Schaltung, was ist besser?', 'Автомат или механика, что лучше?'),
    ('Mit der Schlüsselzahl B197 musst du dich nicht entscheiden: Du lernst einen Großteil im Automatikauto und machst dort auch die Prüfung. Nach mindestens zehn Übungsstunden im Schaltwagen und einer Testfahrt von mindestens 15 Minuten darfst du später ohne Einschränkung auch Schaltwagen fahren.',
     'С кодом B197 выбирать не нужно: большую часть вы учитесь на автомате и на нём же сдаёте экзамен. После не менее десяти часов на механике и пробной поездки не менее 15 минут вы сможете без ограничений водить и механику.'),
    ('Was ist bei Klasse B eingeschlossen?', 'Что входит в категорию B?'),
    ('Mit Klasse B darfst du auch Fahrzeuge der Klassen L und AM fahren. Ein Vorbesitz ist für Klasse B nicht erforderlich.',
     'С категорией B можно водить и транспорт категорий L и AM. Другие категории для B не нужны.'),
    ('Was kostet der Führerschein?', 'Сколько стоят права?'),
    ('Die Kosten hängen davon ab, wie viele Fahrstunden du brauchst. Grundbetrag, Preise je Fahrstunde und Prüfungsvorstellungen findest du in unserer Preisinformation.',
     'Стоимость зависит от того, сколько уроков вождения вам понадобится. Базовую стоимость, цену урока и экзаменов вы найдёте в нашей информации о ценах (на немецком).'),
    ('<a href="/files/info-preise-klasse-b.pdf">Info und Preise Klasse B (PDF)</a><br /><a href="/files/info-preise-klasse-be.pdf">Info und Preise Klasse BE (PDF)</a>',
     '<a href="/files/info-preise-klasse-b.pdf">Информация и цены, категория B (PDF)</a><br /><a href="/files/info-preise-klasse-be.pdf">Информация и цены, категория BE (PDF)</a>'),
    ('Kann ich den Führerschein finanzieren?', 'Можно ли оплатить права в рассрочку?'),
    ('Ja, mit STARTHILFE, einer Führerscheinfinanzierung, die der Verlag Heinrich Vogel und die Credit Europe Bank speziell für Fahrschüler entwickelt haben.',
     'Да, через STARTHILFE, финансирование прав, которое издательство Heinrich Vogel и Credit Europe Bank разработали специально для учеников автошкол.'),
    ('target="_blank">Mehr zu STARTHILFE</a>', 'target="_blank">Подробнее о STARTHILFE (на немецком)</a>'),
    ('Gibt es einen Schnellkurs?', 'Есть ли экспресс-курс?'),
    ('Ja. Im Theorie-Schnellkurs lernst du die Theorie in wenigen, kompakten Tagen. Die nächsten Termine erfährst du telefonisch oder per E-Mail.',
     'Да. На экспресс-курсе вы пройдёте теорию за несколько насыщенных дней. Ближайшие даты можно узнать по телефону или по электронной почте.'),
    ('<span class="faq__qtx">Sprecht ihr Russisch?</span>', '<span class="faq__qtx">Вы говорите по-русски?</span>'),
    ('<p>Ja, wir beraten dich auch auf Russisch. <span lang="ru">Говорим по-русски.</span></p><p><a href="/ru/fuehrerschein/" hreflang="ru" lang="ru">Информация на русском языке</a></p>',
     '<p>Да, мы консультируем и на русском языке. Говорим по-русски.</p><p><a href="/fuehrerschein/" hreflang="de" lang="de">Diese Seite auf Deutsch</a></p>'),
    ('Noch Fragen? Ruf an: <a', 'Остались вопросы? Звоните: <a'),
]

BKF = [
    ('<title>BKF-Weiterbildung in Lahr, Schlüsselzahl 95 | Fahrschule Strauch</title>',
     '<title>Повышение квалификации профводителей в Ларе, код 95 | Автошкола Strauch</title>'),
    ('content="BKF-Weiterbildung nach BKrFQG in Lahr: Module 1 bis 5 für die Schlüsselzahl 95 bei der Fahrschule Strauch, amtlich anerkannte Ausbildungsstätte."',
     'content="Повышение квалификации профессиональных водителей по BKrFQG в Ларе: модули 1–5 для кода 95 в автошколе Strauch, официально признанном учебном центре."'),
    ('<meta property="og:title" content="BKF-Weiterbildung in Lahr" />', '<meta property="og:title" content="Повышение квалификации профводителей в Ларе" />'),
    ('<meta property="og:description" content="Module 1 bis 5 für die Schlüsselzahl 95. Amtlich anerkannte Ausbildungsstätte." />',
     '<meta property="og:description" content="Модули 1–5 для кода 95. Официально признанный учебный центр." />'),
    ('</span>Berufskraftfahrer · Fahrschule Strauch</span>', '</span>Профводители · автошкола Strauch</span>'),
    ('BKF-Weiterbildung <span class="ac">in Lahr.</span>', 'Профводители: <span class="ac">обучение в Ларе.</span>'),
    ('Amtlich anerkannte Ausbildungsstätte für die Weiterbildung nach dem Berufskraftfahrerqualifikationsgesetz, Schlüsselzahl 95.',
     'Официально признанный учебный центр для повышения квалификации по закону о квалификации профессиональных водителей (BKrFQG), код 95.'),
    ('<b>1 bis 5</b><span>Module</span>', '<b>1–5</b><span>модули</span>'),
    ('<b>95</b><span>Schlüsselzahl</span>', '<b>95</b><span>код</span>'),
    ('<b>BKrFQG</b><span>Grundlage</span>', '<b>BKrFQG</b><span>основа</span>'),
    ANRUFEN,
    MAIL,
    ('alt="Lkw mit dem Logo der Fahrschule Strauch auf der Autobahn bei Abendlicht (KI-Symbolbild)"', 'alt="Грузовик с логотипом автошколы Strauch на автобане вечером (символическое изображение, создано ИИ)"'),
    ('</svg>Amtlich anerkannt</span>', '</svg>Официально признано</span>'),
    ('</span>Die Module</span>', '</span>Модули</span>'),
    ('Fünf Module, <b>eine Schlüsselzahl.</b>', 'Пять модулей, <b>один код.</b>'),
    ('Wir bieten wieder unsere altbewährten Weiterbildungen für Berufskraftfahrer an. Termine und Anmeldung telefonisch oder per E-Mail.',
     'Мы снова проводим проверенное временем повышение квалификации для профессиональных водителей. Даты и запись по телефону или по электронной почте. Занятия проходят на немецком языке.'),
    *[(f'<span class="mini">Modul {i}</span>', f'<span class="mini">Модуль {i}</span>') for i in (1, 3, 5)],
    *[(f'<span class="tag">Modul {i}</span>', f'<span class="tag">Модуль {i}</span>') for i in (2, 4)],
    ('Eco-Training und Assistenzsysteme</h3>', 'Эко-тренинг и системы помощи водителю</h3>'),
    ('<li>Eigenschaften der kinematischen Kette für eine optimierte Nutzung</li>', '<li>Особенности трансмиссии для оптимального использования</li>'),
    ('<li>Technische Merkmale und Funktionsweise der Sicherheitsausstattung</li>', '<li>Технические характеристики и работа систем безопасности</li>'),
    ('<li>Kraftstoffverbrauch optimieren</li>', '<li>Оптимизация расхода топлива</li>'),
    ('Sozialvorschriften und Fahrtenschreiber</h3>', 'Социальные нормы и тахограф</h3>'),
    ('<li>Sozialrechtliche Rahmenbedingungen und Vorschriften für Güterkraft- und Personenverkehr</li>', '<li>Социально-правовые условия и правила грузовых и пассажирских перевозок</li>'),
    ('<li>Vorschriften für den Güterkraftverkehr</li>', '<li>Правила грузовых перевозок</li>'),
    ('<li>Vorschriften für den Personenverkehr</li>', '<li>Правила пассажирских перевозок</li>'),
    ('Gefahrenwahrnehmung</h3>', 'Восприятие опасности</h3>'),
    ('<li>Sicherheit und Komfort der Fahrgäste gewährleisten</li>', '<li>Безопасность и комфорт пассажиров</li>'),
    ('<li>Bewusstsein für Risiken des Straßenverkehrs und Arbeitsunfälle</li>', '<li>Понимание рисков на дороге и несчастных случаев на работе</li>'),
    ('<li>Lage bei Notfällen richtig einschätzen</li>', '<li>Правильная оценка ситуации при чрезвычайных происшествиях</li>'),
    ('Schadensprävention</h3>', 'Предотвращение ущерба</h3>'),
    ('<li>Sicherheit der Ladung gewährleisten</li>', '<li>Безопасность груза</li>'),
    ('<li>Gesundheitsschäden vorbeugen</li>', '<li>Профилактика вреда здоровью</li>'),
    ('<li>Verhalten, das zu einem positiven Bild des Unternehmens beiträgt</li>', '<li>Поведение, которое создаёт положительный образ компании</li>'),
    ('Sicherheit für Ladung und Fahrgast</h3>', 'Безопасность груза и пассажиров</h3>'),
    ('<li>Ladungssicherung nach den Sicherheitsvorschriften und richtige Benutzung des KOM</li>', '<li>Крепление груза по правилам безопасности и правильное использование автобуса</li>'),
    ('<span class="visually-hidden">Nächstes Modul</span>', '<span class="visually-hidden">Следующий модуль</span>'),
    ('Termin anfragen <svg', 'Узнать даты <svg'),
    ('Weiterbildung nach dem Berufskraftfahrerqualifikationsgesetz (BKrFQG).', 'Повышение квалификации по закону о квалификации профессиональных водителей (BKrFQG).'),
    ('<span class="eyebrow">Ansprechpartner Viktor Strauch</span>', '<span class="eyebrow">Контактное лицо Viktor Strauch</span>'),
    ('Rufen Sie uns an, wir beraten Sie gern.</h2>', 'Позвоните нам, мы с радостью проконсультируем.</h2>'),
    ('<p class="pz__sub">Schwarzwaldstraße 93, 77933 Lahr.</p>', '<p class="pz__sub" lang="de">Schwarzwaldstraße 93, 77933 Lahr.</p>'),
    ('<h3 class="pz__st">Anrufen oder schreiben</h3>', '<h3 class="pz__st">Позвонить или написать</h3>'),
    ('Telefonisch unter +49 155 60 41 04 13 oder per E-Mail an service@fahrschule-strauch.de.', 'По телефону +49 155 60 41 04 13 или по почте service@fahrschule-strauch.de.'),
    ('<h3 class="pz__st">Termin abstimmen</h3>', '<h3 class="pz__st">Согласовать дату</h3>'),
    ('Wir nennen Ihnen die nächsten Termine für die Module.', 'Мы сообщим ближайшие даты модулей.'),
    ('<span class="pz__pill">Module 1 bis 5</span>', '<span class="pz__pill">Модули 1–5</span>'),
    ('<h3 class="pz__st">Weiterbildung besuchen</h3>', '<h3 class="pz__st">Пройти обучение</h3>'),
    ('Bei uns in der Fahrschule, amtlich anerkannte Ausbildungsstätte.', 'У нас в автошколе, официально признанном учебном центре.'),
    ('<span class="pz__pill">Schlüsselzahl 95</span>', '<span class="pz__pill">Код 95</span>'),
]

UEBER = [
    ('<title>Über uns: Team und Fahrlehrer | Fahrschule Strauch Lahr</title>', '<title>О нас: команда и инструкторы | Автошкола Strauch, Лар</title>'),
    ('content="Das Team der Fahrschule Viktor Strauch in Lahr: Fahrlehrer seit 1984, 1988, 2000 und 2007. Bei uns dürfen Fehler passieren und Fragen sind erwünscht."',
     'content="Команда автошколы Viktor Strauch в Ларе: инструкторы с 1984, 1988, 2000 и 2007 года. Здесь можно ошибаться и задавать вопросы."'),
    ('<meta property="og:title" content="Über uns: das Team der Fahrschule Strauch" />', '<meta property="og:title" content="О нас: команда автошколы Strauch" />'),
    ('<meta property="og:description" content="Fahrlehrer seit 1984, 1988, 2000 und 2007 in Lahr." />', '<meta property="og:description" content="Инструкторы с 1984, 1988, 2000 и 2007 года, Лар." />'),
    ('</span>Über die Fahrschule Strauch in Lahr</span>', '</span>Об автошколе Strauch в Ларе</span>'),
    ('In guten Händen, <span class="ac">vom ersten Meter an.</span>', 'В надёжных руках <span class="ac">с первого метра.</span>'),
    ('Willkommen in der Fahrschule Viktor Strauch. Hier wird dein Weg zum Führerschein eine Reise, die sich lohnt.',
     'Добро пожаловать в автошколу Viktor Strauch. Здесь путь к правам становится поездкой, которая того стоит.'),
    ('<b>1984</b><span>Fahrlehrer seit</span>', '<b>1984</b><span>инструкторы с</span>'),
    ('<b>4</b><span>Fahrlehrer</span>', '<b>4</b><span>инструктора</span>'),
    ('<b>DE · RU</b><span>Beratung</span>', '<b>DE · RU</b><span>консультации</span>'),
    ('alt="Inhaber Viktor Strauch lehnt an einem Fahrschulauto"', 'alt="Владелец Viktor Strauch у учебного автомобиля"'),
    ('</svg>Inhaber Viktor Strauch</span>', '</svg>Владелец Viktor Strauch</span>'),
    ('<span class="tag">Haltung</span>', '<span class="tag">Подход</span>'),
    ('Fehler passieren.</h2>', 'Ошибки случаются.</h2>'),
    ('Wir ermutigen dich, aus ihnen zu lernen, ohne Angst davor zu haben. Du sollst dich bei uns wohlfühlen und jede Frage stellen können.',
     'Мы поддерживаем вас, чтобы вы учились на них без страха. У нас вам должно быть комфортно, и любой вопрос можно задать.'),
    ('<li>Fragen sind erwünscht</li><li>Keine Angst vor Fehlern</li>', '<li>Вопросы приветствуются</li><li>Без страха ошибок</li>'),
    ('<span class="mini">Unterricht</span>', '<span class="mini">Занятия</span>'),
    ('Verstehen statt auswendig lernen.</h2>', 'Понимать, а не зубрить.</h2>'),
    ('Unser Unterricht setzt auf moderne Lehrmethoden, interaktive Stunden und praktische Übungen, damit du das Verkehrsgeschehen wirklich verstehst.',
     'Наши занятия строятся на современных методах, интерактивных уроках и практических упражнениях, чтобы вы действительно понимали дорожную обстановку.'),
    ('<li>Theorie</li><li>Fahrstunde</li><li>Bei jedem Schritt dabei</li>', '<li>Теория</li><li>Урок вождения</li><li>Рядом на каждом шаге</li>'),
    ('alt="Das Team der Fahrschule Strauch mit vier Fahrschulautos vor dem Gebäude"', 'alt="Команда автошколы Strauch с четырьмя учебными автомобилями перед зданием"'),
    ('<span class="kicker">Fahrlehrer seit</span>', '<span class="kicker">Инструкторы с</span>'),
    ('<span class="tag">Ziel</span>', '<span class="tag">Цель</span>'),
    ('Mehr als die Prüfung.</h2>', 'Больше, чем экзамен.</h2>'),
    ('Unser Ziel ist nicht nur, dass du die Prüfung bestehst, sondern dass du ein verantwortungsbewusster und sicherer Fahrer wirst.',
     'Наша цель не только в том, чтобы вы сдали экзамен, но и в том, чтобы вы стали ответственным и уверенным водителем.'),
    ('<li>Sicher und selbstbewusst</li><li>Beratung auch auf Russisch</li>', '<li>Уверенно и спокойно</li><li>Консультации на русском</li>'),
    WEITER,
    ANMELDEN,
    ('</span>Das Team</span>', '</span>Команда</span>'),
    ('Wer neben dir <b>sitzt.</b>', 'Кто сидит <b>рядом с вами.</b>'),
    ('Unsere Fahrlehrer lieben ihren Job und bringen dir alles bei, was du brauchst, um sicher und selbstbewusst hinter dem Steuer zu sitzen.',
     'Наши инструкторы любят свою работу и научат всему, что нужно, чтобы уверенно и спокойно сидеть за рулём.'),
    ALT_VIKTOR, ALT_PETER, ALT_GEROLD, ALT_NADINE,
    ('Inhaber, Fahrlehrer seit 2007', 'Владелец, инструктор с 2007 года'),
    ('Fahrlehrer aller Klassen seit 1984', 'Инструктор по всем категориям с 1984 года'),
    ('Fahrlehrer aller Klassen seit 1988. Das Hobby zum Beruf gemacht.', 'Инструктор по всем категориям с 1988 года. Хобби стало профессией.'),
    ('Fahrlehrerin seit 2000', 'Инструктор с 2000 года'),
    QUOTE_VIKTOR, QUOTE_PETER, QUOTE_GEROLD, QUOTE_NADINE,
    ('<span class="eyebrow">Jobs</span>', '<span class="eyebrow">Вакансии</span>'),
    ('Fahrlehrer (m/w/d) gesucht.</h2>', 'Ищем инструкторов (м/ж/д).</h2>'),
    ('Unser Team braucht Verstärkung. Wenn du Fahrlehrerin oder Fahrlehrer bist und zu uns passen möchtest, melde dich.',
     'Нашей команде нужно пополнение. Если вы инструктор по вождению и хотите работать с нами, свяжитесь с нами.'),
    ANRUFEN,
    ('>Bewerbung per E-Mail</a>', '>Отклик по электронной почте</a>'),
]

ANMELDUNG = [
    ('<title>Anmeldung und Kontakt | Fahrschule Strauch Lahr</title>', '<title>Запись и контакты | Автошкола Strauch, Лар</title>'),
    ('content="Bei der Fahrschule Strauch in Lahr anmelden: online, mit dem Anmeldeformular oder persönlich. Formulare, Finanzierung und Kontakt auf einen Blick."',
     'content="Запись в автошколу Strauch в Ларе: онлайн, по бланку или лично. Бланки, финансирование и контакты. Говорим по-русски."'),
    ('<meta property="og:title" content="Anmeldung bei der Fahrschule Strauch" />', '<meta property="og:title" content="Запись в автошколу Strauch" />'),
    ('<meta property="og:description" content="Online anmelden, Formulare herunterladen, Kontakt und Anfahrt." />',
     '<meta property="og:description" content="Записаться онлайн, скачать бланки, контакты и как добраться." />'),
    ('</span>Anmeldung bei der Fahrschule Strauch</span>', '</span>Запись в автошколу Strauch</span>'),
    ('Anmelden <span class="ac">und losfahren.</span>', 'Записаться <span class="ac">и поехать.</span>'),
    ('Online, mit dem Formular oder persönlich bei uns in der Schwarzwaldstraße&nbsp;93.',
     'Онлайн, с помощью бланка или лично у нас на <span lang="de">Schwarzwaldstraße&nbsp;93</span>.'),
    ('<b>Online</b><span>Fahrschulmanager</span>', '<b>Онлайн</b><span>Fahrschulmanager</span>'),
    ('<b>PDF</b><span>Anmeldeformular</span>', '<b>PDF</b><span>бланк записи</span>'),
    ('<b>Vor Ort</b><span>Schwarzwaldstr. 93</span>', '<b>Лично</b><span lang="de">Schwarzwaldstr. 93</span>'),
    ('type="submit">Online anmelden <svg', 'type="submit">Записаться онлайн <svg'),
    ('</svg>Anmeldeformular</a>', '</svg>Бланк записи</a>'),
    ('Die Online-Anmeldung öffnet den Fahrschulmanager in einem neuen Tab.', 'Онлайн-запись откроет Fahrschulmanager в новой вкладке. Форма на немецком языке.'),
    ('alt="Fahrlehrer Gerold Remmele neben einem Fahrschulauto vor der Fahrschule"', 'alt="Инструктор Gerold Remmele рядом с учебным автомобилем перед автошколой"'),
    ('</svg>Auch persönlich vor Ort</span>', '</svg>Можно и лично</span>'),
    ('</span>Formulare</span>', '</span>Бланки</span>'),
    ('Formulare <b>zum Herunterladen.</b>', 'Бланки <b>для скачивания.</b>'),
    ('Lieber auf Papier? Anmeldeformular ausdrucken, ausfüllen und vorbeibringen.',
     'Удобнее на бумаге? Распечатайте бланк записи, заполните и принесите нам. Бланки на немецком языке.'),
    *PDF_KB,
    ('<h3 class="qa__title">Anmeldeformular</h3>', '<h3 class="qa__title">Бланк записи</h3>'),
    ('Für die Anmeldung auf Papier.', 'Для записи на бумаге.'),
    ('<h3 class="qa__title">Führerscheinantrag</h3>', '<h3 class="qa__title">Заявление на получение прав</h3>'),
    ('Den Antrag bekommst du auch bei uns als Formular.', 'Бланк заявления можно получить и у нас.'),
    ('<h3 class="qa__title">Info und Preise Klasse B</h3>', '<h3 class="qa__title">Информация и цены, категория B</h3>'),
    ('<h3 class="qa__title">Info und Preise Klasse BE</h3>', '<h3 class="qa__title">Информация и цены, категория BE</h3>'),
    ('Grundbetrag, Fahrstunden und Prüfungsvorstellungen.', 'Базовая стоимость, уроки вождения и экзамены.'),
    ('<h3 class="qa__title">Antrag Begleitetes Fahren ab 17</h3>', '<h3 class="qa__title">Заявление на вождение с 17 лет</h3>'),
    ('Für BF17, ab 16½ Jahren.', 'Для BF17, с 16½ лет.'),
    ('<h3 class="qa__title">BF17: Erklärung der Begleitperson</h3>', '<h3 class="qa__title">BF17: заявление сопровождающего</h3>'),
    ('Für jede Begleitperson ein eigenes Formular.', 'Отдельный бланк на каждого сопровождающего.'),
    ('<h3 class="qa__title">Vordruck Kartenführerschein</h3>', '<h3 class="qa__title">Бланк для пластиковых прав</h3>'),
    ('Der Vordruck für deinen Kartenführerschein.', 'Бланк для ваших прав в формате карты.'),
    ('<span class="visually-hidden">Weitere Formulare</span>', '<span class="visually-hidden">Другие бланки</span>'),
    ('aria-label="App und Finanzierung"', 'aria-label="Приложение и финансирование"'),
    ('<h2 class="bt">App Fahren Lernen MAX</h2>', '<h2 class="bt">Приложение Fahren Lernen MAX</h2>'),
    ('Mit interaktiven Lektionen und Übungen lernst du die Theorie, wann und wo du willst: auf dem Sofa oder unterwegs in der Bahn. Du siehst deinen Lernfortschritt und übst gezielt dort, wo du noch unsicher bist.',
     'С интерактивными уроками и упражнениями вы учите теорию, когда и где удобно: дома на диване или в электричке. Вы видите свой прогресс и целенаправленно тренируете то, в чём ещё не уверены.'),
    ('<h2 class="bt">Finanzierung mit STARTHILFE</h2>', '<h2 class="bt">Финансирование с STARTHILFE</h2>'),
    ('STARTHILFE wurde speziell für Fahrschüler entwickelt, vom Verlag Heinrich Vogel und der Credit Europe Bank N.V. in Frankfurt am Main.',
     'STARTHILFE разработано специально для учеников автошкол издательством Heinrich Vogel и Credit Europe Bank N.V. во Франкфурте-на-Майне.'),
    ('Mehr zu STARTHILFE <svg', 'Подробнее о STARTHILFE (на немецком) <svg'),
]

TABLE = {'': START, 'fuehrerschein': FUEHRERSCHEIN, 'berufskraftfahrer': BKF, 'ueber-uns': UEBER, 'anmeldung': ANMELDUNG}

# Deutsche Wörter, die im sichtbaren Text der russischen Seiten nicht mehr vorkommen dürfen
LEFTOVER = re.compile(r'\b(und|oder|der|die|das|mit|für|Klasse|Fahrlehrer|Anmelden|Jetzt|Weiter|Unterlagen|Führerschein)\b')


def visible_text(html):
    html = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', html)
    html = re.sub(r'<!--[\s\S]*?-->', ' ', html)
    html = re.sub(r'<[^>]*\blang="de"[^>]*>[^<]*<', '<', html)  # bewusst deutsche Stellen
    return re.sub(r'<[^>]+>', ' ', html)


def main():
    for page in PAGES:
        src = os.path.join(ROOT, page, 'index.html')
        text = open(src, encoding='utf-8').read()
        text = replace_all(text, TABLE[page], page)
        text = common(text, page)
        body = visible_text(text.split('<body>', 1)[1])
        left = sorted(set(LEFTOVER.findall(body)))
        if left:
            sys.exit(f'[{page or "start"}] deutsche Wörter übrig: {left}')
        out_dir = os.path.join(ROOT, 'ru', page)
        os.makedirs(out_dir, exist_ok=True)
        head, rest = text.split('\n', 1)
        text = head + '\n<!-- Automatisch erzeugt aus der deutschen Seite: python3 scripts/translate_ru.py -->\n' + rest
        open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(text)
        print('✓ ru/' + (page + '/' if page else ''))


if __name__ == '__main__':
    main()
