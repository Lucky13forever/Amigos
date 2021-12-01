#Birla Alexandru si Puscasu Vlad
def  calculate_surplus_gain(price_per_kW :float, user_consumption :list, energy_production :list):
    l=[]
    for i in range(len(energy_production)):
        if user_consumption[i] > energy_production[i]:
            l.append(0)
        else:
            dif=(energy_production[i]-user_consumption[i]) * price_per_kW
            l.append(dif)
    return l