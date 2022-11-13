#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import dotenv
import sys
from djangolearn.settings import BASE_DIR


def main():
    """Run administrative tasks."""
    DOT_ENV_PATH = BASE_DIR / '.env'
    if DOT_ENV_PATH.exists():
        dotenv.read_dotenv()
    else:
        print('-'*40)
        print('-> PLEASE setup .env File 1st')
        print('-'*40)
        return

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangolearn.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
