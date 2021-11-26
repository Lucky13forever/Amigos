import json


class Panels:
      
      def __init__(self, model, pret, suprafata, putere):
            self.model = model
            self.price = pret
            self.surface = suprafata
            self.power = putere

all_panels = []
def load_all_panels():
      global all_panels

      with open("AMIGOS/website/database/panouri.json", "r") as pan_file:
            my_dict = json.load(pan_file)

      for pan in my_dict.values():
            all_panels.append(Panels(pan["type"], pan["price"], pan["size"], pan["power"]))
      
      return all_panels


      