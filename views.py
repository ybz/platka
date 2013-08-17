from app import app
from flask_utils import json_response

import api; api


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
