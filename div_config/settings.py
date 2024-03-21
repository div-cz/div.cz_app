"""
Django settings for divdb project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(7wns0c0f-zk&jpy02dw*^k9iv-q8dg4ofd36tz_+&!o^g3u+q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['46.28.109.39',
        'div.cz',
        'www.div.cz',
        '2001:4860:7:20a::fd',
        'localhost', 
        '127.0.0.1',
        'localhost:8000']
INTERNAL_IPS =  [
        '46.28.109.39',
        '193.179.123.10', 
        '2001:4860:7:20a::fd',
        '127.0.0.1',
        '2001:4860:7:20a::fd'
        ]

DEBUG_TOOLBAR_CONFIG = {
#    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
#    'SHOW_TOOLBAR_CALLBACK': lambda request: True, #show toolbar for all requests
    'SHOW_TOOLBAR_CALLBACK': 'div_config.settings.custom_show_toolbar',

}

def custom_show_toolbar(request):
    if hasattr(request, 'user') and request.user.is_authenticated:
        return request.user.username == 'Martin2dd'
    return False
 
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'div_content',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.microsoft',
    'star_ratings'

]#    'crispy_forms', 

#https://console.cloud.google.com/apis/credentials/oauthclient/696202768234-bamc765kjqrbidnd2jdo5k1blr7gu4s1.apps.googleusercontent.com?project=knihy-div
# https://developers.facebook.com/apps/642069596173684/fb-login/settings/
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '696202768234-bamc765kjqrbidnd2jdo5k1blr7gu4s1.apps.googleusercontent.com',
            'secret': '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',
            'key': 'AIzaSyDlJ9E567Xdsxi1Vb-mYdc_yBQp6kD0-mo'
        }
    },
    'facebook': {
    'APP': {
        'client_id': '642069596173684',
        'secret': 'bfe2272459085a3d74223481477ff3ee'
    }
}


}




MIDDLEWARE = [
    # Bezpečnost by měla být vždy na prvním místě
    'django.middleware.security.SecurityMiddleware',

    # Session middleware by měl předcházet Authentication middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # CSRF middleware a CommonMiddleware obvykle následují po autentizační vrstvě
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # Debug Toolbar by měla být co nejvýše v seznamu, ale po Session a Authentication middlewares
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # Další standardní middlewares
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Middleware pro Allauth
    'allauth.account.middleware.AccountMiddleware',
]


MIGRATION_MODULES = {
#    "div_content": None,
}
 
ROOT_URLCONF = 'div_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'div_content/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',

            ],
        },
    },
]


WSGI_APPLICATION = 'div_config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'divDB',
        'USER': 'martindb', #'editordb2',
        'PASSWORD': 'Han1cka+1a9', #'2*mP3jD6kW',
        'HOST': 'localhost', #'46.28.109.39',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

]
ACCOUNT_USE_SIGNUP_HONEYPOT = True

#AUTH_USER_MODEL = 'div_content.CustomUser'
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'cs-cz'
LANGUAGES = [
    ('cs', 'Czech'),
]

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DEFAULT_CHARSET = 'utf-8'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = '/var/www/div/div_app/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/img/'
#MEDIA_ROOT = '/var/www/div_app/img/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'img')

#STATIC_ROOT = '/var/www/div_app/static/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'var/log/django.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {  # '' znamená default logger pro celou aplikaci
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}"""

