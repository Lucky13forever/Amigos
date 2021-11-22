from flask import Blueprint, render_template

from .our_classes.user_class import User

views = Blueprint('views', __name__)

@views.route('/')
def home():
    print(User.check_if_in_database('Emanuel', 'lugobugo'))
    print(User.get_table_user())
    print(User.check_if_in_database("Vlad", "vladboss"))
    return render_template("home.html", table_user=User.get_table_user())