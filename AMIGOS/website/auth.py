from flask import Blueprint, render_template, request

from .our_classes.user_class import User

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
        User.create_new_user(name, email, password, 'Timis', 'Timisoara', '1234567890', 300, 50)
    return render_template("sign-up.html")