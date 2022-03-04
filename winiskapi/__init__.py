from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from winiskapi.config import Config
from flask_login import LoginManager
from flask_argon2 import Argon2

db = SQLAlchemy()
migrate = Migrate()
argon2 = Argon2()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(cfg="development"):  # testing, development, or production
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)
    app.config.from_pyfile(f"{cfg}.py")

    db.init_app(app)
    migrate.init_app(app, db)
    argon2.init_app(app)
    login_manager.init_app(app)

    from winiskapi.main.routes import main
    from winiskapi.auth.routes import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
