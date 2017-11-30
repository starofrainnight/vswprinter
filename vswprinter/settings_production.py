"""
Production django settings for vswprinter project.

You could simply run a http server by follow command:

DJANGO_SETTINGS_MODULE="vswprinter.settings_production" python manage.py runserver 0.0.0.0:8000

"""

from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
