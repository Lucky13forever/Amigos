import json
from AMIGOS.website.our_classes.Regulator_with_invertor_class import Regulator_with_invertor
def load_all_regulators(address: str):
    data = json.load(address,"r")
    l=[]
    for keys,value in data.items():
        Regulator_with_invertor