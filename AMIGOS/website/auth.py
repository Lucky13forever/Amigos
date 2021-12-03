from os import error
from sys import flags
from types import new_class
from flask import Blueprint, render_template, request, redirect, url_for
import flask
from flask.helpers import flash
from flask_login import login_user, login_required, logout_user, current_user
import json

from .models import *
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)



new_user = {
    'name' : "",
    'email' : "",
    'password' : "",
    'phone' : "",
    'county' : "",
    'city' : "",
    'roof_length' : 0.0,
    'roof_width' : 0.0,
    'month' : "",  
    'consumption' : 0,
}

@auth.route('/SIgnInSignUp', methods=['GET', 'POST'])
def SIgnInSignUp():
    data = request.form

    if request.method == 'POST':

        state = data.get('state')
        if state == 'create':
        
            global new_user
            
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            phone = data.get('phone')
            county = data.get('county')
            city = data.get('city')

            new_user['name'] = name
            new_user['email'] = email
            new_user['password'] = password
            new_user['phone'] = phone
            new_user['county'] = county
            new_user['city'] = city

            print(new_user)
            print(f'STATE ____________ {state}')
        else:
            print(f'STATE_____________ {state}')


    # while 1 == 1:
    #     db.session.query(User).delete()
    #     db.session.commit()
    #     break
    return render_template('SIgnInSignUp.html', user=current_user)






@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form

    # delete entire User table
    # while 1 == 1:
    #     db.session.query(User).delete()
    #     db.session.commit()
    #     break

    old_info = []

    if request.method == 'POST':
        email = data.get('email')
        password = data.get('password')

        old_info.append(email)

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

    return render_template("login.html", old_info=old_info, user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


def load_cities():
   orase = {}
   with open('AMIGOS/website/database/orase.json', 'r') as file:
      orase = json.load(file)
      for key in orase.keys():
          orase[key] = sorted(orase[key])

   return orase

def load_months():
    return ['Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie', 'August', 'Septembrie', 'Octombrie', 'Noiembrie', 'Decembrie']


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    old_info = ["", "", "", 'Alba', "", "", "", 'Ianuarie', ""]
    error = 0

    orase = load_cities()
    months = load_months()


    if request.method == 'POST':
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        county = data.get('county')
        city = data.get('city')
        roof_length = data.get('roof_length')
        roof_width = data.get('roof_width')
        month = data.get('month')
        consumption = data.get('consumption')
        phone = data.get('phone')
        
        
        
        refresh = data.get('refresh')




        print(f'This is the county {county}')
        
        
        print(f"AICI BA {data.get('refresh')}")


        old_info = [name, email, password, county, city, roof_length, roof_width, month, consumption, phone]

        flash = flask.flash

        my_user = User.query.filter_by(email= email).first()

        if refresh != 'refresh':

            if len(name) < 2:
                flash('Name must have atleast 2 characters', category='error')
                error = 1
            if len(email) < 4:
                flash('Email must have at least 4 characters', category='error')
                error = 1
            if my_user:
                flash('This email is being used by another account, try a different one', category='error')
                error = 1
            if len(password) < 6:
                flash('Password must have a length of at least 6 characters', category='error')
                error = 1

            if roof_length == "":
                flash('Please enter a roof length', category='error')
                error = 1
            if roof_width == "":
                flash('Please enter a roof width', category='error')
                error = 1
            if consumption == "":
                flash("Please enter a consumption", category='error')
                error = 1

            if error == 0:
                new_user = User(name= name, email= email, password=generate_password_hash(password, method='sha256'), phone=phone, county=county, city=city, roof_length=roof_length, roof_width=roof_width, month=month, consumption=consumption)

                print(f'The name of the new user is {new_user.name}')
                login_user(new_user, remember=True)
                db.session.add(new_user)
                db.session.commit()
                flash('Account created', category='succes')

                return redirect(url_for('views.home'))


    return render_template("sign-up.html", months=months, orase=orase, old_info=old_info, user=current_user)