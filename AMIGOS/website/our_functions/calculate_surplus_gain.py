#Puscasu Vlad si Birla Alexandru
def calculate_surplus_gain(price_per_kW :float, user_consumption :list, energy_production :list):
    l=[]
    for i in range(len(user_consumption)):
        if user_consumption[i]>energy_production[i]:
            l.append(0)
        else:
            val=(energy_production[i]-user_consumption[i]) * price_per_kW
            l.append(val)
    return l