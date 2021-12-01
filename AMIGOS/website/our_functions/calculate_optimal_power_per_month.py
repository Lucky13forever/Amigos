#Lucian Muntiu si Vlad Neagoe
def calculate_optimal_power_per_month(total_power: int):
    energy_for_a_day = total_power * 5
    energy_for_a_month = energy_for_a_day * 30 # energia pe o luna in W
    energy_for_a_month_kW = energy_for_a_month / 1000