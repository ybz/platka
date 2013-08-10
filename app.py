import os
from flask import Flask

app = None

def init_app():
    global app

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    import models; models;

    @app.route('/')
    def index():
        return 'hello platka'
        return app

    return app
