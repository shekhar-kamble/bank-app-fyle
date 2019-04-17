import os

from flask import Flask
from flask_assets import Environment
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SSL_DISABLE = (os.environ.get('SSL_DISABLE') or 'True') == 'True'
print SQLALCHEMY_DATABASE_URI
db = SQLAlchemy()
compress = Compress()
# app_ctx = None
def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.app = app
        # register_extensions(app)
    # not using sqlalchemy event system, hence disabling it

    # app_ctx = app
    # Set up extensions
    db.init_app(app)
    # print db.engine
    compress.init_app(app)

    # Configure SSL if platform supports it
    if not app.debug and not app.testing and not SSL_DISABLE:
        from flask_sslify import SSLify
        SSLify(app)

    # Create app blueprints
    from .common import default as common_blueprint
    app.register_blueprint(common_blueprint)
    return app
