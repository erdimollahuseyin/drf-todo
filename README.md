# Build a Django RESTful API 

Together, we’re going to build the back-end for a “To Do” application. 
We write and deploy a RESTful API service. 
The APIs allow you to Create, Read, Update, and Delete (CRUD) a task. 
The tasks are stored in a database and we’re using the Django ORM (Object Relational Mapping) 
to deal with the database management.

## Setup

create a Python 3 virtual environment.

```bash
$ mkdir todoapp
$ cd todoapp
$ python3 -m venv .venv
$ source .venv/bin/activate
```

install the dependencies.

```bash
(.venv)$ pip install djangorestframework django
```

[DRF(Django REST Framework)](https://www.django-rest-framework.org)  is a framework that create RESTful CRUD APIs and gives useful features.

## Create the Django project and application

```bash
$ django-admin startproject todo_app
```

create the app in project.

```bash
$ cd todo_app
$ django-admin startapp todo
```

Let’s add `rest_framework` and todo to the list of `INSTALL_APPS` in the project’s `settings.py`.

```
todoapp/todo_app/settings.py
```

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'todo',
]
```

## Model and Database

By default, Django uses the SQLite database management system.

`todo_app/todo/models.py:`

```python
from django.db import models

class Task(models.Model):
    STATES = (('todo', 'To Do'), ('in progress', 'In Progress'), ('done', 'Done'))
    title = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=4, choices=STATES, default='todo')

```

Now create the database migration script that Django uses to update the database with changes.

```bash
python manage.py makemigrations
```

Then you can apply the migration to the database.

```bash
python manage.py migrate
```

## Access to the data

### Creating a Serializer

Serializers are used to deserialize JSON or other content types into the data structure defined in the model.

Let’s add our TaskSerializer object by creating a new file in the project `todo_app/todo/serializers.py:`

```python
from rest_framework.serializers import ModelSerializer
from todo.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

```

We’re using the generic ModelSerializer from DRF,
to automatically create a serializer with the fields that correspond to our Task model.


### Creating a View

The ModelViewSet provides the following actions on a data model: list, retrieve, create, update, partial update, and destroy.

Let’s add our view to `todo_app/todo/views.py`:

```python
from rest_framework.viewsets import ModelViewSet

from .models import Task
from .serializer import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

```

### Creating a Router

The DRF `DefaultRouter` takes care of mapping actions to HTTP Method and URLs.
Add the following to `todo_app/urls.py:`

```python
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from todo.views import TaskViewSet

router = DefaultRouter()
router.register(r'todo', TaskViewSet)

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^api/', include((router.urls, 'todo'))),
]

```
we’re mapping all the router URLs to the /api endpoint. 
DRF takes care of mapping the URLs and HTTP methods(list, retrieve, create, update, destroy).


## Running the application

```python
python manage.py runserver
```

- Now we can access the application at the following URL: `http://127.0.0.1:8000/api/`

- listing or creating tasks, using the following URL: `http://127.0.0.1:8000/api/todo`

- updating/deleting an existing tasks with this URL: `http://127.0.0.1:8000/api/todo/1`

## Conclusion

In this article you’ve learned how to create a basic RESTful API using the Django REST Framework.







