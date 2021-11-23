from enum import unique
from . import db
from flask_login import UserMixin

# id, name, email, password, county, city, phone, avg_consumption, surface

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    