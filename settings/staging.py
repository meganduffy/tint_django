from base import *

# Debug settings
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# PayPal Settings
SITE_URL = 'http://0bae84f3.ngrok.io'
PAYPAL_NOTIFY_URL = 'http://0bae84f3.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'meganemilyduffy@gmail.com'
PAYPAL_TEST = True

ALLOWED_HOSTS.append('http://0bae84f3.ngrok.io')

LOGGING = {
    'version' : 1,
    'disable_existing_loggers' : False,
    'handlers' : {
        'console' : {
            'class' : 'logging.StreamHandler',
        },
    },
    'loggers' : {
        'django' : {
            'handlers' : ['console'],
            'level' : os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
