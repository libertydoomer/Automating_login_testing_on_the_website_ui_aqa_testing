# Automating_login_testing_on_the_website_ui_aqa_testing

## Быстрый старт

Для корректной работы тестов и генерации отчётов требуется наличие Allure и Docker.

- [Инструкция по установке Allure](https://allurereport.org/docs/)
- [Инструкция по установке Docker](https://docs.docker.com/get-started/get-docker/)

### Установка зависимостей

1. Клонируй репозиторий:

```bash
git clone https://github.com/libertydoomer/Automating_login_testing_on_the_website_ui_aqa_testing.git
```

2. Переходим в папку с проектом:

```bash
cd Automating_login_testing_on_the_website_ui_aqa_testing
```

3. Создай виртуальное окружение:

```bash
python -m venv .venv
```

4. Установи зависимости:
```bash
pip install -r requirements.txt
```

### Запуск тестов

1. Активируй виртуальное окружение

2. Запуск тестов локально на вашем ПК:

```bash
pytest -v --alluredir=allure-results
```

3. Отобразить отчёты:

```bash
allure serve allure-results
```

4. Запуск тестов в Docker:

```bash
docker run --rm -v ${PWD}\docker-results:/allure-results login_tests
```

5. Отобразить результаты тестирования работы Docker:

```bash
allure serve docker-results
```
