import sys
from flask import Flask, current_app as app

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!!!'

def print_cmd(cmd, args):
  print('Running: {0}\n'.format(
    ' '.join([('\'' + a + '\'' if ' ' in a else a) for a in [cmd] + args])))
  sys.stdout.flush()

if __name__ == '__main__':
  app.run()
  assert sys.version_info >= (3, 6), "Python 3.6 or above is required"
