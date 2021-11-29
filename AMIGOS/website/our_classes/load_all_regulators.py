# Despina Cojocaru
import json


class Load_All_Regulators:
    def load_region_dict(self, address: str):
        try:
            data = json.load(address)
            return data
        except FileReadError as e:
            raise e
        except FileNotFoundError as e:
            raise e
