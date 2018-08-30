import binascii
import math
import time

import flask
from flask_paginate import Pagination

bp = flask.Blueprint('user', __name__)

@bp.route('/user/<:id>', methods=['GET'])
def view_user(user_id):
  return 'This is user id'
