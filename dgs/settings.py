"""
Django settings for dgs project.

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
    'mptt',
    'import_export',
    'admin_reorder',
    'modeltranslation',
    'haystack',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'imagekit',
    'goals',
    'goals_search',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'dgs.urls'

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
                'dgs.context_processors.site',
            ],
        },
    },
]

WSGI_APPLICATION = 'dgs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DATABASE_NAME', 'dgs'),
        'USER': os.environ.get('DATABASE_USER', 'dgs'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'dgs'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'CONN_MAX_AGE': int(os.environ.get('DATABASE_CONN_MAX_AGE', 0))
    }
}

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': os.environ.get('HAYSTACK_DEFAULT_ENGINE', 'haystack_elasticsearch5.Elasticsearch5SearchEngine'),
        'URL': os.environ.get('HAYSTACK_DEFAULT_URL', 'http://127.0.0.1:9200/'),
        'INDEX_NAME': os.environ.get('HAYSTACK_DEFAULT_INDEX_NAME', 'dgs'),
        'INCLUDE_SPELLING': bool(os.environ.get('HAYSTACK_DEFAULT_INCLUDE_SPELLING', True)),
        'KWARGS': {}
    },
}

haystack_default_http_auth = os.environ.get('HAYSTACK_DEFAULT_HTTP_AUTH', '').split()
if len(haystack_default_http_auth) >= 2:
    HAYSTACK_CONNECTIONS['default']['KWARGS']['http_auth'] = haystack_default_http_auth[:2]

haystack_default_use_ssl = bool(os.environ.get('HAYSTACK_DEFAULT_USE_SSL', False))
if haystack_default_use_ssl:
    HAYSTACK_CONNECTIONS['default']['KWARGS']['use_ssl'] = haystack_default_use_ssl
    HAYSTACK_CONNECTIONS['default']['KWARGS']['verify_certs'] = bool(os.environ.get('HAYSTACK_DEFAULT_VERIFY_CERTS', True))

haystack_default_connection_class = os.environ.get('HAYSTACK_DEFAULT_CONNECTION_CLASS', '')
if haystack_default_connection_class:
    HAYSTACK_CONNECTIONS['default']['KWARGS']['connection_class'] = haystack_default_connection_class

HAYSTACK_SIGNAL_PROCESSOR = os.environ.get('HAYSTACK_SIGNAL_PROCESSOR', 'haystack.signals.RealtimeSignalProcessor')

HAYSTACK_DEFAULT_OPERATOR = os.environ.get('HAYSTACK_DEFAULT_OPERATOR', 'AND')

HAYSTACK_SEARCH_RESULTS_PER_PAGE = int(os.environ.get('HAYSTACK_SEARCH_RESULTS_PER_PAGE', 30))

# Cache

CACHES = {
    "default": {
        "BACKEND": os.environ.get('CACHE_DEFAULT_BACKEND', 'django_redis.cache.RedisCache'),
        "LOCATION": os.environ.get('CACHE_DEFAULT_LOCATION', 'redis://localhost:6379/0'),
        "TIMEOUT": int(os.environ.get('CACHE_DEFAULT_TIMEOUT', 300)),
        "OPTIONS": {
            "CLIENT_CLASS": os.environ.get('CACHE_DEFAULT_CLIENT_CLASS', 'django_redis.client.DefaultClient')
        }
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

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en')

MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGE_CODE

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('sw', gettext('Kiswahili')),
)

if os.environ.get('LANGUAGES',''):
    LANGUAGES = []
    for lang in os.environ.get('LANGUAGES','').split(';'):
        LANGUAGES.append([i.strip() for i in lang.split(':')])

LOCALE_PATHS = [
    'locale',
]

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

# Imagekit

IMAGEKIT_DEFAULT_CACHEFILE_BACKEND = os.environ.get('IMAGEKIT_DEFAULT_CACHEFILE_BACKEND', 'imagekit.cachefiles.backends.Simple')

IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = os.environ.get('IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY', 'imagekit.cachefiles.strategies.Optimistic')

# Site

SITE_NAME = os.environ.get('SITE_NAME', 'DGs')

SITE_API_NAME = os.environ.get('SITE_API_NAME', 'DGs API')

SITE_API_URL = os.environ.get('SITE_API_URL', '/api/')

ADMIN_SITE_TITLE = os.environ.get('ADMIN_SITE_TITLE', 'DGs Management')

ADMIN_SITE_HEADER = os.environ.get('ADMIN_SITE_HEADER', 'Development Goals (DGs)')

ADMIN_INDEX_TITLE = os.environ.get('ADMIN_INDEX_TITLE', 'Management')

# https://django-modeladmin-reorder.readthedocs.io/en/latest/
ADMIN_REORDER = (
    {'app': 'auth', 'models': ('auth.User', 'auth.Group')},
    {'app': 'goals',
             'label': gettext('Development goals'),
             'models': ('goals.Plan', 'goals.Goal', 'goals.Target',
                        'goals.Indicator', 'goals.Component', 'goals.Progress')},
    {'app': 'goals',
            'label': gettext('Areas'),
            'models': ('goals.AreaType', 'goals.Area')},
)

# API

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'goals.api.renderers.CSVRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}

# CORS
CORS_ORIGIN_ALLOW_ALL = str_to_bool(os.environ.get('CORS_ORIGIN_ALLOW_ALL', 'True'))

CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST', '*').split()

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + tuple(os.environ.get('CORS_ALLOW_EXTRA_HEADERS', 'x-client-id').split())

CORS_MODEL = os.environ.get('CORS_MODEL', None)
