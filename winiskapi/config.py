import os


class Config(object):
    # defaults
    SECRET_KEY = os.environ.get("SECRET_KEY") or "development key"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
