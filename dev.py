import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config
from app.models import User

# from app.models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/hello')
def hello_world():
    return 'Hello World!!!'


@app.route('/create_db')
def init_db():
    db.create_all()

    user1 = User(email='user1@yopmail.com')
    db.session.add(user1)
    db.session.commit()
    return 'DB created'


def print_help():
    print('Tsukuyomi Development Helper')
    print('=======================\n')
    print('Usage: {0} command [different arguments]'.format(sys.argv[0]))
    print('Command can be one of the following:\n')
    print('  lint | check       : do a lint check (flake8 + flake8-isort)')
    print('  fix  | autolint    : try and auto-fix lint (autopep8)')
    print('  isort              : fix import sorting (isort)')
    print('  test | pytest      : run tests (pytest)')
    print('  help | -h | --help : show this help and exit')
    print('')
    print('You may pass different arguments to the script that is being run.')
    print('For example: {0} test tests/ --verbose'.format(sys.argv[0]))
    print('')
    return 1


def print_cmd(cmd, args):
    print('Running: {0}\n'.format(
        ' '.join([('\'' + a + '\'' if ' ' in a else a) for a in [cmd] + args])))
    sys.stdout.flush()


if __name__ == '__main__':
    # app.run()
    assert sys.version_info >= (3, 6), "Python 3.6 or above is required"
