# Getting Started with Django

[Django](https://www.djangoproject.com) is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Other alternatives to Django are [Flask](https://flask.palletsprojects.com/en/2.2.x/) or [CherryPy](https://docs.cherrypy.dev/en/latest/).

The goal in this section is to create a webapp using Django and your browser.

## Installation

```bash
pyenv global tutoring
python -m pip install Django
python -m django --version
```

## Create project

```bash
pip install django-admin-cli
django-admin startproject uppercase .
```

This creates `manage.py` and a directory `/learning_log`.

- `manage.py`: A command-line utility that lets you interact with this Django project. More info [here](https://docs.djangoproject.com/en/4.1/ref/django-admin/).
  - `/learning_log` directory:
  - `mysite/__init__.py:`: empty file that tells Python that this directory should be considered a Python package. More about package [here](https://docs.python.org/3/tutorial/modules.html#tut-packages).
  - `mysite/settings.py`: Settings/configuration for this Django project
  - `mysite/urls.py`:  The URL declarations for this Django project
  - `mysite/asgi.py`: An entry-point for ASGI-compatible (Asynchronous Server Gateway Interface) web servers to serve your project.
  - `mysite/wsgi.py`:  An entry-point for WSGI-compatible (Web Server Gateway Interface) web servers to serve your project.

## Deploy Server on your local machine

```bash
python manage.py runserver
```

>Ignore the warning about unapplied database migrations for now.

now you can hit  http://127.0.0.1:8000/

## Create App

Django comes with a utility that automatically generates the basic directory structure of an app.

```bash
cd mysite
python manage.py startapp uppercase
```

1. Go to `uppercase/views.py` and paste:

```python
from django.http import HttpResponse


def to_upper_case(request, name: str):
    return HttpResponse(name.upper())
```

This is what we want to execute and return when we hit the endpoint.

2.Go to `uppercase/urls.py` and paste (create the files if it does not exist):

```python
from django.urls import path

from . import views


urlpatterns = [
    path('', views.to_upper_case, name='index'),
]
```

3. Go to `mysite/urls.py` and paste:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('uppercase/<str:name>/', include('uppercase.urls')), # str: is not required since str is the default
    path('admin/', admin.site.urls),
]
```

now we can run the server again with `python manage.py runserver` and hit the endpoint http://127.0.0.1:8000/uppercase/john/

### Exercises

1. Create `sports` app that with the following features, given a list of sports `sports = ['football', 'basketball', 'tennis', 'rugby']`:
   1. GET endpoint `/api/sports/{int:index}` that returns the value for the given index in uppercase.
   2. DELETE endpoint `/api/sports/{int:index}` that deletes a sport value at the given index.
