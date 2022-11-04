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