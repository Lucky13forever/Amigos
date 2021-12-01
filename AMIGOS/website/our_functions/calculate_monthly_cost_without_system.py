# Cinteza Emilian


def calculate_monthly_cost_without_system(price_per_kW: float, monthly_user_consumption: list):
    monthly_price = []
    for each_month in monthly_user_consumption:
        monthly_price.append(each_month * price_per_kW)
    return monthly_price
