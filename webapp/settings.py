# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('WEBAPP_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class RedisConfig(object):
    HOST = 'redis'
    PORT = 6379
    DB = 0
    URL = 'redis://%s:%d/%d' % (HOST, PORT, DB)


class MongoConfig(object):
    HOST = 'mongo'
    PORT = 27017
    DB = 'test'


class MysqlConfig(object):
    USER = 'root'
    PASSWORD = 'p@ssw0rd123'
    DATABASE = 'wordpress'
    HOSTNAME = 'mysqlserver'
    URL = 'mysql://%s:%s@%s/%s' % (USER, PASSWORD, HOSTNAME, DATABASE)


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = MysqlConfig.URL
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.

    MONGODB_SETTINGS = {
        'db': MongoConfig.DB,
        'host': MongoConfig.HOST,
        'port': MongoConfig.PORT,
    }
    REDIS_URL = RedisConfig.URL


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
