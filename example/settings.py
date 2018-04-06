"""
Django settings for example project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v70yjf=f-h=8*sesl0$6j(lq9a9ux7((pvl@6y1=d86m)kz6ei'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'example.autocompletionexample',
    'example.demo',
    'tags_input',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.sqlite3'),
    },
    'other': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'other_database.sqlite3'),
    },
}
DATABASE_ROUTERS = 'example.db_router.Router',


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


def get_queryset(*args, **kwargs):
    from example.autocompletionexample import models
    return models.Spam.objects.all()

TAGS_INPUT_MAPPINGS = {
    'demo.SimpleName': {'field': 'name', 'create_missing': True},
    'demo.DoubleName': {'fields': ('name_a', 'name_b')},
    'demo.ManyToManyToDoubleName': {'field': 'name', 'create_missing': True},
    'demo.ErrorName': {'field': 'name', 'create_missing': True},
    'demo.ForeignKeyToSimpleName': {'field': 'name', 'create_missing': True},
    'demo.ManyToManyToSimpleName': {'field': 'name', 'create_missing': True},
    'demo.ManyToManyToError': {'field': 'name', 'create_missing': True},
    'demo.ThroughModel': {'field': 'name', 'create_missing': True},
    'demo.ManyToManyThrough': {'field': 'name', 'create_missing': True},
    'demo.InlineModel': {'field': 'name', 'create_missing': True},
    'autocompletionexample.Foo': {'field': 'name', 'create_missing': True},
    'autocompletionexample.Bar': {'field': 'name'},
    'autocompletionexample.Spam': {'field': 'name', 'queryset': get_queryset},
    'autocompletionexample.Egg': {'fields': ('name', 'name2')},
}

TAGS_INPUT_INCLUDE_JQUERY = True

ALLOWED_HOSTS = (
    'localhost',
    '127.0.0.1',
)

