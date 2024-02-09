"""
this assets of settings will be userd if DEBUG=True
to make this working, logic of manage.py are changed, same for production.py"""

from .base import *
# from django.core.management.utils import get_random_secret_key


ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

