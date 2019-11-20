from importlib import import_module
import os


oeg = os.environ.get


settings = import_module(oeg('COOKIE_CUTTER_SETTINGS', 'cookie_cutter.settings.base'))
