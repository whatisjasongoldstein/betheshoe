# Django settings for betheshoe project.
import os
import sys
from unipath import Path

DEBUG = False
if 'runserver' in sys.argv:
    DEBUG = True
    pass

TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = Path(__file__).ancestor(2)

ADMINS = (
    ('Jason Goldstein', 'jason@betheshoe.com'),
)

THUMBNAIL_BASEDIR = "thumbnails/"

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'betheshoeproductions',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'betheshoe',
        'PASSWORD': os.environ["BETHESHOE_DB_PASSWORD"],
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
if 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "betheshoe.com",
    "preview.betheshoe.com",
    "local.betheshoe.com",
    "127.0.0.1",
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
SITE_URL = "http://betheshoe.com"

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR.child("media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_DIR.child("static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['BETHESHOE_DB_SECRET_KEY']

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'johnny.middleware.LocalStoreClearMiddleware',
    'johnny.middleware.QueryCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DEBUG_TOOLBAR = False

if DEBUG and DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {
        "INTERCEPT_REDIRECTS": False,
    }

ROOT_URLCONF = 'betheshoe.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'betheshoe.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_USERNAME_REQUIRED = False
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True
# SOCIALACCOUNT_AVATAR_SUPPORT = True
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_REQUIRED = True

PERSONA_AUDIENCE = 'http://betheshoe.com'
if 'runserver' in sys.argv:
    PERSONA_AUDIENCE = "http://betheshoe.bs:8000"

SOCIALACCOUNT_PROVIDERS = { 
    'facebook': { 'SCOPE': ['email',],
          'AUTH_PARAMS': { 'auth_type': 'reauthenticate' },
          'METHOD': 'oauth2' ,
          'LOCALE_FUNC': lambda request: 'en_US'}, 
    'persona': { 'AUDIENCE': PERSONA_AUDIENCE, } 
}


LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_ON_GET = True

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    "betheshoe.context_processors.current_site_url",
 )

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_JS_FILTERS = ()  # Don't jack with anything, just combined them


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'compressor',

    'betheshoe', # Templates preempt allauth's

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.persona',

    'avatar',
    'easy_thumbnails',
    'markdown_deux',
    'genericadmin',
    'django_nose',
    'typogrify',

    'responsive_bits',
    'django_featuring',
    'cropper',
    'draftin',

    'betheshoe.movies',
    'betheshoe.blog',
    'betheshoe.music',
    'betheshoe.staff',
]

if DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
    'johnny' : {
        'BACKEND' : 'johnny.backends.memcached.MemcachedCache',
        'LOCATION' : ['127.0.0.1:11211'],
        'JOHNNY_CACHE' : True,
    },
}
JOHNNY_MIDDLEWARE_KEY_PREFIX='jhnybeshoe'


FEATURABLE_CONTENT_TYPES = (
    'movies/movie',
    'blog/post',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


EMAIL_HOST=os.environ['BETHESHOE_EMAIL_HOST']
EMAIL_HOST_USER=os.environ['BETHESHOE_EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD=os.environ['BETHESHOE_EMAIL_HOST_PASSWORD']
EMAIL_PORT=587
DEFAULT_FROM_EMAIL = os.environ['BETHESHOE_DEFAULT_FROM_EMAIL']
SERVER_EMAIL = os.environ['BETHESHOE_SERVER_EMAIL']
EMAIL_USE_TLS=True

MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": "escape",
    },
    "embeds": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": False,
    },
}

