# Проект "Blogicum v. 2.0"
Реализация социальной сети **Blogicum**. 

Основные возможности:
- чтение публикаций. 

Проект является учебным. Основная польза в приобретении понимания реализации проекта через фреймворк `Django`, а именно: 
- базовые описаны в - [Blogicum v. 1.0](https://github.com/Furturnax/django_sprint1);
- описание моделей;
- создание базы данных на основе созданных моделей;
- загрузка готовых фикстур в базу данных;
- регистрация и настройка панели администратора;
- настройка `ORM` запросов. 

<br>

## Технологический стек:
- Python 3.11.5
- Django 3.2.16
- SQLite
- Pytest 7.1.3

<br>

## Как запустить проект :shipit: :
+ Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:Furturnax/django_sprint3.git
```

```bash
cd django_sprint3/
```

+ Cоздать и активировать виртуальное окружение (Windows/Bash):
```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

+ Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

+ Перейти в директорию с manage.py:
```bash
cd blogicum/
```

+ Выполнить миграции:
```bash
python manage.py migrate
```

+ Загрузить фикстуры:
```bash
python manage.py loaddata db.json
```

+ Запустить проект:
```bash
python manage.py runserver
```

<br>

## Просмотр контента:
Перейти по адресу http://127.0.0.1:8000/. На данный момент доступно несколько записей, загруженных из фикстуры в базу данных. 

<br>

## Доступ к панели администратора:
Зарегистрировать пользователя через Admin-panel.
+ Перейти в директорию с manage.py:
```bash
cd blogicum/
```

+ Создать пользователя-администратора:
```bash
python manage.py createsuperuser
```

+ Перейти по адресу http://127.0.0.1:8000/admin/ и ввести данные пользователя-администратора.
Через панель администратора можно создавать публикации, категории, местоположение, группы пользователей и всем этим управлять в одном месте. 

<br>

## Тестирование проекта:
Тестирование реализовано с использованием библиотеки Pytest. 

+ Запустить тесты из основной директории проекта:
```bash
pytest
```

<br>

## Авторство
Автор проекта - Yandex Practicum | [GitHub](https://github.com/yandex-praktikum)

Разработчик - Andrew Fedorchenko | [GitHub](https://github.com/Furturnax) [Telegram](https://t.me/furturnax)

Ревьюер - Evgeniy Salahutdinov | [GitHub](https://github.com/EugeneSal)
