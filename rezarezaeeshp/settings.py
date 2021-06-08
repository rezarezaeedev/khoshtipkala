"""
Django settings for rezarezaeeshp project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ksvu5az^h00=xq=!fj)(fis9x1w!2cxunyy^n^%u-+_cs47bl*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 1

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_render_partial',
    'captcha',

    # Our apps
    'eshop_account',
    'eshop_products',
    'eshop_tag',
    'eshop_products_category',
    'eshop_sliders',
    'eshop_brands',
    'eshop_contacts',
    'eshop_seller',
    'eshop_sitesetting',
    'eshop_order',
    'eshop_payment'
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

ROOT_URLCONF = 'rezarezaeeshp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'rezarezaeeshp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fa-ir'
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Set Static files directories
STATICFILES_DIRS = [
    BASE_DIR / "assets",
]

# Static files config
STATIC_URL = '/site_statics/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'static_root')

# Media files config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'media_root')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'r871017h800501@gmail.com'
EMAIL_HOST_PASSWORD = 'rezar87gmailrezahadis7880'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

RECAPTCHA_PUBLIC_KEY = '6LcC4RsbAAAAAOceFxxSkTv3wZUUTbaOL2DHuhR0' # for v2-checkbox
# RECAPTCHA_PUBLIC_KEY = '6Ld79hsbAAAAAFdEf3jcoA-IwD8saX_9mbl8bC1_' # for v3
RECAPTCHA_PRIVATE_KEY = '6LcC4RsbAAAAACqcMNRey6slZ3Ufythcmh385B_Z' # for v2-checkbox
# RECAPTCHA_PRIVATE_KEY = '6Ld79hsbAAAAAEm-SUswcwYvlt30lYRxKK4UjwCu'# for v3
