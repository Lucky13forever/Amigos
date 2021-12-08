from flask import Blueprint, render_template, request, redirect, url_for
import flask
from sqlalchemy.orm.query import Query
from .models import *
from flask_login import login_required, current_user
from .recomandare import *
from .grafice import *
import json
from werkzeug.security import generate_password_hash, check_password_hash


views = Blueprint('views', __name__)


@views.route('/header_footer_general')
def header_footer_general():

    return render_template('header_footer_general.html', user=current_user, show_system=False )


calculator_step = ""
@views.route('/experimente')
def experimente():
    return render_template('experimente.html', user=current_user, show_system=False, step=calculator_step)

@views.route('/profile', methods=['POST', 'GET'])
def profile():
    data = request.form

    if request.method == 'POST':
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        new_password = data.get('password')


        county = data.get('county')
        city = data.get('city')
        month = data.get('month')
        roof_length = data.get('roof_length')
        roof_width = data.get('roof_width')
        consumption = data.get('consumption')


        search_user = User.query.filter_by(id=current_user.id).first()
        if search_user:
            search_user.name = name
            search_user.email = email
            search_user.phone = phone
            search_user.county = county
            search_user.city = city
            search_user.month = month
            search_user.roof_length = roof_length
            search_user.roof_width = roof_width
            search_user.consumption = consumption

            if new_password != "":
                password = generate_password_hash(new_password, method='sha256')
                search_user.password = password

            db.session.commit()

        print(county, city, month, consumption)
    return render_template('profile.html', user=current_user, show_system=False )


@views.route('/')
def home():
    
    # return render_template("home.html", user=current_user, show_system=False )

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
    return render_template("home.html", user=current_user, show_system=False ) #User.query.all()




result = ((None, None, None, None), (None, None, None), None, None)

pictures = [None, None, None]
budget = None
@views.route("/system")
def system():
    try:
        return render_template('system.html', user=current_user, show_system=True , step=calculator_step, result=result, pictures=pictures, budget=budget)
    except:
        return redirect(url_for("views.calculator", user=current_user, show_system=False, low_buget=True ))

get_all_panels = load_all_panels()
get_all_accumulators = load_all_accumulators()
get_all_regulators = load_all_regulators()
get_region_dict = load_region_dict()

@views.route("/calculator", methods=['POST', 'GET'])
def calculator():

    global result
    global calculator_step
    global pictures
    global budget
    user = current_user
    
    # result = get_full_system(10000, user.roof_width , user.roof_length, user.county , load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())

    data = request.form

    if request.method == 'POST':
        step = data.get('step')
        calculator_step = step

        if step == "full_solar":
            budget = 500000
        else:
            budget = int(step)

        result = get_full_system(budget, user.roof_width, user.roof_length, user.county, get_all_panels, get_all_accumulators, get_all_regulators, get_region_dict)
        
        return redirect(url_for("views.system", user=current_user, show_system=False , step=calculator_step, result=result, pictures=pictures, budget=budget))


    return render_template("calculator.html", user=current_user, low_budget=False, show_system=False )

@views.route('/test')
def test():
    
    # return render_template("home.html", user=current_user, show_system=False )

    # prblema daca bugetul e prea mic, NonType Error
    # result = get_full_system(2000, 10, 10, "Constanta", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())
    # Suma ramasa din buget e -1727, deci as pune userul sa plateasca aproape dublu
    # ToDo: daca nu reusim sa gasim niciun sistem, fix la return
    user = current_user

    result = get_full_system(1000000, 2000 , 2000, user.county , load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())


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
    return render_template("test.html", orase = orase, panouri=panouri, acumulatori=acumulatori, regulatori=regulatori, ramas=ramas_din_buget, pret_sistem = pret_sistem, ok = ok, user=current_user, show_system=False ) #User.query.all()


@views.route('/database')
def database():

    rows = User.query.count()

    return render_template('database.html', user=current_user, show_system=False , table_user=User.query.all(), rows=rows)

@views.route('/graf_test')
def graf_test():

    global result
    user = current_user
    
    result = get_full_system(40000, user.roof_width , user.roof_length, user.county , load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict())

    consumption_graph = create_consumption_graph(result)


    price_per_kW = 0.67
    cost_graph = create_cost_graph(result, price_per_kW)

    surplus_graph = create_surplus_graph(result, price_per_kW)


    return render_template('graf_test.html', consumption_graph=consumption_graph, cost_graph=cost_graph, surplus_graph=surplus_graph, user=current_user, show_system=False )


@views.route("/graph_consum")
def consum():


    consumption_graph = create_consumption_graph(result)
    return render_template("graph_consum.html", user=current_user, show_system=True , consumption_graph=consumption_graph)

@views.route("/graph_cost", methods=['POST', 'GET'])
def cost():
    data = request.form

    price_per_kW = 0.67

    if request.method == 'POST':
        price_per_kW = float(data.get('price_per_kW'))

    # price_per_kW = 0.67
    print(f'THIS IS PRICE: {price_per_kW}')
    print(f'type: {type(price_per_kW)}')
    cost_graph = create_cost_graph(result, price_per_kW)

    return render_template("graph_cost.html", user=current_user, show_system=True , cost_graph=cost_graph)

@views.route("/graph_surplus", methods=['POST', 'GET'])
def surplus():
    data = request.form

    price_per_kW = 0.67

    if request.method == 'POST':
        price_per_kW = float(data.get('price_per_kW'))

    
    surplus_graph = create_surplus_graph(result, price_per_kW)
    return render_template("graph_surplus.html", user=current_user, show_system=True, surplus_graph=surplus_graph)