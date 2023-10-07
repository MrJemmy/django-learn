## SIGNALS
- to config signals 
```bash
    # go in apps.py file in APP to config signal 
    class AppnameConfig(AppConfig):
        name = 'Appname'
        def ready(self):
            import Appname.signal_file
    # go in __init__.py file in APP and set variable 
    default_app_config = 'Appname.apps.AppnameConfig'  # AppnameConfig class name in apps.py
    # instead on declaring 'default_app_config' variable
    # in settings.py -> INSTALLED_APPS ->  'Appname.apps.AppnameConfig' this stad of only Appname
```

- How signals will called
```bash
    def receiver_function(sender, **kwargs):
        pass
    # using connector 
    signal_name.connect(receiver_function, sender=None, weak=True, dispatch_uid=None) # weak=True, dispatch_uid=None optional
    
    # using Decorator 
    @receiver(signal_name or list of signal_name, sender=ModleName) # sender can be any thing 
    def receiver_function(sender, **kwargs): # **kwargs could be diff params for diff signals 
        pass
```
- sender : we can specific sender
- weak : ?
- dispatch_uid : unique dispatch id


### Builtin Signals
#### Loging and Logout Signals
- user_logged_in(sender, request, user)
  - sender : The class of the user that just logged in 
  - request : current HttpRequest instance
  - user : USER Instance 
- user_logged_out(sender, request, user)
  - sender : The class of the user that just logged out or None if user was not authenticated  
  - request : current HttpRequest instance
  - user : USER Instance or None if user was not authenticated  
- user_login_failed( sender, credentials, request)
  - sender : The name of module used for authentication
  - credentials : a dictionary of user credentials using authentication failed
  - request : current HttpRequest instance


#### Model Signals
- pre_init(sender, *args, *kwargs)
  - when django model will instantiate, signal will send before `__init__()` method start
  - sender : modal class that just had instantiate 
  - args : argument passed to `__init__()`
  - kwargs : dictionary  passed to `__init__()`

- post_init(sender, instance)
  - when django model will instantiate, signal will send after `__init__()` method finish
  - sender : modal class that just had instantiate 
  - instance : instance of model just created 

- pre_save(sender, instance, raw, using, updated_fields) `# raw, using, updated_fields this are not mandatory`
  - send before models save() method
  - sender : model class
  - instance : instance being saved
  - raw : ?
  - using : database alias/given_name 
  - updated_fields : fields to update as passed to save(), or None if not passed.

- post_save(sender, instance, created, raw, using, updated_fields)  `# raw, using, updated_fields this are not mandatory`
  - send before models save() method
  - sender : model class
  - created : True if instance hase created otherwise False
  - instance : instance being saved
  - raw : ?
  - using : database alias/given_name 
  - updated_fields : fields to update as passed to save(), or None if not passed.

- pre_delete(sender, instance, using) `# using is not mandatory`
  - send before instance delete() method
  - sender : model class
  - instance : instance that will delete 
  - using : database alias/given_name 

- post_delete(sender, instance, using) `# using is not mandatory`
  - send after instance delete() method
  - sender : model class
  - instance : instance that deleted 
  - using : database alias/given_name 
  - Here this object will no longer will be in database.

- m2m_changed(sender, instance, action, reverse, model, pk_set_using)
  - sent when many to many fild is changed on model instance.
  - ?

- class_prepared(sender)
  - sent when django models class is registered in django 


#### Request/Response Signals
- request_started(sender, environ)
  - sender : Handler class : WsgiHandler
  - environ : dictionary values provided in request
- request_finished(sender)
  - sender : Handler class
- got_request_exception(sender, request)
  - sender : always None
  - request : HttpRequest object
  - which kind of exception it can handel 
    - program exception
    - ?(test) request url not found


#### management signals : sent by Django Admin
- pre_migrate(sender, app_config, verbosity, interactive, using, plan, apps)
  - this will send when we call migrate command
  - sender : AppConfig class Instance which is in apps.py file
  - app_config : AppConfig Instance same as sender 
  - verbosity : how much info manage.py is printing in terminal
  - interactive : if true then safe to input values in terminal, if False then function should not try to listen values from terminal
  - using : database alias/given_name 
  - plan : it is tuple of 2 values (1st item is instance of migration class, 2nd itme rolled back (True/False)), this is migration plan will going to run in migration
  - apps : an instance of APP contain state of project before migration run

- post_migrate(sender, app_config, verbosity, interactive, using, plan, apps)
  - this will send after execution of migrate command
  - same as abow


#### Test Signals 
- setting_changes(sender, setting, value, enter)
  - ?


#### database wrappers
- django.db.backends.signals
  - connection_created : sent when DB wrapper makes initial connection with DataBase
    - helpful when want to send any post connection commands to SQL
  - sender : The Database wrapper class
  - Connection : DB connection that was open 