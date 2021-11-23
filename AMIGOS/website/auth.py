from sys import flags
from flask import Blueprint, render_template, request, redirect, url_for
import flask
from flask.helpers import flash

from .models import *
from werkzeug.security import generate_password_hash, check_password_hash

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
            new_user = User(name= name, email= email, password=generate_password_hash(password, method='sha256'))
            
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='succes')

            return redirect(url_for('views.home'))

    return render_template("sign-up.html")