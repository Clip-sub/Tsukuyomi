import os.path

from flask import abort
from flask.config import Config
from flask_assets import Environment
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import BaseQuery, Pagination, SQLAlchemy

assets = Environment()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cache = Cache(config={'CACHE-TYPE': 'simple'})

def _get_config():
  root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
  config = Config(root_path)
  config.from_object('config')
  return config

config = _get_config()
