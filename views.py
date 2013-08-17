from app import app
from flask import render_template
from flask_utils import json_response

import api; api


@app.route('/')
def index():
    return render_template('index.html')

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