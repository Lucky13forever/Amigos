import json

class Panels:
      
      def __init__(self, name: str, type:str, power: int, length: float, width: float, price: int, picture: str, link: str):
            self.name = name
            self.type = type
            self.power = power
            self.length = length
            self.width = width
            self.price = price
            self.picture = picture
            self.link = link


def load_all_panels():
      all_panels = []
      with open("AMIGOS/website/database/panouri.json", "r") as pan_file:
            my_dict = json.load(pan_file)

      for pan in my_dict.values():
            all_panels.append(Panels(pan["name"], pan["type"], pan["power"], pan["length"], pan["width"], pan["price"], pan["picture"], pan["link"]))
      
      return all_panels

      