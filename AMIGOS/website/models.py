from enum import unique
from . import db
from flask_login import UserMixin

# id, name, email, password, county, city, phone, avg_consumption, surface
# UserMixin is used for flask-login -> current_user
# when adding new columns, i need to delete database.db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    phone = db.Column(db.String(150))
    county = db.Column(db.String(150))
    city = db.Column(db.String(150))
    roof_length = db.Column(db.Float)
    roof_width = db.Column(db.Float)
    month = db.Column(db.String(150))
    consumption = db.Column(db.Integer)
    budget = db.Column(db.Integer)
    #annual_savings = db.Column(db.Integer)
    #annual_profits = db.Column(db.Integer)

class Stats(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    m_consumption = db.Column(db.Integer)
    m_annual_savings = db.Column(db.Integer)
    m_annual_profits = db.Column(db.Integer)
    m_budget = db.Column(db.Integer)
    nr_users = db.Column(db.Integer)






