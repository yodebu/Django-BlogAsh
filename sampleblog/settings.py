"""
Django settings for sampleblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sampleblog.settings')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.setdefault('some_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['blogging-application.herokuapp.com']

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'blog/templates/blog'),
    #Putstringshere,like"/home/html/django_templates"r"C:/www/django/templates"
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

MEDIA_ROOT = os.path.join(BASE_DIR, '/media/')

STATIC_ROOT = 'staticfiles'

STATIC_URL = "/static/"

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
    )

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/')

SOUTH_TESTS_MIGRATE = False


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'blog',
    'taggit',
    'social_auth',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django-session-idle-timeout',
)

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
	 'django.template.loaders.app_directories.Loader'
		)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

AUTHENTICATION_BACKENDS=(
	'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
	)


SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django-session-idle-timeout.middleware.SessionIdleTimeout',
)

SESSION_IDLE_TIMEOUT = 60

GOOGLE_OAUTH2_CLIENT_ID = os.environ.get("googleclientid")

GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get("googleclientsecret")

FACEBOOK_APP_ID = os.environ.get("fbID")

FACEBOOK_API_SECRET = os.environ.get("fbsecret")

TWITTER_CONSUMER_KEY = os.environ.get("twitterapi")

TWITTER_CONSUMER_SECRET = os.environ.get("twittersecret")

LOGIN_URL = '/blog/'
LOGIN_REDIRECT_URL = '/blog/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/blog/'
SOCIAL_AUTH_INACTIVE_USER_URL = '...'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

ROOT_URLCONF = 'sampleblog.urls'

WSGI_APPLICATION = 'sampleblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = "/static/"

BLOG_NUMBER_OF_ENTRIES_PER_PAGE = 3



STATIC_URL = '/static/'

BLOG_NUMBER_OF_ENTRIES_PER_PAGE = 3

BLOG_NUMBER_OF_RECENT_ENTRIES_PER_PAGE = 5

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("emailhost")
EMAIL_HOST_USER = os.environ.get("hostuser")
EMAIL_HOST_PASSWORD = os.environ.get("hostpswd")
EMAIL_USE_TLS = True
EMAIL_PORT = os.environ.get("emailport")

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
