from app.extensions import db
from flask import Flask

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(120), unique = True, nullable = False)
