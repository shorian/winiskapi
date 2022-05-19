from flask import Flask
from flask_argon2 import Argon2
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_redmail import RedMail
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
argon2 = Argon2()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
mail = RedMail()
debug_toolbar = DebugToolbarExtension()


def create_app(cfg="development"):
    # config filename: testing, development, or production
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile(f"{cfg}.py")

    db.init_app(app)
    argon2.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    debug_toolbar.init_app(app)

    from winiskapi.auth.routes import auth
    from winiskapi.contacts.routes import contacts
    from winiskapi.main.routes import main

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(contacts)

    return app
