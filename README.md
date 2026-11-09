# Dinastiya Stom Clinic

Сайт стоматологии Dinastiya Stom Clinic (Астана, пр. Туран 34Б). Чистые HTML, CSS и JS, на сервере сборка не нужна.

## Структура

- `index.html` — главная страница (правится вручную)
- `implantation.html`, `orthodontics.html`, `therapy.html`, `orthopedics.html`, `kids.html` — страницы услуг, **создаются генератором**, руками не править
- `tools/build.py` — генератор страниц услуг, а также `sitemap.xml` и `robots.txt`
- `css/style.css` — стили
- `js/data.js` — контакты, отзывы, врачи на главной
- `js/main.js` — меню, анимации, форма заявки в WhatsApp
- `img/` — логотип и фотографии

## Как менять страницы услуг

Тексты, цены, вопросы и врачи страниц лежат в `tools/build.py` (список `PAGES` и словарь `DOCTORS`).
После правок запустить из корня репозитория:

```
python3 tools/build.py
```

и закоммитить получившиеся `.html`, `sitemap.xml` и `robots.txt`.

## Запуск локально

```
python3 -m http.server 8000
```

Открыть http://localhost:8000

## Что где менять

- отзывы: `js/data.js`, массив `reviews`
- врачи на главной: `js/data.js`, массив `team` (врачи на страницах услуг: `tools/build.py`, `DOCTORS`)
- график работы: `js/data.js`, поле `hours`
- цены на главной: блок `#prices` в `index.html`
