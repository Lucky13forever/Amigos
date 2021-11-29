"""
Cinteza Emilian
Bulzan Nicola
Cucu Raul
Melnic Katalin
Radu Apreotesei
"""
from our_classes.panou_class import Panels
from our_classes.accumulator_class import Accumulator
from our_classes.Regulator_with_invertor_class import Regulator_with_invertor
# from our_classes.get_panel_system import get_panel_system


class get_system:
    def get_full_system(self, user_budget: int, user_surface: float, user_location: str, panel_list: Panels,
                        accumulator_list: Accumulator,
                        regulators_with_invertors: Regulator_with_invertor,
                        region_dict: dict):
        print("This is just so i can see there is no error")
