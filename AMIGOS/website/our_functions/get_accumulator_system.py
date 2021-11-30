#Vlad Neagoe, Birla Alexandru si Puscasu Vlad
import sys
def get_accumulator_system(all_accumulators:list,required_capacity:int):
    
    d={}
    for i in range(len(all_accumulators)):
        sum=0 # capacitatea totala a unui tip de acumulator
        k=0 #numarul de acumulatori
        while sum<required_capacity:
            sum+=all_accumulators[i].capacity
            k+=1 
        pret = k*all_accumulators[i].price      
        d[i]=[all_accumulators[i].name, sum,k,pret]
    pret_min=sys.maxsize
    #cautam cea mai eficienta optiune
    for keys,value in d.items():
        if value[3]<pret_min: 
            pret_min=value[3]
            ind=key
    return (all_accumulators[ind], d[ind][2],d[ind][3])    