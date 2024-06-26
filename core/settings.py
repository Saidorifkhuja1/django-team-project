"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_9rhu18*__cgm-tzhqqa+bvv5q*!ywpjmf&ceic&nddjwa$4vf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["0.0.0.0",
    "127.0.0.1"
]



# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_jinja",
    "app_administrator.apps.AppAdministratorConfig",
    "app_banners.apps.AppBannersConfig",
    "app_cart.apps.AppCartConfig",
    "app_catalog.apps.AppCatalogConfig",
    "app_discounts.apps.AppDiscountsConfig",
    "app_orders.apps.AppOrdersConfig",
    "app_payment.apps.AppPaymentConfig",
    "app_users.apps.AppUsersConfig",
    "app_main_page.apps.AppMainPageConfig",
    "phone_field",

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            # django-jinja defaults
            "match_extension": ".jinja2",
            "match_regex": None,
            "app_dirname": "templates",
            "environment": "config.utils.environment",
            "constants": {},
            "globals": {},
            "context_processors": [
                "app_cart.context_processors.cart",
                "app_cart.context_processors.comparison",
            ],
        },
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

COMPARISON_SESSION_ID = "comparison"

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "uploads"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "app_users.User"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}


USE_DJANGO_JQUERY = True


LOGIN_REDIRECT_URL = reverse_lazy("app_users:profile")


TEMPLATE_CONTEXT_PROCESSORS = (
    "app_catalog.context_processors.foos",
    "django.contrib.messages.context_processors.messages",
)

CART_SESSION_ID = "cart"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        },
    },
    "handlers": {
        "import_products": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "import_log.txt",  # имя лог.файла
            "maxBytes": 1024 * 1024 * 1,  # 1 MB
            "backupCount": 3,  # 3 файла
            "formatter": "verbose",
        }
    },
    "root": {"handlers": ["import_products"], "level": "INFO", "propagate": True},
}


# Celery settings

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"

CELERY_BROKER_URL = 'amqp://localhost:5672'
