from app import app
from flask.ext.assets import Environment, Bundle

assets = Environment(app)

index_js = Bundle('index.coffee', filters='coffeescript', output='gen/index.js')
assets.register('index_js', index_js)
