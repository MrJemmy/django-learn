- If project is in Debug mode `[Debug=True]`, then django will serve static files.
- otherwise it will give admin panel without CSS

> - static
>   - app name
>     - css
>       - base-file.css

> - app name
>   - static
>     - app name
>       - css
>         - base-file.css

> ```bash
>  python manage.py collectstatic
> ```
> This command is use for collecting static files, for that we need to have set `STATICFILES_DIRS`, `STATIC_ROOT`
> this will create folder with same name we have given to `STATIC_ROOT` Variable in settings.py
> and all static files will be stored there

> If we want to store out static files and media file to spacefy storage in server then for configurations we can use video 75 Try Django  