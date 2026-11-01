# Вариант 3

Этот проект содержит реализацию 12 практик варианта 3. Копии пользовательских Word-отчетов находятся в reports пакета для сдачи; реальные результаты — в results. Все команды, кроме сборки Docker, выполняются из корня этого варианта.

## Подготовка

Установить Python 3.12 и Microsoft Edge. Создать окружение: python -m venv .venv. В Windows cmd активировать .venv\Scripts\activate.bat; в PowerShell использовать .venv\Scripts\Activate.ps1. Если активация недоступна, выполнять .venv\Scripts\python.exe напрямую. В Linux/macOS: source .venv/bin/activate. Затем установить python -m pip install -r requirements.txt.

Для ручного просмотра формы: python -m web.portal, затем http://127.0.0.1:5050/join. Начальная учетная запись demo@example.com / ValidSecret2026. Тесты создают собственный сервер на свободном порту.

## Запуск по номерам

### Практика 1

```console
python -m lab01.search "Software testing"
python -m lab01.search "Python programming"
```

### Практика 2

```console
python -m pytest lab02 -v -s
```

### Практика 3

```console
python -m pytest lab03 -v
```

### Практика 4

```console
python -m unittest lab04.test_unittest_enrollment -v
```

### Практика 5

```console
python -m pytest lab05 -v
```

### Практика 6

```console
python -m pytest lab06 -v
```

### Практика 7

```console
python -m pytest lab07 -v --html=artifacts/browser.html --self-contained-html
```

### Практика 8

```console
cd lab08
docker build -t practice-tests .
docker run --name practice-tests-run practice-tests
```

### Практика 9

```console
python -m lab09.measure
```

### Практика 10

```console
python -m pytest lab10 -v
```

### Практика 11

```console
python -m behave lab11/features
```

### Практика 12

```console
python -m pytest lab12 -v
```

## Структура и подтверждения

Файлы __init__.py пустые: это маркеры пакетов Python. В lab08 действительно лежат Dockerfile, module.py, test_module.py и requirements.txt. Для сборки сначала перейти в lab08; затем вернуться в корень командой cd .. В lab11 папка features содержит сценарий, а features/steps содержит реализацию шагов.

Для №6 и №7 разместить содержимое этого варианта в корне отдельного GitHub репозитория. Каталог .github/workflows должен остаться непосредственно в корне. Проверить Actions при push и pull request. В №6 включить уведомления Actions в своем аккаунте, продемонстрировать ошибочный запуск и исправление. Workflow автоматически сохраняют отчеты.

Для №8 выполнить сборку, правильный запуск, запуск с временно неверным ожидаемым значением и повторную сборку после исправления. Код завершения: docker inspect practice-tests-run --format="{{.State.ExitCode}}". Перед повторным запуском с тем же именем удалить остановленный контейнер: docker rm practice-tests-run.

В №1 внешний сайт может показать согласие или CAPTCHA. Их необходимо обработать вручную, а при изменении разметки уточнить локатор. Для другого запроса использовать аргументы команды.

В №9 смешивание implicit и explicit в одной сессии не применяется. Поле ok=False для неявной проверки изменения состояния является наблюдаемым ограничением этого механизма. Это не успешное ожидание. Сравнивать время следует вместе с достижением условия.

В браузерных pytest сценариях общая фикстура сохраняет изображение перед закрытием окна в artifacts/. unittest использует собственные ресурсы: необходимые изображения фиксируются при ручном просмотре формы или добавлением save_screenshot перед закрытием. Журнал регистрации также находится в artifacts/.

Копии пользовательских Word-отчетов находятся в ../reports. В них изменяются только места для изображений; остальные текст, подписи и оформление сохраняются. Неподтвержденные проверки и расхождения указаны в ../STATUS.md.

Актуальные журналы, CSV, XML, HTML и снимки находятся в ../results пакета для сдачи. Статус отдельных проверок указан в ../STATUS.md. Наличие workflow само по себе не подтверждает его реальный запуск.


## Локальный запуск Edge и Chrome в CI

Локально функция support.browser.chrome() сохраняет прежнее имя для совместимости, но по умолчанию запускает Edge. BROWSER=edge или BROWSER=chrome явно выбирает браузер. В CI используется Chrome; workflow e2e.yml явно задаёт BROWSER=chrome и HEADLESS=1. EDGE_DRIVER при необходимости задаёт полный путь к msedgedriver.exe, иначе драйвер подбирает Selenium Manager. Для фонового локального запуска задать HEADLESS=1.

Актуальный статус практик см. в ../STATUS.md; журналы, CSV и снимки — в ../results. Старые verification/ и шаблоны word_reports/ из исходной папки в пакет для сдачи не включены.
