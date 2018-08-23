import logging
import os
import string

import flask
from flask_assets import Bundle

def create_app(config):
  app = flask.Flask(__name__)
  app.config.from_object(config)

  app.config['SESSION_REFRESH_EACH_REQUEST'] = False

  # Debugging:
  if app.config['DEBUG']:
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

  return app
