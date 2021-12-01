from sys import flags
from flask import Blueprint, render_template, request, redirect, url_for
import flask
from flask.helpers import flash
from flask_login import login_user, login_required, logout_user, current_user

from .models import *
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form

    # delete entire User table
    # while 1 == 1:
    #     db.session.query(User).delete()
    #     db.session.commit()
    #     break


    if request.method == 'POST':
        email = data.get('email')
        password = data.get('password')

        my_user = User.query.filter_by(email= email).first()
        if my_user:
            if check_password_hash(my_user.password, password):
                flash('Credentials are corect, redirecting to home page', category='success')
                login_user(my_user, remember=True)
                return redirect(url_for('views.home', user=current_user))
            else:
                flash('Your password is incorrect, please try again', category='error')
        else:
            flash('Your email is incorrect, please try again', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    if request.method == 'POST':
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        flash = flask.flash

        my_user = User.query.filter_by(email= email).first()

        if my_user:
            flash('This email is being used by another account, try a different one', category='error')

        if len(name) < 2:
            flash('Name must have atleast 4 characters', category='error')
        if len(email) < 4:
            flash('Email must have at least 4 characters', category='error')
        if len(password) < 6:
            flash('Password must have a length of at least 6 characters', category='error')
        else:
            new_user = User(name= name, email= email, password=generate_password_hash(password, method='sha256'), county='Timis', city='Timisoara', roof_length=10, roof_width=3, month='Ianuarie', consumption=300)

            print(f'The name of the new user is {new_user.name}')
            login_user(new_user, remember=True)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='succes')

            # return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)