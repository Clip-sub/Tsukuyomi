import sys

TEST_PATHS = ['tests']
DATABASE_URI = 'mysql://username:password@server/db'

def print_cmd(cmd, args):
  print('Running: {0}\n'.format(
    ' '.join([('\'' + a + '\'' if ' ' in a else a) for a in [cmd] + args])))
  sys.stdout.flush()

if __name__ == '__main__':
  assert sys.version_info >= (3, 6), "Python 3.6 or above is required"
