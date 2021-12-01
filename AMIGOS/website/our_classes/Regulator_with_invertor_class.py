# Osman Raluca, Vlad Neagoe
import json


class Regulator_with_invertor :
    def __init__(self,name:str,power:str,charging:int,price:int,link:str,picture:str):
        self.name=name
        self.power=power
        self.charging=charging
        self.price=price
        self.link=link
        self.picture=picture

def load_all_regulators(address = "website/database/invertor_cu_regulator.json"):
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