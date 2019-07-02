# Quick-start development settings - unsuitable for production
# https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

from .base import os, BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "{{cookiecutter.secret_key}}"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# User uploaded files - not suitable for production!
# https://docs.djangoproject.com/en/2.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")
