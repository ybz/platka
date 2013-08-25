from flask.ext.login import LoginManager, AnonymousUserMixin

from app import app
from models import User

login_manager = LoginManager()
login_manager.init_app(app)

class PLAnonymousUser(AnonymousUserMixin):
    def __nonzero__(self):
        return False
    def __repr__(self):
        return '%s()' % (self.__class__.__name__,)
login_manager.anonymous_user = PLAnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

login_manager.login_view = 'login'
login_manager.login_message = 'Please login'
