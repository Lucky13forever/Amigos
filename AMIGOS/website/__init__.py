from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
   app = Flask(__name__)
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   app.config['SECRET_KEY'] = 'abcd1234'
   app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
   db.init_app(app)

   from .views import views
   from .auth import auth

   app.register_blueprint(views, url_prefix='/')
   app.register_blueprint(auth, url_prefix='/')

   from . import models

   create_database(app)

   login_manager = LoginManager()
   # login_view, if user is not logged in then specify where to redirect them, in this case -> auth.login
   login_manager.login_view = 'auth.login'
   login_manager.init_app(app)

   @login_manager.user_loader
   def load_user(id):
      try:
         id = int(id)
         return models.User.query.get(int(id))
      except:
         pass
      
   return app

def create_database(app):
   if not path.exists('website/' + DB_NAME):
      db.create_all(app= app)
      print('Created Database!')