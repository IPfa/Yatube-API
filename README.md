# Yatube-API
REST API for web application Yatube written on Python. This is a continuation of Yatube project (https://github.com/IPfa/Yatube). Yatube was developed using HTML rendering and CSS. Modern approach consists of separating frontend and backend of web application. Backend is an API in such case. Yatube-API is an learning project corresponding to this approach. API has exactly the same functionallity as Yatube. Djoser library was used as a solution for new users creation and authentication.

# Technology Stack
Python, Django, Django REST, SQLite, Djoser.

# Launching
Create Python environment.
```
python3.7 -m venv venv
```
Start Python environment.
```
source venv/bin/activate
```
Perform migrations.
```
python3 manage.py migrate
```
Run the project.
```
python3 manage.py runserver
```
For static files collection and creating of superuser perform following commands.
```
python3 manage.py collectstatic
python3 manage.py createsuperuser
```
**Project is available on:**
http://127.0.0.1:8000/

# Authors
[IPfa](https://github.com/IPfa)