from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import environ
import os

db = SQLAlchemy()

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


def create_app():
    app = Flask(__name__)
    DEBUG = 'RENDER' not in os.environ
    app.config['SECRET_KEY'] = env('SECRET_KEY', default='006363ce276b892f9f89d16571fd0113')
    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI', default='sqlite:///db.sqlite3')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    db.create_all(app=app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.signup"
    login_manager.login_message = ""
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
