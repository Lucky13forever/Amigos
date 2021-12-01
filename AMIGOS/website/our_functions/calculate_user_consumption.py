montly_consumption = [9.3, 8.7, 9, 8.5, 7.6, 7.8, 8.4, 7.5, 8, 8.2, 8.7]
def calculate_user_consumption(monthly_consumption: list, annual_consumption: int): #definesc functia
    list=[] #creez o noua lista care va contine consumul lunar
    for i in range(len(monthly_consumption)): #parcurg lista
        list.append(montly_consumption[i]/100*annual_consumption) #adaug in lista consumul calculat
    return list #returnez lista creata

#test
#n=int(input())
#print(calculate_user_consumption(montly_consumption,n))