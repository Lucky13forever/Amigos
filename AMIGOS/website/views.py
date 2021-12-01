from flask import Blueprint, render_template
from .models import *
from flask_login import login_required, current_user
from .recomandare import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
    
    # return render_template("home.html", user=current_user)

    result = get_full_system(3000, 10, 10, "Timis", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())
    panouri = result[0]
    return render_template("home.html", panouri=panouri, user=current_user) #User.query.all()

