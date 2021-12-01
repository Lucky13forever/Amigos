from flask import Blueprint, render_template
from .models import *
from flask_login import login_required, current_user
from .recomandare import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
    
    # return render_template("home.html", user=current_user)

    # prblema daca bugetul e prea mic, NonType Error
    # result = get_full_system(2000, 10, 10, "Constanta", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())
    # Suma ramasa din buget e -1727, deci as pune userul sa plateasca aproape dublu
    # ToDo: daca nu reusim sa gasim niciun sistem, fix la return
    result = get_full_system(10000, 10, 10, "Satu-Mare", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())
    
    print(result)

    ok = 1
    if result[0][0] == None:
        ok = 0
    
    panouri = result[0]
    acumulatori = result[1]
    regulatori = result[2]
    ramas_din_buget = result[3]
    return render_template("home.html", panouri=panouri, acumulatori=acumulatori, regulatori=regulatori, ramas=ramas_din_buget, ok = ok, user=current_user) #User.query.all()


@views.route('/test')
def test():
    
    # return render_template("home.html", user=current_user)

    # prblema daca bugetul e prea mic, NonType Error
    # result = get_full_system(2000, 10, 10, "Constanta", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())
    # Suma ramasa din buget e -1727, deci as pune userul sa plateasca aproape dublu
    # ToDo: daca nu reusim sa gasim niciun sistem, fix la return
    result = get_full_system(120000, 10, 10, "Constanta", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())
    
    print(result)

    ok = 1
    if result[0][0] == None:
        ok = 0
    
    panouri = result[0]
    acumulatori = result[1]
    regulatori = result[2]
    ramas_din_buget = result[3]
    return render_template("test.html", panouri=panouri, acumulatori=acumulatori, regulatori=regulatori, ramas=ramas_din_buget, ok = ok, user=current_user) #User.query.all()
