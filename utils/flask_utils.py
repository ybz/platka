import json
from httplib import OK
from flask import make_response

def json_response(ret_obj, status=OK, extra_headers={}):
    ret_json = json.dumps(ret_obj)
    headers = {'Content-Type': 'application/json'}
    headers.update(extra_headers)
    resp = make_response(ret_json, status, headers)
    return resp
