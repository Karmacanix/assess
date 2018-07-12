from .base import *

DEBUG = False

ALLOWED_HOSTS = ['thawing-ocean-69787.herokuapp.com', ]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

    # django.db.backends.postgresql_psycopg2

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL')
    )
}
