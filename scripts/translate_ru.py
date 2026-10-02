#!/usr/bin/env python3
"""Erzeugt die russischen Seiten unter ru/ aus den deutschen Seiten.

Jede deutsche Textstelle wird gezielt ersetzt. Fehlt eine Stelle (weil der
deutsche Text geändert wurde), bricht das Skript mit einer Meldung ab, damit
keine Seite halb übersetzt veröffentlicht wird.

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
    text = text.replace('<!-- @include head locale="de_DE" -->', '<!-- @include head locale="ru_RU" -->')
    text = re.sub(r'<!-- @include header page="([\w-]+)" de="[^"]*" ru="[^"]*" -->',
                  lambda m: f'<!-- @include header-ru page="{m.group(1)}" de="{de_url}" ru="{ru_url}" -->', text)
    for part in ('footer', 'contact', 'finale'):
        text = text.replace(f'<!-- @include {part} -->', f'<!-- @include {part}-ru -->')
    # interne Links auf die russischen Seiten umbiegen (Dateien, Bilder, Rechtstexte bleiben)
    text = re.sub(r'href="/(fuehrerschein|ueber-uns|anmeldung|berufskraftfahrer)/', r'href="/ru/\1/', text)
    text = text.replace('href="/#', 'href="/ru/#')
    text = text.replace('<li><a href="/">Start</a></li>', '<li><a href="/ru/">Главная</a></li>')
    # Canonical und hreflang
    text = text.replace(f'<link rel="canonical" href="{BASE}{de_url}" />',
                        f'<link rel="canonical" href="{BASE}{ru_url}" />\n'
                        f'    <link rel="alternate" hreflang="de" href="{BASE}{de_url}" />\n'
                        f'    <link rel="alternate" hreflang="ru" href="{BASE}{ru_url}" />')
    text = text.replace(f'<meta property="og:url" content="{BASE}{de_url}" />',
                        f'<meta property="og:url" content="{BASE}{ru_url}" />')
    # doppelte hreflang-Zeilen der Startseite entfernen
    text = re.sub(r'(\s*<link rel="alternate" hreflang="(de|ru)" href="[^"]+" />)(?=[\s\S]*\1)', '', text)
    return text


# --------------------------------------------------------------------------
# Gemeinsame Bausteine in mehreren Seiten
ROLL_ANMELDEN = ('<span class="btn__label"><span>Jetzt anmelden</span><span aria-hidden="true">Jetzt anmelden</span></span>',
                 '<span class="btn__label"><span>Записаться</span><span aria-hidden="true">Записаться</span></span>')
ANRUFEN = ('</svg>Anrufen</a>', '</svg>Позвонить</a>')
MAIL = ('</svg>E-Mail schreiben</a>', '</svg>Написать письмо</a>')

QUOTES = [
    ('„Der Weg ist das Ziel, viel Spaß auf deinen neuen Wegen.“', '«Путь и есть цель. Удачи на новых дорогах!»'),
    ('„Ein Stop-Schild ist keine Empfehlung.“', '«Знак „Стоп“ не рекомендация.»'),
    ('„Und immer noch Spaß daran, Jugendliche sicher auf die Straße zu bringen.“', '«И мне до сих пор нравится помогать молодым людям безопасно выезжать на дорогу.»'),
    ('„Fährst du rückwärts gegen Baum, verkleinert sich dein Kofferraum!“', '«Сдашь назад в дерево, и багажник станет меньше!»'),
]
ROLES = [
    ('Fahrlehrer aller Klassen seit 1984', 'Инструктор по всем категориям с 1984 года'),
    ('Fahrlehrer aller Klassen seit 1988', 'Инструктор по всем категориям с 1988 года'),
    ('Fahrlehrerin seit 2000', 'Инструктор с 2000 года'),
    ('Inhaber, Fahrlehrer seit 2007', 'Владелец, инструктор с 2007 года'),
]
ALTS = [
    ('Peter Harter an der geöffneten Fahrertür eines Fahrschulautos', 'Peter Harter у открытой водительской двери учебного автомобиля'),
    ('Gerold Remmele neben einem Fahrschulauto vor der Fahrschule', 'Gerold Remmele рядом с учебным автомобилем перед автошколой'),
    ('Nadine Dürr an der geöffneten Fahrertür eines Fahrschulautos', 'Nadine Dürr у открытой водительской двери учебного автомобиля'),
    ('Viktor Strauch lehnt an einem Fahrschulauto', 'Viktor Strauch у учебного автомобиля'),
]

# --------------------------------------------------------------------------
START = [
    ('<title>Fahrschule Strauch in Lahr | Führerschein Klasse B, BE, BF17 und B197</title>',
     '<title>Автошкола Strauch в Ларе | Права категорий B, BE, BF17 и B197</title>'),
    ('content="Fahrschule Viktor Strauch in Lahr, Schwarzwaldstraße 93: Führerschein Klasse B und BE, Begleitetes Fahren ab 17, Automatik mit Schaltberechtigung (B197), Auffrischung und BKF-Weiterbildung."',
     'content="Автошкола Viktor Strauch в Ларе (Lahr), Schwarzwaldstraße 93: права категорий B и BE, вождение с сопровождением с 17 лет, автомат с правом вождения механики (B197), восстановление навыков и повышение квалификации профводителей. Говорим по-русски."'),
    ('<meta property="og:title" content="Fahrschule Strauch: Führerschein in Lahr" />',
     '<meta property="og:title" content="Автошкола Strauch: права в Ларе" />'),
    ('<meta property="og:description" content="Klasse B und BE, Begleitetes Fahren ab 17 und B197. Schwarzwaldstraße 93, Lahr." />',
     '<meta property="og:description" content="Категории B и BE, вождение с 17 лет и B197. Schwarzwaldstraße 93, Лар. Говорим по-русски." />'),
    ('"url": "https://www.fahrschule-strauch.de/",', '"url": "https://www.fahrschule-strauch.de/ru/",'),
    # Hero
    ('<span class="hero__line">Führerschein</span>', '<span class="hero__line">Права</span>'),
    ('<span class="hero__line accent">in Lahr.</span>', '<span class="hero__line accent">в Ларе.</span>'),
    ('Fahrschule Viktor Strauch: Klasse B und BE, Begleitetes Fahren ab 17 und Automatik mit Schaltberechtigung.',
     'Автошкола Viktor Strauch: категории B и BE, вождение с сопровождением с 17 лет и автомат с правом вождения механики.'),
    ROLL_ANMELDEN,
    ('<a class="btn btn--secondary" href="#klassen">Klassen ansehen</a>', '<a class="btn btn--secondary" href="#klassen">Категории</a>'),
    ('alt="Illustration: die Fahrschule Strauch mit Logo über dem Schaufenster, drei Fahrschulautos mit Logo, ein Fahrlehrer und ein Fahrschüler mit Autoschlüssel"',
     'alt="Иллюстрация: автошкола Strauch с логотипом над витриной, три учебных автомобиля с логотипом, инструктор и ученик с ключом от машины"'),
    ('Klasse B und BE anzeigen', 'Показать: категории B и BE'),
    ('>Klasse B und BE<svg', '>Категории B и BE<svg'),
    ('Automatik oder Schaltung anzeigen', 'Показать: автомат или механика'),
    ('>Automatik + Schaltung<svg', '>Автомат + механика<svg'),
    ('Fahrlehrer seit 1984 anzeigen', 'Показать: инструкторы с 1984 года'),
    ('>Seit 1984<svg', '>С 1984 года<svg'),
    ('Schwarzwaldstraße 93 anzeigen', 'Показать: Schwarzwaldstraße 93'),
    ('data-spot-pick="0">Klasse B und BE</button>', 'data-spot-pick="0">Категории B и BE</button>'),
    ('Pkw bis 3,5 t und größere Anhänger. Mit Begleitetem Fahren schon ab 17.',
     'Легковые автомобили до 3,5 т и прицепы побольше. С сопровождением уже с 17 лет.'),
    ('Klassen ansehen <svg', 'Все категории <svg'),
    ('data-spot-pick="1">Automatik oder Schaltung</button>', 'data-spot-pick="1">Автомат или механика</button>'),
    ('Mit B197 beides: Prüfung im Automatikauto, danach auch Schaltwagen fahren.',
     'С B197 и то и другое: экзамен на автомате, а потом можно водить и механику.'),
    ('So geht B197 <svg', 'Как работает B197 <svg'),
    ('data-spot-pick="2">Fahrlehrer seit 1984</button>', 'data-spot-pick="2">Инструкторы с 1984 года</button>'),
    ('Peter Harter, Gerold Remmele, Nadine Dürr und Viktor Strauch.', 'Peter Harter, Gerold Remmele, Nadine Dürr и Viktor Strauch.'),
    ('Das Team <svg', 'Команда <svg'),
    ('Theorie montags 19:00 bis 20:30 Uhr. Wir beraten auf Deutsch und Russisch.',
     'Теория по понедельникам с 19:00 до 20:30. Консультируем на русском и немецком.'),
    ('href="#kontakt">Kontakt <svg', 'href="#kontakt">Контакты <svg'),
    # Intro
    ('Bei uns darfst du <span class="accent">Fehler machen.</span>', 'У нас можно <span class="accent">ошибаться.</span>'),
    ('alt="Fahrlehrer Gerold Remmele vor dem Schaufenster der Fahrschule mit dem Logo"',
     'alt="Инструктор Gerold Remmele у витрины автошколы с логотипом"'),
    ('Fragen sind erwünscht, und niemand muss Angst vor einem Fehler haben. Unser Ziel ist nicht nur die bestandene Prüfung, sondern dass du danach sicher und selbstbewusst fährst.',
     'Вопросы приветствуются, и никто не должен бояться ошибок. Наша цель не только сданный экзамен, но и то, чтобы потом вы ездили уверенно и безопасно.'),
    ('<p class="intro__ru"><span lang="ru">Говорим по-русски.</span> Wir beraten dich auch auf Russisch.</p>',
     '<p class="intro__ru"><span>Говорим по-русски.</span> Консультации на русском и немецком языке.</p>'),
    ('Mehr über uns', 'Подробнее о нас'),
    ('alt="Inhaber Viktor Strauch lehnt an seinem Fahrschulauto"', 'alt="Владелец Viktor Strauch у своего учебного автомобиля"'),
    # Klassen
    ('Welche Klasse <span class="accent">passt zu dir?</span>', 'Какая категория <span class="accent">вам подходит?</span>'),
    ('id="cls-b">Klasse B</h3>', 'id="cls-b">Категория B</h3>'),
    ('Pkw und leichte Lkw bis 3,5 t. Ab 18 Jahren, mit Begleitetem Fahren ab 17. Anhänger bis 750 kg sind inklusive.',
     'Легковые автомобили и лёгкие грузовики до 3,5 т. С 18 лет, с сопровождением с 17. Прицеп до 750 кг включён.'),
    ('Alles zu Klasse B <svg', 'Всё о категории B <svg'),
    ('id="cls-be">Klasse BE</h3>', 'id="cls-be">Категория BE</h3>'),
    ('Für größere Anhänger hinter dem Pkw. Voraussetzung ist Klasse B.', 'Для прицепов побольше за легковым автомобилем. Нужна категория B.'),
    ('Alles zu Klasse BE <svg', 'Всё о категории BE <svg'),
    ('Automatik oder Schaltung? <span class="class-tile__em">Beides.</span>', 'Автомат или механика? <span class="class-tile__em">И то и другое.</span>'),
    ('Mit B197 machst du die Prüfung im Automatikauto und darfst danach ohne Einschränkung auch Schaltwagen fahren.',
     'С B197 вы сдаёте экзамен на автомате, а потом без ограничений можете водить и механику.'),
    ('So funktioniert B197 <svg', 'Как работает B197 <svg'),
    ('id="cls-bf17">Begleitetes Fahren ab 17</h3>', 'id="cls-bf17">Вождение с 17 лет</h3>'),
    ('Antrag ab 16½, Prüfung kurz vor dem 17. Geburtstag. Danach fährst du mit einer eingetragenen Begleitperson.',
     'Заявление с 16,5 лет, экзамен незадолго до 17-летия. Затем вы ездите с сопровождающим, вписанным в документ.'),
    ('Unterlagen für BF17 <svg', 'Документы для BF17 <svg'),
    ('Außerdem: <a href="/fuehrerschein/#schnellkurs">Schnellkurse</a>, <a href="/fuehrerschein/#auffrischung">Auffrischungsstunden</a> und <a href="/berufskraftfahrer/">BKF-Weiterbildung</a>.',
     'А также: <a href="/fuehrerschein/#schnellkurs">интенсивные курсы</a>, <a href="/fuehrerschein/#auffrischung">занятия для восстановления навыков</a> и <a href="/berufskraftfahrer/">повышение квалификации профводителей</a>.'),
    # Ablauf
    ('So läuft deine <span class="accent">Ausbildung.</span>', 'Как проходит <span class="accent">обучение.</span>'),
    ('Von der Anmeldung bis zum Führerschein in sechs Etappen.', 'От записи до прав за шесть этапов.'),
    ('<h3 class="step__title">Anmelden</h3>', '<h3 class="step__title">Запись</h3>'),
    ('Online über den Fahrschulmanager, mit dem Anmeldeformular oder direkt bei uns in der Schwarzwaldstraße&nbsp;93.',
     'Онлайн через Fahrschulmanager, с помощью бланка или прямо у нас на Schwarzwaldstraße&nbsp;93.'),
    ('Zur Anmeldung <svg', 'К записи <svg'),
    ('<h3 class="step__title">Unterlagen</h3>', '<h3 class="step__title">Документы</h3>'),
    ('Sehtest, Erste-Hilfe-Kurs, biometrisches Passfoto und Ausweis. Den Führerscheinantrag bekommst du bei uns als Formular.',
     'Проверка зрения, курс первой помощи, биометрическое фото и удостоверение личности. Бланк заявления на права вы получите у нас.'),
    ('<h3 class="step__title">Theorie</h3>', '<h3 class="step__title">Теория</h3>'),
    ('Unterricht montags von 19:00 bis 20:30 Uhr, mittwochs nach Vereinbarung. Zwischendurch lernst du mit der App Fahren Lernen MAX.',
     'Занятия по понедельникам с 19:00 до 20:30, по средам по договорённости. В промежутках можно учиться в приложении Fahren Lernen MAX.'),
    ('<h3 class="step__title">Fahrstunden</h3>', '<h3 class="step__title">Уроки вождения</h3>'),
    ('Grundausbildung und die Sonderfahrten über Land, auf der Autobahn und bei Dunkelheit. Im Schalt- oder im Automatikwagen.',
     'Базовое обучение и обязательные специальные поездки: за городом, по автобану и в тёмное время суток. На механике или на автомате.'),
    ('<h3 class="step__title">Prüfung</h3>', '<h3 class="step__title">Экзамен</h3>'),
    ('Erst die Theorieprüfung, dann die praktische Prüfung. Wir melden dich an, wenn du so weit bist.',
     'Сначала теоретический экзамен, затем практический. Мы запишем вас, когда вы будете готовы.'),
    ('<h3 class="step__title">Führerschein</h3>', '<h3 class="step__title">Права</h3>'),
    ('Bestanden. Mit Begleitetem Fahren ab 17 fährst du zunächst mit Begleitung, sonst ab sofort allein.',
     'Сдано! При вождении с 17 лет сначала ездите с сопровождающим, в остальных случаях сразу самостоятельно.'),
    # Team
    *ALTS,
    ('Wer neben dir <span>sitzt.</span>', 'Кто сидит <span>рядом с вами.</span>'),
    ('aria-label="Fahrlehrer auswählen"', 'aria-label="Выбрать инструктора"'),
    QUOTES[0],
    ('data-quote="Der Weg ist das Ziel, viel Spaß auf deinen neuen Wegen."', 'data-quote="Путь и есть цель. Удачи на новых дорогах!"'),
    ('data-quote="Ein Stop-Schild ist keine Empfehlung."', 'data-quote="Знак „Стоп“ не рекомендация."'),
    ('data-quote="Und immer noch Spaß daran, Jugendliche sicher auf die Straße zu bringen."', 'data-quote="И мне до сих пор нравится помогать молодым людям безопасно выезжать на дорогу."'),
    ('data-quote="Fährst du rückwärts gegen Baum, verkleinert sich dein Kofferraum!"', 'data-quote="Сдашь назад в дерево, и багажник станет меньше!"'),
    *ROLES,
    ('Peter Harter zeigen', 'Показать: Peter Harter'),
    ('Gerold Remmele zeigen', 'Показать: Gerold Remmele'),
    ('Nadine Dürr zeigen', 'Показать: Nadine Dürr'),
    ('Viktor Strauch zeigen', 'Показать: Viktor Strauch'),
    # Angebote
    ('Mehr als die <span class="accent">erste Fahrstunde.</span>', 'Больше, чем <span class="accent">первый урок.</span>'),
    ('<span class="offer__title">Theorie-Schnellkurs</span>', '<span class="offer__title">Интенсивный курс теории</span>'),
    ('Intensivkurs für alle mit wenig Zeit. Die nächsten Termine erfährst du bei uns.', 'Для тех, у кого мало времени. Ближайшие даты узнавайте у нас.'),
    ('<span class="offer__title">Auffrischung</span>', '<span class="offer__title">Восстановление навыков</span>'),
    ('Wieder sicher fahren: Einparken, Dunkelheit, schwierige Situationen, Angst am Steuer.',
     'Снова уверенно за рулём: парковка, темнота, сложные ситуации, страх вождения.'),
    ('<span class="offer__title">BKF-Weiterbildung</span>', '<span class="offer__title">Повышение квалификации BKF</span>'),
    ('Module 1 bis 5 für die Schlüsselzahl 95. Amtlich anerkannte Ausbildungsstätte.', 'Модули с 1 по 5 для кода 95. Официально признанный учебный центр.'),
    ('<span class="offer__title">Finanzierung</span>', '<span class="offer__title">Финансирование</span>'),
    ('STARTHILFE, die Führerscheinfinanzierung für Fahrschüler vom Verlag Heinrich Vogel und der Credit Europe Bank.',
     'STARTHILFE: финансирование обучения для учеников автошкол от издательства Heinrich Vogel и Credit Europe Bank.'),
    ('<span class="offer__title">App Fahren Lernen MAX</span>', '<span class="offer__title">Приложение Fahren Lernen MAX</span>'),
    ('Lernen, wann und wo du willst: auf dem Sofa oder unterwegs in der Bahn.', 'Учитесь, когда и где удобно: дома на диване или в электричке.'),
    # FAQ
    ('Häufige <span class="accent">Fragen.</span>', 'Частые <span class="accent">вопросы.</span>'),
    ('Ab wann kann ich mit dem Führerschein anfangen?', 'С какого возраста можно начинать?'),
    ('Für Klasse B bist du mit 18 dabei. Mit Begleitetem Fahren ab 17 kannst du den Antrag schon ab 16½ Jahren stellen, mit Einwilligung deiner Erziehungsberechtigten. So kannst du pünktlich zum 17. Geburtstag fertig sein.',
     'Для категории B нужно 18 лет. При вождении с сопровождением заявление можно подать уже с 16,5 лет с согласия родителей. Так вы успеете получить права к 17-летию.'),
    ('Welche Unterlagen brauche ich?', 'Какие документы нужны?'),
    ('Personalausweis oder Pass, ein biometrisches Passfoto, eine Sehtestbescheinigung (nicht älter als zwei Jahre) und den Nachweis über die Erste-Hilfe-Schulung. Für BF17 kommt für jede Begleitperson ein eigenes Formular dazu.',
     'Удостоверение личности или паспорт, биометрическое фото, справка о проверке зрения (не старше двух лет) и подтверждение курса первой помощи. Для BF17 на каждого сопровождающего нужен отдельный бланк.'),
    ('Alle Formulare zum Herunterladen', 'Все бланки для скачивания'),
    ('Automatik oder Schaltung, was ist besser?', 'Автомат или механика: что лучше?'),
    ('Mit der Schlüsselzahl B197 musst du dich nicht entscheiden: Du lernst einen Großteil im Automatikauto und machst dort auch die Prüfung. Nach mindestens zehn Übungsstunden im Schaltwagen und einer Testfahrt von mindestens 15 Minuten darfst du später ohne Einschränkung auch Schaltwagen fahren.',
     'С кодом B197 выбирать не нужно: большую часть обучения вы проходите на автомате и там же сдаёте экзамен. После не менее десяти учебных часов на механике и контрольной поездки не менее 15 минут вы сможете без ограничений водить и механику.'),
    ('Was kostet der Führerschein?', 'Сколько стоят права?'),
    ('Die Kosten hängen davon ab, wie viele Fahrstunden du brauchst. Grundbetrag, Preise je Fahrstunde und Prüfungsvorstellungen findest du in unserer Preisinformation.',
     'Стоимость зависит от того, сколько уроков вождения вам понадобится. Базовый взнос, цены за урок и за допуск к экзаменам указаны в нашей информации о ценах (на немецком).'),
    ('Info und Preise Klasse B (PDF)', 'Информация и цены, категория B (PDF, нем.)'),
    ('Info und Preise Klasse BE (PDF)', 'Информация и цены, категория BE (PDF, нем.)'),
    ('Kann ich den Führerschein finanzieren?', 'Можно ли профинансировать обучение?'),
    ('Ja, mit STARTHILFE, einer Führerscheinfinanzierung, die der Verlag Heinrich Vogel und die Credit Europe Bank speziell für Fahrschüler entwickelt haben.',
     'Да, через STARTHILFE: финансирование, которое издательство Heinrich Vogel и Credit Europe Bank разработали специально для учеников автошкол.'),
    ('>Mehr zu STARTHILFE</a>', '>Подробнее о STARTHILFE (на немецком)</a>'),
    ('Gibt es einen Schnellkurs?', 'Есть ли интенсивный курс?'),
    ('Ja. Im Theorie-Schnellkurs lernst du die Theorie in wenigen, kompakten Tagen. Die nächsten Termine erfährst du telefonisch oder per E-Mail.',
     'Да. На интенсивном курсе теории вы пройдёте теорию за несколько насыщенных дней. Ближайшие даты узнавайте по телефону или по e-mail.'),
    ('Sprecht ihr Russisch?', 'На каком языке можно получить консультацию?'),
    ('<p>Ja, wir beraten dich auch auf Russisch. <span lang="ru">Говорим по-русски.</span></p>\n                <p><a href="/ru/" hreflang="ru">Информация на русском языке</a></p>',
     '<p>Мы консультируем на русском и немецком языке. Все вопросы можно обсудить с нами по-русски.</p>\n                <p><a href="/" hreflang="de" lang="de">Deutsche Version</a></p>'),
]

FUEHRERSCHEIN = [
    ('<title>Führerschein Klasse B, BE, B197 und BF17 in Lahr | Fahrschule Strauch</title>',
     '<title>Права категорий B, BE, B197 и BF17 в Ларе | Автошкола Strauch</title>'),
    ('content="Führerscheinklassen bei der Fahrschule Strauch in Lahr: Klasse B, BE, Automatik mit Schaltberechtigung (B197), Begleitetes Fahren ab 17, Theorie-Schnellkurs und Auffrischungsstunden."',
     'content="Категории прав в автошколе Strauch в Ларе: B, BE, автомат с правом вождения механики (B197), вождение с сопровождением с 17 лет, интенсивный курс теории и занятия для восстановления навыков."'),
    ('<meta property="og:title" content="Führerschein in Lahr: Klassen und Kurse" />', '<meta property="og:title" content="Права в Ларе: категории и курсы" />'),
    ('<meta property="og:description" content="Klasse B, BE, B197, BF17, Schnellkurs und Auffrischung bei der Fahrschule Strauch in Lahr." />',
     '<meta property="og:description" content="Категории B, BE, B197, BF17, интенсивный курс и восстановление навыков в автошколе Strauch в Ларе." />'),
    ('<li aria-current="page">Führerschein</li>', '<li aria-current="page">Права</li>'),
    ('Klassen und Kurse <span class="accent">im Überblick.</span>', 'Категории и курсы <span class="accent">в обзоре.</span>'),
    ('Wir bilden in den Klassen B und BE aus, auch mit Begleitetem Fahren ab 17 und mit Automatik und Schaltberechtigung. Dazu kommen Schnellkurse und Auffrischungsstunden.',
     'Мы обучаем по категориям B и BE, в том числе с вождением с 17 лет и на автомате с правом вождения механики. Кроме того, есть интенсивные курсы и занятия для восстановления навыков.'),
    ('aria-label="Auf dieser Seite"', 'aria-label="На этой странице"'),
    ('<li><a href="#klasse-b">Klasse B</a></li>', '<li><a href="#klasse-b">Категория B</a></li>'),
    ('<li><a href="#klasse-be">Klasse BE</a></li>', '<li><a href="#klasse-be">Категория BE</a></li>'),
    ('<li><a href="#bf17">Begleitetes Fahren ab 17</a></li>', '<li><a href="#bf17">Вождение с 17 лет</a></li>'),
    ('<li><a href="#schnellkurs">Schnellkurs</a></li>', '<li><a href="#schnellkurs">Интенсивный курс</a></li>'),
    ('<li><a href="#auffrischung">Auffrischung</a></li>', '<li><a href="#auffrischung">Восстановление навыков</a></li>'),
    # Klasse B
    ('<h2 class="h2" id="b-title">Klasse B</h2>', '<h2 class="h2" id="b-title">Категория B</h2>'),
    ('Der Führerschein für Pkw und leichte Lkw, der Klassiker für den Alltag.', 'Права на легковые автомобили и лёгкие грузовики, классика для повседневной жизни.'),
    ('<dt>Fahrzeuge</dt><dd>Kraftfahrzeuge bis 3.500 kg zulässige Gesamtmasse, für höchstens acht Personen außer dem Fahrer</dd>',
     '<dt>Транспортные средства</dt><dd>Автомобили с разрешённой максимальной массой до 3500 кг, не более восьми пассажиров помимо водителя</dd>'),
    ('<dt>Anhänger</dt><dd>bis 750 kg zulässige Gesamtmasse oder schwerer, solange die Kombination 3.500 kg nicht übersteigt</dd>',
     '<dt>Прицеп</dt><dd>до 750 кг разрешённой максимальной массы или тяжелее, если масса всего состава не превышает 3500 кг</dd>'),
    ('<dt>Mindestalter</dt><dd><strong>18</strong> <span class="muted">mit Begleitetem Fahren 17</span></dd>',
     '<dt>Минимальный возраст</dt><dd><strong>18</strong> <span class="muted">с сопровождением 17</span></dd>'),
    ('<dt>Vorbesitz</dt><dd>nicht erforderlich</dd>', '<dt>Предыдущая категория</dt><dd>не требуется</dd>'),
    ('<dt>Eingeschlossen</dt><dd>Klassen L und AM</dd>', '<dt>Включает</dt><dd>категории L и AM</dd>'),
    ROLL_ANMELDEN,
    ('</svg>Info und Preise (PDF)</a>', '</svg>Информация и цены (PDF, нем.)</a>'),
    # Klasse BE
    ('<h2 class="h2" id="be-title">Klasse BE</h2>', '<h2 class="h2" id="be-title">Категория BE</h2>'),
    ('Für Gespanne mit größerem Anhänger, die über die Grenzen der Klasse B hinausgehen.', 'Для составов с прицепом побольше, которые выходят за рамки категории B.'),
    ('<dt>Fahrzeuge</dt><dd>Kombinationen aus einem Fahrzeug der Klasse B und einem Anhänger, die die Grenzwerte der Klasse B oder B96 übersteigen</dd>',
     '<dt>Транспортные средства</dt><dd>Составы из автомобиля категории B и прицепа, превышающие пределы категории B или B96</dd>'),
    ('<dt>Vorbesitz</dt><dd>Klasse B</dd>', '<dt>Предыдущая категория</dt><dd>категория B</dd>'),
    # B197
    ('Automatik oder Schaltung? <span class="accent">Beides.</span>', 'Автомат или механика? <span class="accent">И то и другое.</span>'),
    ('Du machst die Prüfung im Automatikauto und darfst danach ohne Einschränkung auch Schaltwagen fahren. In der Theorie gibt es keinen Unterschied.',
     'Вы сдаёте экзамен на автомате, а потом без ограничений можете водить и механику. В теории разницы нет.'),
    ('<h3>Grundausbildung</h3><p>Zum Großteil im Automatikauto. Du kannst aber auch im Schaltwagen beginnen.</p>',
     '<h3>Базовое обучение</h3><p>В основном на автомате. Но начать можно и на механике.</p>'),
    ('<h3>Besondere Ausbildungsfahrten</h3><p>Über Land, auf der Autobahn und bei Dunkelheit, teils im Automatik-, teils im Schaltwagen.</p>',
     '<h3>Специальные учебные поездки</h3><p>За городом, по автобану и в тёмное время суток, частично на автомате, частично на механике.</p>'),
    ('<h3>Mindestens 10 Übungsstunden im Schaltwagen</h3><p>Erst danach darf die Testfahrt stattfinden.</p>',
     '<h3>Не менее 10 учебных часов на механике</h3><p>Только после этого можно пройти контрольную поездку.</p>'),
    ('<h3>Testfahrt von mindestens 15 Minuten</h3><p>Dein Fahrlehrer stellt fest, dass du den Schaltwagen sicher, verantwortungsvoll und umweltbewusst fährst. Dafür bekommst du eine Bescheinigung.</p>',
     '<h3>Контрольная поездка не менее 15 минут</h3><p>Инструктор подтверждает, что вы водите механику безопасно, ответственно и экономно. Об этом вы получаете справку.</p>'),
    ('<h3>Praktische Prüfung im Automatikauto</h3><p>Prüfungsvorbereitung und Prüfung finden im Automatikauto statt.</p>',
     '<h3>Практический экзамен на автомате</h3><p>Подготовка к экзамену и сам экзамен проходят на автомате.</p>'),
    # BF17
    ('<h2 class="h2" id="bf17-title">Begleitetes Fahren ab 17</h2>', '<h2 class="h2" id="bf17-title">Вождение с 17 лет</h2>'),
    ('Mit 17 Jahren die Klasse B oder BE erwerben und mit einer Begleitperson fahren, die in der Prüfungsbescheinigung namentlich eingetragen ist.',
     'Получить категорию B или BE в 17 лет и ездить с сопровождающим, который поимённо указан в экзаменационном свидетельстве.'),
    ('<p><strong>Ab 16½ Jahren</strong> kannst du den Antrag stellen, mit Einwilligung deiner Erziehungsberechtigten. Wer mit 16 anfängt, kann zum 17. Geburtstag fertig sein.</p>',
     '<p><strong>С 16,5 лет</strong> можно подать заявление с согласия родителей. Кто начинает в 16, может закончить к 17-летию.</p>'),
    ('<h3 class="h3">Diese Unterlagen brauchst du</h3>', '<h3 class="h3">Какие документы нужны</h3>'),
    ('<li>Personalausweis oder Pass</li>', '<li>Удостоверение личности или паспорт</li>'),
    ('<li>Ein biometrisches Lichtbild</li>', '<li>Одна биометрическая фотография</li>'),
    ('<li>Sehtestbescheinigung<small>nicht älter als zwei Jahre</small></li>', '<li>Справка о проверке зрения<small>не старше двух лет</small></li>'),
    ('<li>Nachweis über die Unterweisung in lebensrettenden Sofortmaßnahmen</li>', '<li>Подтверждение курса неотложной помощи</li>'),
    ('<li>Für jede Begleitperson die „Anlage zum Antrag Begleitetes Fahren ab 17“<small>mit Personalien und Unterschrift der Begleitperson, Kopie ihres Personalausweises und ihres Führerscheins</small></li>',
     '<li>Для каждого сопровождающего приложение к заявлению <span lang="de">„Anlage zum Antrag Begleitetes Fahren ab 17“</span><small>с личными данными и подписью сопровождающего, копией его удостоверения личности и водительских прав</small></li>'),
    ('<h3 class="h3" style="margin-top: 3rem; margin-bottom: 1rem">Formulare</h3>', '<h3 class="h3" style="margin-top: 3rem; margin-bottom: 1rem">Бланки (на немецком)</h3>'),
    ('<span class="download__name">Antrag Begleitetes Fahren ab 17</span><span class="download__meta">PDF, 286 KB</span>',
     '<span class="download__name">Заявление на вождение с 17 лет</span><span class="download__meta">PDF, 286 КБ</span>'),
    ('<span class="download__name">Erklärung der Begleitperson</span><span class="download__meta">PDF, 504 KB</span>',
     '<span class="download__name">Заявление сопровождающего</span><span class="download__meta">PDF, 504 КБ</span>'),
    ('<span class="download__name">Vordruck Kartenführerschein</span><span class="download__meta">PDF, 306 KB</span>',
     '<span class="download__name">Бланк для пластиковых прав</span><span class="download__meta">PDF, 306 КБ</span>'),
    # Schnellkurs
    ('Theorie-<span class="accent">Schnellkurs</span>', 'Интенсивный <span class="accent">курс теории</span>'),
    ('Wenig Zeit für die Führerscheinausbildung? Im Intensivkurs, oft auch Crashkurs genannt, schaffst du die Theorie in kürzester Zeit.',
     'Мало времени на обучение? На интенсивном курсе вы пройдёте теорию в самые короткие сроки.'),
    ('Die nächsten Termine für Klasse B erfährst du telefonisch oder per E-Mail. Zur Anmeldung reicht eine kurze Nachricht an',
     'Ближайшие даты для категории B узнавайте по телефону или по e-mail. Для записи достаточно короткого сообщения на'),
    ANRUFEN,
    # Auffrischung
    ('Führerschein <span class="accent">auffrischen.</span>', 'Восстановить <span class="accent">навыки вождения.</span>'),
    ('Separate Auffrischungsstunden für die Klassen B und BE. Was trainiert wird, vereinbarst du mit deinem Fahrlehrer.',
     'Отдельные занятия для категорий B и BE. Что именно тренировать, вы решаете вместе с инструктором.'),
    ('<p><strong>Voraussetzung:</strong> Du besitzt die jeweilige Führerscheinklasse.</p>', '<p><strong>Условие:</strong> у вас уже есть права соответствующей категории.</p>'),
    ('<h3 class="h3">Mögliche Trainingsinhalte</h3>', '<h3 class="h3">Что можно тренировать</h3>'),
    ('<li>Verkehrsregeln auffrischen, durch Teilnahme am Theorieunterricht</li>', '<li>Освежить правила дорожного движения на теоретических занятиях</li>'),
    ('<li>Fahren mit Schalt- oder Automatikfahrzeug</li>', '<li>Вождение на механике или на автомате</li>'),
    ('<li>Angstbewältigung im Straßenverkehr</li>', '<li>Преодоление страха на дороге</li>'),
    ('<li>Schwierige Verkehrssituationen meistern</li>', '<li>Сложные дорожные ситуации</li>'),
    ('<li>Einparken</li>', '<li>Парковка</li>'),
    ('<li>Fahren bei Dunkelheit</li>', '<li>Вождение в тёмное время суток</li>'),
    ('<li>Fahren bei Eis und Schnee<small>saisonbedingt und nur im Pkw</small></li>', '<li>Вождение по льду и снегу<small>в зависимости от сезона и только на легковом автомобиле</small></li>'),
]

BKF = [
    ('<title>BKF-Weiterbildung in Lahr, Schlüsselzahl 95 | Fahrschule Strauch</title>',
     '<title>Повышение квалификации профводителей в Ларе, код 95 | Автошкола Strauch</title>'),
    ('content="BKF-Weiterbildung nach BKrFQG in Lahr: Module 1 bis 5 für die Schlüsselzahl 95 bei der Fahrschule Strauch, amtlich anerkannte Ausbildungsstätte."',
     'content="Повышение квалификации профессиональных водителей по закону BKrFQG в Ларе: модули с 1 по 5 для кода 95 в автошколе Strauch, официально признанный учебный центр."'),
    ('<meta property="og:title" content="BKF-Weiterbildung in Lahr" />', '<meta property="og:title" content="Повышение квалификации профводителей в Ларе" />'),
    ('<meta property="og:description" content="Module 1 bis 5 für die Schlüsselzahl 95. Amtlich anerkannte Ausbildungsstätte." />',
     '<meta property="og:description" content="Модули с 1 по 5 для кода 95. Официально признанный учебный центр." />'),
    ('<li aria-current="page">Berufskraftfahrer</li>', '<li aria-current="page">Профводители</li>'),
    ('BKF-Weiterbildung <span class="accent">in Lahr.</span>', 'Повышение квалификации <span class="accent">в Ларе.</span>'),
    ('Amtlich anerkannte Ausbildungsstätte für die Weiterbildung nach dem Berufskraftfahrerqualifikationsgesetz, Schlüsselzahl 95.',
     'Официально признанный учебный центр для повышения квалификации профессиональных водителей по закону BKrFQG, код 95.'),
    ANRUFEN,
    MAIL,
    ('Die fünf <span class="accent">Module.</span>', 'Пять <span class="accent">модулей.</span>'),
    ('Wir bieten wieder unsere altbewährten Weiterbildungen für Berufskraftfahrer an. Termine und Anmeldung telefonisch oder per E-Mail.',
     'Мы снова проводим наше проверенное повышение квалификации для профессиональных водителей. Даты и запись по телефону или по e-mail.'),
    ('<h3>Eco-Training und Assistenzsysteme</h3>', '<h3>Эко-тренинг и системы помощи водителю</h3>'),
    ('<li>Eigenschaften der kinematischen Kette für eine optimierte Nutzung</li>', '<li>Особенности трансмиссии для оптимального использования</li>'),
    ('<li>Technische Merkmale und Funktionsweise der Sicherheitsausstattung</li>', '<li>Технические характеристики и работа систем безопасности</li>'),
    ('<li>Kraftstoffverbrauch optimieren</li>', '<li>Снижение расхода топлива</li>'),
    ('<h3>Sozialvorschriften und Fahrtenschreiber</h3>', '<h3>Социальные предписания и тахограф</h3>'),
    ('<li>Sozialrechtliche Rahmenbedingungen und Vorschriften für Güterkraft- und Personenverkehr</li>', '<li>Социально-правовые условия и правила для грузовых и пассажирских перевозок</li>'),
    ('<li>Vorschriften für den Güterkraftverkehr</li>', '<li>Правила грузовых перевозок</li>'),
    ('<li>Vorschriften für den Personenverkehr</li>', '<li>Правила пассажирских перевозок</li>'),
    ('<h3>Gefahrenwahrnehmung</h3>', '<h3>Восприятие опасностей</h3>'),
    ('<li>Bewusstsein für Risiken des Straßenverkehrs und Arbeitsunfälle</li>', '<li>Осознание рисков дорожного движения и несчастных случаев на работе</li>'),
    ('<li>Lage bei Notfällen richtig einschätzen</li>', '<li>Правильная оценка ситуации в экстренных случаях</li>'),
    ('<h3>Schadensprävention</h3>', '<h3>Предотвращение ущерба</h3>'),
    ('<li>Gesundheitsschäden vorbeugen</li>', '<li>Профилактика вреда для здоровья</li>'),
    ('<li>Verhalten, das zu einem positiven Bild des Unternehmens beiträgt</li>', '<li>Поведение, которое формирует положительный образ компании</li>'),
    ('<h3>Sicherheit für Ladung und Fahrgast</h3>', '<h3>Безопасность груза и пассажиров</h3>'),
    ('<li>Sicherheit der Ladung gewährleisten</li>', '<li>Безопасность груза</li>'),
    ('<li>Sicherheit und Komfort der Fahrgäste gewährleisten</li>', '<li>Безопасность и комфорт пассажиров</li>'),
    ('<li>Ladungssicherung nach den Sicherheitsvorschriften und richtige Benutzung des KOM</li>', '<li>Крепление груза по правилам безопасности и правильное использование автобуса</li>'),
    ('Rufen Sie uns an, <span class="accent">wir beraten Sie gern.</span>', 'Позвоните нам, <span class="accent">мы охотно проконсультируем.</span>'),
    ('<dt>Ansprechpartner</dt>', '<dt>Контактное лицо</dt>'),
    ('<dt>Telefon</dt>', '<dt>Телефон</dt>'),
    ('<dt>E-Mail</dt>', '<dt>E-mail</dt>'),
    ('<dt>Adresse</dt><dd>Schwarzwaldstraße 93, 77933 Lahr</dd>', '<dt>Адрес</dt><dd lang="de">Schwarzwaldstraße 93, 77933 Lahr</dd>'),
]

UEBER = [
    ('<title>Über uns: Team und Fahrlehrer | Fahrschule Strauch Lahr</title>', '<title>О нас: команда и инструкторы | Автошкола Strauch, Лар</title>'),
    ('content="Das Team der Fahrschule Viktor Strauch in Lahr: Fahrlehrer seit 1984, 1988, 2000 und 2007. Eine Fahrschule, in der Fehler passieren dürfen und Fragen erwünscht sind."',
     'content="Команда автошколы Viktor Strauch в Ларе: инструкторы с 1984, 1988, 2000 и 2007 года. Автошкола, где можно ошибаться и задавать вопросы."'),
    ('<meta property="og:title" content="Über uns: das Team der Fahrschule Strauch" />', '<meta property="og:title" content="О нас: команда автошколы Strauch" />'),
    ('<meta property="og:description" content="Fahrlehrer seit 1984, 1988, 2000 und 2007 in Lahr." />', '<meta property="og:description" content="Инструкторы с 1984, 1988, 2000 и 2007 года в Ларе." />'),
    ('<li aria-current="page">Über uns</li>', '<li aria-current="page">О нас</li>'),
    ('In guten Händen, <span class="accent">vom ersten Meter an.</span>', 'В надёжных руках <span class="accent">с первого метра.</span>'),
    ('Willkommen in der Fahrschule Viktor Strauch. Hier wird dein Weg zum Führerschein eine Reise, die sich lohnt.',
     'Добро пожаловать в автошколу Viktor Strauch. Здесь путь к правам становится путешествием, которое того стоит.'),
    ('alt="Das Team der Fahrschule Strauch mit vier Fahrschulautos vor dem Gebäude in der Schwarzwaldstraße"',
     'alt="Команда автошколы Strauch с четырьмя учебными автомобилями перед зданием на Schwarzwaldstraße"'),
    ('Verstehen statt <span class="accent">auswendig lernen.</span>', 'Понимать, <span class="accent">а не зубрить.</span>'),
    ('Unsere Fahrlehrer lieben ihren Job und bringen dir alles bei, was du brauchst, um sicher und selbstbewusst hinter dem Steuer zu sitzen.',
     'Наши инструкторы любят свою работу и научат всему, что нужно, чтобы уверенно и безопасно сидеть за рулём.'),
    ('Fehler passieren. Wir ermutigen dich, aus ihnen zu lernen, ohne Angst davor zu haben. Du sollst dich bei uns wohlfühlen und jede Frage stellen können.',
     'Ошибки случаются. Мы поддерживаем вас, чтобы вы учились на них без страха. У нас вам должно быть комфортно, и любой вопрос можно задать.'),
    ('Unser Unterricht setzt auf moderne Lehrmethoden, interaktive Stunden und praktische Übungen, damit du das Verkehrsgeschehen wirklich verstehst. Ob Theorie oder Fahrstunde: Wir begleiten dich bei jedem Schritt.',
     'Наши занятия строятся на современных методах, интерактивных уроках и практических упражнениях, чтобы вы действительно понимали дорожную обстановку. Теория или урок вождения: мы сопровождаем вас на каждом шаге.'),
    ('Unser Ziel ist nicht nur, dass du die Prüfung bestehst, sondern dass du ein verantwortungsbewusster und sicherer Fahrer wirst. Und wir beraten dich auch auf Russisch: <span lang="ru">говорим по-русски</span>.',
     'Наша цель не только в том, чтобы вы сдали экзамен, но и в том, чтобы вы стали ответственным и уверенным водителем. И мы говорим по-русски.'),
    ('Das <span class="accent">Team.</span>', 'Наша <span class="accent">команда.</span>'),
    ('alt="Viktor Strauch lehnt an einem Fahrschulauto"', 'alt="Viktor Strauch у учебного автомобиля"'),
    ('alt="Peter Harter neben einem Fahrschulauto"', 'alt="Peter Harter рядом с учебным автомобилем"'),
    ('alt="Gerold Remmele neben einem Fahrschulauto"', 'alt="Gerold Remmele рядом с учебным автомобилем"'),
    ('alt="Nadine Dürr an der geöffneten Fahrertür eines Fahrschulautos"', 'alt="Nadine Dürr у открытой водительской двери учебного автомобиля"'),
    *QUOTES,
    *ROLES,
    ('<p class="person__extra">Das Hobby zum Beruf gemacht.</p>', '<p class="person__extra">Хобби стало профессией.</p>'),
    ('Fahrlehrer <span class="accent">gesucht.</span>', 'Ищем <span class="accent">инструкторов.</span>'),
    ('Unser Team braucht Verstärkung. Wenn du Fahrlehrerin oder Fahrlehrer bist und zu uns passen möchtest, melde dich.',
     'Нашей команде нужно пополнение. Если вы инструктор по вождению и хотите работать с нами, свяжитесь с нами.'),
    ANRUFEN,
    MAIL,
]

ANMELDUNG = [
    ('<title>Anmeldung und Kontakt | Fahrschule Strauch Lahr</title>', '<title>Запись и контакты | Автошкола Strauch, Лар</title>'),
    ('content="Bei der Fahrschule Strauch in Lahr anmelden: online über den Fahrschulmanager oder mit dem Anmeldeformular. Formulare, App Fahren Lernen MAX, Finanzierung und Kontakt."',
     'content="Запись в автошколу Strauch в Ларе: онлайн через Fahrschulmanager или с помощью бланка. Бланки, приложение Fahren Lernen MAX, финансирование и контакты."'),
    ('<meta property="og:title" content="Anmeldung bei der Fahrschule Strauch" />', '<meta property="og:title" content="Запись в автошколу Strauch" />'),
    ('<meta property="og:description" content="Online anmelden, Formulare herunterladen, Kontakt und Anfahrt." />',
     '<meta property="og:description" content="Записаться онлайн, скачать бланки, контакты и как добраться." />'),
    ('<li aria-current="page">Anmeldung und Kontakt</li>', '<li aria-current="page">Запись и контакты</li>'),
    ('Anmelden <span class="accent">und losfahren.</span>', 'Записаться <span class="accent">и поехать.</span>'),
    ('Online, mit dem Formular oder persönlich bei uns in der Schwarzwaldstraße&nbsp;93.',
     'Онлайн, с помощью бланка или лично у нас на Schwarzwaldstraße&nbsp;93.'),
    ('<h2 class="h2" id="online-title">Online anmelden</h2>', '<h2 class="h2" id="online-title">Записаться онлайн</h2>'),
    ('Die Anmeldung läuft über den Fahrschulmanager. Dort gibst du deine Daten einmal online ein.',
     'Запись проходит через Fahrschulmanager. Там вы один раз вводите свои данные онлайн. Форма на немецком языке.'),
    ('type="submit">Jetzt anmelden <svg', 'type="submit">Записаться <svg'),
    ('Öffnet die Anmeldung beim Fahrschulmanager in einem neuen Tab.', 'Запись в Fahrschulmanager откроется в новой вкладке.'),
    ('Formulare <span class="accent">zum Herunterladen.</span>', 'Бланки <span class="accent">для скачивания.</span>'),
    ('Lieber auf Papier? Anmeldeformular ausdrucken, ausfüllen und vorbeibringen.',
     'Удобнее на бумаге? Распечатайте бланк записи, заполните и принесите нам. Бланки на немецком языке.'),
    ('<span class="download__name">Anmeldeformular</span><span class="download__meta">PDF, 653 KB</span>', '<span class="download__name">Бланк записи</span><span class="download__meta">PDF, 653 КБ</span>'),
    ('<span class="download__name">Führerscheinantrag</span><span class="download__meta">PDF, 216 KB</span>', '<span class="download__name">Заявление на получение прав</span><span class="download__meta">PDF, 216 КБ</span>'),
    ('<span class="download__name">Info und Preise Klasse B</span><span class="download__meta">PDF, 15 KB</span>', '<span class="download__name">Информация и цены, категория B</span><span class="download__meta">PDF, 15 КБ</span>'),
    ('<span class="download__name">Info und Preise Klasse BE</span><span class="download__meta">PDF, 12 KB</span>', '<span class="download__name">Информация и цены, категория BE</span><span class="download__meta">PDF, 12 КБ</span>'),
    ('<span class="download__name">Antrag Begleitetes Fahren ab 17</span><span class="download__meta">PDF, 286 KB</span>', '<span class="download__name">Заявление на вождение с 17 лет</span><span class="download__meta">PDF, 286 КБ</span>'),
    ('<span class="download__name">BF17: Erklärung der Begleitperson</span><span class="download__meta">PDF, 504 KB</span>', '<span class="download__name">BF17: заявление сопровождающего</span><span class="download__meta">PDF, 504 КБ</span>'),
    ('<span class="download__name">Vordruck Kartenführerschein</span><span class="download__meta">PDF, 306 KB</span>', '<span class="download__name">Бланк для пластиковых прав</span><span class="download__meta">PDF, 306 КБ</span>'),
    ('aria-label="App und Finanzierung"', 'aria-label="Приложение и финансирование"'),
    ('<h2 class="h3">App Fahren Lernen MAX</h2>', '<h2 class="h3">Приложение Fahren Lernen MAX</h2>'),
    ('Mit interaktiven Lektionen und Übungen lernst du die Theorie, wann und wo du willst: auf dem Sofa oder unterwegs in der Bahn. Du siehst deinen Lernfortschritt und übst gezielt dort, wo du noch unsicher bist.',
     'С интерактивными уроками и упражнениями вы учите теорию, когда и где удобно: дома на диване или в электричке. Вы видите свой прогресс и целенаправленно тренируете то, в чём ещё не уверены.'),
    ('<h2 class="h3">Finanzierung mit STARTHILFE</h2>', '<h2 class="h3">Финансирование с STARTHILFE</h2>'),
    ('STARTHILFE wurde speziell für Fahrschüler entwickelt, vom Verlag Heinrich Vogel und der Credit Europe Bank N.V. in Frankfurt am Main.',
     'STARTHILFE разработано специально для учеников автошкол издательством Heinrich Vogel и Credit Europe Bank N.V. во Франкфурте-на-Майне.'),
    ('Mehr zu STARTHILFE <svg', 'Подробнее о STARTHILFE (на немецком) <svg'),
]

TABLE = {'': START, 'fuehrerschein': FUEHRERSCHEIN, 'berufskraftfahrer': BKF, 'ueber-uns': UEBER, 'anmeldung': ANMELDUNG}


def main():
    for page in PAGES:
        src = os.path.join(ROOT, page, 'index.html')
        text = open(src, encoding='utf-8').read()
        text = replace_all(text, TABLE[page], page)
        text = common(text, page)
        out_dir = os.path.join(ROOT, 'ru', page)
        os.makedirs(out_dir, exist_ok=True)
        head, rest = text.split('\n', 1)
        text = head + '\n<!-- Automatisch erzeugt aus der deutschen Seite: python3 scripts/translate_ru.py -->\n' + rest
        open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(text)
        print('✓ ru/' + (page + '/' if page else ''))


if __name__ == '__main__':
    main()
