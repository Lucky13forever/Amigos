#Despina Cojocaru
def calculate_energy_production(power: int, region_dict: dict, county: str, monthly_effic: list):
    region_effic = get_region_effic(region_dict, county)
    result = []
    for each_month in monthly_effic:
        result.append(get_percent(power, region_effic)+each_month)
    return result