from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from winiskapi.main.routes import main
    from winiskapi.auth.routes import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
