import os
from flask import Flask
from flask_utils import json_response

app = None

def init_app():
    global app

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    import models; models

    @app.route('/')
    def index():
        return 'hello platka'

    @app.route('/test_json')
    def test_json():
        return json_response([
            {
                'prop_a' : 13,
                'prop_b' : 21,
            },
            {
                'prop_a' : 90,
                'proc_b' : 40,
                'proc_c' : 85,
            },
        ])

    return app
