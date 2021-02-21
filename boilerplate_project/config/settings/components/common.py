import os
from pathlib import Path

import dj_database_url

# -----------------------------------------------------------------------------
# COMMON SETTINGS
# -----------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', default='secret-key')

ROOT_URLCONF = 'boilerplate_project.config.urls'

WSGI_APPLICATION = 'boilerplate_project.config.wsgi.application'

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# -----------------------------------------------------------------------------
# STATIC & MEDIA SETTINGS
# -----------------------------------------------------------------------------

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]

# -----------------------------------------------------------------------------
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# -----------------------------------------------------------------------------
DEFAULT_DB = 'postgres://postgres@db_container/postgres'

DATABASES = {
    'default': dj_database_url.config(default=DEFAULT_DB, conn_max_age=600)
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATA_UPLOAD_MAX_NUMBER_FIELDS = 300000
# -----------------------------------------------------------------------------
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
# -----------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
