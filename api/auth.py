from httplib import NO_CONTENT
from flask.views import MethodView
from flask.ext.login import current_user
from app import app
from utils.flask_utils import json_response

class SessionApi(MethodView):
    def marshal_user(self, user):
        return {
            'username': user.username
        }
    def get(self):
        print '\n\n\n current_user %s' % current_user
        if current_user:
            return json_response(self.marshal_user(current_user))
        return ('', NO_CONTENT, {})
    def put(self):
        return json_response({ 'method' : 'put' })

app.add_url_rule('/api/session', view_func=SessionApi.as_view('api_session'))
