from pathlib import Path
import os
from datetime import timedelta
import environ


# Env variables initialization
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') # SECURITY WARNING: keep the secret key used in production secret!

DEBUG = os.getenv('DJANGO_DEBUG_TRUE', '0').lower() in ['true', '1', 't', 'y', 'yes']

ALLOWED_HOSTS = [
    '.ngrok-free.app',
    '*'
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.ngrok-free.app',
    'https://*'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # REST API Dependencies
    'rest_framework',
    # Project's Apps
    'Application',
    'Authentication',
]

# API and JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=20),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=1),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Authentication.middlewares.UserLanguageMiddleware',
    'Application.middlewares.UploadDataValidationMiddleware',
]

ROOT_URLCONF = 'DataForge.urls'

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
                # 'Application.context_processors.languages_list'
            ],
        },
    },
]

WSGI_APPLICATION = 'DataForge.wsgi.application'


# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_LOCALHOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Users Model for Authentication
AUTH_USER_MODEL = 'Authentication.User'

# Password validation
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
LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French'),
    ('es', 'Spanish'),
    ('pt', 'Portuguese'), # Add more if needed
    ('it', 'Italian'),
    ('jp', 'Japanese'),
    ('cn', 'Chinese'),
    ('ru', 'Russian'),
    ('ge', 'German'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',  # Ensure your translation files are in the "locale" folder
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# login Default Redirection URL
LOGIN_URL = 'login'

# Emails service settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_DEFAULT_FROM', 'DataForge')