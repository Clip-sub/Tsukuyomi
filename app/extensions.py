import os.path

from flask.config import Config
from flask_assets import Environment
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

assets = Environment()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cache = Cache(config={'CACHE-TYPE': 'simple'})


def _get_config():
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    cfg = Config(root_path)
    cfg.from_object('config')
    return cfg


config = _get_config()
