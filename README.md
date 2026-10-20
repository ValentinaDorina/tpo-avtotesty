# Автотесты — Лабораторная работа 9 (ТПО): CI/CD с GitHub Actions

Задача: автоматический запуск автотестов при коммите в репозиторий.
Тесты взяты из лабораторной работы № 5 — Python-аналог Postman-тестов
для публичного REST API [reqres.in](https://reqres.in/) (`requests` + `pytest`).

## Локальный запуск

```bash
pip install -r requirements.txt
pytest tests/ -v
```

## CI/CD (GitHub Actions)

Workflow описан в `.github/workflows/run-tests.yml` и запускается
на каждый push в ветку `main` и на pull request. Шаги:

1. Checkout кода (`actions/checkout@v4`);
2. Установка Python 3.11 (`actions/setup-python@v5`);
3. Установка зависимостей (`pip install -r requirements.txt`);
4. Запуск тестов (`pytest tests/ -v`).

Если все тесты проходят — в Actions горит зелёная галочка.
