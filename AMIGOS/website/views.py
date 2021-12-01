from flask import Blueprint, render_template
from .models import *
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    
    return render_template("home.html", user=current_user)
    # return render_template("home.html", table_user=User.query.all(), user=current_user)