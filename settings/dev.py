from base import *

# Debug mode
DEBUG = True

# INSTALLED_APPS.append('debug_toolbar')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# PayPal Settings
# SITE_URL = 'http://127.0.0.1:8000'
SITE_URL = 'http://0bae84f3.ngrok.io'
PAYPAL_NOTIFY_URL = 'http://0bae84f3.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'meganemilyduffy@gmail.com'
PAYPAL_TEST = True