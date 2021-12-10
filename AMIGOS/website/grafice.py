from .our_classes.graph_class import Graph
from .models import User
from flask_login import current_user
from .our_functions.get_region_effic import get_region_effic
from .our_functions.get_percent import get_percent
from .our_functions.load_region_dict import load_region_dict
from .our_functions.apply_percent import apply_percent

monthly_consumption = [9.3, 8.7, 9, 8.5, 7.6, 7.8, 8.4, 8.4, 7.5, 8, 8.2, 8.7]
monthly_effic = [50, 59, 78, 85, 90, 93, 100, 95, 86, 73, 57, 48]

month_provided_index = None
consumption_provided = None

def calculate_annual_consumption(montly_consumption,month,consumption):
    months=['january', 'jebruary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    
    global month_provided_index
    global consumption_provided

    month=month.lower()
    index_month=months.index(month)

    month_provided_index = index_month
    consumption_provided = consumption
    
    return int(consumption*(100/montly_consumption[index_month]))

def calculate_user_consumption(monthly_consumption: list, annual_consumption: int): #definesc functia
    rez=[] #creez o noua lista care va contine consumul lunar
    for i in range(len(monthly_consumption)): #parcurg lista
        if i == month_provided_index:
            rez.append(consumption_provided)
        else:
            rez.append(int(monthly_consumption[i]/100*annual_consumption)) #adaug in lista consumul calculat
    return rez #returnez lista creata

def calculate_optimal_power_per_month(total_power: int):
    energy_for_a_day = total_power * 5
    energy_for_a_month = energy_for_a_day * 30 # energia pe o luna in W
    energy_for_a_month_kW = energy_for_a_month / 1000
    return int(energy_for_a_month_kW)

def calculate_energy_production(power: int, region_dict: dict, county: str, monthly_effic: list):
    region_effic = get_region_effic(region_dict, county)
    result = []
    for each_month in monthly_effic:
        result.append(int(apply_percent(apply_percent(power, region_effic), each_month)))
    return result

def calculate_monthly_cost_without_system(price_per_kW: float, monthly_user_consumption: list):
    monthly_price = []
    for each_month in monthly_user_consumption:
        monthly_price.append(int(each_month * price_per_kW))
    return monthly_price

def calculate_montly_cost_with_system(price_per_kW :float, user_consumption :list, energy_production :list):
    month_cost=[0]*12 #initializez lista
    for i in range(12):
        if energy_production[i] <= user_consumption[i]:
            month_cost[i]= int((user_consumption[i] - energy_production[i])* price_per_kW)
    return month_cost 

def calculate_annual_savings (monthly_cost_without_system: list, monthly_cost_with_system: list):
    s=int(0)
    for i in range(0, 12):
        s += monthly_cost_without_system[i] - monthly_cost_with_system[i]
    return s

def calculate_surplus_gain(price_per_kW :float, user_consumption :list, energy_production :list):
    l=[]
    for i in range(len(user_consumption)):
        if user_consumption[i]>energy_production[i]:
            l.append(0)
        else:
            val=int( (energy_production[i]-user_consumption[i]) * price_per_kW)
            l.append(val)
    return l

def calculate_surplus_profit(price_per_kW,monthly_profit):
    s=0
    for i in monthly_profit:
        s=s+i
    return s






# result is the recommended system
#this are measured in kW
user_consumption = 0
energy_production = 0
def create_consumption_graph(result, user) -> Graph:
    # user = current_user
    annual_consumption = calculate_annual_consumption(monthly_consumption, user.month, user.consumption)
    
    # column 1
    global user_consumption
    user_consumption = calculate_user_consumption(monthly_consumption, annual_consumption)
    
    # print(f'Consumul anual este {annual_consumption}')
    # print(f'From grafice I have this\nUser consumption: {user_consumption}')
    optimal_power = calculate_optimal_power_per_month(result[0][2])
    # print(f'This is optimal: {optimal_power} from {result[0][2]}')
    
    # column 2
    global energy_production
    energy_production = calculate_energy_production(optimal_power, load_region_dict(), user.county, monthly_effic)
    # print(f'Energy produced is {energy_production}')


    # now let's create the consumption graph

    consumption_graph = Graph(user_consumption, energy_production)
    # print(f'This is max_point {consumption_graph.max_point}')
    # print(f'This is the y_axis: {consumption_graph.yaxis_values}')
    # print(f'This is the first column : {consumption_graph.colums1}')
    # print(f'This is the second column : {consumption_graph.colums2}')

    return consumption_graph


annual_savings = 0


def create_cost_graph(result, price_per_kW, user):
    
    create_consumption_graph(result, user)



    monthly_cost_without_system = calculate_monthly_cost_without_system(price_per_kW, user_consumption)

    monthly_cost_with_system = calculate_montly_cost_with_system(price_per_kW, user_consumption, energy_production)

    global annual_savings
    annual_savings = calculate_annual_savings(monthly_cost_without_system, monthly_cost_with_system)


    cost_graph = Graph(monthly_cost_without_system, monthly_cost_with_system)
    cost_graph.annual_savings = annual_savings


    # print(f'This is monthly_cost_without: {monthly_cost_without_system}')
    # print(f'This is monthly_cost_wit_system: {monthly_cost_with_system}')
    # print(f'This is annual savings : {annual_savings}')
    
    return cost_graph

annual_profits = 0
def create_surplus_graph(result, price_per_kW, user):
    
    create_consumption_graph(result, user)

    surplus_gain = calculate_surplus_gain(price_per_kW, user_consumption, energy_production)

    surplus_profit = calculate_surplus_profit(price_per_kW, surplus_gain)

    surplus_graph = Graph(surplus_gain, surplus_gain)
    surplus_graph.annual_profit = surplus_profit

    global annual_profits
    annual_profits = surplus_profit

    # print(f'This is surplus: {surplus_gain}')

    return surplus_graph

def get_user_stats(result, user):
    create_consumption_graph(result, user)
    create_cost_graph(result, 0.67, user)
    create_surplus_graph(result, 0.23, user)

    return annual_savings, annual_profits