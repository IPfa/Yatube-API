## api_final
api_final

# Описание
Програмный интерфейс (API) написанный для web-приложения Yatube.

# Установка

Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone https://github.com/IPfa/api_final_yatube.git
```

```sh
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```sh
python3 -m venv env
```

```sh
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

Выполнить миграции:

```sh
python3 manage.py migrate
```

Запустить проект:

```sh
python3 manage.py runserver
```

# Примеры запросов

http://127.0.0.1:8000/api/v1/posts/ GET

```sh
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2019-08-24T14:15:22Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

http://127.0.0.1:8000/api/v1/groups/ GET

```sh
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
