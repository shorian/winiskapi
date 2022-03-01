import os


class Config(object):
    # defaults
    SECRET_KEY = os.environ.get("SECRET_KEY") or "development key"
    # SQLALCHEMY_DATABASE_URI = `postgresql://username:password@hostname/database`
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
