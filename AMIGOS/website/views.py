from re import search
from flask import Blueprint, render_template, request, redirect, url_for
import flask
from sqlalchemy.orm.query import Query
from .models import *
from flask_login import login_required, current_user
from .recomandare import *
from .grafice import *
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import random


views = Blueprint('views', __name__)

@views.route('/header_footer_general')
def header_footer_general():


    return render_template('header_footer_general.html', user=current_user, show_system=False )


calculator_step = ""
@views.route('/experimente')
def experimente():
    return render_template('experimente.html', user=current_user, show_system=False, step=calculator_step)

@views.route('/stats')
def stats():
    return render_template('stats.html', user=current_user, table_stats=Stats.query.all())






def generate_users():

    all_users = []

    with open('AMIGOS/website/database/usernames.json', 'r') as file:
        usernames = json.load(file)

        with open('AMIGOS/website/database/orase.json', 'r') as orase_file:
            orase = json.load(orase_file)
            counties = list(orase.keys())

            print(f'COUNTIES: {len(usernames)}')



            m_savings = 0
            m_profits = 0
            m_cons = 0
            m_budget = 0
            for i in range(1, 5_000 + 1):
                name = usernames[i % 4800]
                county = random.choice(counties)
                city = random.choice(orase[county])
                

                cons = random.randint(200, 1000)
                budget = random.randint(6000, 120_000)



                length = random.randint(1, 20)
                width = random.randint(1, 20)

                global result
                result = get_full_system(budget, width, length, county, get_all_panels, get_all_accumulators, get_all_regulators, get_region_dict)


                new_user = User(name= name, email= f'{name}{i}@gmail.com', password=generate_password_hash(f'{name}{i}', method='sha256'), phone='0123456789', county=county, city=city, roof_length=length, roof_width=width, month='November', consumption=cons, budget = budget)
                savings, profits = get_user_stats(result, new_user)
                
                m_budget += budget
                m_savings += savings
                m_profits += profits
                m_cons += cons

                # login_user(new_user, remember=True)
                all_users.append(new_user)
            
                if i % 5_000 == 0:

                    search
                    print('another 5_000')
                    db.session.add_all(all_users)

                    db.session.commit()
                    all_users = []
                    
            imp = 5000
            m_cons /= imp
            m_savings /= imp
            m_profits /= imp
            m_budget /= imp
            nr_users = imp

    new_stats = Stats(m_consumption=m_cons, m_annual_savings=m_savings, m_annual_profits=profits, m_budget=m_budget, nr_users=nr_users)
    db.session.add(new_stats)
    db.session.commit()


@views.route('/profile', methods=['POST', 'GET'])
def profile():
    # try to output usersw
    # table_users = User.query.all()
    # ok = 0
    # for user in table_users:
    #     if user.id==8000:
    #         print('Found 1000')
    #     ok = user.name

    print('DONE')

    # add new users
    # generate_users()
    # add a new Stat

    # stat = Stats(county='Timis', buget=150, annual_savings=500, annual_profits=300)

    # db.session.add(stat)
    # db.session.commit()


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
        try:
            consumption = int(data.get('consumption'))
        except:
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
    print(get_all_panels)

    # generate_users()
    
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
            budget = 120000
        else:
            budget = int(step)

        search = User.query.filter_by(id = user.id).first()

        result = get_full_system(budget, user.roof_width, user.roof_length, user.county, get_all_panels, get_all_accumulators, get_all_regulators, get_region_dict)
       
        if search and search.budget == 0:
            search.budget = budget
            db.session.commit()
            newStat = Stats.query.first()
            newStat.m_consumption = newStat.m_consumption * (newStat.nr_users / (newStat.nr_users + 1)) + user.consumption
            newStat.m_budget = newStat.m_budget * (newStat.nr_users / (newStat.nr_users + 1)) + budget
            newStat.nr_users += 1

            savings, profits = get_user_stats(result, search)
            newStat.m_annual_savings = newStat.m_annual_savings * (newStat.nr_users / (newStat.nr_users + 1)) + savings
            newStat.m_annual_profits = newStat.m_annual_profits * (newStat.nr_users / (newStat.nr_users + 1)) + profits
    
        
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

    consumption_graph = create_consumption_graph(result, user)


    price_per_kW = 0.67
    cost_graph = create_cost_graph(result, price_per_kW, user)

    surplus_graph = create_surplus_graph(result, price_per_kW, user)


    return render_template('graf_test.html', consumption_graph=consumption_graph, cost_graph=cost_graph, surplus_graph=surplus_graph, user=current_user, show_system=False )


@views.route("/graph_consum")
def consum():

    user = current_user
    consumption_graph = create_consumption_graph(result, user)

    
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
    
    user = current_user
    cost_graph = create_cost_graph(result, price_per_kW, user)

    return render_template("graph_cost.html", user=current_user, show_system=True , cost_graph=cost_graph)

@views.route("/graph_surplus", methods=['POST', 'GET'])
def surplus():
    data = request.form

    price_per_kW = 0.23

    if request.method == 'POST':
        price_per_kW = float(data.get('price_per_kW'))

    
    user=current_user
    surplus_graph = create_surplus_graph(result, price_per_kW, user)
    return render_template("graph_surplus.html", user=current_user, show_system=True, surplus_graph=surplus_graph)