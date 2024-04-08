from flask import Flask
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = ""

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Educloud_Abdoul'

    # Register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
