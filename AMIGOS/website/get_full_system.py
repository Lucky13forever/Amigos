"""
Cinteza Emilian
Bulzan Nicola
Cucu Raul
Melnic Katalin
Radu Apreotesei
"""


def get_full_system(self,
                    user_budget: int,
                    user_surface: float,
                    user_location: str,
                    panel_list: Panels,
                    accumulator_list: Accumulator,
                    regulators_with_invertors_list: Regulator_with_invertor,
                    region_dict: dict):
    remaining_budget = user_budget
    i = 0.2 #procentul 20%
    ok = 0
    while remaining_budget >= 0.02 * user_budget: #verificam ca bugetul ramas > 2% din bugetul total
        ok = 1 #verificam ca exista macar un panou
        panels = get_panel_system(panel_list, int(user_budget * i), user_surface)
        power = get_percent(panels[2], get_region_effic(region_dict, user_budget))
        accumulators = get_accumulator_system(accumulator_list, power)
        regulators = get_regulator_invertor_system(regulators_with_invertors_list, power)
        i += 0.02 #crestem procentul cu 2%
        remaining_budget = user_budget - panels[3] - accumulators[2] - regulators.price
    if ok == 1:
        result = set(panels, accumulators, regulators, remaining_budget)
        return result
    else:
        result = ((None, None, None), (None, None, None), None, None)
        return result

"""
exemplu
100 - bugetul total
(bugetul total - pret panels - pret acumulatori - pret regulatori = buget ramas)
100 - 1 -1 -1 = 97 
97 >= 2
100 -2 -2 -2 = 94
94 >= 2
100 -50 -40 -19 = 1
1 => 2
"""