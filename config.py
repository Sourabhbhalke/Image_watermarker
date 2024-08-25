import os
from os import environ

class Config(object):
    DEBUG = False
    TESTING = False
    
    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = environ.get('SECRET_KEY', 'default_secret_key')

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = environ.get('DB_PASSWORD', 'default_password')

    UPLOADS = os.path.join(basedir, 'static', 'uploads')

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = environ.get('DB_PASSWORD', 'default_password')

    UPLOADS = os.path.join(Config.basedir, 'static', 'uploads')  # Access basedir from Config
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    DEBUG = True

    DB_NAME = "testing-db"
    DB_USERNAME = "root"
    DB_PASSWORD = environ.get('DB_PASSWORD', 'default_password')

    UPLOADS = os.path.join(Config.basedir, 'static', 'uploads')  # Access basedir from Config
    SESSION_COOKIE_SECURE = False


class DebugConfig(Config):
    DEBUG = False
