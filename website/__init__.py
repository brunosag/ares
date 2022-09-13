from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import environ

db = SQLAlchemy()

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


def create_app():
    app = Flask(__name__)
    app.debug = env('DEBUG')
    app.config['SECRET_KEY'] = env('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
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
