import json

with open('orase.json', 'r') as file:
    my_dict = json.load(file)

    for key, cities in my_dict.items():
        for i in range(len(cities)):
            my_dict[key][i] = my_dict[key][i].capitalize()

    for key in my_dict.keys():
        my_dict[key] = sorted(my_dict[key])

    with open('output.json', 'w') as out:
        json.dump(my_dict, out, indent=4)