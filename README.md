# Атестаційне завдання — GitHub Actions

[![1. Pytest](https://github.com/USER/REPO/actions/workflows/01-pytest.yml/badge.svg)](https://github.com/USER/REPO/actions/workflows/01-pytest.yml)
[![2. Lint](https://github.com/USER/REPO/actions/workflows/02-lint.yml/badge.svg)](https://github.com/USER/REPO/actions/workflows/02-lint.yml)
[![3. Multi-version](https://github.com/USER/REPO/actions/workflows/03-multi-version.yml/badge.svg)](https://github.com/USER/REPO/actions/workflows/03-multi-version.yml)
[![4. Docker](https://github.com/USER/REPO/actions/workflows/04-docker.yml/badge.svg)](https://github.com/USER/REPO/actions/workflows/04-docker.yml)
[![5. HTML Report](https://github.com/USER/REPO/actions/workflows/05-html-report.yml/badge.svg)](https://github.com/USER/REPO/actions/workflows/05-html-report.yml)

Проєкт демонструє п'ять сценаріїв CI/CD на GitHub Actions для невеликого Python-пакета з калькулятором та рядковими утилітами.

## Структура

```
.
├── src/
│   ├── __init__.py
│   ├── calculator.py      # Калькулятор з історією
│   └── string_utils.py    # Утиліти для рядків
├── tests/
│   ├── test_calculator.py    # 20 тестів
│   └── test_string_utils.py  # 26 тестів
├── .github/workflows/
│   ├── 01-pytest.yml          # Завдання 1
│   ├── 02-lint.yml            # Завдання 2
│   ├── 03-multi-version.yml   # Завдання 3
│   ├── 04-docker.yml          # Завдання 4
│   └── 05-html-report.yml     # Завдання 5
├── main.py
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
└── .flake8
```

## П'ять реалізованих задач

### 1. Автоматичне тестування з Pytest (`01-pytest.yml`)
Запускає 46 тестів на Ubuntu з Python 3.12 при кожному push та pull request. Тести використовують fixtures, parametrize і організовані по класах.

### 2. Перевірка стилю коду — Linting (`02-lint.yml`)
Перевіряє код двома інструментами: **flake8** (стиль PEP 8) і **black** (форматування у режимі `--check`).

### 3. Мультиверсійне тестування (`03-multi-version.yml`)
Матриця 4 × 3 = **12 комбінацій**: Python 3.9 / 3.10 / 3.11 / 3.12 на Ubuntu / Windows / macOS. `fail-fast: false`, тому одна помилка не зупиняє решту.

### 4. Збірка Docker-контейнера (`04-docker.yml`)
- Налаштовує Docker Buildx;
- Збирає образ з кешуванням шарів через `type=gha`;
- Запускає контейнер для перевірки, що `main.py` коректно стартує.

### 5. Автоматичний HTML-звіт (`05-html-report.yml`)
- Генерує HTML-звіт через `pytest-html` + звіт покриття через `pytest-cov`;
- Зберігає як артефакт workflow на 30 днів;
- Публікує на **GitHub Pages** (живе посилання після першого успішного запуску).

## Як запустити локально

```bash
# Встановлення dev-залежностей
pip install -r requirements-dev.txt

# Тести
pytest -v

# Лінтинг
flake8 src tests main.py
black --check src tests main.py

# HTML-звіт
pytest --html=report.html --self-contained-html --cov=src --cov-report=html

# Docker
docker build -t atestation-app .
docker run --rm atestation-app
```

## Налаштування GitHub Pages

Щоб workflow №5 запрацював:
1. Settings → Pages → Source: **GitHub Actions**.
2. Після push на `main` workflow автоматично опублікує звіт.
3. Посилання з'явиться у вкладці Actions → конкретний run → Deploy job.

## Результати локальної перевірки

- ✅ 46 тестів пройдено
- ✅ flake8 без зауважень
- ✅ black без зауважень
- ✅ покриття згенеровано
