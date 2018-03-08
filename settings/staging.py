from base import *
import dj_database_url

# Debug settings
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        'mysql://bc8a1f6390516f:3cbdc587@eu-cdbr-west-01.cleardb.com/heroku_b91badd0d37c867?reconnect=true')
}

# PayPal Settings
SITE_URL = 'https://typeitnow.herokuapp.com'
PAYPAL_NOTIFY_URL = 'http://0bae84f3.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'meganemilyduffy@gmail.com'
PAYPAL_TEST = True


ALLOWED_HOSTS.append('typeitnow.herokuapp.com')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
