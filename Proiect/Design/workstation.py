from Implementare.user_functions import User

# User.delete_database()
rez = User.create_new_user('Razvan_05', 'razvan@gmail.com', '1234', 'Timis', 'Timisoara', '1234567890', 400, 50)

print(rez)

unu = User.create_new_user('Razvan_06', 'razvan12@gmail.com', '1234', 'Timis', 'Timisoara', '123450', 400, 50)
print(unu)
# rez = User.get_table_user()
# print(rez['1'])

# User.change_attr('1', {'name' : 'Razvan_05'})
# table_user = get_table_user()
# print(User.create_new_user('Emanuel', 'emanuel@gamil.com', '1234', 'Timis', 'Timisoara', '0724037007', 300, 2))

# table_user = User.get_table_user()
# print(table_user)
# # table_user = get_table_user()
# # print(table_user)

# User.change_attr('1', {
#     'name' : 'Emanuel_1',
#     'email' : 'emanuel_1@gmail.com',
#     'password' : '1234_parola_1',
#     'county' : 'Arad',
#     'city' : 'Arad',
#     'phone' : '1234567890',
#     'avg_consumption' : 400,
#     'surface' : 20,

# })
from Proiect import Implementare

rez = User.delete_database()

