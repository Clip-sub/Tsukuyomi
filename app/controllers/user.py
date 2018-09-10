import flask

bp = flask.Blueprint('user', __name__)


@bp.route('/user/<:user_id>', methods=['GET'])
def view_user(user_id):
    return 'This is user id' + user_id
