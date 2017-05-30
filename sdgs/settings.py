"""
Django settings for sdgs project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from .utils import str_to_bool

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    import dotenv
    dotenv.read_dotenv(os.path.join(BASE_DIR, ".env"))
except ImportError:
    pass


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'sztug!hpjf_(7s0nmcn410t0h6esqn4246&34$4ri%vx+g2moz')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str_to_bool(os.environ.get('DEBUG', 'False'))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split()

INTERNAL_IPS = os.environ.get('INTERNAL_IPS', '127.0.0.1').split()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'import_export',
    'rest_framework',
    'goals',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sdgs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sdgs.context_processors.site',
            ],
        },
    },
]

WSGI_APPLICATION = 'sdgs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DATABASE_NAME', 'sdgs'),
        'USER': os.environ.get('DATABASE_USER', 'sdgs'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'sdgs'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'CONN_MAX_AGE': int(os.environ.get('DATABASE_CONN_MAX_AGE', 0))
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-us')

TIME_ZONE = os.environ.get('TIME_ZONE', 'Africa/Dar_es_Salaam')

USE_I18N = str_to_bool(os.environ.get('USE_I18N', 'True'))

USE_L10N = True

USE_TZ = str_to_bool(os.environ.get('USE_TZ', 'True'))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL =  os.environ.get('STATIC_URL', '/static/')

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static_root'))

MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media_root'))

# Site

SITE_NAME = os.environ.get('SITE_NAME', 'SDGs')

SITE_API_NAME = os.environ.get('SITE_API_NAME', 'SDGs API')

SITE_API_URL = os.environ.get('SITE_API_URL', '/api/')

ADMIN_SITE_TITLE = os.environ.get('ADMIN_SITE_TITLE', 'SDGs Management')

ADMIN_SITE_HEADER = os.environ.get('ADMIN_SITE_HEADER', 'SDGs')

ADMIN_INDEX_TITLE = os.environ.get('ADMIN_INDEX_TITLE', 'Management')

# API

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
