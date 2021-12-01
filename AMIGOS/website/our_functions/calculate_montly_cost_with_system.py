#Trif Rares, Sabau Paula
def calculate_montly_cost_with_system(price_per_kW :float, user_consumption :list, energy_production :list):
    month_cost=[0]*12 #initializez lista
    for i in range(12):
        if energy_production[i] <= user_consumption[i]:
            month_cost[i]= (user_consumption[i] - energy_production[i])* price_per_kW
    return month_cost 
