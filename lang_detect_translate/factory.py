"""This module handles creating instances of app"""
import os
from flask import Flask
from werkzeug.utils import find_modules, import_string

from lang_detect_translate.models.base import db
from lang_detect_translate.schemata.base import marsh

def create_app(config=None):
    """Creates an instance of app"""
    app = Flask('lang-detect-translate')

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcloud_auth.json"

    # Load settings for instance
    app.config.from_object("lang_detect_translate.settings")
    app.config.from_object(config)

    # Connect Database to app
    db.init_app(app)

    # Initializes Marshmallow schemata
    marsh.init_app(app)

    # Registered all blueprints
    register_blueprints(app)

    return app

def register_blueprints(app):
    """Registers all blueprints for app"""
    for module_path in find_modules("lang_detect_translate.blueprints"):
        module = import_string(module_path)
        if hasattr(module, 'bp'):
            app.register_blueprint(module.bp)
