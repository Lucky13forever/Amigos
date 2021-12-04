from flask import Blueprint, render_template, request, redirect, url_for
import flask
from sqlalchemy.orm.query import Query
from .models import *
from flask_login import login_required, current_user
from .recomandare import *
from .grafice import *
import json


views = Blueprint('views', __name__)


@views.route('/header_footer_general')
def header_footer_general():

    return render_template('header_footer_general.html', user=current_user)


@views.route('/profile', methods=['POST', 'GET'])
def profile():
    data = request.form

    if request.method == 'POST':
        county = data.get('county')
        city = data.get('city')
        month = data.get('month')
        roof_length = data.get('roof_length')
        roof_width = data.get('roof_width')
        consumption = data.get('consumption')

        search_user = User.query.filter_by(id=current_user.id).first()
        if search_user:
            search_user.county = county
            search_user.city = city
            search_user.month = month
            search_user.roof_length = roof_length
            search_user.roof_width = roof_width
            search_user.consumption = consumption

            db.session.commit()

        print(county, city, month, consumption)
    return render_template('profile.html', user=current_user)


@views.route('/')
def home():
    
    # return render_template("home.html", user=current_user)

    # prblema daca bugetul e prea mic, NonType Error
    # result = get_full_system(2000, 10, 10, "Constanta", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())
    # Suma ramasa din buget e -1727, deci as pune userul sa plateasca aproape dublu
    # ToDo: daca nu reusim sa gasim niciun sistem, fix la return
    # result = get_full_system(10000, 10, 10, "Satu-Mare", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())
    
    # print(result)

    # ok = 1
    # if result[0][0] == None:
    #     ok = 0
    
    # panouri = result[0]
    # acumulatori = result[1]
    # regulatori = result[2]
    # ramas_din_buget = result[3]
    return render_template("home.html", user=current_user) #User.query.all()


@views.route('/calculator')
def calculator():
    return render_template('calculator.html', user=current_user)

result = ((None, None, None, None), (None, None, None), None, None)
@views.route("/buget")
def buget():
    global result
    user = current_user
    
    result = get_full_system(10000, user.roof_width , user.roof_length, user.county , load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())

    return render_template("buget.html", user=current_user)

@views.route('/test')
def test():
    
    # return render_template("home.html", user=current_user)

    # prblema daca bugetul e prea mic, NonType Error
    # result = get_full_system(2000, 10, 10, "Constanta", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())
    # Suma ramasa din buget e -1727, deci as pune userul sa plateasca aproape dublu
    # ToDo: daca nu reusim sa gasim niciun sistem, fix la return
    user = current_user

    result = get_full_system(40000, user.roof_width , user.roof_length, user.county , load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())


    orase = {}
    with open('AMIGOS/website/database/orase.json', 'r') as file:
        orase = json.load(file)

    print(result)

    ok = 1
    if result[0][0] == None:
        ok = 0
    
    panouri = result[0]
    acumulatori = result[1]
    regulatori = result[2]
    ramas_din_buget = result[3]

    pret_sistem = result[0][3] + result[1][2] + result[2].price
    return render_template("test.html", orase = orase, panouri=panouri, acumulatori=acumulatori, regulatori=regulatori, ramas=ramas_din_buget, pret_sistem = pret_sistem, ok = ok, user=current_user) #User.query.all()


@views.route('/database')
def database():

    return render_template('database.html', user=current_user, table_user=User.query.all())

@views.route('/graf_test')
def graf_test():

    global result
    user = current_user
    
    result = get_full_system(40000, user.roof_width , user.roof_length, user.county , load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())

    consumption_graph = create_consumption_graph(result)


    price_per_kW = 0.67
    cost_graph = create_cost_graph(result, price_per_kW)

    surplus_graph = create_surplus_graph(result, price_per_kW)


    return render_template('graf_test.html', consumption_graph=consumption_graph, cost_graph=cost_graph, surplus_graph=surplus_graph, user=current_user)