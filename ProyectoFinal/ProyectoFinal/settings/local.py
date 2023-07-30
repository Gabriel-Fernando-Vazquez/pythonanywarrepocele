from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['Gabriel94.mysql.pythonanywhere-services.com']

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


