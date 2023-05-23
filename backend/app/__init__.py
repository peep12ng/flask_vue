from flask import Flask, jsonify
from flask_cors import CORS

from .routes import bp
from .extensions import db, migrate
from . import config

def create_app():
    app = Flask(__name__)

    CORS(app, resources={r'/*': {'origins':'*'}})
    configure_app(app, config)
    configure_extensions(app)
    configure_blueprint(app, bp)

    return app

def configure_app(app, config):
    app.config.from_object(config)

def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

    from .models import ddragon, riotapi

def configure_blueprint(app, blueprint):
    app.register_blueprint(blueprint)