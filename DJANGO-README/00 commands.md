#### To Create Project `[at the end of command with '.' create project in currunt dir]`
```bash
  python -m django startproject projectname
  python -m django startproject projectname .
```
#### To start Django server
```bash
  python manage.py runserver
```
#### To Create Application
```bash
  python manage.py startapp appname
```
#### To Do migrations
```bash
  python manage.py makemigrations
  python manage.py migrate
```
#### To Use/Access Django Models data in shell
```bash
  python manage.py shell
```
#### To Create superuser of project 
```bash
  python manage.py createsuperuser
  username : 
  Email Address :
  Password : 
  Password (again): 
```
##### To gerenare SECURE_KEY 
```bash
  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())
```
##### Importing From Pycharm Environment variables and from .env file both are SAME[Need Resurch]
NOTE : The .env file should be in the same directory as settings.py
```bash
  import environ
  env = environ.Env()
  environ.Env.read_env()
  env("KEY")
```