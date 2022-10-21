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