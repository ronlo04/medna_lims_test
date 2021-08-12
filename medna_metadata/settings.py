"""
Django settings for medna_metadata project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import logging.config
import os

from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", default=get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', True)

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="localhost [::1]").split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    'users',
    'field_sites',
    'sample_labels',
    'field_survey',
    'wet_lab',
    'freezer_inventory',
    'bioinfo_denoising',
    'bioinfo_taxon',
    'corsheaders',
    'import_export', # django-import-export
    'allauth', # django-allauth handles user registration as well as social authentication.
    'allauth.account', # Good for email address verification, resetting passwords, etc.
    'allauth.socialaccount',
#    'allauth.socialaccount.providers.google', # need to set up google APIs settings https://django-allauth.readthedocs.io/en/latest/providers.html#google
    'rest_auth', # django-rest-auth provides API endpoints for user reg, login/logout,
    'rest_auth.registration', # password change/reset, social auth, etc
    'rest_framework',  # integrates with django-filter .. might as well set it all up correctly from the get-go
    'rest_framework_gis', # needed for geojson and geodjango - maybe read later .. is not compatible with import-export because tablib doesn't have geojson format. Would have to add multiple serializers.
    'rest_framework.authtoken',  # for the creation of api tokens
    'phonenumber_field', # specific formatting for phone numbers - django-phonenumber-field[phonenumberslite]

]

# grab currently logged in user for reference in models
# Adding the following line to the “settings.py” file will let Django know to use the new User class:
AUTH_USER_MODEL = 'users.CustomUser'

# The list of authentication backends to use is specified in the AUTHENTICATION_BACKENDS setting.
# This should be a list of Python path names that point to Python classes that know how to authenticate.
# These classes can be anywhere on your Python path.
AUTHENTICATION_BACKENDS = [
    # the basic authentication backend that checks the Django users database and queries the built-in permissions.
    # It does not provide protection against brute force attacks via any rate limiting mechanism.
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

#  You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE,
#  but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes
#  it more difficult for network traffic sniffers to steal the CSRF token.
#CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes
# it more difficult for network traffic sniffers to hijack user sessions.
#SESSION_COOKIE_SECURE = True
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'medna_metadata.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS is a list of filesystem directories to check when loading Django templates;
        # it’s a search path.
        # templates that belong to a particular application should be placed in that application’s
        # template directory (e.g. polls/templates) rather than the project’s (templates).
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'medna_metadata.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', 'medna_metadata'),
        'USER': os.environ.get('DJANGO_DATABASE_USERNAME', 'django'),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', 'password'),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DJANGO_DATABASE_PORT', 5433),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# media files (if uploaded)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# location for dump or load of initial data
FIXTURE_DIRS = [os.path.join(BASE_DIR, 'fixtures/'),]

# Then set the redirect links for login and logout, which will both go to our home index template
# https://learndjango.com/tutorials/django-custom-user-model
LOGIN_REDIRECT_URL = 'users:home' # default to /accounts/profile .. which doesn't exist
ACCOUNT_LOGOUT_REDIRECT_URL = 'users:home'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django-phonenumber-field[phonenumberslite] settings
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'US'

## these are settings for Django REST framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',  # can authenticate via token
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', # have to be authenticated to view rest API
    ),
}

# make sure serializer is not default serializer, but the custom one with additional fields
# https://krakensystems.co/blog/2020/custom-users-using-django-rest-framework
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'users.serializers.CustomLoginSerializer',
    'USER_DETAILS_SERIALIZER': 'users.serializers.CustomUserDetailsSerializer',
}

## settings for import-export to allow exporting data via csv
IMPORT_EXPORT_USE_TRANSACTIONS = True

SITE_ID = 1

# Django rest-auth and allauth settings:
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'
# Controls the life time of the session. Set to None to ask the user (“Remember me?”),
# False to not remember, and True to always remember.
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 900 # 15 mins in seconds


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django SMTP Email Settings:
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = os.environ.get('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD')

## django-cors-headers to open up the backend to connect to the frontend
CORS_ORIGIN_WHITELIST = [
     'http://localhost:8000'
]


# Logging Configuration
# Clear prev config
LOGGING_CONFIG = None

# Get loglevel from env
LOGLEVEL = os.environ.get('DJANGO_LOGLEVEL', 'info').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console',],
        },
    },
})