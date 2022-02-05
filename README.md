# Yatube-API

REST API веб приложения Yatube написанный на Python. Изначально было создано веб приложение Yatube. Его можно найти в списке моих репозиториев. Приложение написано на связке Django и Python без использования современного фронтенда. В основе лежит рендеринг HTML страниц и использование CSS. Далее в качестве развитися проекта был написан этот API.

# Стек Технологий
Python, Django, Django REST, SQLite.

# Запуск
Развернуть виртуальное окружение.
```
python3.7 -m venv venv
```
Запустить виртуальное окружение.
```
source venv/bin/activate
```
Установить зависимости.
```
pip install -r requirements.txt
```
Перейти в папку Yatube_api и запустить проект.
```
python3 manage.py runserver
```
Команды для сбора статики, выполнения миграций и создания суперпользователя.
```
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py createsuperuser
```
**Проект доступен по адресу:**
http://127.0.0.1/

# Авторы
[IPfa](https://github.com/IPfa)