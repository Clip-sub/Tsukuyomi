from app.extensions import db
import config

if config.USE_MYSQL:
    from sqlalchemy.dialects import mysql

    BinaryType = mysql.BINARY
    TextType = mysql.TEXT
    MediumBlobType = mysql.MEDIUMBLOB
    COL_UTF8_GENERAL_CI = 'utf8_general_ci'
    COL_UTF8MB4_BIN = 'utf8mb4_bin'
    COL_ASCII_GENERAL_CI = 'ascii_general_ci'
else:
    BinaryType = db.Binary
    TextType = db.String
    MediumBlobType = db.BLOB
    COL_UTF8_GENERAL_CI = 'NOCASE'
    COL_UTF8MB4_BIN = None
    COL_ASCII_GENERAL_CI = 'NOCASE'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email
