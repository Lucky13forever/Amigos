#Balutoiu Deian, Birla Alexandru si Puscasu Vlad
import json
from our_classes.accumulator_class import Accumulator
def load_all_accumulators(address: str):
    try:
        with open(address, "r") as file:
            data = json.load(file)
            l=[]
            for keys,value in data.items():
                acc=Accumulator(value["name"],value["type"],value["capacity"],value["price"],value["link"],value["picture"])
                l.append(acc)
        return l
    except FileExistsError:
        print("FileReadError")
    