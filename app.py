import os
from flask import Flask

app = None

def init_app():
    global app

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['DEBUG'] = bool(int(os.environ.get('DEBUG', 0)))
    app.config['ASSETS_DEBUG'] = bool(int(os.environ.get('ASSETS_DEBUG', 0)))
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    import assets; assets
    import models; models
    import views; views
    import auth; auth

    return app
