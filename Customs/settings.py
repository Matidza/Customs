from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load Dotenv
load_dotenv()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8%g&cru09l5k89!v&+%s99o9o_3_m=dl^9enu@rmztn2'
#SECRET_KEY =os.environ.get['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Production
ALLOWED_HOSTS = [
    'customs.up.railway.app',
    'customkicks.onrender.com',
    'localhost'
]

CSRF_TRUSTED_ORIGINS = [
    'https://customs.up.railway.app',
    'https://customkicks.onrender.com',
    'http://localhost',
    'https://localhost'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'cart',
    'payment',
    'whitenoise.runserver_nostatic',
    'paypal.standard.ipn',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Customs.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'Customs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

''' '''
DATABASES = {
    'default': {
        # Development
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',

        # Production
        # Aivien
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'defaultdb',
        #'USER': 'avnadmin',
        #'PASSWORD': os.environ.get('what'),
        #'HOST': 'customkicks-matidza46-4129.e.aivencloud.com',
        #'PORT': '12695',
    }
}

# Aiven.io
#DATABASES = {
 ## 'default': dj_database_url.parse(os.environ.get('Aiven'), conn_max_age=600)
#}

# Railway.app
'''  '''
DATABASES = {
<<<<<<< HEAD
    'default': dj_database_url.parse(os.environ.get('POSTGRES_CONNECTION_STRING'), conn_max_age=600)
}'''
=======
    'default': dj_database_url.parse(os.environ['POSTGRES_CONNECTION_STRING'], conn_max_age=600)
}
>>>>>>> 87fc61a4e649521f9321aeca02ff9d8a198c6187



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    # This should point to the directory where your app-specific static files are located
    BASE_DIR / 'static/',
]

# Whitenoise static stuff
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# STATIC_ROOT = BASE_DIR / 'staticfiles'  # This is where collectstatic will collect all static files

MEDIA_URL = '/media/'  # Also ensure this has the leading slash
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Pappay Stuf
# Sandbox

PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = 'customkicks@gmail.com'
