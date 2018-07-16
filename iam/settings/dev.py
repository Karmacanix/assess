from .base import *

SECRET_KEY = '-1t3&^v)&u425p#lsif$qy&ds7)!6$wucs#q!3-i2x5w++$z7e'

DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'david.rigby@ccdhb.org.nz'
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True


    # django.db.backends.postgresql_psycopg2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'assess',
        'USER': 'postgres',
        'PASSWORD': 'Rambo8731',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}