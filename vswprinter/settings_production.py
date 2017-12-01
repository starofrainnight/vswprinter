"""
Production django settings for vswprinter project.

You could simply run a http server by follow command:

DJANGO_SETTINGS_MODULE="vswprinter.settings_production" python manage.py runserver 0.0.0.0:8000

"""

import os.path
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# WhiteNoise must work with STATIC_ROOT setting!
# It must not defined inside debug setttings, otherwise django will complain
# that STATIC_ROOT must not inside STATICFILES_DIRS.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
