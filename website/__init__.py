from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "quizz_app_database.db"

def create_app():
    """
    Creates the web application itself on which the views will be rendered.
    :return: app
    :rtype: Flask(__name__)
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'teste123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note

    create_database(app)

    loginManager = LoginManager()
    loginManager.login_view = 'auth.login'
    loginManager.init_app(app)

    @loginManager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app



def create_database(app):
    """
    Renders the login page as well as its methods and routes.
    :param app Flask(__name__): Web application
    """
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')