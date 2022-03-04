class Config(object):
    # defaults
    SECRET_KEY = "for development only!"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
