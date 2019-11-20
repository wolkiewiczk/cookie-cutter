import os


oeg = os.environ.get


ENV = oeg('COOKIE_CUTTER_ENV', 'production')
DEBUG = oeg('COOKIE_CUTTER_DEBUG', 'false').lower() == 'true'
USE_X_SENDFILE = oeg('COOKIE_CUTTER_USE_X_SENDFILE', 'false').lower() == 'true'

