from enum import unique
from . import db
from flask_login import UserMixin

# id, name, email, password, county, city, phone, avg_consumption, surface
# UserMixin is used for flask-login -> current_user
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    county = db.Column(db.String(150))
    city = db.Column(db.String(150))
    roof_length = db.Column(db.Integer)
    roof_width = db.Column(db.Integer)
    month = db.Column(db.String(150))
    consumption = db.Column(db.Integer)
    