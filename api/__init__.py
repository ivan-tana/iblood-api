from flask import Flask

from flask_cors import CORS
from .extensions import api, db
from .commands import create_tables
from . import resources

def create_app(config_file='bin/settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    api.init_app(app)
    CORS(app)

    

    app.cli.add_command(create_tables)

    return app