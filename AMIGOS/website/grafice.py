from .our_classes.graph_class import Graph
from .models import User
from flask_login import current_user
from .our_functions.get_region_effic import get_region_effic
from .our_functions.get_percent import get_percent
from .our_functions.load_region_dict import load_region_dict
from .our_functions.apply_percent import apply_percent

monthly_consumption = [9.3, 8.7, 9, 8.5, 7.6, 7.8, 8.4, 8.4, 7.5, 8, 8.2, 8.7]
monthly_effic = [50, 59, 78, 85, 90, 93, 100, 95, 86, 73, 57, 48]

def calculate_annual_consumption(montly_consumption,month,consumption):
    months=["ianuarie","februarie","martie","aprilie","mai","iunie","iulie","august","septembrie","octombrie","noiembrie","decembrie"]
    month=month.lower()
    index_month=months.index(month)
    return int(consumption*(100/montly_consumption[index_month]))

def calculate_user_consumption(monthly_consumption: list, annual_consumption: int): #definesc functia
    rez=[] #creez o noua lista care va contine consumul lunar
    for i in range(len(monthly_consumption)): #parcurg lista
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


# result is the recommended system
def create_consumption_graph(result) -> Graph:
    user = current_user
    annual_consumption = calculate_annual_consumption(monthly_consumption, user.month, user.consumption)
    
    # column 1
    user_consumption = calculate_user_consumption(monthly_consumption, annual_consumption)
    
    print(f'Consumul anual este {annual_consumption}')
    print(f'From grafice I have this\nUser consumption: {user_consumption}')
    optimal_power = calculate_optimal_power_per_month(result[0][2])
    print(f'This is optimal: {optimal_power}')
    
    # column 2
    energy_production = calculate_energy_production(optimal_power, load_region_dict(), user.county, monthly_effic)
    print(f'Energy produced is {energy_production}')


    # now let's create the consumption graph

    consumption_graph = Graph(user_consumption, energy_production)
    print(f'This is max_point {consumption_graph.max_point}')
    print(f'This is the y_axis: {consumption_graph.yaxis_values}')
    print(f'This is the first column : {consumption_graph.colums1}')
    print(f'This is the second column : {consumption_graph.colums2}')

    return consumption_graph