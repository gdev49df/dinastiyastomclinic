#!/usr/bin/env python3
"""Генератор страниц услуг Dinastiya Stom Clinic.

Также обновляет подвал на главной между маркерами <!-- footer:start --> и <!-- footer:end -->.

Запуск из корня репозитория:  python3 tools/build.py
Создаёт implantation.html, orthodontics.html, therapy.html, orthopedics.html, kids.html,
а также sitemap.xml и robots.txt. Главная страница (index.html) пишется вручную.
Контакты и тексты общие для всех страниц лежат в начале этого файла.
"""
import os
from html import escape
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://dinastiyastomclinic.gdev.uk"
PHONE = "+7 776 773 24 21"
PHONE_RAW = "+77767732421"
WA = "77767732421"

DOCTORS = {
    "dilnara": dict(photo="img/doc-5.webp", name="Гуламова Дильнара Эркиновна", role="Руководитель клиники, главный врач-стоматолог, терапевт-эндодонтист",
                    about="Руководит клиникой, формирует профессиональную команду и следит за качеством медицинских услуг и комфортом пациентов. Лечит зубы и проводит эндодонтическое лечение."),
    "kirill": dict(photo="img/doc-1.webp", name="Дарцимелидзе Кирилл Окроевич", role="Стоматолог-терапевт, хирург и детский стоматолог. Лечение под микроскопом",
                   about="Лечит заболевания полости рта у пациентов всех возрастов, в том числе под микроскопом. Работает по современным методикам с индивидуальным подходом."),
    "vivadi": dict(photo="img/doc-2.webp", name="Хамедов Видади Адилоглы", role="Терапевт, хирург-ортопед",
                   about="Восстанавливает зубы коронками и винирами, проводит протезирование и лечение зубов."),
    "miras": dict(photo="img/doc-3.webp", name="Жетібаев Мирас Куанышевич", role="Хирург имплантолог-ортопед",
                  about="Выполняет имплантацию по протоколу All-on-4 / All-on-6 и восстанавливает зубной ряд."),
    "dinmukhamed": dict(photo="img/doc-6.webp", name="Қонарбаев Дінмұхамед Мадиұлы", role="Пародонтолог, терапевт, хирург",
                        about="Лечит заболевания дёсен и тканей вокруг зуба, проводит терапевтический приём и хирургические вмешательства."),
}

SERVICES = [
    ("/implantation", "Имплантация зубов", "Импланты премиум-класса, All-on-4 / All-on-6, гарантия 10 лет."),
    ("/therapy#ortho", "Ортодонтия", "Брекеты, элайнеры, пластинки, капы и ретейнеры."),
    ("/therapy", "Лечение зубов", "Кариес, эндодонтия, лечение под микроскопом."),
    ("/orthopedics", "Ортопедия", "Коронки, виниры и восстановление зубного ряда."),
    ("/periodontics", "Пародонтология", "Лечение дёсен и заболеваний пародонта."),
    ("/kids", "Детская стоматология", "Детский терапевт-хирург. Бережный приём."),
]

HOURS = "Пн–Пт 9:00–20:00, Сб–Вс 10:00–20:00"


def wa(text):
    return f"https://wa.me/{WA}?text={quote(text)}"


def btn_wa(text, label, cls="btn--gold"):
    return f'<a class="btn {cls}" data-wa="{escape(text)}" href="{wa(text)}" target="_blank" rel="noopener">{escape(label)}</a>'


def header():
    return f'''<header class="header" id="top">
  <div class="wrap header__in">
    <a class="logo" href="/" aria-label="Dinastiya Stom Clinic — на главную">
      <img src="/img/logo.webp" alt="Dinastiya Stom Clinic" width="121" height="76">
    </a>
    <nav class="nav" id="nav" aria-label="Основное меню">
      <a href="/#services">Услуги</a>
      <a href="/#prices">Цены</a>
      <a href="/#implants">Имплантация</a>
      <a href="/#installment">Рассрочка</a>
      <a href="/#team">Команда</a>
      <a href="/#contacts">Контакты</a>
    </nav>
    <div class="header__actions">
      <div class="lang" id="lang">
        <button class="lang__btn" id="lang-btn" type="button" aria-haspopup="true" aria-expanded="false" aria-label="Язык сайта"><span id="lang-cur">RU</span><svg viewBox="0 0 12 8" aria-hidden="true"><path d="m1 1.500 5 5 5-5"/></svg></button>
        <ul class="lang__menu" id="lang-menu" role="menu" hidden>
          <li><button type="button" role="menuitem" data-lang="kk">Қазақша</button></li>
          <li><button type="button" role="menuitem" data-lang="ru">Русский</button></li>
          <li><button type="button" role="menuitem" data-lang="en">English</button></li>
        </ul>
      </div>
      <a class="header__phone" href="tel:{PHONE_RAW}">{PHONE}</a>
      <a class="btn btn--gold btn--sm" data-wa="Здравствуйте! Хочу записаться на приём." href="{wa('Здравствуйте! Хочу записаться на приём.')}" target="_blank" rel="noopener">Записаться</a>
      <button class="burger" id="burger" aria-label="Открыть меню" aria-expanded="false" aria-controls="nav"><span></span><span></span></button>
    </div>
  </div>
</header>'''


GIS = "https://2gis.kz/astana/search/Dinastiya%20Stom%20Clinic"
EMAIL = "dinastiya.stomclinic@mail.ru"


def footer_html(on_index=False):
    """Подвал. На главной ссылки-якоря короткие (#prices), на остальных страницах ведут на /#..."""
    pre = "" if on_index else "/"
    home = "#top" if on_index else "/"
    svc = "".join(f'<li><a href="{h}">{escape(title)}</a></li>' for h, title, _ in SERVICES)
    clinic = "".join(f'<li><a href="{pre}#{a}">{escape(label)}</a></li>' for a, label in [
        ("prices", "Цены"), ("installment", "Рассрочка"), ("team", "Команда"),
        ("reviews", "Отзывы"), ("faq", "Частые вопросы"), ("contacts", "Контакты")])
    return f'''<footer class="footer">
  <div class="wrap footer__grid">
    <div class="footer__brand">
      <a class="logo" href="{home}" aria-label="Dinastiya Stom Clinic — наверх"><img src="/img/logo.webp" alt="Dinastiya Stom Clinic" width="97" height="61" loading="lazy"></a>
      <p class="footer__addr">Астана, проспект Туран, 34Б</p>
      <p><a class="footer__phone" href="tel:{PHONE_RAW}">{PHONE}</a></p>
      <p class="footer__hours">{HOURS}</p>
    </div>
    <nav class="footer__col" aria-label="Услуги">
      <h3>Услуги</h3>
      <ul>{svc}</ul>
    </nav>
    <nav class="footer__col" aria-label="Клиника">
      <h3>Клиника</h3>
      <ul>{clinic}</ul>
    </nav>
    <div class="footer__col">
      <h3>Связаться</h3>
      <ul>
        <li><a href="{wa('Здравствуйте!')}" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a href="https://www.instagram.com/dinastiyastomclinic/" target="_blank" rel="noopener">Instagram</a></li>
        <li><a href="{GIS}" target="_blank" rel="noopener">2ГИС</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer__bottom">
    <p class="footer__note">Имеются противопоказания. Необходима консультация специалиста.</p>
    <p class="footer__copy">© 2024–2026 Dinastiya Stom Clinic. Все права защищены.</p>
  </div>
</footer>'''


def fab():
    return f'''<a class="fab" data-wa="Здравствуйте! Хочу записаться на приём." href="{wa('Здравствуйте! Хочу записаться на приём.')}" target="_blank" rel="noopener" aria-label="Написать в WhatsApp">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.2 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8s.7-2 .9-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.3.4-.4.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.7-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4Z"/></svg>
</a>'''


def initials(name):
    parts = [w for w in name.split() if w[:1].isalpha()]
    return "".join(w[0] for w in parts[:2]).upper()


def photo_html(d, w=340, h=400):
    if d["photo"]:
        return f'<img src="/{d["photo"]}" alt="{escape(d["name"])}" width="{w}" height="{h}" loading="lazy">'
    return f'<div class="ph" role="img" aria-label="{escape(d["name"])}"><span>{escape(initials(d["name"]))}</span></div>'


def doctor_card(key):
    d = DOCTORS[key]
    return f'''<figure class="person reveal" style="margin:0">
          <div class="person__photo">{photo_html(d)}</div>
          <figcaption><b>{escape(d['name'])}</b><span>{escape(d['role'])}</span><p>{escape(d['about'])}</p></figcaption>
        </figure>'''


def doctor_wide(key):
    d = DOCTORS[key]
    return f'''<article class="docwide reveal">
          <div class="docwide__photo">{photo_html(d, 420, 500)}</div>
          <div class="docwide__text"><b>{escape(d['name'])}</b><span>{escape(d['role'])}</span><p>{escape(d['about'])}</p></div>
        </article>'''


def doctor_split(keys, eyebrow, title, intro=None, ivory=False):
    """Заголовок и текст о враче слева, фото справа."""
    cls = "section section--ivory" if ivory else "section"
    blocks = ""
    for k in keys:
        d = DOCTORS[k]
        blocks += f'''<div class="docsplit reveal">
        <div class="docsplit__text">
          <h3>{escape(d['name'])}</h3>
          <span>{escape(d['role'])}</span>
          <p>{escape(d['about'])}</p>
        </div>
        <div class="docsplit__photo">{photo_html(d, 420, 500)}</div>
      </div>'''
    sub = f'<p class="section__sub">{escape(intro)}</p>' if intro else ""
    return f'''<section class="{cls}" id="doctors">
    <div class="wrap">
      <header class="section__head reveal">
        <p class="eyebrow">{escape(eyebrow)}</p>
        <h2>{escape(title)}</h2>
        {sub}
      </header>
      {blocks}
    </div>
  </section>'''


def hero_media(kind, img, alt):
    if kind == "duo":
        a, b = img
        return (f'<div class="duo-photos"><div class="photo-frame"><img src="/{a}" alt="{escape(alt[0])}" width="760" height="900" fetchpriority="high"></div>'
                f'<div class="photo-frame"><img src="/{b}" alt="{escape(alt[1])}" width="760" height="900" fetchpriority="high"></div></div>')
    if kind == "arch":
        return f'<div class="arch"><img src="/{img}" alt="{escape(alt)}" width="724" height="797" fetchpriority="high"></div>'
    return f'<div class="photo-frame"><img src="/{img}" alt="{escape(alt)}" width="760" height="900" fetchpriority="high"></div>'


def facts(items):
    li = "".join(f"<li><b>{escape(b)}</b><span>{escape(s)}</span></li>" for b, s in items)
    return f'<ul class="hero__facts">{li}</ul>'


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{escape(i)}</li>" for i in items) + "</ul>"


def steps(items):
    out = ""
    for n, (t, d) in enumerate(items, 1):
        out += f'<li class="reveal"><span>{n}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></li>'
    cols = ' style="grid-template-columns:repeat(%d,1fr)"' % len(items) if len(items) != 4 else ""
    return f'<ol class="steps">{out}</ol>'


def faq(items, ivory=False):
    body = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in items)
    return f'''<section class="section{' section--ivory' if ivory else ''}" id="faq">
    <div class="wrap wrap--narrow">
      <header class="section__head reveal">
        <p class="eyebrow">Вопросы</p>
        <h2>Частые вопросы</h2>
      </header>
      <div class="faq reveal">{body}</div>
    </div>
  </section>'''


def price_strip(rows, note=None):
    lis = "".join(f"<li><span>{escape(a)}</span><b>{escape(b)}</b></li>" for a, b in rows)
    n = f'<p class="price-note">{escape(note)}</p>' if note else ""
    return f'''<section class="section section--ivory" id="price">
    <div class="wrap wrap--narrow">
      <header class="section__head reveal">
        <p class="eyebrow">Цены</p>
        <h2>Стоимость приёма</h2>
      </header>
      <div class="price-card reveal">
        <div class="price-card__head"><span>Услуга</span><i>{len(rows)}</i></div>
        <ul class="price-list">{lis}</ul>
      </div>
      {n}
      <div class="center reveal" style="margin-top:28px"><a class="btn btn--ghost" href="/#prices">Все цены</a></div>
    </div>
  </section>'''


def other_services(current, ivory=False):
    cards = ""
    for href, title, text in SERVICES:
        if href.split("#")[0] == current:
            continue
        cards += f'''<article class="card reveal">
          <h3>{escape(title)}</h3>
          <p>{escape(text)}</p>
          <a class="card__link" href="{href}">Подробнее</a>
        </article>'''
    return f'''<section class="section{' section--ivory' if ivory else ''}" id="other">
    <div class="wrap">
      <header class="section__head reveal">
        <p class="eyebrow">Другие услуги</p>
        <h2>Что ещё мы делаем</h2>
      </header>
      <div class="cards cards--four">{cards}</div>
    </div>
  </section>'''


def cta(title, text, wa_text):
    return f'''<section class="section section--dark" id="contacts">
    <div class="wrap cta reveal">
      <div>
        <p class="eyebrow">Запись на приём</p>
        <h2>{escape(title)}</h2>
        <p class="section__sub">{escape(text)}</p>
      </div>
      <div class="cta__actions">
        {btn_wa(wa_text, "Записаться в WhatsApp")}
        <a class="btn btn--ghost cta__phone" href="tel:{PHONE_RAW}">{PHONE}</a>
        <p class="cta__addr">Астана, проспект Туран, 34Б</p>
      </div>
    </div>
  </section>'''


def page(p):
    slug = p["slug"]
    url = f"{SITE}/{slug[:-5]}"
    ld = f'''<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Главная", "item": "{SITE}/"}},
      {{"@type": "ListItem", "position": 2, "name": "{escape(p['crumb'])}", "item": "{url}"}}
    ]
  }}
  </script>'''
    doctors = ""
    if p.get("doctors"):
        mode = p.get("doctors_mode", "cards")
        title = p.get('doctors_title', 'Кто вас примет')
        if mode == "split":
            doctors = doctor_split(p["doctors"], "Специалист", title, p.get("doctors_intro"))
        else:
            cards = "".join(doctor_wide(k) for k in p["doctors"])
            doctors = f'''<section class="section" id="doctors">
    <div class="wrap">
      <header class="section__head reveal">
        <p class="eyebrow">Специалисты</p>
        <h2>{escape(title)}</h2>
      </header>
      <div class="docwide-list">{cards}</div>
    </div>
  </section>'''
    prices = price_strip(p['prices'], p.get('price_note')) if p.get('prices') else ""
    return f'''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(p['title'])}</title>
  <meta name="description" content="{escape(p['description'])}">
  <meta name="theme-color" content="#fbf9f4">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="/img/logo.webp" type="image/webp">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(p['title'])}">
  <meta property="og:description" content="{escape(p['description'])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/{p['hero_img']}">
  <meta property="og:locale" content="ru_RU">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  {ld}
</head>
<body>

{header()}

<main>
  <section class="page-hero">
    <div class="wrap page-hero__in">
      <div class="reveal">
        <nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span>/</span><a href="/#services">Услуги</a><span>/</span>{escape(p['crumb'])}</nav>
        <p class="eyebrow">{escape(p['eyebrow'])}</p>
        <h1>{p['h1']}</h1>
        <p class="lead">{escape(p['lead'])}</p>
        <div class="hero__cta">
          {btn_wa(p['wa'], p.get('cta_label', 'Записаться на приём'))}
          {('<a class="btn btn--ghost" href="#price">Цены</a>' if p.get('prices') else '')}
        </div>
        {facts(p['facts'])}
      </div>
      <div class="page-hero__media reveal">
        {hero_media(p['hero_kind'], p['hero_img'], p['hero_alt'])}
      </div>
    </div>
  </section>

  {p['body']}

  {doctors}

  {prices}

  {faq(p['faq'], ivory=not p.get('prices'))}

  {other_services("/" + slug[:-5], ivory=bool(p.get('prices')))}

  {cta(p['cta_title'], p['cta_text'], p['wa'])}
</main>

{footer_html()}

{fab()}

<script src="/js/data.js"></script>
<script src="/js/i18n.js"></script>
<script src="/js/main.js"></script>
<script src="/js/lang.js"></script>
</body>
</html>
'''


def split_block(eyebrow, title, text, items, side_img=None, side_alt="", id_=None, ivory=False):
    idattr = f' id="{id_}"' if id_ else ""
    cls = "section section--ivory" if ivory else "section"
    sub = f'<p class="section__sub">{escape(text)}</p>' if text else ""
    if side_img:
        media = f'<div class="split__media reveal"><div class="photo-frame"><img src="/{side_img}" alt="{escape(side_alt)}" width="760" height="900" loading="lazy"></div></div>'
        return f'''<section class="{cls}"{idattr}>
    <div class="wrap split">
      {media}
      <div class="split__text reveal">
        <p class="eyebrow">{escape(eyebrow)}</p>
        <h2>{escape(title)}</h2>
        {sub}
        {checks(items)}
      </div>
    </div>
  </section>'''
    return f'''<section class="{cls}"{idattr}>
    <div class="wrap duo">
      <div class="duo__head reveal">
        <p class="eyebrow">{escape(eyebrow)}</p>
        <h2>{escape(title)}</h2>
        {sub}
      </div>
      <div class="duo__list reveal">
        {checks(items)}
      </div>
    </div>
  </section>'''


def brands_block(eyebrow, title, sub, items, id_="brands", ivory=False, cols=4):
    cards = "".join(f'<li class="brand reveal"><b>{escape(n)}</b><span>{escape(c)}</span></li>' for n, c in items)
    cls = "section section--ivory" if ivory else "section"
    subh = f'<p class="section__sub">{escape(sub)}</p>' if sub else ""
    return f'''<section class="{cls}" id="{id_}">
    <div class="wrap">
      <header class="section__head reveal">
        <p class="eyebrow">{escape(eyebrow)}</p>
        <h2>{escape(title)}</h2>
        {subh}
      </header>
      <ul class="brands brands--{cols}">{cards}</ul>
    </div>
  </section>'''


def steps_block(eyebrow, title, items):
    return f'''<section class="section section--ivory">
    <div class="wrap">
      <header class="section__head reveal">
        <p class="eyebrow">{escape(eyebrow)}</p>
        <h2>{escape(title)}</h2>
      </header>
      {steps(items)}
    </div>
  </section>'''


PAGES = []

INSTALLMENT = '''<section class="section section--dark" id="installment">
    <div class="wrap">
      <header class="section__head reveal">
        <p class="eyebrow">Рассрочка</p>
        <h2>Лечитесь сейчас, платите постепенно</h2>
        <p class="section__sub">Рассрочка на имплантацию зубов: от 100 000 до 400 000 ₸.</p>
      </header>
      <div class="grid3">
        <div class="stat reveal"><b>0%</b><span>Без процентов и переплат</span></div>
        <div class="stat reveal"><b>до 24</b><span>месяцев рассрочки</span></div>
        <div class="stat reveal"><b>Halyk · Kaspi</b><span>0-0-24 от банка или рассрочка от клиники</span></div>
      </div>
    </div>
  </section>'''

# ---------- имплантация ----------
PAGES.append(dict(
    slug="implantation.html",
    crumb="Имплантация",
    title="Имплантация зубов в Астане с гарантией 10 лет | Dinastiya Stom Clinic",
    description="Имплантация зубов в Астане: импланты SIN, Straumann, Osstem и Neodent, All-on-4 / All-on-6, фиксированная цена, рассрочка 0-0-24. Гарантия 10 лет.",
    eyebrow="Имплантация",
    h1="Имплантация зубов <em>с&nbsp;гарантией 10&nbsp;лет</em>",
    lead="Импланты премиум-класса из Кореи, Швейцарии и Бразилии и фиксированная цена. Операцию проводит опытный хирург-ортопед.",
    wa="Здравствуйте! Хочу консультацию по имплантации.",
    facts=[("10 лет", "гарантия на имплантацию"), ("335", "операций за прошлый год"), ("0-0-24", "рассрочка Halyk и Kaspi")],
    hero_kind="frame", hero_img="img/doc-3.webp", hero_alt="Жетібаев Мирас Куанышевич, хирург имплантолог-ортопед",
    body=(
        split_block("Почему мы", "Импланты, которые служат десятилетиями",
                    "Мы ставим проверенные системы имплантов и отвечаем за результат: на имплантацию действует гарантия 10 лет. Каждый этап планируем заранее, поэтому результат предсказуем, а цена известна до операции.",
                    ["Импланты премиум-класса: Корея, Швейцария и Бразилия",
                     "Прямая поставка сертифицированных имплантов от производителей",
                     "Хирургические шаблоны для точной установки",
                     "Высокая приживаемость",
                     "Фиксированная цена на импланты, без скрытых доплат",
                     "Гарантия 10 лет"], id_="why")
        + brands_block("Системы имплантов", "С какими имплантами мы работаем",
                       "Устанавливаем импланты проверенных мировых производителей.",
                       [("SIN", "Бразилия"), ("Straumann", "Швейцария"), ("Osstem", "Корея"), ("Neodent", "Швейцария")])
        + split_block("All-on-4 / All-on-6", "Восстановление всех зубов на имплантах",
                      "Один из самых надёжных и проверенных методов восстановления всего зубного ряда. Имплантацию выполняет хирург-ортопед по протоколу All-on-4 / All-on-6.",
                      ["Подходит, когда нужно восстановить зубной ряд целиком",
                       "Фиксация на 4 или 6 имплантах",
                       "Планирование операции до начала лечения",
                       "Операцию выполняет хирург-ортопед"], id_="all-on", ivory=True)
        + steps_block("Этапы", "Как проходит имплантация", [
            ("Консультация", "Осмотр и консультация хирурга. Определяем, какое лечение вам нужно."),
            ("Обследование", "Осмотр, снимок и подбор системы импланта."),
            ("План и цена", "Подробный план лечения с фиксированной стоимостью."),
            ("Операция и гарантия", "Установка импланта опытными специалистами. Гарантия 10 лет."),
        ])
        + INSTALLMENT
    ),
    doctors=["miras"], doctors_mode="split", doctors_title="Кто проводит имплантацию",
    prices=[("Консультация хирурга", "5 000 ₸"), ("Консультация хирурга-ортопеда", "5 000 ₸")],
    price_note="Стоимость имплантации врач называет после обследования и фиксирует в плане лечения.",
    faq=[("Какая гарантия на имплантацию?", "Гарантия на имплантацию составляет 10 лет."),
         ("Можно ли оформить рассрочку?", "Да. Доступна рассрочка без процентов до 24 месяцев: Halyk и Kaspi 0-0-24 или рассрочка от клиники."),
         ("Какие импланты вы ставите?", "Мы устанавливаем импланты SIN (Бразилия), Straumann (Швейцария), Osstem (Корея) и Neodent (Швейцария). Поставка прямая, от производителей, имплантаты сертифицированы."),
         ("Как узнать точную стоимость?", "После обследования врач составит план лечения с фиксированной ценой. Консультация хирурга стоит 5 000 ₸.")],
    cta_title="Запишитесь на консультацию по имплантации",
    cta_text="Напишите нам в WhatsApp или позвоните, подберём удобное время.",
))

# ---------- лечение зубов + ортодонтия ----------
PAGES.append(dict(
    slug="therapy.html",
    crumb="Лечение зубов",
    title="Лечение зубов и ортодонтия в Астане: кариес, эндодонтия, брекеты | Dinastiya Stom Clinic",
    description="Лечение кариеса и эндодонтическое лечение в Астане, лечение зубов под микроскопом взрослым и детям, ортодонтия: брекеты, элайнеры, пластинки, капы, ретейнеры. Консультация 5 000 ₸, лечение от 30 000 ₸.",
    eyebrow="Терапия и ортодонтия",
    h1="Лечение зубов: <em>кариес, эндодонтия, ортодонтия</em>",
    lead="Лечим кариес по современным методикам, проводим эндодонтическое лечение, в том числе под микроскопом, и исправляем прикус.",
    wa="Здравствуйте! Хочу записаться на лечение зубов.",
    facts=[("от 30 000 ₸", "лечение"), ("5 000 ₸", "консультация"), ("микроскоп", "для взрослых и детей")],
    hero_kind="frame", hero_img="img/doc-5.webp", hero_alt="Гуламова Дильнара Эркиновна, главный врач-стоматолог",
    body=(
        split_block("Что лечим", "Современное лечение без лишнего",
                    "Подбираем методику под конкретный случай и объясняем план лечения до начала работы.",
                    ["Лечение кариеса",
                     "Эндодонтическое лечение",
                     "Лечение зубов под микроскопом взрослым и детям",
                     "Прицельный снимок зуба",
                     "Неотложная помощь для взрослых"], id_="what", ivory=True)
        + brands_block("Что входит", "Ортодонтия", "Исправляем прикус и выравниваем зубы.",
                       [("Брекеты", "Исправляют прикус и выравнивают зубы"),
                        ("Элайнеры", "Прозрачные капы для выравнивания"),
                        ("Пластинки", "Съёмные ортодонтические аппараты"),
                        ("Капы", "Защита зубов и контроль положения"),
                        ("Ретейнеры", "Удерживают результат после лечения")],
                       id_="ortho", cols=5)
        + steps_block("Этапы", "Как проходит приём", [
            ("Осмотр", "Консультация врача и осмотр. Стоит 5 000 ₸."),
            ("Диагностика", "При необходимости делаем прицельный снимок зуба."),
            ("План лечения", "Врач называет стоимость и объясняет, что и как будем делать."),
            ("Лечение", "Лечим зуб, гарантия качества на лечение."),
        ])
    ),
    doctors=["dilnara"], doctors_mode="split", doctors_title="Кто вас примет",
    prices=[("Консультация терапевта", "5 000 ₸"), ("Консультация ортодонта", "5 000 ₸"), ("Лечение", "от 30 000 ₸")],
    price_note="Точная стоимость зависит от случая и называется врачом после осмотра.",
    faq=[("Сколько стоит лечение зуба?", "Лечение начинается от 30 000 ₸. Точную стоимость врач называет после осмотра."),
         ("Лечите ли вы под микроскопом?", "Да, мы лечим зубы под микроскопом и взрослым, и детям."),
         ("Что входит в ортодонтию?", "Брекеты, элайнеры, пластинки, капы и ретейнеры."),
         ("Есть ли срочная помощь?", "Да, у нас есть неотложная помощь для взрослых. Позвоните или напишите нам в WhatsApp."),
         ("Нужна ли консультация перед лечением?", "Да, сначала врач осматривает и составляет план лечения. Консультация стоит 5 000 ₸.")],
    cta_title="Запишитесь на лечение",
    cta_text="Напишите нам в WhatsApp или позвоните, подберём удобное время.",
))

# ---------- ортопедия ----------
PAGES.append(dict(
    slug="orthopedics.html",
    crumb="Ортопедия",
    title="Ортопедия в Астане: коронки, виниры, протезирование зубов | Dinastiya Stom Clinic",
    description="Стоматологическая ортопедия в Астане: коронки, виниры и другие конструкции, восстановление зубного ряда. Коронка за 7–10 дней. Консультация ортопеда 5 000 ₸. Dinastiya Stom Clinic, пр. Туран 34Б.",
    eyebrow="Ортопедия",
    h1="Ортопедия: <em>коронки, виниры, восстановление</em>",
    lead="Восстанавливаем зубной ряд с помощью коронок, виниров и других ортопедических конструкций, чтобы результат выглядел естественно и был удобным.",
    wa="Здравствуйте! Интересует протезирование и виниры.",
    facts=[("5 000 ₸", "консультация ортопеда"), ("2", "ортопеда в команде"), ("7–10 дней", "изготовление коронки")],
    hero_kind="duo", hero_img=("img/doc-3.webp", "img/doc-2.webp"),
    hero_alt=("Жетібаев Мирас Куанышевич, хирург имплантолог-ортопед", "Хамедов Видади Адилоглы, терапевт, хирург-ортопед"),
    body=(
        split_block("Что делаем", "Эстетика и комфорт",
                    "Подбираем оптимальное решение для каждого пациента, обеспечивая эстетику и комфорт.",
                    ["Коронки",
                     "Виниры",
                     "Другие ортопедические конструкции",
                     "Восстановление зубного ряда",
                     "Восстановление на имплантах, в том числе All-on-4 / All-on-6"], id_="what")
        + steps_block("Этапы", "Как проходит лечение", [
            ("Консультация ортопеда", "Осмотр и обсуждение вариантов. Стоит 5 000 ₸."),
            ("Обследование", "Осмотр и подбор конструкции, чтобы заранее обсудить результат."),
            ("План и цена", "Подробный план лечения без скрытых доплат."),
            ("Протезирование", "Изготовление и установка конструкций."),
        ])
    ),
    doctors=["miras", "vivadi"], doctors_title="Кто вас примет",
    prices=[("Консультация ортопеда", "5 000 ₸"), ("Консультация хирурга-ортопеда", "5 000 ₸")],
    price_note="Стоимость протезирования зависит от выбранной конструкции. Её называет врач после консультации.",
    faq=[("Какой срок готовности коронки?", "Коронка готова от 7 до 10 дней."),
         ("Сколько стоит консультация ортопеда?", "Консультация ортопеда стоит 5 000 ₸."),
         ("Можно ли восстановить все зубы сразу?", "Да, для этого есть имплантация по протоколу All-on-4 / All-on-6. Подробнее на странице об имплантации."),
         ("Есть ли рассрочка?", "На имплантацию доступна беспроцентная рассрочка до 24 месяцев. По остальным услугам условия уточните у администратора.")],
    cta_title="Запишитесь к ортопеду",
    cta_text="Напишите нам в WhatsApp или позвоните, подберём удобное время.",
))

# ---------- пародонтология ----------
PAGES.append(dict(
    slug="periodontics.html",
    crumb="Пародонтология",
    title="Пародонтология в Астане: лечение дёсен | Dinastiya Stom Clinic",
    description="Пародонтология в Астане: лечение заболеваний дёсен и тканей вокруг зуба. Приём пародонтолога в Dinastiya Stom Clinic, пр. Туран 34Б.",
    eyebrow="Пародонтология",
    h1="Пародонтология: <em>здоровые дёсны</em>",
    lead="Лечим заболевания дёсен и тканей, которые удерживают зуб. Приём ведёт пародонтолог, он же терапевт и хирург.",
    wa="Здравствуйте! Хочу записаться к пародонтологу.",
    facts=[("1", "специалист: пародонтолог, терапевт, хирург"), ("снимок", "прицельный снимок зуба"), ("взрослым", "приём пародонтолога")],
    hero_kind="arch", hero_img="img/team.webp", hero_alt="Команда врачей Dinastiya Stom Clinic",
    body=(
        split_block("Что лечим", "Забота о дёснах и пародонте",
                    "Здоровые дёсны нужны и для своих зубов, и для имплантов. Врач осматривает полость рта и подбирает лечение под ваш случай.",
                    ["Консультация пародонтолога",
                     "Лечение заболеваний дёсен",
                     "Лечение тканей вокруг зуба",
                     "Прицельный снимок зуба",
                     "Хирургические вмешательства при необходимости"], id_="what")
        + steps_block("Этапы", "Как проходит приём", [
            ("Осмотр", "Врач осматривает дёсны и зубы, расспрашивает о жалобах."),
            ("Диагностика", "При необходимости делаем прицельный снимок зуба."),
            ("План лечения", "Объясняем, что и как будем лечить, и называем стоимость."),
            ("Лечение", "Проводим лечение и наблюдаем за результатом."),
        ])
    ),
    doctors=["dinmukhamed"], doctors_mode="split", doctors_title="Кто вас примет",
    prices=None,
    faq=[("Кто ведёт приём пародонтолога?", "Приём ведёт Қонарбаев Дінмұхамед Мадиұлы: пародонтолог, терапевт и хирург."),
         ("Как узнать стоимость?", "Стоимость врач называет после осмотра. Уточнить можно у администратора или в WhatsApp."),
         ("Нужна ли консультация перед лечением?", "Да, сначала врач осматривает и составляет план лечения.")],
    cta_title="Запишитесь к пародонтологу",
    cta_text="Напишите нам в WhatsApp или позвоните, подберём удобное время.",
))

# ---------- дети ----------
PAGES.append(dict(
    slug="kids.html",
    crumb="Детская стоматология",
    title="Детская стоматология в Астане | Dinastiya Stom Clinic",
    description="Детская стоматология в Астане: детский терапевт-хирург, лечение зубов под микроскопом детям. Консультация детского врача 5 000 ₸.",
    eyebrow="Детская стоматология",
    h1="Детская стоматология <em>с&nbsp;бережным подходом</em>",
    lead="Лечим пациентов всех возрастов. В клинике работает детский терапевт-хирург.",
    wa="Здравствуйте! Хочу записать ребёнка на приём.",
    facts=[("5 000 ₸", "консультация детского врача"), ("терапевт-хирург", "детский приём"), ("микроскоп", "лечение детям")],
    hero_kind="frame", hero_img="img/doc-1.webp", hero_alt="Дарцимелидзе Кирилл Окроевич, стоматолог-терапевт, хирург и детский стоматолог",
    body=(
        split_block("Направления", "Всё для здоровых зубов ребёнка",
                    "Приём ведёт детский терапевт-хирург. Лечим молочные и постоянные зубы, при необходимости проводим хирургические вмешательства и объясняем родителям каждый шаг. Бережный подход и внимание к каждому маленькому пациенту.",
                    ["Детский стоматолог-терапевт",
                     "Детский терапевт-хирург",
                     "Лечение зубов под микроскопом детям"], id_="what")
        + steps_block("Этапы", "Как проходит первый визит", [
            ("Знакомство", "Врач знакомится с ребёнком и родителями."),
            ("Осмотр", "Консультация детского врача. Стоит 5 000 ₸."),
            ("План", "Объясняем родителям, что нужно сделать, и называем стоимость."),
            ("Лечение", "Проводим лечение по согласованному плану."),
        ])
    ),
    doctors=["kirill"], doctors_mode="split", doctors_title="Кто принимает детей",
    prices=[("Консультация детского врача", "5 000 ₸")],
    price_note="Стоимость лечения называет врач после осмотра ребёнка.",
    faq=[("Вы принимаете детей?", "Да, мы лечим пациентов всех возрастов, а у нас есть детский терапевт-хирург."),
         ("Сколько стоит консультация детского врача?", "Консультация детского врача стоит 5 000 ₸."),
         ("Лечите ли вы детей под микроскопом?", "Да, лечение зубов под микроскопом доступно и взрослым, и детям.")],
    cta_title="Запишите ребёнка на приём",
    cta_text="Напишите нам в WhatsApp или позвоните, подберём удобное время.",
))


def write(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(content)


def page404():
    chips = "".join(f'<li><a href="{h}">{escape(title)}</a></li>' for h, title, _ in SERVICES)
    return f'''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Страница не найдена | Dinastiya Stom Clinic</title>
  <meta name="robots" content="noindex">
  <meta name="theme-color" content="#fbf9f4">
  <link rel="icon" href="/img/logo.webp" type="image/webp">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>

{header()}

<main>
  <section class="notfound">
    <div class="wrap notfound__in">
      <p class="notfound__code" aria-hidden="true">404</p>
      <h1>Такой страницы нет</h1>
      <p class="lead">Возможно, ссылка устарела или в адресе опечатка. Вернитесь на главную или выберите нужную услугу.</p>
      <div class="notfound__cta">
        <a class="btn btn--gold" href="/">На главную</a>
        {btn_wa("Здравствуйте! Хочу записаться на приём.", "Записаться на приём", "btn--ghost")}
      </div>
      <ul class="chips notfound__links">{chips}</ul>
    </div>
  </section>
</main>

{footer_html()}

{fab()}

<script src="/js/data.js"></script>
<script src="/js/i18n.js"></script>
<script src="/js/main.js"></script>
<script src="/js/lang.js"></script>
</body>
</html>
'''


def main():
    write("404.html", page404())
    write("orthodontics.html", f'''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>Ортодонтия | Dinastiya Stom Clinic</title>
  <meta name="robots" content="noindex">
  <link rel="canonical" href="{SITE}/therapy">
  <meta http-equiv="refresh" content="0; url=/therapy#ortho">
</head>
<body><p>Страница переехала: <a href="/therapy#ortho">Ортодонтия</a>.</p>
<script>location.replace("/therapy#ortho");</script>
</body>
</html>
''')
    for p in PAGES:
        write(p["slug"], page(p))
    idx_path = os.path.join(ROOT, "index.html")
    with open(idx_path, encoding="utf-8") as f:
        idx = f.read()
    a, b = idx.index("<!-- footer:start -->"), idx.index("<!-- footer:end -->")
    idx = idx[:a] + "<!-- footer:start -->\n" + footer_html(on_index=True) + "\n" + idx[b:]
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx)
    urls = [""] + [p["slug"][:-5] for p in PAGES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sm += f"  <url><loc>{SITE}/{u}</loc></url>\n"
    sm += "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print("готово:", ", ".join(["404.html"] + [p["slug"] for p in PAGES]))


if __name__ == "__main__":
    main()
