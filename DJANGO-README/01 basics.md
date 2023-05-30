> - views.py is not given in project's dir, so we have to create `views.py` in our project's dir here that dir is `djangolearn`

> - after creating app we need to add app name in `project's dir -> settings .py -> INSTALLED_APP` list

> - we can create models(database tables) using `app name -> models.py` file for that we need to configer DB connection in `project's dir -> settings .py -> DATABASES` dicts
> - to connect mysql server we need to install `mysqlclient`
> - At one connection we can only connect one database then how to connect multiple  DB????

> - To create table in database we need to run migration using migration commands
> - those command will create few default tables [10] in database by default and also one which we want to create using models

> - To Store HTML files we make `templates` dir in `app dir` or in `root dir`
> - but we have to add path of `templates dir` in `project's dir -> settings.py -> TEMPLATES[list] -> DIRS'[list]` so Django know the location of out Templates

> - There is consept call `templates inheritance` which makes easy and dynamic to built site
> - we can divide HTML portions in diff HTML page and reuse that for other pages just using python templates

> - we can achieve dynamic URL by passing <`int:id`> in `project dir -> urls.py -> urlpatterns[list]` and variable is received as params by `views.py -> viewFunction`
> - passing variable can be any type but type must define in `urls.py -> urlpatterns[list]`

> - we have to create superuser here and which will give access to `ROOT-URL/admin` of django and because of that we can manipulate data using Admin penal
> - and also we can create other users with respective permission required.
> - if we do some change's in app's admin.py file then we can see data of models in admin penal.

> - Using GET and POST Request We can create Search Form, Login Logout, and Also Data or User Crate Form
> - Data Passed by GET and POST we can use in View's Function as Dicts and also based on that We can also redirect template as we want

> - we can authenticate and login logout user using `from django.contrib.auth import (authenticate,login,logout)` as Django's `/admin` users for our project
> - we return django shortcut `redirect('URL')` when want to redirect user to other relevant page
> - and also we can redirect page when we submit form with GET and POST Dict Data but There is  in both redirection .

> - Django Template have Access of few Classes [debug, request, auth, messages] which we can see at `settings.py -> TEMPLATES[LIST] -> OPTIONS`
> - using that we can check that user is authenticated or not this classes also can be used in view functions 
> - if we check authentication in view function then for every view function related to that template we have to check for authentication condition but in Template we need to check for that only ones.

> - `from django.contrib.auth.decorators import login_required` @decorator is also used for views when it is required login before accessing that view or Hitting URL
> - after using that decorator if we try to Hit this decorated URL/view without login, user will redirect to LOGIN page and for that we have to SET that in `settings.py` as `LOGIN_URL[str]` otherwise it will redirect user to default django LOGIN_URL
> - There are other settings related to LOGIN_URL search in `Django Documentation`

> - We can directly create LOGIN form without writing HTML fild with help of `from django import forms`
> 1. create `form.py` in respective app and import `django.form`
> 2. By Inheriting `forms.ModelForm` to any class we can replicate Model's fild as Form, and by handelling this calls in view we can create form in which we do not have to save data in Models it will do automatically.
> 3. By Inheriting `forms.Form` to any class we can create fild using python and by handdeling this class in view we need to push data in database 
> - we can see both process in `fisrtapp->forms.py` and `firstapp->views.py`
> - we can see that in `fisrtapp->forms.py->forms.Form` we have created inner class `Meta` to get info's and `clean` function to clean data coming from HTML_FORM 
> - `clean` function is also we can create in `forms.ModelForm` if needed

> - Django has inbuilt form for Authentication and UserCreation, we can use by `from django.contrib.auth.forms import UserCreationForm, AuthenticationForm`
> - we can see that in `accounts->views.py` we have implementation HTML and Django form 
> - Not Working as expected
 
> - `.env` is file to keep environment variable which should not define in code 
> - after installing `django-dotenv` module we can access `.env` variables 
> - to import and read `.env` we have to `dotenv.read_dotenv()` write in `manage.py` file

> - with help of `python manage.py test` we can run `test.py` files which we have to create in `MainApp` Folder 
> - test is important to create to check necessary conditions before making it public.
> - 