# PNID — CI/CD Pipeline

[![CI](https://github.com/Ihor-Sl/PNID/actions/workflows/ci.yml/badge.svg)](https://github.com/Ihor-Sl/PNID/actions/workflows/ci.yml)

Проєкт використовує єдиний файл `.github/workflows/ci.yml` із 6 джобами.

## Структура пайплайну

```
push / pull_request / workflow_dispatch
│
├── 1 · lint ─────────────────────────────────────────┐
│         │                                            │
│         ├── 2 · test ──── 4 · docker-build          │
│         │         └───── 5a · generate-report        │
│         │                        └── 5b · deploy-pages
│         │
│         └── 3 · test-matrix  (3 ОС × 4 версії Python)
```

> `generate-report` та `deploy-pages` не запускаються на `pull_request` — деплой тільки з `main`/`master`.

---

## Джоби

### 1 · Lint — перевірка стилю коду

**Тригер:** будь-який push / PR  
**Залежності:** немає (запускається першим)

| Інструмент | Версія | Що перевіряє |
|-----------|--------|--------------|
| `flake8`  | 7.1.1  | PEP 8, синтаксичні помилки |
| `black`   | 24.10.0 | Форматування коду (`--check`) |

Перевіряються: `src/`, `tests/`, `main.py`

---

### 2 · Pytest — автоматичне тестування

**Тригер:** після успішного `lint`  
**Python:** 3.12 / ubuntu-latest

Запускає повний набір тестів із детальним виводом:
```bash
pytest -v --tb=short
```

---

### 3 · Multi-version — матричне тестування

**Тригер:** після успішного `lint` (паралельно з `test`)  
**Матриця:** 3 ОС × 4 версії = **12 джобів**

| ОС | Python |
|----|--------|
| ubuntu-latest | 3.9 |
| windows-latest | 3.10 |
| macos-latest | 3.11 |
| | 3.12 |

`fail-fast: false` — усі комбінації завершуються незалежно одна від одної.

---

### 4 · Docker — збірка контейнера

**Тригер:** після успішного `test`  
**Що робить:**
- Збирає образ `atestation-app:latest` через Docker Buildx
- Використовує GitHub Actions Cache (`type=gha`) для прискорення повторних збірок
- Перевіряє запуск контейнера (`docker run --rm`)
- `push: false` — образ не публікується в registry

---

### 5 · HTML-звіт → GitHub Pages

**Тригер:** після успішного `test`, тільки на `push` (не на PR)

**5a `generate-report`** — генерує звіт:
```bash
pytest --html=public/index.html --self-contained-html \
       --cov=src --cov-report=html:public/coverage
```

**5b `deploy-pages`** — публікує папку `public/` на GitHub Pages.

Звіт доступний за адресою:  
**https://ihor-sl.github.io/PNID/**

---

## Налаштування GitHub Pages (одноразово)

Перед першим деплоєм необхідно увімкнути Pages вручну:

1. Відкрити **Settings → Pages**
2. У полі **Source** обрати **GitHub Actions**
3. Зберегти

> Без цього кроку `deploy-pages` повертає помилку 404.

---

## Локальний запуск

```bash
# Встановлення залежностей
pip install -r requirements-dev.txt

# Тести
pytest -v --tb=short

# Лінтинг
flake8 src tests main.py
black --check src tests main.py

# HTML-звіт локально
pytest --html=report.html --self-contained-html --cov=src --cov-report=html:coverage
```

---

## Структура файлів

```
.
├── .github/
│   └── workflows/
│       └── ci.yml          # єдиний CI файл (6 джобів)
├── src/                    # вихідний код
├── tests/                  # тести
├── main.py
├── requirements-dev.txt    # pytest, flake8, black, pytest-html, pytest-cov
└── Dockerfile
```