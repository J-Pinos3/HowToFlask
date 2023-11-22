from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fsdf56sdf 564'#SECURE COOKIES AND SESSION DATA


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')#url prefix is all the url 
    app.register_blueprint(auth, url_prefix='/')#that are inside that blueprints file

    return app