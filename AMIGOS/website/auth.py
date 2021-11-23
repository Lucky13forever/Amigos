from sys import flags
from flask import Blueprint, render_template, request
import flask
from flask.helpers import flash

from AMIGOS.website.our_classes.user_class import User

from . import models

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", user="Emanuel", boolean=False)

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    if request.method == 'POST':
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        flash = flask.flash

        if len(name) < 2:
            flash('Name must have atleast 4 characters', category='error')
        if len(email) < 4:
            flash('Email must have at least 4 characters', category='error')
        if len(password) < 6:
            flash('Password must have a length of at least 6 characters', category='error')
        else:
            new_user = User()
            flash('Account created', category='succes')
        User.create_new_user(name, email, password, 'Timis', 'Timisoara', '1234567890', 300, 50)
    return render_template("sign-up.html")