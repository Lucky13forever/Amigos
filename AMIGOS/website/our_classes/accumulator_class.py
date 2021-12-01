import json


class Accumulator:
 
    def __init__(self, name :str, type :str, capacity :int, price :int, link :str, picture :str):
        self.name=name
        self.type=type
        self.capacity=capacity
        self.price=price
        self.link=link
        self.picture=picture

def load_all_accumulators(address = "website/database/acumulatori.json"):
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

# nume=input()
# tip=input()
# capacitate=int(input())
# pret=int(input())
# linc=input()
# poza=input()
# obj=Accumulator(nume,tip,capacitate,pret,linc,poza)
# print(obj.name)

#Cazan Dorin