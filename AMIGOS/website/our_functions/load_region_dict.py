# Despina Cojocaru
import json
def load_region_dict(self, address: str):
    try:
        file = open(address)
        data = json.load(file)
        return data
    except FileExistsError:
        raise "FileReadError"
    except FileNotFoundError:
        raise "FileNotFound"
