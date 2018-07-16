from .base import *

from decouple import config

DEBUG = True

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['thawing-ocean-69787.herokuapp.com', ]

ANYMAIL = {
    "MAILGUN_API_KEY": "a4c8297ba9e8d5b02c2f229cff530574-8b7bf2f1-3e430b47",
}

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

DEFAULT_FROM_EMAIL = 'david.rigby@ccdhb.org.nz'
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True


    # django.db.backends.postgresql_psycopg2

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL')
    )
}
