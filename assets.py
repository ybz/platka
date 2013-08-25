from app import app
from flask.ext.assets import Environment, Bundle

assets = Environment(app)

assets.register('css_reset',
    'core/reset.scss',
    output='gen/reset.css', filters='scss')

assets.register('css_login',
    'login/login.scss',
    output='gen/login.css', filters='scss')

vendor_js = Bundle('vendor/lodash/lodash.js', 'vendor/backbone/backbone.js')
index_coffee = Bundle('index/*.coffee', filters='coffeescript', output='gen/index.coffee.js')
index_js = Bundle(vendor_js, index_coffee, filters='yui_js', output='gen/index.js')

assets.register('index_js', index_js)
