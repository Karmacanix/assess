from .base import *

SECRET_KEY = '-1t3&^v)&u425p#lsif$qy&ds7)!6$wucs#q!3-i2x5w++$z7e'

DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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