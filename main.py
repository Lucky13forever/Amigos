from Implementare.user_functions import User

# User.create_new_user('Emanuel', 'emanuel@gmail.com', '1234', 'Timis', 'Timisoara', '0724037007', 300, 20)

rez = User.create_new_user('Emanuel', 'emanuel@gmail.com', '1234', 'Timis', 'Timisoara', '0724037007', 300, 20)

print(rez)

rez = User.get_table_user()

print(rez)