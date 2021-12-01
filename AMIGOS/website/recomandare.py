from .our_classes.Regulator_with_invertor_class import *
import sys
from .our_classes.panou_class import *
from .our_classes.accumulator_class import *
import json


def load_region_dict(address = "website/database/regiuni.json"):
    try:
        file = open(address, "r")
        data = json.load(file)
        return data
    except FileExistsError:
        raise "FileReadError"
    except FileNotFoundError:
        raise "FileNotFound"



def get_percent(x,y):
    y=(y*x)//100
    return y



def get_region_effic(region_dict,city):
    for i in range(1,6):
        if city in region_dict[str(i)]:
            return(70+6*i)



def get_accumulator_system(all_accumulators:list,required_capacity:int):
    
    d={}
    for i in range(len(all_accumulators)):
        sum=0 # capacitatea totala a unui tip de acumulator
        k=0 #numarul de acumulatori
        while sum<required_capacity:
            sum+=all_accumulators[i].capacity
            k+=1 
        pret = k*all_accumulators[i].price      
        d[i]=[all_accumulators[i].name, sum,k,pret]
    pret_min=sys.maxsize
    #cautam cea mai eficienta optiune
    for keys,value in d.items():
        if value[3]<pret_min: 
            pret_min=value[3]
            ind=keys
    return (all_accumulators[ind], d[ind][2],d[ind][3])



def get_panel_system(all_panels,user_buget,user_length,user_width):
    max_total_power=0
    total_price=0
    number_of_panels=0
    index_panel=-1
    for i in range(len(all_panels)):
        if ((all_panels[i].length<=user_length and all_panels[i].width<=user_width) or (all_panels[i].width<=user_length and all_panels[i].length<=user_width)):
            if user_length//all_panels[i].length*user_width//all_panels[i].width>user_length//all_panels[i].width*user_width//all_panels[i].length:
                max_number_of_panel=user_length//all_panels[i].length*user_width//all_panels[i].width
            else:
                max_number_of_panel=user_length//all_panels[i].width*user_width//all_panels[i].length
            contor=0
            current_price=0
            current_power=0
            while contor<=max_number_of_panel and current_price+all_panels[i].price<=user_buget:
                contor+=1
                current_price+=all_panels[i].price
                current_power+=all_panels[i].power
            if (current_power>max_total_power) or (current_power==max_total_power and current_price<total_price):
                max_total_power=current_power
                total_price=current_price
                number_of_panels=contor
                index_panel=i
    if index_panel!=-1:
        return (all_panels[index_panel],number_of_panels,max_total_power,total_price)
    return None




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




def get_full_system(user_budget: int,
                    user_width: float,
                    user_length: float,
                    user_location: str,
                    panel_list: list,
                    accumulator_list: list,
                    regulators_with_invertors_list: list,
                    region_dict: dict):
    
    remaining_budget = user_budget
    i = 0.2 #procentul 20%
    ok = 0
    while remaining_budget >= 0.02 * user_budget: #verificam ca bugetul ramas > 2% din bugetul total
        ok = 1 #verificam ca exista macar un panou
        panels = get_panel_system(panel_list, int(user_budget * i), user_length, user_width)
        power = get_percent(panels[2], get_region_effic(region_dict, user_location))
        accumulators = get_accumulator_system(accumulator_list, power)
        regulators = get_regulator_invertor_system(regulators_with_invertors_list, power)
        i += 0.02 #crestem procentul cu 2%
        remaining_budget = user_budget - panels[3] - accumulators[2] - regulators.price
    
    
    return 'BABABUI'
    if ok == 1:
        result = (panels, accumulators, regulators, remaining_budget)
        return result
    else:
        result = ((None, None, None, None), (None, None, None), None, None)
        return result

print(get_full_system(3000, 10, 10, "Timis", load_all_panels(), load_all_accumulators(), load_all_regulators(), load_region_dict()))