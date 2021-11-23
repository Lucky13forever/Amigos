# Instructions

# User.create_new_user() appends a new user in the database

# User.check_if_in_database() return False if not found, returns user_id if it founds the user

# User.change_attr() can change attr to a specific user by taking a dict with the attr that u want to change

# User.delete_database() deletes all the users

# USer.delete_user() deletes the user with a specific id

# User.get_table_user() returns a dict with all the users

import json

class User_json():
    def __init__(self, name, email, password, county, city, phone, avg_consumption, surface) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.county = county
        self.city = city
        self.phone = phone
        self.avg_consumption = avg_consumption #measured in kW
        self.surface = surface # measured in m^2

    def unique_name(current: dict, name):
            for key, user in current.items():
                if key == "0":
                    continue
                if user["name"] == name:
                    return False
            
            return True

    def unique_email(current: dict, email):
            for key, user in current.items():
                if key == "0":
                    continue
                if user["email"] == email:
                    return False
            
            return True

    def good_password(current, password):
            return len(password) >= 4

    def good_phone(current, phone):
        return len(phone) == 10


    def create_new_user(name, email, password, county, city, phone, avg_consumption, surface):
        new_user = User(name, email, password, county, city, phone, avg_consumption, surface)
        
        

        # append the new_user
        with open(r"AMIGOS/website/database/tabel_users.json", 'r') as file:
            current = json.load(file)


            # name should be unique
            if User.unique_name(current, name) == False:
                return 'Your username is taken'

            # email shoulb be unique
            if User.unique_email(current, email) == False:
                return 'There is already a user registered with this email'

            # password should have atleast a length of 4
            if User.good_password(current, password) == False:
                return 'Password should have atleast a length of 4'


            # wrong county


            # wrong city

            # phone should have 10 digits
            if User.good_phone(current, phone) == False:
                return 'Phone number should have 10 digits'

            k = current['0']

            current[f'{k+1}'] = {
                'name' : name,
                'email' : email,
                'password' : password,
                'county' : county,
                'city' : city,
                'phone' : phone,
                'avg_consumption' : avg_consumption,
                'surface' : surface
            }

            current['0'] += 1

            with open(r"AMIGOS/website/database/tabel_users.json", 'w') as file:
                json.dump(current, file, indent=4)

        return 'User has been added succesfully'


    def check_if_in_database(email_or_username, password):
        with open(r"AMIGOS/website/database/tabel_users.json", 'r') as file:
            current = json.load(file)

            for user_id, user_data in current.items():
                if type(user_data) == dict:
                    if email_or_username == user_data['name'] or email_or_username == user_data['email']:
                        if password == user_data['password']:
                            return user_id

        return False

    check_if_in_database.__doc__ = "Returns the id for an user, after checking the username and password"
    
    
    
    
    # change indent from None to 4 to pretty print
    def change_attr(user_id, my_dict):
        with open(r"AMIGOS/website/database/tabel_users.json", 'r') as file:
            current = json.load(file)

            for key, value in my_dict.items():
                current[user_id][key] = value

            with open(r"AMIGOS/website/database/tabel_users.json", 'w') as file:
                json.dump(current, file, indent=4)

    change_attr.__doc__ = "Attributes of a user are 'name', 'email', 'password', 'county', 'city', 'phone', 'avg_consumption', 'surface'"

    def delete_user(user_id):
        with open(r"AMIGOS/website/database/tabel_users.json", 'r') as file:
            current = json.load(file)

            del current[user_id]

            with open(r"AMIGOS/website/database/tabel_users.json", 'w') as file:
                json.dump(current, file, indent=4)

    def delete_database():
        with open(r"AMIGOS/website/database/tabel_users.json", 'r') as file:
            current = {
                "0" : 0,
            }

            with open(r"AMIGOS/website/database/tabel_users.json", 'w') as file:
                json.dump(current, file, indent=4)



    def get_table_user():
        rez = {}
        with open(r"AMIGOS/website/database/tabel_users.json", 'r') as file:
            rez = json.load(file)
            
        return rez

    get_table_user.__doc__ = 'Returns the user table'


    def pretty_print():
        with open(r"AMIGOS/website/database/tabel_users.json", 'r') as file:
            rez = json.load(file)

            with open(r"AMIGOS/website/database/tabel_users.json", 'w') as file:
                json.dump(rez, file, indent=4)

