# Bulzan Nicola, Soreata Eduard, Iovescu Razvan

def calculate_annual_savings (price_per_kW: float, monthly_cost_without_system: list, monthly_cost_with_system: list):
    s=int(0)
    for i in range(0, 12):
        s += monthly_cost_without_system[i] - monthly_cost_with_system[i]
    s=s*price_per_kW
    return s
