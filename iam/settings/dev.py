from .base import *

SECRET_KEY = '-1t3&^v)&u425p#lsif$qy&ds7)!6$wucs#q!3-i2x5w++$z7e'

DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}