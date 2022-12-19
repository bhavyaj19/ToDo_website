from flask import Flask, render_template
app = Flask(__name__)

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = 'keystologinsite' #this is a encryption key to encrypt the cookies data

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
    