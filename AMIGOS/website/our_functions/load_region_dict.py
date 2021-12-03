# Despina Cojocaru
import json
def load_region_dict():
    try:
        with open('AMIGOS/website/database/regiuni.json', 'r') as file:
            data = json.load(file)
            return data
    except FileExistsError:
        raise "FileReadError"
    except FileNotFoundError:
        raise "FileNotFound"
