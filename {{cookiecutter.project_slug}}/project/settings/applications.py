# Application definition
# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-INSTALLED_APPS

# Django native applications
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Applications from third-party packages
CONTRIB_APPS = [

]

# Custom and project own apps
CUSTOM_APPS = [
    'accounts',
]

# Global variable used by Django, contains all apps listed above
INSTALLED_APPS = DJANGO_APPS + CONTRIB_APPS + CUSTOM_APPS


# Contrib and custom apps config
# Put bellow all configurations specific to non-django applications
