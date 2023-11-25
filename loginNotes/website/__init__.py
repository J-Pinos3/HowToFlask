from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fsdf56sdf 564'#SECURE COOKIES AND SESSION DATA
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')#url prefix is all the url 
    app.register_blueprint(auth, url_prefix='/')#that are inside that blueprints file


    from .models import User, Note
    
    with app.app_context():
        db.create_all()
    #create_database(app)

    return app

def create_database(app): #checks if db already exists
    if not path.exists('website/'+DB_NAME):
        db.create_all(app=app)
        print('Db Created!!')