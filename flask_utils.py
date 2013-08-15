import json
from flask import make_response

def json_response(ret_obj):
    ret_json = json.dumps(ret_obj)
    resp = make_response(ret_json)
    resp.headers['Content-Type'] = "application/json"
    return resp
