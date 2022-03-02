from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


def create_app(env):  # testing, development, or production
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)
    app.config.from_pyfile(f"{env}.py")

    db.init_app(app)

    from winiskapi.main.routes import main
    from winiskapi.auth.routes import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
