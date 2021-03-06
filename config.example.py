import os
import re

DEBUG = True

# A read-only maintenance mode, in which the database is not modified
MAINTENANCE_MODE = False
# A maintenance message (used in layout.html template)
MAINTENANCE_MODE_MESSAGE = 'Site is currently in read-only maintenance mode.'
# Allow logging in during maintenance (without updating last login date)
MAINTENANCE_MODE_LOGINS = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_CONNECT_OPTIONS = {}

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'd731ad92-82ef-48f1-8844-ae935b2761d8'

# Use MySQL or Sqlite3 (mostly deprecated)
USE_MYSQL = True

# Enable password recovery (by reset link to given email address)
# Depends on email support!
ALLOW_PASSWORD_RESET = True

if USE_MYSQL:
    SQLALCHEMY_DATABASE_URI = ('mysql://test:test123@localhost/tsukuyomi?charset=utf8mb4')
else:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(BASE_DIR, 'test.db') + '?check_same_thread=False')
