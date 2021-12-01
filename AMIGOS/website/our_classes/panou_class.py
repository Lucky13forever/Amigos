import json

class Panels:
      
      def __init__(self, name: str, price: int, width: float, length: float, power: int, picture: str, link: str):
            self.name = name
            self.price = price
            self.length = length
            self.width = width
            self.power = power
            self.picture = picture
            self.link = link


def load_all_panels():
      all_panels = []
      with open("AMIGOS/website/database/panouri.json", "r") as pan_file:
            my_dict = json.load(pan_file)

      for pan in my_dict.values():
            all_panels.append(Panels(pan["type"], pan["price"], pan["size"], pan["power"]))
      
      return all_panels

      