import os.path
from logging import getLogger

from flask.config import Config
from flask.ext.celery import Celery
from flask.ext.redis import Redis
from flask_assets import Environment
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import listens_for

LOG = getLogger(__name__)
assets = Environment()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cache = Cache(config={'CACHE-TYPE': 'simple'})


@listens_for(Pool, 'connect', named=True)
def _on_connect(dbapi_connection, **_):
    LOG.debug('Setting SQL Mode to TRADITIONAL')
    dbapi_connection.cursor().execute("SET SESSION sql_mode='TRADITIONAL'")


def _get_config():
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    cfg = Config(root_path)
    cfg.from_object('config')
    return cfg


celery = Celery()
db = SQLAlchemy()
redis = Redis()
config = _get_config()
