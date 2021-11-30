class Accumulator:
 
    def __init__(self, name :str, type :str, capacity :int, price :int, link :str, picture :str):
        self.name=name
        self.type=type
        self.capacity=capacity
        self.price=price
        self.link=link
        self.picture=picture

nume=input()
tip=input()
capacitate=int(input())
pret=int(input())
linc=input()
poza=input()
obj=Accumulator(nume,tip,capacitate,pret,linc,poza)
print(obj.name)

#Cazan Dorin