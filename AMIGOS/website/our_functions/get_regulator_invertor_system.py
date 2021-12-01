# Sabau Paula, Trif Catalin

from our_classes import Regulator_with_invertor

def get_regulator_invertor_system(all_regulators_with_invertors: list,required_power: int):
    reg_exist = 0 #check if regulator exists
    for i in range(len(all_regulators_with_invertors)):
        if all_regulators_with_invertors[i].power >= required_power:
            if reg_exist == 0:
                regulator_invertor = all_regulators_with_invertors[i]
                reg_exist = 1
                point = i #indice element
            else:
                if all_regulators_with_invertors[i].price <= all_regulators_with_invertors[point].price:
                    regulator_invertor = all_regulators_with_invertors[i]
                    point = i

    if reg_exist==0:
        return None
    else:
        return regulator_invertor
