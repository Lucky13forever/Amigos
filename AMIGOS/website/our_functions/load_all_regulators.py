#Birla Alexandru si Puscasu Vlad
import json
from our_classes.Regulator_with_invertor_class import Regulator_with_invertor
def load_all_regulators(address: str):
    try:
        with open(address, "r") as file:
            data = json.load(file)
            l=[]
            for keys,value in data.items():
                panou=Regulator_with_invertor(value["name"],value["power"],value["charging"],value["price"],value["link"], value["picture"])
                l.append(panou)
        return l
    except FileExistsError:
        print("FileReadError")
